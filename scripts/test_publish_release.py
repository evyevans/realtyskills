#!/usr/bin/env python3
"""Regression checks for versioned publication without live GitHub writes."""
import contextlib
import hashlib
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
from urllib.error import HTTPError

import publish_release as publisher


class Response(io.BytesIO):
    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()


class PublicationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.asset = Path(self.temp.name) / 'example.zip'
        self.asset.write_bytes(b'expected verified bytes')
        self.release = {'id': 7, 'tag_name': publisher.TAG, 'draft': False,
                        'upload_url': 'https://uploads.github.com/repos/test/assets{?name}',
                        'html_url': 'https://github.com/evyevans/realtyskills/releases/tag/' + publisher.TAG}
        self.asset_record = {'id': 8, 'name': self.asset.name, 'size': self.asset.stat().st_size,
                             'digest': 'sha256:' + hashlib.sha256(self.asset.read_bytes()).hexdigest(),
                             'browser_download_url': 'https://github.com/test/download/example.zip'}
        self.calls = []

    def run_publisher(self, responder):
        def open_request(request, **kwargs):
            url = request if isinstance(request, str) else request.full_url
            method = 'GET' if isinstance(request, str) else request.get_method()
            self.calls.append((method, url))
            return Response(responder(method, url, request))
        with patch.object(publisher, 'verified_assets', return_value=[self.asset]), \
             patch.object(publisher, 'urlopen', side_effect=open_request), \
             patch.object(publisher.time, 'sleep'), \
             patch.dict(publisher.os.environ, {'GH_TOKEN': 'test-only',
                        'GITHUB_SHA': 'a' * 40, 'GITHUB_REPOSITORY': publisher.REPOSITORY}), \
             patch('sys.argv', ['publish_release.py']), contextlib.redirect_stdout(io.StringIO()):
            publisher.main()

    def existing(self, public_bytes):
        def respond(method, url, request):
            self.assertEqual(method, 'GET', 'A published version must never be modified')
            if '/assets?' in url:
                return json.dumps([self.asset_record]).encode()
            if '/releases?' in url:
                return json.dumps([self.release]).encode()
            return public_bytes
        return respond

    def test_matching_published_release_is_verified_without_writes(self):
        self.run_publisher(self.existing(self.asset.read_bytes()))
        self.assertEqual(len(self.calls), 3)

    def test_changed_published_release_requires_new_version_without_writes(self):
        with self.assertRaisesRegex(SystemExit, 'Bump catalog.json version'):
            self.run_publisher(self.existing(b'older download'))
        self.assertTrue(all(method == 'GET' for method, _ in self.calls))

    def test_new_release_uses_catalog_tag_and_verifies_download(self):
        draft = dict(self.release, draft=True)
        uploaded = dict(self.asset_record, state='uploaded')
        def respond(method, url, request):
            if method == 'POST' and url.endswith('/releases'):
                body = json.loads(request.data)
                self.assertEqual(body['tag_name'], 'v' + publisher.DATA['version'])
                self.assertEqual(body['target_commitish'], 'a' * 40)
                self.assertTrue(body['draft'])
                return json.dumps(draft).encode()
            if method == 'POST':
                self.assertEqual(request.data, self.asset.read_bytes())
                return json.dumps(uploaded).encode()
            if method == 'PATCH':
                self.assertFalse(json.loads(request.data)['draft'])
                return json.dumps(self.release).encode()
            if '/assets?' in url:
                already_uploaded = any(m == 'POST' and 'uploads.github.com' in u for m, u in self.calls)
                return json.dumps([uploaded] if already_uploaded else []).encode()
            if '/releases?' in url:
                return b'[]'
            return self.asset.read_bytes()
        self.run_publisher(respond)
        self.assertEqual([method for method, _ in self.calls].count('POST'), 2)
        self.assertEqual([method for method, _ in self.calls].count('PATCH'), 1)

    def test_permission_error_stops_after_first_request(self):
        def denied(*args):
            raise HTTPError('https://api.github.com/', 403, 'Forbidden', {}, io.BytesIO(b'permission denied'))
        with self.assertRaisesRegex(SystemExit, 'GitHub request failed \\(403\\)'):
            self.run_publisher(denied)
        self.assertEqual(len(self.calls), 1)

    def test_bad_checksum_is_rejected_before_network(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / 'dist').mkdir()
            (root / 'catalog.json').write_text(json.dumps({'skills': [{'id': 'example'}]}))
            (root / 'dist/example.zip').write_bytes(b'corrupt bytes')
            (root / 'dist/SHA256SUMS.txt').write_text('0' * 64 + '  example.zip\n')
            with patch.object(publisher, 'ROOT', root), patch.object(publisher, 'urlopen') as network:
                with self.assertRaises(AssertionError):
                    publisher.verified_assets()
                network.assert_not_called()


if __name__ == '__main__':
    unittest.main()
