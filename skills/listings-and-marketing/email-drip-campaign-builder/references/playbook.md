# Source playbook

This playbook supplies task procedures and examples. Follow the working rules in the skill entry, verify current jurisdiction-specific claims, and treat examples as illustrative.

# Real Estate Email Drip Campaign Builder

This skill generates a complete, audience-specific email drip campaign — subject lines, full email body copy, send timing, and behavioral trigger logic — for any real estate audience segment: active buyers, active sellers, past clients, investor leads, sphere of influence, or any other defined segment. Every email is written as finished, deployable copy — not a template requiring fill-in.

## 🧠 SKILL IDENTITY

**WHO this skill is for:**
A high-volume independent agent, team lead, or brokerage owner who needs ready-to-deploy email sequences for their database — without spending 8 hours writing individual emails. Also: a real estate investor who needs a drip campaign to nurture seller leads from their direct mail or cold calling list.

**WHAT this skill does:**
Produces a complete email drip campaign package for one audience segment, containing: a 6–10 email sequence with subject lines, full body copy, and optimal send timing; behavioral trigger recommendations (what action triggers each email in an automated system); an A/B subject line variant for the 3 highest-value emails; and deployment instructions for Mailchimp, Follow Up Boss, or kvCORE.

**WHERE to use this skill:**
Attach to a Claude.ai chat session and specify your audience segment, your market, and your primary value proposition. Claude writes all emails fully — copy the output directly into your email platform.

**WHEN to activate this skill:**
Activate when setting up a new audience segment in your CRM, when a new lead source requires a dedicated nurture sequence, or when an existing drip campaign is underperforming and needs a complete rewrite.

**WHY this skill matters:**
This workflow makes the required inputs and output structure explicit. Its numerical benchmarks are configurable assumptions, not validated performance claims.

**HOW this skill works (Overview):**
Claude identifies the audience segment's stage in the buying/selling/investing cycle, their primary anxieties and motivations, and the value the agent can deliver to them at each stage. It writes each email to deliver genuine value (market insight, useful tips, relevant data) rather than pure promotion — because value-first emails generate 3–5× higher open rates than promotional emails. Every email ends with a soft, single call to action.

---

## 📥 REQUIRED INPUTS

| Input | Format | Source | Required? | Example |
|-------|--------|--------|-----------|---------|
| Audience segment | See list below | User provides | Yes | Active buyer leads — pre-approved, searching 3+ months |
| Market name | City or region | User provides | Yes | Columbus, OH |
| Campaign goal | What action should subscribers take? | User provides | Yes | Schedule a showing appointment |
| Agent name and brokerage | Plain text | User provides | Yes | Marcus Johnson, Maple Realty Group |
| Campaign length | Weeks or number of emails | User provides | No | 8 emails over 90 days |
| Agent's unique value proposition | What makes you different? | User provides | No | 12-year Columbus specialist, investor-friendly agent |
| Current market conditions | Brief summary | User provides | No | Inventory up 18%, rates at 7.1%, market cooling |

