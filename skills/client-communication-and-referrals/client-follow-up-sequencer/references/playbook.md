# Source playbook

This playbook supplies task procedures and examples. Follow the working rules in the skill entry, verify current jurisdiction-specific claims, and treat examples as illustrative.

# Client Follow-Up Sequencer

Turn every lead into a relationship with a structured follow-up system that never lets a prospect slip through the cracks. This skill designs complete, multi-channel follow-up sequences tailored to each client type — new buyer leads, new seller leads, post-showing follow-ups, post-offer communications, past clients, and sphere of influence. For each stage, you get the exact message (email, text, or call script), the optimal timing, and the channel selection logic. Every template includes personalization tokens so your outreach feels human even when it is systematized. Built for agents who know that 80% of sales happen between the 5th and 12th contact, but most agents give up after 2.

## 🧠 SKILL IDENTITY

**WHO this skill is for:**
An agent, team lead, wholesaler, or property manager with 50+ contacts in pipeline who knows 80% of sales happen between contact 5 and contact 12 — but only follows up 2 times before leads go cold because writing personalized cadences takes too long.

**WHAT this skill does:**
Generates a personalized multi-channel follow-up sequence (call/SMS/email/handwritten note/video) for a specific client by stage (new lead, warm prospect, under-contract client, post-close past-client, dormant sphere). Output: timing, channel selection per touchpoint, ready-to-send message templates with personalization filled in, an objection-aware re-engagement plan, a referral-ask script, and metrics to track.

**WHERE to use this skill:**
Standalone chat for one-off cadences; Project for team consistency; Cowork Task for batching cadences for 50+ contact CRM segments.

**WHEN to activate this skill:**
Immediately after a new lead enters pipeline; on day a transaction goes pending; 7 days after closing; when a lead has gone silent 21+ days; quarterly sphere reactivation.

**WHY this skill matters:**
This workflow makes the required inputs and output structure explicit. Its numerical benchmarks are configurable assumptions, not validated performance claims.

**HOW this skill works (Overview):**
Claude reads the client's stage, source, motivation, and prior interactions, selects the right cadence pattern (length, channel mix, timing), drafts each touchpoint with the client's name and specific reference points worked in, layers in a re-engagement branch for non-responders, and closes with a referral-ask script.

## When to Use

- Setting up a follow-up sequence for a brand new lead (any source)
- Designing the post-showing communication plan for a buyer you just toured with
- Creating a post-listing-appointment follow-up for a seller who said "I need to think about it"
- Building a past-client nurture campaign to generate referrals and repeat business
- Automating your sphere-of-influence touches (friends, family, former colleagues)
- Re-engaging cold leads that went silent 30-90 days ago
- Designing the communication plan for a buyer or seller under contract (closing coordination)
- Creating a post-closing follow-up sequence to turn a client into a referral source

## 📥 REQUIRED INPUTS

| Parameter | Type | Required | Description |
|---|---|---|---|
| client_name | string | Yes | Full name of the client |
| client_type | string | Yes | new-buyer-lead, new-seller-lead, post-showing, post-listing-appointment, under-contract-buyer, under-contract-seller, post-closing, past-client, sphere-of-influence, re-engagement |
| lead_source | string | No | Where the lead came from (open-house, zillow, referral, etc.) |
| contact_phone | string | Yes | Phone number for text and call touchpoints |
| contact_email | string | Yes | Email address |
| key_details | string | No | Relevant context: property they viewed, price range, timeline, neighborhood preference, etc. |
| last_contact_date | string | No | Date of most recent contact (YYYY-MM-DD) |
| last_contact_outcome | string | No | What happened: no-answer, brief-chat, detailed-conversation, showed-property, sent-cma, made-offer, said-not-ready |
| preferred_channel | string | No | client's preferred communication: text, email, call, any (default: any) |
| agent_name | string | Yes | Your name (for message personalization) |
| urgency_level | string | No | hot, warm, cool, cold (default: warm) |
| special_dates | string | No | Birthday, home anniversary, closing anniversary (for past clients) |

