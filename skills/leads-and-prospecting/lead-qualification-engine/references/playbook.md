# Source playbook

This playbook supplies task procedures and examples. Follow the working rules in the skill entry, verify current jurisdiction-specific claims, and treat examples as illustrative.

# Lead Qualification Engine

Transform your chaotic lead pipeline into a ranked action list in minutes. This skill scores incoming buyer and seller leads across four dimensions — readiness signals, financial qualification, timeline urgency, and engagement behavior — then assigns each lead to a priority tier (Ready Now, Warming Up, Long-Term Nurture, Not Qualified) with specific follow-up actions and personalized outreach scripts. Built for listing agents, buyer's agents, and team leads who receive leads from open houses, Zillow, Realtor.com, social media, sign calls, referrals, and sphere of influence.

## 🧠 SKILL IDENTITY

**WHO this skill is for:**
A high-volume independent agent, ISA, listing-team lead, or brokerage owner managing 20+ active leads per week from open houses, Zillow, Realtor.com, IDX websites, sphere of influence, and paid ads — who cannot afford to spend the day calling the wrong leads first.

**WHAT this skill does:**
Ingests a batch of buyer/seller leads (from a pasted list, CRM CSV export, or open-house sign-in sheet) and returns a ranked action list with each lead scored 0–100 across four dimensions (source quality, financial readiness, timeline urgency, behavioral engagement), classified into one of four priority tiers (Ready Now, Warming Up, Long-Term Nurture, Not Qualified), and paired with a specific next-action and a personalized opening message.

**WHERE to use this skill:**
Standalone Claude.ai chat is the primary deployment — paste a batch of 5–50 leads, get a ranked report back in 2–5 minutes. For brokerages, deploy via Claude.ai Project so every team member uses the same scoring rubric. Cowork Task mode is appropriate when the input is a 200+ row CRM export and you want Claude to write the scored output to a file for import back into the CRM.

**WHEN to activate this skill:**
First thing every morning before you start dialing; immediately after an open house when 30 sign-ins need triage; the moment a Zillow lead batch lands in your CRM; quarterly when you need to clean dead weight out of your pipeline.

**WHY this skill matters:**
This workflow makes the required inputs and output structure explicit. Its numerical benchmarks are configurable assumptions, not validated performance claims.

**HOW this skill works (Overview):**
Claude reads the lead batch, applies a four-dimension scoring rubric (source 0–20, finance 0–25, timeline 0–25, engagement 0–30), assigns each lead a priority tier and recommended cadence, and then drafts a personalized opening message tuned to the lead's source, motivation, and stage. The result is a ranked report you can act on in the next 60 minutes.

## When to Use

- Processing a batch of new leads from an open house sign-in sheet
- Sorting incoming Zillow, Realtor.com, or IDX website leads each morning
- Prioritizing which leads to call first when you have 20+ in your pipeline
- Evaluating referral leads from past clients or sphere of influence
- Re-scoring leads that have been sitting in your CRM for 30+ days with no activity
- Deciding which social media DMs or comments deserve a personal call versus an automated response
- Training a new ISA (Inside Sales Agent) or showing assistant on lead prioritization
- Quarterly pipeline cleanup to identify dead leads consuming your attention

## 📥 REQUIRED INPUTS

| Parameter | Type | Required | Description |
|---|---|---|---|
| lead_name | string | Yes | Full name of the prospective client |
| lead_type | string | Yes | buyer, seller, buyer-seller (dual), or investor-buyer |
| lead_source | string | Yes | Where the lead originated: open-house, zillow, realtor-com, sign-call, referral, sphere, social-media-dm, website-form, paid-ad, cold-call, fsbo-outreach, expired-outreach |
| contact_info | string | Yes | Phone number and/or email address |
| pre_approved | string | No | yes, no, unknown (default: unknown) |
| stated_budget | number | No | Maximum price point stated by the lead |
| timeline | string | No | When they want to buy/sell: immediately, 1-3-months, 3-6-months, 6-12-months, just-looking, unknown |
| property_to_sell | string | No | Address of property they want to sell (for seller leads) |
| current_agent | string | No | Whether they are working with another agent: yes, no, unknown |
| motivation_notes | string | No | Any known motivation: relocating, divorce, upsizing, downsizing, job-change, retirement, first-time-buyer, investment, estate-sale |
| contact_attempts | number | No | Number of times you have attempted contact (default: 0) |
| contact_responses | number | No | Number of times the lead has responded (default: 0) |
| days_in_pipeline | number | No | Days since the lead first entered your pipeline (default: 0) |
| engagement_notes | string | No | Specific engagement behaviors: visited-open-house, clicked-listing-email, requested-showing, attended-seminar, downloaded-guide, saved-listings |
| referral_source_name | string | No | Name of the person who referred this lead (if referral) |

