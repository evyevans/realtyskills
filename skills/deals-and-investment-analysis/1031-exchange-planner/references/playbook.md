# Source playbook

This playbook supplies task procedures and examples. Follow the working rules in the skill entry, verify current jurisdiction-specific claims, and treat examples as illustrative.

# 1031 Exchange Timeline & Replacement Property Screener

This skill plans a complete Section 1031 like-kind exchange — calculating the exact identification and closing deadlines, the minimum replacement property value to fully defer capital gains, the boot amount and tax exposure on any underage, and screening up to three candidate replacement properties against the exchange requirements. Designed for investors, their attorneys, and their CPAs.

## 🧠 SKILL IDENTITY

**WHO this skill is for:**
A real estate investor who is selling an investment property and wants to defer capital gains taxes by reinvesting into a like-kind replacement property under IRC Section 1031. Also: a real estate attorney or CPA advising a client on structuring a tax-deferred exchange. The skill handles the timeline math, the replacement value calculation, and the boot analysis — the three elements most commonly miscalculated.

**WHAT this skill does:**
Produces a complete 1031 Exchange Plan containing: (1) Exact 45-day identification deadline and 180-day closing deadline calculated from the relinquished property closing date; (2) Minimum replacement property value to fully defer all capital gains (equity reinvestment rule); (3) Boot calculation — the taxable portion if the investor acquires less than required; (4) Replacement property screening — up to 3 candidate properties evaluated against exchange requirements; (5) Three-property rule vs. 200% rule analysis; (6) QI (Qualified Intermediary) requirement checklist; (7) Attorney review checklist for complex exchanges.

**WHERE to use this skill:**
Attach to a Claude.ai chat session and provide the relinquished property details, sale price, debt information, and any candidate replacement properties. Claude delivers the complete exchange plan with all calculations shown.

**WHEN to activate this skill:**
Activate the moment the investor decides to sell an investment property and considers a 1031 exchange — ideally before listing, so the QI is engaged before close. At minimum, activate before the relinquished property closes. The 45-day clock starts at closing — there is no extension.

**WHY this skill matters:**
This workflow makes the required inputs and output structure explicit. Its numerical benchmarks are configurable assumptions, not validated performance claims.

**HOW this skill works (Overview):**
Claude calculates the exchange deadlines from the relinquished property closing date, determines the equity reinvestment and debt replacement requirements for a full deferral, calculates boot exposure for any candidate replacement properties that don't meet the full requirements, and produces a prioritized action checklist with exact deadlines and required steps.

---

## 📥 REQUIRED INPUTS

| Input | Format | Source | Required? | Example |
|-------|--------|--------|-----------|---------|
| Relinquished property closing date | MM/DD/YYYY | User provides | Yes | 05/15/2026 |
| Sale price (relinquished property) | Dollar amount | User provides | Yes | $850,000 |
| Adjusted basis (cost + improvements − depreciation) | Dollar amount | User provides | Yes | $320,000 |
| Existing mortgage balance at closing | Dollar amount | User provides | Yes | $280,000 |
| Closing costs on relinquished property | Dollar amount | User provides | No | $45,000 |
| Net equity from relinquished property | Dollar amount | User provides | No | (auto-calculated if not provided) |
| QI engaged? | Yes / No | User provides | No | No — need to find one |
| State of relinquished property | US state | User provides | No | Ohio |
| Candidate replacement properties | Address + price + financing | User provides | No | Up to 3 properties |
| Investor's capital gains tax rate | Federal rate | User provides | No | 20% federal (default for high-income) |

---

## ⚙️ EXECUTION SOP

### Step 1: Calculate Exchange Deadlines

**What Claude does:**
Calculate both mandatory 1031 exchange deadlines from the relinquished property closing date:

**45-Day Identification Deadline:**
Day 1 = Day after relinquished property closes
Day 45 = The exact calendar date by which the investor must identify replacement property in writing to the QI
Calculated date: [Closing date] + 45 calendar days
⚠️ No extensions exist for the 45-day deadline under any circumstances (except presidentially declared disasters — currently none)

