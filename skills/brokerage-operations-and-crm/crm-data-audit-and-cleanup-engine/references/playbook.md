# Source playbook

This playbook supplies task procedures and examples. Follow the working rules in the skill entry, verify current jurisdiction-specific claims, and treat examples as illustrative.

# CRM Data Audit & Cleanup Engine

This skill ingests a CRM contact export (CSV or pasted data), performs a systematic data quality audit, identifies duplicate contacts, flags incomplete records, reclassifies contacts by lead stage and recency, and produces a prioritized cleanup action plan with a cleaned dataset ready for re-import. Designed for agents and teams whose CRM has grown organically for years and is now an unreliable, chaotic source of "data" rather than a clean database of real relationships.

## 🧠 SKILL IDENTITY

**WHO this skill is for:**
A high-volume agent, team lead, or brokerage owner whose CRM contains 500–10,000+ contacts accumulated over years of lead generation — and who knows that a significant portion of those contacts are duplicates, incomplete, outdated, or incorrectly tagged. The CRM feels like a liability rather than an asset.

**WHAT this skill does:**
Produces five outputs from a CRM export:
1. **Data Quality Audit Report:** Overall data health score + findings on missing fields, formatting errors, and field inconsistencies
2. **Duplicate Detection Report:** Identified duplicate or near-duplicate contacts with recommended merge actions
3. **Contact Reclassification:** Each contact assigned to a lead stage (HOT / WARM / COLD / DEAD / PAST CLIENT / SPHERE) based on last activity date and available data
4. **Cleanup Action Plan:** Prioritized list of specific cleanup actions, starting with the highest-value segments
5. **Cleaned Export File:** A corrected version of the database ready for re-import (column standardization, formatting fixes applied)

**WHERE to use this skill:**
Export your CRM contacts to CSV and upload or paste into Claude. Claude processes the full export within its 1M token context window — handling databases up to approximately 50,000 contacts.

**WHEN to activate this skill:**
Run this audit annually (minimum) or whenever: CRM open rates fall below 15%, your team complains the CRM isn't accurate, before migrating to a new CRM, before running a major re-engagement campaign, or when you realize you "never look at your CRM anymore."

**WHY this skill matters:**
This workflow makes the required inputs and output structure explicit. Its numerical benchmarks are configurable assumptions, not validated performance claims.

**HOW this skill works (Overview):**
Claude reads the CSV export, parses every column, identifies field patterns, flags anomalies, runs duplicate detection logic across name/phone/email combinations, reclassifies contacts by recency and stage, and produces both the audit findings and a corrected version of the dataset. The 1M token context window handles large exports in a single pass.

---

## 📥 REQUIRED INPUTS

| Input | Format | Source | Required? | Example |
|-------|--------|--------|-----------|---------|
| CRM contact export | CSV file (uploaded or pasted) | User provides | Yes | Follow Up Boss export: Name, Email, Phone, Stage, Last Activity |
| CRM platform | Platform name | User provides | No | Follow Up Boss |
| Total contact count (expected) | Integer | User provides | No | 3,847 contacts |
| Key fields to audit | Field names | User provides | No | Email, Phone, Stage, Last Activity Date, Source |
| Re-engagement threshold | Days since last contact = "cold" | User provides | No | 365 days (default) |

**Note:** This skill is fully autonomous once the CSV is provided. No additional user input required to run the full audit.

---

## ⚙️ EXECUTION SOP

### Step 1: Parse and Profile the Dataset

**What Claude does:**
Read the full CSV export and generate a dataset profile:
- Total record count
- Column inventory: list all fields present, identify which are populated vs. empty
- Field completeness rates: For each column, calculate % of records with a non-empty value
- Data type validation: Identify fields with mixed types (e.g., phone numbers in multiple formats), date fields in inconsistent formats
- Encoding issues: Flag any rows with character encoding problems, special characters, or import artifacts

**Field Completeness Benchmarks (flag if below):**
- First Name: should be ≥ 95% complete
- Email address: should be ≥ 70% complete (buyers and investors often have email; off-market leads may not)
- Phone number: should be ≥ 85% complete
- Lead Stage / Contact Type: should be ≥ 80% complete
- Last Activity Date: should be ≥ 60% complete
- Lead Source: should be ≥ 60% complete

**Tools / Resources needed:**
Claude's 1M token context window for full CSV processing. No external tools required.

**Data source:**
User-provided CSV export.

**Output of this step:**
Dataset Profile Report: record count, field inventory, completeness rates, and data type flags.

**Cowork behavior:**
PROCEED WITH ANALYSIS AND DRAFTING — fully autonomous.

**If this step fails or required data is missing:**
If the CSV is malformed or missing headers, ask: "The CSV appears to be missing column headers. Can you paste the first row of your export (the header row) so I can identify the field structure?"