## ⚙️ EXECUTION SOP

### Step 1: Lead Source Quality Scoring (0-20 points)

**What Claude does:** Read each lead's `lead_source` field and assign a base point value from the source-quality table below, then apply a referral bonus when the referrer is a known past client.
**Tools / Resources needed:** Source-quality scoring table (embedded in this skill), the user's pasted lead batch, optional CRM CSV export.
**Data source:** The `lead_source` and `referral_source_name` fields provided in the user's input.
**Output of this step:** A 0–20 source score attached to each lead, plus a one-line justification ("Referral from past client + bonus" or "Zillow — high volume, low commitment").
**Cowork behavior:** PROCEED WITH ANALYSIS AND DRAFTING — this is deterministic table-lookup with no judgment calls.
**If this step fails or required data is missing:** If `lead_source` is blank or unknown, default to 5 points (cold-call equivalent) and flag the lead with a recommended discovery question for the agent's first call.

Not all lead sources are equal. Use this configurable source-weighting heuristic; these weights are not established conversion statistics.

| Lead Source | Points | Conversion Context |
|---|---|---|
| referral (past client) | 20 | Illustrative high-trust source weight |
| sphere (friend/family/neighbor) | 18 | High trust, strong relationship foundation |
| sign-call | 16 | Active buyer in your farm area, high intent |
| open-house (registered + engaged) | 15 | Physically present, evaluating properties |
| expired-outreach (you contacted expired listing) | 14 | Already tried to sell, may be frustrated with previous agent |
| fsbo-outreach (you contacted FSBO) | 13 | Already want to sell, need agent help |
| website-form (your personal site) | 12 | Sought you out specifically |
| realtor-com | 10 | Active searcher, but low loyalty — shopping agents too |
| zillow | 9 | High volume, low commitment — many are "just browsing" |
| paid-ad (Facebook, Google, Instagram) | 8 | Clicked an ad, interest level varies widely |
| social-media-dm | 7 | Casual inquiry, often early-stage |
| cold-call | 5 | No prior relationship, lowest initial trust |

**Referral Bonus:** If `referral_source_name` is provided AND the referrer is a past client who closed a transaction with you, add +3 bonus points (cap at 20).

### Step 2: Financial Readiness Scoring (0-25 points)

**What Claude does:** Read the lead's pre-approval status, stated budget, and (for sellers) equity signals; map to the buyer or seller financial-readiness table below to assign 0–25 points.
**Tools / Resources needed:** Financial-readiness scoring tables (buyer + seller), local market median price knowledge for sanity check on "stated budget under viable price."
**Data source:** `pre_approved`, `stated_budget`, `property_to_sell`, and any `motivation_notes` referencing equity, lender, or pricing.
**Output of this step:** A 0–25 financial score per lead with a one-sentence rationale (e.g., "Pre-approved with letter — ready to write offers today").
**Cowork behavior:** PROCEED WITH ANALYSIS AND DRAFTING — table-lookup with light inference.
**If this step fails or required data is missing:** If pre-approval and budget are both blank, score 5 points and add a "needs discovery call to qualify financially" action item to the lead's plan.

Evaluate the lead's ability to transact based on financial signals.

**For Buyer Leads:**

| Signal | Points | Reasoning |
|---|---|---|
| Pre-approved with lender letter in hand | 25 | Ready to write offers today |
| Pre-approved (verbal, no letter yet) | 20 | Financially qualified, minor paperwork remaining |
| Spoken with a lender, application in process | 15 | Serious intent, in qualification pipeline |
| Has stated budget but no lender contact | 10 | Intent exists, but unverified purchasing power |
| No budget information, no lender contact | 5 | Unknown financial readiness — needs discovery call |
| Stated budget under minimum viable price for area | 3 | May not be able to buy in your market |

**For Seller Leads:**

| Signal | Points | Reasoning |
|---|---|---|
| Home equity positive, no liens, ready to list | 25 | Clean transaction, can list immediately |
| Home equity positive, minor prep needed | 20 | 2-4 weeks to market-ready |
| Uncertain about pricing, needs CMA | 15 | Interested but needs education and confidence |
| Underwater or near-zero equity | 8 | Complex transaction, possible short sale |
| Unknown financial position | 5 | Needs discovery conversation |

### Step 3: Timeline & Urgency Scoring (0-25 points)

