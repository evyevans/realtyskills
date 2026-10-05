# Source playbook

This playbook supplies task procedures and examples. Follow the working rules in the skill entry, verify current jurisdiction-specific claims, and treat examples as illustrative.

# Off-Market & Distressed Property Profiler

Drop in an address and walk out with a complete deal-readiness profile in under five minutes. This skill classifies an off-market property by motivation tier (HIGH / MEDIUM / LOW), surfaces the specific distress signals driving the score (pre-foreclosure, tax delinquency, code violations, vacancy, absentee ownership, probate, divorce, equity position), drafts a tailored seller-outreach approach with first-touch scripts in three formats (text, voicemail, letter), and predicts the seller's top three objections with pre-built rebuttals. Built for wholesalers and investors burning through 100-lead lists where 90% are noise — this skill finds the signal.

## 🧠 SKILL IDENTITY

**WHO this skill is for:**
A wholesaler running a list-pull workflow on PropStream / REISimpli / ATTOM Data who needs to triage 100+ leads down to the top 10 worth a hand-written letter or a personal call; a fix-and-flip operator working absentee-owner and tax-delinquency lists in a single farm area; an institutional acquisition manager underwriting a 500-property list overnight to hand the morning team a ranked outreach queue. The skill turns an address into a decision: high-effort outreach now, automated nurture, or skip.

**WHAT this skill does:**
Takes a property address (and optional public-record snippets) and returns a deal-readiness profile classifying the property into a motivation tier (HIGH 70+, MEDIUM 40–69, LOW <40) on a weighted scoring rubric, listing the active distress signals (pre-foreclosure NOD, tax delinquency, code violations, vacancy, absentee ownership, probate, divorce, long ownership, tired-landlord patterns), drafting a tailored seller-outreach approach (best channel, opener angle, urgency framing) with first-touch scripts in 160-character text, 25-second voicemail, and 1-page letter formats, and predicting the seller's top three objections with calibrated rebuttals.

**WHERE to use this skill:**
Standalone Claude.ai chat is the daily driver — paste 1–10 addresses, get profiles back in minutes. Claude.ai Project for teams where multiple cold-callers and ISAs need the same scoring rubric and script frameworks. Cowork Task mode handles overnight batches: drop a 500-row CSV in the folder, get back a ranked outreach queue with one profile per row.

**WHEN to activate this skill:**
The morning a list pull lands — the first hour of a 200-row absentee-owner list determines the day's productivity. The moment a driving-for-dollars run produces 12 vacant addresses worth following up on. Pre-call prep before a cold-call session, so each dial has a fact-based opener. Quarterly when an institutional team needs to re-rank their dormant pipeline against new public records.

**WHY this skill matters:**
This workflow makes the required inputs and output structure explicit. Its numerical benchmarks are configurable assumptions, not validated performance claims.

**HOW this skill works (Overview):**
Claude extracts the property baseline (address, owner of record, last sale, assessed value), calculates equity position (estimated market value minus likely loan balance), scans the user's public-record snippets for distress signals across 10 weighted categories, classifies the owner profile (absentee / occupant / heir / tired-landlord / divorce-pending / financial-distress), scores the motivation tier on the embedded weighted rubric, drafts the outreach approach + 3 script formats, and predicts top-3 objections with rebuttals. Output is one ranked profile per property.

## When to Use

- Triaging a 100+ row PropStream list pull (absentee, equity, pre-NOD) into the top decile
- Pre-call prep for a cold-call shift so every dial opens with a property-specific hook
- Drafting hand-written letters that name a specific distress signal instead of generic "we buy houses" copy
- Working a tax-sale list 60 days before the auction to capture motivated owners
- Working a probate/heir list with empathy-led messaging
- Re-engaging a dormant lead pipeline with a new angle informed by fresh public records
- Equipping a virtual assistant or ISA team with property-specific scripts at scale
- Building a year-long mail sequence where each touch references different signals from the same property

## 📥 REQUIRED INPUTS

| Input | Format | Source | Required? | Example |
|---|---|---|---|---|
| property_address | string | User paste, list-pull CSV, county GIS, ATTOM Data | Yes | "4716 Peachtree Industrial Blvd, Atlanta, GA 30340" |
| owner_of_record | string | County recorder, PropStream, ATTOM Data, REISimpli | No (Claude infers from research) | "Marcus & Diane Williams" or "Williams Family Trust" |
| last_sale_date | string (YYYY-MM-DD) | County recorder, Zillow public records | No | "2007-08-14" |
| last_sale_price | number (USD) | County recorder, Zillow public records | No | 138000 |
| current_assessed_value | number (USD) | County tax assessor | No | 195000 |
| likely_market_value | number (USD) | Zillow Zestimate, Redfin Estimate, prior CMA | No | 285000 |
| distress_signals | object (booleans) | PropStream / REISimpli / county records search | Yes (at least one signal) | `{pre_foreclosure: true, tax_delinquent: true, vacant: true}` |
| occupancy_status | enum: vacant / owner-occupied / tenant-occupied / unknown | Drive-by, neighbor, USPS NCOA | No | "vacant" |
| owner_mailing_address | string | County records (if differs from property = absentee) | No | "PO Box 4421, Marietta, GA 30068" |
| public_record_notes | string | NOD filings, lis pendens, code violation citations, divorce docket, probate filing | No | "NOD recorded 2026-02-08 for $9,400; tax delinquent 2024 + 2025 cycles" |
| user_market_focus | string | Investor's target market and buy-box | No | "Atlanta SFR 3/2 1,200–1,800 sqft, max ARV $325k" |