---

### Step 2: Duplicate Detection

**What Claude does:**
Run three passes of duplicate detection at increasing sensitivity levels:

**Pass 1 — Exact Duplicates:**
Identify records where email address, phone number, or full name + address match exactly. These are definitive duplicates — flag for immediate merge.

**Pass 2 — Near-Duplicate Detection (Fuzzy Match):**
Identify records where:
- First name is the same AND last name is the same AND phone numbers share 7+ digits
- Email address domain matches AND first name matches (e.g., john@example.com and j.smith@example.com for "John Smith")
- Same address with different name spellings (Rob vs. Robert, etc.)
These are probable duplicates — flag for human review before merging.

**Pass 3 — Family/Household Detection:**
Identify records sharing the same address who may be a household unit (husband/wife, parent/adult child). These are not duplicates — flag as "SAME HOUSEHOLD" for potential household record consolidation.

**For each duplicate set, recommend:**
- Which record to keep (the more complete record, or the more recently contacted)
- Which record to merge into it (and which fields to preserve from each)

**Tools / Resources needed:**
None — string matching and comparison within Claude context.

**Data source:**
Parsed dataset from Step 1.

**Output of this step:**
Duplicate Detection Report: exact duplicate count, near-duplicate count, household cluster count, and merge recommendations.

**Cowork behavior:**
PROCEED WITH ANALYSIS AND DRAFTING — flag for human review but do not auto-merge without user confirmation.

**If this step fails or required data is missing:**
If email and phone are both missing for most records, run name-only duplicate detection and flag as lower confidence.

> 💡 **Precision Note:** When merging duplicates, always preserve the EARLIEST lead creation date and ALL phone numbers and email addresses from both records. The goal is to retain all valid contact information in a single record, not to discard any potentially valid contact method.

---

### Step 3: Contact Reclassification by Stage and Recency

**What Claude does:**
For each contact, assign a current lifecycle stage based on available data:

**Stage Classification Logic (in order of priority):**
1. **PAST CLIENT:** Last transaction date within the record, or any note/stage indicating "closed" or "sold"
2. **HOT LEAD:** Last activity within 30 days AND a stage indicating active buyer/seller intent
3. **WARM LEAD:** Last activity 31–180 days ago, OR any stage indicating "nurture" or "follow up"
4. **COLD LEAD:** Last activity 181–365 days ago, no transaction
5. **DEAD LEAD:** Last activity > 365 days ago, no transaction — candidate for re-engagement campaign before archiving
6. **SPHERE:** Contact type indicates personal relationship (friend, family, colleague) — regardless of last activity
7. **UNCLASSIFIED:** Insufficient data to classify — flag for manual review

**Recency Buckets (last activity date analysis):**
- Active (0–30 days): Flag for immediate personal outreach
- Recent (31–90 days): Flag for drip campaign or task assignment
- Dormant (91–365 days): Flag for re-engagement sequence
- Lapsed (>365 days): Flag for re-engagement or archive decision

**Tools / Resources needed:**
None — classification from available CRM fields.

**Data source:**
Parsed dataset from Step 1.

**Output of this step:**
Reclassification summary: count per stage + count per recency bucket + list of HOT contacts requiring immediate personal outreach.

**Cowork behavior:**
PROCEED WITH ANALYSIS AND DRAFTING.

**If this step fails or required data is missing:**
If last activity date is missing for most records, classify by stage field only and flag: "⚠️ Last activity dates missing for [X]% of records — recency classification is incomplete. Update last-contact dates as you make calls."

---

### Step 4: Generate Cleanup Action Plan

**What Claude does:**
Produce a prioritized, specific action plan for cleaning up the database. Organize by ROI — highest-value actions first.

**Priority 1 — Revenue-Critical (Do this week):**
- Merge all exact duplicates (list count)
- Contact all HOT leads personally — not via drip
- Verify email and phone for all PAST CLIENTS — these are your best referral source

**Priority 2 — Database Hygiene (Do this month):**
- Merge all near-duplicates (review recommended list)
- Assign stage tags to all UNCLASSIFIED contacts (requires manual review of [X] records)
- Add missing emails or phones for WARM leads via skip tracing (BatchSkipTracing, BeenVerified)
- Set up re-engagement drip for COLD leads

**Priority 3 — Long-Term Maintenance (Set up ongoing):**
- Archive all DEAD leads (>365 days, no response to re-engagement) into an inactive list
- Establish a data hygiene standard: any new contact added to CRM must have at minimum: full name, one contact method, lead source, and stage
- Set up quarterly database audit schedule (re-run this skill every 90 days)

**Tools / Resources needed:**
Follow Up Boss / kvCORE / Salesforce for executing merges and updates. BatchSkipTracing or BeenVerified for enriching missing contact data.