**What Claude does:** Map the lead's stated `timeline` to a base score, then add motivation multipliers (relocation, divorce, lease expiry, etc.) up to a cap of 25.
**Tools / Resources needed:** Timeline base table + motivation multiplier table (both embedded below).
**Data source:** `timeline` and `motivation_notes` fields.
**Output of this step:** A 0–25 timeline score with the base points, multipliers applied, and a short rationale.
**Cowork behavior:** PROCEED WITH ANALYSIS AND DRAFTING.
**If this step fails or required data is missing:** If timeline is blank, default to 3 ("just-looking equivalent") and add a "ask about decision timeline on first call" item to the action plan.

Score based on when the lead intends to act and what is driving the timeline.

| Timeline | Base Points | Adjustment |
|---|---|---|
| immediately (within 30 days) | 25 | No adjustment needed |
| 1-3-months | 20 | Active pipeline, schedule regular touchpoints |
| 3-6-months | 12 | Nurture phase, monthly check-ins |
| 6-12-months | 6 | Long nurture, quarterly value-adds |
| just-looking / unknown | 3 | Lowest urgency, drip campaign only |

**Motivation Multipliers (add to base, cap at 25):**

| Motivation | Bonus | Why It Matters |
|---|---|---|
| Job relocation with start date | +5 | Hard deadline creates urgency |
| Lease expiring within 60 days | +4 | Housing deadline approaching |
| Estate sale / inherited property | +4 | Property is a burden, want resolution |
| First-time buyer exploring | +1 | Excited but often slow to commit |

### Step 4: Engagement & Behavioral Scoring (0-30 points)

**What Claude does:** Read the `engagement_notes`, `contact_attempts`, and `contact_responses` fields and map the strongest signal to the engagement-behavior table; this illustrative rubric assigns engagement a maximum of 30 points.
**Tools / Resources needed:** Engagement-behavior scoring table (embedded below).
**Data source:** `engagement_notes`, `contact_attempts`, `contact_responses`, `days_in_pipeline`.
**Output of this step:** A 0–30 engagement score per lead with the specific behavior cited.
**Cowork behavior:** PROCEED WITH ANALYSIS AND DRAFTING.
**If this step fails or required data is missing:** If the lead is brand-new (zero attempts, zero responses, days_in_pipeline ≤ 1), score 10 (neutral fresh-lead default) rather than the low-engagement penalty.

Score the supplied engagement signals using this illustrative rubric; it is not a validated prediction model.

| Behavior | Points | What It Signals |
|---|---|---|
| Inbound call or text (they reached out to you) | 30 | Highest intent — they chose you |
| Requested a showing or CMA | 28 | Active evaluation, ready to take next step |
| Attended your open house AND asked detailed questions | 25 | Serious buyer/seller, evaluating you as agent |
| Returned your call/text within 24 hours | 22 | High responsiveness, values the relationship |
| Clicked 5+ listings in your email campaigns | 18 | Active search behavior, narrowing preferences |
| Downloaded your buyer/seller guide or lead magnet | 15 | Research phase, building trust |
| Responded to a social media post or DM | 12 | Engaged but casual |
| Attended open house but did not provide full info | 8 | Mild interest, guarded |
| No contact yet (fresh lead, just entered pipeline) | 10 | Neutral — has not had chance to engage |
| 3+ contact attempts with no response | 4 | Low engagement signal |
| Unsubscribed or asked to stop contact | 0 | Respect immediately, mark as Not Qualified |

### Step 5: Total Score & Tier Assignment

Before assigning an outreach action, check contact status. An opt-out or do-not-contact request overrides every score and tier: return DO NOT CONTACT, preserve the preference, and exclude the lead from calls, texts, emails, and drip campaigns.

**What Claude does:** Sum the four dimension scores into a total (max 100) and assign one of four priority tiers with a specific response-time SLA and action protocol.
**Tools / Resources needed:** Tier-assignment table (below); user-configurable thresholds from the Advanced Configuration section if the agent has tuned them.
**Data source:** The four sub-scores from Steps 1–4.
**Output of this step:** Total score 0–100 + tier label (READY NOW / WARMING UP / LONG-TERM NURTURE / NOT QUALIFIED) + response-time SLA + action protocol per lead.
**Cowork behavior:** PROCEED WITH ANALYSIS AND DRAFTING.
**If this step fails or required data is missing:** Cannot fail unless prior steps did — if any prior dimension is missing, flag the lead with an "incomplete data" badge alongside the tentative tier.

**Total Score = Source Score + Financial Score + Timeline Score + Engagement Score (max 100)**