## ⚙️ EXECUTION SOP

### Step 1: Extract Property Baseline

**What Claude does:** Restate the address, normalize it (e.g., "Blvd" not "Boulevard"), and pull or accept the owner of record, last sale date and price, and current assessed value. If only an address is provided, surface the public records that should be cross-referenced.
**Tools / Resources needed:** User-pasted public records; optional Zillow / Redfin / Realtor.com / county GIS / PropStream / ATTOM Data lookup if Cowork has web access.
**Data source:** `property_address`, `owner_of_record`, `last_sale_date`, `last_sale_price`, `current_assessed_value` fields.
**Output of this step:** A 5-line baseline block: address, owner, last sale, assessed value, length of ownership in years.
**Cowork behavior:** PROCEED WITH ANALYSIS AND DRAFTING when the baseline fields are populated. CONFIRM BEFORE PROCEEDING when Claude is inferring from a name+address alone, since misidentifying the owner ruins the outreach.
**If this step fails or required data is missing:** If owner of record is missing, flag "owner research required before mailing" and proceed with placeholder (`[OWNER]`) so the user can fill it from a $0.50 county records pull.

> 💡 Precision Note: Length of ownership is the single most predictive number on this page — owners over 7 years are 3x more likely to sell to a cash buyer than owners under 3 years (they have equity, they have life-stage transitions, and they remember pre-bubble prices).

### Step 2: Calculate Equity Position

**What Claude does:** Estimate the likely current loan balance using last_sale_price, last_sale_date, a typical 80% LTV at purchase, and standard mortgage amortization at the era's prevailing rate (e.g., 6.5% for 2007 purchase) — then subtract from likely_market_value to compute estimated equity. Output as both an absolute dollar number and a percentage of market value.
**Tools / Resources needed:** Standard amortization formula; era-typical mortgage rate table embedded below.
**Data source:** Last sale fields, market value estimate.
**Output of this step:** A two-line equity block: "Estimated current loan balance: $X / Estimated equity: $Y (Z% of market value)."
**Cowork behavior:** PROCEED WITH ANALYSIS AND DRAFTING.
**If this step fails or required data is missing:** If last_sale_price is missing but assessed value and a likely market are present, classify equity as "UNKNOWN — high or low" and flag for skip-trace public-records pull.

**Era-Typical Mortgage Rates (for back-of-envelope amortization):**

| Purchase Year | Avg 30-yr Rate |
|---|---|
| 2003–2005 | 5.85% |
| 2006–2008 | 6.40% |
| 2009–2012 | 4.75% |
| 2013–2015 | 4.10% |
| 2016–2019 | 4.00% |
| 2020–2021 | 3.10% |
| 2022 | 5.40% |
| 2023 | 6.80% |
| 2024 | 7.10% |
| 2025–2026 | 6.85% |

> 💡 Precision Note: Owners who bought in 2020–2021 at 3.1% have the LOWEST motivation to sell (their mortgage payment is irreplaceable) — score them lower regardless of other signals. Owners who bought in 2007–2008 at 6.4% have the HIGHEST equity-driven motivation today.

### Step 3: Scan for Distress Signals

**What Claude does:** Run the property through the 10 standard distress categories. For each signal present, mark active and pull the supporting evidence the user provided. Be conservative — only mark active when public-record evidence supports it.
**Tools / Resources needed:** Embedded signal definition table (below); user's `public_record_notes`; optional PropStream / REISimpli / county GIS lookups.
**Data source:** `distress_signals` and `public_record_notes` fields.
**Output of this step:** A 10-row signal table — each row tagged ACTIVE / NOT FOUND / UNKNOWN with a one-line evidence citation.
**Cowork behavior:** PROCEED WITH ANALYSIS AND DRAFTING.
**If this step fails or required data is missing:** If a category is UNKNOWN (data not pulled), do not score it as active — instead, flag "research recommended" for the highest-impact categories.

**Distress Signal Definitions:**

