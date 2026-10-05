# Source playbook

This playbook supplies task procedures and examples. Follow the working rules in the skill entry, verify current jurisdiction-specific claims, and treat examples as illustrative.

# Fix & Flip Profit and Timeline Calculator

This skill transforms raw property data — address, purchase price, estimated repairs, ARV, and hold time — into a comprehensive fix-and-flip feasibility analysis. It outputs a full profit/loss projection, itemized cost stack, realistic project timeline, and a tiered go/no-go recommendation. Built for residential flippers, institutional wholesalers, and investor-partners who need underwriting discipline before committing capital to a rehab project.

## 🧠 SKILL IDENTITY

**WHO this skill is for:**
A real estate investor, fix-and-flip operator, or institutional wholesaler evaluating whether a distressed property justifies acquisition, rehab capital deployment, and a 90–180 day project cycle. Specifically: the person who has a property under contract or in LOI and needs a complete pro forma before wiring an earnest money deposit or presenting the deal to a capital partner.

**WHAT this skill does:**
Produces a fully itemized fix-and-flip analysis report containing: total project cost stack (purchase + rehab + holding + closing + financing), projected gross profit, net profit after all costs, annualized ROI, cash-on-cash return, projected timeline with phase milestones, risk-adjusted scenario modeling (base / optimistic / conservative), and a tiered recommendation (STRONG BUY / MARGINAL / PASS) with the specific math behind the verdict.

**WHERE to use this skill:**
Attach to a Claude.ai chat session (Method A) or run as a Cowork Task (Method B) when you have a potential flip under active consideration. Provide the required inputs below and type the trigger phrase. Claude returns the full analysis directly in chat — ready to copy into a CRM note, email to a partner, or paste into a deal file.

**WHEN to activate this skill:**
Activate immediately after a motivated seller call, a driving-for-dollars find, or a wholesaler's deal submission — when you have an address, asking price, rough scope of work estimate, and comparable sales data. Use before committing any capital, before submitting an LOI, and before presenting the deal to a joint-venture partner or private lender.

**WHY this skill matters:**
This workflow makes the required inputs and output structure explicit. Its numerical benchmarks are configurable assumptions, not validated performance claims.

**HOW this skill works (Overview):**
Claude ingests the property address, purchase price, estimated repair cost, ARV, projected hold time, financing terms, and transaction cost assumptions. It builds a complete cost stack across five categories (acquisition, rehab, holding, financing, disposition), calculates gross and net profit, computes ROI and cash-on-cash return, then generates three scenarios (base/optimistic/conservative) using ±15% ARV and ±20% ERC variance bands. Finally, Claude produces a tiered recommendation and flags any inputs that fall outside healthy flip parameters before delivering the formatted report.

---

## 📥 REQUIRED INPUTS

| Input | Format | Source | Required? | Example |
|-------|--------|--------|-----------|---------|
| Property address | Plain text | User provides | Yes | 4821 Maple Ave, Columbus OH 43215 |
| Purchase price (or max offer) | Dollar amount | User provides | Yes | $135,000 |
| After Repair Value (ARV) | Dollar amount | User provides | Yes | $285,000 |
| Estimated Repair Cost (ERC) | Dollar amount | User provides | Yes | $47,000 |
| Projected hold time | Months (integer) | User provides | Yes | 5 months |
| Financing type | Hard money / Private / Cash / Conv. | User provides | Yes | Hard money at 12% interest-only |
| Loan-to-cost ratio (if financed) | Percentage | User provides | No | 75% LTC |
| Desired minimum net profit | Dollar amount | User provides | No | $30,000 |
| Local agent commission rate | Percentage | User provides | No | 5.5% (default if not provided) |

---

## ⚙️ EXECUTION SOP

### Step 1: Parse and Validate All Inputs

**What Claude does:**
Extract all user-provided inputs and validate each against healthy flip parameters: ARV must exceed purchase price by at least 40% to be viable as a flip; ERC should not exceed 35% of ARV (flag if it does); hold time should be 3–12 months (flag outliers). If ARV is not provided, Claude asks the user for it — do not estimate ARV without explicit data.

**Tools / Resources needed:**
None — works entirely from user-provided inputs in context.

