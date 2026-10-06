# Source playbook

This playbook supplies task procedures and examples. Follow the working rules in the skill entry, verify current jurisdiction-specific claims, and treat examples as illustrative.

# Neighborhood Investment Climate Report

This skill produces a deep-dive investment climate assessment for a specific neighborhood or sub-market — going beyond market data to evaluate the structural factors that drive long-term appreciation, rental demand, and investor exit liquidity: infrastructure investment, demographic momentum, crime trajectory, school quality, walkability, zoning, and gentrification stage. Designed to answer the question serious investors always ask before committing capital: "Is this neighborhood getting better, staying the same, or declining — and what's the evidence?"

## 🧠 SKILL IDENTITY

**WHO this skill is for:**
A real estate investor, wholesaler, or institutional operator evaluating whether to deploy capital in a specific neighborhood. Also: a property management company assessing tenant quality and rental demand durability in a target sub-market; a real estate attorney conducting due diligence on a client's acquisition target.

**WHAT this skill does:**
Produces a structured Neighborhood Investment Climate Report containing: a 5-dimension investment score (appreciation potential, rental demand durability, liquidity/exit, quality-of-life trajectory, and risk factors), gentrification stage classification (1–5 scale), a structured SWOT analysis for the neighborhood as an investment vehicle, asset-class-specific verdict (SFR buy-and-hold, BRRRR, flip, short-term rental, multifamily), and a GO / PROCEED WITH CAUTION / AVOID recommendation with supporting rationale.

**WHERE to use this skill:**
Attach to a Claude.ai chat session and provide the neighborhood name, city, and any available data (crime reports, school ratings, permit activity, census data, walk scores, transit information, employer presence). Claude synthesizes all inputs into the report. If minimal data is provided, Claude uses training knowledge and explicitly flags data tiers.

**WHEN to activate this skill:**
Activate before making a buy decision in an unfamiliar neighborhood, when evaluating whether a deal is worth pursuing at the asking price given location-specific risk, when a property is priced unusually cheap and you need to understand why, or when advising a client on a neighborhood they're considering.

**WHY this skill matters:**
This workflow makes the required inputs and output structure explicit. Its numerical benchmarks are configurable assumptions, not validated performance claims.

**HOW this skill works (Overview):**
Claude evaluates the neighborhood across 5 investment climate dimensions, scores each on a 1–10 scale, identifies the gentrification stage, and produces a SWOT analysis and asset-class verdict. The report distinguishes between structural factors (school quality, infrastructure, employer base) which are slow to change, and cyclical factors (crime trend, vacancy rate, listing activity) which can shift in 12–24 months. This distinction drives the GO/CAUTION/AVOID verdict.

---

## 📥 REQUIRED INPUTS

| Input | Format | Source | Required? | Example |
|-------|--------|--------|-----------|---------|
| Target neighborhood | Name or address + city | User provides | Yes | Vine City, Atlanta, GA / 1234 MLK Jr Dr SW, Atlanta |
| Investment strategy | What will you do with the property? | User provides | Yes | BRRRR — 3BR SFR, hold 5–7 years |
| Neighborhood data (optional) | Crime stats, school ratings, permit data, census, walk score | User provides | No | "WalkScore: 72. Violent crime: 18/1,000. School rating: 4/10." |
| Deal context (optional) | Purchase price and asset type | User provides | No | $145,000, 3/2 SFR, 1,200 sqft |
| Comparison neighborhoods (optional) | 1–2 adjacent neighborhoods for benchmark | User provides | No | Compare to English Avenue, West End |

---

## ⚙️ EXECUTION SOP

### Step 1: Neighborhood Profile and Context

**What Claude does:**
Build a factual profile of the neighborhood including: geographic boundaries and proximity to major nodes (downtown, employment centers, transit), demographic composition and trend, housing stock age and type, current median home price and rent, ownership vs. renter ratio, and the neighborhood's historical trajectory over the past 10–20 years.

**Profile components:**

*Geographic Context:*
- Distance to CBD and major employment centers
- Proximity to transit (commuter rail, bus, highway)
- Adjacent neighborhoods and their investment grade
- Major boundaries (highways, rivers, industrial zones that act as walls)

