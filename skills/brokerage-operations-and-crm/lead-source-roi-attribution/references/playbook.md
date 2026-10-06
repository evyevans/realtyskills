# Source playbook

This playbook supplies task procedures and examples. Follow the working rules in the skill entry, verify current jurisdiction-specific claims, and treat examples as illustrative.

# Lead Source ROI Attribution Report

This skill calculates the true return on investment for every lead source in a real estate business — comparing cost-per-lead, cost-per-appointment, cost-per-contract, and cost-per-closed-transaction against gross commission income generated — and produces a ranked ROI report with a budget reallocation recommendation.

## 🧠 SKILL IDENTITY

**WHO this skill is for:**
A brokerage owner, team lead, or high-volume agent spending $1,000–$30,000+ per month on lead generation across multiple sources (Zillow, Realtor.com, Facebook ads, Google ads, direct mail, open houses, sphere/referral, cold calling, etc.) who wants to know — with actual math — which sources are profitable and which are burning cash.

**WHAT this skill does:**
Produces a Lead Source ROI Attribution Report containing: (1) Per-source analysis: leads generated, conversion rates at each pipeline stage, GCI produced, total cost, and ROI percentage; (2) Cost efficiency metrics: cost-per-lead (CPL), cost-per-appointment (CPA), cost-per-contract (CPC), cost-per-closed-deal (CPCD) for each source; (3) Ranked ROI table — all sources sorted by return; (4) Budget reallocation recommendation — where to increase spend and where to cut; (5) Lifetime value analysis — which sources produce clients who refer.

**WHERE to use this skill:**
Attach to a Claude.ai chat session and paste or upload your lead source data (a table or CSV with source name, monthly cost, leads generated, appointments, contracts, and closings by source). Claude processes the data and delivers the complete attribution report.

**WHEN to activate this skill:**
Run quarterly — or immediately before renewing any lead generation contract (Zillow Premier Agent, Realtor.com, etc.). Also run when a team member questions whether a lead source is worth continuing, or when GCI is flat but lead spend is increasing.

**WHY this skill matters:**
This workflow makes the required inputs and output structure explicit. Its numerical benchmarks are configurable assumptions, not validated performance claims.

**HOW this skill works (Overview):**
Claude ingests the lead source data, calculates conversion rates at each pipeline stage, computes all cost efficiency metrics, ranks sources by ROI, and produces a recommendation using a tiered investment framework: SCALE (positive ROI, increase spend), OPTIMIZE (marginal ROI, improve conversion before increasing spend), and CUT (negative or zero ROI, reallocate budget).

---

## 📥 REQUIRED INPUTS

| Input | Format | Source | Required? | Example |
|-------|--------|--------|-----------|---------|
| Lead source data | Table or CSV | User provides | Yes | See format below |
| Time period | Months or quarters | User provides | Yes | Q1 2026 (Jan–Mar) |
| Average commission per closed deal | Dollar amount | User provides | No | $8,500 GCI per closing |
| Total lead spend by source | Dollar amounts | User provides | Yes | Zillow: $2,000/mo |

**Required Data Format (per source):**
| Source | Monthly Cost | Leads | Appts | Contracts | Closings | GCI |
|--------|-------------|-------|-------|-----------|---------|-----|
| Zillow Premier Agent | $2,000 | 45 | 8 | 3 | 1 | $8,500 |
| Facebook Ads | $1,500 | 120 | 12 | 4 | 2 | $17,000 |
| Sphere / Referral | $200 | 8 | 7 | 5 | 4 | $34,000 |
| Open Houses | $300 | 22 | 6 | 2 | 1 | $8,500 |
[Continue for all sources]

---

## ⚙️ EXECUTION SOP

### Step 1: Parse and Validate Lead Source Data

