# Publishing RealtySkills

These steps are for Evy Evans, the repository owner. The intended public address is `https://github.com/evyevans/realtyskills`. A written target URL is not evidence that the repository exists or is public.

## Account and authentication

Before publication, confirm the account is unrestricted. If a previous suspension remains unresolved, contact GitHub through its [appeal and reinstatement process](https://docs.github.com/en/site-policy/acceptable-use-policies/github-appeal-and-reinstatement) before publishing. Technical authentication success alone does not establish that an earlier restriction is resolved.

The recommended authentication route is GitHub CLI's official browser flow. Run in your own terminal:

```bash
gh auth login --hostname github.com --git-protocol https --web --scopes workflow
gh api user --jq .login
```

The second command must show `evyevans`. Do not print, paste into a chat, or commit the stored token. The extra `workflow` scope permits publishing the repository's GitHub Actions file. See [GitHub CLI authentication](https://cli.github.com/manual/gh_auth_login).

If you specifically need a token instead, use [GitHub's fine-grained token creation page](https://github.com/settings/personal-access-tokens/new) and [official token guidance](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens). Prefer a short expiration and access limited to this repository after creating it in the browser. Contents write is needed to push and upload release assets; Workflows write is needed for workflow files; Administration write is needed to change repository settings and topics. Fine-grained repository creation has separate permission requirements. Choose only what your intended operation requires; browser login avoids needing to configure these permissions for this launch. Do not send a token to an assistant.

## Prepare locally

From the project folder, run validation and packaging using the Python environment described in [installation](installation.md). Inspect the README, catalog, and examples. The bundle excludes `.remember`, local agent settings, credentials, Git internals, and build caches.

Initialize Git from your own terminal if it is not already initialized. These commands create a local repository and commit only the public allowlisted paths:

```bash
git init -b main
git config --local user.name "Evy Evans"
git config --local user.email "evyevans@users.noreply.github.com"
git add README.md LICENSE CONTRIBUTING.md CHANGELOG.md catalog.json requirements-dev.txt .gitignore skills docs examples archive assets scripts .github
git diff --cached --stat
git diff --cached --check
git commit -m "Launch RealtySkills: 42 real estate AI workflows"
```

If Git is already initialized, inspect its branch, status, and remotes before using these instructions. Do not reset or overwrite existing history. This session's filesystem policy prevented `.git` initialization; it did not prevent building the resource files.

## Create and publish one repository

Check `https://github.com/evyevans/realtyskills` in your browser before creating it. If it already exists, inspect its contents and ownership before connecting this project. Do not overwrite an existing project. If it is available:

```bash
gh repo create evyevans/realtyskills --public --source . --remote origin --description "Free real estate AI skills by Evy Evans: 42 workflows for agents, investors, property managers, and brokerage teams."
git push -u origin main
```

Run each command once and inspect its result. Stop on authentication failures, account restrictions, unexpected ownership, or rate-limit responses; resolve the stated cause before retrying. Do not use force pushes for this launch.

Add relevant search topics after the push succeeds:

```bash
gh repo edit evyevans/realtyskills --add-topic real-estate --add-topic ai-skills --add-topic agent-skills --add-topic claude-skills --add-topic llm --add-topic prompt-engineering --add-topic property-management --add-topic real-estate-agents
```

## Release and verify

Wait for the Library checks workflow to finish successfully. Create the release, then upload each of the 44 ZIPs and `SHA256SUMS.txt` **one at a time**, checking each result. For example:

```bash
gh release create v1.0.0 --repo evyevans/realtyskills --target main --title "RealtySkills v1.0.0 — Real Estate AI Skills by Evy Evans" --notes-file docs/release-notes-v1.0.0.md
gh release upload v1.0.0 dist/realtyskills-v1.0.0.zip --repo evyevans/realtyskills
gh release upload v1.0.0 dist/realtyskills-chat-guides-v1.0.0.zip --repo evyevans/realtyskills
```

Upload the individual skill ZIPs and checksum file the same way. Leave at least one second between uploads. Stop on errors rather than repeating a failed request. The CLI also supports uploading multiple assets in one command, but sequential uploads make it easier to observe and handle errors for this launch.

Verify from a logged-out or private browser window that the repository, README links, examples, and release downloads are accessible. Download one starter and one detailed ZIP, verify their checksums, and confirm each contains its entry and any references.

Update the release notes with the actual publication and GitHub Actions results. Then use the [LinkedIn announcement draft](linkedin-launch.md).

## Policy basis and limits

GitHub's [Acceptable Use Policies](https://docs.github.com/en/site-policy/acceptable-use-policies/github-acceptable-use-policies) permit project-related promotional text in a README and prohibit fake engagement, rank abuse, spam, privacy violations, and excessive bulk activity. Publish useful project material and invite voluntary feedback. Do not automate starring, following, or promotional messages to other repositories.

GitHub's [API best practices](https://docs.github.com/en/rest/using-the-rest-api/best-practices-for-using-the-rest-api) advise sequential requests, pauses between large numbers of writes, and respecting rate-limit responses. Repeatedly ignoring errors can lead to enforcement.

These steps follow documented publishing practices. No token type, request schedule, or assistant can guarantee an account will never be restricted. Only GitHub can determine account standing and resolve a prior suspension.
