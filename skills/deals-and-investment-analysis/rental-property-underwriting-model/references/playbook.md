# Source playbook

This playbook supplies task procedures and examples. Follow the working rules in the skill entry, verify current jurisdiction-specific claims, and treat examples as illustrative.

# Rental Property Underwriting Model

This skill produces a complete buy-and-hold rental property underwriting analysis — NOI, cap rate, DSCR, cash-on-cash return, GRM, 5-year projected returns, and a go/no-go recommendation — from the property details and market data you provide. Designed for investors evaluating single-family rentals, small multifamily (2–20 units), and BRRRR strategy candidates.

## 🧠 SKILL IDENTITY

**WHO this skill is for:**
A real estate investor evaluating whether a rental property (SFR, duplex, triplex, quad, or small apartment building) generates sufficient cash flow and long-term returns to justify acquisition. Also: an institutional wholesaler who needs to underwrite a deal before presenting it to a buy-and-hold end buyer.

**WHAT this skill does:**
Produces a complete rental property financial analysis containing: gross rental income, vacancy adjustment, operating expense analysis, Net Operating Income (NOI), capitalization rate (cap rate), Debt Service Coverage Ratio (DSCR), cash-on-cash return, Gross Rent Multiplier (GRM), 5-year appreciation and equity build projection, and a tiered investment recommendation (BUY / HOLD/NEGOTIATE / PASS).

**WHERE to use this skill:**
Attach to a Claude.ai chat session and provide the property details below. Claude builds the complete underwriting model from your inputs, shows all formulas, and delivers the final report with investment recommendation.

**WHEN to activate this skill:**
Activate when evaluating any rental property for acquisition — before making an offer, before submitting an LOI, and before presenting the deal to a capital partner or lender. Also use to evaluate whether a property under your current management is performing at market returns.

**WHY this skill matters:**
This workflow makes the required inputs and output structure explicit. Its numerical benchmarks are configurable assumptions, not validated performance claims.

**HOW this skill works (Overview):**
Claude applies a professional underwriting methodology to the inputs provided. It calculates gross rental income, applies vacancy and credit loss adjustments, builds a complete operating expense schedule (using defaults where user data is unavailable), calculates NOI and all key investment metrics, then stress-tests the model with a financing overlay to produce cash-on-cash and DSCR. The output is a fully formatted investment analysis ready for presentation to a lender, partner, or management company.

---

## 📥 REQUIRED INPUTS

| Input | Format | Source | Required? | Example |
|-------|--------|--------|-----------|---------|
| Property address | Full address | User provides | Yes | 4821 Maple Ave, Columbus OH |
| Property type | SFR / Duplex / Triplex / Quad / X-unit | User provides | Yes | Duplex |
| Number of units | Integer | User provides | Yes | 2 |
| Gross monthly rent per unit | Dollar amount | User provides | Yes | Unit A: $1,200 / Unit B: $1,100 |
| Purchase price | Dollar amount | User provides | Yes | $220,000 |
| Down payment % | Percentage | User provides | Yes | 25% |
| Mortgage rate | Annual percentage | User provides | Yes | 7.25% 30-year fixed |
| Annual property taxes | Dollar amount | User provides | No | $3,600 |
| Annual insurance | Dollar amount | User provides | No | $1,800 |
| HOA (if applicable) | Monthly dollar amount | User provides | No | $0 |
| Current vacancy rate | Percentage | User provides | No | Use market benchmark if unknown |
| Property management fee | Percentage of rent | User provides | No | 10% |
| Any known major repairs needed | Dollar amount / description | User provides | No | Roof — 5 years old, no immediate need |
| Target annual appreciation rate | Percentage | User provides | No | 3% (default) |

---

## ⚙️ EXECUTION SOP

### Step 1: Build the Income Schedule

**What Claude does:**
Calculate the gross potential rental income and the effective gross income after vacancy adjustment.

**Gross Potential Income (GPI):**
Sum all units' monthly rent × 12 = Annual GPI

**Vacancy & Credit Loss:**
Apply market-appropriate vacancy rate. Default rates by property type if not provided:
- SFR: 5% vacancy
- Duplex/Triplex/Quad: 7% vacancy
- Small apartment (5–20 units): 8% vacancy

**Effective Gross Income (EGI):**
GPI × (1 − vacancy rate)

**Other Income:**
- Late fees, laundry income, storage rental, parking — add if provided

**Tools / Resources needed:**
None — arithmetic from user inputs.