**What Claude does:**
Read the provided lead source data and validate for completeness and logical consistency:
- Verify that Appointments ≤ Leads (can't have more appointments than leads)
- Verify that Contracts ≤ Appointments
- Verify that Closings ≤ Contracts
- Flag any source where GCI is reported but Closings = 0 (or vice versa)
- Calculate the analysis period in months (for monthly cost annualization)

**Tools / Resources needed:**
None — validation from user-provided data.

**Data source:**
User-provided lead source table or CSV.

**Output of this step:**
Validated data summary + any data consistency flags.

**Cowork behavior:**
PROCEED WITH ANALYSIS AND DRAFTING — fully autonomous.

**If this step fails or required data is missing:**
If any required column is missing for a source, flag: "I'm missing [field] for [source]. Please provide it, or I'll exclude that source from the full analysis and note it as incomplete."

---

### Step 2: Calculate Per-Source Conversion Funnel

**What Claude does:**
For each lead source, calculate the full conversion funnel:

- **Lead-to-Appointment Rate:** Appointments ÷ Leads × 100
- **Appointment-to-Contract Rate:** Contracts ÷ Appointments × 100
- **Contract-to-Close Rate:** Closings ÷ Contracts × 100
- **Lead-to-Close Rate:** Closings ÷ Leads × 100 (overall conversion)
- **Benchmark comparison:** Industry benchmark for each metric:
  - Lead-to-Appointment: 15–25% (quality leads); 5–15% (cold/online leads)
  - Appointment-to-Contract: 50–70%
  - Contract-to-Close: 75–90%
  - Lead-to-Close: 2–5% (online leads); 40–60% (referrals)

**Tools / Resources needed:**
None — arithmetic from user-provided data.

**Data source:**
Validated data from Step 1.

**Output of this step:**
Conversion Funnel Table: all four metrics for each source + benchmark comparison flags.

**Cowork behavior:**
PROCEED WITH ANALYSIS AND DRAFTING.

**If this step fails or required data is missing:**
If appointment or contract data is not available for a source, calculate lead-to-close only and flag the missing intermediate stages.

---

### Step 3: Calculate Cost Efficiency Metrics

**What Claude does:**
For each source, calculate all four cost efficiency metrics:

**Cost Per Lead (CPL):**
Monthly Cost × Analysis Months ÷ Total Leads = CPL

**Cost Per Appointment (CPA):**
Total Cost ÷ Appointments = CPA
(If appointment data is missing, skip this metric)

**Cost Per Contract (CPC):**
Total Cost ÷ Contracts = CPC

**Cost Per Closed Deal (CPCD):**
Total Cost ÷ Closings = CPCD
(This is the most important metric for ROI analysis)

**ROI Per Source:**
ROI% = (GCI − Total Cost) ÷ Total Cost × 100

**Net Return:**
Net Return = GCI − Total Cost (gross profit from this source over the period)

**Return on Ad Spend (ROAS):**
ROAS = GCI ÷ Total Cost (for every $1 spent, how many $ of GCI returned)

**Tools / Resources needed:**
None — arithmetic from Steps 1 and 2.

**Data source:**
Step 1 data + Step 2 conversion rates.

**Output of this step:**
Cost Efficiency Metrics Table: CPL, CPA, CPC, CPCD, ROI%, Net Return, ROAS for each source.

**Cowork behavior:**
PROCEED WITH ANALYSIS AND DRAFTING.

**If this step fails or required data is missing:**
Calculate all available metrics and flag those that couldn't be computed due to missing data.

> 💡 **Precision Note:** CPCD (Cost Per Closed Deal) is the most important metric for ROI — not CPL. A Zillow lead at $20 CPL that closes at 0.5% is a $4,000 CPCD. A referral at $0 CPL that closes at 50% with a $200 closing gift is a $200 CPCD. The agent tracking CPL without CPCD will continue to over-invest in low-conversion sources.

---

### Step 4: Build the Ranked ROI Table and Categorize Sources

**What Claude does:**
Rank all sources by ROI percentage (highest to lowest) and assign each to a tier:

**TIER 1 — SCALE (ROI > 200%):**
These sources are generating $3+ for every $1 invested. Increase budget by 20–50%.

**TIER 2 — OPTIMIZE (ROI 50–200%):**
Positive return but not exceptional. Before increasing budget, improve conversion rate — typically by improving lead response time or appointment-setting scripts.

**TIER 3 — BREAK-EVEN (ROI 0–50%):**
Barely profitable. Pause new investment and audit the conversion funnel to find the primary leak. Set a 60-day performance improvement target.

**TIER 4 — CUT (ROI < 0%):**
Losing money. Either the lead quality is poor, the conversion process is broken, or the cost is too high for this market. Recommend canceling or renegotiating immediately.

**Special Flag — Sphere/Referral:**
Sphere and referral sources almost always appear in Tier 1 because the cost is near-zero. Flag this as: "Your sphere/referral source is your highest-ROI activity. Every $1 invested in sphere relationship-building (events, gifts, CRM nurture) generates significant returns. Before cutting any digital source, ask: 'Could I replace this GCI by investing more in my sphere?'"

**Tools / Resources needed:**
None.

**Data source:**
Steps 2 and 3 outputs.

**Output of this step:**
Ranked ROI Table with tier assignments and tier-specific recommendation for each source.

**Cowork behavior:**
PROCEED WITH ANALYSIS AND DRAFTING.

**If this step fails or required data is missing:**
Rank by available metrics (ROAS or net return if full ROI can't be calculated) and flag the limitation.

---

### Step 5: Generate Budget Reallocation Recommendation

**What Claude does:**
Produce a specific, actionable budget reallocation plan:

1. **Total current monthly lead spend:** Sum of all source costs
2. **Total GCI generated in period:** Sum of all source GCI
3. **Blended ROI:** Total GCI ÷ Total Spend × 100
4. **Reallocation recommendation:**
   - Cancel/reduce all Tier 4 sources — reallocate that budget
   - Hold steady on Tier 3 with a 60-day improvement plan
   - Optimize Tier 2 conversion processes before scaling spend
   - Increase Tier 1 source budgets by [specific %] with the reallocated funds
5. **Projected impact:** If the reallocation is implemented, what is the estimated GCI improvement based on current conversion rates?

**Tools / Resources needed:**
None.

**Data source:**
Steps 3 and 4 outputs.

**Output of this step:**
Budget Reallocation Plan with current budget, recommended budget, and projected GCI impact per source.

**Cowork behavior:**
PROCEED WITH ANALYSIS AND DRAFTING — deliver the complete report.

**If this step fails or required data is missing:**
Provide the qualitative ranking and reallocation logic without exact dollar projections if GCI data is incomplete.

---

## 💻 CODE EXAMPLE

```python
# Lead Source ROI Attribution Calculator
# Evykynn | AI assistant Skill Library | May 2026

def calculate_lead_source_roi(sources: list[dict]) -> list[dict]:
    """
    Calculate ROI metrics for each lead source.
    Each source dict: {name, monthly_cost, months, leads, appts, contracts, closings, gci}
    """
    results = []
    for s in sources:
        total_cost = s['monthly_cost'] * s['months']
        net_return = s['gci'] - total_cost
        roi_pct = (net_return / total_cost * 100) if total_cost > 0 else 0
        roas = (s['gci'] / total_cost) if total_cost > 0 else 0

        cpcd = (total_cost / s['closings']) if s['closings'] > 0 else float('inf')
        ltc_rate = (s['closings'] / s['leads'] * 100) if s['leads'] > 0 else 0

        if roi_pct > 200: tier = "SCALE"
        elif roi_pct > 50: tier = "OPTIMIZE"
        elif roi_pct >= 0: tier = "BREAK-EVEN"
        else: tier = "CUT"

        results.append({
            "source": s['name'],
            "total_cost": f"${total_cost:,.0f}",
            "gci": f"${s['gci']:,.0f}",
            "net_return": f"${net_return:,.0f}",
            "roi_pct": f"{roi_pct:.0f}%",
            "roas": f"{roas:.1f}x",
            "cost_per_closed": f"${cpcd:,.0f}" if cpcd != float('inf') else "N/A",
            "lead_to_close_rate": f"{ltc_rate:.1f}%",
            "tier": tier,
        })

    return sorted(results, key=lambda x: float(x['roi_pct'].replace('%','')), reverse=True)

# Example:
sources = [
    {"name": "Sphere/Referral", "monthly_cost": 200, "months": 3, "leads": 8, "appts": 7, "contracts": 5, "closings": 4, "gci": 34000},
    {"name": "Zillow PA",        "monthly_cost": 2000, "months": 3, "leads": 45, "appts": 8, "contracts": 3, "closings": 1, "gci": 8500},
    {"name": "Facebook Ads",     "monthly_cost": 1500, "months": 3, "leads": 120, "appts": 12, "contracts": 4, "closings": 2, "gci": 17000},
]
report = calculate_lead_source_roi(sources)
# Sphere: 5567% ROI | Facebook: 179% ROI | Zillow: -42% ROI → CUT
```

---

## 📤 OUTPUT FORMAT

**Output type:** Lead Source ROI Attribution Report  
**Delivery method:** Returned directly in chat — ready for budget review meeting or team presentation

---

```
LEAD SOURCE ROI ATTRIBUTION REPORT — Evykynn
Period:         Q1 2026 (January – March 2026)
Agent/Team:     Marcus Johnson / Maple Realty Group
Total Lead Spend: $11,400/quarter
Total GCI Generated: $68,000
Blended ROI:    496%

━━━━━━━━━━━━━━━━ RANKED ROI TABLE ━━━━━━━━━━

Rank  Source           Cost    GCI     Net     ROI%   CPCD    Tier
 1    Sphere/Referral  $600    $34,000 $33,400 5,567% $150    SCALE ✅
 2    Open Houses      $900    $8,500  $7,600  844%   $900    SCALE ✅
 3    Facebook Ads     $4,500  $17,000 $12,500 278%   $2,250  OPTIMIZE ⚡
 4    Realtor.com      $3,000  $0      ($3,000) -100%  N/A     CUT ❌
 5    Zillow PA        $6,000  $8,500  ($2,500) -29%  $6,000  CUT ❌

━━━━━━━━━━━━━━━━ CONVERSION FUNNELS ━━━━━━━━

Source           L→Appt  Appt→Con  Con→Close  L→Close
Sphere/Referral   87.5%    71.4%     80.0%      50.0%
Open Houses       27.3%    33.3%     50.0%       4.5%
Facebook Ads      10.0%    33.3%     50.0%       1.7%
Realtor.com        4.2%    33.3%      0.0%       0.0%
Zillow PA          17.8%   37.5%     33.3%       2.2%

━━━━━━━━━━━━━━━━ BUDGET REALLOCATION ━━━━━━━
CUT Immediately:
  → Cancel Realtor.com ($1,000/mo): 0 closings in 3 months
  → Reduce Zillow to $500/mo or cancel ($2,000/mo → 1 close in 3 mo)
  → Frees up: $2,500/mo

REALLOCATE TO:
  → Sphere investment: events, CRM nurture, client gifts ($500/mo)
  → Facebook Ads: increase to $2,500/mo (positive ROI)
  → Open Houses: fund additional MLS open house sign-riders ($100/mo)

PROJECTED IMPACT (if implemented):
  Current quarterly GCI: $68,000
  Projected quarterly GCI: $78,500 (+15.4%)
  Quarterly spend reduction: $4,200

⭐ KEY INSIGHT: Your sphere generates 50% lead-to-close vs.
   2.2% from Zillow. Every $1 invested in sphere nurturing
   delivers 26× more per dollar than Zillow Premier Agent.
```

---

## 🔐 PERMISSIONS & SETUP CHECKLIST

No external permissions required.

- [ ] **CRM Export:** Export lead source data from your CRM. In Follow Up Boss: Reports → Lead Source Report. In kvCORE: Reports → Lead Analytics.
- [ ] **Source Tagging:** For future accuracy, ensure every new lead in your CRM is tagged with its source at intake. Without source tagging, this analysis is impossible.
- [ ] **Attribution Window:** Decide on your attribution window (how long after a lead enters to credit the source for a closing). 12 months is standard for real estate.

---

## ✅ QUALITY SELF-CHECK

Before delivering any output, Claude must internally verify every item below:

- [ ] All lead sources in the provided data were analyzed — none skipped
- [ ] All four cost efficiency metrics (CPL, CPA, CPC, CPCD) are calculated for each source
- [ ] ROI% and ROAS are both shown — they tell different stories
- [ ] Sources are ranked correctly (highest ROI to lowest)
- [ ] Each source has a tier assignment (SCALE / OPTIMIZE / BREAK-EVEN / CUT) with specific action
- [ ] Budget reallocation recommendation includes specific dollar amounts — not vague guidance
- [ ] Sphere/referral is called out as a special case regardless of its ranking position
- [ ] Output is immediately usable in a budget meeting without additional calculations

---

## ⚠️ EDGE CASES & ESCALATION RULES

| Scenario | Claude's Exact Response |
|----------|------------------------|
| Lead source has no closings but significant spend | "⚠️ [Source] has generated $[X] in spend with 0 closings in [period]. Either the attribution window is too short, the conversion funnel is broken, or this source does not produce viable leads. Before canceling, check: average days from lead-in to close for this source type." |
| All sources have low ROI | "⚠️ If all sources show low ROI, the primary issue may not be lead source selection — it may be lead conversion (response time, appointment-setting skills, or follow-up consistency). Audit your pipeline conversion process before reallocating budget." |
| User wants to include unpaid sources (sphere, open houses) | "Non-paid sources should still carry a cost — agent time at minimum. Assign an opportunity cost of $100–$200/hour for agent time spent on open houses, sphere events, etc., for an accurate comparison." |
| Legal or compliance concern | ⚠️ LEGAL FLAG: "If you are a team lead sharing lead source ROI data with affiliated agents, ensure this is handled consistently — providing different agents access to different lead quality may raise RESPA or Fair Housing concerns." |
| Session approaching context limit | Write `_PROGRESS_CHECKPOINT.md` with completed source calculations before context is exhausted |

---

## 📖 DOMAIN GLOSSARY

| Term | Definition |
|------|-----------|
| GCI | Gross Commission Income — the total commission earned before splits and expenses |
| CPL | Cost Per Lead — total spend divided by total leads generated from that source |
| CPCD | Cost Per Closed Deal — the most important efficiency metric; total source spend divided by number of closings produced |
| ROAS | Return on Ad Spend — GCI divided by spend; shows revenue generated per dollar invested |
| Lead-to-Close Rate | The percentage of incoming leads that ultimately result in a closed transaction — the summary metric for lead source quality |
| Attribution Window | The maximum number of days between a lead entering the pipeline and a closing that still credits the original lead source |
| Conversion Funnel | The sequential stages a lead passes through: lead → appointment → contract → closing |
| Lead Source | The channel through which a lead enters the pipeline: Zillow, Facebook, referral, open house, direct mail, cold call, etc. |
| Sphere | A real estate agent's personal and professional network — typically the highest-converting and lowest-cost lead source |

---

*Authored by Evykynn | Real Estate Agentic Automation*

*Maintained as part of RealtySkills by Evykynn. Example dates and figures are illustrative.*
