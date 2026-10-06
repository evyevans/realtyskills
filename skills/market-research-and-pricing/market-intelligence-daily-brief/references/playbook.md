# Source playbook

This playbook supplies task procedures and examples. Follow the working rules in the skill entry, verify current jurisdiction-specific claims, and treat examples as illustrative.

# Real Estate Market Intelligence Daily Brief

This skill produces a structured, actionable market intelligence brief for any target real estate market — synthesizing supply/demand indicators, pricing trends, days-on-market, investor activity signals, and economic context into a single executive-ready report. Designed for operators who need to make capital allocation, pricing, or prospecting decisions based on current market data rather than gut feel.

## 🧠 SKILL IDENTITY

**WHO this skill is for:**
A real estate investor, team lead, brokerage owner, or institutional operator who needs a structured market read before deploying capital, adjusting pricing strategy, or directing their team's prospecting focus. Also: a high-volume agent who needs to deliver credible, current market context to buyers and sellers without spending 2 hours pulling reports.

**WHAT this skill does:**
Produces a complete Market Intelligence Brief for a specified market (city, county, zip code, or metro area) containing: a supply/demand snapshot (inventory levels, absorption rate, months of supply), pricing trajectory (median price, price-per-sqft trend, list-to-sale ratio), deal velocity indicators (DOM, new listings, expired/withdrawn rate), investor activity signals (cash buyer %, distressed property rate, auction volume), economic context (employment trend, rate environment, migration), and a forward-looking operator recommendation (BUY/HOLD/WAIT/EXIT posture per asset class).

**WHERE to use this skill:**
Attach to a Claude.ai chat session and paste in any available market data (MLS export, PropStream report, Redfin/Zillow snapshot, CoStar summary). Claude synthesizes the data into the brief. If no data is pasted, Claude generates the brief from its training knowledge for the specified market, clearly flagging which figures are estimated vs. verified.

**WHEN to activate this skill:**
Activate before making a buy decision in a new market, at the start of each month to calibrate pricing and offer strategy, when briefing a seller client on where the market is going, or when a team/brokerage leader needs an executive briefing to present to partners or investors.

**WHY this skill matters:**
This workflow makes the required inputs and output structure explicit. Its numerical benchmarks are configurable assumptions, not validated performance claims.

**HOW this skill works (Overview):**
Claude identifies the market, pulls or accepts data for 6 indicator categories, scores each indicator on a bullish/neutral/bearish scale, synthesizes the composite picture into a market phase classification, and produces the brief with an operator recommendation by asset class. Every figure is sourced (user-provided data or Claude training estimate) and the brief distinguishes between lagging indicators (closed sale data) and leading indicators (pending sales, new listings, search volume).

---

## 📥 REQUIRED INPUTS

| Input | Format | Source | Required? | Example |
|-------|--------|--------|-----------|---------|
| Target market | City, ZIP, county, or metro area | User provides | Yes | Phoenix, AZ Metro / Maricopa County |
| Asset class focus | SFR, multifamily, commercial, land, or all | User provides | Yes | SFR — 3–4BR, $250K–$450K |
| Market data (optional) | Pasted MLS export, PropStream report, or market summary | User provides | No | "New listings: 1,842. Median DOM: 28 days..." |
| Report date or data period | Month/Year | User provides | No | April 2026 |
| Operator context | What decision is being made? | User provides | No | Deciding whether to increase offer aggression in Q2 |

---

## ⚙️ EXECUTION SOP

### Step 1: Data Ingestion and Source Classification

**What Claude does:**
Ingest all market data provided by the user. Classify each data point by: indicator category (supply, demand, pricing, velocity, investor, economic), data type (hard figure vs. estimate), recency (current month, trailing 30/60/90 days, year-over-year), and reliability tier (user-provided MLS/CoStar = Tier 1; PropStream/Redfin = Tier 2; Claude training estimate = Tier 3, flagged).

**Data categories and key metrics to identify:**

*Supply Indicators:*
- Active listing count and YoY change
- New listings added (trailing 30 days)
- Months of supply (active listings ÷ monthly closed sales)
- Expired and withdrawn listings rate

