#!/usr/bin/env python3
"""Publish verified RealtySkills downloads through GitHub's normal Releases API."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import time
from urllib.error import HTTPError
from urllib.parse import quote
from urllib.request import Request, urlopen
import zipfile

ROOT = Path(__file__).resolve().parents[1]
TAG = 'v1.0.0'
REPOSITORY = 'evyevans/realtyskills'


def verified_assets():
    data = json.loads((ROOT / 'catalog.json').read_text())
    assert data['version'] == '1.0.0'
    expected = {f"{skill['id']}.zip" for skill in data['skills']}
    expected.update({'realtyskills-v1.0.0.zip', 'realtyskills-chat-guides-v1.0.0.zip'})
    checksums = {}
    for line in (ROOT / 'dist/SHA256SUMS.txt').read_text().splitlines():
        digest, name = line.split('  ', 1)
        assert name in expected and name not in checksums
        path = ROOT / 'dist' / name
        assert hashlib.sha256(path.read_bytes()).hexdigest() == digest, name
        with zipfile.ZipFile(path) as archive:
            assert archive.testzip() is None, name
        checksums[name] = digest
    assert set(checksums) == expected and len(expected) == 44
    paths = [ROOT / 'dist' / name for name in sorted(expected)]
    paths.append(ROOT / 'dist/SHA256SUMS.txt')
    return paths


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--verify-only', action='store_true')
    args = parser.parse_args()
    paths = verified_assets()
    if args.verify_only:
        print('Verified 44 ZIPs and SHA256SUMS.txt for release publication.')
        return
    assert os.environ['GITHUB_REPOSITORY'] == REPOSITORY
    token = os.environ['GH_TOKEN']
    commit = os.environ['GITHUB_SHA']
    assert len(commit) == 40 and all(c in '0123456789abcdef' for c in commit)

    def request(url, method='GET', payload=None, content_type='application/json'):
        if not url.startswith(('https://api.github.com/', 'https://uploads.github.com/')):
            raise ValueError('Unexpected GitHub API host')
        raw = json.dumps(payload).encode() if isinstance(payload, dict) else payload
        headers = {'Authorization': f'Bearer {token}', 'Accept': 'application/vnd.github+json',
                   'X-GitHub-Api-Version': '2022-11-28', 'User-Agent': 'RealtySkills-release'}
        if raw is not None:
            headers['Content-Type'] = content_type
        try:
            with urlopen(Request(url, data=raw, headers=headers, method=method), timeout=120) as response:
                body = response.read()
        except HTTPError as error:
            # Stop after the first failed request, including account and rate restrictions.
            detail = error.read().decode(errors='replace')
            error.close()
            raise SystemExit(f'GitHub request failed ({error.code}): {detail}') from error
        if method != 'GET':
            time.sleep(1)
        return json.loads(body) if body else None

    base = f'https://api.github.com/repos/{REPOSITORY}'
    releases = []
    page = 1
    while True:
        batch = request(f'{base}/releases?per_page=100&page={page}')
        releases.extend(batch)
        if len(batch) < 100:
            break
        page += 1
    matches = [release for release in releases if release['tag_name'] == TAG]
    assert len(matches) <= 1
    title = 'RealtySkills v1.0.0 — 42 Real Estate AI Workflows by Evykynn'
    notes = (ROOT / 'docs/release-notes-v1.0.0.md').read_text()
    notes += f'\nPublished from verified source commit `{commit}`. Release checks passed in GitHub Actions.\n'
    if matches:
        release = matches[0]
    else:
        release = request(f'{base}/releases', 'POST',
                          {'tag_name': TAG, 'target_commitish': commit, 'name': title,
                           'body': notes, 'draft': True, 'prerelease': False})
    assets = []
    page = 1
    while True:
        batch = request(f"{base}/releases/{release['id']}/assets?per_page=100&page={page}")
        assets.extend(batch)
        if len(batch) < 100:
            break
        page += 1
    by_name = {asset['name']: asset for asset in assets}
    assert len(by_name) == len(assets), 'Duplicate release asset names'
    upload_url = release['upload_url'].split('{', 1)[0]
    for path in paths:
        content = path.read_bytes()
        digest = 'sha256:' + hashlib.sha256(content).hexdigest()
        old = by_name.get(path.name)
        if old and old.get('digest') == digest and old['size'] == len(content):
            print('Already current:', path.name)
            continue
        if old:
            if release['draft']:
                raise SystemExit(f'Existing draft asset requires inspection before replacement: {path.name}')
            # Preserve and inspect the old public bytes before replacing a matching named asset.
            with urlopen(old['browser_download_url'], timeout=120) as response:
                backup = response.read()
            assert len(backup) == old['size'], 'Existing asset download incomplete'
            backup_dir = ROOT / 'release-backups'
            backup_dir.mkdir(exist_ok=True)
            (backup_dir / path.name).write_bytes(backup)
            if hashlib.sha256(backup).hexdigest() == hashlib.sha256(content).hexdigest():
                print('Already current:', path.name)
                continue
            request(f"{base}/releases/assets/{old['id']}", 'DELETE')
        uploaded = request(upload_url + '?name=' + quote(path.name), 'POST', content,
                           'application/zip' if path.suffix == '.zip' else 'text/plain')
        assert uploaded['state'] == 'uploaded' and uploaded['size'] == len(content), path.name
        if uploaded.get('digest'):
            assert uploaded['digest'] == digest, path.name
        print('Uploaded:', path.name)
    final = request(f"{base}/releases/{release['id']}/assets?per_page=100")
    assert {path.name for path in paths} <= {asset['name'] for asset in final}
    published = request(f"{base}/releases/{release['id']}", 'PATCH',
                        {'name': title, 'body': notes, 'draft': False, 'prerelease': False,
                         'make_latest': 'true'})
    final_by_name = {asset['name']: asset for asset in final}
    for path in paths:
        with urlopen(final_by_name[path.name]['browser_download_url'], timeout=120) as response:
            public_bytes = response.read()
        assert hashlib.sha256(public_bytes).digest() == hashlib.sha256(path.read_bytes()).digest(), path.name
    print('Published and anonymously verified all 45 downloads:', published['html_url'])


if __name__ == '__main__':
    main()
