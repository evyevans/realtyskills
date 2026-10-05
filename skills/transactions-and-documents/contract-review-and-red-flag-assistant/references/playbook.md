# Source playbook

This playbook supplies task procedures and examples. Follow the working rules in the skill entry, verify current jurisdiction-specific claims, and treat examples as illustrative.

# Contract Review Assistant

Catch the contract risks that cost your clients thousands — before they sign. This skill reviews purchase agreements, listing contracts, buyer representation agreements, and addenda clause by clause, scoring each for risk level, identifying missing protections, flagging unreasonable timelines, and surfacing negotiation opportunities. The output is a structured risk report with an overall score, clause-by-clause analysis, recommended amendments, and talking points for the other party's agent. Built for listing agents and buyer's agents who want to protect their clients and demonstrate expertise at the offer table.

**Important Disclaimer:** This skill provides a real estate professional's analytical review, not legal advice. Always recommend that clients consult a licensed real estate attorney for complex legal questions, especially regarding title issues, easements, boundary disputes, or unusual contract clauses.

## 🧠 SKILL IDENTITY

**WHO this skill is for:**
A listing or buyer's agent reviewing a counter-offer at 9pm before signing; a team lead doing a final check on a junior agent's contract before brokerage compliance review; a brokerage owner running a weekly QA pass on the team's pending files; a transaction or business attorney pre-screening contracts before billable review hours.

**WHAT this skill does:**
Performs a clause-by-clause review of a real estate contract, scoring each clause for risk (LOW / MODERATE / HIGH / CRITICAL), surfacing missing standard clauses, identifying negotiation opportunities, and producing an action-item list with talking points for the client conversation. Output includes an overall risk score (0–100), a clause-by-clause matrix, missing-clauses list, negotiation opportunities ranked by leverage, action items, and a one-paragraph executive summary the agent can paste into the client email.

**WHERE to use this skill:**
Standalone chat for one-off counter-offer reviews; Cowork Task when reviewing a stack of contracts (brokerage QA day); Claude.ai Project for transaction-attorney teams who want every contract pre-screened to a consistent rubric before partner review.

**WHEN to activate this skill:**
The moment a counter-offer comes in; before signing any addendum; during the 5–10 day attorney-review window in IL/NY; when a wholesaler receives an assignment contract; when a property manager is reviewing a new lease before tenant signing; before any contract goes to compliance/broker review.

**WHY this skill matters:**
This workflow makes the required inputs and output structure explicit. Its numerical benchmarks are configurable assumptions, not validated performance claims.

**HOW this skill works (Overview):**
Claude reads the contract end-to-end, identifies the form template (CAR/TREC/FAR-BAR/etc.), runs a clause-by-clause risk pass, cross-references against the standard "missing clauses" library, scores overall risk, prioritizes negotiation opportunities by leverage and reversibility, and outputs a presentation-ready risk memo. Every flagged item includes a ⚠️ tag and the specific contract section reference.

## When to Use

- Reviewing an incoming offer on your listing before presenting to the seller
- Reviewing a purchase agreement before your buyer signs
- Evaluating a counter-offer to identify what changed and what it means
- Checking a listing agreement before a seller signs your representation contract
- Reviewing a buyer representation agreement before a buyer signs
- Analyzing addenda (inspection, appraisal, financing, HOA) for hidden risks
- Comparing multiple offers side by side to advise your seller
- Preparing talking points before a negotiation call with the other agent

## 📥 REQUIRED INPUTS

| Parameter | Type | Required | Description |
|---|---|---|---|
| contract_type | string | Yes | purchase-agreement, listing-agreement, buyer-representation, counter-offer, addendum, lease-option |
| representing | string | Yes | buyer, seller, or listing-agent (your role in the transaction) |
| contract_text | string | Yes | Full contract text OR a structured summary of key clauses (see Key Clause Fields below) |
| property_address | string | Yes | Subject property address |
| list_price | number | No | Listed price of the property |
| offer_price | number | No | Offered purchase price |
| market_conditions | string | No | seller-market, buyer-market, balanced (affects risk weighting) |
| state | string | No | State where the property is located (contract law varies by state) |
| days_on_market | number | No | How long the property has been listed (context for negotiation leverage) |
| multiple_offers | boolean | No | Whether there are competing offers (default: false) |

**Key Clause Fields (if providing structured summary):**

| Clause | Type | Description |
|---|---|---|
| earnest_money_amount | number | Earnest money deposit in USD |
| earnest_money_due_date | string | When the deposit is due |
| closing_date | string | Scheduled closing date |
| financing_type | string | conventional, FHA, VA, cash, hard-money |
| financing_contingency_days | number | Days buyer has to secure financing |
| inspection_contingency_days | number | Days buyer has to complete inspections |
| appraisal_contingency | boolean | Whether there is an appraisal contingency |
| appraisal_gap_coverage | number | Amount buyer agrees to cover if appraisal comes in low |
| title_review_days | number | Days for title review/objection |
| closing_cost_credits | number | Seller concessions in USD |
| home_warranty | boolean | Whether seller provides a home warranty |
| included_items | string | Personal property included in the sale |
| possession_date | string | When buyer takes possession |
| escalation_clause | string | Details of any escalation clause |
| contingencies_list | string | All contingencies listed in the contract |

