#!/usr/bin/env python3
"""Validate public skill packages, source accounting, metadata, and local links."""
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote

import yaml

ROOT = Path(__file__).resolve().parents[1]
PUBLIC_FILES = ['README.md', 'LICENSE', 'CONTRIBUTING.md', 'CHANGELOG.md',
                'catalog.json', 'requirements-dev.txt', '.gitignore']
PUBLIC_DIRS = ['skills', 'docs', 'examples', 'archive', 'assets', 'scripts', '.github']


def public_files():
    files = [ROOT / name for name in PUBLIC_FILES if (ROOT / name).is_file()]
    for directory in PUBLIC_DIRS:
        files.extend(path for path in (ROOT / directory).rglob('*')
                     if path.is_file() and not any(part.startswith('.') or part == '__pycache__'
                                                for part in path.relative_to(ROOT / directory).parts)
                     and path.suffix != '.pyc')
    return sorted(set(files))


def without_code(text):
    return re.sub(r'^(`{3,}|~{3,}).*?^\1[^\n]*$', '', text, flags=re.M | re.S)


def main():
    data = json.loads((ROOT / 'catalog.json').read_text())
    errors = []
    skills = data['skills']
    identifiers = [skill['id'] for skill in skills]
    if len(identifiers) != len(set(identifiers)):
        errors.append('Skill identifiers must be unique')
    actual = {str(path.relative_to(ROOT)) for path in (ROOT / 'skills').rglob('SKILL.md')}
    expected = {skill['path'] for skill in skills}
    if actual != expected:
        errors.append(f'Catalog/package mismatch: {actual ^ expected}')
    for skill in skills:
        entry = ROOT / skill['path']
        if not entry.is_file():
            errors.append(f'Missing entry: {entry}')
            continue
        if entry.parent.name != skill['id']:
            errors.append(f"Folder and identifier mismatch: {skill['id']}")
        try:
            text = entry.read_text()
            parts = re.split(r'^---\s*$', text, maxsplit=2, flags=re.M)
            if len(parts) != 3 or parts[0].strip():
                raise ValueError('Missing YAML frontmatter')
            metadata = yaml.safe_load(parts[1])
            if metadata.get('name') != skill['id']:
                raise ValueError('name does not match identifier')
            if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', skill['id']) or len(skill['id']) >= 64:
                raise ValueError('Invalid skill identifier')
            description = metadata.get('description', '')
            if not isinstance(description, str) or not 1 <= len(description) <= 1024:
                raise ValueError('Invalid description length or type')
            if '<' in description or '>' in description:
                raise ValueError('Description contains markup')
            if metadata.get('license') != 'MIT':
                raise ValueError('Missing MIT license metadata')
            info = metadata.get('metadata', {})
            for key in ['author', 'version', 'category', 'level', 'jurisdiction']:
                if not info.get(key):
                    raise ValueError(f'Missing metadata.{key}')
            if info['category'] != skill['category'] or info['level'] != skill['level'].lower():
                raise ValueError('Catalog and entry metadata disagree')
            if skill['category'] not in data['categories'] or skill['level'] not in ['Starter', 'Detailed']:
                raise ValueError('Unknown category or level')
            if skill.get('related') and skill['related'] not in identifiers:
                raise ValueError('Unknown related skill')
            if skill['level'] == 'Detailed' and not (entry.parent / 'references/playbook.md').is_file():
                raise ValueError('Missing detailed playbook')
            # Installable packages must not depend on another directory in the repository.
            for target in re.findall(r'\[[^\]]*\]\(([^\s)]+)', without_code(parts[2])):
                if not re.match(r'^(?:[a-z]+:|#)', target):
                    resolved = (entry.parent / unquote(target.split('#')[0])).resolve()
                    if not resolved.is_relative_to(entry.parent.resolve()):
                        raise ValueError(f'Package depends on an external local file: {target}')
        except (yaml.YAMLError, ValueError, TypeError, AttributeError) as error:
            errors.append(f'{skill["path"]}: {error}')
    originals = [skill for skill in skills if 'source' in skill] + data['archive']
    if len(originals) != 49 or len({item['source'] for item in originals}) != 49:
        errors.append('Original source accounting must include exactly 49 distinct files')
    for item in originals:
        if not re.fullmatch(r'[a-f0-9]{64}', item.get('source_sha256', '')):
            errors.append(f'Invalid original source hash: {item["source"]}')
    for item in data['archive']:
        if not (ROOT / item['path']).is_file():
            errors.append(f'Missing archived file: {item["path"]}')
    actual_archive = {str(path.relative_to(ROOT)) for path in (ROOT / 'archive/legacy-skills').glob('*.md')}
    if actual_archive != {item['path'] for item in data['archive']}:
        errors.append('Archived file inventory mismatch')

    secret_patterns = [r'gh[pousr]_[A-Za-z0-9]{30,}', r'github_pat_[A-Za-z0-9_]{40,}',
                       r'sk-(?:proj-)?[A-Za-z0-9_-]{32,}',
                       r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----',
                       r'AKIA[0-9A-Z]{16}']
    for path in public_files():
        if path.suffix not in ['.md', '.json', '.py', '.yml', '.yaml', '.txt', '.svg']:
            continue
        text = path.read_text()
        if any(re.search(pattern, text) for pattern in secret_patterns):
            errors.append(f'Possible credential in {path.relative_to(ROOT)}; inspect locally')
        if path.suffix == '.md':
            if 'omerion.io' in text.lower() or 'Claude Opus 4.7' in text:
                errors.append(f'Obsolete attribution or model claim: {path.relative_to(ROOT)}')
            content = without_code(text)
            targets = re.findall(r'\[[^\]]*\]\(([^\s)]+)', content)
            targets.extend(re.findall(r'(?:src|href)="([^"]+)"', content))
            for target in targets:
                if re.match(r'^(?:[a-z]+:|#|//)', target, re.I):
                    continue
                relative, _, anchor = unquote(target.strip('<>')).partition('#')
                resolved = (path.parent / relative).resolve() if relative else path
                if not resolved.is_relative_to(ROOT.resolve()) or not resolved.exists():
                    errors.append(f'Broken local link in {path.relative_to(ROOT)}: {target}')
                elif anchor and resolved.suffix == '.md':
                    headings = re.findall(r'^#{1,6}\s+(.+)$', without_code(resolved.read_text()), re.M)
                    anchors = {re.sub(r'[^\w\- ]', '', heading.lower()).replace(' ', '-') for heading in headings}
                    if anchor not in anchors:
                        errors.append(f'Broken heading link in {path.relative_to(ROOT)}: {target}')
    if errors:
        print('\n'.join(errors), file=sys.stderr)
        raise SystemExit(1)
    print(f'Validated {len(skills)} active skills, {len(data["archive"])} archived files, '
          f'{len(data["categories"])} categories, 49 original mappings, metadata, local links, and credential patterns.')


if __name__ == '__main__':
    main()
