# Source playbook

This playbook supplies task procedures and examples. Follow the working rules in the skill entry, verify current jurisdiction-specific claims, and treat examples as illustrative.

# Motivated Seller Outreach Script Generator

This skill generates a complete, situation-specific outreach package for motivated seller leads — including a cold call opening script, voicemail drop script, SMS follow-up sequence (Days 1/3/7/14), and a 3-touch email sequence. Every script is calibrated to the seller's specific motivation type (probate, divorce, pre-foreclosure, tired landlord, driving-for-dollars, etc.) and builds empathy before pivoting to acquisition. No generic "I want to buy your house" scripts.

## 🧠 SKILL IDENTITY

**WHO this skill is for:**
A real estate wholesaler, investor, or high-volume acquisition agent who is working a list of off-market motivated seller leads — whether sourced from driving for dollars, PropStream lists, county probate records, pre-foreclosure NOD lists, or cold outreach campaigns — and needs situation-specific scripts that don't sound robotic or predatory.

**WHAT this skill does:**
Produces a complete 5-part outreach package for one motivated seller lead:
1. Cold call opening script (60–90 seconds, with objection handlers for the top 4 objections)
2. Voicemail drop script (25–30 seconds, warm and conversational)
3. SMS sequence: Day 1 initial text, Day 3 follow-up, Day 7 re-engagement, Day 14 final attempt
4. Email sequence: 3 emails over 14 days (introduction, value proposition, last-chance)
5. Appointment confirmation script (for when the seller says yes to a walkthrough)

Every script is calibrated to the seller's motivation type and property situation.

**WHERE to use this skill:**
Attach to a Claude.ai chat session or load into a Claude.ai Project shared with your acquisitions team. Type the trigger phrase and provide the lead details. Output is immediately ready to paste into your CRM, dialer (Mojo, Batch Dialer), or SMS platform (Twilio, Launch Control).

**WHEN to activate this skill:**
Activate the moment a new motivated seller lead enters your pipeline — whether from a list pull, a driving-for-dollars app ping, a county records export, or an inbound inquiry. Best used before the first call or before loading the contact into a drip campaign.

**WHY this skill matters:**
This workflow makes the required inputs and output structure explicit. Its numerical benchmarks are configurable assumptions, not validated performance claims.

**HOW this skill works (Overview):**
Claude first identifies the seller's motivation type from the lead information provided, then selects the appropriate emotional register and script framework for that motivation type. It writes every piece of outreach from the seller's perspective — leading with empathy and a solution frame rather than a lowball offer frame. Every script includes built-in objection handlers and a clear, low-pressure call to action (a 15-minute walkthrough appointment, not a commitment to sell).

---

## 📥 REQUIRED INPUTS

| Input | Format | Source | Required? | Example |
|-------|--------|--------|-----------|---------|
| Seller name | First name preferred | User provides | Yes | Robert |
| Property address | Street address | User provides | Yes | 4821 Maple Ave, Columbus OH |
| Motivation type | See list below | User provides | Yes | Pre-foreclosure — NOD filed 60 days ago |
| How lead was sourced | Plain text | User provides | No | PropStream list, driving for dollars, county records |
| Any known property details | Condition, vacant, tenant-occupied | User provides | No | Vacant, appears neglected, overgrown yard |
| Your name / company name | Plain text | User provides | Yes | Marcus / Maple Capital LLC |
| Your phone number | Phone number | User provides | Yes | (614) 555-0142 |

**Motivation Type Options (choose the closest match):**
- Probate / estate sale (heir inheriting unwanted property)
- Pre-foreclosure / NOD / notice of default
- Divorce / relationship dissolution
- Tired landlord / problem tenant situation
- Fire / flood / storm damage — can't afford repairs
- Job loss / financial distress / behind on taxes
- Absentee owner / out-of-state landlord
- Death of occupant / vacant property
- Relocation / job transfer / needs to sell fast
- Driving for dollars (condition-based, motivation unknown)

---

## ⚙️ EXECUTION SOP

### Step 1: Classify Motivation Type and Set Emotional Register

**What Claude does:**
Based on the motivation type provided, assign a script emotional register from the following framework:

