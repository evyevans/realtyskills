# CRM Data Cleanup — detailed procedure

## Intake and preservation

Confirm export scope, personal-data permissions, file type/encoding, headers, stable IDs, field dictionary, timestamp/time-zone conventions, enum values, required fields, and destination import behavior. Preserve the original unchanged. Do not retrieve unrelated notes or enrich missing private information without authorization. If only a sample is supplied, state that findings cover the sample, not the full database.

## Profile and normalize

Report row and unique-ID counts, missing required fields, invalid values, conflicting dates, malformed emails/phone fields, inconsistent stage/source tags, and explicit opt-out handling. Distinguish syntax validation from deliverability or ownership; do not claim an email or phone number was verified from formatting alone. Phone normalization needs country context. Date ambiguity needs clarification. Keep original raw values where useful and avoid transforming notes into unsupported facts.

## Candidate duplicates and merges

Use evidence combinations such as stable IDs, exact normalized contact fields, supplied entity/household relationships, and record context. Fuzzy name similarity is a candidate, not permission to merge. Shared household addresses/phones and reused emails can represent distinct people. Provide match basis, confidence, conflicting fields, proposed survivor ID, and manual-review reason. Do not invent a calibrated confidence threshold.

Apply the user-approved survivorship policy. Preserve history, attribution, representation/contact restrictions, and the strongest known suppression requirement; never turn an opt-out into opt-in through a merge. Conflicting consent evidence goes to review. Do not create consent from a date, stage, or note. Stage changes require actual lifecycle rules and evidence; age/nonresponse alone is not permission to mark a record dead or remove it.

## Dataset and import

Produce a proposed cleaned CSV/table with stable IDs and all required columns, plus per-record old/new/reason/rule/source log and an exceptions table. Keep review-required merges separate from automated normalization. Formula-like text in spreadsheet-bound CSV fields needs a safe export option; document any protective transformation and retain raw source so data is not silently lost.

Reconcile input count, output count, duplicate candidates, approved merges, rejected/held rows, and unchanged records. If file generation is unavailable, provide bounded copy-ready chunks with exact schema and disclose when the entire dataset cannot fit rather than claiming a complete CSV exists.

Before authorized live import, verify backup, target account, match key, update versus create behavior, suppression protection, sample/dry-run if supported, rollback, and results. Never execute deletions or mass merges merely because the audit recommends them. Stop on uncertain match behavior or partial-write errors and report affected IDs without blind re-import.

## Deliverable

Return quality summary; schema/assumptions; issue statistics; proposed cleaned data; candidate merge decisions; row-level change log; unresolved exceptions; count reconciliation; and review/import/rollback checklist.

## Before delivery

Original data is preserved; IDs and counts reconcile; shared contacts are not blindly merged; opt-outs survive normalization; no invented stages or consent; output coverage and live-write status are honest.
