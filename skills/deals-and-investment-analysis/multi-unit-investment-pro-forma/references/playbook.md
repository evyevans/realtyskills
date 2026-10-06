# Source playbook

This playbook supplies task procedures and examples. Follow the working rules in the skill entry, verify current jurisdiction-specific claims, and treat examples as illustrative.

# Multi-Unit Investment Pro Forma Generator

This skill builds a comprehensive 10-year investment pro forma for multi-unit residential or mixed-use properties (5–100 units). It models current and stabilized NOI, value-add upside, financing scenarios, internal rate of return (IRR), equity multiple, and a full sensitivity analysis — producing institutional-quality analysis from the data you provide.

## 🧠 SKILL IDENTITY

**WHO this skill is for:**
A real estate investor, institutional wholesaler, or real estate business attorney evaluating a multi-family acquisition ranging from a 5-unit apartment building to a 100-unit complex. Specifically: the GP/LP partnership structure, where a General Partner needs to present the deal to Limited Partners or lenders with credible financial projections.

**WHAT this skill does:**
Produces a 10-Year Investment Pro Forma containing: (1) Current vs. stabilized rent roll analysis; (2) Full operating expense waterfall (NOI); (3) Financing structure analysis (senior debt, mezzanine, equity); (4) 10-year income and expense projections with stated growth assumptions; (5) Exit analysis at Year 5, 7, and 10 with projected sale price, net proceeds, and total equity; (6) IRR and equity multiple calculations for the equity investor; (7) DSCR analysis by year; (8) Sensitivity table showing returns under bear/base/bull scenarios; (9) Investment summary suitable for LP presentation.

**WHERE to use this skill:**
Attach to a Claude.ai chat session and provide the property's rent roll, operating expenses, purchase price, and financing terms. Claude's 1M token context window handles large rent roll uploads and full operating statements simultaneously.

**WHEN to activate this skill:**
Activate during the due diligence phase of a multi-family acquisition — after initial LOI is executed and the seller's rent roll and T12 (trailing 12-month operating statement) are received. Use to validate the seller's pro forma and build your own independent underwriting.

**WHY this skill matters:**
This workflow makes the required inputs and output structure explicit. Its numerical benchmarks are configurable assumptions, not validated performance claims.

**HOW this skill works (Overview):**
Claude ingests the rent roll and operating data, reconstructs the current and stabilized NOI from scratch, applies a cap rate to establish independent value, builds the 10-year projection with unit-level rent growth modeling, calculates returns for the equity investor, and delivers the complete pro forma with sensitivity analysis.

---

## 📥 REQUIRED INPUTS

| Input | Format | Source | Required? | Example |
|-------|--------|--------|-----------|---------|
| Property address | Full address | User provides | Yes | 100 Elm Street, Columbus OH |
| Total units | Integer | User provides | Yes | 24 units |
| Rent roll | Unit-by-unit: unit#, bedrooms, current rent, market rent, lease end date | User provides | Yes | See format below |
| Purchase price | Dollar amount | User provides | Yes | $2,400,000 |
| Senior loan terms | Loan amount, rate, amortization | User provides | Yes | $1,680,000 @ 6.5% / 30yr / 5yr balloon |
| Trailing 12-month (T12) expenses | Operating statement | User provides | Yes | Taxes: $28,000, Insurance: $14,400, Utilities: $12,000, Payroll: $22,000, Maintenance: $18,000, Management: $24,000 |
| Value-add plan | Description + timeline | User provides | No | Renovate 12 vacant units at $8K each; raise rents from $850 to $1,050 |
| Target exit cap rate | Percentage | User provides | No | 5.75% |
| Equity invested | Dollar amount | User provides | No | $720,000 (30% down + closing costs) |
| Holding period | Years | User provides | No | 7 years |

**Rent Roll Format:**
Unit | Beds | Current Rent | Market Rent | Lease End
101 | 1BR | $850 | $1,050 | 08/31/2026
102 | 1BR | $875 | $1,050 | 06/30/2026
[continue for all units]

---

## ⚙️ EXECUTION SOP

### Step 1: Reconstruct the Current Rent Roll and Calculate Occupancy

**What Claude does:**
Process the rent roll and calculate:
- Total current monthly rent (occupied units)
- Total vacant unit capacity
- Current physical occupancy rate = occupied units ÷ total units
- Current economic occupancy = actual rent collected ÷ gross potential rent
- Below-market units: units where current rent < market rent, and the upside (market rent − current rent) × 12
- Near-term lease expirations: flag all leases expiring within 90 days (immediate rollover risk or upside opportunity)
- Total Annual Value-Add Upside: Sum of all below-market rent gaps × 12

**Tools / Resources needed:**
None — analysis from user-provided rent roll.

**Data source:**
User-provided rent roll.