## ⚙️ EXECUTION SOP

### Step 1: Sequence Type Selection

**What Claude does:** Map the user's `client_type` to the matching cadence template (length, intensity, primary goal) using the table below.
**Tools / Resources needed:** Sequence-template lookup table; agent's CRM context if attached.
**Data source:** User-provided `client_type`, `urgency_level`, `lead_source`.
**Output of this step:** A confirmed sequence type with length (e.g., "14 touchpoints over 90 days") and a stated primary conversion goal.
**Cowork behavior:** PROCEED WITH ANALYSIS AND DRAFTING
**If this step fails or required data is missing:** If `client_type` is unclear, ask the user to pick one of the 10 enumerated types — do not guess.

Match the `client_type` to the appropriate sequence template:

| Client Type | Sequence Length | Intensity | Primary Goal |
|---|---|---|---|
| new-buyer-lead | 14 touchpoints over 90 days | High (daily -> weekly -> biweekly) | Convert to buyer consultation |
| new-seller-lead | 12 touchpoints over 60 days | High (daily -> weekly) | Convert to listing appointment |
| post-showing | 8 touchpoints over 21 days | Medium (daily -> every 3 days) | Get feedback, schedule next showing or offer |
| post-listing-appointment | 7 touchpoints over 14 days | High (daily -> every 2 days) | Secure the listing agreement |
| under-contract-buyer | 10 touchpoints over 30-45 days | Medium (milestone-based) | Smooth closing, manage expectations |
| under-contract-seller | 10 touchpoints over 30-45 days | Medium (milestone-based) | Smooth closing, manage expectations |
| post-closing | 12 touchpoints over 12 months | Low (monthly -> quarterly) | Generate referrals and repeat business |
| past-client | 8 touchpoints per year | Low (quarterly + special dates) | Stay top-of-mind, generate referrals |
| sphere-of-influence | 6 touchpoints per year | Low (bimonthly) | Maintain relationship, ask for referrals |
| re-engagement | 5 touchpoints over 30 days | Medium (strategic spacing) | Re-qualify or archive |

### Step 2: Channel Selection Logic

**What Claude does:** Assign the optimal channel (text/email/call/handwritten/video) to each touchpoint, alternating channels to honor the rotation rule.
**Tools / Resources needed:** Channel-selection matrix below; client's `preferred_channel` constraint; TCPA / DNC awareness checklist.
**Data source:** Step 1 cadence template + `preferred_channel` + `last_contact_outcome`.
**Output of this step:** Touchpoint-by-touchpoint channel map.
**Cowork behavior:** PROCEED WITH ANALYSIS AND DRAFTING
**If this step fails or required data is missing:** If a channel was not consented to (e.g., no SMS opt-in on record), drop SMS from the cadence and substitute email/call; flag the constraint in the output.

Choose the optimal channel for each touchpoint based on context:

| Scenario | Best Channel | Reasoning |
|---|---|---|
| First contact with a new online lead | Text | Highest open rate (98%), fastest response |
| Follow-up after no response to text | Call | Voice creates personal connection |
| Sharing market data or listings | Email | Allows links, images, attachments |
| Quick check-in after showing | Text | Casual, low-pressure |
| Listing appointment follow-up | Call + Email | Call for relationship, email for CMA recap |
| Under-contract milestone update | Call or Text | Depends on urgency of update |
| Past client birthday/anniversary | Text + Handwritten note | Personal touch stands out |
| Re-engagement (cold lead) | Email | Non-intrusive, allows them to respond on their time |
| Referral request | Call | Personal ask gets higher conversion |

**Channel Rotation Rule:** Never use the same channel for 3 consecutive touchpoints. Alternating channels increases response rates by 40-60%.

### Step 3: Message Template Generation

