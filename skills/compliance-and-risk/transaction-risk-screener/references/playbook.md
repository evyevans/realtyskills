# Source playbook

This playbook supplies task procedures and examples. Follow the working rules in the skill entry, verify current jurisdiction-specific claims, and treat examples as illustrative.

# Transaction Risk & Red Flag Screener

This skill performs a systematic pre-closing risk assessment on a real estate transaction — screening for fraud indicators, title risks, entity legitimacy concerns, contract structure vulnerabilities, and regulatory compliance issues. It produces a Risk Assessment Report with a severity-tiered red flag list, the specific legal or financial exposure each flag creates, and recommended remediation actions for each finding.

## 🧠 SKILL IDENTITY

**WHO this skill is for:**
A real estate transaction attorney, institutional wholesaler, or brokerage owner who needs to assess whether a transaction has unusual risk characteristics before committing time, capital, or professional reputation to it. Particularly valuable for: transactions involving unknown counterparties, discounted-price acquisitions, wire transfers over $50,000, distressed properties with complex title histories, or any deal that "feels off" but you can't immediately articulate why.

**WHAT this skill does:**
Produces a Transaction Risk Assessment Report covering six risk dimensions: (1) Fraud and impersonation indicators, (2) Title and ownership red flags, (3) Entity and counterparty legitimacy, (4) Contract structure vulnerabilities, (5) Wire transfer and financial risk, (6) Regulatory and compliance exposure. Each flag is assigned a severity level (CRITICAL / HIGH / MEDIUM / LOW) with the specific risk it creates and the exact remediation step required.

**WHERE to use this skill:**
Attach to a Claude.ai chat session and paste the transaction summary (parties, property, purchase price, financing structure, and any known background). Claude uses extended thinking to analyze the complete risk profile before delivering findings.

**WHEN to activate this skill:**
Activate before signing any contract, before wiring earnest money, before disbursing closing proceeds, and before accepting any transaction with unusual characteristics. Also activate when a counterparty, attorney, or title company exhibits behaviors inconsistent with standard transaction practices.

**WHY this skill matters:**
This workflow makes the required inputs and output structure explicit. Its numerical benchmarks are configurable assumptions, not validated performance claims.

**HOW this skill works (Overview):**
Claude applies extended thinking to analyze the transaction across six risk dimensions simultaneously, cross-referencing all provided information for internal consistency. It flags any information gap that is inconsistent with a legitimate transaction, assigns each flag to a risk dimension and severity level, and provides specific verification steps to confirm or eliminate each concern. The output is a structured risk report, not a yes/no verdict — it equips the professional to make an informed decision about how to proceed.

---

## 📥 REQUIRED INPUTS

| Input | Format | Source | Required? | Example |
|-------|--------|--------|-----------|---------|
| Property address | Full address | User provides | Yes | 4821 Maple Ave, Columbus OH 43215 |
| Purchase price | Dollar amount | User provides | Yes | $285,000 |
| Seller name(s) | Full legal name | User provides | Yes | John Smith |
| Buyer name(s) / entity | Full legal name or entity | User provides | Yes | Maple Capital LLC |
| Transaction structure | Cash / Financed / Subject-to / Assignment | User provides | Yes | Cash purchase |
| How deal originated | MLS / direct / wholesaler / referral | User provides | No | Off-market direct-to-seller |
| Any known title history issues | Plain text | User provides | No | Inherited property — probate closed 2024 |
| Wire instructions source | How received — email / portal / phone | User provides | No | Email from title company |
| Any unusual terms or requests | Plain text | User provides | No | Seller requests cash at closing, no title company |
| Timeline pressure | Stated urgency | User provides | No | Must close in 5 days |

---

## ⚙️ EXECUTION SOP

### Step 1: Parse Transaction Profile and Flag Information Gaps

**What Claude does:**
Read all provided transaction information and immediately flag any information that is absent but should be present in a legitimate transaction. The absence of standard information is itself a red flag. Specifically:

**Information that should be present in every legitimate transaction:**
- Full legal name of all parties (not nicknames, abbreviations, or "the owner")
- A title company or closing attorney handling the transaction
- A verifiable property address that matches public records
- A logical price relative to the property type and location
- A documented source for how the deal originated
- Standard closing timeline (14–60 days for cash, 30–45 for financed)

**Red flags at intake:**
- Seller claims to own property but can't or won't provide their full legal name
- No title company, settlement agent, or attorney involved
- Urgency to close in fewer than 7 business days with no explanation
- Purchase price significantly below market with no disclosed reason
- All communication is via email only — no phone, no in-person contact
- Deal originated through an unknown third party with unclear role

