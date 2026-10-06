> Archived overlapping version. Use the active catalog for maintained skills.

---
name: market-analysis-reporter
description: Creates professional Comparative Market Analysis reports with comps, pricing adjustments, and market trend context for listing presentations.
version: "1.0"
author: Evykynn
---

# Market Analysis Reporter

Generate a professional, client-ready Comparative Market Analysis (CMA) report in minutes. This skill takes a subject property and 3-6 comparable sales, calculates adjusted price-per-square-foot values, analyzes market trends (days on market, absorption rate, list-to-sale ratio), and produces a pricing recommendation with three strategies: aggressive, market value, and conservative. Built for listing agents who need to win listing appointments, and buyer's agents who need to justify offer prices to clients. The output is formatted for direct client presentation — clean, professional, and backed by data.

## When to Use

- Preparing for a listing presentation to win a new seller client
- Advising a seller on pricing strategy before going live on MLS
- Helping a buyer determine a fair offer price on a property they want
- Responding to a seller who says "my Zestimate says it's worth more"
- Justifying a price reduction recommendation to a seller after 30+ days on market
- Comparing the subject property against recent sales when an appraiser challenges your price
- Presenting market data to a FSBO to demonstrate the value of professional representation
- Quarterly market updates for your sphere of influence and farming area

## Input Required

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

## Process

### Step 1: Comparable Validation

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

## Output Format

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

## Integration

This skill connects with the broader real estate agent toolkit:

- **Skill 01 (Lead Qualification Engine):** When a seller lead scores as WARMING UP, run a quick CMA before the listing appointment to arrive prepared — a professional CMA is the #1 conversion tool for listing presentations.
- **Skill 02 (Property Description Generator):** After completing the CMA and agreeing on list price, feed the property details into the Description Generator to create all marketing copy in the same session.
- **Skill 04 (Client Follow-Up Sequencer):** If a seller decides not to list after seeing the CMA, use the Sequencer to create a nurture campaign that sends monthly market updates, gradually building the case for listing when conditions improve.
- **Skill 05 (Objection Handler Coach):** When sellers push back on your pricing recommendation ("I want to list higher"), use the Objection Handler for data-backed responses to common pricing objections.
- **Skill 06 (Contract Review Assistant):** Once offers come in, use the Contract Review Assistant to evaluate each offer against the CMA-established value — helps sellers understand whether an offer is fair relative to market data.
