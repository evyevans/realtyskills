# Source playbook

This playbook supplies task procedures and examples. Follow the working rules in the skill entry, verify current jurisdiction-specific claims, and treat examples as illustrative.

# Comparative Market Analysis Reporter

Generate a professional, client-ready Comparative Market Analysis (CMA) report in minutes. This skill takes a subject property and 3-6 comparable sales, calculates adjusted price-per-square-foot values, analyzes market trends (days on market, absorption rate, list-to-sale ratio), and produces a pricing recommendation with three strategies: aggressive, market value, and conservative. Built for listing agents who need to win listing appointments, and buyer's agents who need to justify offer prices to clients. The output is formatted for direct client presentation — clean, professional, and backed by data.

## 🧠 SKILL IDENTITY

**WHO this skill is for:**
A listing agent or buyer's agent preparing for a listing presentation in 24–48 hours; an investor evaluating ARV before submitting an offer; a team lead reviewing pricing on a junior agent's listing before MLS go-live; a brokerage owner running a quality pass on team listings before they go to market.

**WHAT this skill does:**
Produces a broker-grade Comparative Market Analysis report with subject-property summary, 6–10 ranked comparable sales (with adjustments shown), price-per-square-foot analysis, market-condition narrative (DOM trend, list-to-sale ratio, inventory direction), and a defensible pricing recommendation with three price scenarios (aggressive / market / conservative) and the reasoning behind each — formatted to drop directly into a listing presentation deck or buyer offer-strategy memo.

**WHERE to use this skill:**
Standalone Claude.ai chat for solo agents working a single listing; Cowork Task mode when running CMAs on a portfolio of 5+ properties (institutional flippers, brokerage acquisitions); Claude.ai Project for teams who want every CMA to follow the same adjustment methodology.

**WHEN to activate this skill:**
After collecting comp data the night before a listing presentation; immediately upon a wholesaler getting under contract on a flip (to validate ARV); when an existing listing has been on the market 14+ days with no offers (price-reduction defense); during a buyer's offer strategy meeting on a competitive property.

**WHY this skill matters:**
This workflow makes the required inputs and output structure explicit. Its numerical benchmarks are configurable assumptions, not validated performance claims.

**HOW this skill works (Overview):**
Claude reads the subject property and the comp set the user provides, filters comps to those that meet defensible criteria (closed within 180 days, within 0.5 miles, similar bed/bath/sqft/condition), runs a per-feature adjustment grid (lot, garage, age, condition, view, etc.), calculates a price-per-square-foot range, narrates the market context, and outputs three price points with explicit reasoning. The output is presentation-ready.

## When to Use

- Preparing for a listing presentation to win a new seller client
- Advising a seller on pricing strategy before going live on MLS
- Helping a buyer determine a fair offer price on a property they want
- Responding to a seller who says "my Zestimate says it's worth more"
- Justifying a price reduction recommendation to a seller after 30+ days on market
- Comparing the subject property against recent sales when an appraiser challenges your price
- Presenting market data to a FSBO to demonstrate the value of professional representation
- Quarterly market updates for your sphere of influence and farming area

## 📥 REQUIRED INPUTS

| Parameter | Type | Required | Description |
|---|---|---|---|
| subject_address | string | Yes | Full address of the subject property |
| subject_beds | number | Yes | Number of bedrooms |
| subject_baths | number | Yes | Number of bathrooms |
| subject_sqft | number | Yes | Total living square footage |
| subject_lot_size | string | No | Lot size (acres or sqft) |
| subject_year_built | number | Yes | Year the property was built |
| subject_condition | string | Yes | Condition: excellent, good, average, fair, poor |
| subject_features | string | No | Standout features: pool, garage, renovated kitchen, etc. |
| subject_garage | string | No | Garage type: 2-car-attached, 1-car-detached, carport, none |
| comparables | array | Yes | Array of 3-6 comparable sales (see Comparable Fields below) |
| market_area | string | Yes | Neighborhood, subdivision, or zip code for market trends |
| current_market_type | string | No | seller-market, buyer-market, balanced (default: balanced) |
| agent_name | string | No | Your name for the report header |
| brokerage_name | string | No | Your brokerage name for branding |

**Comparable Fields (for each comp):**