- **Probate/Estate:** Compassionate, unhurried, focused on relieving burden and honoring the family's process. Lead with condolences if recently bereaved. Never pressure.
- **Pre-foreclosure:** Urgent but empathetic. Acknowledge the stress of the situation. Lead with relief — "there are options" — before discussing buying.
- **Divorce:** Neutral, business-like, respectful of complexity. Never reference fault or take sides. Focus on a fast, clean resolution that lets both parties move forward.
- **Tired Landlord:** Peer-to-peer, casual, validate the frustration. Lead with "I understand problem tenants" — position as a fellow investor solving their problem.
- **Damage / Can't Afford Repairs:** Solution-focused, non-judgmental. Lead with "I buy properties as-is" — never reference the condition in a way that sounds like judgment.
- **Financial Distress / Tax Delinquent:** Dignity-preserving. Lead with options (short sale, subject-to, cash offer). Never use language that implies blame.
- **Absentee Owner:** Efficiency-focused. They want a simple, remote close. Lead with "no showings, no repairs, close on your timeline."
- **Driving for Dollars (unknown motivation):** Neutral curiosity — "I noticed your property and wondered if you'd considered an offer." Don't assume distress.

**Tools / Resources needed:**
None — classification from user-provided motivation type.

**Data source:**
User-provided motivation type and lead details.

**Output of this step:**
Confirmed motivation classification + emotional register selection (internal — not shown to user). Proceed directly to script writing.

**Cowork behavior:**
PROCEED WITH ANALYSIS AND DRAFTING — classification is analytical.

**If this step fails or required data is missing:**
If motivation is unknown (driving for dollars / cold list), use the neutral curiosity register and produce adaptable scripts with prompts for the caller to adjust based on what the seller reveals.

---

### Step 2: Write the Cold Call Opening Script

**What Claude does:**
Produce a 60–90 second cold call script with the following structure:

1. **Introduction (10 sec):** Name, company, how you got their info (honest, not mysterious)
2. **Empathy Bridge (15 sec):** Acknowledge their specific situation without being presumptuous
3. **Value Proposition (15 sec):** What you offer (cash offer, fast close, as-is, no fees)
4. **Soft Ask (10 sec):** Request a 15-minute walkthrough — not a commitment to sell
5. **Objection Handlers (30 sec each, 4 handlers):**
   - "I'm not interested"
   - "I already have an agent"
   - "What's your offer?" (premature)
   - "I need to think about it"

Write every line of spoken dialogue — not bullet points describing what to say.

**Tools / Resources needed:**
None — fully generated from Step 1 classification and user inputs.

**Data source:**
Motivation classification from Step 1 + user-provided lead details.

**Output of this step:**
Complete cold call script with dialogue written out in full, with [PAUSE] and [LISTEN] stage directions where appropriate.

**Cowork behavior:**
PROCEED WITH ANALYSIS AND DRAFTING.

**If this step fails or required data is missing:**
If seller name is not known, use "Hi, is this the homeowner at [address]?" as the opener.

> 💡 **Precision Note:** The soft ask must be for a 15-minute walkthrough — not an offer. Asking for a commitment to sell on the first call triggers objections. Asking for a quick visit to "better understand your situation" lowers resistance. The appointment is the conversion goal of the cold call.

---

### Step 3: Write the Voicemail Drop Script

**What Claude does:**
Produce a 25–30 second voicemail script that:
- States the caller's name and company
- References the property address (makes it specific, not spam)
- States a genuine reason for calling related to their motivation type
- Provides callback number twice (clearly)
- Does NOT ask them to "press 1" or sound like a robocall
- Ends with a warm, human close — not a hard sell

**Tools / Resources needed:**
None — generated from Step 1 and user inputs.

**Data source:**
Step 1 classification + user-provided name, company, phone.

**Output of this step:**
Complete voicemail script (25–30 seconds when read aloud at normal pace — Claude will verify approximate word count: 60–75 words).

**Cowork behavior:**
PROCEED WITH ANALYSIS AND DRAFTING.

**If this step fails or required data is missing:**
Produce a generic version that can be quickly adapted if some lead details are missing.

---

### Step 4: Write the SMS Follow-Up Sequence

**What Claude does:**
Produce four SMS messages — one for each follow-up timing — each under 160 characters (single SMS unit) unless a longer message is strategically warranted. Every SMS must feel human-written, not automated.

