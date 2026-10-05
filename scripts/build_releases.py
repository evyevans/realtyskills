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
    print(f'Built and verified {len(outputs)} ZIPs: {len(data["skills"])} individual skills, '
          'one chat-guide bundle, one full library, plus SHA256SUMS.txt.')
    print(f'Total ZIP size: {sum(path.stat().st_size for path in outputs):,} bytes. Output: {destination}')


if __name__ == '__main__':
    main()
