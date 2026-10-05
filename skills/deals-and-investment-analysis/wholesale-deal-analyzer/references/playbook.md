# Source playbook

This playbook supplies task procedures and examples. Follow the working rules in the skill entry, verify current jurisdiction-specific claims, and treat examples as illustrative.

# Wholesale Deal Analyzer (ARV / MAO / Exit Strategy)

Turn a raw property address and a handful of comp links into a complete acquisition decision package in under ten minutes. This skill calculates ARV from defensible closed comps, builds a conservative line-item Estimated Repair Cost (ERC), runs the Maximum Allowable Offer (MAO) under both the standard 70% rule and a custom-margin variant, and compares four exit strategies side-by-side — wholesale assignment, fix-and-flip, BRRRR, and wholetail — so the investor knows not just whether the deal works, but which exit closes the most cash. Built for solo wholesalers analyzing 5 deals a day and institutional acquisition managers underwriting bulk pipelines into the same defensible framework.

## 🧠 SKILL IDENTITY

**WHO this skill is for:**
A working wholesaler with 1–10 leads in the funnel each day; a fix-and-flip operator who needs to underwrite a deal during a 20-minute drive between showings; an institutional-scale wholesaler-flipper running 50+ deals a month across multiple markets who needs every acquisition manager on the team using the same MAO math. The skill is tuned for the moment between "this looks interesting" and "I'm sending an offer" — when a wrong number costs 10–40 grand.

**WHAT this skill does:**
Takes a property address, basic specs (beds / baths / sqft / year built / condition tier), and an optional comp set, then produces a defensible acquisition package: ARV from median price-per-sqft of closed comps within 0.5 miles and 180 days, conservative ERC broken down by trade with a 10% contingency, MAO calculated under the 70% rule and a user-defined custom margin, and a four-way exit strategy comparison (wholesale assignment / fix-and-flip / BRRRR / wholetail) showing projected profit, capital required, and timeline for each. Output ends in a one-line go/no-go recommendation with the specific offer price to lead with.

**WHERE to use this skill:**
Standalone Claude.ai chat is the daily driver — paste a property and a comp list, get a full underwrite back in 8 minutes. Cowork Task mode handles bulk pipelines (acquisition managers running 20+ properties through the same rubric overnight, writing a deal_summary.md per address). Claude.ai Project deployment is the right call for institutional teams where every analyst needs to use the same ARV/ERC/MAO methodology — upload once, every team member triggers the same skill.

**WHEN to activate this skill:**
The moment a motivated seller calls back; immediately after a property walkthrough when the contractor's repair estimate is fresh; right before submitting an LOI or PSA so the offer price is data-backed; on every wholesale deal before assigning to a buyers list (so you know exactly what fee to ask); during weekly pipeline review when an institutional team needs to grade 30 properties at once.

**WHY this skill matters:**
This workflow makes the required inputs and output structure explicit. Its numerical benchmarks are configurable assumptions, not validated performance claims.

**HOW this skill works (Overview):**
Claude confirms the subject property baseline, validates or pulls the comp set against the closed-180-days/0.5-miles standard, computes ARV via median price-per-sqft applied to the subject's above-grade square footage, builds a conservative line-item ERC with trade-by-trade breakouts, calculates MAO under both the 70% rule and the user's custom margin, runs the four exit strategies through their distinct math (assignment fee, flip with holding costs, BRRRR refi, wholetail cosmetic), surfaces risk flags, draws a capital-stack outline, and ends with a clear go/no-go and lead offer price.

## When to Use

- Underwriting a wholesale deal before assigning the contract to a cash-buyers list
- Validating ARV on a fix-and-flip before submitting an offer
- Choosing between exit strategies on a property that pencils for multiple paths
- Comparing two competing deals to decide which one gets the limited capital this week
- Running an institutional acquisition team's daily pipeline through a uniform underwriting standard
- Defending an offer price to a seller, JV partner, or hard money lender
- Pre-screening a wholesaler's deal before agreeing to be the cash buyer
- Building the capital stack for a deal that needs hard money plus private money plus rehab draw

## 📥 REQUIRED INPUTS

| Input | Format | Source | Required? | Example |
|---|---|---|---|---|
| subject_address | string | User paste, MLS export, PropStream, REISimpli, ATTOM Data | Yes | "1842 Linden Ave, Columbus, OH 43211" |
| subject_specs | object (beds, baths, sqft, year_built) | User paste, county assessor, Zillow, Redfin | Yes | `{beds: 3, baths: 1.5, sqft: 1380, year_built: 1958}` |
| condition_tier | enum: excellent / good / average / fair / poor / distressed | Walkthrough, photos, wholesaler notes | Yes | "fair" |
| occupancy_status | enum: vacant / owner-occupied / tenant-occupied / squatter / unknown | Seller intake call, drive-by, county records | Yes | "vacant" |
| comp_set | array of 4–6 closed sales (address, sold_price, sold_date, beds, baths, sqft, condition) | Zillow, Redfin, Realtor.com, MLS via RETS/RESO, PropStream, ATTOM Data | Yes | 5 closed comps within 0.5 mi / 180 days |
| repair_scope | object or text (line items by trade or "light/medium/heavy") | Contractor walkthrough, PropStream rehab estimator, photos + Claude inference | No (Claude can estimate from photos+condition) | "Roof: $9k, HVAC: $6k, Kitchen full: $14k, Bath full: $7k, Flooring: $5k, Paint: $3k, Misc: $3k" |
| desired_profit_target | number (USD) | Investor preference; institutional teams use a fixed return target | No (defaults to $25k flip / $10k assignment / 10% CoC for BRRRR) | 35000 |
| financing_assumption | enum: cash / hard_money / private_money / transactional / conventional | Investor's funding source | No (defaults to hard money 10% / 2 pts) | "hard_money" |
| target_market_for_exit | string | User context — STR market, retail buyer market, rental-strong market | No | "Columbus near OSU campus — strong rental and retail" |
| as-is_value_estimate | number (USD) | County assessor, Zillow Zestimate, BPO | No | 142000 |