- **Day 1 SMS:** Sent same day as call attempt. Introduce yourself, reference the property, invite a quick reply. Under 160 characters.
- **Day 3 SMS:** Light follow-up. Reference that you reached out previously. One-sentence value reminder. Ask a yes/no question to trigger engagement.
- **Day 7 SMS:** Re-engagement with a new angle or piece of value (market insight, no-obligation offer mention). Respect their time.
- **Day 14 SMS:** Final contact. Human, not desperate. Leave the door open — "whenever you're ready."

**Tools / Resources needed:**
None — generated from context. Optional: Twilio or Launch Control for deployment.

**Data source:**
Step 1 classification + user inputs.

**Output of this step:**
Four labeled SMS messages with character counts verified.

**Cowork behavior:**
PROCEED WITH ANALYSIS AND DRAFTING.

**If this step fails or required data is missing:**
Produce the sequence and note which messages may need personalization if seller details were incomplete.

> 💡 **Precision Note:** Never use SMS to reference a seller's financial distress explicitly (e.g., "I saw your foreclosure notice"). This can feel predatory and may violate TCPA regulations in some states. Keep SMS language neutral and invitation-based. Save the empathy-specific language for voice calls where you can gauge reaction in real time.

---

### Step 5: Write the 3-Touch Email Sequence

**What Claude does:**
Produce three emails for the following schedule:

- **Email 1 (Day 1 — Introduction):** Subject line + 4–6 sentence body. Introduce yourself, reference the property, explain what you do (buy homes as-is), and invite a no-obligation conversation. Include a clear call to action (reply, call, or click to schedule). Professional but warm.
- **Email 2 (Day 5 — Value Proposition):** Subject line + 5–7 sentence body. Lead with a benefit statement relevant to their motivation type. Mention your buying process (no repairs, no showings, fast close, no agent fees). Include a testimonial-style statement ("Sellers I've worked with often say..."). One clear CTA.
- **Email 3 (Day 14 — Last Chance):** Subject line + 3–4 sentence body. Acknowledge this is your last outreach. Leave the door open without pressure. Provide your contact info for when they're ready.

**Tools / Resources needed:**
None — generated from context. Optional: Gmail API, Mailchimp, or MailerLite for delivery.

**Data source:**
Step 1 classification + user inputs.

**Output of this step:**
Three complete emails with subject lines, bodies, and signature block.

**Cowork behavior:**
PROCEED WITH ANALYSIS AND DRAFTING.

**If this step fails or required data is missing:**
If no email address is available for the seller, note that email sequence is ready for deployment when an email is obtained (via skip tracing: BeenVerified, BatchSkipTracing, PropStream).

---

### Step 6: Write the Appointment Confirmation Script

**What Claude does:**
Produce a 30-second phone script and a confirmation SMS/email for use when the seller agrees to a walkthrough appointment. Include:
- Verbal confirmation of date, time, and address
- What to expect during the visit (15–20 minutes, no pressure, you just want to see the property)
- Reminder that no commitment is required
- Your contact info for questions or rescheduling

**Tools / Resources needed:**
None — generated from context.

**Data source:**
User inputs + motivation classification.

**Output of this step:**
Appointment confirmation phone script + confirmation SMS + confirmation email.

**Cowork behavior:**
PROCEED WITH ANALYSIS AND DRAFTING.

**If this step fails or required data is missing:**
Produce the confirmation templates with [DATE/TIME] placeholder for manual fill if appointment details were not provided.

---

## 📤 OUTPUT FORMAT

**Output type:** Outreach Script Package  
**Delivery method:** Returned directly in chat — ready to paste into CRM, dialer, SMS platform, or email tool

---

