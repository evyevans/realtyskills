# Local verification record

Prepared October 5, 2026. Publication has not been completed in this session.

## Completed checks

- 42 active workflows and seven archived files accounted for against all 49 original source files.
- Nine category counts, catalog entries, related workflow identifiers, and original source hashes checked.
- All 42 packages passed the bundled local Codex skill-creator validator.
- Valid YAML metadata, internal Markdown links and heading links, detailed references, updated attribution, and recognizable credential patterns checked.
- GitHub workflow triggers, read-only token permissions, issue templates, and Python script syntax checked locally.
- 44 ZIPs built with byte comparisons and archive-integrity checks, plus matching SHA-256 checksums. Private local history, credentials, Git internals, and caches excluded.
- Rental example arithmetic independently recomputed: monthly payment USD 1,348.99; annual debt service USD 16,187.86; after-reserve annual cash flow USD 2,232.14.

## Checks limited by this session

- GitHub CLI could not connect to `api.github.com`. An authentication-status error therefore does not establish the account's standing or the validity of the stored credential.
- Project Git initialization was denied by the filesystem policy; no local commit or remote push was made.
- A local Codex discovery check was attempted in an isolated temporary project, but app-server startup was denied by the filesystem policy before it returned a skill list. Actual skill discovery remains unverified here.
- Claude upload, live LLM execution, GitHub Actions execution, public repository availability, and logged-out downloads have not been tested.

Installation instructions were checked against the linked official documentation; structural validation is not a substitute for live behavior verification. Worked examples are hand-authored demonstrations. Professional accuracy and jurisdiction-specific requirements need current evidence and appropriate review.

## Reproduce structural checks

```bash
python scripts/render_catalog.py --check
python scripts/validate_library.py
python scripts/build_releases.py
```

Use the development environment in [installation](installation.md). Follow [maintainer publishing](maintainer-publishing.md) once account status and authentication are confirmed, then update this record with actual external results.