## ⚙️ EXECUTION SOP

### Step 1: Clause Identification and Categorization

**What Claude does:** Parses the full contract text (PDF or pasted), enumerates every distinct clause, and assigns each to one of seven canonical categories (Financial / Timeline / Contingencies / Property Condition / Legal-Title / Liability / Miscellaneous).
**Tools / Resources needed:** Claude PDF reader (native chat drag-drop) or pasted text; the 7-category mapping table below; optional state-form template (CAR-RPA, TREC 1-4, FAR-BAR ASIS-7, NY Standard, IL-RES).
**Data source:** User-provided `contract_text` field plus `contract_type` and `state`.
**Output of this step:** A numbered list of every clause found, each tagged with its category and the exact section number from the contract.
**Cowork behavior:** PROCEED WITH ANALYSIS AND DRAFTING
**If this step fails or required data is missing:** If the contract is illegible (poor scan) or only partially provided, Claude lists exactly which sections it could read and asks the user to re-supply or paste the missing sections before proceeding.

Parse the contract and identify all clauses, categorizing each into one of these groups:

| Category | Examples | Risk Weight |
|---|---|---|
| **Financial** | Price, earnest money, financing, closing costs, appraisal gap | High |
| **Timeline** | Closing date, contingency deadlines, possession | Medium-High |
| **Contingencies** | Inspection, financing, appraisal, sale-of-home | High |
| **Property Condition** | As-is, repairs, warranties, disclosures | Medium |
| **Legal/Title** | Title insurance, survey, liens, easements | High |
| **Liability** | Default clauses, liquidated damages, mediation/arbitration | Medium |
| **Miscellaneous** | Included items, HOA, special stipulations | Low-Medium |

### Step 2: Risk Scoring Per Clause

**What Claude does:** Assigns a 1–5 risk score to each clause from the perspective of the user's role (buyer / seller / listing agent), using the risk-scoring factors table; flags every score of 4 or 5 with a ⚠️.
**Tools / Resources needed:** Risk scoring rubric (1–5 scale); risk factor table; brokerage / firm risk policy (if user supplied one).
**Data source:** Step 1 clause inventory + user's `representing` role + `market_conditions` + financial inputs (`list_price`, `offer_price`, `earnest_money_amount`, etc.).
**Output of this step:** A risk matrix — one row per clause — with score, ⚠️ tag where applicable, and a one-line rationale.
**Cowork behavior:** PROCEED WITH ANALYSIS AND DRAFTING
**If this step fails or required data is missing:** If a clause's risk depends on a value not provided (e.g., earnest money $ but no purchase price given), score the clause as MODERATE by default and explicitly note "needs `[field]` to refine."

Score each clause on a 1-5 risk scale based on who you represent:

| Score | Risk Level | Meaning |
|---|---|---|
| 1 | SAFE | Clause is standard, fair, and protects your client |
| 2 | LOW RISK | Minor concern, standard language, no action needed |
| 3 | MODERATE | Clause could be improved, consider negotiating |
| 4 | HIGH RISK | Clause creates significant exposure for your client |
| 5 | CRITICAL | Clause is dangerous, must be amended or removed before signing |

**Risk Scoring Factors:**

| Factor | Increases Risk | Decreases Risk |
|---|---|---|
| Earnest money | Above 3% of purchase price | Below 1% with strong contingencies |
| Inspection period | Less than 7 days | 10-14 days |
| Financing contingency | Less than 14 days | 21-30 days |
| Closing timeline | Less than 21 days (unless cash) | 30-45 days |
| Appraisal contingency | Absent (in financed deal) | Present with reasonable gap coverage |
| As-is clause | Present (for buyer) | Absent or with repair allowance |
| Possession before closing | Buyer takes possession pre-close | Possession at closing or post-close |
| Escalation clause | Unlimited or very high cap | Reasonable cap with proof requirement |
| Default clause | Only benefits one party | Mutual remedies |
| Attorney review | Absent in state where common | Present with reasonable timeline |

### Step 3: Missing Clause Detection

**What Claude does:** Cross-references the clauses found in Step 1 against the canonical "expected clauses" library for the contract type and user's role, flagging anything absent.
**Tools / Resources needed:** Missing-clause library tables (buyer-side / seller-side, below); state-form expected sections (CAR/TREC/FAR-BAR/etc.).
**Data source:** Step 1 clause inventory + `contract_type` + `state` + `representing`.
**Output of this step:** A "Missing Clauses" table with each missing clause, its risk-if-missing rating, and recommended action.
**Cowork behavior:** PROCEED WITH ANALYSIS AND DRAFTING
**If this step fails or required data is missing:** If state/form is unspecified, run a generic residential-PSA expectation list and add a note: "Run again with state-specific form for jurisdiction-aware results."