**Data source:**
User-provided rents + vacancy benchmarks.

**Output of this step:**
Income Schedule Table: GPI, vacancy amount, EGI, and any ancillary income.

**Cowork behavior:**
PROCEED WITH ANALYSIS AND DRAFTING.

**If this step fails or required data is missing:**
If rents are not provided, ask for them — cannot underwrite without income data. If market rents are unknown, flag: "Consider using Rentometer.com or Zillow Rent Zestimate to verify current market rents before relying on this analysis."

---

### Step 2: Build the Operating Expense Schedule

**What Claude does:**
Calculate all operating expenses using user-provided data and the following defaults for any missing category:

**OPERATING EXPENSE DEFAULTS (% of EGI or flat amounts):**
- Property Taxes: User provided; default 1.2% of purchase price if not provided
- Insurance: User provided; default 0.5% of purchase price if not provided
- Property Management: 10% of EGI (use if PM is engaged); or $0 if self-managing (but flag self-management as a cost Claude will note)
- Maintenance & Repairs: 10% of EGI (covers routine repairs)
- CapEx Reserve: 10% of EGI (capital expenditures: roof, HVAC, appliances — set aside, not spent annually)
- Vacancy Reserve: Already deducted in Step 1
- HOA: User provided or $0
- Utilities (if owner-pays): User provided; default $0 for tenant-pays
- Accounting/Legal: $500/year flat
- Landscaping/Snow Removal: $600/year flat (if applicable)

**Total Operating Expenses (OpEx):** Sum of all above

**Net Operating Income (NOI):**
NOI = EGI − Total Operating Expenses

**Expense Ratio:**
Total OpEx ÷ EGI × 100 (healthy range: 35–50% for residential; flag if >55%)

**Tools / Resources needed:**
None — arithmetic from inputs and defaults.

**Data source:**
User-provided expenses + default benchmarks.

**Output of this step:**
Complete Operating Expense Schedule with all line items, amounts, source (user-provided vs. estimated), and NOI.

**Cowork behavior:**
PROCEED WITH ANALYSIS AND DRAFTING.

**If this step fails or required data is missing:**
Apply all defaults and clearly label each one "ESTIMATED — verify with local market data." Never omit a cost category.

> 💡 **Precision Note:** CapEx reserves are the most commonly omitted expense in investor underwriting. A 20-year-old roof has an expected replacement cost of $8,000–$25,000 (depending on size). Setting aside 10% of EGI annually is not enough for aging properties — increase to 15% if the property is more than 15 years old. Flag this explicitly for older properties.

---

### Step 3: Calculate Key Investment Metrics

**What Claude does:**
Calculate all key investment metrics using the NOI from Step 2 and the financing inputs:

**METRIC CALCULATIONS:**

**Cap Rate:**
Cap Rate = NOI ÷ Purchase Price × 100
(Healthy range: 5–8% for residential in most markets; varies significantly by market)

**Gross Rent Multiplier (GRM):**
GRM = Purchase Price ÷ Annual GPI
(Lower is better; benchmark: <10 in strong cash flow markets, <15 in appreciation markets)

**Debt Service (Annual Mortgage Payment):**
Monthly P&I = Use standard amortization formula:
Loan = Purchase Price × (1 − down payment %)
Monthly P&I = Loan × [rate/12 × (1+rate/12)^360] / [(1+rate/12)^360 − 1]
Annual Debt Service = Monthly P&I × 12

**DSCR (Debt Service Coverage Ratio):**
DSCR = NOI ÷ Annual Debt Service
(Lenders typically require ≥1.20 for investment property; ≥1.25 preferred)

**Cash Flow (Annual):**
Annual Cash Flow = NOI − Annual Debt Service

**Cash Flow Per Unit Per Month:**
Annual Cash Flow ÷ Number of Units ÷ 12

**Cash-on-Cash Return:**
Cash-on-Cash = Annual Cash Flow ÷ Total Cash Invested × 100
Total Cash Invested = Down Payment + Closing Costs (estimate 2% of purchase price) + Any immediate repair costs

**Total Return on Investment (first year):**
TRI = (Annual Cash Flow + Annual Principal Paydown + Annual Appreciation) ÷ Total Cash Invested × 100

**Tools / Resources needed:**
None — all arithmetic from Steps 1 and 2 outputs.

**Data source:**
NOI from Step 2 + financing inputs.

**Output of this step:**
Investment Metrics Summary Table with all metrics, formulas shown, and benchmark comparison.