| Tier | Score Range | Label | Response Time | Action Protocol |
|---|---|---|---|---|
| Tier 1 | 75-100 | READY NOW | Within 1 hour | Personal call, schedule appointment, prepare CMA or showing list |
| Tier 2 | 50-74 | WARMING UP | Within 24 hours | Personal call, add to active drip, send market report |
| Tier 3 | 25-49 | LONG-TERM NURTURE | Within 48 hours | Personalized email, add to monthly newsletter, quarterly check-in calls |
| Tier 4 | 0-24 | NOT QUALIFIED | Low priority | Automated drip only, re-score in 90 days, archive if no engagement at 180 days |

### Step 6: Personalized Outreach Script Generation

**What Claude does:** For each lead, draft a customized opening message using the CARE framework (Connect, Acknowledge, Resource, Easy Next Step) tuned to the lead's tier, source, and known motivation.
**Tools / Resources needed:** CARE script framework, tier-tone mapping (below), lead-specific facts from the input.
**Data source:** All previously-collected lead fields plus the assigned tier from Step 5.
**Output of this step:** A copy-paste-ready opening message (call script, text, or email) per lead, tuned to their tier and source.
**Cowork behavior:** PROCEED WITH ANALYSIS AND DRAFTING for Tier 2–4 scripts. CONFIRM BEFORE PROCEEDING for Tier 1 (READY NOW) scripts when the agent wants to personalize the language further before sending.
**If this step fails or required data is missing:** If lead name is missing, generate a generic placeholder script and flag "[INSERT NAME]" — but mark the lead for human completion before send.

For each lead, generate a customized outreach script based on their tier, source, and known details.

**Script Framework (CARE Method):**

```
C - Connect: Reference how you got their info (open house, referral name, their inquiry)
A - Acknowledge: Show you understand their situation (timeline, motivation, needs)
R - Resource: Offer specific value (market report, CMA, showing schedule, buyer guide)
E - Easy Next Step: Propose one low-commitment action (15-min call, coffee meeting, quick text chat)
```

**Script Tone by Tier:**
- READY NOW: Confident, action-oriented, schedule-focused
- WARMING UP: Helpful, consultative, value-offering
- LONG-TERM NURTURE: Casual, relationship-building, no-pressure
- NOT QUALIFIED: Brief, automated, resource-sharing

## 📤 OUTPUT FORMAT

```
# Lead Qualification Report

**Generated:** [date]
**Agent:** [your name]
**Batch Size:** [N] leads
**Source Mix:** [breakdown by source]

---

## Priority Rankings

| Rank | Lead Name | Type | Score | Tier | Top Signal | Recommended Action |
|---|---|---|---|---|---|---|
| 1 | [name] | [buyer/seller] | [score]/100 | [READY NOW] | [primary signal] | [action] |
| 2 | [name] | [type] | [score]/100 | [tier] | [signal] | [action] |
| ... | ... | ... | ... | ... | ... | ... |

---

## Detailed Lead Scorecards

### Lead 1: [name] — [lead_type]

**Score: [total]/100 — [TIER]**

| Dimension | Score | Details |
|---|---|---|
| Lead Source Quality | [X]/20 | [source] — [context] |
| Financial Readiness | [X]/25 | [pre-approval status, budget notes] |
| Timeline & Urgency | [X]/25 | [timeline] + [motivation signals] |
| Engagement & Behavior | [X]/30 | [engagement description] |

**Key Facts:**
- Source: [lead_source]
- Budget: $[stated_budget] | Pre-approved: [yes/no/unknown]
- Timeline: [timeline]
- Motivation: [motivation_notes]
- Days in Pipeline: [days_in_pipeline]
- Contact History: [attempts] attempts, [responses] responses

**Action Plan:**
1. [First action with specific timeline]
2. [Second action]
3. [Third action]

**Personalized Outreach Script:**
> "[CARE-method script customized to this lead's situation, source, and tier]"

**CRM Tags:** [tier], [source], [timeline], [buyer/seller]

---

[Repeat for each lead]

---

## Pipeline Summary

| Tier | Count | % of Batch | Time Allocation |
|---|---|---|---|
| READY NOW | [N] | [X%] | 50% of daily outreach time |
| WARMING UP | [N] | [X%] | 30% of daily outreach time |
| LONG-TERM NURTURE | [N] | [X%] | 15% of daily outreach time |
| NOT QUALIFIED | [N] | [X%] | 5% (automated only) |

**Conversion Forecast:**
- READY NOW leads: [X]% expected to transact within 30 days
- WARMING UP leads: [X]% expected to transact within 90 days
- Pipeline Value: $[estimated commission value based on stated budgets and average price points]

**Priority Actions This Week:**
1. [Most important action]
2. [Second priority]
3. [Third priority]
4. [Data gaps to fill — leads needing pre-approval check, budget discovery, etc.]
```

## Methodology

**CARE Scoring Model (Connection-Ability-Readiness-Engagement)**