```
MOTIVATED SELLER OUTREACH PACKAGE — Evykynn
Seller: Robert | Property: 4821 Maple Ave, Columbus OH
Motivation: Pre-foreclosure (NOD filed 60 days ago)
Your Name/Company: Marcus / Maple Capital LLC
─────────────────────────────────────────────────

PART 1 — COLD CALL SCRIPT
──────────────────────────
"Hi, is this Robert? ... Hi Robert, my name is Marcus, I'm with
Maple Capital here in Columbus. I came across your property on
Maple Avenue and wanted to reach out personally.

[PAUSE — let them confirm]

Robert, I know this might be coming out of the blue, and I'll be
completely upfront with you — I'm a local real estate investor,
and I specialize in working with homeowners who might be dealing
with a stressful situation with their property. I don't know your
full situation, but if you're facing any kind of time pressure or
financial challenge, I might be able to help.

What I do is buy properties directly from homeowners — as-is,
no repairs needed, no agents involved, and I can close on your
timeline. There's no obligation whatsoever.

I'd love to just stop by for 15 minutes to take a look at the
property and hear more about your situation. Would that work
for you sometime this week?

[LISTEN]

OBJECTION: "I'm not interested."
"I completely respect that, Robert. I just want you to know that
if your situation ever changes — and these things can move fast —
you're welcome to reach out to me directly. I'll text you my
number so you have it. Take care."

OBJECTION: "I already have an agent."
"That's great — having someone in your corner is smart. I work
alongside agents sometimes too. My offer is typically a cash
offer that closes faster than most listed sales. Are you under
contract yet, or just listed?"

OBJECTION: "What's your offer?"
"I want to give you a fair number, Robert, and to do that I need
to see the property first — even just briefly. I don't want to
throw out a number that's off base without actually seeing it.
Can we set up just 15 minutes?"

OBJECTION: "I need to think about it."
"Of course — absolutely no pressure. Would it be okay if I
followed up with you in a day or two? And in the meantime, feel
free to text or call me anytime. [Your number]."

─────────────────────────────────────────────────

PART 2 — VOICEMAIL DROP (28 seconds / ~70 words)
──────────────────────────────────────────────────
"Hi Robert, this is Marcus with Maple Capital here in Columbus.
I'm calling about your property on Maple Avenue. I work with
homeowners in situations like yours and I might be able to offer
a solution that works for you. Completely no obligation. Please
give me a call back at 614-555-0142 — that's 614-555-0142.
Hope to talk soon. Thanks, Robert."

─────────────────────────────────────────────────

PART 3 — SMS SEQUENCE
──────────────────────
Day 1 (141 chars):
"Hi Robert, Marcus from Maple Capital here. Left you a VM about
4821 Maple Ave. We buy homes as-is, fast close. Worth a 15-min
chat? — (614) 555-0142"

Day 3 (138 chars):
"Hey Robert — Marcus again re: Maple Ave. Still interested in
making you a fair cash offer. No repairs, no hassle. Still open
to talk? Reply anytime."

Day 7 (155 chars):
"Hi Robert, Marcus with Maple Capital. Columbus market is moving
fast right now. If selling is on your mind for Maple Ave, I can
close in 14 days. No pressure — (614) 555-0142"

Day 14 (132 chars):
"Last note from Marcus at Maple Capital re: Maple Ave. Door's
always open if timing changes. Wishing you well either way.
— (614) 555-0142"

─────────────────────────────────────────────────

PART 4 — EMAIL SEQUENCE
─────────────────────────
Email 1 — Day 1
Subject: Quick question about 4821 Maple Ave, Columbus

Hi Robert,

My name is Marcus — I'm a local real estate investor here in
Columbus with Maple Capital LLC. I came across your property
on Maple Avenue and wanted to reach out directly.

I specialize in buying homes as-is — no repairs, no showings,
no agent fees — and I can often close in 14 days or on whatever
timeline works for you.

I'd love to have a quick, no-obligation conversation. Would you
be open to a brief call or a 15-minute visit to the property?

You can reach me at (614) 555-0142 or just reply here.

Marcus
Maple Capital LLC | Columbus, OH

[Emails 2 and 3 follow same format — Day 5 value, Day 14 close]

─────────────────────────────────────────────────

PART 5 — APPOINTMENT CONFIRMATION
────────────────────────────────────
Call Script (when they say yes):
"Perfect, Robert — I really appreciate it. So we're confirmed
for [DAY], [DATE] at [TIME] at 4821 Maple Ave. I'll just plan
on 15–20 minutes — I'll take a quick look at the property and
we can chat about your situation. No pressure whatsoever,
and no commitment required. If anything comes up, just text
or call me at (614) 555-0142. See you then!"

Confirmation SMS:
"Confirmed! Marcus from Maple Capital — see you [DAY DATE] at
[TIME] at 4821 Maple Ave. My number: (614) 555-0142 if you
need to reach me. Looking forward to it!"
```

---

## 🔐 PERMISSIONS & SETUP CHECKLIST