*Demand Indicators:*
- Pending/under-contract count
- Absorption rate (closed sales ÷ active listings)
- Showing activity trend (if available)
- Cash offer prevalence

*Pricing Indicators:*
- Median sale price and YoY change
- Median price per square foot
- List-to-sale price ratio
- Price reduction rate (% of active listings with at least one reduction)

*Velocity Indicators:*
- Median days on market (DOM)
- Days to offer (DOM to accepted offer)
- Expired listing rate (% of listings that don't sell)

*Investor Activity Signals:*
- Cash buyer percentage of closed sales
- Distressed property rate (foreclosure, pre-foreclosure, short sale as % of active listings)
- Fix-and-flip activity (estimated from cash + short hold resales)
- Auction and REO volume

*Economic Context:*
- Local unemployment rate and trend
- Population and migration trend
- Major employer announcements (hiring, layoffs, relocations)
- Current 30-year fixed mortgage rate

**Tools / Resources needed:**
User-provided data. Claude training knowledge for missing metrics.

**Data source:**
User input + Claude training knowledge (Tier 3 estimates flagged explicitly).

**Output of this step:**
Organized data inventory table with source tier for each metric. Used internally.

**Cowork behavior:**
PROCEED WITH ANALYSIS AND DRAFTING. If no data is provided, proceed with Tier 3 estimates and flag every figure with *(est.)*.

**If this step fails or required data is missing:**
Generate the brief using available data. Clearly note at the top: "⚠️ Data Notice: [X] metrics in this brief are Claude estimates based on training data through [date]. Replace with live MLS/PropStream data before making capital decisions."

---

### Step 2: Market Phase Classification

**What Claude does:**
Score each indicator category on a 3-point scale, then classify the market into one of 5 market phases.

**Scoring rubric per category (score each 1–3):**

| Score | Meaning |
|-------|---------|
| 3 | Bullish — strongly favors sellers / strong demand |
| 2 | Neutral — balanced or transitioning |
| 1 | Bearish — favors buyers / soft demand |

**Categories scored:**
- Supply (low inventory = 3, high inventory = 1)
- Demand (high absorption, low DOM = 3)
- Pricing momentum (prices rising = 3, falling = 1)
- Velocity (fast sales = 3, slow/high DOM = 1)
- Investor activity (high cash/flip activity = signals hot market, but also compresses margins)
- Economic backdrop (strong employment, in-migration = 3)

**Composite score → Market Phase:**

| Composite Score | Market Phase | Operator Posture |
|-----------------|-------------|-----------------|
| 15–18 | Peak Seller's Market | CAUTION — margins compressed; execute fast or wait |
| 11–14 | Active Seller's Market | DEPLOY — strong demand, move quickly on quality deals |
| 8–10 | Balanced / Transitioning | SELECTIVE — disciplined criteria, negotiate hard |
| 5–7 | Buyer's Market Emerging | OPPORTUNITY — motivated sellers, increasing negotiating leverage |
| Below 5 | Distressed Market | AGGRESSIVE BUY — deep discounts available, hold for recovery |

**Tools / Resources needed:**
None — scoring is analytical.

**Data source:**
Step 1 data inventory.

**Output of this step:**
Scored indicator table + Market Phase classification + composite score. Used in Step 3.

**Cowork behavior:**
PROCEED WITH ANALYSIS AND DRAFTING.

**If this step fails or required data is missing:**
Score available indicators only. Assign market phase with confidence qualifier: HIGH / MEDIUM / LOW based on data completeness.

---

### Step 3: Write the Market Intelligence Brief

**What Claude does:**
Produce the full formatted brief. Every section has a structured data block followed by a 2–3 sentence plain-language interpretation written for an operator making a capital or pricing decision — not for a consumer audience.

**Brief sections:**

**Header block:**
- Market name and asset class
- Report period
- Data sources used (MLS, PropStream, Claude estimate)
- Market Phase and composite score

**Section 1: Supply Snapshot**
- Active inventory count + YoY change
- Months of supply with benchmark context (6 months = balanced)
- New listings trend (rising, falling, flat)
- Operator interpretation: Is supply growing or shrinking? Is the market getting easier or harder to find deals?

**Section 2: Demand Snapshot**
- Absorption rate
- Pending sales count and trend
- Cash buyer %
- Operator interpretation: Is demand accelerating or decelerating? Where is buyer urgency?

**Section 3: Pricing Trajectory**
- Median sale price + YoY and MoM change
- Price per sqft trend
- List-to-sale ratio
- Price reduction rate
- Operator interpretation: Is pricing pressure building or releasing? Where is the negotiation window?

**Section 4: Deal Velocity**
- Median DOM + YoY change
- Expired listing rate
- Showings-to-offer ratio (if available)
- Operator interpretation: How fast must you move? What is the cost of hesitation?

**Section 5: Investor Activity**
- Cash buyer %
- Distressed property rate
- Fix-and-flip activity signal
- Operator interpretation: Is competition from investors increasing or decreasing? Are distressed opportunities growing?

**Section 6: Economic Context**
- Local unemployment rate
- Migration trend (in-flow or out-flow)
- Rate environment and buyer affordability impact
- Any major economic events affecting this market
- Operator interpretation: What macro forces are shaping demand in the next 6–12 months?

**Section 7: Operator Recommendation**
- Market phase + confidence level
- Recommended posture by role:
  - **Investor/Buyer:** Offer aggression level (X% below ask / full ask / above ask), deal criteria to prioritize
  - **Agent/Seller:** Pricing strategy (price at X% of Zestimate, expect X days, price reduction trigger at day X)
  - **Brokerage/Team Lead:** Prospecting focus (expired listings, FSBO, rental tenants — rank by opportunity)
- Forward outlook (60–90 day projection with key watch indicators)

**Tools / Resources needed:**
None.

**Data source:**
Steps 1 and 2 outputs.

**Output of this step:**
Complete Market Intelligence Brief.

**Cowork behavior:**
PROCEED WITH ANALYSIS AND DRAFTING. Deliver the full brief in the chat.

**If this step fails or required data is missing:**
Complete all sections with available data. Insert *(est.)* flags where data is estimated. Add a "Data Gaps" section at the bottom listing which metrics, if provided by the user, would most improve brief accuracy.

---

### Step 4: Produce Supporting Tables

**What Claude does:**
After the narrative brief, produce 3 supporting tables:

**Table A — Market Scorecard:**

| Indicator Category | Metric | Value | YoY Change | Score (1–3) | Signal |
|-------------------|--------|-------|------------|-------------|--------|
| Supply | Months of Supply | X.X months | +/- X% | X | Bullish/Neutral/Bearish |
| Demand | Absorption Rate | X% | +/- X% | X | |
| Pricing | Median Sale Price | $XXX,XXX | +/- X% | X | |
| Velocity | Median DOM | XX days | +/- X days | X | |
| Investor | Cash Buyer % | XX% | +/- X% | X | |
| Economic | Unemployment | X.X% | +/- X% | X | |
| **COMPOSITE** | | | | **X/18** | **[Market Phase]** |

**Table B — Asset Class Opportunity Matrix:**

| Asset Class | Current Availability | Pricing Pressure | Investor Competition | Operator Verdict |
|-------------|---------------------|-----------------|---------------------|-----------------|
| SFR < $300K | Low/Med/High | Rising/Flat/Falling | High/Med/Low | BUY / HOLD / AVOID |
| SFR $300K–$500K | | | | |
| SFR $500K+ | | | | |
| 2–4 Unit | | | | |
| 5+ Unit Multifamily | | | | |
| Vacant Land | | | | |

**Table C — 90-Day Watch List:**
Key metrics to monitor that will signal a market shift. 5 specific data points to track with threshold triggers:

| Metric to Watch | Current Value | Bull Trigger (if X happens → more aggressive) | Bear Trigger (if X happens → pull back) |
|----------------|---------------|-----------------------------------------------|----------------------------------------|
| Months of Supply | X.X | Falls below X.X | Rises above X.X |
| Median DOM | XX days | Falls below XX days | Rises above XX days |
| New Listings (MoM) | X | Falls X% MoM | Rises X% MoM |
| Mortgage Rate | X.XX% | Falls below X% | Rises above X% |
| Price Reduction Rate | X% | Falls below X% | Rises above X% |

**Tools / Resources needed:**
None.

**Data source:**
Steps 1–3 outputs.

**Output of this step:**
Three formatted tables appended to the brief.

**Cowork behavior:**
PROCEED WITH ANALYSIS AND DRAFTING.

---

## 📤 OUTPUT FORMAT

**Output type:** Market Intelligence Brief  
**Delivery method:** Returned directly in chat

---

```
MARKET INTELLIGENCE BRIEF — Evykynn
Market:      Phoenix, AZ Metro (Maricopa County)
Asset Class: SFR — 3–4BR, $250K–$450K
Period:      April 2026
Data Source: User-provided PropStream export (Tier 1) + Claude estimates for economic data (Tier 3, flagged)
Phase:       Balanced / Transitioning  ·  Composite Score: 9/18  ·  Confidence: MEDIUM

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 1 — SUPPLY SNAPSHOT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Active Listings (SFR, target price band): 4,812  (+31% YoY)
Months of Supply:                          3.8 months
New Listings Added (Last 30 Days):         1,240  (+18% MoM)
Expired/Withdrawn Rate:                    14%

📊 OPERATOR READ: Inventory is up sharply year-over-year but still
below the 6-month balanced threshold. The spike in new listings and
expired rate signals sellers are testing the market aggressively —
expect price reductions to accelerate over the next 45–60 days.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 2 — DEMAND SNAPSHOT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Absorption Rate:              68%
Pending Sales:                3,270  (-8% MoM)
Cash Buyer %:                 22%
Showings-to-Offer Ratio:      N/A (not provided)

📊 OPERATOR READ: Demand is holding but decelerating. The 8%
month-over-month drop in pending sales is the leading indicator
to watch — it precedes median price softening by 60–90 days.
Cash buyers are still active, primarily in the sub-$300K tier.

[Sections 3–6 continue with same format...]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 7 — OPERATOR RECOMMENDATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Market Phase: BALANCED / TRANSITIONING  (Score: 9/18)
Confidence:   MEDIUM (4 of 6 categories have Tier 1 data)

FOR INVESTORS/BUYERS:
  Offer aggression: 3–5% below asking on properties 30+ DOM
  Prioritize: Properties with price reductions already taken
  Avoid: New listings priced at ask from non-distressed sellers
  Condition trigger: Demand inspection + financing contingency

FOR AGENTS/SELLERS:
  Pricing: List at 97–98% of verified CMA value (not Zestimate)
  Timeline expectation: 25–40 days to offer
  Price reduction trigger: No showing activity by day 14

FOR BROKERAGE/TEAM LEADS:
  Primary prospecting focus: Expired listings (14% exp. rate)
  Secondary: FSBOs testing the market — they'll call in 60 days
  De-prioritize: Cold buyer leads — active buyer demand is flat

Forward Outlook (60–90 days): WATCH for further deceleration.
If months of supply crosses 5.0 or pending sales drop another
10% MoM, upgrade operator posture to BUYER'S MARKET EMERGING.

━━━━━━━━━━━━━━━━━ MARKET SCORECARD ━━━━━━━━━━━━━━━━
[Scorecard table follows...]

⚠️ DATA GAPS: Adding showing activity data and local employment
figures would raise brief confidence from MEDIUM to HIGH.
```

---

## 🔐 PERMISSIONS & SETUP CHECKLIST

No external permissions required for brief generation.

- [ ] **Data freshness:** For capital decisions, use data no older than 30 days. Brief clearly timestamps each data point.
- [ ] **Market specificity:** Briefs for ZIP-level or neighborhood-level markets are more actionable than metro-wide briefs. Specify the tightest geography your data supports.
- [ ] **Asset class specificity:** A brief for "all residential" obscures asset-class-level opportunity. Always specify price band and property type.
- [ ] **Disclaimer:** Tier 3 (Claude estimate) data should be replaced with live MLS or PropStream data before committing capital. This brief is an analytical framework, not a licensed appraisal or market report.

---

## ✅ QUALITY SELF-CHECK

Before delivering any output, Claude must internally verify every item below:

- [ ] Market phase classification is supported by the composite score with scoring rationale shown
- [ ] Every data point is labeled by source tier (Tier 1/2/3) — no unattributed figures
- [ ] Operator interpretation paragraphs translate data into decisions, not just descriptions
- [ ] Operator Recommendation section provides distinct guidance for Investor, Agent, and Brokerage roles
- [ ] 90-Day Watch List includes specific numeric trigger thresholds, not vague directional language
- [ ] Asset Class Opportunity Matrix covers all 6 asset classes with a clear verdict
- [ ] Brief is calibrated to the specified asset class — not generic residential commentary
- [ ] Data gaps identified and listed at the bottom

---

## ⚠️ EDGE CASES & ESCALATION RULES

| Scenario | Claude's Exact Response |
|----------|------------------------|
| No market data provided | Proceed with Tier 3 estimates. Flag every figure with *(est.)* Add: "⚠️ DATA NOTICE: This brief uses Claude training estimates. Replace with live MLS or PropStream data before making capital decisions." |
| User specifies a very small market (single ZIP code) | Produce brief with note: "⚠️ ZIP-level analysis has higher variance. 30-day sample sizes may be too small for reliable absorption rate calculation. Supplement with county-level data for validation." |
| Market data is contradictory (e.g., rising prices but rising DOM) | Flag the contradiction explicitly: "⚠️ DIVERGENT SIGNALS: Median price is rising while DOM is also rising — this indicates a bifurcated market. Upper price tier likely softening while lower tier remains competitive. Segment analysis recommended." |
| User asks for comparison across 2+ markets | Produce a condensed 1-page Scorecard for each market plus a side-by-side Capital Deployment Ranking. |
| User requests a brief for a commercial asset class (office, retail) | Produce brief with note: "⚠️ Commercial real estate market dynamics differ significantly from residential. CoStar or LoopNet data is recommended for commercial briefs. Claude training data for commercial sub-markets may be less granular." |
| Data is more than 90 days old | ⚠️ DATA AGE FLAG: "The data provided is X days old. Real estate market conditions can shift materially in 30–60 days. Treat this brief as a directional guide, not a current market read." |
| Session approaching context limit | Write `_PROGRESS_CHECKPOINT.md` with completed sections and restart instructions |

---

## 📖 DOMAIN GLOSSARY

| Term | Definition |
|------|-----------|
| Absorption Rate | The percentage of available listings that sell in a given period. Calculated as: (Closed Sales ÷ Active Listings) × 100. Above 20% monthly = strong demand. |
| Months of Supply | How long it would take to sell all current inventory at the current absorption rate if no new listings entered the market. Under 3 = seller's market; 5–7 = balanced; above 7 = buyer's market. |
| Days on Market (DOM) | The number of days between a listing's active date and its accepted offer date. A leading indicator of pricing pressure. |
| List-to-Sale Ratio | The ratio of final sale price to original list price, expressed as a percentage. Above 100% = above-ask offers common. Below 97% = significant buyer negotiation leverage. |
| Price Reduction Rate | The percentage of active listings that have had at least one list price reduction. Rising price reduction rates precede median price declines by 30–60 days. |
| Expired Listing Rate | The percentage of listings that expire or are withdrawn without a sale. Above 10% signals pricing/presentation problems or soft demand. |
| Cash Buyer Percentage | The share of closed sales funded without a mortgage. High cash buyer % compresses margins for leveraged buyers but signals strong investor demand. |
| Market Phase | A classification of current supply/demand equilibrium: Peak Seller's Market, Active Seller's Market, Balanced/Transitioning, Buyer's Market Emerging, or Distressed Market. |
| Leading vs. Lagging Indicator | Leading indicators (pending sales, new listings, showing activity) predict where the market is going. Lagging indicators (closed sale prices, DOM) describe where the market has been. |
| Operator Posture | A recommended strategic stance based on market conditions: DEPLOY (move aggressively), SELECTIVE (disciplined criteria), WAIT (hold capital), or CONTRARIAN (buy against the trend for long-term returns). |

---

*Authored by Evykynn | Real Estate Agentic Automation*

*Maintained as part of RealtySkills by Evykynn. Example dates and figures are illustrative.*