**Output of this step:**
Rent Roll Analysis Table: occupancy rates, total current vs. potential income, value-add upside by unit, and near-term lease exposure summary.

**Cowork behavior:**
PROCEED WITH ANALYSIS AND DRAFTING.

**If this step fails or required data is missing:**
If rent roll is not provided in the correct format, ask for it in table format: "Please provide the rent roll as: Unit | Beds | Current Rent | Market Rent | Lease End Date."

---

### Step 2: Reconstruct Operating Expenses and NOI

**What Claude does:**
Build the operating expense schedule from the T12 data provided. Compare to industry benchmarks and flag any line item that deviates significantly from market norms.

**Industry Benchmarks (per unit per year — adjust for market):**
- Taxes: $800–$2,000/unit (verify with T12 and county records)
- Insurance: $300–$700/unit
- Utilities (owner-pays): $600–$1,200/unit (varies: water, electric, gas)
- Property Management: 5–10% of EGI (larger properties get lower rates)
- Payroll (on-site staff): Divide T12 payroll by units — benchmark $300–$700/unit for properties requiring on-site staff
- Maintenance: $500–$1,000/unit
- Landscaping/Exterior: $150–$400/unit
- CapEx Reserve: $400–$600/unit (institutional standard — frequently omitted by sellers)
- Administrative: $150–$300/unit

**Seller Pro Forma Manipulation Check:**
Flag if any T12 line item appears unusually low vs. benchmark. Common seller manipulations:
- Omitting CapEx reserve entirely
- Below-market management fee (seller self-manages but buyer will need PM)
- One-time income items normalized into base income
- Deferred maintenance not reflected in expenses

**NOI (Stabilized):**
Calculate NOI at current rents AND at fully stabilized (all units at market rent, 95% occupancy)

**Tools / Resources needed:**
None — analysis from T12 data.

**Data source:**
User-provided T12 operating statement.

**Output of this step:**
Operating Expense Schedule with per-unit benchmarks, T12 comparison, seller pro forma adjustments (if any), and current + stabilized NOI.

**Cowork behavior:**
PROCEED WITH ANALYSIS AND DRAFTING.

**If this step fails or required data is missing:**
If T12 is not provided, apply industry benchmarks for all expense categories (labeled as estimated) and flag: "⚠️ T12 not provided — expense estimates based on industry benchmarks. Request actual T12 from seller before closing."

> 💡 **Precision Note:** The most reliable red flag in seller-provided pro formas is an expense ratio below 35% of EGI. Legitimate multi-family operating expenses for most markets run 40–55% of EGI. If the seller's pro forma shows 25–30%, they are almost certainly omitting CapEx, management fees, or understating maintenance. Recalculate using the 45% expense ratio rule as a sanity check.

---

### Step 3: Debt Service and Financing Structure Analysis

**What Claude does:**
Build the financing model from the stated loan terms:

**Senior Debt:**
- Loan amount, rate, amortization period
- Annual debt service = monthly P&I × 12
- DSCR (Year 1 current NOI): NOI ÷ Annual Debt Service
- DSCR (Stabilized NOI): Stabilized NOI ÷ Annual Debt Service
- Debt yield = NOI ÷ Loan Amount (lenders target ≥8%)

**Equity:**
- Equity invested = Purchase Price − Loan Amount + Closing Costs (estimate 2% of purchase price)
- Note any mezz debt or preferred equity in the capital stack if provided

**Balloon Risk:**
If a 5-year balloon is present, calculate the projected outstanding balance at balloon date and verify refinancing feasibility: Does the projected NOI at Year 5 produce a DSCR of ≥1.25 at assumed refinance rates?

**Tools / Resources needed:**
None — amortization calculation in Claude context.

**Data source:**
User-provided loan terms + Step 2 NOI.

**Output of this step:**
Financing Structure Table: debt service, DSCR by scenario, debt yield, balloon analysis.

**Cowork behavior:**
PROCEED WITH ANALYSIS AND DRAFTING.

**If this step fails or required data is missing:**
If balloon maturity risk is high (projected NOI insufficient to refinance), flag as CRITICAL: "⚠️ REFINANCE RISK: At Year 5 balloon, projected NOI may not support refinancing at then-current rates. Stress test with +150bps rate increase."

---

### Step 4: Build 10-Year Projection and Return Analysis

**What Claude does:**
Build the 10-year model with the following growth assumptions (adjust if user provides different rates):
- Annual rent growth: 3% per year (or market-specific if provided)
- Value-add rent pop: Applied when renovated units are re-leased (user-provided timeline)
- Annual expense growth: 2.5% per year
- Debt service: Fixed (P&I on amortizing loan)