No external permissions or setup required for script generation. Attach this file to any Claude.ai chat and type the trigger phrase.

- [ ] **TCPA Compliance:** Before deploying SMS or cold calls, ensure your outreach complies with the Telephone Consumer Protection Act. Do not contact numbers on the National Do Not Call Registry without a prior business relationship. ⚠️ Consult a compliance attorney if operating at scale (1,000+ contacts/month).
- [ ] **Optional — Twilio:** For automated SMS deployment, set up a Twilio account and verified sender number. Twilio pricing: approximately $0.0079/SMS.
- [ ] **Optional — CRM Integration:** Paste scripts into Follow Up Boss, Podio, or REISimpli lead notes for quick retrieval by your acquisitions team.
- [ ] **Optional — Dialer:** Load call scripts into Mojo Dialer, Batch Dialer, or CallTools for power dialing campaigns.

---

## ✅ QUALITY SELF-CHECK

Before delivering any output, Claude must internally verify every item below:

- [ ] Motivation type was identified and the correct emotional register was applied — scripts are not generic
- [ ] Cold call script includes all four objection handlers written as full spoken dialogue
- [ ] Voicemail script is 60–75 words (approximately 25–30 seconds at normal speaking pace)
- [ ] All four SMS messages are under 160 characters each (verified)
- [ ] Email sequence has three emails with unique subject lines and differentiated body content
- [ ] Appointment confirmation script includes date/time placeholder, address, and contact info
- [ ] No script uses language that references a seller's financial distress in SMS/email (TCPA risk)
- [ ] Output is immediately usable — scripts are written as dialogue, not instructions

---

## ⚠️ EDGE CASES & ESCALATION RULES

| Scenario | Claude's Exact Response |
|----------|------------------------|
| Seller motivation is unknown (DFD / cold list) | Use neutral curiosity register — never assume distress. Produce adaptable scripts with caller guidance notes. |
| Probate seller is recently bereaved | Open with condolences. Remove any urgency language. Flag: "⚠️ Bereaved sellers require extra sensitivity — do not discuss timelines or offers on first contact." |
| User requests aggressive or high-pressure scripts | Decline and explain: "High-pressure scripts damage seller relationships and can trigger TCPA complaints. I'll write scripts that convert more appointments through empathy." |
| Legal or compliance risk (TCPA, fair housing) | Insert ⚠️ LEGAL FLAG: "Ensure all outreach complies with TCPA and your state's telemarketing laws. Consult a compliance attorney before scaling to 1,000+ contacts." |
| Seller has an active bankruptcy (user mentions it) | Flag: "⚠️ LEGAL FLAG: Contacting a seller in active bankruptcy without trustee permission may violate the automatic stay. Consult a real estate attorney before proceeding." |
| User wants scripts in Spanish or another language | Translate all scripts to the requested language while preserving the emotional register and structure. |

---

## 📖 DOMAIN GLOSSARY

| Term | Definition |
|------|-----------|
| Motivated Seller | A property owner with a compelling reason to sell quickly, often at below-market price — common motivations include financial distress, probate, divorce, relocation, or property damage |
| NOD | Notice of Default — the formal legal filing that initiates the pre-foreclosure process when a homeowner is delinquent on their mortgage |
| Driving for Dollars (DFD) | A lead generation strategy where investors physically drive neighborhoods to identify distressed properties for direct outreach |
| Skip Tracing | The process of locating a property owner's contact information (phone, email) using data aggregation services like BatchSkipTracing or BeenVerified |
| TCPA | Telephone Consumer Protection Act — federal law regulating telemarketing calls and texts; violations can result in $500–$1,500 per call/text in statutory damages |
| As-Is | A purchase condition where the buyer accepts the property in its current state without requiring the seller to make any repairs or improvements |
| Power Dialer | Outbound calling software that automatically dials a list of numbers in sequence, connecting the agent only when a live person answers |
| Probate | The legal process by which a deceased person's estate is administered and distributed to heirs; probate properties are frequently sold by heirs who don't want to manage them |
| Assignment Fee | The profit earned by a wholesaler who transfers a purchase contract to an end buyer without taking title to the property |

---

*Authored by Evykynn | Real Estate Agentic Automation*

*Maintained as part of RealtySkills by Evykynn. Example dates and figures are illustrative.*