**Data source:**
Findings from Steps 1–3.

**Output of this step:**
Prioritized cleanup action plan with specific counts and instructions.

**Cowork behavior:**
PROCEED WITH ANALYSIS AND DRAFTING.

**If this step fails or required data is missing:**
Produce the plan with estimated counts and flag where specific counts couldn't be determined.

---

### Step 5: Deliver Cleaned Dataset

**What Claude does:**
Apply all non-destructive fixes to the dataset and deliver a corrected version:
- Standardize phone number format: (XXX) XXX-XXXX for all US numbers
- Standardize email format: lowercase, remove spaces
- Standardize name capitalization: Title Case for names
- Fix date format inconsistencies: MM/DD/YYYY standard
- Remove obviously corrupt records (e.g., records where name = "test" or email = "abc@example.com")
- Add the new "Audit Stage" classification column from Step 3

**Output a corrected CSV** (in the same column order as the original) ready for re-import.

⚠️ Do NOT merge duplicate records in the cleaned output — deliver a separate merge recommendation list. Merging records in the CRM is a destructive action that requires human confirmation.

**Tools / Resources needed:**
None — text processing within Claude context.

**Data source:**
Original dataset + cleanup findings from Steps 1–4.

**Output of this step:**
Cleaned CSV (in chat, formatted for copy-paste or Cowork file write) + merge recommendation list as a separate table.

**Cowork behavior:**
CONFIRM BEFORE PROCEEDING — before delivering the cleaned file, confirm: "I've prepared a cleaned version of your database with formatting fixes and a new 'Audit Stage' column. The duplicate merge recommendations are separate — you'll review and merge those manually in your CRM. Shall I deliver the cleaned file?"

**If this step fails or required data is missing:**
Deliver the cleanup findings and action plan even if the cleaned file cannot be generated from pasted data.

---

## 💻 CODE EXAMPLE

```python
# CRM Duplicate Detection — Phone & Email Matching
# Evykynn | AI assistant Skill Library | May 2026

import csv
from collections import defaultdict

def normalize_phone(phone: str) -> str:
    """Strip all non-digit characters from phone number."""
    return ''.join(c for c in str(phone) if c.isdigit())

def find_duplicates(csv_file_path: str) -> dict:
    """
    Identify duplicate contacts by email and normalized phone.
    Returns dict of duplicate groups with contact IDs.
    """
    email_groups = defaultdict(list)
    phone_groups = defaultdict(list)

    with open(csv_file_path, 'r') as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader):
            email = row.get('Email', '').lower().strip()
            phone = normalize_phone(row.get('Phone', ''))
            name = row.get('Name', f'Row {i+1}')

            if email and len(email) > 5:
                email_groups[email].append({'id': i, 'name': name, 'row': row})
            if phone and len(phone) >= 10:
                phone_groups[phone].append({'id': i, 'name': name, 'row': row})

    exact_email_dupes = {k: v for k, v in email_groups.items() if len(v) > 1}
    exact_phone_dupes = {k: v for k, v in phone_groups.items() if len(v) > 1}

    return {
        'email_duplicates': exact_email_dupes,
        'phone_duplicates': exact_phone_dupes,
        'total_email_dupes': sum(len(v) - 1 for v in exact_email_dupes.values()),
        'total_phone_dupes': sum(len(v) - 1 for v in exact_phone_dupes.values()),
    }

# Example usage:
results = find_duplicates('crm_export.csv')
print(f"Duplicate emails found: {results['total_email_dupes']}")
print(f"Duplicate phones found: {results['total_phone_dupes']}")
```

---

## 📤 OUTPUT FORMAT

**Output type:** CRM Audit Report + Cleaned Dataset  
**Delivery method:** Returned directly in chat — report is ready to act on; cleaned CSV is ready to re-import

---

