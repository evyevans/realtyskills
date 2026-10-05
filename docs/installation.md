# Installation and downloads

For occasional use, [copy or attach the instructions](getting-started.md). Installation helps supported agents find a workflow without uploading it each time.

## Downloads

The [v1.0.0 release](https://github.com/evyevans/realtyskills/releases/tag/v1.0.0) is designed to provide:

- `realtyskills-v1.0.0.zip`: the public library, documentation, and archive.
- `realtyskills-chat-guides-v1.0.0.zip`: 42 standalone Markdown guides, each containing its complete instructions for chat attachment.
- `<skill-name>.zip`: one installable skill folder with its reference files and license.
- `SHA256SUMS.txt`: checksums for downloaded ZIPs.

You can also download the repository using GitHub's **Code → Download ZIP**. Extract it before opening files. The repository source ZIP does not contain generated release downloads; build them locally if a release is not yet available.

## Claude skills upload

Download an **individual** skill ZIP from the release. In Claude's skill management area, choose the custom skill upload option and upload that ZIP. Menu wording, plan eligibility, and organization permissions may vary. Enable the skill, start a new conversation, and describe a matching task.

Use the individual package, not the whole-library or chat-guide ZIP. Each package contains one top-level folder named after the skill, with `SKILL.md` inside and `references/` where needed. See [Claude's official custom skill guide](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills).

Claude Code's personal files and Claude account uploads are different installation routes. A file in your local `~/.claude/skills` does not by itself install an account skill for Cowork or cloud sessions. See [Claude's official skills documentation](https://code.claude.com/docs/en/skills).

## Local agent installation

Copy **one complete skill folder**, including references, into the appropriate directory. Category folders are for browsing the library; do not copy them as the installed skill's parent.

| Tool | Project installation | Personal installation |
|---|---|---|
| Claude Code | `.claude/skills/<skill-name>/` | `~/.claude/skills/<skill-name>/` |
| Codex | `.agents/skills/<skill-name>/` | `~/.agents/skills/<skill-name>/` |

These paths follow [Claude Code documentation](https://code.claude.com/docs/en/skills) and [OpenAI's skill documentation](https://learn.chatgpt.com/docs/build-skills), checked October 5, 2026. Your installed tool version or administrator policy may affect discovery.

From the extracted repository root, this example installs a starter for the current project:

```bash
# Claude Code
mkdir -p .claude/skills
cp -R skills/listings-and-marketing/listing-description-engine .claude/skills/

# Codex
mkdir -p .agents/skills
cp -R skills/listings-and-marketing/listing-description-engine .agents/skills/
```

Check whether a same-named destination exists before copying; preserve your customizations instead of overwriting them. Start a new session after installation. In Claude Code, try `/listing-description-engine`. In Codex, explicitly select `$listing-description-engine` in a request. Ask the tool to confirm which skill it loaded, then use the fictional [listing example](../examples/listing-copy.md).

Install only the workflows you use, then add others as needed. Installation provides instructions; it does not provide an MLS feed, browsing access, CRM connector, sending permissions, or a calculator.

## Other LLMs and agents

Use the standalone chat guides with assistants that accept sufficiently long text or Markdown attachments. For another agent tool, consult its own skill discovery documentation and preserve the complete folder. Standard packaging makes adaptation easier; it is not a guarantee that every product discovers or executes skills identically.

When constructing context programmatically, use [catalog.json](../catalog.json) to choose a skill, then load its entry and linked reference if present. Explicitly provide tools and data required for that task.

## Build the downloads locally

With Python 3.10 or newer, run from the repository root:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
.venv/bin/python scripts/validate_library.py
.venv/bin/python scripts/build_releases.py
```

Files are written to ignored `dist/`. The builder only packages the allowlisted public library; it excludes `.remember`, local agent settings, credentials, and Git internals. Run validation again after changing content.
