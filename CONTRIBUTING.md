# Contributing to RealtySkills

Thanks for helping make practical AI workflows easier to use in real estate.

## Suggest an improvement

Open an [issue](https://github.com/evyevans/realtyskills/issues/new/choose) for unclear instructions, missing inputs, a broken link, or a workflow request. Describe the real task in plain language and use fictional or redacted data. Cite current authoritative sources for legal or market-specific changes.

## Change or add a skill

1. Choose the most relevant category. Give new skills a unique lowercase identifier using letters, digits, and hyphens, under 64 characters.
2. Create `skills/<category>/<identifier>/SKILL.md` with valid YAML `name`, `description`, `license: MIT`, and `metadata` identifying author, version, category, level, and jurisdiction. The description must explain what the skill does and when to use it, within 1,024 characters.
3. State the audience, required inputs, result, tool requirements, example request, and working rules. Keep task selection concise. Put extensive procedures in `references/` and link them explicitly. Keep packages self-contained.
4. Add the entry to `catalog.json`. Add related skill identifiers when they help users choose. New contributions may omit original-source fields; do not change the historical source mapping for the original 49 files.
5. Update the catalog and any affected README counts. Add synthetic input/output examples when they explain behavior. Do not add claims about performance without reproducible evidence.
6. Run the checks below and open a pull request describing the user task, the resulting behavior, and what was checked.

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
.venv/bin/python scripts/render_catalog.py
.venv/bin/python scripts/validate_library.py
.venv/bin/python scripts/build_releases.py
```

If GitHub Actions reports stale generated documentation, run `render_catalog.py` and commit the resulting catalog changes. Generated release files stay in ignored `dist/`.

## Content standards

- Ask for missing facts; do not encourage the AI to fabricate data, testimonials, comparable sales, or credentials.
- Identify jurisdiction and cite primary sources where rules matter. A local variant must explain what changed and its review date.
- Preserve drafting and external-action boundaries. Do not silently send messages or modify client records.
- Use `example.com` for example email addresses and clearly synthetic data for examples.
- Keep language understandable to nontechnical professionals. Explain industry abbreviations on first use.
- Do not add tracking, paid dependencies, or unrelated promotions to a skill.

Contributions are distributed under this project's [MIT License](LICENSE). Submit only material you have the right to share, and preserve any required third-party notices. Maintainer review is required before changes enter the published library.