**What Claude does:** For each touchpoint, write the complete ready-to-send message — subject line if applicable, body, personalization slots filled with `client_name` / `agent_name` / `key_details`, and branch responses (positive / no-response / negative).
**Tools / Resources needed:** Tone guidelines per client type; objection-bank for re-engagement; agent's voice samples if attached.
**Data source:** Steps 1–2 outputs + `key_details` + `agent_name`.
**Output of this step:** Touchpoint-numbered messages, fully personalized, with conditional follow-up logic per branch.
**Cowork behavior:** PROCEED WITH ANALYSIS AND DRAFTING
**If this step fails or required data is missing:** If `key_details` is empty, write neutral templates and leave bracketed `[Specific reference point]` slots for the user to fill in.

For each touchpoint, generate the complete message with these components:

**Template Structure:**
```
Touchpoint [N]: [Channel] — [Timing]
Subject/Purpose: [one-line description]
Personalization tokens: {client_name}, {agent_name}, {property_address}, {neighborhood}, {price_range}

[Complete message text ready to send]

If no response: [what to do]
If positive response: [next step]
If negative response: [graceful exit]
```

**Message Tone Guidelines by Client Type:**
- **New leads:** Helpful, consultative, no-pressure ("just checking in to be a resource")
- **Post-showing:** Specific, detail-oriented ("what did you think about the kitchen layout?")
- **Post-listing-appointment:** Confident, value-focused ("here is the marketing plan we discussed")
- **Under contract:** Professional, proactive ("here is what happens this week")
- **Past clients:** Warm, genuine, celebratory ("happy one-year home anniversary!")
- **Re-engagement:** Curious, low-pressure ("are you still thinking about...")

### Step 4: Timing Optimization

**What Claude does:** Place each touchpoint on a specific day-of-week + time-of-day slot, optimizing for response rate per channel.
**Tools / Resources needed:** Day-of-week + time-of-day optimization tables (below); agent's time zone; client's last-known time zone.
**Data source:** Step 2 channel map + `last_contact_date` + agent's working hours.
**Output of this step:** A scheduled calendar of touchpoints with timing rationale.
**Cowork behavior:** PROCEED WITH ANALYSIS AND DRAFTING
**If this step fails or required data is missing:** Default to agent's local timezone and weekday-business-hours scheduling; flag any cross-timezone clients for manual review.

Apply optimal timing based on research and industry data:

| Day of Week | Best For | Avoid |
|---|---|---|
| Tuesday | Email campaigns, first outreach | — |
| Wednesday | Follow-up calls, showing scheduling | — |
| Thursday | Listing appointment follow-ups | — |
| Saturday | Open house follow-ups, showing follow-ups | Evening (family time) |
| Monday | Re-engagement emails, weekly market updates | Before 10am (inbox overload) |
| Friday | Light check-ins, weekend showing scheduling | Afternoon (people check out) |
| Sunday | Market update emails (for Monday morning reads) | Calls (intrusive) |

**Time of Day:**
- **Texts:** 9:00-10:00am or 5:00-6:30pm (before work starts, after work ends)
- **Calls:** 10:00am-12:00pm or 2:00-4:00pm (business hours, post-morning rush)
- **Emails:** 7:00-8:00am (top of inbox) or 1:00-2:00pm (post-lunch scan)

### Step 5: Re-engagement Triggers

**What Claude does:** Define automatic branch logic for what happens if the lead goes silent or generates a behavioral signal (clicks an email, views a listing, hits an anniversary).
**Tools / Resources needed:** Trigger-condition table below; CRM behavioral-event names if integration is in scope.
**Data source:** Step 1–4 outputs; user's CRM signals if accessible.
**Output of this step:** A decision-tree-style appendix to the cadence covering each trigger and the response action.
**Cowork behavior:** CONFIRM BEFORE PROCEEDING (re-engagement triggers can fire many automated messages — confirm with user before activating)
**If this step fails or required data is missing:** Default to time-based triggers only (30/90/180 days of silence); skip behavioral triggers if no CRM integration provided.