Check for clauses that should be present but are not. Missing protections are often more dangerous than bad clauses:

**For Buyer Representation:**

| Expected Clause | Risk if Missing |
|---|---|
| Inspection contingency | Buyer waives right to discover defects |
| Financing contingency | Buyer at risk of losing earnest money if loan falls through |
| Appraisal contingency | Buyer may need to cover gap out of pocket or lose deposit |
| Title contingency | Buyer may inherit title defects, liens, or encumbrances |
| Home warranty | Buyer has no protection against system failures post-close |
| Attorney review (if applicable by state) | Buyer signs without legal review |
| Lead-based paint disclosure (pre-1978 homes) | Federal violation |
| HOA document review period (condos/HOA communities) | Buyer cannot review rules/financials before committing |
| Property disclosure statement | Seller has not disclosed known defects |

**For Seller Representation:**

| Expected Clause | Risk if Missing |
|---|---|
| Earnest money with reasonable amount | Buyer has minimal skin in the game |
| Proof of funds or pre-approval letter | Unqualified buyer tying up the property |
| Liquidated damages clause | Unclear remedy if buyer defaults |
| Financing commitment deadline | Buyer can delay indefinitely |
| Closing cost credit limit | Open-ended seller concessions |
| Included/excluded items list | Disputes over fixtures and personal property |
| Clear closing date | No timeline accountability |

### Step 4: Negotiation Opportunity Identification

**What Claude does:** Re-reads the contract through a leverage lens, identifying clauses where the user can extract value (price, timeline, contingency, EMD increase, possession flexibility, etc.) and ranks each by potential dollar value and reversibility.
**Tools / Resources needed:** Negotiation-opportunity reference table (below); user's `market_conditions`, `days_on_market`, `multiple_offers` inputs.
**Data source:** Step 1–3 outputs + market context inputs.
**Output of this step:** A "Negotiation Opportunities" table with each opportunity, dollar-value estimate, and exact talking-point script for the other agent.
**Cowork behavior:** CONFIRM BEFORE PROCEEDING — show user the proposed negotiation list before generating the full Step 5 risk memo, so the user can deselect items they don't want raised.
**If this step fails or required data is missing:** If market conditions are unknown, default to "balanced market" leverage assumptions and flag that recommendations may shift if user clarifies the market context.

Beyond risk, identify clauses where your client can gain leverage:

| Opportunity Type | Example | Potential Value |
|---|---|---|
| Price adjustment | Inspection findings support repair credit | $5,000-$30,000 |
| Timeline extension | Buyer needs more time for financing | Goodwill + clean closing |
| Contingency removal | Buyer offers to waive appraisal contingency | Stronger offer position |
| Earnest money increase | Buyer increases deposit to strengthen offer | Demonstrates commitment |
| Closing cost reallocation | Shift closing costs from seller to buyer (or vice versa) | $3,000-$10,000 |
| Possession flexibility | Early possession or rent-back agreement | Solves logistics for both parties |
| Repair vs. credit | Credit at closing instead of repairs | Simpler, fewer re-negotiation points |

### Step 5: Overall Risk Assessment

**What Claude does:** Aggregates all clause-level risk scores into a weighted 0–100 overall risk score and a banded label (LOW / MODERATE / HIGH / CRITICAL); produces the final structured risk memo.
**Tools / Resources needed:** The Python `aggregate_risk()` function below (Claude runs the math inline); the risk-band scale.
**Data source:** Step 2 clause-level scores + Step 3 missing-clause severity adjustments.
**Output of this step:** Overall score, band, list of CRITICAL clauses, "recommend_attorney_review" boolean, and the formatted output memo.
**Cowork behavior:** PROCEED WITH ANALYSIS AND DRAFTING
**If this step fails or required data is missing:** If the contract has fewer than 5 reviewable clauses extracted, output `band: INSUFFICIENT_DATA` and ask the user to re-supply the full contract text.

Calculate the overall contract risk score:

```
Overall Risk = (sum of all clause risk scores) / (number of clauses scored) x 20

Scale:
0-25:  LOW RISK — Contract is well-structured and protective
26-50: MODERATE RISK — Some clauses need attention before signing
51-75: HIGH RISK — Multiple clauses create significant exposure
76-100: CRITICAL RISK — Do not sign without major amendments
```

**Risk Aggregation — Implementation Reference**

Claude uses the following weighted aggregation logic when computing the overall risk score across clauses. Each clause carries both a `risk_level` (qualitative) and a `weight` (1 = boilerplate, 5 = deal-determinative). This ensures a CRITICAL liquidated-damages clause cannot be averaged-away by a stack of LOW boilerplate clauses.