**For each year 1–10, calculate:**
- EGI (with rent growth + value-add pop schedule)
- Total Operating Expenses
- NOI
- Debt Service
- DSCR
- Cash Flow to Equity
- Cash-on-Cash Return
- Cumulative equity investor cash distributions

**Exit Analysis (Years 5, 7, and 10):**
- Exit property value = Projected NOI at exit year ÷ exit cap rate
- Outstanding loan balance at exit year
- Gross sale proceeds
- Less: selling costs (4% of sale price)
- Less: outstanding loan balance
- Net proceeds to equity
- Total equity investor return = Cumulative distributions + net proceeds
- Equity multiple = Total equity return ÷ Equity invested
- IRR = internal rate of return on equity cash flows (show calculation with annual cash flows)

**Tools / Resources needed:**
None — all calculations within Claude context.

**Data source:**
Steps 1–3 + growth rate assumptions.

**Output of this step:**
10-year projection table + exit analysis at Years 5, 7, 10 + IRR and equity multiple.

**Cowork behavior:**
PROCEED WITH ANALYSIS AND DRAFTING.

**If this step fails or required data is missing:**
Generate the projection with stated assumptions and flag any assumption that materially affects returns.

---

### Step 5: Sensitivity Analysis and LP Investment Summary

**What Claude does:**
Generate a 3×3 sensitivity matrix showing equity multiple and IRR under combinations of:
- **Rent Growth:** Bear (1%), Base (3%), Bull (4%)
- **Exit Cap Rate:** Bear (6.5%), Base (5.75%), Bull (5.25%)

Also produce a one-page LP Investment Summary suitable for partner or investor presentation, containing: deal overview, investment thesis, return targets, key risks, and sponsor information.

**Tools / Resources needed:**
None.

**Data source:**
Step 4 model with varied inputs.

**Output of this step:**
Sensitivity matrix + LP Investment Summary (1 page).

**Cowork behavior:**
CONFIRM BEFORE PROCEEDING — present the complete pro forma and ask: "Would you like me to adjust any assumptions or add additional scenarios before I finalize this as your LP presentation?"

**If this step fails or required data is missing:**
Produce the sensitivity analysis with the available data and note which inputs most materially affect the returns.

---

## 📤 OUTPUT FORMAT

**Output type:** Multi-Unit Investment Pro Forma  
**Delivery method:** Returned directly in chat — ready for LP presentation, lender package, or deal file

---

```
MULTI-UNIT INVESTMENT PRO FORMA — Evykynn
Property:     100 Elm Street, Columbus OH (24-Unit Apartment)
Purchase:     $2,400,000 | Equity: $720,000 | Loan: $1,680,000
Date:         May 10, 2026

CURRENT RENT ROLL SUMMARY
  Occupied:    20 units (83.3% physical occupancy)
  Vacant:       4 units
  Current EGI: $204,000/yr (at 95% economic occupancy)
  Stabilized:  $282,000/yr (all 24 units at market $1,050)
  Value-Add Upside: $78,000/yr (full stabilization)

OPERATING EXPENSES (T12 Adjusted)
  Taxes:        $28,000   ($1,167/unit — within benchmark)
  Insurance:    $14,400   ($600/unit — within benchmark)
  Utilities:    $12,000   ($500/unit)
  Management:   $20,400   ($850/unit — 10% of current EGI)
  Maintenance:  $18,000   ($750/unit)
  CapEx Reserve: $9,600   ($400/unit — ADDED: not in seller T12)
  Admin:         $4,800   ($200/unit)
  Total OpEx:  $107,200

CURRENT NOI:   $96,800  | Cap Rate: 4.03%
STABILIZED NOI: $174,800 | Cap Rate: 7.28% ← value-add thesis

DEBT SERVICE
  Loan: $1,680,000 @ 6.5% / 30yr am = $126,912/yr
  DSCR (current NOI): 0.76 — BELOW threshold (negative cash flow)
  DSCR (stabilized):  1.38 — ✅ HEALTHY at stabilization

10-YEAR HIGHLIGHTS
  Year 3 DSCR:    1.15 (improving with rent growth + value-add)
  Year 5 DSCR:    1.28 — lender refinance threshold crossed
  Year 7 Cash Flow: $52,400/yr
  Year 10 Cash Flow: $68,800/yr

EXIT ANALYSIS (Year 7 — Base Case)
  Exit NOI:        $198,000
  Exit Cap Rate:    5.75%
  Sale Price:      $3,443,478
  Selling Costs:   ($137,739)
  Loan Balance:   ($1,512,000)
  Net to Equity:   $1,793,739
  Cumulative Dist: $142,000
  Total Return:    $1,935,739 on $720,000 invested
  Equity Multiple: 2.69×  |  IRR: 15.3%

SENSITIVITY (Equity Multiple at Year 7)
                Bear Cap (6.5%)  Base (5.75%)  Bull (5.25%)
  Bear Rents (1%):    1.89×          2.24×         2.51×
  Base Rents (3%):    2.31×          2.69×         3.01×
  Bull Rents (4%):    2.53×          2.94×         3.29×

RECOMMENDATION: ✅ BUY (at stabilized value-add execution)
Value creation thesis is strong: current 4.03% cap → stabilized
7.28% cap at full build-out. Negative current cash flow requires
12–18 months of operating reserves ($95,000 minimum recommended).
```