**180-Day Closing Deadline:**
Day 180 = The exact calendar date by which the replacement property must close
Calculated date: [Closing date] + 180 calendar days
Note: The 180-day period ends at the earlier of 180 days OR the investor's tax return due date (including extensions) for the year the relinquished property sold — whichever comes first. If the relinquished property closes late in the tax year (after October 17), the tax return deadline may be sooner than 180 days.

**Tax Return Deadline Check:**
If relinquished property closes between October 18 and December 31, 2026: Tax return due April 15, 2027 (extension to October 15, 2027). The 180-day deadline may be earlier than April 15, 2027 — flag this.

**Tools / Resources needed:**
None — calendar arithmetic.

**Data source:**
User-provided closing date.

**Output of this step:**
Exchange Deadline Summary: 45-day date, 180-day date, and any tax return deadline conflict flag.

**Cowork behavior:**
PROCEED WITH ANALYSIS AND DRAFTING.

**If this step fails or required data is missing:**
If closing date is not provided, ask: "What date does (or did) the relinquished property close? The entire exchange timeline is calculated from this date."

> 💡 **Precision Note:** The 45-day and 180-day deadlines run concurrently from the same start date — they do not run sequentially. The 180-day closing deadline is not 180 days after the 45-day identification deadline; both start the day after closing.

---

### Step 2: Calculate Replacement Property Requirements (Full Deferral)

**What Claude does:**
Calculate the minimum replacement property value required to defer 100% of capital gains taxes.

**Step 2A — Calculate the Realized Gain:**
Realized Gain = Sale Price − Adjusted Basis − Selling Costs
= $850,000 − $320,000 − $45,000 = $485,000

**Step 2B — Calculate Net Exchange Equity:**
Net Exchange Equity = Sale Price − Mortgage Balance − Selling Costs
= $850,000 − $280,000 − $45,000 = $525,000

**Step 2C — Full Deferral Requirements (Both must be met):**

Rule 1 — Equal or Greater Value:
Replacement property purchase price ≥ Relinquished property sale price
Minimum: ≥ $850,000 (full deferral) — or accept boot on any amount below

Rule 2 — Equal or Greater Debt:
Replacement property mortgage ≥ Relinquished property mortgage ($280,000)
If replacement debt < $280,000, the difference is "mortgage boot" and is taxable
Exception: If the investor contributes additional cash to compensate for reduced debt, the debt boot can be offset

**Step 2D — Net Boot Calculation:**
If replacement property value < $850,000:
Cash Boot = ($850,000 − replacement price) taxed at capital gains rate
Debt Boot = ($280,000 − replacement mortgage) if not offset by additional cash

**Total Tax Exposure on Boot:**
Boot Amount × Effective Capital Gains Rate (federal + state + NIIT)

**Tools / Resources needed:**
None — arithmetic from user inputs.

**Data source:**
User-provided sale price, basis, mortgage, and selling costs.

**Output of this step:**
Full Deferral Requirements Table + Boot Calculator for any below-requirement scenarios.

**Cowork behavior:**
PROCEED WITH ANALYSIS AND DRAFTING.

**If this step fails or required data is missing:**
If adjusted basis is not provided, flag: "⚠️ Adjusted basis not provided. Your CPA or tax advisor can calculate this from your original purchase price + improvement costs − accumulated depreciation. This is required for accurate boot calculation."

---

### Step 3: Property Identification Rules

**What Claude does:**
Explain the three identification rules and advise the investor which applies to their situation:

**Three-Property Rule (Most Common):**
Investor may identify up to 3 replacement properties of any value. All 3 must be submitted in writing to the QI by Day 45. Investor must ultimately acquire at least 1 identified property.
→ RECOMMEND this rule for investors with 1–3 strong replacement candidates.