Define automatic re-engagement triggers for leads that go cold:

| Trigger | Condition | Action |
|---|---|---|
| Cold lead reactivation | No response after 3 touchpoints | Switch to bi-weekly email-only, send market report |
| Website activity detected | Lead clicks a listing in your email | Immediately text: "I noticed you were looking at [address] — want to see it this weekend?" |
| Price change alert | A property matching their criteria drops price | Send text/email with the update + offer to show |
| New listing match | New listing matches their saved search criteria | Send personalized text + email with details |
| Anniversary trigger | 30/90/180/365 days since last meaningful contact | Send appropriate check-in based on elapsed time |
| Market shift | Significant rate change, new inventory surge, etc. | Send market update email positioning change as opportunity |

## 📤 OUTPUT FORMAT

```
# Follow-Up Sequence: [client_name]

**Client Type:** [type]
**Sequence:** [N] touchpoints over [timeframe]
**Primary Goal:** [goal]
**Created:** [date]
**Agent:** [agent_name]

---

## Sequence Overview

| # | Day | Channel | Purpose | Status |
|---|---|---|---|---|
| 1 | Day 0 | [channel] | [purpose] | Pending |
| 2 | Day 1 | [channel] | [purpose] | Pending |
| 3 | Day 3 | [channel] | [purpose] | Pending |
| ... | ... | ... | ... | ... |

---

## Detailed Touchpoints

### Touchpoint 1: [Channel] — Day [N]

**Purpose:** [specific goal of this touchpoint]
**Timing:** [day of week, time of day]

**Message:**

[Complete, ready-to-send message with personalization tokens filled in]

**If they respond positively:** [specific next action]
**If no response:** [proceed to Touchpoint 2]
**If they say not interested:** [graceful exit script]

---

### Touchpoint 2: [Channel] — Day [N]

[Same format as above]

---

[Continue for all touchpoints]

---

## Re-engagement Plan

If the full sequence completes with no response:

1. [Action 1 — e.g., move to quarterly email drip]
2. [Action 2 — e.g., set 90-day re-score reminder]
3. [Action 3 — e.g., send one final "door is always open" message]

## Referral Ask Script (for past clients and sphere)

[Complete script for asking for referrals, with specific timing recommendation]

## Sequence Metrics to Track

| Metric | Target | How to Measure |
|---|---|---|
| Response rate | [X%] | Responses / touchpoints sent |
| Conversion rate | [X%] | Appointments / leads sequenced |
| Average touchpoints to conversion | [X] | Touchpoints before first appointment |
| Opt-out rate | < [X%] | Unsubscribes / leads sequenced |
```

## Methodology

**DRIP Framework (Deliver-Relevance-Interval-Personalize)**

The DRIP framework is built on the NAR (National Association of Realtors) finding that the average buyer contacts 1.5 agents before choosing one — meaning speed and consistency of follow-up is the primary differentiator, not skill or market knowledge. The framework ensures every touchpoint Delivers value (not just "checking in"), maintains Relevance to the client's specific situation, uses research-backed Intervals that match buyer psychology (daily urgency fading to weekly nurture), and Personalizes every message so automation feels like attention. Studies show that agents with systematic follow-up plans convert leads at 3x the rate of agents who follow up ad-hoc.

## Advanced Configuration

| Parameter | Default | Range | Description |
|---|---|---|---|
| max_touchpoints_no_response | 5 | 3-8 | Stop active outreach after N consecutive no-responses |
| text_first_delay_minutes | 5 | 1-30 | Minutes after lead receipt before first text |
| channel_rotation | true | true/false | Enforce channel alternation rule |
| include_handwritten_notes | true | true/false | Include handwritten note touchpoints for past clients |
| referral_ask_frequency | quarterly | monthly/quarterly/biannually | How often to ask past clients for referrals |
| re_engagement_window_days | 90 | 30-180 | Days of silence before triggering re-engagement |
| email_market_report_frequency | monthly | weekly/biweekly/monthly | How often to send market update emails |
| post_closing_gift_touchpoint | true | true/false | Include closing gift delivery as a touchpoint |
| include_video_touchpoints | false | true/false | Add video message options (BombBomb, Loom) |
| holiday_touchpoints | true | true/false | Include seasonal/holiday greetings in sequences |

