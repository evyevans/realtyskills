# Source playbook

This playbook supplies task procedures and examples. Follow the working rules in the skill entry, verify current jurisdiction-specific claims, and treat examples as illustrative.

# License & Disclosure Compliance Tracker

This skill audits a real estate professional's current compliance posture across three dimensions: active license status and renewal deadlines, required continuing education (CE) completion, and transaction-specific disclosure obligations. It produces a prioritized action checklist with exact deadlines, the specific forms required, and the consequences of non-compliance for each item.

## 🧠 SKILL IDENTITY

**WHO this skill is for:**
A brokerage owner managing 10+ licensed agents, a team lead responsible for their team's compliance calendar, or a high-volume independent agent who needs to track CE hours, license renewal dates, E&O insurance renewals, and transaction-specific disclosures across multiple active deals simultaneously — without letting a deadline slip through.

**WHAT this skill does:**
Produces a Compliance Status Report containing: (1) License renewal countdown with exact expiration date, renewal fee, and CE hours completed vs. required; (2) Transaction disclosure checklist for each active deal — which forms are required, which have been delivered, and which are past due; (3) Brokerage-level compliance items (E&O insurance, trust account audit, branch office registration); (4) A red/yellow/green traffic-light status for each compliance item; (5) A calendar of upcoming deadlines in the next 90 days.

**WHERE to use this skill:**
Attach to a Claude.ai chat session or load into a Claude.ai Project for team-wide access. Provide your state, license type, expiration date, CE hours completed, and any active transaction details. Claude produces the full compliance status report in chat.

**WHEN to activate this skill:**
Run monthly for brokerage owners and team leads. Run before opening each new transaction file. Run immediately if you receive any communication from your state licensing board. Run 90 days before any license renewal date.

**WHY this skill matters:**
This workflow makes the required inputs and output structure explicit. Its numerical benchmarks are configurable assumptions, not validated performance claims.

**HOW this skill works (Overview):**
Claude uses the state and license type provided to apply the correct regulatory framework (each state has unique CE requirements, renewal cycles, and disclosure forms). It evaluates each compliance dimension, assigns a traffic-light status, calculates days remaining to each deadline, and delivers a prioritized action checklist with the exact steps required to cure any non-compliant item.

---

## 📥 REQUIRED INPUTS

| Input | Format | Source | Required? | Example |
|-------|--------|--------|-----------|---------|
| State | US state abbreviation | User provides | Yes | OH |
| License type | Salesperson / Broker / Managing Broker | User provides | Yes | Broker |
| License expiration date | MM/DD/YYYY | User provides | Yes | 05/31/2027 |
| CE hours completed this cycle | Number | User provides | Yes | 18 of 30 required |
| CE cycle end date | MM/DD/YYYY | User provides | No | 05/31/2027 |
| Active transactions | List with addresses and contract dates | User provides | No | 3 transactions — see below |
| E&O insurance renewal date | MM/DD/YYYY | User provides | No | 11/15/2026 |
| Trust account last audited | MM/DD/YYYY | User provides | No | 01/15/2026 |
| Agent roster (for brokers) | Names and license numbers | User provides | No | 12 agents — list provided |

---

## ⚙️ EXECUTION SOP

### Step 1: Establish State Regulatory Framework

**What Claude does:**
Based on the user's state, apply the correct regulatory requirements. For each of the 50 states, Claude knows the following (using embedded regulatory knowledge current as of May 2026):

**Key variables by state (examples):**
- **Ohio (OH):** Salesperson renewal: every 3 years; CE required: 30 hours per cycle (including 3 hours core law, 3 hours civil rights); Broker: 30 hours per cycle
- **California (CA):** Salesperson: 4-year renewal; 45 CE hours including 3-hour ethics, 3-hour agency, 3-hour trust fund handling, 3-hour fair housing, 9-hour consumer protection electives; Broker: same
- **Texas (TX):** Salesperson: 2-year renewal; 18 CE hours including specific required courses; Broker: same
- **Florida (FL):** 2-year renewal; 14 CE hours including 3-hour core law; Broker: 60 hours post-license first renewal

Note all mandatory topics, any recent changes to CE requirements, and the specific forms required for each transaction type in that state.

⚠️ IMPORTANT: Claude's regulatory knowledge has a training cutoff. Always verify current requirements with your state licensing board before relying on CE counts or renewal fees for compliance purposes.

**Tools / Resources needed:**
Claude's embedded regulatory knowledge base. For verification: each state's real estate commission website.