## ⚙️ EXECUTION SOP

### Step 1: Confirm Subject Property Baseline

**What Claude does:** Restate the subject property to the user — address, beds/baths, above-grade square footage, year built, condition tier, and current occupancy status. Surface any internal inconsistency (e.g., "you said 1380 sqft but 4 bedrooms — confirm the layout").
**Tools / Resources needed:** Pasted user input; optional Zillow / Redfin / Realtor.com / county assessor cross-reference if address is provided alone.
**Data source:** The `subject_address` and `subject_specs` fields.
**Output of this step:** A 4-line subject summary block, plus an explicit list of assumptions Claude is making (e.g., "Treating 'fair' condition as cosmetic + minor mechanical — no structural").
**Cowork behavior:** PROCEED WITH ANALYSIS AND DRAFTING when all subject fields are provided and internally consistent. CONFIRM BEFORE PROCEEDING when the user provided only an address and Claude must look up specs from public sources (since pulled values may be stale).
**If this step fails or required data is missing:** Ask for the specific missing field — never guess sqft (the entire ARV depends on it). For year built, default to "post-1978" if missing (this affects lead-paint disclosure language only).

> 💡 Precision Note: Above-grade living area is the only square footage that drives ARV via $/sqft — finished basements are valued separately at 35–60% of above-grade $/sqft depending on egress and finish. Never include basement sqft in the $/sqft calc.

### Step 2: Validate or Pull the Comp Set

**What Claude does:** Score every comp the user provided against the defensible-comp standard: closed within the last 180 days, within 0.5 miles, similar bed/bath count (±1), within ±20% of subject sqft, similar condition or with a known adjustment. Reject any comp that fails two or more criteria; flag any that fail one. Require a minimum of 4 valid comps; ideal is 6.
**Tools / Resources needed:** User-pasted comp set; optional Zillow / Redfin / Realtor.com / MLS via RETS/RESO / PropStream / ATTOM Data if the user wants Claude to suggest additional comps to pull.
**Data source:** `comp_set` array.
**Output of this step:** A validated comp table with each row tagged VALID / FLAGGED / REJECTED and a one-line reason; a Comp Confidence Score: HIGH (6+ valid), MEDIUM (4–5 valid), LOW (<4 valid).
**Cowork behavior:** PROCEED WITH ANALYSIS AND DRAFTING if Comp Confidence is HIGH. CONFIRM BEFORE PROCEEDING if MEDIUM or LOW — present the gap and ask whether to expand the window (1.0 mi / 270 days) or proceed with confidence flag.
**If this step fails or required data is missing:** If fewer than 4 comps remain after validation, expand the search window to 1.0 mi / 270 days and rerun. If still <4, flag Comp Confidence as LOW, recommend a BPO, and proceed with a wider $/sqft band in the ARV calc.

> 💡 Precision Note: Active listings and pending sales are NOT comps for ARV. They tell you about list-side competition, not realized market value. Use only closed sales for ARV; surface actives separately as "competitive supply."

### Step 3: Calculate ARV via Median Price-per-Square-Foot

**What Claude does:** Compute each valid comp's $/sqft (sold_price ÷ sqft), take the median (not mean — outliers distort means), apply that $/sqft to the subject's above-grade sqft, then layer in feature adjustments (extra bath, garage, lot size, finished basement, view, condition delta) using the standard adjustment grid embedded below. Report ARV as a point estimate with a ±5% confidence band.
**Tools / Resources needed:** Median-$/sqft formula; standard adjustment grid; subject's feature set.
**Data source:** Validated comp set from Step 2; subject specs from Step 1.
**Output of this step:** ARV point estimate (e.g., $285,000) with the math shown — comp $/sqft list, median, subject sqft, adjustments, final number — plus a confidence band ($271k – $299k).
**Cowork behavior:** PROCEED WITH ANALYSIS AND DRAFTING.
**If this step fails or required data is missing:** If a comp's sqft is missing, recompute using $/bed or skip the comp; never invent a sqft value.

**Standard Adjustment Grid (subject-vs-comp deltas, applied to comp before averaging):**