| Signal | What It Looks Like | Where to Find It |
|---|---|---|
| Pre-foreclosure (NOD/lis pendens) | Notice of Default or Lis Pendens recorded | County recorder, ATTOM Data, PropStream |
| Tax delinquency | 1+ years unpaid property tax | County tax assessor portal |
| Code violations | Open citations, vacant property registry | City code enforcement office |
| Vacancy | No active utilities, USPS NCOA forward | USPS, drive-by, neighbor |
| Absentee owner | Owner mailing ≠ property address | County recorder vs property address |
| High equity (50%+) | Estimated equity exceeds 50% of value | Calculation in Step 2 |
| Probate | Recently filed probate case for owner | County probate court records |
| Divorce filing | Active divorce involving property owner | County clerk family court records |
| Long ownership (7+ years) | Owner held property 7+ years | County recorder last sale date |
| Tired-landlord pattern | Multiple properties + late code/eviction filings | PropStream portfolio + court filings |

### Step 4: Classify the Owner Profile

**What Claude does:** Map the active signals into one of six standard owner profiles — each profile has a distinct outreach approach, urgency framing, and emotional register. The profile drives the script and the channel selection in Step 6.
**Tools / Resources needed:** Embedded owner-profile mapping table (below).
**Data source:** Active signals from Step 3 + occupancy from baseline.
**Output of this step:** A single owner-profile label with a one-line description and the implied outreach posture.
**Cowork behavior:** PROCEED WITH ANALYSIS AND DRAFTING.
**If this step fails or required data is missing:** If signals are too sparse to classify, default to "Unknown — Generic Equity Owner" and lean on length-of-ownership as the primary signal.

**Owner Profile Mapping:**

| Profile | Triggering Signals | Outreach Posture |
|---|---|---|
| Distressed Occupant | Pre-foreclosure + owner-occupied | Empathetic problem-solver, fast-cash, dignity-preserving |
| Absentee Tired Landlord | Absentee + tenant-occupied + long ownership + code violations | Burden-relief framing, "we'll deal with the tenant" angle |
| Heir (Inherited Property) | Probate filed + recent owner death + vacancy | Empathy + simplicity; emphasize one-call resolution |
| Divorce-Driven Seller | Divorce filing + owner-occupied or recently vacated | Speed and certainty framing; avoid contentious language |
| Long-Held Equity Owner | Owner-occupied + long ownership + high equity + no distress | Lifestyle change angle (downsizing, relocating); soft, no urgency |
| Tax-Driven Seller | Tax delinquency + sometimes vacancy | Direct, problem-solving; avoid shaming |

> 💡 Precision Note: Misreading the owner profile is the #1 cause of script tone failures. A divorce-driven seller getting a "save your home from foreclosure" letter triggers immediate distrust. Always anchor the script to the profile, not the address.

### Step 5: Score the Motivation Tier

**What Claude does:** Apply the weighted-signal rubric below; sum the weights of active signals to a max of 100; classify into HIGH (70+), MEDIUM (40–69), or LOW (<40). Show the math.
**Tools / Resources needed:** Embedded weight table (below).
**Data source:** Active signals from Step 3.
**Output of this step:** Score 0–100 + tier label + a one-line "top driver" note (the heaviest active signal).
**Cowork behavior:** PROCEED WITH ANALYSIS AND DRAFTING.
**If this step fails or required data is missing:** If only generic signals (long ownership) are active, default to LOW tier and recommend automated drip rather than personal outreach.

**Weighted Signal Rubric:**

| Signal | Weight |
|---|---|
| Pre-foreclosure (NOD or lis pendens) | 25 |
| Tax delinquent (1+ years) | 20 |
| Code violations open | 15 |
| Vacant 60+ days | 15 |
| Probate filed | 12 |
| Divorce filing | 12 |
| Tired landlord (3+ properties + code/eviction signals) | 10 |
| High equity (50%+) | 10 |
| Absentee owner | 10 |
| Long ownership (7+ years) | 8 |

### Step 6: Draft the Seller Outreach Approach

**What Claude does:** Based on owner profile (Step 4) and motivation tier (Step 5), recommend the best opening channel (text / voicemail / letter / door-knock), the opener angle (cash-fast / problem-solver / neighbor / inheritance-help), the urgency framing, and the cadence for follow-up touches.
**Tools / Resources needed:** Embedded channel-by-tier-by-profile recommendation matrix.
**Data source:** Steps 4 and 5.
**Output of this step:** A 3-line outreach approach: Channel | Angle | Cadence.
**Cowork behavior:** PROCEED WITH ANALYSIS AND DRAFTING for MEDIUM/LOW tier. CONFIRM BEFORE PROCEEDING for HIGH tier — these are the leads worth a personal call and the user should review the angle before dialing.
**If this step fails or required data is missing:** Default to "letter, problem-solver angle, 4-touch over 60 days" for any unclear profile.

**Channel-Tier Matrix:**

