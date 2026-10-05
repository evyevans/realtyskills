#!/usr/bin/env python3
"""Render the public task catalog and source inventory from catalog.json."""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def render(data):
    skills = data['skills']
    categories = data['categories']
    catalog = [
        '# Find a RealtySkills workflow', '',
        f"{len(skills)} active workflows across {len(categories)} categories. "
        'Use your browser’s Find feature to search for a task or audience.', '',
        '**Starter** is a focused workflow. **Detailed** is an extensive playbook. '
        'For chat use, attach the entry and any linked playbook, or use the standalone release guide.', '',
        '[First-use guide](getting-started.md) · [Installation](installation.md) · '
        '[Connected workflows](workflows.md) · [Limitations](quality-and-limitations.md)', '',
    ]
    by_id = {skill['id']: skill for skill in skills}
    for category, label in categories.items():
        group = [skill for skill in skills if skill['category'] == category]
        catalog.extend([f'## {label}', '', f'{len(group)} workflows.', '',
                        '| Skill | Level | Task | For |', '|---|---|---|---|'])
        for skill in sorted(group, key=lambda item: (item['level'] != 'Starter', item['title'])):
            catalog.append(f"| [{skill['title']}](../{skill['path']}) | {skill['level']} | "
                           f"{skill['task']} | {skill['audience']} |")
        catalog.append('')
        for skill in sorted(group, key=lambda item: (item['level'] != 'Starter', item['title'])):
            catalog.extend([f"### {skill['title']}", '',
                            f"[{skill['level']} instructions](../{skill['path']})", '',
                            f"- **Provide:** {skill['inputs']}.",
                            f"- **Receive:** {skill['output']}.",
                            f"- **Jurisdiction:** {skill['jurisdiction']}.",
                            f"- **Tools:** {skill['tools']}."])
            related = by_id.get(skill.get('related'))
            if related:
                catalog.append(f"- **Related workflow:** [{related['title']}](../{related['path']}) "
                               f"({related['level']}).")
            catalog.extend(['', f"> Example request: {skill['trigger']}", ''])
    inventory = ['# Source inventory', '',
                 'The launch collection contained 49 skill files: 30 expanded playbooks, '
                 '12 focused workflows, and seven older overlapping versions. All are accounted for below.', '',
                 'Source hashes identify the original bytes before attribution, metadata, and publication edits. '
                 'The obsolete index and audit were replaced because their counts and folder claims did not '
                 'match the actual collection. They are not skill files.', '',
                 '## Active source mapping', '',
                 '| Original file | Public workflow | Level |', '|---|---|---|']
    for skill in sorted(skills, key=lambda item: item.get('source', item['id'])):
        if 'source' in skill:
            inventory.append(f"| `{skill['source']}` | [{skill['title']}](../{skill['path']}) | {skill['level']} |")
    inventory.extend(['', '## Archived source mapping', '',
                      '| Original file | Archived file |', '|---|---|'])
    for item in data['archive']:
        inventory.append(f"| `{item['source']}` | [{Path(item['path']).name}](../{item['path']}) |")
    inventory.extend(['', 'Machine-readable mappings and original SHA-256 hashes are in '
                      '[catalog.json](../catalog.json). Archive files retain useful historical content '
                      'with updated attribution and illustrative contacts; they are not active installation packages.', ''])
    return {'docs/catalog.md': '\n'.join(catalog), 'docs/inventory.md': '\n'.join(inventory)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Fail if generated documentation is stale')
    args = parser.parse_args()
    documents = render(json.loads((ROOT / 'catalog.json').read_text()))
    stale = []
    for name, content in documents.items():
        target = ROOT / name
        if args.check:
            if not target.exists() or target.read_text() != content:
                stale.append(name)
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(content)
    if stale:
        raise SystemExit('Stale documentation: ' + ', '.join(stale) + '. Run scripts/render_catalog.py.')
    print('Catalog and inventory ' + ('are current.' if args.check else 'generated.'))


if __name__ == '__main__':
    main()