---

## 🔐 PERMISSIONS & SETUP CHECKLIST

No external permissions required.

- [ ] **T12 Verification:** Obtain actual bank statements or tax returns to verify T12 operating figures — never rely solely on seller-provided statements.
- [ ] **Rent Roll Verification:** Verify each tenant's lease against the rent roll — confirm lease terms, deposits held, and any concessions.
- [ ] **Lender Confirmation:** Confirm DSCR requirements with the proposed lender before proceeding — bridge loans, agency (Fannie/Freddie), and bank loans have different requirements.

---

## ✅ QUALITY SELF-CHECK

Before delivering any output, Claude must internally verify every item below:

- [ ] CapEx reserve is included in the expense schedule — not omitted as in seller pro forma
- [ ] DSCR is calculated on current AND stabilized NOI — both scenarios shown
- [ ] IRR is calculated using year-by-year equity cash flows (including exit proceeds)
- [ ] Seller pro forma manipulation check was performed on T12 data
- [ ] Balloon risk is assessed if a term loan is present
- [ ] Sensitivity table covers 9 scenarios (3 rent growth × 3 cap rate)
- [ ] LP summary is clean and suitable for investor presentation
- [ ] All assumptions are stated explicitly — no hidden inputs

---

## ⚠️ EDGE CASES & ESCALATION RULES

| Scenario | Claude's Exact Response |
|----------|------------------------|
| Stabilized NOI doesn't support purchase price | "⚠️ At a [X]% stabilized cap rate, this property is valued above market. The purchase price implies a [Y]% going-in cap — acceptable only if value-add execution is highly certain and well-capitalized." |
| DSCR below 1.0 at current NOI | "⚠️ NEGATIVE CASH FLOW: The property cannot cover its debt service at current rents. This is a heavy value-add play requiring substantial operating reserves and a clear path to stabilization." |
| Balloon maturity risk | ⚠️ FINANCIAL FLAG: "Loan balloons in Year [X]. Projected stabilized NOI must support refinancing at then-current rates. Add a 150–200bps rate stress to verify." |
| Legal or compliance risk (rent control) | ⚠️ LEGAL FLAG: "Multi-family properties in rent-controlled jurisdictions have legally limited rent increase ability. Verify local rent control ordinances — value-add thesis may not be achievable at projected pace." |
| GP/LP structure | "⚠️ SEC DISCLOSURE: GP/LP investment structures may constitute securities offerings subject to federal and state securities laws. Consult a securities attorney before presenting to investors." |
| Session approaching context limit | Write `_PROGRESS_CHECKPOINT.md` with completed model sections |

---

## 📖 DOMAIN GLOSSARY

| Term | Definition |
|------|-----------|
| IRR | Internal Rate of Return — the annualized rate of return that makes the net present value of all cash flows (including exit) equal to zero; the primary return metric for equity investors |
| Equity Multiple | Total equity returned (distributions + exit proceeds) divided by equity invested; e.g., 2.5× means $1 invested returned $2.50 |
| T12 | Trailing 12-Month operating statement — the most recent 12 months of actual income and expenses; the foundation for independent NOI underwriting |
| Rent Roll | A unit-by-unit schedule of tenants, lease terms, current rents, and market rents for a multi-unit property |
| Stabilized NOI | Net Operating Income at full occupancy (typically 95%) with all units at market rent — the "as-if-stabilized" value used to assess value-add upside |
| Debt Yield | NOI divided by total loan amount; lenders use this metric (target ≥8%) alongside DSCR and LTV to assess loan risk |
| Value-Add | A multi-family investment strategy that involves increasing NOI through rent increases (renovations, re-tenanting) and expense reductions, then refinancing or selling at a higher value |
| Bridge Loan | Short-term financing (typically 2–3 years) used during the value-add/stabilization phase before refinancing into permanent (agency) financing |
| Agency Financing | Freddie Mac or Fannie Mae-backed multifamily loans — lower rates and higher LTV than bank loans; typically requires ≥1.25 DSCR and stabilized occupancy |
| Cap Rate Compression | The decline in cap rates over time as more capital competes for the same assets — results in higher property values even without NOI growth |

---

*Authored by Evykynn | Real Estate Agentic Automation*

*Maintained as part of RealtySkills by Evykynn. Example dates and figures are illustrative.*