```python
# Contract Risk Aggregator — weighted clause scoring
def aggregate_risk(clauses: list[dict]) -> dict:
    """
    clauses: list of {clause_name, risk_level, weight}
      risk_level in {'LOW', 'MODERATE', 'HIGH', 'CRITICAL'}
      weight: 1 (boilerplate) to 5 (deal-determinative)
    Returns overall risk score 0–100, banded.
    """
    risk_points = {'LOW': 0, 'MODERATE': 25, 'HIGH': 60, 'CRITICAL': 100}
    if not clauses:
        return {"score": 0, "band": "INSUFFICIENT_DATA"}
    weighted_sum = sum(risk_points[c['risk_level']] * c['weight'] for c in clauses)
    weight_total = sum(c['weight'] for c in clauses)
    score = round(weighted_sum / weight_total)
    band = (
        "LOW"      if score < 20 else
        "MODERATE" if score < 45 else
        "HIGH"     if score < 75 else
        "CRITICAL"
    )
    critical_clauses = [c['clause_name'] for c in clauses if c['risk_level'] == 'CRITICAL']
    return {
        "score": score,
        "band": band,
        "critical_clauses": critical_clauses,
        "recommend_attorney_review": band in ("HIGH", "CRITICAL")
    }

# Example usage:
clauses = [
    {"clause_name": "Earnest Money", "risk_level": "MODERATE", "weight": 5},
    {"clause_name": "Financing Contingency", "risk_level": "HIGH",     "weight": 5},
    {"clause_name": "Inspection Period",     "risk_level": "LOW",      "weight": 4},
    {"clause_name": "Liquidated Damages",    "risk_level": "CRITICAL", "weight": 5},
]
result = aggregate_risk(clauses)
# → score: 70, band: HIGH, recommend_attorney_review: True
```

When `recommend_attorney_review` returns `True`, Claude inserts a ⚠️ ATTORNEY REVIEW REQUIRED block at the top of the output memo and lists the top 3 questions the user should ask the attorney.

## 📤 OUTPUT FORMAT

```
# Contract Review: [property_address]

**Contract Type:** [type]
**Your Role:** [buyer-agent / seller-agent / listing-agent]
**Review Date:** [date]

**DISCLAIMER:** This review is provided as a real estate professional's analysis. It does not constitute legal advice. Clients should consult a licensed real estate attorney for legal questions.

---

## Overall Risk Score: [X]/100 — [LOW/MODERATE/HIGH/CRITICAL]

[1-2 sentence summary of the overall contract quality from your client's perspective]

---

## Risk Summary

| Status | Count | Clauses |
|---|---|---|
| SAFE (1) | [N] | [clause names] |
| LOW RISK (2) | [N] | [clause names] |
| MODERATE (3) | [N] | [clause names] |
| HIGH RISK (4) | [N] | [clause names] |
| CRITICAL (5) | [N] | [clause names] |

---

## Clause-by-Clause Analysis

### 1. [Clause Name] — Risk: [score]/5 [SAFE/LOW/MODERATE/HIGH/CRITICAL]

**Current Language:** [quote or summary of the clause]

**Analysis:** [what this clause means for your client, in plain English]

**Risk Factors:** [specific concerns]

**Recommendation:** [keep as-is / request amendment / add language / remove]

**Suggested Amendment:** [exact language to propose, if applicable]

**Talking Point for Other Agent:**
> "[What to say to the other agent to justify this request]"

---

[Repeat for each clause]

---

## Missing Clauses

| Missing Clause | Risk Level | Why It Matters | Recommended Action |
|---|---|---|---|
| [clause] | [HIGH/CRITICAL] | [explanation] | [add this language] |
| ... | ... | ... | ... |

---

## Negotiation Opportunities

| Opportunity | Potential Value | Approach |
|---|---|---|
| [opportunity] | $[value or description] | [how to raise it with the other side] |
| ... | ... | ... |

---

## Action Items

1. **MUST DO before signing:** [critical items]
2. **SHOULD negotiate:** [important but not deal-breaking items]
3. **NICE TO HAVE:** [items that improve your client's position]

---

## Talking Points Summary

[3-5 bullet points your agent can use in the next conversation with the other agent or their client, summarizing the key requests and justifications]
```

## Methodology

**GUARD Framework (Gap-Understand-Assess-Recommend-Defend)**

The GUARD framework approaches contract review in five phases: identify Gaps in protection (missing clauses), Understand the intent and impact of each existing clause, Assess the risk from your client's perspective, Recommend specific amendments with exact language, and prepare Defend talking points so the agent can justify each request to the other party. This methodology is adapted from corporate due diligence practices and simplified for residential real estate transactions, where the typical purchase agreement contains 15-25 reviewable clauses that can collectively represent $10,000-$100,000 of risk exposure.