## Example

**Input:**
```
client_name: Amanda Chen
client_type: new-buyer-lead
lead_source: open-house
contact_phone: 512-555-0187
contact_email: amanda.chen@example.com
key_details: "Attended open house at 4521 Elm St. Couple with one toddler. Looking for 3-4BR in Westlake/Eanes ISD area. Budget around $600K. Currently renting, lease ends in 4 months."
last_contact_date: 2026-02-10
last_contact_outcome: brief-chat
preferred_channel: text
agent_name: Sarah Martinez
urgency_level: warm
```

**Output:**
```
# Follow-Up Sequence: Amanda Chen

**Client Type:** New Buyer Lead (Open House)
**Sequence:** 14 touchpoints over 90 days
**Primary Goal:** Convert to buyer consultation and first showing tour
**Created:** 2026-02-12
**Agent:** Sarah Martinez

---

## Sequence Overview

| # | Day | Channel | Purpose | Status |
|---|---|---|---|---|
| 1 | Day 0 | Text | Thank you + connection | Pending |
| 2 | Day 1 | Email | Market report + similar listings | Pending |
| 3 | Day 3 | Text | Check-in + specific listing tease | Pending |
| 4 | Day 5 | Call | Buyer consultation invitation | Pending |
| 5 | Day 7 | Email | Eanes ISD school guide | Pending |
| 6 | Day 10 | Text | New listing alert | Pending |
| 7 | Day 14 | Call | Second call attempt + voicemail | Pending |
| 8 | Day 18 | Email | "What $600K buys in Westlake" report | Pending |
| 9 | Day 25 | Text | Market update + showing offer | Pending |
| 10 | Day 35 | Email | Client success story | Pending |
| 11 | Day 45 | Text | Lease timeline check-in | Pending |
| 12 | Day 60 | Email | Monthly market report | Pending |
| 13 | Day 75 | Text | "2 months until lease ends" check-in | Pending |
| 14 | Day 90 | Call | Final qualifying call | Pending |

---

## Detailed Touchpoints

### Touchpoint 1: Text — Day 0 (Same day as open house)

**Purpose:** Establish connection while the open house experience is fresh
**Timing:** Within 2 hours of open house, ideally by 5:00pm

**Message:**

Hi Amanda! This is Sarah Martinez — it was great meeting you and your family at the open house on Elm St today. I loved chatting about the Westlake area with you. I have a couple of listings coming up in the Eanes ISD zone that might be perfect for your family. Would you like me to send those over when they hit the market?

**If they respond positively:** Send listings immediately, then propose a 15-minute call or coffee meeting to discuss their search criteria in detail
**If no response:** Proceed to Touchpoint 2
**If they say not interested:** "No worries at all, Amanda! If anything changes, I'm always here. Wishing you and your family the best."

---

### Touchpoint 2: Email — Day 1 (Monday morning)

**Purpose:** Provide immediate value with relevant market data
**Timing:** Tuesday 7:30am (top of inbox)

**Subject:** 3 homes near Eanes ISD your family might love

**Message:**

Hi Amanda,

It was wonderful meeting you at the open house yesterday! I know you mentioned looking for a 3-4 bedroom in the Westlake/Eanes ISD area around $600K.

I pulled together three listings that match what you described:

1. [Listing 1 — address, beds/baths, price, one-line hook]
2. [Listing 2 — address, beds/baths, price, one-line hook]
3. [Listing 3 — address, beds/baths, price, one-line hook]

I can set up automatic alerts so you are the first to know when new homes hit the market in your target area. Just reply "yes" and I will get those started.

Also — with your lease ending in about 4 months, now is the perfect time to get pre-approved and start touring so you can close before you need to renew.

Happy to answer any questions!

Sarah Martinez
[Phone] | [Email]

**If they respond positively:** Propose a buyer consultation call or coffee meeting
**If no response:** Proceed to Touchpoint 3

---

### Touchpoint 3: Text — Day 3 (Wednesday)

**Purpose:** Keep momentum with a specific, intriguing listing
**Timing:** Wednesday 5:15pm

**Message:**

Hey Amanda — a 4BR just came on in Westlake Hills at $585K with a huge backyard. Perfect for your little one! Want me to grab you a showing this weekend? I can send photos first if you'd like.

**If they respond:** Share listing details, schedule showing
**If no response:** Proceed to Touchpoint 4

---

### Touchpoint 4: Call — Day 5 (Friday)

**Purpose:** Voice connection, invite to buyer consultation
**Timing:** Friday 10:30am

**Call Script:**

"Hi Amanda, this is Sarah Martinez — we met at the open house on Elm Street last weekend. I hope I'm not catching you at a bad time! I wanted to check in because I sent over a few listings in the Eanes ISD area and wanted to see if any of them caught your eye.

I also wanted to mention — I do a complimentary buyer consultation where we sit down for about 20 minutes and I walk you through exactly how the buying process works in this market, what to expect with timelines, and how to make your $600K budget go as far as possible. No pressure, just good information. Would that be helpful?"

**If they schedule:** Confirm time, send calendar invite, prepare CMA materials
**If voicemail:** "Hi Amanda, Sarah Martinez here — just a quick call to see if any of those Westlake listings caught your attention. I will send you a text with a couple more options this week. Talk soon!"
**If not interested:** "Totally understand, Amanda. I will keep your info on file and if you ever want to jump back in, just give me a shout. Best to your family!"

---

### Touchpoint 5: Email — Day 7

**Purpose:** Provide high-value content related to their specific need (schools)
**Timing:** Monday 7:30am

**Subject:** Your guide to Eanes ISD schools (from a local agent who knows them)

**Message:**

Hi Amanda,

Since schools are important to your family's search, I put together a quick guide to the Eanes ISD schools — ratings, boundaries, and which neighborhoods feed into each campus.

[Attach or link to school guide]

The neighborhoods that get you into the highest-rated elementary schools while staying in your budget are [X], [Y], and [Z]. I would love to show you homes in those areas when you are ready.

Let me know if you have any questions about the schools or the market!

Sarah

---

[Touchpoints 6-14 continue with similar detail, progressively shifting from active pursuit to value-providing nurture, with the lease timeline as a recurring urgency anchor]

### Touchpoint 11: Text — Day 45

**Purpose:** Lease timeline creates natural urgency
**Timing:** Weekday 9:30am

**Message:**

Hey Amanda! Just thinking about you — your lease is about 2.5 months out, right? If you want to close before it ends, now is the sweet spot to start touring seriously. Homes in your range are taking about 3-4 weeks from offer to close in this market. Want to grab coffee this week and map out a game plan?

---

### Touchpoint 14: Call — Day 90

**Purpose:** Final qualifying call — determine if lead is active or should move to long-term nurture
**Timing:** Weekday 2:00pm

**Call Script:**

"Hi Amanda, Sarah Martinez. I know we have been going back and forth for a few months and I just wanted to check in one more time. Are you and your family still thinking about buying in the Westlake area? If the timing is not right, that is completely fine — I can put you on my monthly market update list so you stay informed without any pressure. Just want to make sure I am being helpful, not annoying!"

**If active:** Reset sequence with fresh urgency, schedule showing tour
**If not ready:** Move to past-client/sphere quarterly touchpoint cadence
**If not interested:** Thank them, remove from active sequence, add to annual holiday card list only

---

## Re-engagement Plan

If the full 14-touchpoint sequence completes with no response:

1. Move Amanda to quarterly email-only cadence (monthly market report + quarterly personal check-in)
2. Set a 6-month re-engagement trigger — if her lease renewal date is known, trigger outreach 4 months before next renewal
3. Send one final "door is always open" text: "Hi Amanda! I've loved keeping you updated on the Westlake market. I'm going to scale back my outreach so I'm not clogging your inbox, but I'm always just a text away when you're ready to start looking. Wishing your family well! — Sarah"

## Referral Ask Script (for past clients and sphere)

"Hey [client_name], I hope the new home is treating you well! Quick question — do you know anyone who is thinking about buying or selling? I have some availability to take on a couple more clients and I would love to give someone you know the same experience you had. No pressure at all — just thought I'd ask. And if you ever need anything for the house — contractor recommendations, landscaper, plumber — I have a great list. Just text me anytime."

## Sequence Metrics to Track

| Metric | Target | How to Measure |
|---|---|---|
| Response rate | 35%+ | Responses / touchpoints sent |
| Conversion to appointment | 15-20% | Appointments / leads sequenced |
| Average touchpoints to conversion | 4-6 | Touchpoints before first appointment |
| Opt-out rate | < 5% | Unsubscribes / leads sequenced |
| Referral generation (past clients) | 2+ per year | Referrals received / past clients in sequence |
```