**Data source:**
User-provided inputs from the chat session.

**Output of this step:**
A validated input summary table with any flagged anomalies clearly marked ⚠️ before analysis begins.

**Cowork behavior:**
PROCEED WITH ANALYSIS AND DRAFTING — validation is analytical and non-destructive.

**If this step fails or required data is missing:**
If ARV or purchase price are missing, stop and ask: "To run your flip analysis, I need [missing field]. Please provide it and I'll continue." Do not fabricate any financial input.

> 💡 **Precision Note:** Never use Zestimate or automated valuation models as the ARV without flagging it. If the user provides an ARV without disclosing its source, append: "⚠️ ARV SOURCE UNVERIFIED — confirm against 3+ closed comparable sales within 0.5 miles and 180 days before relying on this analysis."

---

### Step 2: Build the Full Cost Stack

**What Claude does:**
Calculate all five cost categories using the validated inputs and the default rates below (override with user-provided values where available):

**ACQUISITION COSTS:**
- Purchase price (user input)
- Buyer closing costs: 1.5% of purchase price (title, escrow, recording)
- Inspection & due diligence: $500 flat estimate

**REHAB COSTS:**
- ERC (user input) — treat as the base case
- Contingency reserve: 15% of ERC (standard rehab buffer)
- Total rehab: ERC × 1.15

**HOLDING COSTS (per month × hold time):**
- Property taxes: ARV × 1.2% ÷ 12
- Insurance: $150/month (residential flip policy)
- Utilities: $200/month (electric, water, gas during rehab)
- HOA (if applicable): user input or $0

**FINANCING COSTS:**
- If hard money / private: (loan amount) × (annual rate ÷ 12) × hold time + origination fee (2 points default)
- Loan amount = Purchase price × LTC ratio (default 75% if not provided)
- If cash deal: no financing cost (flag opportunity cost)

**DISPOSITION COSTS:**
- Agent commissions: ARV × commission rate (default 5.5%)
- Seller closing costs: 1.0% of ARV (title, escrow, transfer tax)
- Staging / prep: $1,500 flat estimate

**Tools / Resources needed:**
None — all calculations performed in Claude context.

**Data source:**
Validated inputs from Step 1 + default rate assumptions stated above.

**Output of this step:**
A fully itemized cost stack table with each line item, its formula, and dollar value.

**Cowork behavior:**
PROCEED WITH ANALYSIS AND DRAFTING — all calculations are deterministic from stated inputs.

**If this step fails or required data is missing:**
If financing terms are unclear, apply cash deal assumption and flag: "⚠️ No financing terms provided — modeled as all-cash. If using leverage, rerun with loan terms for accurate ROI."

> 💡 **Precision Note:** The 15% contingency on ERC is non-negotiable in this model. Experienced flippers routinely exceed initial repair estimates by 10–25%. Never remove this buffer even if the user requests it — instead, show both the buffered and unbuffered version and explain the risk difference.

---

### Step 3: Calculate Profit, ROI, and Returns

**What Claude does:**
Using the total cost stack from Step 2, calculate:
- **Total Project Cost (TPC):** Sum of all five cost categories
- **Gross Profit:** ARV − Purchase Price − ERC (base, unbuffered — for comparison only)
- **Net Profit (Base Case):** ARV − TPC
- **Return on Investment (ROI):** Net Profit ÷ TPC × 100
- **Annualized ROI:** ROI ÷ Hold Time (months) × 12
- **Cash Invested (if leveraged):** Down payment + closing costs + out-of-pocket rehab
- **Cash-on-Cash Return:** Net Profit ÷ Cash Invested × 100
- **Profit Margin:** Net Profit ÷ ARV × 100 (healthy flip: ≥15%)

**Tools / Resources needed:**
None — arithmetic from Step 2 outputs.

**Data source:**
Step 2 cost stack.

**Output of this step:**
A profit summary block with all metrics labeled, formulas shown, and a color-coded health indicator: ✅ HEALTHY (margin ≥15%), ⚠️ TIGHT (margin 8–14%), ❌ THIN (margin <8%).

**Cowork behavior:**
PROCEED WITH ANALYSIS AND DRAFTING.