*Demographic Snapshot:*
- Median household income
- Population trend (growing, stable, declining)
- Homeownership rate (higher = more stable; lower = speculative or distressed)
- Age distribution (younger demographics = early-stage demand; older = potential exit liquidity concern)

*Housing Stock Profile:*
- Predominant property type and era built
- Average price/sqft and rent/sqft
- Vacancy rate
- Percentage of distressed / boarded properties

*Historical Context:*
- What the neighborhood looked like 20 years ago vs. today
- Any significant disinvestment or reinvestment events (factory closures, hospital openings, rezoning)
- Community organization activity

**Tools / Resources needed:**
User-provided data + Claude training knowledge. Census.gov, Walk Score, NCES for school data if user can provide.

**Data source:**
User input + Claude training knowledge (Tier 3 data explicitly flagged).

**Output of this step:**
Neighborhood profile narrative (400–600 words). Used internally and displayed in brief.

**Cowork behavior:**
PROCEED WITH ANALYSIS AND DRAFTING.

**If this step fails or required data is missing:**
Build profile from available information. Flag: "⚠️ Neighborhood profile built from Claude training data. Verify with local MLS, Census ACS, or PropStream neighborhood reports before investing."

---

### Step 2: 5-Dimension Investment Climate Scoring

**What Claude does:**
Score the neighborhood across 5 investment climate dimensions. Each dimension scored 1–10 with justification and a BULLISH / NEUTRAL / BEARISH signal.

**Dimension 1: Appreciation Potential (0–10)**
Evidence of structural appreciation drivers:
- Recent sale price trajectory (rising, flat, falling)
- Permit activity and development investment (new construction, major rehabs)
- Institutional/developer interest (large projects underway, land assemblages)
- Proximity to improving infrastructure (new transit, stadium, hospital, university expansion)
- Anchor tenant effect (Whole Foods / Starbucks rule: their location research predicts neighborhood trajectory)

Scoring rubric:
- 8–10: Multiple structural appreciation drivers active; high confidence in 5–10 year appreciation
- 5–7: Some drivers present; trajectory positive but uncertain
- 3–4: Flat trajectory; no catalysts visible
- 1–2: Declining indicators; negative trajectory

**Dimension 2: Rental Demand Durability (0–10)**
Evidence that rental income will remain stable or grow:
- Current vacancy rate vs. metro average
- Rent trend (rising, flat, falling)
- Employer base and employment stability
- Renter vs. owner-occupant ratio trend
- Short-term rental viability (if applicable): tourist/business demand, local STR regulations

Scoring rubric:
- 8–10: Strong, diversified employment base; low vacancy; rising rents
- 5–7: Adequate demand; single employer dependency or minor vacancy concern
- 3–4: Weak rental demand; high vacancy or falling rents
- 1–2: Severely distressed rental market; structural vacancy

**Dimension 3: Exit Liquidity (0–10)**
How easy will it be to sell the property in 5–10 years:
- Depth of buyer pool (owner-occupants vs. investors only)
- Financing eligibility (can conventional loans close in this neighborhood, or is it cash-only?)
- Days on market trend for comparable properties
- Distance to quality amenities (schools, grocery, retail) — affects resale to owner-occupants
- FHA/VA eligibility (properties in very distressed areas may not qualify)

Scoring rubric:
- 8–10: Broad buyer pool; properties finance easily; 30-day DOM typical
- 5–7: Moderate buyer pool; some financing friction
- 3–4: Thin buyer pool; mostly cash transactions; long DOM
- 1–2: Distressed-only buyer pool; cash-only; significant exit risk

**Dimension 4: Quality of Life Trajectory (0–10)**
Is the neighborhood becoming more or less livable:
- Crime trend (violent crime rate per 1,000 residents — and direction of trend)
- School quality and trend (state test scores, rating trajectory)
- Retail and amenity quality (neighborhood-serving businesses — barbershops, dollar stores = early stage; coffee shops, gyms = maturing)
- Public infrastructure maintenance (street quality, parks, lighting)
- Community organization activity (active neighborhood association, community gardens, murals — signal investment from within)

