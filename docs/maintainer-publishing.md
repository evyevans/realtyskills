# Maintaining and publishing RealtySkills

The public library is [evyevans/realtyskills](https://github.com/evyevans/realtyskills), owned by `evyevans`. Public author credits use Evykynn; the MIT copyright notice retains its existing legal attribution.

## Update the existing repository

Clone the existing repository rather than creating a new Git history:

```bash
git clone https://github.com/evyevans/realtyskills.git
cd realtyskills
python3 -m pip install -r requirements-dev.txt
python3 scripts/render_catalog.py --check
python3 scripts/validate_library.py
python3 scripts/build_releases.py
```

Inspect the branch, remote, repository instructions, and existing changes before editing. Preserve remote edits, use ordinary commits, and honor branch protections. Never force-push or bypass secret protection. Stage only public source paths; exclude `dist/`, credentials, caches, local history, and agent settings.

## Release publication

**Library checks** validates source updates. **Publish verified release** validates and builds 44 ZIPs, publishes them and `SHA256SUMS.txt` in Releases, and anonymously downloads and checksums every asset.

The publishing job uses GitHub's repository token with `contents: write`. It needs no personal token stored in source. It runs on `main` when its workflow, publisher script, release notes, or verification record changes. It can also be run through **Actions → Publish verified release → Run workflow**.

The publisher inspects releases, keeps matching assets, and replaces only differing named downloads. Unknown assets remain untouched. Existing public assets are downloaded and inspected before replacement; backup bytes remain in the runner's `release-backups/` directory during the job. An existing draft with differing assets requires manual inspection. Any API error stops publication without retry.

The current publisher is explicitly for `v1.0.0`. For a new version, update the catalog, release notes, publisher version checks, filenames, and workflow concurrency group together.

## Repository presentation

Use the gear beside **About** to set:

> 42 free AI workflows for real estate professionals. Listing copy, lead follow-ups, market research, investment analysis, and more. By Evykynn.

Topics: `real-estate`, `ai-skills`, `agent-skills`, `claude-skills`, `llm`, `property-management`, `prompt-engineering`, `open-source`.

Under **Settings → General → Social preview → Edit → Upload an image**, select `assets/realtyskills-social-preview.png`.

## Account and API errors

Do not send passwords, tokens, or device codes into chat. If authentication fails after connectivity is confirmed, use GitHub CLI's browser login in your own terminal and verify the account is `evyevans`.

Authentication success does not resolve an existing suspension. Stop on restriction or rate-limit responses. GitHub provides an [appeal and reinstatement process](https://docs.github.com/en/site-policy/acceptable-use-policies/github-appeal-and-reinstatement).

Follow GitHub's [API best practices](https://docs.github.com/en/rest/using-the-rest-api/best-practices-for-using-the-rest-api) and [Acceptable Use Policies](https://docs.github.com/en/site-policy/acceptable-use-policies/github-acceptable-use-policies). Do not automate stars, follows, spam, or unsolicited promotional messages. No publishing method guarantees freedom from account enforcement.
