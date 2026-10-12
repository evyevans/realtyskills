# Verification record

Source publication, local package checks, and release downloads are separate milestones.

## Current status — October 11, 2026

- **Successful source push:** GitHub `main` advanced from `2df750f` to `a12c7f4` for the full-library skill revision. The local checkout records this commit; this session has not independently retrieved the live branch.
- **Prepared next release:** catalog version `1.0.1`; 42 active skills, 12 Starters, 30 Detailed workflows, and nine categories. Seven legacy copies are removed from current source and packages. All 49 original source mappings retain hashes; retired records point to Git history at `a12c7f4`.
- **Release status:** v1.0.1 publication and public download checksums are pending verification. A source push alone does not confirm the README Download link serves updated packages.
- **Local verification:** reproduce the checks below. The builder checks all 44 ZIPs for integrity and source-byte equality and generates SHA-256 checksums. The publisher checks the 45 expected release assets before any API write.
- **Marketplace status:** Agensi uploads are separate and remain manual.

## Publication history

The October 6 initial publishing attempt failed at its first write request with GitHub HTTP 403, `Resource not accessible by integration`. That attempt created no remote commit or release.

A later successful publication advanced `main` from `722af2d` to `2df750f`. The original v1.0.0 release was confirmed with 45 anonymously verified assets after a release-job retry. These are historical results for v1.0.0, not verification of v1.0.1.

On October 11 the subsequent source revision was pushed as `a12c7f4`. Revised downloads still require a new successful release job.

## Release verification criteria

The **Publish verified release** workflow builds current source, checks the inventory, publishes the catalog version as a new release, and anonymously downloads and checksums every asset. An existing published version cannot be overwritten with different bytes; bump the catalog version and add matching release notes for another revision. Confirm both the Actions result and the latest release before reporting download publication complete.

## Limits

This session's shell cannot resolve GitHub hosts and its GitHub CLI sign-in reports an invalid token. This is an access limit for this session, not evidence that the earlier successful push failed.

Live Claude/Codex discovery and model execution have not been tested. Worked examples are illustrative. Structural checks do not establish professional accuracy, model reliability, or jurisdiction-specific compliance.

## Reproduce

```bash
python3 -m pip install -r requirements-dev.txt
python3 scripts/render_catalog.py --check
python3 scripts/validate_library.py
python3 scripts/build_releases.py
python3 scripts/publish_release.py --verify-only
```