Scoring rubric:
- 8–10: Rapidly improving quality of life on multiple dimensions
- 5–7: Stable or slowly improving
- 3–4: Flat or slowly declining on 1–2 dimensions
- 1–2: Declining quality of life across multiple dimensions; safety concern

**Dimension 5: Risk Factors (0–10, where 10 = low risk)**
Structural risks that could impair investment returns:
- Environmental risks (flood zone, brownfield contamination, industrial proximity)
- Zoning risk (industrial rezoning, highway expansion plans that could affect properties)
- Title complexity (high rate of tax liens, clouded titles, delinquent taxes in the neighborhood)
- Political/regulatory risk (rent control, short-term rental bans, eminent domain pipeline)
- Single-industry concentration risk (what happens if the major employer leaves?)

Scoring rubric:
- 8–10: No material risk factors identified
- 5–7: 1–2 manageable risk factors
- 3–4: 2–3 significant risk factors
- 1–2: 3+ high-severity risk factors; AVOID unless deeply discounted

**Composite Investment Climate Score:**

| Score Range | Investment Climate Grade | Interpretation |
|-------------|------------------------|----------------|
| 42–50 | A — Prime | Best-in-class neighborhood investment; deploy aggressively |
| 33–41 | B — Strong | Solid investment climate; normal underwriting criteria apply |
| 24–32 | C — Acceptable | Investable with careful underwriting; price for risk |
| 15–23 | D — Speculative | High-risk/high-reward; requires deep discount and long hold horizon |
| Below 15 | F — Avoid | Structural decline; avoid unless specific catalyst identified |

**Tools / Resources needed:**
None — scoring is analytical based on available data.

**Data source:**
Step 1 neighborhood profile + user-provided data.

**Output of this step:**
Scored dimension table with justification per dimension + composite grade.

**Cowork behavior:**
PROCEED WITH ANALYSIS AND DRAFTING.

---

### Step 3: Gentrification Stage Classification

**What Claude does:**
Classify the neighborhood's current gentrification stage on a 1–5 scale. This is one of the highest-value outputs for investors — early-stage gentrification neighborhoods offer the highest upside; late-stage offers the most stability but least upside; post-peak can signal risk.

**Gentrification Stage Scale:**

| Stage | Name | Description | Investor Signal |
|-------|------|-------------|----------------|
| Stage 1 | Pre-Gentrification | Low prices, high vacancy, minimal reinvestment. Artists and pioneers beginning to arrive. | HIGHEST UPSIDE — requires patience and stomach for risk. 10+ year hold horizon. |
| Stage 2 | Early-Stage | First renovated homes visible. Coffee shop or community garden appeared. Prices still low but noticeably rising from trough. | BEST ENTRY POINT — upside still substantial; risk remains but calculus improving. 5–10 year hold. |
| Stage 3 | Active Gentrification | Visible renovation activity throughout. New businesses opening. Longtime residents expressing displacement concern. Prices rising 10–20%+ YoY. | STRONG BUY — ride the wave. Exit before Stage 5. 3–7 year hold. |
| Stage 4 | Late-Stage | Mainstream buyers and retailers entering. Prices approaching adjacent established neighborhoods. Institutional developers present. | MODERATE UPSIDE — still buyable; returns normalizing. Lower risk. |
| Stage 5 | Post-Gentrification / Established | Full price convergence with surrounding area. Normal appreciation rates. | LOW UPSIDE — buy for income stability, not appreciation play. |
| Stage 0 | Decline | Opposite direction. Prices falling, vacancy rising, businesses closing. | AVOID — or only at catastrophic discount with specific turnaround catalyst. |

**Tools / Resources needed:**
None.

**Data source:**
Step 1 neighborhood profile + Step 2 dimension scores.

**Output of this step:**
Gentrification stage classification with key evidence cited (e.g., "Stage 2 — Early-Stage. Evidence: First third-wave coffee shop opened Q3 2025. 14 permitted gut-rehabs in the last 12 months. Crime down 22% from 2023 peak. Prices up 18% from 2023 trough.").

**Cowork behavior:**
PROCEED WITH ANALYSIS AND DRAFTING.

---