| Feature Delta | Adjustment Direction | Typical Adjustment |
|---|---|---|
| Subject has 1 more bath | + to comp | $5,000–$8,000 per half bath |
| Subject has 1-car garage advantage | + to comp | $6,000–$12,000 |
| Subject has finished basement (comp doesn't) | + to comp | 35–60% of above-grade $/sqft × basement sqft |
| Subject lot is +0.25 acre vs comp | + to comp | $3,000–$10,000 (market-dependent) |
| Subject is 10+ years newer than comp | + to comp | $5–$15/sqft × subject sqft |
| Subject condition is one tier worse than comp | − from comp | 5–12% of comp price |
| Subject backs to railroad / commercial | − from comp | $5,000–$20,000 |

> 💡 Precision Note: Median beats mean for $/sqft because one $400k flipper sale can drag the average up $30/sqft and overstate ARV by 15%. Always show both numbers — if they diverge by more than 8%, investigate the outlier.

### Step 4: Build the Estimated Repair Cost (ERC) — Line-Item by Trade

**What Claude does:** Either accept the user's contractor walkthrough estimates verbatim, or build a line-item ERC from the condition tier and any photos/notes. Itemize across nine standard buckets — roof, HVAC, plumbing, electrical, kitchen, bathrooms, flooring, paint, exterior — plus mechanicals and a hard 10% contingency. Use regional cost benchmarks (Columbus OH / Atlanta GA / Phoenix AZ are the calibrated markets in this skill; flag for any market outside).
**Tools / Resources needed:** Embedded ERC benchmark table (below); user's repair scope or photos.
**Data source:** `repair_scope` field, `condition_tier`, photos if attached.
**Output of this step:** A 10-row ERC table with quantity / unit cost / line total per trade, contingency, and a single bottom-line ERC number.
**Cowork behavior:** PROCEED WITH ANALYSIS AND DRAFTING when the user has provided contractor estimates. CONFIRM BEFORE PROCEEDING when Claude is inferring ERC from condition tier alone — overestimating by 30% is the safe bias, but the user should approve the assumed scope.
**If this step fails or required data is missing:** If condition tier is "distressed" and no scope is provided, build TWO scenarios (light: $35–$50/sqft, heavy: $65–$85/sqft) and recommend an inspection contingency on the offer.

**ERC Trade Benchmarks — 1,200–1,600 sqft SFR, average finishes (2026 dollars):**

| Trade | Light Scope | Medium Scope | Heavy Scope |
|---|---|---|---|
| Roof | $4,500 | $9,000 | $14,000 |
| HVAC (full replace, 3-ton) | $0 (still functional) | $6,500 | $9,500 |
| Plumbing (sewer, supply lines, fixtures) | $1,500 | $5,000 | $14,000 |
| Electrical (panel + rewire as needed) | $1,000 | $4,500 | $11,000 |
| Kitchen (cabinets, counters, appliances) | $4,000 | $11,000 | $22,000 |
| Bathroom (full per bath) | $2,500 | $5,500 | $9,500 |
| Flooring (LVP, $4–7/sqft installed) | $4 × sqft | $5.50 × sqft | $7 × sqft |
| Paint (interior + minor exterior) | $2,500 | $4,500 | $7,000 |
| Exterior (siding, gutters, paint, landscaping) | $1,500 | $5,500 | $14,000 |
| Misc / permits / dumpsters | $1,500 | $3,000 | $5,500 |
| **Contingency** | **+10%** | **+10%** | **+10%** |

> 💡 Precision Note: Sewer line replacement ($8–14k) is the most commonly missed repair on pre-1970 homes. Always ask whether a sewer scope was performed; if not, add a $2,500 contingency line.

### Step 5: Calculate MAO — 70% Rule AND Custom Margin Variant

**What Claude does:** Compute MAO under two methods. Method 1 — 70% Rule: MAO = (ARV × 0.70) − ERC. Method 2 — Custom Margin: MAO = ARV − ERC − Selling Costs − Holding Costs − Financing Costs − Desired Profit. Show both. Flag the lower of the two as the conservative MAO and the higher as the aggressive MAO.
**Tools / Resources needed:** ARV from Step 3; ERC from Step 4; user's `desired_profit_target` and `financing_assumption`.
**Data source:** Steps 3 and 4 outputs.
**Output of this step:** A two-line MAO summary — "70% Rule MAO: $X / Custom Margin MAO: $Y / Lead with $Z" — plus the full math behind the custom margin (selling costs at 8% of ARV, holding 4 months, financing at the user's assumption).
**Cowork behavior:** PROCEED WITH ANALYSIS AND DRAFTING.
**If this step fails or required data is missing:** If `desired_profit_target` is blank, default to $25,000 flip profit / $10,000 assignment fee and explicitly label the assumption.

> 💡 Precision Note: The 70% rule was calibrated for hard-money flips with 6% commission and 4 months of holding. In strong seller markets with cash buyers and 30-day flips, a 75% or even 80% rule may pencil; in soft markets or expensive permitting jurisdictions, drop to 65%. Always show both rules.

### Step 6: Compare Exit Strategies — Wholesale / Flip / BRRRR / Wholetail

**What Claude does:** Run the deal through all four exits using the math below; compute projected profit and capital required for each; rank them by projected return on capital and by speed-to-cash; surface which exit (if any) the deal does NOT pencil for.
**Tools / Resources needed:** ARV (Step 3), ERC (Step 4), MAO (Step 5), local rent estimate from Zillow Rent Zestimate or Rentometer (for BRRRR), local STR ADR if relevant.
**Data source:** All prior steps + user's `target_market_for_exit`.
**Output of this step:** A four-column exit-strategy comparison table — Wholesale Assignment / Fix-and-Flip / BRRRR / Wholetail — each with projected profit, capital required, timeline, and a green/yellow/red light.

**Exit-Strategy Math:**

| Exit | Math | Capital Required | Timeline |
|---|---|---|---|
| Wholesale Assignment | Assignment Fee = (End Buyer's Max Offer) − (Your Contract Price); end buyer typically uses 70% rule | $1k–$10k EMD + closing | 7–30 days |
| Fix-and-Flip | Profit = ARV − Selling Costs (8%) − ERC − Holding (4 mo × HOA/tax/insurance/financing) − Financing Points − Acquisition Price | Down payment (10–25%), full ERC reserve, holding cost reserve | 4–7 months |
| BRRRR | Refi Proceeds = ARV × 0.75 (typical DSCR LTV); Cash Left In = Acquisition + ERC + Closing − Refi Proceeds; cash flow = NOI − refi debt service | Acquisition + ERC up front; refi typically 6 mo seasoning | 6–12 months to cash-out |
| Wholetail | Profit = (Light-Cosmetic ARV) × 0.92 − Cosmetic Cost (~$8–15k) − Holding (2 mo) − Acquisition; uses 80% rule on offer | Acquisition + cosmetic | 30–75 days |

**Cowork behavior:** PROCEED WITH ANALYSIS AND DRAFTING.
**If this step fails or required data is missing:** If rent estimate is missing for BRRRR, pull from Zillow Rent Zestimate / Rentometer if Cowork has web access; otherwise compute the other three exits and flag BRRRR as "rent estimate required."

> 💡 Precision Note: A deal that pencils for only ONE exit is still a valid deal — but the lack of optionality means the offer should be 3–5% lower than MAO to compensate for the increased risk. A deal that pencils for three or four exits is a "stack" — pursue at the higher MAO.

### Step 7: Surface Risk Flags

**What Claude does:** Scan for the standard nine acquisition risks — title issues (liens, judgments), structural unknowns (foundation, roof structure), environmental (mold, asbestos, lead paint, oil tank, radon), zoning (non-conforming use, ADU restrictions), HOA (assessments, restrictions), occupancy (squatter, holdover tenant, eviction needed), financing (un-warrantable condo, assignability prohibition), legal (probate, divorce, lis pendens), and exit market (comp confidence LOW).
**Tools / Resources needed:** Public records signals from PropStream / ATTOM Data / county GIS; user's notes.
**Data source:** `occupancy_status`, user's risk notes, comp confidence from Step 2.
**Output of this step:** A risk-flag block — each flag tagged HIGH / MEDIUM / LOW with a one-line mitigation step.
**Cowork behavior:** PROCEED WITH ANALYSIS AND DRAFTING.
**If this step fails or required data is missing:** Flag missing data as a risk in itself ("title status unknown — pull preliminary title report before EMD").

> 💡 Precision Note: Tenant-occupied with no lease in hand is a HIGH risk — eviction can take 30–180 days depending on state, and any cash-for-keys negotiation eats into profit. Always quantify in the MAO if applicable.

### Step 8: Build the Capital Stack

**What Claude does:** Outline how the deal gets funded: cash needed at close, hard-money loan amount and terms, private-money gap if any, transactional funding for assignments, rehab draw schedule, and total cash-to-close. Show the full at-risk capital across the project.
**Tools / Resources needed:** User's `financing_assumption`; standard hard money / private money market terms (10% rate / 2 pts / 70% LTC for hard money in 2026).
**Data source:** Step 5 MAO + Step 4 ERC + standard 2026 lender terms.
**Output of this step:** A capital-stack block: "Acquisition $X / Hard money $Y at 10% + 2 pts / Down payment $Z / ERC reserves $A / Closing costs $B / Total cash-to-close $C / Total at-risk capital $D."
**Cowork behavior:** PROCEED WITH ANALYSIS AND DRAFTING.
**If this step fails or required data is missing:** If the user did not specify a financing assumption, present three scenarios (cash, hard money, private+hard money) and let them pick.

> 💡 Precision Note: At-risk capital is more important than cash-to-close. A hard-money deal with low cash-to-close but $80k of personal guarantee is RISKIER than a private-money deal with higher cash-to-close but no guarantee.

### Step 9: Draft the Go/No-Go Decision

**What Claude does:** Write a one-paragraph executive summary stating the recommendation (PURSUE / PASS / RENEGOTIATE), the lead offer price, the recommended exit strategy, the projected profit at MAO, and the top two risk flags. Tone: institutional acquisition memo — clear, direct, no hedging.
**Tools / Resources needed:** All prior steps.
**Data source:** Steps 1–8.
**Output of this step:** A 4–6 sentence executive summary plus a single-line "Lead with: $XXX,XXX" offer recommendation.
**Cowork behavior:** CONFIRM BEFORE PROCEEDING — the offer-price recommendation is the highest-stakes line in the document; the user should explicitly acknowledge before it goes into an LOI.
**If this step fails or required data is missing:** Cannot fail unless prior steps did.

> 💡 Precision Note: A "RENEGOTIATE" outcome — common when the seller's asking is 10–20% above MAO — should include the exact counter-offer price plus the talking points (recent comps, rehab scope) the user can use on the call.

### Step 10: Output the Full Underwriting Package + One-Page Seller-Facing Offer Summary

**What Claude does:** Assemble the complete deal packet: subject summary, comp set, ARV math, ERC table, MAO, exit comparison, risk flags, capital stack, and executive summary — formatted for the user's records. Then produce a SEPARATE one-page seller-facing version that strips internal margin math and presents only the offer price, terms, and a brief justification appropriate to share with a motivated seller.
**Tools / Resources needed:** All prior step outputs.
**Data source:** Steps 1–9.
**Output of this step:** Two artifacts — (1) the internal underwriting package for the investor's file, (2) the seller-facing one-pager with the offer terms.
**Cowork behavior:** PROCEED WITH ANALYSIS AND DRAFTING.
**If this step fails or required data is missing:** Cannot fail unless prior steps did.

> 💡 Precision Note: Never share internal MAO math with a seller. The seller-facing one-pager presents the offer as a "fair, fast, certain close" — not as "we backed into this number using the 70% rule."

## 💻 CODE EXAMPLE

```python
# Wholesale Deal Analyzer — MAO Calculator + Multi-Exit Comparison
# Production-grade reference implementation. Adjust constants for your market.

from dataclasses import dataclass
from typing import Optional

@dataclass
class DealInputs:
    address: str
    arv: float                  # After-Repair Value, USD
    erc: float                  # Estimated Repair Cost, USD
    monthly_rent_estimate: float  # For BRRRR exit
    target_profit_flip: float = 30000.0
    target_assignment_fee: float = 10000.0
    holding_months: int = 4
    hard_money_rate: float = 0.10
    hard_money_points: float = 0.02
    selling_cost_pct: float = 0.08   # 6% commission + 2% closing
    monthly_holding_cost_pct: float = 0.012  # tax + insurance + utilities + HOA, ~1.2% of ARV/yr / 12
    refi_ltv: float = 0.75
    refi_rate: float = 0.075
    refi_term_years: int = 30

def analyze_wholesale_deal(d: DealInputs) -> dict:
    """Calculate MAO across exit strategies and flag the best one."""

    # ---- 70% Rule MAO ----
    mao_70 = (d.arv * 0.70) - d.erc

    # ---- Custom-Margin MAO (Flip) ----
    selling_costs = d.arv * d.selling_cost_pct
    holding = d.arv * d.monthly_holding_cost_pct * d.holding_months
    # Hard money carry on rough acquisition+rehab estimate (use 70% rule price as proxy)
    hm_principal = mao_70 + d.erc
    hm_interest = hm_principal * d.hard_money_rate * (d.holding_months / 12)
    hm_points = hm_principal * d.hard_money_points
    financing_costs = hm_interest + hm_points

    mao_custom_flip = (d.arv - selling_costs - d.erc - holding
                       - financing_costs - d.target_profit_flip)

    # ---- Exit 1: Wholesale Assignment ----
    # End buyer typically applies 70% rule themselves
    end_buyer_mao = (d.arv * 0.70) - d.erc
    assignment_fee_target = d.target_assignment_fee
    wholesale_offer = end_buyer_mao - assignment_fee_target
    wholesale = {
        "exit": "Wholesale Assignment",
        "your_offer_price": round(wholesale_offer, 0),
        "projected_profit": round(assignment_fee_target, 0),
        "capital_required": 5000,  # EMD + closing
        "timeline_days": "7–30",
        "pencils": wholesale_offer > 0,
    }

    # ---- Exit 2: Fix-and-Flip ----
    flip_profit_at_mao = (d.arv - selling_costs - d.erc - holding
                          - financing_costs - mao_custom_flip)
    flip = {
        "exit": "Fix-and-Flip",
        "your_offer_price": round(mao_custom_flip, 0),
        "projected_profit": round(flip_profit_at_mao, 0),
        "capital_required": round(mao_custom_flip * 0.20 + d.erc, 0),  # 20% down + full ERC
        "timeline_days": f"{d.holding_months * 30}",
        "pencils": flip_profit_at_mao >= d.target_profit_flip * 0.9,
    }

    # ---- Exit 3: BRRRR ----
    annual_rent = d.monthly_rent_estimate * 12
    annual_opex = annual_rent * 0.40   # 40% expense ratio (tax, ins, vacancy, mgmt, capex)
    noi = annual_rent - annual_opex
    refi_loan_amount = d.arv * d.refi_ltv
    monthly_payment = (refi_loan_amount * (d.refi_rate / 12)) / \
                      (1 - (1 + d.refi_rate / 12) ** (-d.refi_term_years * 12))
    annual_debt_service = monthly_payment * 12
    annual_cash_flow = noi - annual_debt_service
    dscr = noi / annual_debt_service if annual_debt_service > 0 else 0
    all_in_cost = mao_70 + d.erc + (mao_70 * 0.03)   # +3% closing
    cash_left_in = max(0, all_in_cost - refi_loan_amount)
    coc_return = (annual_cash_flow / cash_left_in * 100) if cash_left_in > 0 else float("inf")
    brrrr = {
        "exit": "BRRRR",
        "your_offer_price": round(mao_70, 0),
        "refi_proceeds": round(refi_loan_amount, 0),
        "cash_left_in": round(cash_left_in, 0),
        "annual_cash_flow": round(annual_cash_flow, 0),
        "dscr": round(dscr, 2),
        "coc_return_pct": round(coc_return, 1) if coc_return != float("inf") else "Infinite (zero cash left)",
        "timeline_days": "180–365",
        "pencils": dscr >= 1.20 and annual_cash_flow > 0,
    }

    # ---- Exit 4: Wholetail (light cosmetic, list on MLS) ----
    cosmetic_cost = 12000  # cap ~$15k cosmetic
    wholetail_arv = d.arv * 0.92  # discount for as-is-ish condition
    wholetail_holding = d.arv * d.monthly_holding_cost_pct * 2
    wholetail_offer = (d.arv * 0.80) - cosmetic_cost  # 80% rule
    wholetail_profit = (wholetail_arv - (wholetail_arv * 0.08)
                        - cosmetic_cost - wholetail_holding - wholetail_offer)
    wholetail = {
        "exit": "Wholetail",
        "your_offer_price": round(wholetail_offer, 0),
        "projected_profit": round(wholetail_profit, 0),
        "capital_required": round(wholetail_offer + cosmetic_cost, 0),
        "timeline_days": "30–75",
        "pencils": wholetail_profit > 15000,
    }

    # ---- Decide best exit ----
    exits = [wholesale, flip, brrrr, wholetail]
    pencilling = [e for e in exits if e.get("pencils")]
    if not pencilling:
        recommendation = "PASS — deal does not pencil under any exit"
        lead_offer = 0
    else:
        # Rank: highest projected profit per timeline, but flip/wholetail wins on speed
        best = max(pencilling, key=lambda e: e.get("projected_profit", 0))
        recommendation = f"PURSUE — best exit: {best['exit']}"
        lead_offer = min(e["your_offer_price"] for e in pencilling if e["your_offer_price"] > 0)

    return {
        "address": d.address,
        "arv": d.arv,
        "erc": d.erc,
        "mao_70_rule": round(mao_70, 0),
        "mao_custom_flip": round(mao_custom_flip, 0),
        "exits": exits,
        "recommendation": recommendation,
        "lead_offer_price": lead_offer,
    }


# ---- Realistic example: 1842 Linden Ave, Columbus OH 43211 ----
deal = DealInputs(
    address="1842 Linden Ave, Columbus, OH 43211",
    arv=285000.0,
    erc=47000.0,
    monthly_rent_estimate=1850.0,
    target_profit_flip=35000.0,
    target_assignment_fee=12000.0,
)

result = analyze_wholesale_deal(deal)
import json
print(json.dumps(result, indent=2, default=str))

# ---- Expected output (abbreviated) ----
# {
#   "address": "1842 Linden Ave, Columbus, OH 43211",
#   "arv": 285000.0,
#   "erc": 47000.0,
#   "mao_70_rule": 152500.0,
#   "mao_custom_flip": 135200.0,
#   "exits": [
#     {"exit": "Wholesale Assignment", "your_offer_price": 140500, "projected_profit": 12000, "pencils": true},
#     {"exit": "Fix-and-Flip", "your_offer_price": 135200, "projected_profit": 35000, "pencils": true},
#     {"exit": "BRRRR", "your_offer_price": 152500, "cash_left_in": 19200, "dscr": 1.18, "pencils": false},
#     {"exit": "Wholetail", "your_offer_price": 216000, "projected_profit": -2400, "pencils": false}
#   ],
#   "recommendation": "PURSUE — best exit: Fix-and-Flip",
#   "lead_offer_price": 135200
# }
```

## 📤 OUTPUT FORMAT

**Output type:** Markdown deal-underwriting package + a separate one-page seller-facing offer summary.
**Delivery method:** Inline in chat (Standalone), or written to `deal_underwrite_<address>.md` + `seller_offer_<address>.md` in Cowork Task mode.

### EXAMPLE OUTPUT (filled with realistic numbers)

```markdown
# WHOLESALE DEAL UNDERWRITING — 1842 LINDEN AVE, COLUMBUS, OH 43211

**Underwritten:** 2026-05-10
**Analyst:** [Investor Name]
**Comp Confidence:** HIGH (6 valid comps within 0.4 mi / 92 days)

---

## 1. Subject Property

| Field | Value |
|---|---|
| Address | 1842 Linden Ave, Columbus, OH 43211 |
| Beds / Baths | 3 / 1.5 |
| Above-Grade SqFt | 1,380 |
| Year Built | 1958 |
| Condition Tier | Fair (cosmetic + dated mechanicals) |
| Occupancy | Vacant (3 months per neighbor) |

---

## 2. Comp Set (6 closed sales, 0.5mi / 180d)

| # | Address | Sold Date | Price | SqFt | $/SqFt | Beds/Baths | Status |
|---|---|---|---|---|---|---|---|
| 1 | 1729 Linden Ave | 2026-04-22 | $292,000 | 1,420 | $205.63 | 3/2 | VALID |
| 2 | 1908 Linden Ave | 2026-03-14 | $268,500 | 1,310 | $204.96 | 3/1.5 | VALID |
| 3 | 1645 Cleveland Ave | 2026-04-02 | $278,000 | 1,400 | $198.57 | 3/1.5 | VALID |
| 4 | 2104 Linden Ave | 2026-02-28 | $310,000 | 1,510 | $205.30 | 3/2 | VALID (post-flip) |
| 5 | 1812 Maynard Ave | 2026-03-30 | $264,000 | 1,290 | $204.65 | 3/1 | VALID |
| 6 | 1955 Cleveland Ave | 2026-01-19 | $255,000 | 1,360 | $187.50 | 3/1.5 | FLAGGED — older sale, pre-spring lift |

**Median $/SqFt: $204.96 | Mean: $201.10**
**Confidence: HIGH** — 5 strong + 1 flagged comp; median and mean within 2%.

---

## 3. ARV Calculation

```
Median $/SqFt × Subject SqFt = $204.96 × 1,380 = $282,845
Adjustments:
  + Subject has 1.5 baths (matches median) → $0
  − Subject condition Fair vs comps mostly Average → −5% = ($14,142)
  + Subject lot 0.18 acre vs comp avg 0.16 → +$3,000

ARV = $282,845 − $14,142 + $3,000 ≈ $271,700
ARV (rounded with confidence band): $285,000 (range $271,000 – $299,000)
```

⚠️ **NOTE:** Comp #4 was a post-flip sale at $310k — already excluded from condition baseline. ARV here represents post-rehab, market-condition value.

---

## 4. Estimated Repair Cost (ERC) — Medium Scope, 1,380 SqFt

| Trade | Scope | Cost |
|---|---|---|
| Roof | Tear-off + 30-yr architectural | $9,200 |
| HVAC | Full replace (3-ton + furnace) | $6,500 |
| Plumbing | Fixtures + sewer scope (no replace) | $3,500 |
| Electrical | Panel upgrade + GFCIs | $4,200 |
| Kitchen | Cabinets + quartz + appliances | $13,500 |
| Bathrooms (1.5) | Full primary + half refresh | $7,800 |
| Flooring | LVP throughout, $5.50/sqft × 1,380 | $7,590 |
| Paint | Interior + minor exterior | $4,200 |
| Exterior | Gutters + landscaping + minor siding | $4,500 |
| Misc / permits / dumpster | Standard | $3,000 |
| **Subtotal** | | **$63,990** |
| **Contingency (10%)** | | **$6,399** |
| **TOTAL ERC** | | **$70,389** |

⚠️ **FLAGGED:** Sewer scope not yet performed — recommend $2,500 reserve until inspected.

---

## 5. MAO Calculation

```
70% Rule MAO    = ($285,000 × 0.70) − $70,389 = $129,111
Custom-Margin MAO (flip with $35k profit target):
  ARV                       $285,000
  − Selling Costs (8%)      ($22,800)
  − ERC                      ($70,389)
  − Holding (4 mo @ 1.2%)   ($13,680)
  − Financing (HM 10%/2pt)  ($7,300)
  − Profit Target           ($35,000)
  = MAO                      $135,831

Conservative MAO: $129,111 (70% rule) | Aggressive MAO: $135,831 (custom margin)
LEAD OFFER: $128,500 (1% below conservative)
```

---

## 6. Exit Strategy Comparison

| Exit | Offer Price | Projected Profit | Capital Required | Timeline | Verdict |
|---|---|---|---|---|---|
| Wholesale Assignment | $117,000 | $12,000 fee | $5k EMD + closing | 7–30 days | GREEN |
| Fix-and-Flip | $128,500 | $35,000 | $58k down + $70k ERC reserve | 4–6 months | GREEN |
| BRRRR | $129,111 | $1,830/yr cash flow + $19k equity left in | $129k + $70k up front | 6–12 months | YELLOW (DSCR 1.18) |
| Wholetail | $216,000 | ($2,400) | n/a — does not pencil | n/a | RED |

**Best exit: FIX-AND-FLIP** — highest projected profit, deal also assignable as fallback.

---

## 7. Risk Flags

| Risk | Severity | Mitigation |
|---|---|---|
| Vacant 3+ months — possible vandalism/copper theft | MEDIUM | Walkthrough + photos within 48 hr of contract |
| Pre-1978 home (1958) — lead paint disclosure required | LOW | ⚠️ Standard EPA Lead Disclosure required at sale |
| Sewer line condition unknown (clay-era) | MEDIUM | $2,500 reserve until scope camera run |
| BRRRR DSCR 1.18 — below 1.25 lender minimum | MEDIUM | Either accept lower LTV (70%) or pass on BRRRR |
| Title status not yet pulled | HIGH | Order preliminary title before EMD release |

---

## 8. Capital Stack (assuming Fix-and-Flip exit)

| Item | Amount |
|---|---|
| Acquisition price | $128,500 |
| Hard money loan (75% LTC) | $96,375 |
| Cash down at close | $32,125 |
| ERC reserves | $70,389 |
| Closing costs (2%) | $2,570 |
| **Total cash-to-close** | **$105,084** |
| **Total at-risk capital** | **$105,084 + personal guarantee on HM loan** |

---

## 9. EXECUTIVE SUMMARY — GO/NO-GO

**RECOMMENDATION: PURSUE — Fix-and-Flip exit primary, Wholesale Assignment as fallback.**

ARV is HIGH-confidence at $285,000 (6 closed comps within 0.4 mi / 92 days, median $/sqft 204.96 with low dispersion). Medium rehab scope at $70,389 includes 10% contingency and is conservative against 1958-era mechanicals. The 70% Rule MAO is $129,111 and the custom-margin MAO at $35k profit target is $135,831 — lead offer of $128,500 captures both a $35k flip profit and a $12k assignment-fee fallback. BRRRR pencils only marginally (DSCR 1.18, below typical 1.25 lender threshold) and Wholetail does not pencil. Top risks: title status unverified, sewer line condition unknown.

**Lead with: $128,500. Walk-away above $135,000. Pull title and sewer scope within 5 days of acceptance.**

---

# SELLER-FACING ONE-PAGER

**OFFER ON 1842 LINDEN AVE — Columbus, OH**

We're prepared to offer **$128,500** for your property at 1842 Linden Ave, with the following terms:

- **Cash purchase** — no financing contingency, no appraisal contingency
- **Close in 21 days** from accepted offer
- **As-is** — no repair requests, no inspection objections
- **$2,500 earnest money** wired within 48 hours of mutual acceptance
- **Flexible closing date** — pick the day that works for you

Our offer reflects the work the home needs (mechanical updates, kitchen, bath, flooring) and the recent sale prices on Linden Ave and Cleveland Ave for similar homes. We close every contract we sign — references from past Columbus sellers available on request.

⚠️ This offer is good through Friday 5/15. After that we move to the next property.

---
```

## 🔐 PERMISSIONS & SETUP CHECKLIST

- [ ] **Comp data source:** Confirm read access to at least one of Zillow / Redfin / Realtor.com / MLS via RETS-RESO / PropStream / ATTOM Data / REISimpli — needed for closed comps within 0.5mi / 180d.
- [ ] **Rent estimate source (for BRRRR exit):** Zillow Rent Zestimate or Rentometer access — pasted by user or available in Cowork web fetch.
- [ ] **Public records access (for risk flags):** PropStream or ATTOM Data subscription; or county GIS/recorder's office direct lookup.
- [ ] **Hard money / private money lender terms:** Have your current lender's term sheet (rate, points, LTC) ready before activating the skill — defaults to 10% / 2 pts / 75% LTC if absent.
- [ ] **Compliance check:** Confirm your state's wholesaler licensing requirements (e.g., IL, OK, AR have specific wholesaler statutes as of 2026); the skill drafts the offer language but does NOT confirm your right to assign in your jurisdiction.
- [ ] **Optional integrations:** DealCheck or REISimpli for second-pass underwriting; n8n / Zapier to push the deal_summary.md into Follow Up Boss / kvCORE / Salesforce as a pipeline record.

## ✅ QUALITY SELF-CHECK

Before delivering any output to the user, Claude must internally verify every item below. Do not deliver output until all boxes can be checked:

- [ ] All required inputs were provided by the user or successfully inferred from context
- [ ] Every financial calculation has been shown with its formula and inputs visible
- [ ] Every data reference (comp, rate, regulation) has been sourced or flagged as an estimate
- [ ] Output exactly matches the format specified in the Output Format section — no improvisation
- [ ] Zero placeholder text (like "[INSERT NAME]" or "TBD") remains in the final output
- [ ] Any legal, compliance, or liability language has been surfaced to the user with a ⚠️ flag
- [ ] Output is immediately usable in a real business transaction without further editing
- [ ] Tone and terminology match the target profile — an attorney's output reads differently than a wholesaler's

## ⚠️ EDGE CASES & ESCALATION RULES

| Scenario | Claude's Exact Response |
|----------|------------------------|
| Required input not provided by user | Ask for the specific missing input before proceeding — do not guess or fabricate |
| Data is ambiguous or has multiple valid interpretations | Present both interpretations, state which Claude used, and why |
| Calculation produces a negative or nonsensical result | Flag it explicitly, show the math, and ask user to verify inputs |
| Legal or compliance risk is detected in the output | Insert a ⚠️ LEGAL FLAG block, describe the risk plainly, recommend consulting a licensed professional |
| Output would require information Claude cannot access (live MLS, locked database) | Deliver the maximum output possible with available data, list exactly what's missing and where to get it |
| Conflicting instructions between user input and skill SOP | Follow the SOP — flag the conflict to the user at the end of the output |
| Session approaching context limit mid-task (Cowork) | Write a `_PROGRESS_CHECKPOINT.md` file noting completed steps, current position, and what remains before the session ends |
| Property has significant unknowns (no interior photos, no walkthrough) | Build TWO ERC scenarios (light: $35–50/sqft, heavy: $65–85/sqft); present BOTH MAOs; recommend a 7-day inspection contingency on the offer; flag ARV/ERC confidence as MEDIUM |
| Comps are scarce (rural property, unique architectural style, micro-market) | Expand comp window to 1.0 mi / 270 days; flag Comp Confidence as LOW; recommend a paid BPO from a local broker; widen ARV band to ±10% |
| Deal pencils only on ONE exit (e.g., flip works but BRRRR/wholesale fail) | Still recommend PURSUE if profit clears the threshold, but explicitly note which exits closed the door and reduce lead offer by 3–5% to compensate for lost optionality |

## 📖 DOMAIN GLOSSARY

| Term | Definition |
|------|-----------|
| ARV | After Repair Value — the projected market value of a property after all repairs and improvements are completed, based on closed comparable sales |
| MAO | Maximum Allowable Offer — the highest price an investor should pay for a property to preserve a target profit margin, typically (ARV × 70%) − Repair Costs |
| ERC | Estimated Repair Cost — the conservative total cost of all repairs needed to bring a property to ARV condition; standard practice includes a 10% contingency |
| EMD | Earnest Money Deposit — funds submitted with a purchase offer to demonstrate buyer intent; typically 1–3% of purchase price, sometimes as low as $500–$2,500 in wholesale |
| LOI | Letter of Intent — a non-binding document outlining the proposed terms of a real estate transaction before a formal contract is executed |
| PSA | Purchase and Sale Agreement — the binding contract between buyer and seller detailing price, terms, contingencies, and closing date |
| Subject-To | Acquiring a property "subject to" the existing mortgage remaining in the seller's name — the buyer takes title while the seller's loan stays in place |
| Assignment of Contract | The transfer of a purchase contract from the original buyer (wholesaler) to a new end buyer, with the wholesaler earning an assignment fee |
| BRRRR | Buy-Rehab-Rent-Refinance-Repeat — investor playbook for converting flips into rental holdings via cash-out refi; typical refi LTV is 70–75% on DSCR loans |
| Wholetail | Light-cosmetic flip resold via MLS rather than wholesaled to an investor — captures more equity than a true wholesale but requires holding capital and 30–75 days |
| Hard Money | Short-term, asset-based loan from a private lender; typical 2026 terms are 9–12% interest, 1.5–3 points, 70–80% LTC, 6–12 month term |
| Transactional Funding | Same-day double-close funding used when an assignment cannot be done (lender restriction, deed restriction); typical fee is 1–2% of purchase price |
| Cash-on-Cash Return | Annual pre-tax cash flow ÷ total cash invested; the geared return metric for rentals; minimum acceptable target is typically 8% for SFR rentals |
| NOI | Net Operating Income — annual rental income minus operating expenses, excluding mortgage payments; the core valuation metric |
| CAP Rate | Capitalization Rate — NOI ÷ property value; the ungeared annual return; 2026 benchmarks: ~5% urban, 7% suburban, 9% rural for SFR |
| DSCR | Debt Service Coverage Ratio — NOI ÷ annual debt service; lenders typically require ≥1.25 for investment property loans; below 1.20 the deal is BRRRR-fragile |
| LTC / LTV | Loan-to-Cost / Loan-to-Value — hard money lenders quote LTC (% of acquisition+rehab); refi lenders quote LTV (% of ARV) |
| Comp Confidence | A HIGH/MEDIUM/LOW rating reflecting the quality of comp set; LOW confidence requires a paid BPO before acting on the ARV |
| Wholesaler Licensing | As of 2026, IL / OK / AR / VA require explicit wholesaler licensure or disclosure; other states regulate via real estate agency law — confirm before assigning |

## 🚀 HOW TO USE THIS SKILL

**Method A — Standalone Claude.ai Chat (recommended for daily underwriting):**
1. Open claude.ai → start a new conversation
2. Click the paperclip / attachment icon → attach this .md file
3. Type the trigger phrase: *"Run the numbers on this wholesale deal"*
4. Paste the property address, basic specs, and comp set when Claude asks
5. Review the executive summary before any offer goes out

**Method B — Claude Cowork Task (for batch underwriting and institutional teams):**
1. Open Claude Cowork on Mac → grant folder access to your deal pipeline directory
2. Drop a CSV of property addresses + comp links into the folder
3. Reference this file in your task description ("Underwrite every row using the Wholesale Deal Analyzer skill")
4. Approve Claude's plan; confirm the lead-offer prices on each deal_summary.md before they leave the folder

**Method D — Claude.ai Project (for institutional acquisition teams):**
1. Open your Claude.ai Project → upload this .md to the knowledge base
2. Every acquisition manager on the team can now activate the skill via the trigger phrase in Project chat
3. Standardize the team's MAO/ERC/exit math — no more analyst-by-analyst variance