## Edge Cases & Best Practices

- **Leads Who Respond Once Then Go Silent:** After a positive initial response followed by silence, do not restart the sequence from scratch. Send a light, specific text referencing their last stated interest: "Hey Amanda, that 4BR on Oak Hill I told you about just dropped to $579K. Still on your radar?" A specific detail proves you remember them and are not mass-blasting.

- **Dual-Agent Situations (Buyer Already Has an Agent):** If a lead mentions they are working with another agent, do not continue the sales sequence. Switch immediately to a value-only cadence: monthly market reports, no CTAs, no showing offers. If their agent relationship ends, they will remember you as the one who respected boundaries.

- **Text Message Compliance (TCPA):** Always get written consent before texting. Open house sign-in sheets should include a "consent to text" checkbox. If consent is unclear, use email for the first touchpoint and ask for text permission in the email. Never add leads to automated text campaigns without consent.

- **Past Clients Who Had a Bad Experience:** If a transaction was difficult (delayed closing, inspection issues, etc.), adjust the post-closing sequence to be more empathetic. Replace celebratory language with supportive language: "I know the process was stressful, but I'm glad we got through it together. I'm here if you need anything as you settle in."

- **Spouse/Partner Dynamics:** When communicating with a couple, address both people in messages. If one partner is the primary contact but both are decision-makers, occasionally ask: "Have you and [partner name] had a chance to talk about the listings I sent?" This acknowledges the decision is shared.