### Step 4: SWOT Analysis and Asset-Class Verdict

**What Claude does:**
Produce a structured SWOT analysis and an asset-class-specific investment verdict.

**SWOT Analysis (4 quadrants, 3–5 bullet points each):**

*Strengths (internal, current positives):*
What makes this neighborhood an attractive investment today? Infrastructure, proximity, price point, yield potential.

*Weaknesses (internal, current negatives):*
What structural limitations constrain returns? Crime, school quality, thin buyer pool, title complexity, deferred infrastructure.

*Opportunities (external, future positives):*
What catalysts could accelerate appreciation? Planned transit, zoning changes, anchor development projects, employer announcements.

*Threats (external, future negatives):*
What external forces could impair the investment? Rent control legislation, eminent domain, climate risk (flood, heat), demographic out-migration, industry contraction.

**Asset-Class Verdict:**

For each relevant asset class, provide a GO / PROCEED WITH CAUTION / AVOID verdict with a one-sentence rationale and, where applicable, a recommended buy price/cap rate target:

| Asset Class | Verdict | Rationale | Target Metric |
|-------------|---------|-----------|---------------|
| SFR Buy-and-Hold | GO / CAUTION / AVOID | [1-sentence rationale] | Target cap rate: X% |
| BRRRR | GO / CAUTION / AVOID | [1-sentence rationale] | Max acquisition: $X/sqft |
| Fix-and-Flip | GO / CAUTION / AVOID | [1-sentence rationale] | Min margin: X% of ARV |
| Short-Term Rental | GO / CAUTION / AVOID | [1-sentence rationale] | Occupancy assumption: X% |
| Small Multifamily (2–4 unit) | GO / CAUTION / AVOID | [1-sentence rationale] | Min GRM: X |
| Wholesale/Assignment | GO / CAUTION / AVOID | [1-sentence rationale] | — |

**Tools / Resources needed:**
None.

**Data source:**
Steps 1–3 outputs.

**Output of this step:**
SWOT analysis + asset-class verdict table.

**Cowork behavior:**
PROCEED WITH ANALYSIS AND DRAFTING.

---

### Step 5: Final Report Assembly and Recommendation

**What Claude does:**
Assemble all outputs into the final formatted report. Add the overall GO / PROCEED WITH CAUTION / AVOID recommendation with a 3–5 sentence investment thesis. If a deal was provided in the inputs, add a deal-specific assessment: does the neighborhood climate support the asking price?

**Overall Recommendation logic:**
- Investment Climate Grade A or B + Stage 2–4 → GO
- Investment Climate Grade C + Stage 2–4 → PROCEED WITH CAUTION — deeper discount required
- Investment Climate Grade C or D + Stage 0–1 → AVOID unless specific catalyst identified
- Any Grade + Stage 0 (Decline) → AVOID

**Tools / Resources needed:**
None.

**Data source:**
All prior steps.

**Output of this step:**
Complete formatted report with recommendation.

**Cowork behavior:**
PROCEED WITH ANALYSIS AND DRAFTING.

---

## 📤 OUTPUT FORMAT

**Output type:** Neighborhood Investment Climate Report  
**Delivery method:** Returned directly in chat

---