The CARE model adapts enterprise sales qualification frameworks (BANT, MEDDIC) to the relationship-driven world of residential real estate. Unlike investor lead scoring which focuses on property distress and equity, agent lead scoring centers on the client's readiness and willingness to enter a transaction. Research from NAR (National Association of Realtors) shows that speed-to-lead is the single strongest predictor of conversion for online leads — agents who respond within 5 minutes are 100x more likely to connect than those who wait 30 minutes. The CARE model prioritizes engagement signals and timeline urgency to ensure your fastest response times align with your highest-probability leads.

The four dimensions are weighted to reflect real-world conversion patterns: engagement behavior (30%) carries the most weight because a financially qualified buyer who does not return calls will never close, while a highly engaged lead with flexible finances often finds a way to transact.

## Advanced Configuration

| Parameter | Default | Range | Description |
|---|---|---|---|
| ready_now_threshold | 75 | 65-90 | Minimum score to qualify as READY NOW |
| warming_up_threshold | 50 | 35-65 | Minimum score to qualify as WARMING UP |
| nurture_threshold | 25 | 15-40 | Minimum score to qualify as LONG-TERM NURTURE |
| source_weight | 20% | 10-30% | Weight of lead source in total score |
| financial_weight | 25% | 15-35% | Weight of financial readiness in total score |
| timeline_weight | 25% | 15-35% | Weight of timeline urgency in total score |
| engagement_weight | 30% | 20-40% | Weight of behavioral engagement in total score |
| response_time_target_tier1 | 1 hour | 5 min - 4 hours | Maximum response time for READY NOW leads |
| stale_lead_threshold_days | 90 | 30-180 | Days before a lead with no engagement is auto-downgraded |
| re_score_interval_days | 30 | 14-90 | How often to automatically re-score existing pipeline leads |

## Example

**Input:**
```
Batch of 4 leads from various sources — Austin, TX market:

Lead 1:
  lead_name: Sarah & Mike Thompson
  lead_type: buyer
  lead_source: referral
  referral_source_name: Jennifer Walsh (closed with you in 2025)
  pre_approved: yes
  stated_budget: 550000
  timeline: 1-3-months
  motivation_notes: "Relocating from Denver for Mike's new job starting April 1"
  contact_attempts: 0
  contact_responses: 0
  days_in_pipeline: 1
  engagement_notes: "Jennifer texted you directly, said they are serious and ready"

Lead 2:
  lead_name: David Park
  lead_type: buyer
  lead_source: zillow
  pre_approved: unknown
  stated_budget: 400000
  timeline: unknown
  contact_attempts: 1
  contact_responses: 0
  days_in_pipeline: 3
  engagement_notes: "Clicked on 3 listings on Zillow, submitted inquiry form"

Lead 3:
  lead_name: Linda Guerrero
  lead_type: seller
  lead_source: open-house
  pre_approved: N/A
  property_to_sell: 4521 Oakmont Blvd, Austin, TX 78749
  timeline: 3-6-months
  motivation_notes: "Downsizing after youngest left for college, wants to move to a condo"
  contact_attempts: 0
  contact_responses: 0
  days_in_pipeline: 0
  engagement_notes: "Visited your open house at a neighbor's listing, asked about market values, gave full contact info"

Lead 4:
  lead_name: Jason Reed
  lead_type: buyer
  lead_source: paid-ad
  pre_approved: no
  stated_budget: 300000
  timeline: just-looking
  contact_attempts: 2
  contact_responses: 0
  days_in_pipeline: 14
  engagement_notes: "Clicked Facebook ad for first-time buyer guide, downloaded the PDF"
```

