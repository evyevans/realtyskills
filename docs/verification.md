# Verification record

Launch checks prepared October 6, 2026. Local checks and live publication are recorded separately.

## Local checks

- 42 active workflows, 12 starters, 30 detailed playbooks, nine categories, and seven archived files account for all 49 source mappings.
- Catalog freshness, YAML metadata, local Markdown links and anchors, package references, and recognizable credential patterns pass.
- All 44 ZIPs are built with fixed timestamps, checked for integrity, and compared against intended source bytes. SHA-256 checksums cover every ZIP.
- Release publication separately validates the complete expected asset inventory.
- Source staging excludes private history, credentials, caches, agent settings, generated downloads, and upload helpers.
- Gold logo bytes and placement are unchanged. SVGs change only name text; PNG pixel changes are confined to that area. The social PNG is 1280 × 640 and under 1 MB.
- Rental example arithmetic was previously recomputed: monthly payment USD 1,348.99; annual debt service USD 16,187.86; after-reserve annual cash flow USD 2,232.14.

## Live repository inspection

The GitHub plugin confirms the public repository is owned by `evyevans`, the connected account has write/admin permissions, and `main` is its default branch.

The pre-launch inspection found all 42 workflows correctly located, 104 matching prepared public files, six differing files, and eight missing files. No duplicate category or enclosing upload folders existed. The upload included release downloads and a Python cache file, and omitted `.github/` and `.gitignore`.

The isolated checkout preserves all three original commits. Git commit, tree, and blob hashes were verified, and Git object integrity checks passed. Updates preserve existing history.

At preparation time no release or Actions run existed. The release workflow must succeed before publication is called complete. Its publishing step anonymously downloads and checksums all 45 assets after publication.

The October 6 publishing attempt stopped at its first write request with GitHub HTTP 403, `Resource not accessible by integration`. No remote source commit or release was created. The connection lists no installed GitHub app/account. A prepared local commit and rebuilt downloads are available, but live publication remains pending appropriate integration access.

Local release-publisher tests cover new-release publication, preserving current assets on a repeat run, rejecting a corrupt checksum before any request, and stopping after a single permission-denied request.

## Limits

The shell cannot resolve GitHub hosts in this environment; the plugin can read and update source. A browser-rendered logged-out repository check is unavailable because browser startup is restricted. Plugin/API inspection alone is not a visual browser check.

About, topics, and social-preview settings require repository UI access when no settings-capable tool is available.

Live Claude/Codex discovery and model execution have not been tested. Worked examples are illustrative. Structural checks do not establish professional accuracy or jurisdiction-specific compliance.

## Reproduce

```bash
python3 -m pip install -r requirements-dev.txt
python3 scripts/render_catalog.py --check
python3 scripts/validate_library.py
python3 scripts/build_releases.py
python3 scripts/publish_release.py --verify-only
```