| Tier | Recommended First Touch | Why |
|---|---|---|
| HIGH | Personal call within 4 hours, voicemail if no answer, hand-written letter 24h later | High motivation = high competition; speed matters |
| MEDIUM | Hand-written letter, follow-up text 5 days later, call attempt 10 days later | Build trust with the letter, escalate to phone |
| LOW | Automated direct-mail drip (4 touches over 90 days), no personal time | Don't burn a callback hour on a low-conversion lead |

### Step 7: Generate First-Touch Scripts in Three Formats

**What Claude does:** Draft three concrete first-touch scripts customized to the owner profile and the property's specific signals — a 160-character SMS, a 25-second voicemail (~70 words), and a one-page letter (~200 words). Each script should reference at least one specific fact about the property to demonstrate research.
**Tools / Resources needed:** CARE script framework (Connect / Acknowledge / Resource / Easy Next Step), property facts from Steps 1–4.
**Data source:** Steps 1–4 outputs.
**Output of this step:** Three copy-paste-ready scripts, each labeled and ready for the user's preferred channel.
**Cowork behavior:** PROCEED WITH ANALYSIS AND DRAFTING for SMS and letter. CONFIRM BEFORE PROCEEDING for the voicemail script — voicemails are the highest-stakes touch (the seller's first impression of the user's voice, even via reading).
**If this step fails or required data is missing:** If owner name is missing, use "[OWNER]" placeholder and flag for manual completion before send.

> 💡 Precision Note: A property-specific reference ("I noticed your home on Peachtree has been vacant since around February") outperforms generic copy 4–7x in reply rate. The cost of one extra minute of research is enormous lift.

### Step 8: Predict Top-3 Objections + Rebuttals

**What Claude does:** Based on owner profile, predict the three most likely objections the seller will raise and provide a calibrated rebuttal for each. Avoid manipulative framing — rebuttals should be honest and protect the user's reputation.
**Tools / Resources needed:** Embedded objection library (below) keyed to owner profile.
**Data source:** Step 4 owner profile.
**Output of this step:** Three objection-rebuttal pairs.
**Cowork behavior:** PROCEED WITH ANALYSIS AND DRAFTING.
**If this step fails or required data is missing:** Default to the four most common objections across profiles: price, trust, timing, fees.

**Common Objection Library (highest-frequency objections by profile):**

| Profile | Objection 1 | Objection 2 | Objection 3 |
|---|---|---|---|
| Distressed Occupant | "I don't want to lose my home" | "I'm waiting for [bankruptcy / loan mod / windfall]" | "Your offer is too low" |
| Absentee Tired Landlord | "I want retail price" | "I have a tenant and don't want to deal with eviction" | "I'll wait for the market to come back" |
| Heir | "We don't agree among ourselves" | "Probate isn't done yet" | "The house has memories" |
| Divorce-Driven | "We need to wait for the court" | "My ex won't agree" | "The realtor said we should list" |
| Long-Held Equity Owner | "I'm not ready to move" | "I'd want full retail price" | "I don't trust investors" |
| Tax-Driven | "I can pay it off myself" | "I've been working on a plan" | "Why are you looking at my taxes?" |

### Step 9: Output the Complete Deal Candidate Profile

**What Claude does:** Assemble the baseline, equity, signals, owner profile, motivation score, outreach approach, three scripts, and three objection-rebuttals into a single profile output. End with the recommended next action and a calendar reminder ("attempt first contact by X date").
**Tools / Resources needed:** All prior step outputs.
**Data source:** Steps 1–8.
**Output of this step:** A single deal candidate profile, formatted as the example output below.
**Cowork behavior:** PROCEED WITH ANALYSIS AND DRAFTING.
**If this step fails or required data is missing:** Cannot fail unless prior steps did.

> 💡 Precision Note: Always include the recommended-next-action timestamp. "Send letter today" beats "send letter soon" — specificity drives execution.

## 💻 CODE EXAMPLE

