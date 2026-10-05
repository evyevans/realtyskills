# Example: prioritizing a fictional lead batch

**Skill:** [Lead Qualification](../skills/leads-and-prospecting/lead-qualification-engine/SKILL.md)

## Input

All contacts use aliases. All stated budgets fit the user's supplied target inventory range. No timeline bonuses apply. Contact permissions are supplied separately from scores.

| Alias | Source | Financial readiness | Timeline | Strongest engagement | Contact status |
|---|---|---|---|---|---|
| Lead A | Past-client referral | Pre-approval letter supplied | Within 30 days | Requested a showing | Contactable by email |
| Lead B | Personal website form | Budget supplied; no lender contact | 3–6 months | Downloaded buyer guide | Contactable by email |
| Lead C | Social media DM | Budget and lender contact unknown | Unknown | Asked to stop contact | Opted out |

Request: “Use the default rubric in the attached playbook. Show each dimension and total. Flag missing facts and honor the contact status. Draft next actions only.”

## Illustrative output

| Alias | Source / 20 | Finance / 25 | Timeline / 25 | Engagement / 30 | Total / 100 | Result | Next action |
|---|---:|---:|---:|---:|---:|---|---|
| Lead A | 20 | 25 | 25 | 28 | 98 | Ready now | Review showing preferences and draft an email |
| Lead B | 12 | 10 | 12 | 15 | 49 | Long-term nurture | Ask about lender plans and confirm preferred cadence |
| Lead C | 7 | 5 | 3 | 0 | 15 | Do not contact | Preserve opt-out; no outreach or campaign enrollment |

The arithmetic is 20 + 25 + 25 + 28 = 98; 12 + 10 + 12 + 15 = 49; and 7 + 5 + 3 + 0 = 15. Missing financial and timeline information for Lead C is flagged, not inferred.

## Review

These scores are configurable workflow heuristics. They are not validated conversion predictions, loan decisions, or determinations of access to housing. An opt-out overrides any numeric total. Review the facts and lawful contact basis before outreach; no messages have been sent.