**Output:**
```
# Lead Qualification Report

**Generated:** 2026-02-12
**Agent:** [Your Name]
**Batch Size:** 4 leads
**Source Mix:** 1 Referral, 1 Zillow, 1 Open House, 1 Paid Ad

---

## Priority Rankings

| Rank | Lead Name | Type | Score | Tier | Top Signal | Recommended Action |
|---|---|---|---|---|---|---|
| 1 | Sarah & Mike Thompson | Buyer | 90/100 | READY NOW | Past-client referral, pre-approved, relocation deadline | Call within 1 hour, schedule buyer consultation |
| 2 | Linda Guerrero | Seller | 65/100 | WARMING UP | Open house engagement, gave full info, equity positive | Call within 24 hours, offer free CMA |
| 3 | David Park | Buyer | 34/100 | LONG-TERM NURTURE | Zillow inquiry, unknown financials, no response | Send personalized email, add to drip |
| 4 | Jason Reed | Buyer | 24/100 | NOT QUALIFIED | Paid ad click, no pre-approval, just looking, no engagement | Automated drip only, re-score in 90 days |

---

## Detailed Lead Scorecards

### Lead 1: Sarah & Mike Thompson — Buyer

**Score: 90/100 — READY NOW**

| Dimension | Score | Details |
|---|---|---|
| Lead Source Quality | 20/20 | Referral from Jennifer Walsh (past client, closed 2025) + referral bonus |
| Financial Readiness | 25/25 | Pre-approved, $550K budget — well within Austin median |
| Timeline & Urgency | 25/25 | 1-3 months + job relocation with start date (+5) = 25 (capped) |
| Engagement & Behavior | 20/30 | Inbound via referral, not direct contact yet — high implied intent |

**Key Facts:**
- Source: Referral (Jennifer Walsh, past client)
- Budget: $550,000 | Pre-approved: Yes
- Timeline: 1-3 months (job starts April 1)
- Motivation: Relocating from Denver for new job
- Days in Pipeline: 1
- Contact History: 0 attempts, 0 responses (just received)

**Action Plan:**
1. Call within 1 hour — reference Jennifer by name, welcome them to Austin
2. Send a curated list of 8-10 homes in their budget within target neighborhoods
3. Schedule a buyer consultation (video call if they are still in Denver) within 48 hours
4. Connect them with your preferred local lender for a Texas-specific pre-approval letter

**Personalized Outreach Script:**
> "Hi Sarah and Mike, this is [Your Name] — Jennifer Walsh passed along your info and told me about your move to Austin. Congratulations on Mike's new position! I have helped several families relocate to Austin and I know how overwhelming it can be to house-hunt from out of state. I have already pulled together some properties in the $500-550K range in areas that match what Jennifer mentioned you are looking for. Would a quick 15-minute video call this week work to go over the neighborhoods and get you started?"

**CRM Tags:** ready-now, referral, buyer, relocating, pre-approved, 1-3-months

---

### Lead 2: Linda Guerrero — Seller

**Score: 65/100 — WARMING UP**

| Dimension | Score | Details |
|---|---|---|
| Lead Source Quality | 15/20 | Open house attendee, engaged with questions, full contact info |
| Financial Readiness | 20/25 | Likely positive equity (long-term owner in appreciating market), needs CMA |
| Timeline & Urgency | 14/25 | 3-6 months (12) + downsizing after kids leave (+2) = 14 |
| Engagement & Behavior | 16/30 | Visited open house, asked market value questions, volunteered contact info |

**Key Facts:**
- Source: Open House (neighbor's listing at Oakmont Blvd)
- Property: 4521 Oakmont Blvd, Austin, TX 78749
- Budget: N/A (seller) | Pre-approved: N/A
- Timeline: 3-6 months
- Motivation: Downsizing, empty nest, wants a condo
- Days in Pipeline: 0
- Contact History: 0 attempts, 0 responses (just met)

**Action Plan:**
1. Call within 24 hours — reference meeting at the open house, mention the neighborhood by name
2. Offer a complimentary CMA for her home — this is the highest-value next step for sellers
3. Send a "What your home is worth" email with 2-3 recent neighborhood comps as a teaser
4. Feed property details to Skill 03 (Market Analysis Reporter) to prepare a professional CMA

**Personalized Outreach Script:**
> "Hi Linda, this is [Your Name] — it was great meeting you at the open house on Oakmont Blvd yesterday! You mentioned you are thinking about downsizing to a condo now that the kids are off to college. I completely understand that transition — it is a great time to take advantage of what your home is worth in this market. I would love to put together a free market analysis showing exactly what your home could sell for based on recent sales on your street. No commitment, just good information to help you plan. Want me to send that over this week?"

**CRM Tags:** warming-up, open-house, seller, downsizing, 3-6-months

---

### Lead 3: David Park — Buyer

**Score: 34/100 — LONG-TERM NURTURE**

| Dimension | Score | Details |
|---|---|---|
| Lead Source Quality | 9/20 | Zillow inquiry — high volume, low commitment source |
| Financial Readiness | 10/25 | Stated $400K budget but no lender contact, unknown pre-approval |
| Timeline & Urgency | 3/25 | Unknown timeline, no stated motivation |
| Engagement & Behavior | 12/30 | Clicked 3 listings + submitted form, but no response to call attempt |

**Key Facts:**
- Source: Zillow
- Budget: $400,000 | Pre-approved: Unknown
- Timeline: Unknown
- Motivation: None stated
- Days in Pipeline: 3
- Contact History: 1 attempt, 0 responses

**Action Plan:**
1. Send a personalized email within 48 hours referencing the 3 specific listings he clicked on
2. Add to bi-weekly automated listing alert matching his price range and viewed property style
3. Try calling once more at a different time of day (evening if first attempt was daytime)
4. Re-score in 30 days — if still no response, downgrade to NOT QUALIFIED

**Personalized Outreach Script:**
> "Hi David, this is [Your Name] — I saw you were checking out a few homes in the $400K range on Zillow, including that one on [street name]. Great taste! I have a few similar properties that just came on the market that I think you would like. Would it be helpful if I set up automatic alerts so you are the first to know when new listings match what you are looking for? Happy to help — just text me back and I will get those started."

**CRM Tags:** long-term-nurture, zillow, buyer, unknown-timeline

---

### Lead 4: Jason Reed — Buyer

**Score: 24/100 — NOT QUALIFIED**

| Dimension | Score | Details |
|---|---|---|
| Lead Source Quality | 8/20 | Paid ad (Facebook) — interest exists but commitment unclear |
| Financial Readiness | 5/25 | No pre-approval, $300K budget stated (entry-level for Austin) |
| Timeline & Urgency | 3/25 | "Just looking" — no urgency signals |
| Engagement & Behavior | 8/30 | Downloaded guide but zero response to 2 contact attempts over 14 days |

**Key Facts:**
- Source: Facebook Ad (first-time buyer guide)
- Budget: $300,000 | Pre-approved: No
- Timeline: Just looking
- Motivation: First-time buyer (implied from guide download)
- Days in Pipeline: 14
- Contact History: 2 attempts, 0 responses

**Action Plan:**
1. No more personal calls — add to automated first-time buyer drip campaign
2. Send monthly market update email with first-time buyer tips
3. Re-score in 90 days — if engagement increases (email opens, link clicks), upgrade tier
4. If no engagement at 180 days, archive and stop outreach

**Personalized Outreach Script (Automated Email):**
> "Hi Jason, thanks for downloading our First-Time Buyer Guide — I hope it has been helpful! The Austin market is always changing, so I will be sending you monthly updates on new listings and tips for first-time buyers. When you are ready to take the next step, I am here to help — no pressure, no timeline. Just reply to this email anytime."

**CRM Tags:** not-qualified, paid-ad, buyer, first-time-buyer, just-looking

---

## Pipeline Summary

| Tier | Count | % of Batch | Time Allocation |
|---|---|---|---|
| READY NOW | 1 | 25% | 50% of daily outreach time |
| WARMING UP | 1 | 25% | 30% of daily outreach time |
| LONG-TERM NURTURE | 1 | 25% | 15% of daily outreach time |
| NOT QUALIFIED | 1 | 25% | 5% (automated only) |

**Conversion Forecast:**
- READY NOW leads: 65% expected to transact within 30 days
- WARMING UP leads: 25% expected to transact within 90 days
- Pipeline Value: ~$23,375 estimated GCI (assuming 3.0% commission average on $550K + $400K pipeline)

**Priority Actions This Week:**
1. Call the Thompsons within 1 hour — this is your highest-probability deal and a referral you cannot let cool off
2. Call Linda Guerrero tomorrow morning and offer the free CMA — she is a warm seller lead in your farm area
3. Send David Park a personalized listing email referencing his Zillow activity
4. Data gaps: Get David's pre-approval status, confirm Linda's home details for CMA, verify Jason's actual timeline
```