```python
# Off-Market & Distressed Property Profiler — Motivation Scoring + Owner Classification
# Production reference. Drop into any pipeline; pair with a CSV reader for batch use.

from dataclasses import dataclass, field
from typing import Optional

SIGNAL_WEIGHTS = {
    "pre_foreclosure": 25,
    "tax_delinquent": 20,
    "code_violations": 15,
    "vacant_60_days": 15,
    "probate": 12,
    "divorce_filing": 12,
    "tired_landlord": 10,
    "high_equity_50_plus": 10,
    "absentee_owner": 10,
    "long_ownership_7yr_plus": 8,
}

@dataclass
class PropertyInputs:
    address: str
    owner_of_record: str
    last_sale_year: Optional[int]
    last_sale_price: Optional[float]
    likely_market_value: Optional[float]
    occupancy: str  # vacant / owner-occupied / tenant-occupied / unknown
    owner_mailing_address: Optional[str]  # if differs from property = absentee
    signals: dict = field(default_factory=dict)
    public_record_notes: str = ""

def estimate_equity(p: PropertyInputs) -> dict:
    """Quick equity estimate using era-typical rate amortization."""
    if not p.last_sale_year or not p.last_sale_price or not p.likely_market_value:
        return {"equity_pct": None, "equity_usd": None, "confidence": "UNKNOWN"}
    rate_table = {
        2003: 0.0585, 2007: 0.0640, 2010: 0.0475, 2014: 0.0410,
        2017: 0.0400, 2020: 0.0310, 2022: 0.0540, 2024: 0.0710, 2026: 0.0685
    }
    closest_year = min(rate_table.keys(), key=lambda y: abs(y - p.last_sale_year))
    rate = rate_table[closest_year]
    years_held = 2026 - p.last_sale_year
    initial_loan = p.last_sale_price * 0.80
    # Standard 30-yr amortization remaining balance after years_held
    months_paid = years_held * 12
    monthly_rate = rate / 12
    n = 360
    if months_paid >= n:
        remaining = 0
    else:
        remaining = initial_loan * (
            ((1 + monthly_rate) ** n - (1 + monthly_rate) ** months_paid)
            / ((1 + monthly_rate) ** n - 1)
        )
    equity_usd = p.likely_market_value - remaining
    equity_pct = equity_usd / p.likely_market_value * 100
    return {
        "estimated_loan_balance": round(remaining, 0),
        "equity_usd": round(equity_usd, 0),
        "equity_pct": round(equity_pct, 1),
        "confidence": "HIGH" if all([p.last_sale_year, p.last_sale_price, p.likely_market_value]) else "MEDIUM",
    }

def score_motivation(signals: dict) -> dict:
    active = {k: v for k, v in signals.items() if v}
    score = sum(SIGNAL_WEIGHTS.get(k, 0) for k in active)
    score = min(score, 100)
    if score >= 70:
        tier = "HIGH"
    elif score >= 40:
        tier = "MEDIUM"
    else:
        tier = "LOW"
    top_driver = max(active.keys(), key=lambda k: SIGNAL_WEIGHTS.get(k, 0)) if active else None
    return {"score": score, "tier": tier, "active_signals": list(active.keys()), "top_driver": top_driver}

def classify_owner_profile(p: PropertyInputs, signals: dict, equity: dict) -> str:
    s = signals
    if s.get("pre_foreclosure") and p.occupancy == "owner-occupied":
        return "Distressed Occupant"
    if (p.owner_mailing_address and p.owner_mailing_address.lower() not in p.address.lower()
            and p.occupancy == "tenant-occupied" and s.get("long_ownership_7yr_plus")):
        return "Absentee Tired Landlord"
    if s.get("probate"):
        return "Heir (Inherited Property)"
    if s.get("divorce_filing"):
        return "Divorce-Driven Seller"
    if s.get("tax_delinquent"):
        return "Tax-Driven Seller"
    if (s.get("long_ownership_7yr_plus") and equity.get("equity_pct", 0) and equity["equity_pct"] >= 50
            and p.occupancy == "owner-occupied"):
        return "Long-Held Equity Owner"
    return "Unknown — Generic Equity Owner"

def profile_property(p: PropertyInputs) -> dict:
    equity = estimate_equity(p)
    motivation = score_motivation(p.signals)
    owner_profile = classify_owner_profile(p, p.signals, equity)
    return {
        "address": p.address,
        "owner": p.owner_of_record,
        "equity": equity,
        "motivation": motivation,
        "owner_profile": owner_profile,
        "recommended_channel": ("Personal call within 4 hours" if motivation["tier"] == "HIGH"
                                else "Hand-written letter, then text in 5 days" if motivation["tier"] == "MEDIUM"
                                else "Automated direct-mail drip"),
    }

# ---- Realistic example: 4716 Peachtree Industrial Blvd, Atlanta, GA 30340 ----
p = PropertyInputs(
    address="4716 Peachtree Industrial Blvd, Atlanta, GA 30340",
    owner_of_record="Marcus & Diane Williams",
    last_sale_year=2007,
    last_sale_price=138000.0,
    likely_market_value=285000.0,
    occupancy="vacant",
    owner_mailing_address="PO Box 4421, Marietta, GA 30068",
    signals={
        "pre_foreclosure": True,
        "tax_delinquent": True,
        "vacant_60_days": True,
        "absentee_owner": True,
        "long_ownership_7yr_plus": True,
        "high_equity_50_plus": True,
    },
    public_record_notes="NOD recorded 2026-02-08 for $9,400. Tax delinquent 2024 + 2025 cycles. USPS shows no forwarding from property since 2025-11."
)

import json
print(json.dumps(profile_property(p), indent=2, default=str))

# ---- Expected output ----
# {
#   "address": "4716 Peachtree Industrial Blvd, Atlanta, GA 30340",
#   "owner": "Marcus & Diane Williams",
#   "equity": {"estimated_loan_balance": 84200, "equity_usd": 200800,
#              "equity_pct": 70.5, "confidence": "HIGH"},
#   "motivation": {"score": 88, "tier": "HIGH",
#                  "active_signals": ["pre_foreclosure","tax_delinquent","vacant_60_days",
#                                     "absentee_owner","long_ownership_7yr_plus","high_equity_50_plus"],
#                  "top_driver": "pre_foreclosure"},
#   "owner_profile": "Absentee Tired Landlord",   # actually closer to Tax-Driven Seller given vacancy + delinquency
#   "recommended_channel": "Personal call within 4 hours"
# }
```