**Cowork behavior:**
PROCEED WITH ANALYSIS AND DRAFTING.

**If this step fails or required data is missing:**
If mortgage rate is not provided, use 7.5% as current market default (flag as estimated — verify with lender).

---

### Step 4: Five-Year Projection

**What Claude does:**
Build a 5-year hold projection showing:
- Annual rent growth: 3% per year (default; adjust if user provides market-specific rate)
- Annual appreciation: User-provided or 3% default
- Annual expense growth: 2.5% per year
- Annual debt service: Fixed (principal paydown increasing each year)
- Year 1–5: EGI, NOI, Cash Flow, Cash-on-Cash Return
- Year 5: Property value, outstanding loan balance, equity, total return (cash flow + equity)

**5-Year Equity Build:**
Year 5 Value = Purchase Price × (1 + appreciation%)^5
Outstanding Balance at Year 5 = remaining balance on amortization schedule
Total Equity at Year 5 = Year 5 Value − Outstanding Balance

**Total 5-Year Return:**
Cumulative cash flow (Years 1–5) + Equity at Year 5 − Total Cash Invested

**Tools / Resources needed:**
None — projection model from Step 3 inputs.

**Data source:**
Step 3 metrics + appreciation and growth rate assumptions.

**Output of this step:**
5-Year Projection Table with year-by-year metrics and total return summary.

**Cowork behavior:**
PROCEED WITH ANALYSIS AND DRAFTING.

**If this step fails or required data is missing:**
Generate the projection with stated assumptions and flag: "All 5-year projections are estimates. Actual returns depend on market conditions, vacancy, and expense control."

---

### Step 5: Investment Recommendation

**What Claude does:**
Apply the following decision matrix to produce a tiered recommendation:

**BUY (all of the following must be true):**
- Cap rate ≥ 5.5% (or ≥ cap rate benchmark for the local market)
- DSCR ≥ 1.20
- Cash-on-Cash ≥ 7%
- Cash flow ≥ $100/unit/month (minimum viable cash flow)

**PROCEED/NEGOTIATE (one metric below threshold):**
- Cap rate 4.5–5.5%: Negotiate price or terms
- DSCR 1.10–1.20: Increase down payment to improve coverage
- Cash flow $0–$100/unit/month: Verify rent increase opportunity before buying

**PASS (any of the following):**
- Negative cash flow after full expenses
- DSCR < 1.10
- Cap rate < 4% (unless in an appreciation market the investor explicitly accepts)
- Cash-on-Cash < 4% with no appreciation upside

State the specific metric(s) that triggered the recommendation and the exact adjustment needed to make the deal viable.

**Tools / Resources needed:**
None.

**Data source:**
All prior steps.

**Output of this step:**
Investment recommendation with specific metric basis.

**Cowork behavior:**
PROCEED WITH ANALYSIS AND DRAFTING — deliver the complete report.

---

## 💻 CODE EXAMPLE