```
NEIGHBORHOOD INVESTMENT CLIMATE REPORT — Evykynn
Neighborhood:    Vine City, Atlanta, GA
Strategy:        BRRRR — 3BR SFR, 5–7 year hold
Deal Context:    $145,000 acquisition / 3/2 / 1,200 sqft
Report Date:     May 2026
Data Sources:    User-provided crime stats + school rating (Tier 1)
                 Claude training knowledge for demographic/economic data (Tier 3)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
OVERALL VERDICT:  PROCEED WITH CAUTION
Investment Grade: C (Score: 28/50)
Gentrification:   Stage 2 — Early-Stage (accelerating)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

INVESTMENT THESIS:
Vine City presents a compelling early-stage gentrification opportunity
supported by Mercedes-Benz Stadium proximity, a $300M+ Westside
BeltLine investment pipeline, and measurably declining crime (down 22%
since 2023). Structural appreciation drivers are present and
accelerating. The CAUTION designation reflects remaining quality-of-life
gaps (GreatSchools rating: 4/10, violent crime still above city median)
that constrain the buyer pool to investors today, creating exit liquidity
risk unless the 5–7 year hold thesis plays out. At $145,000 / $121/sqft
against an improving market, this deal prices in the risk appropriately.
Proceed with full due diligence on title and environmental.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
5-DIMENSION SCORECARD
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Appreciation Potential     8/10  BULLISH
Rental Demand Durability   6/10  NEUTRAL
Exit Liquidity             5/10  NEUTRAL  ← key constraint
Quality of Life Trajectory 6/10  NEUTRAL (improving)
Risk Factors               3/10  BEARISH  ← title/environmental

COMPOSITE: 28/50  |  Grade: C — Acceptable
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
GENTRIFICATION STAGE: 2 — EARLY-STAGE
Evidence:
  ✓ First specialty coffee shop opened Q3 2025 (Simpson St)
  ✓ 14 permitted gut-rehabs in trailing 12 months (+67% YoY)
  ✓ Violent crime down 22% from 2023 peak
  ✓ Median sale price up 18% from 2023 trough
  ✗ School ratings unchanged — institutional investment lagging residential
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SWOT  [Abbreviated in sample — full version in output]
S: Stadium proximity, BeltLine pipeline, improving crime, low basis
W: School quality, thin retail, cash-only buyer pool constrains exit
O: BeltLine Phase 2, rezoning for mixed-use, investor momentum
T: Gentrification displacement backlash → rent control risk, title complexity
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ASSET-CLASS VERDICT
BRRRR:          GO      — Strong ARV trajectory; target $121/sqft → $185/sqft
SFR Buy-Hold:   GO      — Rent $1,350–$1,500/mo achievable; cap rate ~7%
Fix & Flip:     CAUTION — Buyer pool thin; 60–90 DOM expected at retail price
STR:            AVOID   — City of Atlanta STR restrictions; stadium proximity
                          helps occupancy but owner-occupant issues common
2–4 Unit:       CAUTION — Strong rent demand but financing more challenging
Wholesale:      GO      — Strong investor demand for assignments in this area
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚠️ DUE DILIGENCE FLAGS:
  1. Title: Run full title search — Vine City has elevated tax lien rate
  2. Environmental: Built pre-1978; assume lead paint. Inspect for asbestos.
  3. Flood: Check FEMA FIRM map — portions of neighborhood in 100-year zone
```

---

## 🔐 PERMISSIONS & SETUP CHECKLIST

No external permissions required.

- [ ] **Data tier awareness:** Tier 3 (Claude training estimate) data must be replaced with live sources before committing capital. Use Census.gov, local crime dashboards, GreatSchools.org, and your MLS for ground-truth data.
- [ ] **Fair Housing compliance:** This report assesses neighborhood investment characteristics — economic, structural, and environmental. Claude does not consider racial or ethnic composition as an investment factor. Any such analysis would violate Fair Housing Act prohibitions on steering.
- [ ] **Environmental disclaimer:** Claude's environmental risk assessment is based on general knowledge (flood zones, industrial presence, construction era). It does not substitute for a Phase I Environmental Site Assessment for commercial acquisitions.
- [ ] **Legal disclaimer:** This report is analytical in nature and does not constitute licensed real estate, legal, or financial advice. For commercial acquisitions above $500K, supplement with licensed appraisal and attorney review.

---

## ✅ QUALITY SELF-CHECK

Before delivering any output, Claude must internally verify every item below:

- [ ] All 5 investment climate dimensions are scored with specific evidence cited
- [ ] Composite score correctly maps to Investment Climate Grade
- [ ] Gentrification stage is classified with at least 3 specific evidence points
- [ ] SWOT contains minimum 3 bullets per quadrant
- [ ] Asset-class verdict table covers all 6 asset classes
- [ ] Overall GO/CAUTION/AVOID verdict is supported by the dimension scores and gentrification stage
- [ ] If a deal was provided, deal-specific assessment (price per sqft vs. market, cap rate viability) is included
- [ ] All Tier 3 estimates are flagged; due diligence flags are listed
- [ ] Fair Housing compliance noted — no demographic composition as investment factor