## Edge Cases & Best Practices

- **Dual Buyer-Seller Leads:** When a lead needs to sell their current home AND buy a new one, score them twice — once as a seller and once as a buyer. Use the higher score for tier assignment but create action plans for both sides of the transaction. Dual-transaction leads are your highest-value clients (two commissions) and should get Tier 1 treatment even if one side scores lower.

- **Leads Working with Another Agent:** If `current_agent` is "yes," do not aggressively pursue. Score normally but adjust the outreach script to be consultative rather than sales-oriented. Offer value without poaching. If they are under contract with an agent, respect that — mark as COLD and revisit only if they reach out to you.

- **Open House Leads with Incomplete Info:** Many open house visitors provide only a first name and email. Score engagement normally but flag for data enrichment. Use the email to look up their full profile, and send a "great meeting you" follow-up that encourages them to share their timeline and needs.

- **Stale Pipeline Leads (60+ Days, No Contact):** Leads that have been in your pipeline for 60+ days with zero response should be automatically downgraded one tier. Do not keep calling — switch to a different channel (text if you have been calling, handwritten note if you have been texting). At 180 days with no engagement, archive and free up mental bandwidth.

- **Referral Leads You Cannot Reach:** When a past client gives you a referral but the lead does not answer, loop the referrer back in. Ask them to send a warm text introduction. This can increase connection rates by 300% compared to a cold call from an unknown number.