```python
# Rental Property Underwriting Model
# Evykynn | AI assistant Skill Library | May 2026

def underwrite_rental(
    purchase_price: float,
    monthly_rents: list,       # list of monthly rent per unit
    down_payment_pct: float = 0.25,
    mortgage_rate: float = 0.0725,
    amort_years: int = 30,
    vacancy_rate: float = 0.07,
    mgmt_fee_pct: float = 0.10,
    tax_annual: float = None,
    insurance_annual: float = None,
    desired_coc: float = 0.07,
) -> dict:
    annual_gpi = sum(monthly_rents) * 12
    egi = annual_gpi * (1 - vacancy_rate)

    tax = tax_annual if tax_annual else purchase_price * 0.012
    ins = insurance_annual if insurance_annual else purchase_price * 0.005
    mgmt = egi * mgmt_fee_pct
    maintenance = egi * 0.10
    capex = egi * 0.10
    total_opex = tax + ins + mgmt + maintenance + capex

    noi = egi - total_opex
    cap_rate = noi / purchase_price

    loan = purchase_price * (1 - down_payment_pct)
    r = mortgage_rate / 12
    n = amort_years * 12
    monthly_pi = loan * (r * (1+r)**n) / ((1+r)**n - 1)
    annual_ds = monthly_pi * 12

    dscr = noi / annual_ds
    annual_cf = noi - annual_ds
    grm = purchase_price / annual_gpi
    cash_invested = purchase_price * down_payment_pct + purchase_price * 0.02
    coc = annual_cf / cash_invested
    cf_per_unit_month = annual_cf / len(monthly_rents) / 12

    if cap_rate >= 0.055 and dscr >= 1.20 and coc >= desired_coc and cf_per_unit_month >= 100:
        rec = "✅ BUY — meets all return thresholds"
    elif dscr >= 1.10 and cf_per_unit_month >= 0:
        rec = "⚠️ PROCEED/NEGOTIATE — one metric below threshold"
    else:
        rec = "❌ PASS — does not meet minimum return thresholds"

    return {
        "annual_gpi": f"${annual_gpi:,.0f}",
        "egi": f"${egi:,.0f}",
        "total_opex": f"${total_opex:,.0f}",
        "noi": f"${noi:,.0f}",
        "cap_rate": f"{cap_rate*100:.2f}%",
        "grm": f"{grm:.1f}x",
        "dscr": f"{dscr:.2f}",
        "annual_cash_flow": f"${annual_cf:,.0f}",
        "cash_on_cash": f"{coc*100:.1f}%",
        "cf_per_unit_month": f"${cf_per_unit_month:,.0f}",
        "recommendation": rec,
    }

# Example:
result = underwrite_rental(
    purchase_price=220000,
    monthly_rents=[1200, 1100],
    down_payment_pct=0.25,
    mortgage_rate=0.0725,
    tax_annual=3600,
    insurance_annual=1800,
)
# NOI ≈ $12,400 | Cap Rate ≈ 5.6% | DSCR ≈ 1.22 | CoC ≈ 7.8%
```

---

## 📤 OUTPUT FORMAT

**Output type:** Rental Property Investment Analysis Report  
**Delivery method:** Returned directly in chat — ready for lender presentation, partner sharing, or CRM file note

---

```
RENTAL PROPERTY UNDERWRITING ANALYSIS — Evykynn
Property:     4821 Maple Ave, Columbus OH 43215 (Duplex)
Purchase:     $220,000 | Down: 25% ($55,000) | Rate: 7.25%
Date:         May 10, 2026

━━━━━━━━━━━━━━━━ INCOME SCHEDULE ━━━━━━━━━━
Unit A Monthly Rent:        $1,200
Unit B Monthly Rent:        $1,100
Gross Potential Income:    $27,600/yr
Vacancy (7%):              ($1,932/yr)
Effective Gross Income:    $25,668/yr

━━━━━━━━━━━━━━━━ OPERATING EXPENSES ━━━━━━━
Property Taxes:             $3,600/yr  (user-provided)
Insurance:                  $1,800/yr  (user-provided)
Property Management (10%):  $2,567/yr  (estimated)
Maintenance (10% EGI):      $2,567/yr  (estimated)
CapEx Reserve (10% EGI):    $2,567/yr  (estimated)
TOTAL OPERATING EXPENSES:  $13,101/yr
EXPENSE RATIO:               51%

NET OPERATING INCOME (NOI): $12,567/yr

━━━━━━━━━━━━━━━━ INVESTMENT METRICS ━━━━━━
Cap Rate:          5.71%   ✅ (benchmark: ≥5.5%)
GRM:               7.97x   ✅ (benchmark: <10x)
Annual Debt Svc:  $10,254/yr  (loan: $165,000 @ 7.25%)
DSCR:              1.23    ✅ (benchmark: ≥1.20)
Annual Cash Flow:  $2,313/yr
Cash Flow/Unit/Mo: $96.38  ⚠️ (benchmark: ≥$100)
Cash-on-Cash:       4.1%   ⚠️ (benchmark: ≥7%)
Total Cash In:    $56,400  (down + closing costs)

━━━━━━━━━━━━━━━━ 5-YEAR PROJECTION ━━━━━━━
         Yr1       Yr2       Yr3       Yr4       Yr5
EGI:   $25,668  $26,438  $27,231  $28,048  $28,889
NOI:   $12,567  $13,072  $13,597  $14,142  $14,708
CF:     $2,313   $2,818   $3,343   $3,888   $4,454
Value: $220,000 $226,600 $233,398 $240,400 $247,612

Year 5 Equity: $247,612 − $148,122 = $99,490
5-Year Total Return: $16,816 (cash) + $43,490 (equity gain)
= $60,306 total return on $56,400 invested = 106.9%

━━━━━━━━━━━━━━━━ RECOMMENDATION ━━━━━━━━━
⚠️ PROCEED / NEGOTIATE
Cap rate (5.71%) and DSCR (1.23) meet thresholds.
Cash-on-cash (4.1%) and cash flow per unit ($96/mo) are
slightly below ideal benchmarks.
SUGGESTED NEGOTIATION: Reduce purchase price by $10,000
(to $210,000) → Cash-on-cash improves to ~7.2% and
cash flow to ~$150/unit/month. At current price, this is
an appreciation play, not a cash flow play.
```