- **Holiday and Weekend Boundaries:** Avoid texting or calling on major holidays, Sundays before 10am, or evenings after 8pm. Schedule email for Tuesday-Thursday mornings. Exception: if a client initiated weekend contact first, it is acceptable to respond on weekends.

- **Lead Recycling:** When a "not interested" lead re-engages 6-12 months later (they reach out again), start a fresh sequence but reference the prior relationship: "Welcome back, Amanda! A lot has changed in the Westlake market since we last talked. Here's what's new..."

## 🔐 PERMISSIONS & SETUP CHECKLIST

No external permissions required. Optional setup:

- [ ] **Brokerage compliance one-time:** Confirm your TCPA / CAN-SPAM / state Do-Not-Call policy and SMS-consent record-keeping process. Claude drafts copy; the user is responsible for the consent record.
- [ ] **CRM cadence import (optional):** If using Follow Up Boss, kvCORE, or Sierra Interactive, the skill can output the sequence as JSON for direct cadence import — say so on activation.
- [ ] **Voice baseline (recommended):** Paste 2–3 of your strongest past follow-up emails on first use; Claude mirrors your voice for the rest of the session/Project.
- [ ] **Brand assets (optional):** If your brokerage has approved video-message templates (e.g., BombBomb), reference them.

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
| Client has explicitly opted out of one channel (no SMS, no calls before 9am) | Auto-honor the constraint, redistribute the touchpoint to a different channel, add a "Channel Preference" line at the top of the cadence summary |
| Client is in legal/transactional crisis (divorce-pending, foreclosure, probate) | Drop sales-y language, switch to "support and information" tone, recommend a 2-week pause on commercial CTAs, surface a ⚠️ flag noting jurisdiction-specific outreach restrictions may apply |