**200% Rule:**
Investor may identify more than 3 properties, but the combined fair market value of all identified properties may not exceed 200% of the relinquished property sale price.
200% limit = $850,000 × 2 = $1,700,000 combined FMV
→ RECOMMEND when investor has 4–6 candidate properties or is uncertain which will close.

**95% Rule (Rarely Used):**
Investor may identify any number of properties of any combined value, but must acquire at least 95% of the total identified value.
→ DO NOT recommend without an attorney — extremely difficult to execute.

**Identification Format Requirements:**
The written identification sent to the QI must: identify each property by legal description or address, be signed by the taxpayer, and be received by the QI on or before the 45th day.

**Tools / Resources needed:**
None — regulatory framework.

**Data source:**
User inputs + IRC Section 1031 knowledge.

**Output of this step:**
Identification rule recommendation + required identification format.

**Cowork behavior:**
PROCEED WITH ANALYSIS AND DRAFTING.

**If this step fails or required data is missing:**
Provide all three rules and let the investor and their tax advisor select.

---

### Step 4: Screen Replacement Property Candidates

**What Claude does:**
If the investor provides up to 3 candidate replacement properties, screen each one against the exchange requirements:

For each candidate, evaluate:
1. Price vs. requirement: Is the price ≥ $850,000? If not, calculate boot and tax exposure.
2. Debt level: What is the proposed mortgage? Is it ≥ $280,000? If not, calculate debt boot or cash offset needed.
3. Like-kind qualification: Is the property like-kind (investment real property for investment real property)? Flag any property that might not qualify (personal use property, foreign property, etc.)
4. Timeline feasibility: Can this property realistically close by Day 180?
5. Cash required to close: Down payment + closing costs − exchange proceeds

**Tools / Resources needed:**
None — analysis from user-provided candidate details.

**Data source:**
User-provided candidate property details.

**Output of this step:**
Replacement Property Comparison Table: each candidate with boot exposure, cash required, timeline feasibility, and a RECOMMENDED / MARGINAL / DO NOT USE rating.

**Cowork behavior:**
CONFIRM BEFORE PROCEEDING — present the candidate analysis and ask: "Based on this analysis, do you have a preferred replacement property? I can draft the identification letter for your QI once you've decided."

**If this step fails or required data is missing:**
If no candidates are provided, produce the full requirements summary and note: "Once you identify candidate replacement properties, paste their details and I will screen them against these requirements."

---

### Step 5: QI Checklist and Attorney Review Summary

**What Claude does:**
Produce the QI engagement checklist and the attorney review summary.

**QI Engagement Checklist:**
- [ ] QI must be engaged BEFORE the relinquished property closes — the investor cannot receive exchange proceeds at any point
- [ ] QI is a third party — the investor's attorney, CPA, agent, or employee cannot serve as QI (disqualified person rules)
- [ ] Confirm QI is bonded and insured — exchange proceeds are held in segregated accounts
- [ ] Execute the QI Exchange Agreement before close
- [ ] QI must receive written identification of replacement property on or before Day 45
- [ ] QI funds the replacement property acquisition directly from the exchange account

**Recommended QI resources:** IPX1031, Exeter Exchange, National 1031 Exchange Services (verify current status with your attorney)

**Attorney Review Checklist:**
- [ ] Confirm adjusted basis calculation with CPA before executing exchange
- [ ] Verify like-kind qualification if replacement property type differs from relinquished (e.g., raw land for apartment building)
- [ ] Review state tax implications — some states do not recognize 1031 exchanges (CA recognizes but has "clawback" provisions)
- [ ] Confirm exchange agreement with QI is properly executed
- [ ] Address estate planning implications if the investor is considering holding until death (stepped-up basis planning)

⚠️ LEGAL FLAG: 1031 exchanges involve significant federal and state tax law. This skill produces a planning framework — not tax advice. Consult a licensed CPA and real estate attorney before executing any exchange.