**Data source:**
User-provided state + Claude's training data on state licensing requirements.

**Output of this step:**
State regulatory framework summary: renewal cycle, total CE hours required, mandatory course topics, renewal fee (approximate), and any grace period provisions.

**Cowork behavior:**
PROCEED WITH ANALYSIS AND DRAFTING.

**If this step fails or required data is missing:**
If the state is not one Claude has detailed data for, provide the general framework and instruct: "Verify the exact CE requirements with the [STATE] Real Estate Commission at [state commission website]."

---

### Step 2: License Renewal Status Assessment

**What Claude does:**
Using the license expiration date provided, calculate:
- **Days until expiration:** Exact count from today (May 10, 2026)
- **Status:** GREEN (>180 days), YELLOW (90–180 days), RED (<90 days), CRITICAL (expired or <30 days)
- **Renewal window:** Most states allow renewal 90 days before expiration — calculate when the renewal window opens
- **CE hours remaining:** Required total minus hours completed
- **CE completion deadline:** Typically the same as license expiration; flag if different in the user's state
- **Recommended action:** What the user should do now based on their status

For brokerages with multiple agents, flag any agent whose license expires within 90 days.

**Tools / Resources needed:**
None — arithmetic from user inputs and state framework from Step 1.

**Data source:**
User-provided license dates + Step 1 framework.

**Output of this step:**
License Renewal Status Block with traffic-light indicator, days remaining, CE gap, and next action.

**Cowork behavior:**
PROCEED WITH ANALYSIS AND DRAFTING.

**If this step fails or required data is missing:**
If expiration date is not provided, ask for it before proceeding — the entire compliance analysis depends on it.

---

### Step 3: Transaction-Specific Disclosure Audit

**What Claude does:**
For each active transaction provided by the user, generate a disclosure checklist based on state requirements and transaction type. Apply the following standard disclosure framework (adjusted for state-specific requirements):

**Universal Required Disclosures (all states, all transactions):**
- Agency disclosure: Written representation agreement or disclosure of agency relationship — typically required at "first substantive contact"
- Lead-based paint disclosure: Required for all pre-1978 housing (federal — HUD/EPA Form)
- Seller's Property Disclosure Statement (SPDS): Required in most states for listed properties
- HOA disclosure (if applicable): CC&Rs, financials, pending assessments — typically 3–5 business days before closing

**State-Specific Additions (examples):**
- CA: Transfer Disclosure Statement (TDS), Natural Hazard Disclosure (NHD), AVID form, statewide buyer and seller advisories
- TX: Seller's Disclosure of Property Condition, Texas Veterans Land Board information
- FL: Johnson v. Davis disclosure obligations, flood zone disclosure
- NY: Property Condition Disclosure Statement (seller can offer $500 credit to buyer in lieu in some counties)

For each transaction, check whether each required disclosure has been delivered. If transaction dates are provided, flag any disclosure past its required delivery deadline.

**Tools / Resources needed:**
None — regulatory knowledge embedded in Claude's context.

**Data source:**
User-provided transaction details + Step 1 state framework.

**Output of this step:**
Per-transaction disclosure checklist with status (DELIVERED / PENDING / OVERDUE) for each required form.

**Cowork behavior:**
PROCEED WITH ANALYSIS AND DRAFTING.

**If this step fails or required data is missing:**
If no transaction details are provided, produce the standard disclosure checklist template for the user's state that can be applied to any new transaction.

> 💡 **Precision Note:** The agency disclosure requirement is the single most commonly missed disclosure. In most states, it must be delivered at "first substantive contact" — not at contract signing. If the user has been showing properties or discussing price without a written agency disclosure, flag this as a retroactive compliance gap.

---

### Step 4: Brokerage-Level Compliance Items (for Brokers and Brokerage Owners)

**What Claude does:**
If the user's license type is Broker or Managing Broker, add the following brokerage-level compliance items to the audit:

- **E&O Insurance:** Expiration date check + required minimum coverage amounts by state
- **Trust Account / Escrow Account:** Last audit date — most states require annual reconciliation; flag if overdue
- **Branch Office Registration:** If the brokerage has multiple locations, verify each location is registered with the state commission
- **Agent License Status:** Flag any affiliated licensee whose license is expired, inactive, or under investigation (requires agent roster input)
- **Transaction File Retention:** Most states require 3–5 years of transaction file retention; flag if any files are approaching the retention deadline for purging vs. archiving
- **Team Name Compliance:** Many states require team names to include the brokerage name; flag non-compliant team names if provided