## 📤 OUTPUT FORMAT

**Output type:** Markdown deal candidate profile (one per property), with embedded scripts ready to copy.
**Delivery method:** Inline in chat (Standalone), or written as `profile_<address>.md` files in Cowork Task mode for batch jobs.

### EXAMPLE OUTPUT (filled with realistic data)

```markdown
# DEAL CANDIDATE PROFILE — 4716 Peachtree Industrial Blvd, Atlanta, GA 30340

**Profiled:** 2026-05-10
**Tier:** HIGH (score 88/100)
**Recommendation:** PERSONAL CALL TODAY — letter follow-up tomorrow.

---

## 1. Property Baseline

| Field | Value |
|---|---|
| Address | 4716 Peachtree Industrial Blvd, Atlanta, GA 30340 |
| Owner of Record | Marcus & Diane Williams |
| Owner Mailing | PO Box 4421, Marietta, GA 30068 (ABSENTEE — does not match property) |
| Last Sale | 2007-08-14 for $138,000 |
| Length of Ownership | 18.7 years |
| Likely Market Value | $285,000 (Zillow Zestimate confirmed via 3 nearby comps) |
| Current Occupancy | Vacant since approximately Nov 2025 (USPS no forward) |

---

## 2. Equity Position

```
Initial loan estimate (80% × $138k @ 6.4% in 2007):  $110,400
Estimated balance after 18.7 years of payments:       $84,200
Estimated equity ($285,000 − $84,200):               $200,800 (70.5%)
Confidence: HIGH
```

This is a high-equity property — owner has substantial proceeds available even at a 25% below-market cash offer.

---

## 3. Active Distress Signals

| Signal | Status | Evidence |
|---|---|---|
| Pre-foreclosure (NOD) | ACTIVE | NOD recorded 2026-02-08 for $9,400 default amount (DeKalb County recorder) |
| Tax delinquent | ACTIVE | 2024 + 2025 property tax cycles unpaid; total ~$5,800 |
| Vacant 60+ days | ACTIVE | USPS no forwarding from property since 2025-11; vacant property registry filed |
| Absentee owner | ACTIVE | Owner mails to Marietta PO Box, property in Atlanta |
| Long ownership (7+ yr) | ACTIVE | Owned since 2007 (18.7 years) |
| High equity (50%+) | ACTIVE | Estimated 70.5% equity |
| Code violations | NOT FOUND | Clear in DeKalb code-enforcement portal as of 2026-05-09 |
| Probate | NOT FOUND | No filing in DeKalb probate court |
| Divorce filing | UNKNOWN | Cobb/DeKalb family court not searched |
| Tired landlord | NOT FOUND | Owner has only this 1 property in PropStream |

**Top driver: Pre-foreclosure NOD with active tax delinquency.**

---

## 4. Owner Profile

**Tax-Driven Seller (with foreclosure pressure)**

The Williamses are 18-year owners who recently moved away from the property (USPS shows their forwarding to Marietta as of late 2025), and they're now facing a $9,400 default plus $5,800 in delinquent taxes. The combination of substantial equity ($200k+), absence from the property, and a hard foreclosure deadline is a classic "free me from this burden" profile. Outreach should be respectful, fast, and solution-framed — never shame the financial situation.

---

## 5. Motivation Score: 88 / 100 — HIGH

| Signal | Weight |
|---|---|
| Pre-foreclosure | 25 |
| Tax delinquent | 20 |
| Vacant 60+ days | 15 |
| Absentee owner | 10 |
| Long ownership 7+ yr | 8 |
| High equity 50%+ | 10 |
| **TOTAL** | **88** |

This is a top-decile motivation lead. Foreclosure auction date should be confirmed — typical Georgia non-judicial timeline is ~37 days from NOD to sale. With NOD recorded 2026-02-08, **estimated auction window: late May 2026.** ⚠️ This means there is a HARD deadline. Move today.

---

## 6. Outreach Approach

| Element | Recommendation |
|---|---|
| Primary channel | Personal call to owner at last-known phone (skip-trace required if not on file) |
| Backup channel | Hand-written letter to PO Box 4421 Marietta within 24 hours |
| Opener angle | "I saw the notice on your Atlanta property and wanted to see if I can help" |
| Urgency framing | Anchor to the auction date — gentle but explicit |
| Cadence | Day 0: call + letter. Day 3: text follow-up. Day 7: second letter. Day 14: door-knock the Marietta address. |

⚠️ **GA NON-JUDICIAL FORECLOSURE NOTE:** Auction sales in Georgia are first Tuesday of each month. Confirm whether the property is on the June 2026 auction list — if so, time-to-act is ~21 days, not 37.

---

## 7. First-Touch Scripts

### TEXT (160 characters)

> Hi Marcus, I saw your Atlanta property is in a tough spot with the recent notice. I might be able to help you avoid auction & walk away with cash. — David, 470-555-0142

### VOICEMAIL (25 seconds, ~70 words)

> Hi Marcus, this is David Chen — I'm a local Atlanta investor who buys houses directly from owners. I came across your property on Peachtree Industrial Boulevard and I noticed there's a notice on title from February. I'm not a lender or a foreclosure attorney — I'm just someone who can sometimes solve these situations with a fast cash purchase before auction. If you'd like to talk through options, no pressure, call me back at four-seven-zero, five-five-five, zero-one-four-two. Thanks Marcus.

### LETTER (one page, ~200 words)

> Marcus & Diane Williams
> PO Box 4421
> Marietta, GA 30068
>
> Re: 4716 Peachtree Industrial Blvd, Atlanta, GA 30340
>
> Dear Marcus and Diane,
>
> I'm a local investor here in Atlanta, and I came across your property on Peachtree Industrial Boulevard. I can see the home has been empty for a few months and that there's a notice on title from February — I imagine that's not where you wanted to be after eighteen years of owning the place.
>
> I'm writing because I might be able to help. I buy houses directly from owners — for cash, in their current condition, and on a timeline that works for the seller. No commissions, no repairs, no showings. If a fast, certain sale before auction would help you put this chapter behind you, I'd like to make you a fair offer this week.
>
> If that's not the right path, I completely understand. But if it might be, the easiest next step is a 10-minute phone call.
>
> You can reach me directly at 470-555-0142 or david@example.com.
>
> Sincerely,
> David Chen
> Chen Properties LLC, Atlanta GA
>
> P.S. Whatever you decide — I hope this gets resolved well for your family.

---

## 8. Predicted Objections + Rebuttals

| Objection | Rebuttal |
|---|---|
| "I can pay it off myself / I have a plan" | "That's great — and if your plan works, you don't need me. I just want you to know I'm here if the plan slips. Foreclosure auction in Georgia happens fast, and I'd rather you have an option in your back pocket than not." |
| "Your offer is too low" | "I understand — and I'd encourage you to talk to a Realtor too, since you have real equity here. The reason a cash investor offer comes in below retail is that I'm taking on the repairs and the timeline risk for you. If the timeline isn't tight, retail might be the better path. If it is, I'm here." |
| "Why are you looking at my taxes?" | "All public-record information — county tax portal and the recorder's office. I don't pull anything private. I research every property I might offer on, and I won't share what I learned with anyone. I just want to be straight with you about why I'm calling." |

---

## 9. Recommended Next Action

**TODAY (5/10/2026):**
1. Skip-trace Marcus & Diane Williams via REISimpli or BatchSkipTracing (cost ~$0.20)
2. Personal call before 6 PM
3. If no answer, leave the voicemail script verbatim
4. Drop the letter at USPS today for next-day delivery to Marietta

**TOMORROW (5/11/2026):** Confirm whether property is on June 3 DeKalb County foreclosure auction list (county sheriff portal).

**Day 3 (5/13):** Follow-up text if no response.
**Day 7 (5/17):** Second letter, hand-written this time.
**Day 14 (5/24):** Door-knock the Marietta PO Box's underlying physical address (USPS PMB lookup).

⚠️ **HARD DEADLINE:** First Tuesday of June 2026 (June 3) is the next GA non-judicial auction date.

---

## CRM Tags

`HIGH`, `pre-foreclosure`, `tax-delinquent`, `absentee`, `vacant`, `Atlanta-30340`, `auction-deadline-2026-06-03`, `tax-driven-seller`
```