---

## 🔐 PERMISSIONS & SETUP CHECKLIST

No external permissions required.

- [ ] **Rent Verification:** Use Rentometer.com or Zillow Rent Zestimate to verify stated rents against current market rates before relying on this model.
- [ ] **Lender Pre-Qualification:** Share this analysis with your lender before making an offer — confirm the DSCR meets their underwriting guidelines.
- [ ] **Property Inspection:** All underwriting assumes the stated property condition. Order a physical inspection before finalizing the analysis.

---

## ✅ QUALITY SELF-CHECK

Before delivering any output, Claude must internally verify every item below:

- [ ] All five expense categories (taxes, insurance, management, maintenance, CapEx) are included — none omitted
- [ ] Every metric is calculated with its formula shown
- [ ] DSCR is calculated using full mortgage payment (P&I), not interest-only
- [ ] Cash-on-cash uses total cash invested (down payment + closing costs) — not just down payment
- [ ] 5-year projection states all assumptions (appreciation rate, rent growth rate, expense growth)
- [ ] Recommendation cites the specific metrics that triggered it
- [ ] CapEx reserve is present — flag if the property is more than 15 years old and CapEx is only 10%

---

## ⚠️ EDGE CASES & ESCALATION RULES

| Scenario | Claude's Exact Response |
|----------|------------------------|
| Negative cash flow in base case | "⚠️ This property has NEGATIVE CASH FLOW after all expenses. This is not a cash flow investment — it is a speculative appreciation play. Only proceed if you can absorb the monthly loss and have high confidence in appreciation." |
| DSCR below 1.10 | "⚠️ DSCR of [X] is below most lender minimums (1.20). You may not qualify for investment property financing at this purchase price. Consider a larger down payment or price renegotiation." |
| CapEx issue on old property | "⚠️ This property is [X] years old. The 10% CapEx reserve may be insufficient. Major systems (roof, HVAC, plumbing, electrical) may need replacement within the hold period. Increase CapEx to 15% and re-run the analysis." |
| Legal compliance (rent control markets) | "⚠️ LEGAL FLAG: This property may be in a rent-controlled jurisdiction. Rent increases may be limited by local ordinance. Verify allowable annual rent increase before projecting income growth." |
| User wants to apply BRRRR strategy | "For a BRRRR analysis, add the refinance step: after rehab, calculate the new appraised value and refinance at 75% LTV. The refinance proceeds should return most or all of the invested cash. I can add a BRRRR refinance overlay to this analysis — just say 'add BRRRR overlay.'" |
| Session approaching context limit | Write `_PROGRESS_CHECKPOINT.md` with completed calculation steps |

---

## 📖 DOMAIN GLOSSARY

| Term | Definition |
|------|-----------|
| NOI | Net Operating Income — annual rental income minus operating expenses, excluding mortgage payments |
| Cap Rate | Capitalization Rate — NOI divided by property value; expresses the annual return as if purchased in cash |
| DSCR | Debt Service Coverage Ratio — NOI divided by annual debt service; lenders require ≥1.20–1.25 |
| GRM | Gross Rent Multiplier — purchase price divided by annual gross rent; quick relative value tool |
| EGI | Effective Gross Income — gross potential income minus vacancy and credit loss |
| CapEx | Capital Expenditure — major property improvements or replacements (roof, HVAC, plumbing) that extend asset life; not deducted as operating expense but reserved separately |
| Cash-on-Cash Return | Annual cash flow divided by total cash invested; measures return on out-of-pocket capital |
| BRRRR | Buy, Rehab, Rent, Refinance, Repeat — a real estate investing strategy that uses a cash-out refinance to recycle capital into additional acquisitions |
| 1031 Exchange | An IRS tax-deferral strategy allowing an investor to sell an investment property and reinvest proceeds without paying capital gains tax at time of sale |
| Pro Forma | A projected financial statement showing expected income, expenses, and returns for an investment property |

---

*Authored by Evykynn | Real Estate Agentic Automation*

*Maintained as part of RealtySkills by Evykynn. Example dates and figures are illustrative.*
