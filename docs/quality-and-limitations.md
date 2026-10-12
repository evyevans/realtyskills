# Capabilities, review, and limitations

RealtySkills is an instruction library. It does not include trained models, paid subscriptions, live market feeds, CRM integrations, sending services, or professional advice.

## What the labels mean

**Starter:** a focused task with instructions contained in one entry file. **Detailed:** a more extensive procedure whose full playbook is linked from the entry. More detail is not proof of better results or professional validation.

The 42 active workflows consist of 12 starters and 30 detailed playbooks. Seven older overlapping versions were removed from the current collection and downloads; provenance remains in Git history and catalog records. The [inventory](maintainer/inventory.md) documents every source file.

See the [individual revision audit](maintainer/skill-quality-audit.md) for all 42 reviewed skills and scenario coverage.

## What has been checked

The repository's validation script checks catalog consistency, metadata, identifiers, reference existence, internal Markdown links, file accounting, attribution cleanup, and recognizable secret patterns. Release checks verify self-contained package structure and matching content.

These are structural checks. They do not prove model reliability, legal accuracy, market accuracy, investment returns, or compatibility with every AI account. Worked examples are hand-authored demonstrations, not recorded outputs from live model evaluations. No live platform behavior is claimed unless explicitly documented in a release verification note.

## Data and tools

Never invent comparable sales, rents, client history, property features, or current market statistics. Supply dated evidence or use browsing where supported. A tool without browsing should identify the missing data rather than provide a current report from memory.

Financial models require verified inputs and arithmetic checks. Modeled assumptions must be explicit and separate from observed facts; missing costs and data are unknown, not zero. Use a spreadsheet or calculator for consequential calculations.

## Jurisdiction

Active workflows use the user’s jurisdiction, market evidence, currency, units, and actual terms. Official U.S. source links are starting points for applicable U.S. work, not rules for other countries. The Section 1031 planning workflow retains its U.S. federal scope. Retired source copies are not included in current packages.

Before drafting a legal notice, contract clause, tax plan, or compliance conclusion, confirm jurisdiction, consult current primary sources, and involve a qualified local professional. Each active skill distinguishes confirmed facts, assumptions, and unknowns, and delivers supported work even when some tools or records are unavailable.

One concrete correction in this edition: the source CRM playbook stated that US CAN-SPAM law requires opt-in for commercial email. That statement was replaced with a source-checking instruction covering sender information, postal address, opt-out, and other requirements. See the [FTC's official business guide](https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business). Other jurisdictions may require prior consent.

## Privacy and actions

Use synthetic records for examples. Redact unnecessary client identifiers, sensitive financial data, and private contact information before providing data to an AI tool. Check your product's data policies and your organization's requirements.

Sending messages, publishing content, modifying CRM records, dispatching vendors, and scheduling events are separate actions. They require an available integration and explicit user instructions. The user’s existing authorization applies to the specified actions; an installed skill does not itself grant account access or broader action permissions.

## Report a problem

Open an [issue](https://github.com/evyevans/realtyskills/issues/new/choose) with the skill name, expected behavior, and a redacted or fictional example. For jurisdiction-specific corrections, include authoritative sources and their dates. Never include credentials or private client documents in a public issue.