**Tools / Resources needed:**
None — analysis from provided information.

**Data source:**
User-provided transaction details.

**Output of this step:**
Information gap list (items absent that should be present) + initial red flag count.

**Cowork behavior:**
PROCEED WITH ANALYSIS AND DRAFTING.

**If this step fails or required data is missing:**
If fewer than 4 required inputs are provided, ask for the minimum viable information set before proceeding.

---

### Step 2: Fraud and Impersonation Indicator Screen

**What Claude does:**
Apply the FBI and FinCEN red flag checklist for real estate fraud patterns. Screen for:

**Deed Fraud / Title Fraud Indicators:**
- Property is vacant or the owner is elderly, deceased, or out-of-state
- Seller cannot provide identification or refuses identity verification
- Seller claims to be acting through a power of attorney (POA) — POA fraud is a common vector; verify POA is current, properly executed, and principal is alive
- Price is substantially below market with no distress condition to explain the discount
- Seller initiated contact proactively through unusual channels
- Property recently transferred (within 6 months) at a significantly different price

**Wire Fraud Indicators:**
- Wire instructions were received via email, not through a secure title company portal
- Wire instructions were changed or updated via email close to closing
- The receiving bank account is in a different state or country than the title company
- Pressure to send wire "today" or "before 3 PM" without standard notice
- Email domain of the title company or attorney is slightly misspelled or uses a free email service (@gmail, @yahoo)

**Mortgage Fraud Indicators (for financed transactions):**
- Appraisal was provided by the seller (not the lender)
- Purchase price was recently increased to accommodate a larger loan
- Down payment source is undisclosed or claimed to be a "gift" with no documentation
- Buyer occupancy intent is unclear (investor claiming owner-occupant for better rate)

**Tools / Resources needed:**
None — pattern matching against established fraud indicator databases.

**Data source:**
User-provided transaction details + FBI/FinCEN fraud indicator framework.

**Output of this step:**
Fraud Indicator Assessment: each flagged pattern, its severity, and the specific verification step to confirm or eliminate the risk.

**Cowork behavior:**
PROCEED WITH ANALYSIS AND DRAFTING. If any CRITICAL fraud indicator is found, pause and alert the user immediately before continuing.

**If this step fails or required data is missing:**
Apply the available information and note which fraud dimensions could not be assessed due to missing data.

> 💡 **Precision Note:** The single highest-risk wire fraud indicator is an email-delivered change to wire instructions within 72 hours of closing. This pattern is present in over 60% of real estate wire fraud cases (FBI IC3 2024). Always verify wire instructions via a phone call to a number obtained independently — not a number provided in the same email as the wire instructions.

---

### Step 3: Title and Ownership Red Flag Screen

**What Claude does:**
Evaluate the title and ownership profile for red flags:

- **Chain of title gaps:** Are there recent transfers, quitclaim deeds, or transactions that don't follow a logical ownership progression?
- **Probate / estate sale:** Was the property recently inherited? Is the estate properly administered? Is the personal representative (executor) actually authorized to sell?
- **Joint ownership complications:** Is the seller one of multiple owners? Does the non-selling owner need to consent?
- **LLC / Entity vesting:** If the seller is an entity, who has authority to execute the deed? Is the entity in good standing?
- **Existing liens:** Any mention of mortgages, tax liens, HOA delinquencies, judgment liens, or mechanic's liens that need to be resolved at closing?
- **Recent price anomalies:** Did the property sell recently at a very different price? (Could indicate flipping fraud or inflated appraisal)

**Tools / Resources needed:**
County recorder website / Zillow / Redfin for price history verification. If user can access these, instruct them to check. If not, flag as VERIFY.

**Data source:**
User-provided title information + Claude's ability to reason about ownership chain logic.

**Output of this step:**
Title Risk Assessment with each concern rated by severity.

**Cowork behavior:**
PROCEED WITH ANALYSIS AND DRAFTING.

**If this step fails or required data is missing:**
Produce the title risk framework and instruct the user to verify each item with their title company: "Title commitment with Schedule B exceptions is the definitive source for title risk — obtain this before closing."

---

### Step 4: Entity and Counterparty Legitimacy Screen

**What Claude does:**
If any party to the transaction is an entity (LLC, corporation, trust, partnership), apply the following verification framework:

- **Entity in good standing:** Instruct user to verify entity status at the state Secretary of State website
- **Authorized signatory:** Confirm the person signing on behalf of the entity has authority (operating agreement, corporate resolution, or trustee documentation)
- **Entity age:** A newly formed entity (30–60 days old) buying or selling a property at a significant discount is a red flag
- **Beneficial ownership:** FinCEN's Corporate Transparency Act (CTA) now requires most LLCs to file beneficial ownership information — flag if the entity may be non-compliant
- **FinCEN GTO markets:** If the transaction is in a Geographic Targeting Order (GTO) jurisdiction (currently: major metros — NYC, Miami, LA, etc.) and over the GTO threshold ($300K+), title companies must collect beneficial ownership information on the buyer entity
- **Trust seller:** Verify the trust is validly formed and the trustee has authority to sell. Request a Certificate of Trust, not the full trust document.

**Tools / Resources needed:**
State Secretary of State business search (user must verify). FinCEN GTO list (Claude provides current GTO jurisdictions).

**Data source:**
User-provided entity details + Claude's FinCEN regulatory knowledge.

**Output of this step:**
Entity Legitimacy Checklist with verification steps for each item.

**Cowork behavior:**
PROCEED WITH ANALYSIS AND DRAFTING.

**If this step fails or required data is missing:**
If entity details are not provided, flag as VERIFY and provide the standard entity due diligence checklist.

---

### Step 5: Generate Risk Assessment Report

**What Claude does:**
Compile all findings from Steps 1–4 into the complete Transaction Risk Assessment Report (see Output Format). Assign an overall risk rating: LOW / MEDIUM / HIGH / DO NOT PROCEED. For each finding: state the risk, severity, mechanism of potential harm, and exact remediation step.

**Tools / Resources needed:**
None.

**Data source:**
All prior steps.

**Output of this step:**
Complete Transaction Risk Assessment Report.

**Cowork behavior:**
CONFIRM BEFORE PROCEEDING — if overall rating is HIGH or DO NOT PROCEED, alert the user prominently and ask: "This transaction has HIGH risk indicators. Do you want me to draft a communication to the title company or counterparty requesting resolution of these items before you proceed?"

**If this step fails or required data is missing:**
Deliver partial report with incomplete sections labeled and explain what additional information would complete the assessment.

---

## 📤 OUTPUT FORMAT

**Output type:** Transaction Risk Assessment Report  
**Delivery method:** Returned directly in chat — ready to share with co-counsel, title company, or compliance officer

---

```
TRANSACTION RISK ASSESSMENT — Evykynn
Property:       4821 Maple Ave, Columbus OH 43215
Purchase Price: $285,000
Parties:        Buyer: Maple Capital LLC | Seller: John Smith
Date:           May 10, 2026
Analyst:        AI assistant via Evykynn Skill Library

━━━━━━━━━━━━━━━━ OVERALL RISK RATING ━━━━━━━
⚠️ MEDIUM RISK — Proceed with verification of flagged items

━━━━━━━━━━━━━━━━ FINDINGS SUMMARY ━━━━━━━━━
CRITICAL:   0
HIGH:       1
MEDIUM:     2
LOW:        2

━━━━━━━━━━━━━━━━ DETAILED FINDINGS ━━━━━━━━

[HIGH] Wire Fraud Risk — Email Wire Instructions
Risk: Wire instructions were received via email, not through
a secure title company portal.
Exposure: Wire fraud — misdirected funds are rarely recoverable.
Median wire fraud loss per incident: $179,000 (FBI IC3 2024).
Remediation: Call Midland Title at a phone number obtained from
their official website (not from the email) and verbally confirm
the account name, bank, and last 4 digits of the account number
before initiating any wire.

[MEDIUM] Entity Age — Maple Capital LLC
Risk: Buyer entity registered 45 days ago.
Exposure: Newly formed entities used in fraud transactions are
common. Not definitive — but requires verification.
Remediation: Provide copy of Ohio LLC Operating Agreement and
Certificate of Good Standing. Confirm authorized signatory.

[MEDIUM] Property Price vs. Market
Risk: $285,000 is 12% below Zillow Zestimate of $323,000.
Exposure: Price discount may be legitimate (motivated seller,
as-is condition) or may reflect a problem not yet disclosed.
Remediation: Confirm the reason for the discount in writing
from seller. Conduct thorough physical inspection.

[LOW] POA — Seller Representative
Risk: Seller's adult son claims to be acting as Power of Attorney.
Exposure: POA may be expired, improperly executed, or fraudulent.
Remediation: Obtain copy of the POA document. Title company
must verify it is a durable POA, properly notarized, and the
principal (John Smith) is alive and competent.

[LOW] FinCEN GTO — Columbus Not in GTO List
Status: Columbus, OH is not currently in a FinCEN GTO
jurisdiction. No beneficial ownership reporting required.
Action: No action required.

━━━━━━━━━━━━━━━━ REMEDIATION PRIORITY LIST ━━
1. [HIGH] Verify wire instructions by phone — do today
2. [MEDIUM] Obtain LLC operating agreement and cert of good standing
3. [MEDIUM] Document reason for below-market price in writing
4. [LOW] Verify POA with title company

⚠️ LEGAL DISCLAIMER: This risk assessment was generated by
AI assistant via an automated screening skill. It does not
constitute legal advice. Consult a licensed real estate attorney
for guidance on any HIGH or CRITICAL findings.
```