- **Agent Team Leads vs. Individual Agent Leads:** If you are a team lead receiving leads for distribution, add a "team_member_match" field to assign leads to the agent whose expertise matches (luxury, first-time buyer, relocation, etc.). The scoring model remains the same, but the action plan should include the assigned agent's name.

- **Seasonal Adjustments:** In spring/summer markets, tighten the READY NOW threshold to 80+ because inventory moves faster and leads need quicker response. In winter markets, loosen to 70+ and extend the response window slightly since transactions take longer.

- **Investor-Buyer Leads:** Leads who identify as investors looking for personal residences should be scored as regular buyers. Leads looking for investment properties should be flagged differently — their timeline, motivation, and financial criteria are fundamentally different from homebuyers.

## 🔐 PERMISSIONS & SETUP CHECKLIST

No external permissions or setup required to run this skill in standalone chat mode. Optional integrations:

- [ ] **CRM Export (optional):** If pulling from Follow Up Boss, kvCORE, Sierra Interactive, or Salesforce — export contacts as CSV with columns matching the Required Inputs table. No API key needed; the skill reads CSV pasted directly into the chat.
- [ ] **Claude.ai Project (recommended for teams):** Upload this file once to a Project; every team member can activate the skill without re-attaching. No additional config.
- [ ] **Compliance check (one-time):** Confirm that any opening-message template you adopt has been reviewed against your state's TCPA / Do-Not-Call / SMS-consent requirements before the first send. The skill drafts copy; the user's responsibility is the consent record.

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
| Lead has a "current agent: yes" flag | Auto-tier as Not Qualified UNLESS the user notes the agency relationship is ending or the lead initiated contact themselves; flag for ethics review (RESPA/agent-poaching risk varies by state) |
| Lead source is unknown or blank | Score source as 5 (default cold-call equivalent) and add a recommended discovery question to the opening message: "Where did you hear about me?" |
| Foreign-language lead text in batch | Translate the lead's notes inline, score normally, and draft the opening message in the inferred preferred language (Spanish/Mandarin/etc.) flagged for review by a fluent agent |

## 📖 DOMAIN GLOSSARY

- **ARV (After-Repair Value):** The estimated market value of a property after all renovations and repairs are completed. Used by investor-buyer leads to evaluate flip or BRRRR opportunities; agents working with investors should know each property's ARV ceiling.
- **CMA (Comparative Market Analysis):** An agent-prepared analysis of recently sold, pending, and active listings comparable to a subject property — used to recommend a list price for sellers or an offer range for buyers. The single most powerful conversion tool for warming up seller leads.
- **FSBO (For Sale By Owner):** A homeowner attempting to sell without listing-agent representation. FSBO outreach is a recognized lead source — many FSBOs convert to listings within 30–60 days when the owner realizes the marketing and negotiation workload.
- **Expired Listing:** An MLS listing whose contract term ended without a sale. Expired-listing outreach targets sellers who already wanted to sell but chose the wrong agent or wrong price; conversion rates are higher than cold calls.
- **MLS (Multiple Listing Service):** The regional database of properties for sale, accessed only by licensed members. Lead-source signal: leads sourced through your IDX MLS feed are typically higher-intent than aggregator sites.
- **LOI (Letter of Intent):** A non-binding written expression of a buyer's intent to purchase, often used in commercial or investor transactions before a formal purchase agreement. A lead who mentions an LOI is well into their process and should likely tier as READY NOW.

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

- **Skill 02 (Property Description Generator):** For READY NOW seller leads, use the Property Description Generator to quickly draft a sample listing description during your listing presentation — showing sellers what their home could look like on the MLS builds immediate confidence.
- **Skill 03 (Market Analysis Reporter):** Feed WARMING UP and READY NOW seller leads directly into the Market Analysis Reporter to generate a professional CMA before your listing appointment — the CMA is the #1 tool for winning listings.
- **Skill 04 (Client Follow-Up Sequencer):** After scoring leads, use the Follow-Up Sequencer to generate the exact touchpoint schedule for each tier — HOT leads get a 7-day intensive sequence, NURTURE leads get a 90-day drip.
- **Skill 05 (Objection Handler Coach):** When WARMING UP leads express hesitation during follow-up calls ("I want to wait for prices to drop," "I am not ready"), pull up the Objection Handler for real-time response coaching.
- **Skill 06 (Contract Review Assistant):** When READY NOW leads move to the offer stage, feed the purchase agreement into the Contract Review Assistant to catch red flags before your client signs.
- **Skill 07 (Social Media Content Planner):** Use pipeline data to inform your social media strategy — if most leads are first-time buyers, plan content that speaks to their questions and fears.