## Advanced Configuration

| Parameter | Default | Range | Description |
|---|---|---|---|
| risk_tolerance | moderate | conservative/moderate/aggressive | How strictly to flag risk (conservative flags more) |
| include_legal_disclaimer | true | true/false | Include disclaimer that this is not legal advice |
| state_specific_notes | true | true/false | Add state-specific legal context where applicable |
| compare_to_standard_form | true | true/false | Note deviations from standard state/association forms |
| multiple_offer_mode | false | true/false | Adjust analysis for competitive offer situations |
| include_counter_offer_strategy | true | true/false | Suggest counter-offer approach if applicable |
| earnest_money_risk_threshold | 3% | 1-5% | Percentage of purchase price above which EM is flagged |
| inspection_minimum_days | 10 | 5-14 | Minimum acceptable inspection period |
| financing_minimum_days | 21 | 14-30 | Minimum acceptable financing contingency period |
| closing_minimum_days | 30 | 14-45 | Minimum acceptable days to close |

## Example

**Input:**
```
contract_type: purchase-agreement
representing: seller
property_address: 782 Magnolia Ave, San Antonio, TX 78209
list_price: 475000
offer_price: 460000
market_conditions: balanced
state: TX
days_on_market: 22
multiple_offers: false

Key Clauses:
  earnest_money_amount: 5000
  earnest_money_due_date: "within 3 business days of execution"
  closing_date: 2026-04-15
  financing_type: conventional
  financing_contingency_days: 21
  inspection_contingency_days: 10
  appraisal_contingency: true
  appraisal_gap_coverage: 0
  title_review_days: 15
  closing_cost_credits: 8000
  home_warranty: true (buyer requests seller-paid, $650 cap)
  included_items: "refrigerator, washer, dryer, window blinds, mounted TV in living room"
  possession_date: "at closing"
  escalation_clause: none
  contingencies_list: "inspection, financing, appraisal, title"
```