**Audience Segment Options:**
- Active buyers (pre-approved, actively searching)
- Past clients (closed more than 6 months ago)
- Sphere of influence (not actively buying/selling)
- Expired listings (listing expired, hasn't re-listed)
- FSBO leads (attempting to sell without agent)
- Investor leads (buy-and-hold, flip, or wholesale)
- Seller leads (considering listing, not yet committed)
- Rental tenants (potential future buyers)

---

## ⚙️ EXECUTION SOP

### Step 1: Define Audience Psychology and Campaign Framework

**What Claude does:**
Based on the audience segment, identify: their primary motivation (why they might take action), their primary anxiety (what's stopping them), and the #1 piece of value the agent can deliver to address both.

**Audience Psychology Profiles:**
- **Active Buyers:** Motivated by finding the right home; anxious about missing out, overpaying, or losing to competition. Value: market intelligence, off-market alerts, insider knowledge.
- **Past Clients:** Motivated by equity growth, life change; anxious about market timing. Value: their home's current estimated value, market updates, trusted advisor relationship.
- **Sphere of Influence:** Motivated by making good decisions; anxious about not knowing what they don't know. Value: education, local expertise, being top-of-mind when they're ready.
- **Expired Listings:** Motivated by finally selling; anxious the market rejected their home. Value: fresh perspective, different strategy, honest feedback.
- **FSBOs:** Motivated by saving commission; anxious about legal risk and not finding buyers. Value: data on FSBO vs. agent-assisted outcomes, co-op offer.
- **Investor Leads:** Motivated by deals and returns; anxious about missing opportunities. Value: deal analysis, market data, off-market access.
- **Seller Leads:** Motivated by moving on; anxious about net proceeds and timing. Value: market positioning, net sheet, honest pricing guidance.

**Campaign Framework (based on audience):**
- Emails 1–2: Establish relationship and deliver immediate value (no ask)
- Emails 3–4: Educate on their specific situation (soft positioning)
- Emails 5–6: Social proof and case studies (build trust)
- Emails 7–8: Direct value proposition and soft call to action
- Emails 9–10 (if used): Urgency or scarcity (market timing), final ask

**Tools / Resources needed:**
None.

**Data source:**
User-provided audience segment + user-provided market conditions.

**Output of this step:**
Audience psychology summary + campaign framework (used internally to build the sequence).

**Cowork behavior:**
PROCEED WITH ANALYSIS AND DRAFTING.

**If this step fails or required data is missing:**
If market conditions are not provided, use current national market context (rising inventory, rates above 7%, buyers have more leverage than 2021–2022) and flag: "Add your specific local market data to personalize these emails further."

---

### Step 2: Write the Full Email Sequence

**What Claude does:**
Write every email in the sequence with complete, deployable copy. Every email includes:
- Subject line (and A/B variant for emails 1, 3, and 6)
- Preview text (the line shown after the subject line in inbox)
- Full body copy (150–300 words per email — optimized for mobile reading)
- Call to action (single, soft, specific)
- Send day recommendation

**Email writing rules:**
- First line is never "I hope this finds you well" — open with something immediately valuable or intriguing
- Every email delivers genuine value in the body before making any ask
- One call to action per email — not multiple
- Use the prospect's first name in the subject line or opening for personalization
- Subject lines: 6–10 words; avoid spam triggers (FREE, URGENT, !!!)
- P.S. line at the end of every email — this is the most-read line after the subject; use it for the CTA or a bonus value point

**Tools / Resources needed:**
None.

**Data source:**
Step 1 audience psychology + user-provided market conditions and agent details.

**Output of this step:**
Complete email sequence with all required components for each email.

**Cowork behavior:**
PROCEED WITH ANALYSIS AND DRAFTING.

**If this step fails or required data is missing:**
Generate the full sequence using available information and flag where agent-specific data (their specific listings, past sale examples, testimonials) should be inserted.

---

### Step 3: Generate Behavioral Trigger Logic

**What Claude does:**
For campaigns deployed in an automated CRM (Follow Up Boss, kvCORE, Mailchimp with automation), provide behavioral trigger recommendations:

- **Email 1 trigger:** Immediately on lead entering the segment (within 5 minutes of opt-in or CRM tagging)
- **Email 2 trigger:** Day 3 if Email 1 was not replied to; or immediately if Email 1 was opened but not replied to
- **Email 3 trigger:** Day 7
- **Email 4 trigger:** Day 14, or triggered by a specific action (link click, listing view, open house registration)
- **Email 5 trigger:** Day 21
- **Email 6 trigger:** Day 30 — this is the typical drop-off point; make this email particularly strong
- **Email 7 trigger:** Day 45
- **Email 8 trigger:** Day 60
- **Behavioral branch:** If at any point the contact replies, clicks, or books an appointment → remove from drip sequence and add to active pipeline

**Tools / Resources needed:**
Follow Up Boss action plans / kvCORE drip configuration / Mailchimp automation.

**Data source:**
Email sequence from Step 2.

**Output of this step:**
Behavioral trigger logic with day-by-day schedule and engagement branch recommendations.

**Cowork behavior:**
PROCEED WITH ANALYSIS AND DRAFTING.

**If this step fails or required data is missing:**
Provide the timing schedule and note: "Adjust timing based on your CRM's automation capabilities and your market's typical lead-to-contact conversion window."

---

### Step 4: Deployment Instructions

**What Claude does:**
Provide platform-specific deployment instructions for the top 3 CRM/email platforms:

**Follow Up Boss (FUB):**
1. Navigate to Action Plans → Create New Plan
2. Name the plan: "[Audience Segment] — 90-Day Nurture"
3. Add Email steps with the subject/body from this sequence
4. Set each step's timing (Day X from plan start)
5. Create a Smart List or Tag for this audience segment
6. Assign the Action Plan to all contacts in the segment

**kvCORE:**
1. Marketing → Drip Campaigns → Create Campaign
2. Paste each email's subject and body into the campaign editor
3. Set timing intervals between steps
4. Target by behavioral tag (Buyer, Seller, Investor, etc.)
5. Enable behavioral triggers in the "Smart Drip" settings

**Mailchimp:**
1. Create an Audience Segment using tags or custom fields
2. Automations → Customer Journeys → Build new journey
3. Set trigger: "Contact added to segment"
4. Add Email actions with the provided subject and body
5. Set wait conditions between steps (Day X delays)

**Tools / Resources needed:**
Follow Up Boss / kvCORE / Mailchimp accounts.

**Data source:**
Email sequence from Step 2.

**Output of this step:**
Platform-specific deployment checklist.

**Cowork behavior:**
PROCEED WITH ANALYSIS AND DRAFTING.

**If this step fails or required data is missing:**
Provide the general deployment framework and note which steps are platform-specific.

---

## 📤 OUTPUT FORMAT

**Output type:** Email Drip Campaign Package  
**Delivery method:** Returned directly in chat — copy into email platform

---

```
EMAIL DRIP CAMPAIGN — Evy Evans
Audience:  Active Buyer Leads — Pre-Approved, Searching 3+ Months
Market:    Columbus, OH
Goal:      Schedule a showing appointment
Agent:     Marcus Johnson, Maple Realty Group
Campaign:  8 emails / 90 days

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EMAIL 1 — Send: Immediately on Lead Entry
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Subject: The Columbus market shifted — here's what it means for you
Subject B: What changed in Columbus real estate this week
Preview: Buyers have more options than they've had in 2 years.

Hi [First Name],

I don't know exactly where you are in your home search, but I do
know this: the Columbus market is behaving differently in 2026
than it was 12 months ago.

Inventory is up 18% year-over-year. Homes are sitting on market
an average of 34 days — compared to 12 days in 2024. That means
you have more options, more time to decide, and more negotiating
leverage than buyers had just a year ago.

But rates are still at 7.1%, which is keeping some buyers on
the sidelines — meaning less competition for the homes that are
available.

If you've been watching and waiting, the next 90 days may be
worth a second look.

I've been helping Columbus buyers navigate this market for 12
years. I'm happy to set you up with a custom search alert so
you see new listings the moment they hit — before they're on
Zillow.

Want me to set that up for you?

Marcus Johnson
Maple Realty Group | (614) 555-0142

P.S. Reply to this email with your 3 must-haves and I'll build
you a custom search. Takes me 5 minutes.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EMAIL 2 — Send: Day 3
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Subject: 3 Columbus homes worth a look this week
Preview: Off-market and just-listed — updated search just for you.

[Full email body follows same format...]

[Emails 3–8 continue with complete copy...]

━━━━━━━━━━━━━━━━ BEHAVIORAL TRIGGERS ━━━━━━━
Day 0 (immediate): Email 1
Day 3: Email 2 (if no reply to Email 1)
Day 7: Email 3
Day 14: Email 4
Day 21: Email 5
Day 30: Email 6 ← Most important — personalize maximum
Day 45: Email 7
Day 60: Email 8 — Final in sequence

BRANCH: If contact replies to any email → Remove from drip;
        Add "Active Conversation" tag; follow up personally

━━━━━━━━━━━━━━━━ A/B SUBJECT LINES ━━━━━━━━
Email 1: A: "The Columbus market shifted — here's what it means for you"
         B: "What changed in Columbus real estate this week"
Email 3: A: "Have you seen this Columbus neighborhood?"
         B: "3 things Columbus buyers are missing right now"
Email 6: A: "[First Name], I have a question for you"
         B: "Still looking? (honest question)"
```

---

## 🔐 PERMISSIONS & SETUP CHECKLIST

No external permissions required for copy generation.

- [ ] **CAN-SPAM Compliance:** All emails must include: your physical business address, an unsubscribe link, and honest "From" name/email. Use a business email (not @gmail) for deliverability.
- [ ] **Email Platform:** Set up Mailchimp, Follow Up Boss, or kvCORE account before deploying the sequence.
- [ ] **Contact Import:** Import or tag the audience segment in your CRM before assigning the drip sequence.
- [ ] **Phone Number:** Include a phone number in every email signature — some prospects will call rather than reply.

---

## ✅ QUALITY SELF-CHECK

Before delivering any output, Claude must internally verify every item below:

- [ ] Audience psychology was identified and every email addresses the correct motivation/anxiety
- [ ] Every email delivers genuine value before any ask
- [ ] Each email has: subject line, preview text, full body, CTA, and P.S.
- [ ] A/B subject line variants provided for emails 1, 3, and 6
- [ ] Behavioral trigger timing is specified for every email
- [ ] Email body copy is fully written — not a template with [INSERT CONTENT] gaps
- [ ] CAN-SPAM compliance requirements are noted
- [ ] Deployment instructions for at least one platform are included

---

## ⚠️ EDGE CASES & ESCALATION RULES

| Scenario | Claude's Exact Response |
|----------|------------------------|
| User requests high-pressure or aggressive language | Decline: "High-pressure email language triggers spam filters and generates unsubscribes. I'll write copy that converts through value delivery — which outperforms aggressive tactics in A/B tests." |
| User wants to target expired listings or FSBOs | Produce the sequence with appropriate tone; flag: "⚠️ Direct outreach to expired listings in some markets may conflict with MLS rules or state real estate regulations. Verify your state and MLS policies before deploying." |
| Legal compliance issue in email content | ⚠️ LEGAL FLAG: "Any email making specific investment promises, guarantees of return, or predictions of market performance may trigger securities law or consumer protection law concerns. Avoid specific performance claims." |
| User requests emails for a team (multiple sender names) | "Produce the sequence with [AGENT NAME] placeholder — swap in each team member's name and contact info when deploying to their respective segments." |
| Open rates fall below 15% after deployment | "⚠️ Below-15% open rates typically indicate: poor subject lines, sender reputation issues (high bounce rate, spam complaints), or audience-content mismatch. Review each factor before rewriting." |
| Session approaching context limit | Write `_PROGRESS_CHECKPOINT.md` with completed emails and remaining sequence |

---

## 📖 DOMAIN GLOSSARY

| Term | Definition |
|------|-----------|
| Drip Campaign | A series of pre-written emails sent automatically at scheduled intervals to a defined audience segment |
| Behavioral Trigger | An automated action (sending the next email, alerting an agent) that fires when a contact takes a specific action (opens, clicks, replies, books appointment) |
| CAN-SPAM | The federal law governing commercial email — requires honest sender identification, no deceptive subject lines, a clear opt-out mechanism, and your physical business address |
| Deliverability | The likelihood that an email reaches the recipient's inbox rather than spam folder — affected by sender reputation, content, and list hygiene |
| Open Rate | The percentage of recipients who open a given email — industry benchmark for real estate: 20–35% |
| Click-Through Rate (CTR) | The percentage of email recipients who click a link in the email — benchmark: 2–5% |
| Action Plan | In CRM platforms like Follow Up Boss, a predefined sequence of tasks and communications assigned to a contact |
| Smart Drip | An automated drip campaign that pauses or branches based on contact behavior (replies, opens, link clicks) |
| Sphere of Influence | An agent's personal and professional network — typically the highest-converting segment for email campaigns because of pre-existing trust |

---

*Authored by Evy Evans | Real Estate Agentic Automation*  
*Maintained as part of RealtySkills by Evy Evans. Example dates and figures are illustrative.*