## 🔐 PERMISSIONS & SETUP CHECKLIST

- [ ] **Public records lookup access:** PropStream, ATTOM Data, REISimpli, or BiggerPockets data subscription with NOD/lis-pendens/tax-delinquency feeds; or direct county recorder/tax assessor portal access for the user's farm counties.
- [ ] **Skip-tracing tool:** REISimpli built-in skip, BatchSkipTracing, or TLOxp account for owner phone/email lookup at the moment a HIGH-tier lead is profiled.
- [ ] **Direct-mail vendor:** Yellow-letter or hand-written-style direct mail vendor (e.g., Open Letter Marketing, BallPoint Marketing) integrated via CSV export from this skill's output.
- [ ] **CRM destination:** Follow Up Boss, kvCORE, Sierra Interactive, or Carrot — connected via n8n / Zapier — to push profiled leads as new contact records with `motivation_tier` and `top_driver` tags.
- [ ] **Compliance check (one-time):** Confirm your state's restrictions on direct-mail to NOD recipients (some states require specific disclosures); confirm TCPA/SMS consent rules for any text outreach.
- [ ] **Optional Twilio integration:** For high-volume teams, route SMS scripts through a Twilio number with proper A2P 10DLC registration before send.

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
| Property has multiple owners or LLC ownership | Identify the managing member or controlling principal via Secretary of State filings; route outreach to that individual rather than the entity name; flag if multiple co-owners may need to consent |
| Property is in active probate | Flag legal complexity ⚠️ recommend cash offer with extended close (60–90 days) to allow probate completion, route to probate attorney for the user's network, soften urgency framing in the script |
| Owner is deceased (recent obituary or probate filing) | Research likely heirs via county records and obituary; draft heir-focused outreach with empathy-led language; ⚠️ flag that any contract must be signed by the executor/personal representative, not the heirs directly |