**Output:**
```
# Contract Review: 782 Magnolia Ave, San Antonio, TX 78209

**Contract Type:** Purchase Agreement
**Your Role:** Seller's Agent
**Review Date:** 2026-02-12

**DISCLAIMER:** This review is provided as a real estate professional's analysis. It does not constitute legal advice. Clients should consult a licensed real estate attorney for legal questions.

---

## Overall Risk Score: 42/100 — MODERATE RISK

This offer is structured reasonably but has several areas where your seller is giving up value unnecessarily. The earnest money is low relative to the purchase price, the closing cost credit is generous in a balanced market, and the included personal property list is broader than standard. With targeted negotiation on 3-4 points, this offer can be improved by $8,000-$15,000 in your seller's favor.

---

## Risk Summary

| Status | Count | Clauses |
|---|---|---|
| SAFE (1) | 3 | Closing date, financing contingency, title review |
| LOW RISK (2) | 2 | Inspection contingency, possession |
| MODERATE (3) | 3 | Purchase price, appraisal gap, home warranty |
| HIGH RISK (4) | 2 | Earnest money, closing cost credits |
| CRITICAL (5) | 1 | Included personal property |

---

## Clause-by-Clause Analysis

### 1. Purchase Price — Risk: 3/5 MODERATE

**Current Language:** $460,000 (3.2% below list price of $475,000)

**Analysis:** In a balanced market with 22 DOM, a 3.2% discount is within reasonable negotiation range but at the aggressive end. The buyer is testing your seller's flexibility.

**Risk Factors:** If seller accepts as-is, they leave potential money on the table, especially considering the additional concessions (closing credits, warranty, personal property) that stack on top of the price reduction.

**Recommendation:** Counter at $470,000 or accept $460,000 only if other concessions are reduced.

**Talking Point for Other Agent:**
> "We appreciate the offer. At 22 days on market, we have had steady showing activity and the price reflects the recent upgrades. We can work with the buyer on price if we tighten up some of the other terms."

---

### 2. Earnest Money — Risk: 4/5 HIGH RISK

**Current Language:** $5,000 due within 3 business days of execution

**Analysis:** At $5,000 on a $460,000 offer, the earnest money is only 1.1% of the purchase price. In Texas, the standard range is 1-3%, and in a balanced market, 2% ($9,200) is reasonable. Low earnest money gives the buyer a cheap exit if they get cold feet.

**Risk Factors:** If the buyer defaults, $5,000 is your seller's only liquidated damages. That barely covers 22+ days of carrying costs, additional market time, and the stigma of a failed contract.

**Recommendation:** Counter at $10,000 (2.2% of offer price) minimum.

**Suggested Amendment:** "Earnest money deposit shall be $10,000, delivered to the title company within 2 business days of the effective date."

**Talking Point for Other Agent:**
> "We need the earnest money to reflect the buyer's commitment. At $460K, $10,000 is just over 2% — very standard for this price range. It protects both parties by ensuring serious intent."

---

### 3. Closing Cost Credits — Risk: 4/5 HIGH RISK

**Current Language:** Seller to credit buyer $8,000 toward closing costs

**Analysis:** $8,000 is 1.7% of the offer price. Combined with the $15,000 price discount, the seller's effective concession is $23,000 (4.8% of list price). In a balanced market, this is excessive. Total seller concessions above 3% should be scrutinized.

**Risk Factors:** The buyer may be cash-constrained if they need $8,000 in closing cost help. This could signal financing risk.

**Recommendation:** Counter at $4,000 maximum, or eliminate entirely and lower the price further if the buyer needs cash-to-close flexibility.

**Talking Point for Other Agent:**
> "We can be flexible on closing cost credits, but at $8,000 combined with the price reduction, the total concession is significant. Can your buyer reduce the credit request to $4,000? Alternatively, we can look at the price if that is more helpful for their loan structure."

---

### 4. Appraisal Gap Coverage — Risk: 3/5 MODERATE

**Current Language:** Buyer offers $0 in appraisal gap coverage

**Analysis:** If the appraisal comes in below $460,000, the buyer has no obligation to cover the difference. The seller must either reduce the price to the appraised value, or the deal falls apart. In a balanced market, this is somewhat standard, but your seller should understand the risk.

**Risk Factors:** If the property appraises at $445,000, the seller faces a $15,000 gap with no buyer commitment to cover any portion.

**Recommendation:** Request $5,000-$10,000 in gap coverage as part of the counter.

**Suggested Amendment:** "Buyer agrees to cover up to $7,500 of any shortfall between the appraised value and the contract price."

---

### 5. Included Personal Property — Risk: 5/5 CRITICAL

**Current Language:** "Refrigerator, washer, dryer, window blinds, mounted TV in living room"

**Analysis:** The refrigerator, washer, dryer, and window blinds are standard inclusions in Texas. However, the mounted TV is personal property and should NOT be included without explicit seller agreement and a dollar value assigned. If the TV is a $2,000+ unit, this is an undisclosed cost to the seller.

**Risk Factors:** If the seller's TV is a high-end model (65"+ OLED, $1,500-$4,000 value), including it without negotiation is giving away money. Additionally, leaving a mounted TV creates liability — if it falls after closing, who is responsible?

**Recommendation:** Strike the mounted TV from included items. If the buyer insists, assign a specific dollar value and either increase the offer price accordingly or include it as a separate bill of sale.

**Suggested Amendment:** Remove "mounted TV in living room" from included items. Alternatively: "Mounted TV in living room included at an agreed value of $[X], to be conveyed via separate bill of sale."

**Talking Point for Other Agent:**
> "We need to remove the mounted TV from the inclusions. It is personal property, not a fixture. If your buyer wants it, we are happy to negotiate a separate price for it."

---

### 6. Inspection Contingency — Risk: 2/5 LOW RISK

**Current Language:** 10-day inspection period

**Analysis:** 10 days is standard in Texas. Gives the buyer adequate time for a general inspection plus any specialist inspections (termite, foundation, pool, etc.).

**Recommendation:** Accept as-is. No changes needed.

---

### 7. Financing Contingency — Risk: 1/5 SAFE

**Current Language:** 21-day financing contingency, conventional loan

**Analysis:** 21 days for conventional financing is standard and provides the buyer adequate time to finalize their loan. Conventional loans are generally reliable with pre-approved buyers.

**Recommendation:** Accept as-is. Request a copy of the pre-approval letter to verify qualification.

---

### 8. Closing Date — Risk: 1/5 SAFE

**Current Language:** April 15, 2026 (approximately 62 days from effective date)

**Analysis:** 60+ days provides ample time for all contingencies, financing, title work, and closing. No rushing risk.

**Recommendation:** Accept as-is.

---

### 9. Home Warranty — Risk: 3/5 MODERATE

**Current Language:** Seller-paid home warranty, $650 cap

**Analysis:** Seller-paid home warranties are common in Texas. $650 is within the typical range ($450-$700). However, this is another seller concession that stacks on top of the price reduction and closing credits.

**Recommendation:** Accept if other concessions are reduced. Use as a negotiation chip — keep the warranty if the buyer reduces closing cost credit request.

---

### 10. Title Review — Risk: 1/5 SAFE

**Current Language:** 15-day title review period

**Analysis:** Standard in Texas. Allows buyer to review title commitment and raise objections.

**Recommendation:** Accept as-is.

---

## Missing Clauses

| Missing Clause | Risk Level | Why It Matters | Recommended Action |
|---|---|---|---|
| Pre-approval letter attachment | HIGH | No proof buyer is qualified — could waste 30+ days | Request pre-approval letter within 48 hours of execution |
| Property condition at closing | MODERATE | No language requiring buyer to leave property in same condition during inspections | Add standard "maintain property condition" clause |
| Backup offer provision | LOW | Seller cannot accept backup offers | Add right to continue showing and accept backup offers |

---

## Negotiation Opportunities

| Opportunity | Potential Value | Approach |
|---|---|---|
| Counter price to $470,000 | +$10,000 | "Steady showing activity supports value closer to list" |
| Reduce closing cost credit to $4,000 | +$4,000 saved | "Meet in the middle on concessions" |
| Increase earnest money to $10,000 | Risk reduction | "Standard for this price range" |
| Add $7,500 appraisal gap coverage | Risk reduction | "Shows buyer's commitment to the price they are offering" |
| Remove mounted TV from inclusions | $1,500-$4,000 saved | "Personal property, not a fixture" |

**Total potential improvement from negotiation: $15,500 - $18,000**

---

## Action Items

1. **MUST DO before signing:**
   - Strike mounted TV from included items
   - Request pre-approval letter within 48 hours
   - Counter earnest money to $10,000

2. **SHOULD negotiate:**
   - Counter price to $470,000
   - Reduce closing cost credit to $4,000
   - Add $7,500 appraisal gap coverage

3. **NICE TO HAVE:**
   - Add backup offer provision
   - Add property condition maintenance clause

---

## Talking Points Summary

- "We appreciate the offer and want to work with your buyer. We need to adjust a few terms to make this work for our seller."
- "The total concession package — $15K price discount, $8K closing credit, $650 warranty, plus personal property — is over $24K in effective concessions. In a balanced market with 22 DOM, we need to tighten that up."
- "We can be flexible on price OR closing credits, but not both at these levels. Let's find the combination that works for both sides."
- "The mounted TV is personal property and needs to come off the inclusions. Happy to discuss separately if your buyer really wants it."
- "We need the earnest money to reflect the seriousness of the offer — $10K is very standard at this price point."
```