## 📖 DOMAIN GLOSSARY

| Term | Definition |
|------|-----------|
| ARV | After Repair Value — the projected market value of a property after all repairs and improvements are completed, based on closed comparable sales |
| CMA | Comparative Market Analysis — an evaluation of a property's value based on recent sales of similar nearby properties |
| FSBO | For Sale By Owner — a property sold without a listing agent |
| Expired Listing | A property whose listing agreement ended without a sale, often a high-intent re-list opportunity |
| MLS | Multiple Listing Service — the regional database of active and sold listings used by licensed agents |
| BPO | Broker Price Opinion — a professional valuation prepared by a licensed broker without a full appraisal |
| Cadence | A structured sequence of touchpoints over time, designed to advance a contact from one pipeline stage to the next without manual scheduling per client. |
| Days on Market (DOM) | The number of days a property is actively listed before going under contract |
| Fair Housing Act | Federal law prohibiting discrimination in housing based on protected classes (race, color, religion, sex, national origin, familial status, disability) |

## 🚀 HOW TO USE THIS SKILL

**Method A — Standalone Claude.ai Chat (recommended for most users):**
1. Open claude.ai → start a new conversation
2. Click the paperclip / attachment icon → attach this .md file
3. Type the trigger phrase shown in the front matter
4. Provide the Required Inputs when Claude asks
5. Review output before any live use

**Method B — Claude Cowork Task (for multi-step skills):**
1. Open Claude Cowork on Mac → grant folder access
2. Reference this file in your task description
3. Type the trigger phrase as your task instruction
4. Approve Claude's plan; confirm any "CONFIRM BEFORE PROCEEDING" steps

**Method D — Claude.ai Project (for team-wide deployment):**
1. Open your Claude.ai Project → upload this .md to the knowledge base
2. Any team member can now activate the skill via the trigger phrase in Project chat

## Integration

This skill connects with the broader real estate agent toolkit:

- **Skill 01 (Lead Qualification Engine):** After scoring leads with the Qualification Engine, feed each lead's tier directly into the Sequencer — READY NOW leads get the intensive new-buyer-lead sequence, NURTURE leads get the sphere-of-influence cadence.
- **Skill 02 (Property Description Generator):** When sending listing alerts in your follow-up sequence, use the Description Generator to create personalized listing summaries rather than copy-pasting MLS descriptions.
- **Skill 03 (Market Analysis Reporter):** Embed CMA highlights in your seller follow-up sequences — the Day 1 email after a listing appointment should include key CMA data points that reinforce your pricing recommendation.
- **Skill 05 (Objection Handler Coach):** When a lead responds with an objection during the sequence ("I want to wait for rates to drop"), pull the relevant objection response from the Coach and personalize it before sending.
- **Skill 06 (Contract Review Assistant):** For under-contract sequences, use the Contract Review to generate the milestone updates that keep clients informed at each stage (inspection results, appraisal status, closing timeline).
- **Skill 07 (Social Media Content Planner):** Coordinate your follow-up sequences with your social posting schedule — when you send a "just listed" email sequence, your social channels should be promoting the same listing for maximum visibility.
