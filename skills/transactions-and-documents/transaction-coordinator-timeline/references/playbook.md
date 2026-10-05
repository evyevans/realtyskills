# Source playbook

This playbook supplies task procedures and examples. Follow the working rules in the skill entry, verify current jurisdiction-specific claims, and treat examples as illustrative.

# Transaction Coordinator Timeline & Task Manager

This skill ingests the key dates from an executed purchase contract and generates a fully populated transaction timeline — every deadline, every milestone, every required action, assigned to the responsible party, with exact due dates calculated from the contract date. Designed to replace the manual TC spreadsheet with a Claude-generated, contract-specific task list ready for import into Google Sheets, Follow Up Boss, or any TC management platform.

## 🧠 SKILL IDENTITY

**WHO this skill is for:**
A transaction coordinator, team lead, or high-volume independent agent managing 5+ concurrent transactions who needs a complete, accurate timeline generated from a contract in under 5 minutes — without manually calculating every deadline from the contract date.

**WHAT this skill does:**
Produces a complete transaction timeline containing: all contractual deadlines with exact calculated dates, all required actions with the responsible party (buyer / seller / buyer's agent / listing agent / lender / title / TC), a day-by-day milestone calendar for the first 10 days of the transaction, automated reminders for the 7 highest-risk deadlines (those most commonly missed), and a contact directory template for all transaction parties.

**WHERE to use this skill:**
Attach to a Claude.ai chat session or load into a Claude.ai Project used by your TC team. Paste or type the key contract dates and terms. Claude generates the complete timeline in chat — copy directly into Google Sheets or your TC platform.

**WHEN to activate this skill:**
Activate within 24 hours of contract execution — before any deadline has begun to run. The earlier the timeline is built, the more value it provides.

**WHY this skill matters:**
This workflow makes the required inputs and output structure explicit. Its numerical benchmarks are configurable assumptions, not validated performance claims.

**HOW this skill works (Overview):**
Claude extracts the contract execution date, contingency periods, and closing date from the user's inputs. It calculates every deadline by counting calendar or business days (per the contract's specification), assigns each task to the responsible party, and produces the complete timeline document. It flags the 7 highest-risk deadlines with a special alert marker, and builds the first-10-day milestone calendar that the TC must execute immediately after contract.

---

## 📥 REQUIRED INPUTS

| Input | Format | Source | Required? | Example |
|-------|--------|--------|-----------|---------|
| Contract execution date | MM/DD/YYYY | User provides | Yes | 05/10/2026 |
| Closing date | MM/DD/YYYY | User provides | Yes | 06/15/2026 |
| Inspection contingency period | Days (calendar or business) | User provides | Yes | 10 calendar days |
| Financing contingency period | Days | User provides | Yes | 21 calendar days |
| Appraisal contingency period | Days | User provides | No | 21 calendar days |
| Title review period | Days | User provides | No | 5 business days from title commitment |
| EMD due date or days | Days from execution or specific date | User provides | Yes | 3 business days (due 05/14/2026) |
| EMD amount | Dollar amount | User provides | No | $5,000 |
| Lender name | Plain text | User provides | No | First Federal Bank — loan officer Jane Kim |
| Title company | Plain text | User provides | No | Midland Title & Escrow |
| Property address | Full address | User provides | Yes | 4821 Maple Ave, Columbus OH |
| Purchase price | Dollar amount | User provides | No | $285,000 |
| Loan type | Conventional / FHA / VA / Cash | User provides | No | Conventional |
| Special conditions | Any additional contract terms | User provides | No | Seller leaseback for 30 days post-closing |

---

## ⚙️ EXECUTION SOP

### Step 1: Calculate All Deadline Dates

**What Claude does:**
Using the contract execution date as Day 0, calculate the exact calendar date for every standard transaction deadline. Apply these rules:
- **Calendar days:** Count every day including weekends and holidays
- **Business days:** Exclude Saturday, Sunday, and federal holidays; if a deadline falls on a non-business day, the deadline extends to the next business day
- The contract should specify which applies for each period — if not specified, ask the user