## Edge Cases & Best Practices

- **As-Is Contracts (Buyer's Perspective):** When reviewing an as-is contract for a buyer, ensure the buyer understands that "as-is" does NOT mean they waive the right to inspect — it means the seller will not make repairs. The buyer should still have an inspection contingency and the right to walk away if defects are discovered. If the as-is contract eliminates the inspection contingency entirely, flag it as CRITICAL.

- **Cash Offers Without Appraisal Contingency:** Cash buyers often waive appraisal contingencies, which is standard. However, ensure the cash buyer has provided proof of funds. A cash offer without proof of funds and without an appraisal contingency is high risk — the buyer may not have the capital to close.

- **Escalation Clauses in Multiple-Offer Scenarios:** When reviewing an offer with an escalation clause, check for: a cap amount, a requirement to show proof of the competing offer, and whether the escalation increment is reasonable. Open-ended escalation clauses with no cap expose the buyer to overpaying by an unpredictable amount.

- **Rent-Back Agreements:** If the seller needs to remain in the property after closing (rent-back), ensure the rent-back clause includes: daily rent amount, security deposit, maximum duration, insurance requirements, and holdover penalties. Missing these details creates liability for both parties.

- **New Construction Contracts:** Builder contracts are heavily weighted in the builder's favor and often contain non-standard clauses: no inspection contingency, builder-selected closing date, material substitution rights, and arbitration-only dispute resolution. Flag ALL deviations from standard residential purchase agreements.

- **State-Specific Requirements:** Contract law varies significantly by state. Key variations include: attorney review requirements (NJ, IL, CT), transfer tax responsibility (varies), disclosure obligations (vary), and default remedy structures. Always note when a clause may have state-specific implications and recommend local attorney review for unusual provisions.

## Integration

This skill connects with the broader real estate agent toolkit:

- **Skill 01 (Lead Qualification Engine):** When a READY NOW lead moves to the offer stage, use the Contract Review to ensure the first offer is bulletproof — catching issues before signing prevents deals from falling apart during the transaction.
- **Skill 03 (Market Analysis Reporter):** CMA data supports contract negotiations — when the other agent pushes back on your pricing counter, reference the CMA to justify the number with market data rather than emotion.
- **Skill 04 (Client Follow-Up Sequencer):** For under-contract clients, use the Sequencer to generate milestone-based touchpoints that reference specific contract deadlines — "Your inspection contingency expires on [date], here's what we need to do before then."
- **Skill 05 (Objection Handler Coach):** When the other agent objects to your counter-offer terms, use the Objection Handler for negotiation scripts: "I understand the concern about the earnest money increase, but here's why it protects both parties..."
- **Skill 07 (Social Media Content Planner):** Create educational content about contract red flags for your social media — posts like "3 contract clauses every buyer should understand" position you as an expert and generate engagement.

## 🔐 PERMISSIONS & SETUP CHECKLIST

- [ ] **Contract source (one-time):** Have a PDF, scanned image, or pasted text of the contract ready. Claude reads PDFs natively in chat (drag-drop) or accepts pasted text.
- [ ] **State / form template (recommended):** On first activation, tell Claude the contract form (CAR-RPA, TREC 1-4, FAR-BAR ASIS-7, NY Standard, IL-RES, etc.). The skill is more accurate when it knows the parent template's standard sections.
- [ ] **Brokerage / firm risk policy (optional but recommended):** If your firm has a specific list of unacceptable terms (e.g., "no liquidated damages > 10% of purchase price"), paste it once; Claude will auto-flag violations on every subsequent review.
- [ ] **Disclaimer (mandatory):** This skill provides risk-screening, not legal advice. Output is for licensed agent / attorney review only. The skill includes this disclaimer in every output by default.

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

| Edge Case | Claude's Response |
|---|---|
| Required input not provided by user | Ask for the specific missing input before proceeding — do not guess or fabricate |
| Data is ambiguous or has multiple valid interpretations | Present both interpretations, state which Claude used, and why |
| Calculation produces a negative or nonsensical result | Flag it explicitly, show the math, and ask user to verify inputs |
| Legal or compliance risk is detected in the output | Insert a ⚠️ LEGAL FLAG block, describe the risk plainly, recommend consulting a licensed professional |
| Output would require information Claude cannot access (live MLS, locked database) | Deliver the maximum output possible with available data, list exactly what's missing and where to get it |
| Conflicting instructions between user input and skill SOP | Follow the SOP — flag the conflict to the user at the end of the output |
| Session approaching context limit mid-task (Cowork) | Write a `_PROGRESS_CHECKPOINT.md` file noting completed steps, current position, and what remains before the session ends |
| Contract is in a state with mandatory attorney review (IL, NY, NJ, etc.) | Output explicitly states "Attorney review required by state law — this output supplements, does not replace, your attorney's review" and surfaces top 3 questions the user should ask their attorney |
| Contract contains an "as-is" clause combined with no inspection contingency | CRITICAL risk flag — surface plainly, refuse to characterize the deal as low-risk regardless of other terms, recommend either adding inspection or walking |

## 📖 DOMAIN GLOSSARY

| Term | Definition |
|---|---|
| **PSA (Purchase & Sale Agreement)** | The primary contract between buyer and seller setting out price, terms, contingencies, and closing date. The most common contract this skill reviews. |
| **EMD (Earnest Money Deposit)** | Cash the buyer puts up to demonstrate good faith. Typically 1–3% of purchase price; held in escrow until closing or default. |
| **LOI (Letter of Intent)** | Pre-contract document outlining proposed terms; usually non-binding but creates negotiation expectations. Common in commercial and large residential deals. |
| **Contingency** | A condition that must be satisfied for the contract to proceed (financing, inspection, appraisal, sale-of-home). The buyer's primary protections. |
| **Concession** | Money or value the seller gives the buyer at closing (closing cost credits, repair credits, paid warranty). Stacks against the seller's net proceeds. |
| **Clear-to-Close (CTC)** | Lender confirmation that all underwriting conditions are met and the loan is ready to fund. The "green light" for closing. |
| **Title Commitment** | The title company's preliminary report showing what it will insure, including any liens, easements, or defects that must be cleared. |
| **RESPA (Real Estate Settlement Procedures Act)** | Federal law governing closing-cost disclosure and prohibiting kickbacks on settlement services. |
| **TRID (TILA-RESPA Integrated Disclosure)** | Federal rule requiring the Loan Estimate (within 3 days of application) and Closing Disclosure (3 business days before closing). |
| **Escrow** | Neutral third-party holding of funds and documents until conditions are met. Earnest money sits in escrow until closing or default. |
| **Subject-To** | A creative-finance structure where a buyer takes title "subject to" the existing mortgage staying in place. High legal risk; usually requires attorney involvement. |
| **Assignment of Contract** | The wholesaler's tool — assigning the buyer's rights under a PSA to a third party for a fee. State laws vary on disclosure requirements. |

## 🚀 HOW TO USE THIS SKILL

**Method A — Standalone Claude.ai Chat (recommended):**
1. Open claude.ai → start a new conversation
2. Click the paperclip icon → attach this .md file
3. Type the trigger phrase shown in the front matter
4. Provide the Required Inputs when Claude asks
5. Review output before any live use

**Method B — Claude Cowork Task:**
1. Open Claude Cowork on Mac → grant folder access
2. Reference this file in your task description
3. Type the trigger phrase as your task instruction
4. Approve Claude's plan; confirm any "CONFIRM BEFORE PROCEEDING" steps

**Method D — Claude.ai Project (team deployment):**
1. Open your Claude.ai Project → upload this .md to the knowledge base
2. Any team member can now activate the skill via the trigger phrase in Project chat