**Tools / Resources needed:**
None — state compliance framework from Step 1.

**Data source:**
User-provided brokerage details + Step 1 framework.

**Output of this step:**
Brokerage Compliance Status Table with traffic-light indicators for each item.

**Cowork behavior:**
PROCEED WITH ANALYSIS AND DRAFTING. Skip this step entirely if user is a salesperson (not a broker).

**If this step fails or required data is missing:**
If brokerage details are not provided, note which brokerage-level items could not be audited and provide the template for manual completion.

---

### Step 5: Generate 90-Day Compliance Calendar and Action Checklist

**What Claude does:**
Compile all findings from Steps 1–4 into a prioritized action checklist and 90-day compliance calendar. Assign each item:
- Traffic-light status (RED / YELLOW / GREEN)
- Exact deadline date
- Specific action required (not "renew your license" — but "Submit CE completion proof and renewal application to [STATE] Real Estate Commission at [URL] with $[fee] payment by [date]")
- Consequence of non-compliance stated plainly

**Tools / Resources needed:**
None.

**Data source:**
All prior steps.

**Output of this step:**
Complete Compliance Status Report (see Output Format).

**Cowork behavior:**
PROCEED WITH ANALYSIS AND DRAFTING — deliver the complete report.

**If this step fails or required data is missing:**
Deliver partial report with clearly labeled INCOMPLETE sections.

---

## 📤 OUTPUT FORMAT

**Output type:** Compliance Status Report  
**Delivery method:** Returned directly in chat — ready to share with team members or save to compliance file

---

```
LICENSE & DISCLOSURE COMPLIANCE REPORT — Evykynn
Licensee:       Marcus Johnson, Broker
State:          Ohio
Date:           May 10, 2026
Analyst:        AI assistant via Evykynn Skill Library

━━━━━━━━━━━━━━━━ COMPLIANCE DASHBOARD ━━━━━━━
LICENSE RENEWAL:     🟡 YELLOW — 386 days remaining
CE HOURS:            🔴 RED — 12 hours remaining (18 of 30 complete)
TRANSACTION FILES:   🟡 YELLOW — 2 disclosures pending
E&O INSURANCE:       🟢 GREEN — renews 11/15/2026 (189 days)
TRUST ACCOUNT:       🟡 YELLOW — last audit 01/15/2026 (115 days ago)

━━━━━━━━━━━━━━━━ LICENSE RENEWAL ━━━━━━━━━━━━
Expiration:          05/31/2027
Days Remaining:      386
Renewal Window Opens: 02/28/2027 (90 days prior)
Status:              🟡 YELLOW — schedule CE completion now

CE REQUIREMENTS (Ohio Broker — 30 hours/3-year cycle):
  Completed:  18 hours
  Required:   30 hours
  Remaining:  12 hours
  
  Mandatory Topics Still Needed:
  ✅ Core Law (3 hrs) — COMPLETE
  ✅ Civil Rights (3 hrs) — COMPLETE
  ⬜ Ethics (3 hrs) — INCOMPLETE ← schedule next
  ⬜ Electives (6 hrs remaining)

Action: Complete 12 remaining CE hours before 05/31/2027.
Ohio CE approved providers: Ohio REALTORS®, McKissock Learning,
CE Shop. Verify CE at: myplace.ohio.gov

━━━━━━━━━━━━━━━━ TRANSACTION DISCLOSURES ━━━
Transaction 1 — 4821 Maple Ave (Contracted 04/28/2026)
✅ Agency Disclosure — Delivered 04/28/2026
✅ Lead Paint Disclosure — N/A (built 2004, post-1978)
⚠️ Seller Property Disclosure — PENDING (due within 3 days of contract execution — overdue by 9 days)
✅ HOA Disclosure — N/A (no HOA)

Action: Deliver Seller's Residential Property Disclosure form immediately. Ohio Rev. Code § 5302.30 requires delivery before or at time of contract. Late delivery creates liability exposure.

━━━━━━━━━━━━━━━━ BROKERAGE COMPLIANCE ━━━━━━
E&O Insurance:       Renews 11/15/2026 — Set reminder 10/15/2026
Trust Account Audit: Last: 01/15/2026 — Schedule next by 07/15/2026
Agent License Check: ⚠️ 1 agent license expires 06/30/2026 (51 days)
                     → Contact: Sarah Chen, License #OH-12345

━━━━━━━━━━━━━━━━ 90-DAY ACTION CALENDAR ━━━
May 10:   DELIVER overdue SPDS for 4821 Maple Ave transaction
Jun 30:   Agent Sarah Chen license renewal deadline
Jul 15:   Schedule trust account audit with title company
Oct 15:   Set E&O insurance renewal reminder
Feb 28:   License renewal window opens — submit application

⚠️ DISCLAIMER: Regulatory requirements are sourced from Claude's
training data (current as of May 2026). Verify current requirements
with the Ohio Division of Real Estate at com.ohio.gov/real-estate.
```