**Standard Deadline Calculations:**
- EMD due: Execution date + [stated business days]
- Inspection contingency end: Execution date + [stated calendar or business days]
- Loan application deadline: Typically 5 business days from execution (verify in contract)
- Financing contingency end: Execution date + [stated days]
- Appraisal deadline: Typically within financing contingency period (usually execution + 14 days)
- Title commitment delivery: Typically seller's obligation within 15–20 days
- Title review period: Starts when buyer receives title commitment
- Homeowner's insurance binding date: Typically 5 days before closing
- Final walk-through: Typically 24–48 hours before closing
- Closing disclosure delivery: TRID requires lender deliver CD 3 business days before closing
- Closing date: As stated in contract
- Seller leaseback end (if applicable): Closing date + leaseback period

**Tools / Resources needed:**
None — date arithmetic performed in Claude context using the contract execution date.

**Data source:**
User-provided contract dates and periods.

**Output of this step:**
Complete Deadline Dates Table: every deadline with its calculated calendar date.

**Cowork behavior:**
PROCEED WITH ANALYSIS AND DRAFTING.

**If this step fails or required data is missing:**
If contingency periods are not specified (calendar vs. business days), ask before calculating — this distinction materially changes the deadline date.

> 💡 **Precision Note:** Financing contingency deadlines are the most consequential. Buyers who miss their financing contingency lose their right to terminate and receive EMD refund if the loan falls through. Flag this deadline with maximum prominence.

---

### Step 2: Build the Full Transaction Timeline

**What Claude does:**
Using the calculated dates from Step 1, build the complete timeline with the following structure for each milestone:

| Date | Day # | Milestone | Action Required | Responsible Party | Status |
|------|-------|-----------|-----------------|-------------------|--------|

**Standard milestones to include (in chronological order):**
1. Contract execution date — open transaction file, collect all parties' contact info
2. EMD due — collect and confirm deposit receipt from escrow/title
3. Loan application deadline — verify buyer submitted formal application
4. Inspection contingency period opens — schedule inspector
5. Inspection conducted — flag any issues for negotiation
6. Inspection response deadline — deliver repair request or waiver
7. Seller response to repair request — accept, counter, or reject
8. Inspection contingency end — confirm written waiver or termination
9. Appraisal ordered — confirm lender has ordered appraisal
10. Appraisal received — confirm value meets purchase price
11. Financing contingency end — confirm written loan approval or waiver
12. Title commitment received — begin title review period
13. Title review period end — deliver any title objections
14. Homeowner's insurance binding deadline — buyer binds policy
15. Closing disclosure delivery — lender delivers CD (3 business days before closing)
16. Final walk-through — conduct with buyer and agent
17. Closing — confirm all parties, wiring instructions, and documents
18. Recording — confirm deed and mortgage recorded
19. Commission disbursement — confirm CDA sent to brokerage
20. Post-closing: seller leaseback end (if applicable)

**Tools / Resources needed:**
None — assembled from Step 1 calculations and standard TC workflow.

**Data source:**
Step 1 deadline dates.

**Output of this step:**
Complete Transaction Timeline Table in spreadsheet-ready format.

**Cowork behavior:**
PROCEED WITH ANALYSIS AND DRAFTING.

**If this step fails or required data is missing:**
If a contract term is missing that affects a milestone, note the milestone as TBD and ask the user to provide the missing contract term.

---

### Step 3: Identify and Flag the 7 Highest-Risk Deadlines

**What Claude does:**
From the complete timeline, identify and flag the 7 deadlines with the highest consequence of being missed:

1. **EMD Deadline** — Late EMD means no accepted contract; buyer loses the deal
2. **Inspection Contingency End** — Missing this deadline waives inspection rights
3. **Financing Contingency End** — Missing this means buyer is locked in regardless of loan status
4. **Appraisal Deadline** — A delayed appraisal can trigger financing contingency issues
5. **Title Commitment Delivery** — Seller's obligation; if late, buyer's review period may be compressed
6. **Closing Disclosure 3-Day Rule** — CD must be delivered and acknowledged 3 business days before closing (TRID); if CD changes, the clock restarts
7. **Closing Date** — Any delay in closing requires a signed contract extension — without it, either party may be in breach

