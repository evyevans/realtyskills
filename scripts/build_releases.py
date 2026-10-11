#!/usr/bin/env python3
"""Build and verify self-contained skill ZIPs, chat guides, and the public library."""
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
import zipfile

from validate_library import ROOT, public_files


def write_zip(path, members):
    # Fixed timestamps make rebuilds byte-for-byte reproducible.
    with zipfile.ZipFile(path, 'w', compression=zipfile.ZIP_DEFLATED) as archive:
        for name, content in sorted(members.items()):
            info = zipfile.ZipInfo(name, (2026, 10, 5, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, content)
    with zipfile.ZipFile(path) as archive:
        assert archive.testzip() is None, f'Corrupt ZIP: {path.name}'
        assert set(archive.namelist()) == set(members), f'Member mismatch: {path.name}'
        for name, content in members.items():
            assert archive.read(name) == content, f'Content mismatch: {path.name}/{name}'


def write_navigation(destination, skills, guides):
    """Expose the same complete guides outside the bundle and create macOS shortcuts."""
    guide_dir = destination / 'standalone-guides'
    finder_dir = destination / 'finder'
    guide_dir.mkdir(exist_ok=True)
    finder_dir.mkdir(exist_ok=True)
    rows = ['# All RealtySkills uploads', '',
            'All 42 active skills, including the earlier revisions. Upload the individual ZIP '
            'to Agensi or a supported skill installer. For ordinary LLM chat, attach the complete '
            'Markdown guide. Detailed guides include their playbook.', '',
            'On macOS, open a Finder shortcut in Terminal to select that ZIP in Finder. '
            'The shortcuts only reveal files; they do not upload or publish anything.', '',
            f'[Reveal every skill ZIP in Finder]({destination / "reveal-all-skills.command"})', '',
            '| Skill | Version | Individual ZIP | Complete chat guide | Finder |',
            '|---|---|---|---|---|']
    manifest = []
    for skill in sorted(skills, key=lambda item: item['id']):
        slug = skill['id']
        content = guides[f'realtyskills-chat-guides/{slug}.md']
        guide = guide_dir / f'{slug}.md'
        guide.write_bytes(content)
        package = destination / f'{slug}.zip'
        shortcut = finder_dir / f'{slug}.command'
        shortcut.write_text('#!/bin/zsh\n'
                            'task_dist_dir="${0:A:h:h}"\n'
                            f'/usr/bin/open -R "$task_dist_dir/{slug}.zip"\n')
        shortcut.chmod(0o755)
        match = re.search(rb'^  version: (.+)$', content, re.M)
        skill_version = match.group(1).decode().strip("'\"") if match else 'unknown'
        rows.append(f'| {skill["title"]} | {skill_version} | '
                    f'[{slug}.zip]({package}) | [Markdown]({guide}) | [Reveal]({shortcut}) |')
        manifest.append({'id': slug, 'version': skill_version,
                         'zip': package.name, 'guide': str(guide.relative_to(destination)),
                         'finder': str(shortcut.relative_to(destination)),
                         'zip_sha256': hashlib.sha256(package.read_bytes()).hexdigest(),
                         'guide_sha256': hashlib.sha256(content).hexdigest()})
    all_shortcut = destination / 'reveal-all-skills.command'
    targets = ' '.join(f'"$task_dist_dir/{skill["id"]}.zip"' for skill in skills)
    all_shortcut.write_text('#!/bin/zsh\ntask_dist_dir="${0:A:h}"\n'
                            f'/usr/bin/open -R {targets}\n')
    all_shortcut.chmod(0o755)
    (destination / 'SKILL-UPLOAD-INDEX.md').write_text('\n'.join(rows) + '\n')
    (destination / 'skill-upload-manifest.json').write_text(json.dumps(
        {'skills': manifest}, indent=2) + '\n')
    print(f'Created {len(manifest)} standalone guides and Finder shortcuts, plus SKILL-UPLOAD-INDEX.md.')


def main():
    subprocess.run([sys.executable, str(ROOT / 'scripts/render_catalog.py'), '--check'], check=True)
    subprocess.run([sys.executable, str(ROOT / 'scripts/validate_library.py')], check=True)
    data = json.loads((ROOT / 'catalog.json').read_text())
    version = data['version']
    if not re.fullmatch(r'\d+\.\d+\.\d+', version):
        raise SystemExit('Invalid release version')
    destination = ROOT / 'dist'
    destination.mkdir(exist_ok=True)
    license_bytes = (ROOT / 'LICENSE').read_bytes()
    guides = {'realtyskills-chat-guides/LICENSE': license_bytes,
              'realtyskills-chat-guides/README.md': (
                  '# RealtySkills chat guides\n\nChoose one Markdown guide and attach it to your AI chat. '
                  'Each guide contains the complete entry and playbook, where applicable. '
                  'Provide verified facts and ask for missing inputs before drafting. '
                  'Use the catalog in the full library for jurisdiction and tool requirements.\n'
              ).encode()}
    outputs = []
    for skill in data['skills']:
        entry = ROOT / skill['path']
        folder = entry.parent
        members = {f'{skill["id"]}/{path.relative_to(folder)}': path.read_bytes()
                   for path in folder.rglob('*') if path.is_file() and not path.name.startswith('.')}
        members[f'{skill["id"]}/LICENSE'] = license_bytes
        output = destination / f'{skill["id"]}.zip'
        write_zip(output, members)
        outputs.append(output)
        content = entry.read_text()
        playbook = folder / 'references/playbook.md'
        if playbook.exists():
            content = content.replace('[the detailed playbook](references/playbook.md)',
                                      'the detailed playbook included later in this file')
            content += '\n---\n\n' + playbook.read_text()
        guides[f'realtyskills-chat-guides/{skill["id"]}.md'] = content.encode()
    chat_zip = destination / f'realtyskills-chat-guides-v{version}.zip'
    write_zip(chat_zip, guides)
    outputs.append(chat_zip)
    library_zip = destination / f'realtyskills-v{version}.zip'
    members = {f'realtyskills/{path.relative_to(ROOT)}': path.read_bytes() for path in public_files()}
    write_zip(library_zip, members)
    outputs.append(library_zip)
    checksums = '\n'.join(f'{hashlib.sha256(path.read_bytes()).hexdigest()}  {path.name}'
                          for path in sorted(outputs)) + '\n'
    (destination / 'SHA256SUMS.txt').write_text(checksums)
    write_navigation(destination, data['skills'], guides)
    print(f'Built and verified {len(outputs)} ZIPs: {len(data["skills"])} individual skills, '
          'one chat-guide bundle, one full library, plus SHA256SUMS.txt.')
    print(f'Total ZIP size: {sum(path.stat().st_size for path in outputs):,} bytes. Output: {destination}')


if __name__ == '__main__':
    main()