---

## 🔐 PERMISSIONS & SETUP CHECKLIST

No external permissions or setup required. Attach this file to any Claude.ai chat and type the trigger phrase.

- [ ] **State Licensing Board:** Bookmark your state's real estate commission website for verification of CE credits and license status.
- [ ] **CE Tracking:** Keep a log of completed CE course certificates. Update the inputs to this skill quarterly.
- [ ] **Team Deployment:** Load into Claude.ai Project so all team members and agents can run their own compliance checks.
- [ ] **Optional — Calendar Integration:** After running this skill, add all deadline dates to Google Calendar with 30-day advance reminders.

---

## ✅ QUALITY SELF-CHECK

Before delivering any output, Claude must internally verify every item below:

- [ ] State regulatory framework was correctly applied for the user's license type
- [ ] Days remaining to each deadline calculated correctly from May 10, 2026
- [ ] Every compliance item has a traffic-light status (RED / YELLOW / GREEN)
- [ ] Transaction disclosure checklist is populated for each transaction provided
- [ ] Every action item includes a specific, actionable next step — not a vague directive
- [ ] ⚠️ DISCLAIMER present noting Claude's training data cutoff for regulatory requirements
- [ ] Any CRITICAL or RED items are surfaced prominently at the top of the report
- [ ] Output is immediately usable as a compliance management tool

---

## ⚠️ EDGE CASES & ESCALATION RULES

| Scenario | Claude's Exact Response |
|----------|------------------------|
| License is expired | Flag as CRITICAL: "⚠️ CRITICAL: Practicing real estate on an expired license is a [STATE] criminal offense. Cease all real estate activities immediately and contact [STATE] Real Estate Commission for reinstatement procedures." |
| CE requirement differs from Claude's knowledge | Flag: "⚠️ Verify CE requirements with [STATE] Real Estate Commission — regulatory requirements change. Claude's knowledge is current as of May 2026." |
| Disclosure deadline missed | Flag as CRITICAL: "⚠️ LEGAL FLAG: The delivery deadline for [DISCLOSURE] has passed. Consult a real estate attorney about your disclosure liability exposure before proceeding." |
| Agent on roster has a disciplinary action | Flag: "⚠️ LEGAL FLAG: A disciplinary action on an affiliated licensee's record may affect your brokerage's E&O coverage. Notify your E&O carrier and consult a real estate attorney." |
| User is in a state with attorney settlement requirement | Flag: "⚠️ [STATE] requires a licensed real estate attorney to conduct or supervise closings. Verify your transaction structure complies with this requirement." |
| Session approaching context limit | Write `_PROGRESS_CHECKPOINT.md` with completed audit sections before context is exhausted |

---

## 📖 DOMAIN GLOSSARY

| Term | Definition |
|------|-----------|
| CE | Continuing Education — state-mandated coursework that licensed real estate professionals must complete to renew their license |
| E&O Insurance | Errors and Omissions insurance — professional liability coverage protecting agents and brokers against claims of negligence or mistakes in their professional services |
| SPDS | Seller's Property Disclosure Statement — a form in which the seller discloses known material defects and conditions affecting the property |
| Agency Disclosure | A written document that informs buyers and sellers of the agent's representation relationship in a transaction |
| Trust Account | A segregated bank account in which a broker holds client funds (earnest money, security deposits) — subject to strict state regulations |
| Managing Broker | The licensee responsible for supervising the activities of affiliated salespersons and overseeing the brokerage's regulatory compliance |
| Lead-Based Paint Disclosure | A federally mandated disclosure (HUD/EPA) required for all residential properties built before 1978 |
| Retroactive Compliance Gap | A compliance obligation that has already been violated in a past or current transaction — requires immediate remediation and possibly legal counsel |

---

*Authored by Evykynn | Real Estate Agentic Automation*

*Maintained as part of RealtySkills by Evykynn. Example dates and figures are illustrative.*