For each high-risk deadline, specify: exact date, what happens if missed, and the specific action to take 48 hours before the deadline as a buffer.

**Tools / Resources needed:**
None.

**Data source:**
Step 2 timeline.

**Output of this step:**
🚨 HIGH-RISK DEADLINE ALERT block embedded in the final report.

**Cowork behavior:**
PROCEED WITH ANALYSIS AND DRAFTING.

**If this step fails or required data is missing:**
Identify whichever of the 7 categories are applicable to this transaction type (cash deals have fewer contingencies) and note which are not applicable with the reason.

---

### Step 4: Build First-10-Day Milestone Calendar

**What Claude does:**
Build a day-by-day action calendar for the first 10 days after contract execution — the most action-dense period. For each day, list every action that must be taken and who must take it.

**Day-by-day template (adjust dates to actual contract):**
- **Day 1 (Execution):** Open file; collect all contact info; send introductory emails to all parties; schedule inspector
- **Day 2:** Confirm inspector scheduled; send EMD reminder to buyer's agent
- **Day 3 (Business):** EMD due — confirm receipt with title company
- **Days 1–5:** Buyer submits formal loan application — verify with lender
- **Day 5:** Confirm inspector is scheduled; send lender any HOA docs or disclosures needed
- **Days 3–10:** Inspection conducted — confirm date/time; coordinate access
- **Day 7:** First check-in with lender — loan application status?
- **Day 10 (if applicable):** Inspection contingency end approaching — track response deadline

**Tools / Resources needed:**
None.

**Data source:**
Calculated dates from Step 1.

**Output of this step:**
First-10-Day Action Calendar table.

**Cowork behavior:**
PROCEED WITH ANALYSIS AND DRAFTING.

**If this step fails or required data is missing:**
Produce a generic first-10-day calendar with calculated dates and note any action items that depend on contract terms not yet provided.

---

### Step 5: Generate Complete TC Report

**What Claude does:**
Assemble all outputs from Steps 1–4 into the complete Transaction Coordinator Report (see Output Format), including: full timeline table, high-risk deadline alerts, first-10-day calendar, and the contact directory template.

**Tools / Resources needed:**
None.

**Data source:**
All prior steps.

**Output of this step:**
Complete formatted Transaction Coordinator Report.

**Cowork behavior:**
PROCEED WITH ANALYSIS AND DRAFTING — deliver the complete report.

**If this step fails or required data is missing:**
Deliver partial report with missing sections clearly labeled.

---

## 💻 CODE EXAMPLE

```python
# Transaction Deadline Calculator
# Evy Evans | AI assistant Skill Library | May 2026

from datetime import date, timedelta

FEDERAL_HOLIDAYS_2026 = [
    date(2026, 1, 1),   # New Year's Day
    date(2026, 1, 19),  # MLK Day
    date(2026, 2, 16),  # Presidents Day
    date(2026, 5, 25),  # Memorial Day
    date(2026, 7, 4),   # Independence Day
    date(2026, 9, 7),   # Labor Day
    date(2026, 10, 12), # Columbus Day
    date(2026, 11, 11), # Veterans Day
    date(2026, 11, 26), # Thanksgiving
    date(2026, 12, 25), # Christmas
]

def add_business_days(start_date: date, business_days: int) -> date:
    """Add business days to a date, skipping weekends and federal holidays."""
    current = start_date
    days_added = 0
    while days_added < business_days:
        current += timedelta(days=1)
        if current.weekday() < 5 and current not in FEDERAL_HOLIDAYS_2026:
            days_added += 1
    return current

def calculate_transaction_timeline(
    execution_date: date,
    closing_date: date,
    emd_business_days: int = 3,
    inspection_calendar_days: int = 10,
    financing_calendar_days: int = 21,
    appraisal_calendar_days: int = 14,
) -> dict:
    """Calculate all key transaction deadlines from contract dates."""
    milestones = {
        "Contract Execution": execution_date,
        "EMD Due": add_business_days(execution_date, emd_business_days),
        "Inspection Contingency End": execution_date + timedelta(days=inspection_calendar_days),
        "Appraisal Ordered By": execution_date + timedelta(days=appraisal_calendar_days),
        "Financing Contingency End": execution_date + timedelta(days=financing_calendar_days),
        "Final Walk-Through": closing_date - timedelta(days=1),
        "Closing Disclosure Delivery (Latest)": add_business_days(closing_date, -3),
        "Closing Date": closing_date,
    }
    return {k: v.strftime("%m/%d/%Y (%A)") for k, v in milestones.items()}

# Example:
timeline = calculate_transaction_timeline(
    execution_date=date(2026, 5, 10),
    closing_date=date(2026, 6, 15)
)
# Output: EMD Due: 05/14/2026 (Thursday)
#         Inspection End: 05/20/2026 (Wednesday)
#         Financing End: 05/31/2026 (Sunday → 06/01/2026)
```