**Tools / Resources needed:**
None.

**Data source:**
All prior steps.

**Output of this step:**
QI checklist + attorney review summary.

**Cowork behavior:**
PROCEED WITH ANALYSIS AND DRAFTING — deliver the complete exchange plan.

---

## 📤 OUTPUT FORMAT

**Output type:** 1031 Exchange Plan  
**Delivery method:** Returned directly in chat — share with CPA, attorney, and QI

---

```
1031 EXCHANGE PLAN — Evy Evans
Relinquished Property: 100 Oak St, Columbus OH
Closing Date:          05/15/2026
Analyst:               AI assistant via Evy Evans Skill Library

━━━━━━━━━━━━━━━━ CRITICAL DEADLINES ━━━━━━━━━
🗓️ 45-Day Identification Deadline:  06/29/2026 (Monday)
🗓️ 180-Day Closing Deadline:        11/11/2026 (Wednesday)
⚠️ Tax Return Deadline Check:  Sale in May 2026 — 180-day deadline
   (11/11) is before tax return due date. No conflict. ✅

━━━━━━━━━━━━━━━━ GAIN & DEFERRAL CALCULATION ━━
Sale Price:             $850,000
Adjusted Basis:        ($320,000)
Selling Costs:          ($45,000)
REALIZED GAIN:          $485,000

Potential Tax Without 1031 (est. 23.8%):  ≈ $115,430

━━━━━━━━━━━━━━━━ FULL DEFERRAL REQUIREMENTS ━━
Replacement property must be:
  Price ≥ $850,000 (equal or greater value)
  Mortgage ≥ $280,000 (equal or greater debt)
  Identified by 06/29/2026 | Closed by 11/11/2026

IDENTIFICATION RULE: Three-Property Rule recommended

━━━━━━━━━━━━━━━━ CANDIDATE SCREENING ━━━━━━━━
Candidate A: 200 Maple Dr — $875,000 — 30% down
  Price: ✅ $875K ≥ $850K minimum
  Debt:  ✅ $612,500 mortgage ≥ $280K minimum
  Boot:  $0 — FULL DEFERRAL achievable
  Cash Needed: $262,500 down + $17,500 closing = $280,000
  Exchange Proceeds Cover: $525,000 → SURPLUS of $245,000
  Rating: ✅ RECOMMENDED

Candidate B: 500 Pine Ave — $820,000 — cash purchase
  Price: ⚠️ $820K < $850K minimum
  Debt:  ❌ $0 mortgage < $280K — creates $280K debt boot
  Cash Boot: $30,000 | Debt Boot: $280,000
  TOTAL BOOT: $310,000 | Estimated Tax: $73,780
  Rating: ❌ DO NOT USE (loses majority of tax benefit)

━━━━━━━━━━━━━━━━ QI CHECKLIST ━━━━━━━━━━━━━━━
⚠️ QI NOT YET ENGAGED — Must engage before 05/15 closing!
☐ Engage QI immediately (IPX1031, Exeter Exchange, or similar)
☐ Execute QI Exchange Agreement before closing
☐ QI receives funds directly at relinquished property closing
☐ Written ID submitted to QI by 06/29/2026

⚠️ LEGAL/TAX DISCLAIMER: This analysis is generated by Claude
an AI assistant. It is a planning tool — not tax or legal advice.
Consult your CPA and real estate attorney before executing.
```

---

## 🔐 PERMISSIONS & SETUP CHECKLIST

No external permissions required for planning.

- [ ] **Engage QI Immediately:** A Qualified Intermediary must be engaged BEFORE the relinquished property closes. Once proceeds touch the investor's hands, the exchange is disqualified.
- [ ] **CPA Consultation:** Confirm adjusted basis and depreciation recapture calculation with your CPA before executing the exchange.
- [ ] **Attorney Review:** Have a real estate and/or tax attorney review the QI agreement and exchange structure before closing.

---

## ✅ QUALITY SELF-CHECK