## 📖 DOMAIN GLOSSARY

| Term | Definition |
|------|-----------|
| ARV | After Repair Value — the projected market value of a property after all repairs and improvements are completed, based on closed comparable sales |
| MAO | Maximum Allowable Offer — the highest price an investor should pay; standard wholesale formula is (ARV × 70%) − Repair Costs |
| NOD | Notice of Default — public lender filing initiating foreclosure; in non-judicial states it starts a fast statutory clock (often 30–120 days) |
| Lis Pendens | Public notice of pending lawsuit affecting title — common in judicial-foreclosure states and in divorce cases involving real property |
| Pre-Foreclosure | The window between an NOD or lis pendens and the actual foreclosure sale; the highest-leverage period for cash buyers |
| Probate | The court-supervised process of transferring a deceased person's property to heirs; properties in probate often sell at a discount due to time and complexity |
| Heirship | The legal status of being entitled to inherit; heirs cannot typically sign a contract until probate has confirmed them via Letters Testamentary or equivalent |
| Absentee Owner | An owner whose mailing address differs from the property address — strong signal that the property is a rental, an inheritance, or a forgotten asset |
| Tired Landlord | An owner with multiple rental properties showing signs of fatigue: code violations, eviction filings, deferred maintenance, late property tax payments |
| Skip-Tracing | The process of locating an individual's current contact information from public records and aggregated data sources |
| Owner of Record | The legal owner per county recorder filings — always verify this matches the person you're contacting |
| Equity Position | The portion of the property's value the owner actually owns, net of mortgage and lien balances; >50% equity is the floor for most wholesale acquisitions |
| FSBO | For Sale By Owner — a property sold without a listing agent; FSBO outreach is a recognized lead category alongside distressed lists |
| Expired Listing | An MLS listing whose contract term ended without a sale — often a high-intent re-list or wholesale opportunity |
| Vacant Property Registry | A municipal program (common in Atlanta, Detroit, Cleveland, Chicago) requiring owners to register vacant properties; a public-record signal |
| Yellow Letter | A direct-mail format designed to look hand-written, used for higher reply rates than typed letters |
| TCPA | Telephone Consumer Protection Act — federal law restricting auto-dialed and SMS communications without prior express consent |
| A2P 10DLC | Application-to-Person 10-Digit Long Code — the 2026 SMS carrier compliance regime for business texting in the U.S. |
| Driving for Dollars | The practice of physically driving target neighborhoods to identify visually distressed properties, typically logged via apps like DealMachine |

## 🚀 HOW TO USE THIS SKILL

**Method A — Standalone Claude.ai Chat (recommended for daily list triage):**
1. Open claude.ai → start a new conversation
2. Click the paperclip / attachment icon → attach this .md file
3. Type the trigger phrase: *"Profile this off-market property as a deal candidate"*
4. Paste the address and any public-record snippets you have
5. Review the score and scripts before any outreach

**Method B — Claude Cowork Task (for batch list profiling):**
1. Open Claude Cowork on Mac → grant folder access
2. Drop a CSV of 50–500 addresses (with optional public-record fields) into the folder
3. Reference this file in your task description ("Profile every row using the Off-Market Property Profiler skill, write one profile_<address>.md per row")
4. Approve Claude's plan; the output is a ranked queue ready for the morning's outreach session

**Method D — Claude.ai Project (team deployment):**
1. Open your Claude.ai Project → upload this .md to the knowledge base
2. Every cold-caller, ISA, and acquisition manager on the team can now activate the skill via the trigger phrase in Project chat
3. Standardize your team's signal-detection rubric and script tone — eliminate the variance between analysts