---

## 📤 OUTPUT FORMAT

**Output type:** Transaction Coordinator Timeline Report  
**Delivery method:** Returned in chat — copy into Google Sheets, Trello, TC management software, or email to all parties

---

```
TRANSACTION COORDINATOR TIMELINE — Evy Evans
Property:       4821 Maple Ave, Columbus OH 43215
Purchase Price: $285,000 | Loan: Conventional
Execution Date: 05/10/2026 | Closing Date: 06/15/2026
Analyst:        AI assistant via Evy Evans Skill Library

🚨 HIGH-RISK DEADLINES — NEVER MISS THESE
  05/14 (Thu)  EMD DUE — $5,000 to Midland Title
  05/20 (Wed)  INSPECTION CONTINGENCY END
  05/31 (Sun)  FINANCING CONTINGENCY END (→ 06/01 Mon)
  06/12 (Fri)  CLOSING DISCLOSURE DELIVERY (Latest)
  06/14 (Sun)  FINAL WALK-THROUGH
  06/15 (Mon)  CLOSING

FULL TIMELINE
Date        Day# Milestone                    Party         Status
05/10 Sun    D+0  Contract Execution           All          ✅ Done
05/11 Mon    D+1  Open file; contact all       TC           ⬜ Pending
05/13 Wed    D+3B EMD wired to Midland Title   Buyer/BA     ⬜ Pending
05/14 Thu    D+4  Confirm EMD receipt          TC/Title     ⬜ Pending
05/10-15     D+5  Loan application submitted   Buyer/Lender ⬜ Pending
05/14 Thu    D+4  Inspector scheduled          TC/BA        ⬜ Pending
05/17 Sun   D+10  INSPECTION DUE               Inspector    ⬜ Pending
05/20 Wed   D+10B INSPECTION RESPONSE DUE      Buyer/BA     ⬜ Pending
05/24 Sun   D+14  Appraisal ordered by lender  Lender       ⬜ Pending
05/31 Sun   D+21  FINANCING CONTINGENCY END    Buyer/Lender ⬜ Pending
06/01 Mon        Title commitment received     Title/LA     ⬜ Pending
06/08 Mon   D+29  Title review period end      Buyer/BA     ⬜ Pending
06/10 Wed        H/O Insurance bound           Buyer        ⬜ Pending
06/12 Fri        CD delivered by lender        Lender       ⬜ Pending
06/14 Sun        Final walk-through            Buyer/BA     ⬜ Pending
06/15 Mon   D+36  CLOSING                      All          ⬜ Pending

FIRST 10 DAYS — ACTION CALENDAR
Day 1 (05/10): Open file; email all parties; schedule inspector
Day 2 (05/11): Confirm inspector booked; EMD reminder to buyer
Day 3 (05/12): Verify loan app submitted to lender
Day 3B (05/13): EMD wire due — confirm with title by EOD
Day 4 (05/14): Confirm EMD receipt in writing from Midland Title
Day 7 (05/17): Inspection — confirm access; attend if possible
Day 8 (05/18): Review inspection report; plan repair request
Day 10 (05/20): Deliver repair request OR waiver to seller

CONTACTS
Buyer:           [Name] | [Phone] | [Email]
Buyer's Agent:   [Name] | [Phone] | [Email]
Seller:          [Name] | [Phone] | [Email]
Listing Agent:   [Name] | [Phone] | [Email]
Lender:          Jane Kim @ First Federal | [Phone]
Title:           Midland Title & Escrow | [Phone]
Inspector:       [Name] | [Phone] | Scheduled: [Date/Time]
```