| Field | Type | Required | Description |
|---|---|---|---|
| comp_address | string | Yes | Full address of the comparable sale |
| sale_price | number | Yes | Actual sold price |
| sale_date | string | Yes | Date the sale closed (YYYY-MM-DD) |
| beds | number | Yes | Bedrooms |
| baths | number | Yes | Bathrooms |
| sqft | number | Yes | Living square footage |
| lot_size | string | No | Lot size |
| year_built | number | Yes | Year built |
| condition | string | Yes | Condition at time of sale |
| days_on_market | number | Yes | DOM from listing to contract |
| list_price | number | Yes | Original list price |
| features | string | No | Notable features (pool, renovation, view, etc.) |
| distance_from_subject | string | No | Distance from subject property |

## ⚙️ EXECUTION SOP

### Step 1: Comparable Validation

**What Claude does:** Vet each user-supplied comp against the subject property, ranking by relevance and flagging any comps that exceed acceptable variance on date, distance, size, or age.
**Tools / Resources needed:** MLS export, Redfin, Zillow, Realtor.com — pasted text, CSV, or PDF screenshot of the comp set.
**Data source:** The comp dataset provided by the user during the session.
**Output of this step:** A ranked list of comps with HIGH / MEDIUM / LOW relevance scores and any "aged comp", "extended area", or "size-adjusted" flags surfaced.
**Cowork behavior:** PROCEED WITH ANALYSIS AND DRAFTING.
**If this step fails or required data is missing:** Ask the user for at least 3 comps within 180 days and 1 mile; if fewer are available, surface a "limited comp pool" warning and widen the radius before continuing.

Before running analysis, validate each comparable against the subject:

| Validation Check | Acceptable Range | Action if Outside |
|---|---|---|
| Sale date | Within 6 months | Flag as "aged comp" — still usable but noted |
| Distance | Within 1 mile (urban) / 3 miles (suburban/rural) | Flag as "extended area" comp |
| Size difference | Within 25% of subject sqft | Flag as "size-adjusted" comp |
| Bed/bath count | Within +/- 1 of subject | No flag needed — adjustment handles this |
| Year built | Within 15 years of subject | Flag if 15+ year gap — condition matters more |

Rank comps by relevance: closest in size, age, condition, and proximity gets the highest weight.

### Step 2: Adjustment Calculations

**What Claude does:** Apply the standard adjustment grid to every validated comp, computing a per-feature dollar adjustment and a total adjusted sale price.
**Tools / Resources needed:** Standard Adjustment Table below; user-supplied custom adjustment defaults (if previously specified in the session or Project).
**Data source:** Comp attributes vs. subject attributes from Step 1; market-specific adjustment values from the user's brokerage policy or skill defaults.
**Output of this step:** Per-comp adjustment grid showing each line-item adjustment, total adjustment, and adjusted sale price.
**Cowork behavior:** PROCEED WITH ANALYSIS AND DRAFTING.
**If this step fails or required data is missing:** If a comp's total adjustment exceeds 25% of sale price, disqualify it and note in the report; if condition data is missing, ask the user before assuming "average".

Apply standard adjustments to each comparable to equalize it against the subject property. Adjustments are added to the comp's sale price when the subject has a SUPERIOR feature, and subtracted when the subject has an INFERIOR feature.

**Standard Adjustment Table:**