```
CRM DATA AUDIT REPORT — Evykynn
CRM Platform:   Follow Up Boss
Export Date:    May 10, 2026
Total Records:  3,847
Analyst:        AI assistant via Evykynn Skill Library

━━━━━━━━━━━━━━━━ DATA HEALTH SCORE ━━━━━━━━━
Overall:       62/100 — NEEDS SIGNIFICANT CLEANUP

━━━━━━━━━━━━━━━━ FIELD COMPLETENESS ━━━━━━━━
First Name:    97%  ✅
Email:         68%  ⚠️ (below 70% benchmark — 1,229 missing)
Phone:         82%  ✅
Stage:         71%  ⚠️ (1,117 contacts unclassified)
Last Activity: 54%  ❌ (below 60% — 1,770 contacts undated)
Lead Source:   49%  ❌ (major gap — no source attribution)

━━━━━━━━━━━━━━━━ DUPLICATE DETECTION ━━━━━━━
Exact email duplicates:   234 contact pairs → 234 merges needed
Exact phone duplicates:    87 contact pairs (not already in email)
Near-duplicates (review):  412 likely duplicates
Same household:            156 household clusters
TOTAL ACTIONABLE:          321 definitive merges recommended

━━━━━━━━━━━━━━━━ LIFECYCLE RECLASSIFICATION ━━
PAST CLIENT:      287  ← Highest priority — re-engage
HOT LEAD:          43  ← Contact personally THIS WEEK
WARM LEAD:        612  ← Add to drip campaign
COLD LEAD:      1,204  ← Re-engagement sequence
DEAD LEAD:        891  ← Archive or final attempt
SPHERE:           234  ← Personal outreach
UNCLASSIFIED:     576  ← Manual review needed

━━━━━━━━━━━━━━━━ CLEANUP PRIORITY LIST ━━━━━
1. [THIS WEEK]  Personal outreach to 43 HOT leads
2. [THIS WEEK]  Re-engage 287 past clients — highest referral ROI
3. [THIS MONTH] Merge 321 definitive duplicates
4. [THIS MONTH] Skip trace missing emails for 612 WARM leads
5. [ONGOING]    Tag all 576 unclassified contacts
6. [ONGOING]    Set up quarterly data hygiene audit

Cleaned dataset ready for re-import: [CSV follows]
Merge recommendation list: [Table follows]
```

---

## 🔐 PERMISSIONS & SETUP CHECKLIST

- [ ] **CRM Export:** Export contacts as CSV from your CRM (Follow Up Boss: Settings → Export; kvCORE: Contacts → Export; Salesforce: Reports → Export)
- [ ] **Backup:** Save a copy of the original export before making any changes to your CRM
- [ ] **Skip Tracing:** For missing contact data, create a BatchSkipTracing.com account — typical cost $0.15–$0.40 per record

---

## ✅ QUALITY SELF-CHECK

Before delivering any output, Claude must internally verify every item below:

- [ ] All records in the CSV were processed — no rows skipped
- [ ] Duplicate detection ran all three passes (exact, near-duplicate, household)
- [ ] Reclassification applied to all records — UNCLASSIFIED used only when data is truly insufficient
- [ ] HOT leads and PAST CLIENTS are prominently highlighted in the action plan
- [ ] Cleaned CSV does not contain merged records — merge decisions are left to human review
- [ ] Overall data health score is calculated and present
- [ ] Action plan is prioritized by revenue impact, not alphabetically or by volume

---

## ⚠️ EDGE CASES & ESCALATION RULES

| Scenario | Claude's Exact Response |
|----------|------------------------|
| CSV has no headers | Ask for header row before processing: "I need the column headers to correctly parse your data. Paste the first row (headers) and I'll continue." |
| Database is extremely large (>20,000 rows) | "For very large exports, I'll process in segments. Paste rows 1–5,000 first, then we'll continue." |
| Contact data includes SSNs or financial data | "⚠️ DATA SECURITY FLAG: This export appears to contain sensitive personal data (SSN/financial). Remove these columns before sharing. I will not process SSNs or financial account numbers." |
| Legal compliance concern | ⚠️ LEGAL FLAG: "Ensure your CRM contacts were collected with appropriate consent. TCPA compliance requires express written consent for automated calls/texts. For US commercial email, verify sender identification, postal address, opt-out, and other CAN-SPAM requirements against current FTC guidance; other jurisdictions may require prior consent." |
| User wants to auto-delete dead leads | "Recommend archiving rather than deleting — archived contacts can be reactivated. Deleted contacts cannot be recovered and represent lost historical data." |
| Session approaching context limit | Write `_PROGRESS_CHECKPOINT.md` with audit steps completed and rows processed |

---

## 📖 DOMAIN GLOSSARY

| Term | Definition |
|------|-----------|
| CRM | Customer Relationship Management software — the platform used to track leads, contacts, and communications |
| Duplicate Contact | Two or more CRM records representing the same person — common causes: multiple form submissions, manual re-entry, CRM migrations |
| Skip Tracing | The process of locating a contact's current phone or email using data aggregation services |
| Lead Stage | A classification assigned to a CRM contact indicating their position in the buying/selling cycle (Hot, Warm, Cold, Past Client, etc.) |
| Drip Campaign | A series of automated, pre-written communications sent to a contact segment over a defined period |
| Data Hygiene | The practice of maintaining accurate, complete, and current data in a CRM through regular auditing and correction |
| Database Health Score | A composite metric measuring the completeness, accuracy, and recency of a CRM's contact records |
| Re-engagement Campaign | A targeted outreach effort to contacts who have gone inactive, with the goal of restarting the relationship |

---

*Authored by Evykynn | Real Estate Agentic Automation*

*Maintained as part of RealtySkills by Evykynn. Example dates and figures are illustrative.*