---

## 🔐 PERMISSIONS & SETUP CHECKLIST

No external permissions required for timeline generation.

- [ ] **Optional — Google Sheets:** Copy the timeline table into Google Sheets for collaborative tracking and real-time status updates.
- [ ] **Optional — Follow Up Boss / kvCORE:** Manually transfer deadlines into your CRM's task or transaction management module.
- [ ] **Optional — Google Calendar:** Add all high-risk deadlines to a shared Google Calendar with 48-hour advance reminders.

---

## ✅ QUALITY SELF-CHECK

Before delivering any output, Claude must internally verify every item below:

- [ ] All deadline dates have been calculated from the contract execution date — not estimated
- [ ] Calendar vs. business day distinction is correctly applied for each period
- [ ] If a deadline falls on a weekend or holiday, it is correctly extended to the next business day
- [ ] All 7 high-risk deadlines are identified and prominently flagged
- [ ] First-10-day action calendar is populated with specific daily actions
- [ ] Responsible party is assigned to every milestone
- [ ] Output is formatted for copy-paste into a spreadsheet without additional editing

---

## ⚠️ EDGE CASES & ESCALATION RULES

| Scenario | Claude's Exact Response |
|----------|------------------------|
| Closing date is fewer than 21 days from execution | Flag: "⚠️ Closing timeline is compressed. Financing contingency and appraisal deadlines may overlap — verify feasibility with the lender before proceeding." |
| Contract is a cash deal | Remove financing and appraisal contingencies from the timeline; retain inspection, title, and closing milestones. |
| Calendar vs. business days not specified in contract | Ask: "Does your contract specify calendar days or business days for the [inspection/financing] period? This affects the deadline date by 2–4 days." |
| Contract needs extension | Draft an Extension Amendment: "Contract Extension Addendum: The closing date is hereby extended from [original date] to [new date]. All other terms remain unchanged. Agreed by both parties." |
| Legal or compliance issue detected | ⚠️ LEGAL FLAG: "Any modification to contract terms requires a written, signed addendum from all parties. Oral agreements to extend are not enforceable in most states." |
| Session approaching context limit | Write `_PROGRESS_CHECKPOINT.md` noting all calculated dates and milestone status |

---

## 📖 DOMAIN GLOSSARY

| Term | Definition |
|------|-----------|
| EMD | Earnest Money Deposit — funds submitted with a purchase offer to demonstrate buyer intent; typically 1–3% of purchase price |
| Contingency | A condition that must be satisfied for the purchase contract to remain binding |
| Calendar Days | All days including weekends and holidays — the most common counting method for real estate contract periods |
| Business Days | Monday through Friday, excluding federal holidays — used for some specific deadlines (TRID CD delivery) |
| TRID | TILA-RESPA Integrated Disclosure rule — requires lender to deliver Closing Disclosure minimum 3 business days before consummation |
| Final Walk-Through | The buyer's right to inspect the property in its agreed-upon condition immediately before closing |
| CDA | Commission Disbursement Authorization — the form authorizing the title company to pay agent commissions from closing proceeds |
| Transaction Coordinator (TC) | A professional who manages the administrative and deadline-tracking tasks of a real estate transaction from contract to close |

---

*Authored by Evy Evans | Real Estate Agentic Automation*  
*Maintained as part of RealtySkills by Evy Evans. Example dates and figures are illustrative.*