Before delivering any output, Claude must internally verify every item below:

- [ ] 45-day and 180-day deadlines calculated correctly from the stated closing date (calendar days, no exceptions)
- [ ] Tax return deadline conflict is checked for late-year closings
- [ ] Realized gain calculation shows formula: Sale Price − Adjusted Basis − Selling Costs
- [ ] Both full deferral requirements (equal value AND equal debt) are clearly stated
- [ ] Boot is calculated for any candidate property that doesn't meet full requirements
- [ ] Three-Property Rule vs. 200% Rule recommendation is made
- [ ] ⚠️ LEGAL/TAX DISCLAIMER is present and prominent
- [ ] QI engagement checklist flags whether QI is yet engaged

---

## ⚠️ EDGE CASES & ESCALATION RULES

| Scenario | Claude's Exact Response |
|----------|------------------------|
| QI not yet engaged and closing is imminent | "⚠️ CRITICAL: You have [X] days until closing and no QI engaged. Contact a QI TODAY. The exchange is automatically disqualified if proceeds are received by the investor at closing." |
| Investor wants to use a related party as QI | "⚠️ LEGAL FLAG: Related parties (family members, business associates, your attorney, CPA, or employee) are disqualified persons under IRC § 1031 and cannot serve as QI. Use an independent QI." |
| Investor wants to do a reverse exchange | "A reverse exchange (acquiring replacement property before selling relinquished) is significantly more complex and expensive (Exchange Accommodation Titleholder structure required). Consult a qualified exchange attorney — this skill's standard 1031 framework does not apply to reverse exchanges." |
| Property has been partially used as primary residence | "⚠️ LEGAL FLAG: Mixed-use properties (part investment, part personal use) require allocation of gain between qualifying and non-qualifying portions. Consult a CPA to calculate the 1031-eligible portion." |
| 45-day deadline is missed | "⚠️ CRITICAL: If the 45-day identification deadline has passed without written identification, the exchange is disqualified. The QI must return the exchange funds. Consult your CPA for reporting requirements." |
| State does not recognize 1031 exchanges | "⚠️ LEGAL FLAG: Some states (e.g., California's clawback rule) have specific 1031 regulations. Confirm state tax treatment with a CPA licensed in the relinquished property's state." |

---

## 📖 DOMAIN GLOSSARY

| Term | Definition |
|------|-----------|
| 1031 Exchange | An IRS tax-deferral strategy (IRC Section 1031) allowing an investor to sell an investment property and reinvest proceeds into a like-kind property without paying capital gains tax at the time of sale |
| Qualified Intermediary (QI) | A third-party professional who holds exchange proceeds and facilitates the exchange — required to avoid "constructive receipt" of funds by the investor |
| Like-Kind Property | Real property held for investment or business use exchanged for other real property held for investment or business use — very broadly defined in the US |
| Boot | Any non-like-kind property received in an exchange, including cash, debt relief, or personal property — triggers taxable gain to the extent of boot received |
| Debt Boot | The taxable boot created when the replacement property's mortgage is less than the relinquished property's mortgage — treated as cash received by the investor |
| Adjusted Basis | Original purchase price + capital improvements − accumulated depreciation deductions taken |
| Depreciation Recapture | The portion of gain attributable to prior depreciation deductions — taxed at 25% federal rate (not the lower capital gains rate) |
| Three-Property Rule | The identification rule allowing identification of up to 3 replacement properties of any value |
| 200% Rule | An alternative identification rule allowing identification of any number of properties with total FMV ≤ 200% of the relinquished property's sale price |
| Constructive Receipt | The tax concept that treats funds as received by a taxpayer when they are made available to them — receiving exchange proceeds directly (instead of through a QI) triggers constructive receipt and disqualifies the exchange |

---

*Authored by Evy Evans | Real Estate Agentic Automation*  
*Maintained as part of RealtySkills by Evy Evans. Example dates and figures are illustrative.*