| Feature | Adjustment Value | Notes |
|---|---|---|
| Bedroom (+/- 1) | +/- $8,000 - $15,000 | Varies by market; use $10,000 default |
| Bathroom (+/- 1) | +/- $5,000 - $12,000 | Use $8,000 default |
| Square footage (per sqft) | +/- price_per_sqft x difference | Use comp's $/sqft for calculation |
| Garage (2-car vs. none) | +/- $15,000 - $25,000 | Use $20,000 default |
| Garage (2-car vs. 1-car) | +/- $8,000 - $12,000 | Use $10,000 default |
| Pool (has vs. doesn't) | +/- $15,000 - $35,000 | Market-dependent; use $20,000 default |
| Condition (per level difference) | +/- $10,000 - $30,000 | Excellent > Good > Average > Fair > Poor |
| Age (per 10-year difference) | +/- $5,000 - $15,000 | Newer generally commands premium |
| Lot size (per 0.1 acre) | +/- $3,000 - $10,000 | Varies by market density |
| Renovated kitchen | +/- $15,000 - $30,000 | Major value driver if recent (< 5 years) |
| Renovated bathrooms | +/- $8,000 - $15,000 | Moderate value driver |
| Location premium/discount | +/- $10,000 - $50,000 | For lot position: cul-de-sac, corner, busy road |

**Adjustment Formula per Comp:**
```
Adjusted Sale Price = comp_sale_price
  + (subject has more bedrooms ? +$10,000 x bedroom_diff : -$10,000 x bedroom_diff)
  + (subject has more bathrooms ? +$8,000 x bath_diff : -$8,000 x bath_diff)
  + (sqft_diff x comp_price_per_sqft)
  + (garage adjustment)
  + (pool adjustment)
  + (condition adjustment)
  + (age adjustment)
  + (lot size adjustment)
  + (renovation adjustments)
  + (location adjustment)
```

**Maximum Adjustment Rule:** If total adjustments exceed 15% of a comp's sale price, flag it as "heavily adjusted" and reduce its weight in the final calculation. Adjustments above 25% disqualify the comp — note it but do not include it in the weighted average.

### Step 3: Price Per Square Foot Analysis

**What Claude does:** Calculate raw and adjusted price-per-square-foot for every comp, then compute the median, range, and weighted average using Step 1's relevance scores.
**Tools / Resources needed:** Adjusted sale prices from Step 2; subject sqft.
**Data source:** Output of Step 2 plus subject_sqft from user input.
**Output of this step:** A $/sqft summary table with median, weighted average, and low–high range.
**Cowork behavior:** PROCEED WITH ANALYSIS AND DRAFTING.
**If this step fails or required data is missing:** If subject_sqft is missing, request it before continuing — the entire valuation depends on it.

Calculate raw and adjusted $/sqft for each comp:

```
Raw $/sqft = sale_price / sqft
Adjusted $/sqft = adjusted_sale_price / subject_sqft
```

Build a comparison table and calculate:
- **Median adjusted $/sqft** (more reliable than mean — resistant to outliers)
- **Range:** lowest to highest adjusted $/sqft
- **Weighted average:** weight by relevance score from Step 1

### Step 4: Market Trend Analysis

**What Claude does:** Analyze DOM, list-to-sale ratio, and inventory absorption to characterize the local market regime and translate that into pricing leverage.
**Tools / Resources needed:** DOM and list/sale data from each comp; optional MLS-supplied active listing count and 6-month sold count for absorption math.
**Data source:** Comp dataset; market_area context provided by user.
**Output of this step:** A "Market Conditions" table with average/median DOM, average L/S ratio, months of inventory, and a one-line interpretation of each.
**Cowork behavior:** PROCEED WITH ANALYSIS AND DRAFTING.
**If this step fails or required data is missing:** If active-listing or absorption data is unavailable, deliver DOM and L/S analysis only and explicitly note that absorption rate could not be computed.

Analyze market conditions in the subject's area:

**Days on Market (DOM):**
```
Average DOM = sum of all comp DOMs / number of comps
Median DOM = middle value when sorted

Interpretation:
- DOM < 14: Hot market, price aggressively (may support above-comp pricing)
- DOM 14-30: Active market, price at market value
- DOM 30-60: Moderate market, price competitively
- DOM > 60: Slow market, price below comps to attract attention
```

**List-to-Sale Price Ratio:**
```
L/S Ratio per comp = sale_price / list_price x 100
Average L/S Ratio = average across all comps

Interpretation:
- > 100%: Multiple offer environment, homes selling over asking
- 97-100%: Healthy market, minimal negotiation
- 94-97%: Moderate negotiation expected
- < 94%: Buyers have leverage, expect below-asking offers
```

**Absorption Rate:**
```
Absorption Rate = (sold homes in area last 6 months) / 6
Months of Inventory = active listings / absorption rate

Interpretation:
- < 3 months inventory: Seller's market
- 3-6 months: Balanced market
- > 6 months: Buyer's market
```

### Step 5: Pricing Recommendation

**What Claude does:** Combine the weighted-average $/sqft, market regime, and subject-property positioning to produce three price points (Aggressive / Market / Conservative) with the reasoning, expected DOM, and probability of receiving offers within 30 days.
**Tools / Resources needed:** Outputs from Steps 3 and 4; optional brokerage CMA template if previously supplied.
**Data source:** Steps 1–4 outputs; current market type (user input or inferred).
**Output of this step:** A pricing recommendation table with three strategies, a recommended strategy, a 2–3 sentence justification, and a client-friendly pricing-context paragraph.
**Cowork behavior:** CONFIRM BEFORE PROCEEDING — surface the three prices to the user and confirm the recommended strategy before finalizing the client-facing report.
**If this step fails or required data is missing:** If all comps were disqualified in Step 2, do NOT produce a price; instead deliver a "comp-pool insufficient" memo and recommend a licensed appraisal.

Based on all analysis, produce three pricing strategies:

| Strategy | Formula | Best When |
|---|---|---|
| **Aggressive** | Weighted avg adjusted $/sqft x subject_sqft x 1.03-1.05 | Seller's market, DOM < 14, unique features, high demand area |
| **Market Value** | Weighted avg adjusted $/sqft x subject_sqft | Balanced market, average condition, standard features |
| **Conservative** | Weighted avg adjusted $/sqft x subject_sqft x 0.95-0.97 | Buyer's market, DOM > 45, condition issues, motivated seller |

For each strategy, provide:
- Recommended list price (rounded to nearest $1,000)
- Expected DOM range
- Probability of receiving offers within 30 days
- Expected negotiation range (% below list)

## 📤 OUTPUT FORMAT

```
# Comparative Market Analysis

**Subject Property:** [subject_address]
**Prepared by:** [agent_name] | [brokerage_name]
**Date:** [date]

---

## Subject Property Overview

| Detail | Value |
|---|---|
| Address | [address] |
| Type | [property_type] |
| Bedrooms | [beds] |
| Bathrooms | [baths] |
| Square Footage | [sqft] |
| Lot Size | [lot_size] |
| Year Built | [year_built] |
| Condition | [condition] |
| Key Features | [features] |

---

## Comparable Sales Analysis

### Comp 1: [comp_address]

| Detail | Comp | Subject | Difference | Adjustment |
|---|---|---|---|---|
| Sale Price | $[price] | — | — | — |
| Bedrooms | [beds] | [subject_beds] | [+/-X] | [+/-$X] |
| Bathrooms | [baths] | [subject_baths] | [+/-X] | [+/-$X] |
| Square Footage | [sqft] | [subject_sqft] | [+/-X sqft] | [+/-$X] |
| Condition | [condition] | [subject_condition] | [diff] | [+/-$X] |
| Garage | [garage] | [subject_garage] | [diff] | [+/-$X] |
| Pool | [yes/no] | [yes/no] | [diff] | [+/-$X] |
| Other | [features] | [features] | [diff] | [+/-$X] |
| **Total Adjustment** | | | | **[+/-$X]** |
| **Adjusted Sale Price** | | | | **$[adjusted]** |

- Days on Market: [DOM]
- Sale Date: [date]
- List-to-Sale Ratio: [X%]
- Distance from Subject: [distance]
- Relevance Score: [high/medium/low]

[Repeat for each comp]

---

## Price Per Square Foot Summary

| Comp | Address | Raw $/sqft | Adjusted $/sqft | Weight |
|---|---|---|---|---|
| 1 | [address] | $[raw] | $[adjusted] | [high/med/low] |
| 2 | [address] | $[raw] | $[adjusted] | [weight] |
| ... | ... | ... | ... | ... |

| Metric | Value |
|---|---|
| Median Adjusted $/sqft | $[value] |
| Weighted Average $/sqft | $[value] |
| Range | $[low] - $[high] |

---

## Market Conditions

| Indicator | Value | Interpretation |
|---|---|---|
| Average DOM | [X] days | [hot/active/moderate/slow] |
| Median DOM | [X] days | [context] |
| Avg List-to-Sale Ratio | [X%] | [interpretation] |
| Months of Inventory | [X] months | [seller's/balanced/buyer's market] |
| Market Type | [type] | [implications for pricing] |

---

## Pricing Recommendation

| Strategy | List Price | Expected DOM | Offer Probability (30 days) | Expected Negotiation |
|---|---|---|---|---|
| Aggressive | $[price] | [X-Y] days | [X%] | [X-Y%] below list |
| **Market Value** | **$[price]** | **[X-Y] days** | **[X%]** | **[X-Y%] below list** |
| Conservative | $[price] | [X-Y] days | [X%] | [X-Y%] below list |

**Recommended Strategy:** [strategy name]

[2-3 sentence justification explaining why this strategy is optimal for this property in this market, referencing specific data points]

---

## Pricing Context for Sellers

[1-2 paragraphs in client-friendly language explaining the pricing recommendation, why overpricing is risky, and what the data shows about buyer behavior in this market. Written to be read aloud during a listing appointment.]
```

## Methodology

**COMPASS Framework (Comparable-Optimization-Market-Price-Adjustment-Strategy-Summary)**

The COMPASS framework mirrors the appraisal industry's Sales Comparison Approach but adds market psychology and strategic pricing layers that appraisers omit. While appraisers determine fair market value, agents must determine optimal list price — which incorporates strategic positioning, days-on-market impact, and buyer perception. Research shows that homes priced within 3% of eventual sale price sell in half the time of homes priced 10%+ above market. The COMPASS framework ensures every CMA produces a defensible, data-backed price that aligns seller expectations with market reality.

The adjustment methodology uses standardized values that can be calibrated to any market. Agents should update the adjustment defaults quarterly based on local appraiser feedback and closed transaction data in their area.

## Advanced Configuration

| Parameter | Default | Range | Description |
|---|---|---|---|
| bedroom_adjustment | $10,000 | $5,000-$25,000 | Per-bedroom adjustment value |
| bathroom_adjustment | $8,000 | $3,000-$15,000 | Per-bathroom adjustment value |
| garage_adjustment_full | $20,000 | $10,000-$40,000 | Two-car garage vs. none |
| pool_adjustment | $20,000 | $10,000-$50,000 | Pool present vs. absent |
| condition_step | $15,000 | $8,000-$35,000 | Per condition-level step (e.g., good to average) |
| max_adjustment_pct | 15% | 10-25% | Maximum total adjustment before flagging |
| disqualify_adjustment_pct | 25% | 20-35% | Adjustment level that disqualifies a comp |
| aggressive_premium | 3% | 1-8% | Premium above market value for aggressive strategy |
| conservative_discount | 5% | 2-10% | Discount below market value for conservative strategy |
| comp_max_age_months | 6 | 3-12 | Maximum age of comparable sale before flagging |

## Example

**Input:**
```
subject_address: 1205 Pecan Creek Ln, Round Rock, TX 78681
subject_beds: 4
subject_baths: 2.5
subject_sqft: 2400
subject_lot_size: 0.18 acres
subject_year_built: 2015
subject_condition: good
subject_features: "open floor plan, granite counters, covered patio, 2-car garage"
subject_garage: 2-car-attached
market_area: Round Rock 78681
current_market_type: balanced
agent_name: Maria Santos
brokerage_name: NextHome Premier

comparables:
  - comp_address: 1310 Pecan Creek Ln
    sale_price: 425000
    sale_date: 2026-01-15
    beds: 4
    baths: 2.5
    sqft: 2350
    year_built: 2016
    condition: good
    days_on_market: 18
    list_price: 435000
    features: "similar floor plan, no covered patio, 2-car garage"
    distance_from_subject: 0.1 miles

  - comp_address: 809 Brushy Creek Rd
    sale_price: 445000
    sale_date: 2025-12-02
    beds: 4
    baths: 3
    sqft: 2600
    year_built: 2017
    condition: excellent
    days_on_market: 12
    list_price: 449000
    features: "renovated kitchen, pool, 2-car garage"
    distance_from_subject: 0.4 miles

  - comp_address: 2202 Ridgefield Dr
    sale_price: 398000
    sale_date: 2025-11-20
    beds: 3
    baths: 2
    sqft: 2100
    year_built: 2012
    condition: average
    days_on_market: 34
    list_price: 415000
    features: "original kitchen, small yard, 2-car garage"
    distance_from_subject: 0.6 miles

  - comp_address: 1450 Forest Ridge Blvd
    sale_price: 432000
    sale_date: 2026-01-28
    beds: 4
    baths: 2.5
    sqft: 2500
    year_built: 2018
    condition: good
    days_on_market: 22
    list_price: 439000
    features: "updated bathrooms, covered patio, 2-car garage, cul-de-sac"
    distance_from_subject: 0.3 miles
```

**Output:**
```
# Comparative Market Analysis

**Subject Property:** 1205 Pecan Creek Ln, Round Rock, TX 78681
**Prepared by:** Maria Santos | NextHome Premier
**Date:** 2026-02-12

---

## Subject Property Overview

| Detail | Value |
|---|---|
| Address | 1205 Pecan Creek Ln, Round Rock, TX 78681 |
| Bedrooms | 4 |
| Bathrooms | 2.5 |
| Square Footage | 2,400 |
| Lot Size | 0.18 acres |
| Year Built | 2015 |
| Condition | Good |
| Key Features | Open floor plan, granite counters, covered patio, 2-car garage |

---

## Comparable Sales Analysis

### Comp 1: 1310 Pecan Creek Ln (0.1 miles away)

| Detail | Comp | Subject | Difference | Adjustment |
|---|---|---|---|---|
| Sale Price | $425,000 | — | — | — |
| Bedrooms | 4 | 4 | 0 | $0 |
| Bathrooms | 2.5 | 2.5 | 0 | $0 |
| Square Footage | 2,350 | 2,400 | +50 sqft | +$9,043 |
| Condition | Good | Good | Same | $0 |
| Covered Patio | No | Yes | Subject superior | +$8,000 |
| **Total Adjustment** | | | | **+$17,043** |
| **Adjusted Sale Price** | | | | **$442,043** |

- Days on Market: 18
- Sale Date: 2026-01-15
- List-to-Sale Ratio: 97.7%
- Relevance Score: HIGH (same street, nearly identical specs)

### Comp 2: 809 Brushy Creek Rd (0.4 miles away)

| Detail | Comp | Subject | Difference | Adjustment |
|---|---|---|---|---|
| Sale Price | $445,000 | — | — | — |
| Bedrooms | 4 | 4 | 0 | $0 |
| Bathrooms | 3 | 2.5 | -0.5 | -$4,000 |
| Square Footage | 2,600 | 2,400 | -200 sqft | -$34,231 |
| Condition | Excellent | Good | -1 level | -$15,000 |
| Pool | Yes | No | Subject inferior | -$20,000 |
| Renovated Kitchen | Yes | No | Subject inferior | -$15,000 |
| **Total Adjustment** | | | | **-$88,231** |
| **Adjusted Sale Price** | | | | **$356,769** |

- Days on Market: 12
- Sale Date: 2025-12-02
- List-to-Sale Ratio: 99.1%
- **FLAG: Heavily adjusted (19.8% of sale price). Reduced weighting.**
- Relevance Score: LOW (significant feature differences)

### Comp 3: 2202 Ridgefield Dr (0.6 miles away)

| Detail | Comp | Subject | Difference | Adjustment |
|---|---|---|---|---|
| Sale Price | $398,000 | — | — | — |
| Bedrooms | 3 | 4 | +1 | +$10,000 |
| Bathrooms | 2 | 2.5 | +0.5 | +$4,000 |
| Square Footage | 2,100 | 2,400 | +300 sqft | +$56,857 |
| Condition | Average | Good | +1 level | +$15,000 |
| Year Built | 2012 | 2015 | +3 years | +$4,500 |
| Covered Patio | No | Yes | Subject superior | +$8,000 |
| **Total Adjustment** | | | | **+$98,357** |
| **Adjusted Sale Price** | | | | **$496,357** |

- Days on Market: 34
- Sale Date: 2025-11-20
- List-to-Sale Ratio: 95.9%
- **FLAG: Heavily adjusted (24.7% of sale price). Reduced weighting.**
- Relevance Score: LOW (bedroom, bath, size, condition differences)

### Comp 4: 1450 Forest Ridge Blvd (0.3 miles away)

| Detail | Comp | Subject | Difference | Adjustment |
|---|---|---|---|---|
| Sale Price | $432,000 | — | — | — |
| Bedrooms | 4 | 4 | 0 | $0 |
| Bathrooms | 2.5 | 2.5 | 0 | $0 |
| Square Footage | 2,500 | 2,400 | -100 sqft | -$17,280 |
| Condition | Good | Good | Same | $0 |
| Updated Baths | Yes | No | Subject inferior | -$8,000 |
| Cul-de-Sac | Yes | No | Subject inferior | -$5,000 |
| **Total Adjustment** | | | | **-$30,280** |
| **Adjusted Sale Price** | | | | **$401,720** |

- Days on Market: 22
- Sale Date: 2026-01-28
- List-to-Sale Ratio: 98.4%
- Relevance Score: HIGH (similar specs, close proximity, recent sale)

---

## Price Per Square Foot Summary

| Comp | Address | Raw $/sqft | Adjusted $/sqft | Weight |
|---|---|---|---|---|
| 1 | 1310 Pecan Creek Ln | $180.85 | $184.18 | HIGH |
| 2 | 809 Brushy Creek Rd | $171.15 | $148.65 | LOW |
| 3 | 2202 Ridgefield Dr | $189.52 | $206.82 | LOW |
| 4 | 1450 Forest Ridge Blvd | $172.80 | $167.38 | HIGH |

| Metric | Value |
|---|---|
| Median Adjusted $/sqft | $175.78 |
| Weighted Average $/sqft (high-weight comps) | $175.78 |
| Range | $148.65 - $206.82 |

---

## Market Conditions

| Indicator | Value | Interpretation |
|---|---|---|
| Average DOM | 21.5 days | Active market |
| Median DOM | 20 days | Consistent selling pace |
| Avg List-to-Sale Ratio | 97.8% | Moderate negotiation expected (2-3% below asking) |
| Market Type | Balanced | Neither buyers nor sellers have strong advantage |

---

## Pricing Recommendation

| Strategy | List Price | Expected DOM | Offer Probability (30 days) | Expected Negotiation |
|---|---|---|---|---|
| Aggressive | $435,000 | 25-40 days | 55% | 3-5% below list |
| **Market Value** | **$422,000** | **18-28 days** | **75%** | **2-3% below list** |
| Conservative | $409,000 | 10-18 days | 90% | 0-2% below list |

**Recommended Strategy:** Market Value at $422,000

Based on the two most relevant comparables (Comp 1 at $442K adjusted and Comp 4 at $402K adjusted), the market value centers around $422,000. The balanced market conditions and 97.8% list-to-sale ratio support pricing at market rather than reaching. This price positions the home competitively against active listings while leaving room for the 2-3% negotiation buyers in this area expect.

---

## Pricing Context for Sellers

Your home is in a strong position. The recent sales on Pecan Creek Lane and in the surrounding neighborhood show consistent demand for 4-bedroom homes in the $400-440K range, with well-maintained properties selling in about three weeks.

I recommend listing at $422,000. This price is supported by the two closest comparable sales — your next-door neighbor's home sold for $425,000 in January (and yours has the covered patio theirs did not), and the Forest Ridge property sold at $432,000 with some upgrades yours does not have. Pricing at $422,000 puts us in the sweet spot: competitive enough to attract strong buyer interest in the first two weeks, but high enough to capture the full value of your home. Homes that are priced right from day one sell faster and for more money than homes that start high and chase the market down with price reductions.
```

## Edge Cases & Best Practices

- **Fewer Than 3 Comps Available:** In rural markets or unique properties where fewer than 3 true comparables exist, expand the search radius and age window before using non-comparable sales. Clearly note the limited comp pool in the report and widen the pricing range to reflect higher uncertainty. Consider using pending sales as supplementary data points.

- **New Construction vs. Resale Comps:** When comparing a resale subject property against new construction sales, subtract a "newness premium" of 5-10% from new construction comp prices before adjusting. New homes carry builder warranties, latest building codes, and zero deferred maintenance that inflates their sale prices relative to resale.

- **Rapidly Appreciating or Declining Markets:** In markets appreciating at 1%+ per month, apply a time adjustment to older comps: add approximately 1% per month elapsed since the comp's sale date. In declining markets, subtract similarly. Always note the adjustment and cite local trend data as justification.

- **Zestimate Objections:** When a seller's Zestimate shows $30K+ above your CMA, address it directly: Zillow's algorithm does not see interior condition, upgrades, or hyper-local factors. Present your CMA as "eyes-on-the-ground data" versus an algorithm's estimate. Show the Zestimate's own reported error range (median 6.9% nationally, which on a $400K home is +/- $27,600).

- **Multiple Offers in Comp Data:** When a comp sold above asking (L/S ratio > 100%), note that the sale price was inflated by competition, not solely by property value. Do not use above-asking comps to justify above-market pricing unless current market conditions also show multiple-offer activity.

- **Significant Lot Size Differences:** In areas where lot size varies dramatically (0.1 acre vs. 1 acre), lot size adjustments can overwhelm other factors. Consider using $/sqft of living area and $/sqft of lot as separate metrics and present both to the client.

- **Expired Listings as Negative Comps:** Include expired listings (homes that failed to sell) as context showing what the market rejected. Expired listing prices establish the ceiling — the subject should be priced below the lowest expired comparable.

## 🔐 PERMISSIONS & SETUP CHECKLIST

No external permissions required for chat mode. Optional setup:

- [ ] **Comp data source (one-time):** Have your MLS, Redfin, Zillow, or Realtor.com export workflow ready. The skill accepts pasted text, CSV, or PDF screenshots of comp data.
- [ ] **Adjustment defaults (recommended):** On first activation, tell Claude your standard per-feature adjustments (e.g., "$5K per garage bay, $50/sqft for above-grade space difference, $20K for finished basement"); the skill will use these on every subsequent CMA in the same chat or Project.
- [ ] **Brokerage CMA template (optional):** If your brokerage uses a specific listing-presentation template, paste a sample once; Claude will format every output to match.

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

| Edge Case | Required Behavior |
|---|---|
| Required input not provided by user | Ask for the specific missing input before proceeding — do not guess or fabricate |
| Data is ambiguous or has multiple valid interpretations | Present both interpretations, state which Claude used, and why |
| Calculation produces a negative or nonsensical result | Flag it explicitly, show the math, and ask user to verify inputs |
| Legal or compliance risk is detected in the output | Insert a ⚠️ LEGAL FLAG block, describe the risk plainly, recommend consulting a licensed professional |
| Output would require information Claude cannot access (live MLS, locked database) | Deliver the maximum output possible with available data, list exactly what's missing and where to get it |
| Conflicting instructions between user input and skill SOP | Follow the SOP — flag the conflict to the user at the end of the output |
| Session approaching context limit mid-task (Cowork) | Write a `_PROGRESS_CHECKPOINT.md` file noting completed steps, current position, and what remains before the session ends |
| Subject property has unique features with no comparable transactions (e.g., horse property, ocean-view, historic landmark) | Use cost-approach reasoning AS A SUPPLEMENT, surface a ⚠️ "Unique-Feature Adjustment" flag, recommend a licensed appraiser for final valuation |
| Market is rapidly shifting (rate cut/spike, regional disaster, mass layoff event) | Add a "MARKET REGIME CHANGE" section narrating the shift, reduce the comp window from 180 to 90 days, and present an additional "current-conditions" price point in the recommendation |

## 📖 DOMAIN GLOSSARY

- **ARV (After Repair Value):** The projected market value of a property after planned renovations are completed. Used by flippers and BRRRR investors to underwrite acquisition price and rehab budget.
- **CMA (Comparative Market Analysis):** An agent-prepared valuation using recent comparable sales, active listings, and expired listings to recommend a list price or offer price. Not a legal appraisal.
- **BPO (Broker Price Opinion):** A formal price opinion provided by a licensed broker, often ordered by lenders for short sales, REO valuations, or loss mitigation. More structured than a CMA.
- **DOM (Days on Market):** The number of days between a listing's MLS go-live date and the date it goes pending. Median DOM is the most reliable indicator of market temperature.
- **MLS (Multiple Listing Service):** The agent-only database where listings, sale data, and showing history are recorded. Source of truth for comp data.
- **GRM (Gross Rent Multiplier):** Sale price divided by annual gross rent. A quick screening metric for income-producing residential properties.
- **NOI (Net Operating Income):** Annual rental income minus all operating expenses (excluding debt service). The numerator in the CAP rate formula.
- **CAP Rate (Capitalization Rate):** NOI divided by sale price, expressed as a percentage. The standard yield metric for income property valuation.
- **Concession:** A seller-paid contribution to the buyer at closing — typically buyer closing costs, rate buy-downs, or repair credits. Concessions inflate effective sale price and must be netted out of comp data when adjusting.

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

## Integration

This skill connects with the broader real estate agent toolkit:

- **Skill 01 (Lead Qualification Engine):** When a seller lead scores as WARMING UP, run a quick CMA before the listing appointment to arrive prepared — a professional CMA is the #1 conversion tool for listing presentations.
- **Skill 02 (Property Description Generator):** After completing the CMA and agreeing on list price, feed the property details into the Description Generator to create all marketing copy in the same session.
- **Skill 04 (Client Follow-Up Sequencer):** If a seller decides not to list after seeing the CMA, use the Sequencer to create a nurture campaign that sends monthly market updates, gradually building the case for listing when conditions improve.
- **Skill 05 (Objection Handler Coach):** When sellers push back on your pricing recommendation ("I want to list higher"), use the Objection Handler for data-backed responses to common pricing objections.
- **Skill 06 (Contract Review Assistant):** Once offers come in, use the Contract Review Assistant to evaluate each offer against the CMA-established value — helps sellers understand whether an offer is fair relative to market data.
