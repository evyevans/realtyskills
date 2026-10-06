# Source playbook

This playbook supplies task procedures and examples. Follow the working rules in the skill entry, verify current jurisdiction-specific claims, and treat examples as illustrative.

# Property Management Work Order & Maintenance Tracker

This skill converts a raw tenant maintenance request — a text message, email, voicemail transcript, or verbal description — into a fully formatted work order with priority classification, vendor assignment recommendation, estimated cost range, tenant communication, and a landlord/owner notification. It also tracks open work orders across a portfolio when provided with a work order list.

## 🧠 SKILL IDENTITY

**WHO this skill is for:**
A property management company handling maintenance requests across 20–200+ units, or a real estate investor self-managing a small portfolio who receives maintenance requests via text, email, or tenant portal and needs to triage, dispatch, and track them without a dedicated maintenance coordinator.

**WHAT this skill does:**
Produces five outputs from a single maintenance request:
1. **Formatted Work Order** with property address, unit, tenant contact, issue description, priority level, assigned vendor category, and estimated cost range
2. **Vendor Dispatch Instructions** — what type of contractor to call, what to tell them, what to authorize immediately vs. what requires owner approval
3. **Tenant Acknowledgment Communication** — a text or email confirming receipt and providing expected response timeline
4. **Owner/Investor Notification** — formatted update for the property owner if the estimated cost exceeds the pre-authorized repair limit
5. **Open Work Order Status Log** — if multiple requests are provided, a consolidated status dashboard

**WHERE to use this skill:**
Attach to a Claude.ai chat session or load into a Claude.ai Project used by the property management team. Paste or type the tenant maintenance request. Claude processes it and delivers all five outputs immediately.

**WHEN to activate this skill:**
Activate the moment a maintenance request is received — whether by text, email, tenant portal message, or phone call transcript. Process every request through this skill before dispatching any vendor.

**WHY this skill matters:**
This workflow makes the required inputs and output structure explicit. Its numerical benchmarks are configurable assumptions, not validated performance claims.

**HOW this skill works (Overview):**
Claude reads the maintenance request, classifies it by urgency and trade type, generates the work order with all required fields, recommends the vendor category and cost range based on the repair type, drafts all three communications (tenant ACK, vendor instructions, owner notification if applicable), and formats the outputs for immediate use.

---

## 📥 REQUIRED INPUTS

| Input | Format | Source | Required? | Example |
|-------|--------|--------|-----------|---------|
| Maintenance request text | Plain text (as received) | User provides | Yes | "The kitchen faucet has been dripping for a week and the water heater makes a banging noise" |
| Property address | Full address | User provides | Yes | 4821 Maple Ave, Unit 2B, Columbus OH |
| Tenant name | First and last | User provides | Yes | Sarah Johnson |
| Tenant phone / email | Contact info | User provides | No | (614) 555-0199 / sarah@example.com |
| Date/time of request | Timestamp | User provides | No | 05/10/2026 2:14 PM |
| Owner-authorized repair limit | Dollar amount | User provides | No | $500 (default if not provided) |
| Owner name and contact | Name + phone/email | User provides | No | Marcus — (614) 555-0142 |

---

## ⚙️ EXECUTION SOP

### Step 1: Parse and Classify the Maintenance Request

**What Claude does:**
Read the tenant's maintenance request and identify every distinct issue described. For each issue, assign:

**Priority Level:**
- **EMERGENCY (Respond within 2 hours):** No heat in winter (below 55°F), no running water, gas leak suspected, sewage backup, flooding/active water intrusion, electrical hazard (sparks, burning smell), fire damage, security issue (broken lock, door won't close)
- **URGENT (Respond within 24 hours):** No hot water, refrigerator not working, HVAC failure (not emergency temperature), major appliance failure, roof leak (active)
- **ROUTINE (Respond within 3–5 business days):** Dripping faucet, running toilet, minor appliance issue, interior door/window issues, pest sighting (first report), non-critical electrical (outlet not working)
- **SCHEDULED (Next available):** Cosmetic issues, minor caulking, light bulb replacement, seasonal maintenance items

**Trade Type:**
Plumbing / HVAC / Electrical / Appliance / Roofing / Pest Control / Locksmith / General Handyman / Structural

**Tools / Resources needed:**
None — classification from request text.

**Data source:**
User-provided maintenance request.

**Output of this step:**
Issue list with priority level and trade type for each identified issue.

**Cowork behavior:**
PROCEED WITH ANALYSIS AND DRAFTING.

**If this step fails or required data is missing:**
If the request is vague (e.g., "something is wrong with the water"), classify as URGENT (water issues default high) and ask: "Can you or the tenant describe what specifically is happening with the water?"

> 💡 **Precision Note:** A water heater "banging noise" (kettling) combined with any mention of age (10+ years) or rust-colored water should be classified URGENT — not routine — because a failing water heater is both a safety and habitability issue. Never classify water heater issues as Scheduled.

---

### Step 2: Generate the Formatted Work Order

**What Claude does:**
Produce a complete work order document with the following fields:

```
WORK ORDER #[WO-DATE-UNIT]
─────────────────────────────────────────────────────
Property:      [Address] | Unit: [Unit#]
Date Created:  [Today's date]
Priority:      [EMERGENCY / URGENT / ROUTINE / SCHEDULED]
Status:        OPEN

TENANT
Name:          [Tenant Name]
Phone:         [Tenant Phone]
Email:         [Tenant Email]
Request Date:  [Date/time of original request]

ISSUE DESCRIPTION (as reported)
[Verbatim or close paraphrase of tenant's request]

WORK REQUIRED
Issue 1:  [Issue description] | Trade: [Trade] | Priority: [Level]
Issue 2:  [Issue description] | Trade: [Trade] | Priority: [Level]

ESTIMATED COST RANGE
Issue 1:  $[Low] – $[High]  (based on [market/trade benchmarks])
Issue 2:  $[Low] – $[High]
TOTAL EST: $[Combined range]

VENDOR ASSIGNMENT
[Vendor type] — [Specific dispatch instructions]
Owner Authorization Required: YES / NO (based on repair limit)

NOTES / ACCESS INSTRUCTIONS
[Any special access notes, pet on premises, key location, etc.]

AUTHORIZED BY: [PM Name]            DATE: [Today]
VENDOR SIGNATURE: _______________   DATE: ________
COMPLETION DATE: _______________
```

**Tools / Resources needed:**
None — generated from user inputs and Step 1 classification.

**Data source:**
All user-provided inputs + Step 1 classification.

**Output of this step:**
Complete formatted work order.

**Cowork behavior:**
PROCEED WITH ANALYSIS AND DRAFTING.

**If this step fails or required data is missing:**
Generate the work order with [MISSING: field name] markers for any absent required field rather than fabricating information.

---

### Step 3: Generate Vendor Dispatch Instructions

**What Claude does:**
For each issue, provide specific vendor dispatch instructions:

**PLUMBING:**
- Dripping faucet: Licensed plumber or handyman — typically $75–$200 parts and labor. Authorize up to $200 without owner approval.
- Water heater banging/failure: Licensed plumber only — diagnose first ($85–$120 diagnostic), repair ($200–$500) or replace ($800–$2,500). Owner approval required before replacement.
- Active water leak: Licensed plumber EMERGENCY call — authorize up to $500 to stop the leak; notify owner immediately.

**HVAC:**
- No heat/AC: Licensed HVAC technician — diagnostic $95–$150; repair varies widely ($150–$2,000+). Owner approval before any repair over limit.
- Routine maintenance: Schedule HVAC tune-up ($80–$150) during next available appointment.

**ELECTRICAL:**
- Non-working outlet: Electrician or qualified handyman — typically $100–$250. Check breaker first.
- Burning smell/sparks: EMERGENCY — licensed electrician only, same day. Owner notified immediately.

Include the specific message to send/say to the vendor when dispatching.

**Tools / Resources needed:**
None — embedded trade cost benchmarks.

**Data source:**
Step 1 and 2 outputs + embedded cost benchmarks.

**Output of this step:**
Vendor dispatch instructions with specific authorization levels and communication scripts.

**Cowork behavior:**
PROCEED WITH ANALYSIS AND DRAFTING for ROUTINE and SCHEDULED items. CONFIRM BEFORE PROCEEDING for EMERGENCY items (to ensure owner is notified before dispatch of high-cost vendors).

---

### Step 4: Draft Tenant Acknowledgment Communication

**What Claude does:**
Draft a text message AND an email to the tenant confirming receipt of the maintenance request, the priority level, and the expected response timeline.

**Text (under 160 characters):**
"Hi Sarah — Maple PM here. We got your maintenance request for [issue]. Priority: [level]. Expect [vendor/tech] contact within [timeframe]. Thanks!"

**Email:**
Subject: Maintenance Request Received — [Address] Unit [X]

Dear Sarah,

Thank you for submitting your maintenance request. Here's what to expect:

Issue(s) Reported: [List]
Priority Level: [Level]
Expected Response: [Timeline based on priority]

[For EMERGENCY: Our emergency maintenance contractor will contact you within 2 hours.]
[For URGENT: A technician will contact you within 24 hours to schedule access.]
[For ROUTINE: We'll schedule a repair visit within 3–5 business days.]

Please ensure the unit is accessible during business hours. If you have a pet, please secure it before the technician arrives.

Questions? Contact: [PM Name] | [Phone]

[Property Management Company Name]

**Tools / Resources needed:**
None.

**Data source:**
Tenant contact info + Step 1 classification + Step 3 dispatch timeline.

**Output of this step:**
Ready-to-send tenant text and email.

**Cowork behavior:**
CONFIRM BEFORE PROCEEDING — present both communications and ask: "Shall I finalize these for sending, or would you like to make any changes first?"

**If this step fails or required data is missing:**
If tenant contact is not provided, generate the templates with [TENANT NAME] and [CONTACT] placeholders.

---

### Step 5: Generate Owner Notification (if cost exceeds authorization limit)

**What Claude does:**
If the estimated repair cost exceeds the owner's pre-authorized repair limit (default: $500), generate an owner notification:

Subject: Maintenance Required — [Address] — Owner Approval Needed

[Owner Name],

A maintenance request has been received at your property [Address] that requires your approval before work can proceed.

Property: [Address] | Unit: [Unit]
Tenant: [Tenant Name]
Issue(s): [List]
Estimated Cost: $[Low] – $[High]
Priority: [Level]

RECOMMENDED ACTION: [Dispatch licensed plumber / HVAC / etc.] to diagnose and repair. Estimated timeline for completion: [X] days.

Please respond with approval to proceed or alternate instructions. If this is an emergency and you don't respond within [2 hours / 24 hours], we will proceed with dispatch to protect habitability and your legal obligations as a landlord.

[PM Name] | [PM Contact]

**Tools / Resources needed:**
None.

**Data source:**
Step 3 cost estimate + owner contact from user inputs.

**Output of this step:**
Owner notification email (or "Owner notification not required — within authorization limit").

**Cowork behavior:**
PROCEED WITH ANALYSIS AND DRAFTING for notification drafting; CONFIRM BEFORE PROCEEDING if actually sending via integrated tools.

**If this step fails or required data is missing:**
If owner limit is unknown, default to $500 and flag: "Assumed $500 owner authorization limit — confirm with your management agreement."

---

## 📤 OUTPUT FORMAT

**Output type:** Work Order Package (5 outputs)  
**Delivery method:** Returned directly in chat — ready to use

---

```
WORK ORDER #WO-20260510-2B — Evykynn
─────────────────────────────────────────────────────
Property: 4821 Maple Ave, Unit 2B, Columbus OH 43215
Date:     05/10/2026 | Priority: URGENT | Status: OPEN

TENANT: Sarah Johnson | (614) 555-0199 | sarah@example.com
Request Received: 05/10/2026 2:14 PM

ISSUES REPORTED:
1. Kitchen faucet dripping — ROUTINE | Plumbing | Est. $75–$200
2. Water heater banging noise — URGENT | Plumbing | Est. $150–$2,500

TOTAL ESTIMATED COST: $225 – $2,700
⚠️ Owner approval required if water heater replacement needed

VENDOR DISPATCH:
Licensed plumber for both issues.
Script: "I need a plumber at 4821 Maple Ave, Unit 2B, Columbus.
Tenant reports a dripping kitchen faucet AND a banging water
heater. The water heater issue is urgent — please inspect same
day or within 24 hours. Authorized up to $500 before I need
owner approval. Call me back with diagnosis."

TENANT TEXT (sent):
"Hi Sarah — Maple PM here. Got your maintenance request — dripping
faucet and water heater noise. Plumber will contact you within
24hrs. Secure pets before visit. Questions: (614) 555-0142"

OWNER NOTIFICATION (if water heater replacement needed):
[See full email in output — approval required above $500]

⬜ Vendor contacted: _________ Date: _______
⬜ Appointment scheduled: _____ Date/Time: _______
⬜ Work completed: ____________ Date: _______
⬜ Tenant confirmed satisfaction: _____ Date: _______
⬜ Invoice received: $_______ Date: _______
⬜ Work order CLOSED
```

---

## 🔐 PERMISSIONS & SETUP CHECKLIST

No external permissions required for work order generation.

- [ ] **Optional — Buildium / AppFolio:** Export the work order format into your PM software's work order module.
- [ ] **Optional — Twilio:** For automated tenant text acknowledgments, configure Twilio with your property management phone number.
- [ ] **Vendor List:** Maintain a vendor contact list (plumber, HVAC, electrician, handyman, pest control) for each market. Update this skill's dispatch steps with your preferred vendors for faster dispatch.

---

## ✅ QUALITY SELF-CHECK

Before delivering any output, Claude must internally verify every item below:

- [ ] Every issue in the tenant's request is identified — nothing overlooked
- [ ] Priority level is assigned correctly — water heater and heat issues never classified below URGENT
- [ ] Estimated cost range is provided for each issue
- [ ] Owner authorization threshold is applied correctly
- [ ] Tenant acknowledgment communication is drafted and ready to send
- [ ] Owner notification is generated if cost estimate exceeds authorization limit
- [ ] Work order has all required fields — no blank fields except vendor signature/completion
- [ ] Output is immediately usable without additional editing

---

## ⚠️ EDGE CASES & ESCALATION RULES

| Scenario | Claude's Exact Response |
|----------|------------------------|
| Tenant reports gas smell | Classify EMERGENCY: "⚠️ DO NOT SEND A TECHNICIAN — Call 911 and the gas company immediately. Instruct tenant to leave the building NOW. Do not re-enter until cleared by utility company." |
| No heat in winter below 55°F | Classify EMERGENCY: "⚠️ HABITABILITY VIOLATION: No heat below 55°F is an emergency in most states. Dispatch licensed HVAC immediately. If repair will take >24 hours, provide temporary heat source or alternative accommodation." |
| Suspected mold (tenant reports) | Classify URGENT: "⚠️ LEGAL FLAG: Mold complaints require prompt written response and professional inspection. Do not dismiss. Document all actions. Consult an attorney if mold is confirmed." |
| Tenant requests repair landlord believes is tenant damage | "Do not accuse tenant in written communications. Send the repair technician to assess. Document findings in the work order. If damage is confirmed as tenant-caused, address in security deposit reconciliation." |
| Owner refuses repair on habitability issue | "⚠️ LEGAL FLAG: Refusing to make habitability repairs can constitute constructive eviction and expose the owner to tenant legal action, housing authority complaints, and rent withholding. Consult a real estate attorney immediately." |
| Session approaching context limit | Write `_PROGRESS_CHECKPOINT.md` noting which work orders have been processed and which remain |

---

## 📖 DOMAIN GLOSSARY

| Term | Definition |
|------|-----------|
| Habitability | The legal standard requiring rental property to be maintained in a safe and livable condition — includes heat, hot water, working plumbing, structural integrity, and pest-free conditions |
| Work Order | A formal document authorizing and tracking a specific maintenance task at a rental property |
| Owner Authorization Limit | The dollar threshold above which a property manager must obtain the property owner's approval before contracting for repairs |
| Constructive Eviction | A landlord's failure to maintain habitable conditions that forces a tenant to vacate — treated as an illegal eviction in most states |
| Kettling | A banging or rumbling noise from a water heater caused by mineral buildup on the heating element — typically indicates the unit needs flushing or replacement |
| Emergency Maintenance | Repairs that must be addressed immediately (within 2 hours) to prevent harm to persons, property, or habitability |

---

*Authored by Evykynn | Real Estate Agentic Automation*

*Maintained as part of RealtySkills by Evykynn. Example dates and figures are illustrative.*