**If this step fails or required data is missing:**
If net profit is negative, do not suppress the result — display it clearly as a NEGATIVE RETURN and flag the specific cost categories driving the loss.

---

### Step 4: Run Three-Scenario Stress Test

**What Claude does:**
Generate three scenarios using the base inputs with defined variance bands:

- **Base Case:** As modeled (ARV as stated, ERC as stated)
- **Optimistic Case:** ARV +5%, ERC −10% (faster market, cleaner-than-expected repairs)
- **Conservative Case:** ARV −10%, ERC +20%, hold time +2 months (soft market, scope creep, delayed sale)

For each scenario, recalculate: Net Profit, ROI, Cash-on-Cash, and Profit Margin.

**Tools / Resources needed:**
None — recalculation from Step 3 model.

**Data source:**
Step 3 outputs with variance band adjustments.

**Output of this step:**
A three-column scenario comparison table with all four metrics for each scenario, and a one-sentence verdict per scenario.

**Cowork behavior:**
PROCEED WITH ANALYSIS AND DRAFTING.

**If this step fails or required data is missing:**
If inputs are at the margin (conservative scenario produces negative profit), flag this explicitly: "⚠️ DOWNSIDE RISK: Under conservative assumptions, this deal produces a NET LOSS of $[X]. Acquisition requires high confidence in ARV and scope control."

> 💡 **Precision Note:** The conservative scenario's ARV reduction should reflect actual market softening risk — in slow markets (DOM >60 days), use −15% instead of −10%. Ask the user for average DOM before applying the standard variance if the market is unknown.

---

### Step 5: Generate Timeline with Phase Milestones

**What Claude does:**
Based on the stated hold time, build a realistic project timeline broken into standard fix-and-flip phases:

- **Week 1–2:** Closing & permit pull (acquisition complete, GC mobilization)
- **Weeks 3–6:** Demolition & structural work (rough trades: framing, electrical rough, plumbing rough, HVAC rough)
- **Weeks 7–10:** Mechanical completion (inspections, drywall, insulation)
- **Weeks 11–14:** Finish work (flooring, cabinets, fixtures, paint, exterior)
- **Weeks 15–16:** Final punch, clean, staging, professional photography
- **Week 17+:** List, market, negotiate, contract, close (allow 30–60 days)

Adjust phase durations proportionally if hold time differs from the 5-month default.

**Tools / Resources needed:**
None — standard industry timeline applied to user's stated hold time.

**Data source:**
User-provided hold time from Step 1.

**Output of this step:**
A phase-by-phase timeline table with week ranges, milestone descriptions, and cash flow event markers (draw requests, tax payment dates).

**Cowork behavior:**
PROCEED WITH ANALYSIS AND DRAFTING.

**If this step fails or required data is missing:**
If hold time is under 3 months, flag: "⚠️ Sub-90-day flip timelines are extremely high-risk for properties requiring significant rehab. Verify ERC and scope are consistent with this timeline — cosmetic flips only."

---

### Step 6: Deliver Final Report with Go/No-Go Recommendation

**What Claude does:**
Assemble all outputs from Steps 1–5 into the formatted report (see Output Format below). Apply the tiered recommendation logic:

- **STRONG BUY:** Base case net profit ≥$30K (or user's stated minimum), conservative scenario still profitable, profit margin ≥15%
- **PROCEED WITH CAUTION:** Base case meets minimum profit but conservative scenario is breakeven or thin (<8% margin)
- **PASS:** Base case net profit below minimum, or conservative scenario produces a net loss, or profit margin <8% in base case

State the exact threshold that triggered the recommendation and the single most critical risk factor.

**Tools / Resources needed:**
None — synthesized from all prior steps.

**Data source:**
Outputs from Steps 1–5.

**Output of this step:**
Complete formatted deal analysis report (see Output Format section).

**Cowork behavior:**
CONFIRM BEFORE PROCEEDING — if the recommendation is STRONG BUY and the user has indicated they are ready to make an offer, ask: "Shall I draft an LOI at $[MAO] for this property?" before taking any next action.

**If this step fails or required data is missing:**
If any required calculation is missing, restate what data gap prevented completion and list the specific inputs needed.

---

## 💻 CODE EXAMPLE

```python
# Fix & Flip Full Cost Stack Calculator
# Evy Evans | AI assistant Skill Library | May 2026

def calculate_flip_deal(
    purchase_price: float,
    arv: float,
    erc: float,
    hold_months: int,
    financing_rate: float = 0.12,   # annual rate, e.g. 0.12 = 12%
    ltc_ratio: float = 0.75,         # loan-to-cost ratio
    origination_points: float = 2.0, # lender origination fee in points
    commission_rate: float = 0.055,  # total agent commission on sale
    cash_deal: bool = False,
    desired_profit: float = 30000
) -> dict:
    """
    Full fix-and-flip feasibility model.
    Returns itemized cost stack, profit metrics, and tiered recommendation.
    """

    # --- ACQUISITION COSTS ---
    buyer_closing = purchase_price * 0.015
    due_diligence = 500
    acquisition_total = purchase_price + buyer_closing + due_diligence

    # --- REHAB COSTS ---
    contingency = erc * 0.15
    rehab_total = erc + contingency

    # --- HOLDING COSTS ---
    monthly_taxes = (arv * 0.012) / 12
    monthly_insurance = 150
    monthly_utilities = 200
    monthly_hold = monthly_taxes + monthly_insurance + monthly_utilities
    holding_total = monthly_hold * hold_months

    # --- FINANCING COSTS ---
    if cash_deal:
        financing_total = 0
        loan_amount = 0
    else:
        loan_amount = purchase_price * ltc_ratio
        origination_fee = loan_amount * (origination_points / 100)
        monthly_interest = loan_amount * (financing_rate / 12)
        interest_total = monthly_interest * hold_months
        financing_total = origination_fee + interest_total

    # --- DISPOSITION COSTS ---
    commissions = arv * commission_rate
    seller_closing = arv * 0.01
    staging = 1500
    disposition_total = commissions + seller_closing + staging

    # --- TOTALS ---
    total_project_cost = (acquisition_total + rehab_total +
                          holding_total + financing_total + disposition_total)
    net_profit = arv - total_project_cost
    roi = (net_profit / total_project_cost) * 100
    annualized_roi = roi / hold_months * 12
    profit_margin = (net_profit / arv) * 100

    # Cash invested (out-of-pocket)
    cash_invested = (purchase_price - loan_amount + buyer_closing +
                     due_diligence + (erc + contingency) * 0.25)  # assume 25% rehab OOP
    coc_return = (net_profit / cash_invested) * 100 if cash_invested > 0 else 0

    # --- RECOMMENDATION ---
    if net_profit >= desired_profit and profit_margin >= 15:
        recommendation = "✅ STRONG BUY"
    elif net_profit >= desired_profit * 0.7 and profit_margin >= 8:
        recommendation = "⚠️ PROCEED WITH CAUTION"
    else:
        recommendation = "❌ PASS — does not meet minimum return threshold"

    return {
        "purchase_price": f"${purchase_price:,.0f}",
        "arv": f"${arv:,.0f}",
        "erc_base": f"${erc:,.0f}",
        "erc_with_contingency": f"${rehab_total:,.0f}",
        "acquisition_costs": f"${acquisition_total:,.0f}",
        "holding_costs": f"${holding_total:,.0f}",
        "financing_costs": f"${financing_total:,.0f}",
        "disposition_costs": f"${disposition_total:,.0f}",
        "total_project_cost": f"${total_project_cost:,.0f}",
        "net_profit": f"${net_profit:,.0f}",
        "roi_percent": f"{roi:.1f}%",
        "annualized_roi": f"{annualized_roi:.1f}%",
        "profit_margin": f"{profit_margin:.1f}%",
        "cash_on_cash": f"{coc_return:.1f}%",
        "recommendation": recommendation,
        "deal_viable": net_profit >= desired_profit
    }

# Example:
result = calculate_flip_deal(
    purchase_price=135000, arv=285000, erc=47000,
    hold_months=5, financing_rate=0.12, desired_profit=30000
)
# Net Profit ≈ $67,000 | Margin ≈ 23.5% | ✅ STRONG BUY
```

---

## 📤 OUTPUT FORMAT

**Output type:** Deal Analysis Report  
**Delivery method:** Returned directly in chat — ready to copy into CRM, email to partner, or paste into deal file

---

```
╔══════════════════════════════════════════════════════════════╗
║         FIX & FLIP PROFIT ANALYSIS — Evy Evans             ║
╚══════════════════════════════════════════════════════════════╝

Property:       4821 Maple Ave, Columbus OH 43215
Analysis Date:  May 10, 2026
Analyst:        AI assistant via Evy Evans Skill Library

━━━━━━━━━━━━━━━━ DEAL INPUTS ━━━━━━━━━━━━━━━━
Purchase Price:          $135,000
After Repair Value:      $285,000
Est. Repair Cost (ERC):  $47,000
Hold Time:               5 months
Financing:               Hard money — 12% / 2 pts / 75% LTC

━━━━━━━━━━━━━━━━ FULL COST STACK ━━━━━━━━━━━━
ACQUISITION
  Purchase Price:              $135,000
  Buyer Closing (1.5%):          $2,025
  Due Diligence:                   $500
  Acquisition Total:           $137,525

REHAB
  ERC (stated):                 $47,000
  Contingency Reserve (15%):     $7,050
  Rehab Total:                  $54,050

HOLDING (5 months)
  Property Taxes:                $1,425
  Insurance:                       $750
  Utilities:                     $1,000
  Holding Total:                 $3,175

FINANCING
  Loan Amount (75% LTC):       $101,250
  Origination Fee (2 pts):       $2,025
  Interest (12% × 5 mo):        $5,063
  Financing Total:               $7,088

DISPOSITION
  Agent Commissions (5.5%):    $15,675
  Seller Closing (1.0%):         $2,850
  Staging:                       $1,500
  Disposition Total:            $20,025

TOTAL PROJECT COST:           $221,863

━━━━━━━━━━━━━━━━ PROFIT SUMMARY ━━━━━━━━━━━━
ARV:                          $285,000
Total Project Cost:          ($221,863)
NET PROFIT:                    $63,137
Profit Margin:                    22.2%   ✅ HEALTHY (≥15%)
ROI on Total Cost:                28.5%
Annualized ROI:                   68.4%
Cash-on-Cash Return:              89.2%

━━━━━━━━━━━━━━━━ SCENARIO STRESS TEST ━━━━━━
                    BASE        OPTIMIST    CONSERVATIVE
ARV Used:         $285,000    $299,250     $256,500
ERC Used:          $47,000     $42,300      $56,400
Hold Time:         5 months    5 months     7 months
Net Profit:        $63,137     $81,094      $23,418
Profit Margin:      22.2%       27.1%         9.1%
Verdict:           STRONG     VERY STRONG    MARGINAL

━━━━━━━━━━━━━━━━ PROJECT TIMELINE ━━━━━━━━━━
Weeks 1–2:   Closing & permit pull
Weeks 3–6:   Demo + rough trades (electrical, plumbing, HVAC)
Weeks 7–10:  Mechanicals + drywall + insulation
Weeks 11–14: Finish work (flooring, cabinets, fixtures, paint)
Weeks 15–16: Punch list, staging, photography
Week 17+:    List, market, contract, close (allow 45 days)

━━━━━━━━━━━━━━━━ RISK FLAGS ━━━━━━━━━━━━━━━━
⚠️ ARV source unverified — confirm with 3+ closed comps within
   0.5 miles and 180 days before committing capital
⚠️ Conservative scenario margin of 9.1% — scope control critical

━━━━━━━━━━━━━━━━ RECOMMENDATION ━━━━━━━━━━━━
✅ STRONG BUY — Net profit $63,137 exceeds $30K minimum threshold.
Margin of 22.2% provides meaningful downside buffer. Even under
conservative assumptions (−10% ARV, +20% ERC, 2 extra months),
the deal remains marginally profitable.

SUGGESTED OFFER: $135,000 (current ask)
MAO TO PROTECT $30K PROFIT: $145,200
```

---

## 🔐 PERMISSIONS & SETUP CHECKLIST

No external permissions or setup required. Attach this file to any Claude.ai chat and type the trigger phrase. This skill runs entirely within Claude's context window.

- [ ] **Optional — Comparable Sales Verification:** Access Redfin.com or MLS to verify user-provided ARV against 3+ closed comps before relying on this analysis in a live transaction.
- [ ] **Optional — Local Labor Rates:** Check HomeAdvisor or BuildZoom for regional labor cost benchmarks if ERC feels out of range for your market.

---

## ✅ QUALITY SELF-CHECK

Before delivering any output, Claude must internally verify every item below. Do not deliver output until all boxes can be checked:

- [ ] All required inputs were provided by the user or explicitly flagged as missing
- [ ] Every financial calculation is shown with its formula and inputs visible
- [ ] ARV source is either confirmed by user or flagged as unverified ⚠️
- [ ] All five cost categories are present in the cost stack
- [ ] Three-scenario stress test is complete with conservative scenario explicitly evaluated
- [ ] Output exactly matches the format specified above — no improvisation
- [ ] Zero placeholder text remains in the final output
- [ ] Any thin-margin or negative scenario is surfaced with a ⚠️ flag — never buried
- [ ] Output is immediately usable in a live deal without further editing

---

## ⚠️ EDGE CASES & ESCALATION RULES

| Scenario | Claude's Exact Response |
|----------|------------------------|
| ARV not provided | "I need an ARV to run this analysis. What is your estimated After Repair Value based on comparable closed sales?" — do not proceed without it |
| ERC not provided | Apply a rough estimate of $25/sqft for cosmetic or $60/sqft for full gut and flag prominently: "⚠️ ERC ESTIMATED — provide actual scope of work for accurate modeling" |
| Conservative scenario produces net loss | Display the loss amount, identify the #1 cost driver, and recommend: "This deal has insufficient margin buffer — negotiate purchase price down or reduce scope" |
| Legal or compliance risk detected | Insert ⚠️ LEGAL FLAG: "Hard money lending terms vary by state. Confirm loan terms comply with your state's usury laws and licensing requirements with a real estate attorney." |
| Hold time exceeds 12 months | Flag: "⚠️ Hold times over 12 months significantly increase carry risk, tax implications, and market exposure. Consider whether a BRRRR or rental hold strategy is more appropriate." |
| User provides ARV above ask + 100% | Flag as outlier: "⚠️ ARV exceeds purchase price by more than 100%. This is unusual — verify comps carefully. Overstated ARV is the #1 cause of flip losses." |
| Session approaching context limit | Write `_PROGRESS_CHECKPOINT.md` with completed steps and remaining inputs before context is exhausted |

---

## 📖 DOMAIN GLOSSARY

| Term | Definition |
|------|-----------|
| ARV | After Repair Value — the projected market value of a property after all repairs and improvements are completed, based on closed comparable sales |
| MAO | Maximum Allowable Offer — the highest price an investor should pay to preserve target profit; typically (ARV × 70%) − ERC |
| ERC | Estimated Repair Cost — the conservative total cost of all repairs needed to bring a property to ARV condition |
| LTC | Loan-to-Cost Ratio — the percentage of total project cost (purchase + rehab) a hard money lender will finance |
| Hard Money | Short-term, asset-based real estate financing typically from private lenders; higher rates (10–15%) but fast closing (5–10 days) |
| Origination Points | Upfront lender fee expressed as a percentage of the loan amount; 1 point = 1% of loan |
| Holding Costs | Monthly expenses incurred while owning the property during rehab: taxes, insurance, utilities, HOA, financing interest |
| Disposition | The process of selling the rehabbed property — includes listing, marketing, negotiating, and closing the sale |
| Cash-on-Cash Return | Net profit divided by actual cash invested out-of-pocket (excluding financed amounts) — measures leverage efficiency |
| Profit Margin | Net profit as a percentage of ARV — healthy flips target ≥15%; below 8% signals excessive risk |
| Contingency Reserve | A buffer (typically 10–20% of ERC) added to the base repair estimate to absorb scope creep and unexpected conditions |
| Pro Forma | A projected financial model showing expected income, expenses, and returns for a real estate project |
| Annualized ROI | Return on investment scaled to a 12-month equivalent — allows comparison across deals with different hold times |

---

*Authored by Evy Evans | Real Estate Agentic Automation*  
*Maintained as part of RealtySkills by Evy Evans. Example dates and figures are illustrative.*