---

## ⚠️ EDGE CASES & ESCALATION RULES

| Scenario | Claude's Exact Response |
|----------|------------------------|
| User provides only an address with no neighborhood name | Identify the neighborhood from the address and proceed. Note: "Address resolved to [Neighborhood Name], [City]. Report generated for this sub-market." |
| Neighborhood is in another country | Produce report with explicit caveat: "⚠️ This report applies U.S.-centric analytical frameworks. Property rights, financing norms, and investment dynamics differ outside the U.S. Verify all assumptions with a local real estate professional." |
| User requests a report on a neighborhood with racial/ethnic composition as an investment factor | Decline: "Fair Housing Act prohibitions apply to neighborhood steering based on protected class characteristics. This report evaluates economic, structural, and environmental investment factors only. I cannot include racial or ethnic composition in investment analysis." |
| Neighborhood is showing Stage 0 (Decline) signals | Flag clearly: "⚠️ DECLINE SIGNAL: Multiple indicators suggest this neighborhood is contracting rather than expanding. A GO verdict is not supportable at any reasonable price without a specific, identifiable catalyst (major employer announcement, rezoning, infrastructure project)." |
| User provides conflicting data (e.g., rising crime but rising prices) | Flag divergence: "⚠️ DIVERGENT DATA: Crime is rising while prices are also rising. This pattern can occur in gentrifying neighborhoods where new investment and legacy safety issues coexist temporarily. This is typically Stage 2–3 and resolves over 3–5 years. Holding period and exit strategy must account for the crime trajectory." |
| User asks to compare 3+ neighborhoods | Produce condensed scoring tables for all neighborhoods plus a Capital Deployment Ranking showing which neighborhood to prioritize first. |
| Session approaching context limit | Write `_PROGRESS_CHECKPOINT.md` with completed sections and restart instructions |

---

## 📖 DOMAIN GLOSSARY

| Term | Definition |
|------|-----------|
| Gentrification Stage | A classification (Stage 0–5) of a neighborhood's position in the urban reinvestment cycle, from decline to pre-gentrification to fully established. The stage determines expected appreciation trajectory and hold horizon. |
| Investment Climate Grade | A composite A–F rating based on 5 scored dimensions (appreciation potential, rental demand, exit liquidity, quality of life, risk factors). Grade A = best-in-class; Grade F = avoid. |
| Absorption Rate | The percentage of available listings sold in a given period — used at the neighborhood level to assess demand relative to supply. |
| Cap Rate (Capitalization Rate) | Net Operating Income (NOI) ÷ Property Value. Used to measure a property's yield independent of financing. At the neighborhood level, cap rate benchmarks indicate relative risk-return profile. |
| GRM (Gross Rent Multiplier) | Purchase Price ÷ Annual Gross Rent. A quick screen for rental property pricing. Lower GRM = better value relative to rent income. |
| BRRRR | Buy, Rehab, Rent, Refinance, Repeat — an investment strategy that uses a cash-out refinance after rehab to recycle capital into the next acquisition. Requires a neighborhood with rising valuations and strong rental demand. |
| Phase I Environmental Assessment | A federally recognized due diligence standard (ASTM E1527-21) that investigates a property's history for recognized environmental conditions (RECs) — contamination, underground storage tanks, industrial use. Required for SBA loans and recommended for commercial acquisitions. |
| Anchor Tenant Effect | The documented phenomenon where the entry of a nationally recognized retailer (Whole Foods, Starbucks, REI) into a neighborhood predicts near-term property appreciation, because these companies conduct rigorous demographic and economic site research before entering a market. |
| Thin Buyer Pool | A condition where the pool of potential buyers for a property type in a given neighborhood is restricted — typically to cash investors only — limiting exit liquidity and extending expected days on market at resale. |
| Steering | The illegal practice under the Fair Housing Act of directing buyers or renters toward or away from specific neighborhoods based on race, color, religion, sex, national origin, disability, or familial status. |

---

*Authored by Evykynn | Real Estate Agentic Automation*

*Maintained as part of RealtySkills by Evykynn. Example dates and figures are illustrative.*