---

## 🔐 PERMISSIONS & SETUP CHECKLIST

No external permissions or setup required. Attach this file to any Claude.ai chat and type the trigger phrase.

- [ ] **Optional — Secretary of State:** Verify entity status at your state's SOS business search portal.
- [ ] **Optional — County Recorder:** Check deed and lien history at the county recorder or auditor website.
- [ ] **Wire Verification Protocol:** Establish a firm policy: always verify wire instructions by phone before sending any wire. This is the single most effective wire fraud prevention measure.

---

## ✅ QUALITY SELF-CHECK

Before delivering any output, Claude must internally verify every item below:

- [ ] All six risk dimensions were screened — none skipped
- [ ] Every finding has a severity level, specific risk description, and remediation step
- [ ] Overall risk rating is assigned and prominently displayed
- [ ] Wire fraud indicators received special attention — this is the highest-probability loss event
- [ ] ⚠️ LEGAL DISCLAIMER is present
- [ ] No finding is presented as definitive — each is a flag to investigate, not a verdict
- [ ] Output is immediately actionable — remediation steps are specific, not generic

---

## ⚠️ EDGE CASES & ESCALATION RULES

| Scenario | Claude's Exact Response |
|----------|------------------------|
| Multiple CRITICAL indicators found | "⚠️ DO NOT PROCEED: This transaction has multiple CRITICAL risk indicators consistent with [fraud type]. Cease all activity and consult a real estate attorney and your E&O carrier before taking any further steps." |
| User says "the seller seems trustworthy" | "Trustworthiness is not a substitute for verification. Sophisticated fraudsters are specifically trained to appear trustworthy. Please complete the verification steps regardless." |
| Legal risk detected | ⚠️ LEGAL FLAG: "This finding has legal implications. Consult a licensed real estate attorney in [STATE] before proceeding." |
| Transaction is in a FinCEN GTO market | Flag: "⚠️ This transaction is in a FinCEN Geographic Targeting Order jurisdiction. The title company is required to collect and report beneficial ownership information on the buyer entity." |
| Wire has already been sent | Respond: "If you believe you are a victim of wire fraud, immediately contact your bank's wire transfer department, file a complaint with the FBI's IC3 at ic3.gov, and contact local law enforcement. Time is critical — the longer you wait, the lower the recovery probability." |
| Session approaching context limit | Write `_PROGRESS_CHECKPOINT.md` with completed risk dimensions before context is exhausted |

---

## 📖 DOMAIN GLOSSARY

| Term | Definition |
|------|-----------|
| Title Fraud | A scheme in which a fraudster impersonates a property owner and executes a fraudulent deed or sells a property they do not own |
| Wire Fraud | The interception of wire transfer instructions (typically via email compromise) to redirect funds to a fraudulent account |
| FinCEN GTO | FinCEN Geographic Targeting Order — an anti-money laundering tool requiring title companies in designated markets to collect and report beneficial ownership information on all-cash purchases above the GTO threshold |
| Power of Attorney (POA) | A legal document authorizing one person to act on behalf of another in legal or financial matters; durable POA remains valid if the principal becomes incapacitated |
| Beneficial Ownership | The natural persons who ultimately own or control an entity, as defined under FinCEN's Corporate Transparency Act (CTA) effective January 2024 |
| Quitclaim Deed | A deed that conveys whatever interest the grantor has in a property — without warranty of title; commonly used in estate/divorce transfers but a red flag in arms-length sales |
| Chain of Title | The chronological sequence of historical property ownership transfers documented in public records |
| GTO Threshold | The minimum transaction value triggering FinCEN GTO reporting requirements — currently $300,000 in most GTO markets |
| E&O Carrier | Errors and Omissions insurance company — should be notified when a professional discovers a potentially fraudulent transaction they were involved in |

---

*Authored by Evykynn | Real Estate Agentic Automation*

*Maintained as part of RealtySkills by Evykynn. Example dates and figures are illustrative.*
