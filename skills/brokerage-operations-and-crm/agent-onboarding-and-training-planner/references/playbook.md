# Source playbook

This playbook supplies task procedures and examples. Follow the working rules in the skill entry, verify current jurisdiction-specific claims, and treat examples as illustrative.

# Agent Onboarding & Training Planner

This skill generates a complete 90-day onboarding and training plan for a newly joined real estate agent — tailored to their experience level (new licensee, experienced transfer, or returning agent) and your brokerage's tools and systems. It produces a week-by-week training schedule, a technology setup checklist, a production ramp milestone tracker, a mentorship pairing protocol, and a 90-day check-in agenda.

## 🧠 SKILL IDENTITY

**WHO this skill is for:**
A brokerage owner or team lead who is onboarding a new agent and needs a systematic, structured plan that moves the agent from first day to first commission check — without spending 20 hours manually creating training materials. Also: a team lead whose onboarding process is "we kind of figure it out" and wants to formalize it into a repeatable system.

**WHAT this skill does:**
Produces a complete 90-Day Agent Onboarding Plan containing: (1) Technology setup checklist — every system the agent must access and configure in week 1; (2) Week-by-week training curriculum for the first 12 weeks; (3) Production ramp milestones — the specific activity and production benchmarks the agent should hit at 30, 60, and 90 days; (4) Mentorship pairing protocol — how to pair the agent with a mentor and what the mentor's responsibilities are; (5) 90-day review agenda — the exact questions to cover in the formal check-in meeting.

**WHERE to use this skill:**
Attach to a Claude.ai chat session and provide the agent's background and your brokerage's core tools. Claude builds the complete onboarding plan in chat — ready to share with the new agent, their mentor, and your TC team.

**WHEN to activate this skill:**
Activate the day an agent signs their independent contractor agreement — before their first day. The plan should be ready before they arrive so day one is productive from the first hour.

**WHY this skill matters:**
This workflow makes the required inputs and output structure explicit. Its numerical benchmarks are configurable assumptions, not validated performance claims.

**HOW this skill works (Overview):**
Claude tailors the onboarding plan to the agent's experience level and the brokerage's stated tools and systems. It applies a proven 90-day ramp framework — technology first, fundamentals second, prospecting third, deal support throughout — and builds each week's training agenda around the activities most likely to produce the agent's first transaction. Production milestones are calibrated to the agent's experience level.

---

## 📥 REQUIRED INPUTS

| Input | Format | Source | Required? | Example |
|-------|--------|--------|-----------|---------|
| Agent name | Full name | User provides | Yes | Sarah Chen |
| Agent experience level | New licensee / Experienced transfer / Returning agent | User provides | Yes | New licensee (license pending) |
| Start date | MM/DD/YYYY | User provides | Yes | 06/01/2026 |
| Brokerage name | Plain text | User provides | Yes | Maple Realty Group |
| Core CRM platform | Platform name | User provides | No | Follow Up Boss |
| MLS board | MLS name | User provides | No | Columbus REALTORS® MLS |
| Transaction management platform | Platform name | User provides | No | DotLoop |
- [ ] Showing platform | Platform name | User provides | No | ShowingTime |
| Mentor agent name (if identified) | Name | User provides | No | Marcus Johnson |
| Agent's stated niche or focus | Plain text | User provides | No | First-time buyers, Columbus East Side |
| Agent's sphere size (estimate) | Number | User provides | No | ~150 contacts |
| Brokerage training resources | List | User provides | No | KW Command training library, weekly team meeting |

---

## ⚙️ EXECUTION SOP

### Step 1: Establish Agent Profile and Calibrate the Plan

**What Claude does:**
Based on the agent's experience level, calibrate the training plan accordingly:

**New Licensee (First-year agent):**
- Emphasis: License law compliance, real estate fundamentals, scripts, showing technique
- Production expectation: 1 closed transaction by Day 90 is aspirational — 1 written contract is the realistic milestone
- Priority: Build habits and systems before income pressure creates shortcuts

**Experienced Transfer Agent:**
- Emphasis: Brokerage systems and tools, team culture integration, existing business migration
- Production expectation: 1–2 closings within 60 days using their existing database
- Priority: Get them productive fast — they have existing skills; they need system familiarity

**Returning Agent (was licensed, took a break):**
- Emphasis: Law updates, market knowledge refresh, technology catch-up
- Production expectation: 1 closing within 75 days
- Priority: Rebuild confidence and re-engage their sphere before prospecting new leads

**Tools / Resources needed:**
None — calibration from user-provided profile.

**Data source:**
User-provided agent details.

**Output of this step:**
Agent profile summary + calibrated training approach statement (used internally to build the plan).

**Cowork behavior:**
PROCEED WITH ANALYSIS AND DRAFTING.

**If this step fails or required data is missing:**
If experience level is not specified, ask: "Is Sarah a brand-new licensee, an experienced agent transferring from another brokerage, or a returning agent re-entering the business?" before proceeding.

---

### Step 2: Technology Setup Checklist (Week 1 Priority)

**What Claude does:**
Generate a complete technology setup checklist — every system the agent must access, configure, and practice before they can work a deal. Organize by day.

**Day 1 (Must complete before anything else):**
- [ ] Email address (brokerage domain if applicable) — set up and test
- [ ] MLS access — apply for membership if new; transfer if experienced
- [ ] E-signature platform (DocuSign / DotLoop / Authentisign) — account creation and tutorial
- [ ] CRM access (Follow Up Boss / kvCORE / etc.) — account creation; import existing contacts
- [ ] Showing management (ShowingTime / CSS) — account setup; practice scheduling a showing
- [ ] Transaction management (DotLoop / Skyslope) — account setup; review a template file
- [ ] Brokerage communication (Slack / Teams) — join all relevant channels
- [ ] Calendar (Google Calendar) — sync with CRM; set up showing notification preferences

**Days 2–5:**
- [ ] MLS login confirmed; run first search; bookmark favorite search parameters
- [ ] CRM — import contact list (CSV from phone contacts if new agent)
- [ ] DocuSign — practice sending and signing a test document
- [ ] Zillow / Realtor.com — claim agent profile if experienced; create profile if new
- [ ] Google Business Profile — create or transfer agent profile
- [ ] Social media — set up professional Instagram, Facebook Business Page, LinkedIn
- [ ] Marketing templates — access brokerage Canva templates or listing marketing tools

**Tools / Resources needed:**
As listed — user provides platform names; Claude builds the setup checklist for each.

**Data source:**
User-provided tool list + standard brokerage technology stack knowledge.

**Output of this step:**
Day-by-day technology setup checklist, Week 1.

**Cowork behavior:**
PROCEED WITH ANALYSIS AND DRAFTING.

**If this step fails or required data is missing:**
Generate the standard technology checklist with placeholders for any tools not specified.

---

### Step 3: Build 12-Week Training Curriculum

**What Claude does:**
Build a week-by-week training schedule for the first 12 weeks, calibrated to the agent's experience level. Each week has: theme, 3–5 specific training activities, a practice assignment, and a production goal.

**Week 1: Orientation & Systems**
- Brokerage tour; meet team; review office policies
- Complete all technology setup (Step 2)
- Review brokerage brand standards and marketing guidelines
- Practice assignment: Write 5 mock property descriptions using the skill library
- Production goal: Zero (setup week)

**Week 2: MLS & Market Knowledge**
- MLS deep-dive: running CMAs, setting up buyer searches, reading days-on-market data
- Study the top 3 zip codes in the agent's target market
- Review the brokerage's 5 most recent closed transactions for pricing patterns
- Practice assignment: Run a CMA on 3 properties without assistance
- Production goal: Add 25 contacts to CRM from sphere

**Week 3: Buyer Consultation & Showings**
- Review buyer consultation script and value proposition
- Practice the buyer presentation (role-play with mentor)
- Learn the showing checklist and note-taking system
- Practice assignment: Conduct 1 mock buyer consultation with mentor
- Production goal: Schedule and conduct 2 actual buyer showings (with mentor if needed)

**Week 4: Prospecting Fundamentals**
- Sphere of influence: Write 150 personal contacts into CRM if not done; draft and send a "I'm in real estate now" announcement
- Lead sources overview: Open houses, Zillow leads, sign calls, referrals, social media
- Database outreach: Send handwritten notes to top 30 sphere contacts
- Practice assignment: Make 10 sphere calls using provided script
- Production goal: Schedule 2 coffee/buyer meetings from sphere outreach

**Week 5–6: Contracts & Paperwork**
- Review state purchase contract from first page to last with mentor or broker
- Practice filling out a complete offer package on a fictional deal
- Review the transaction timeline skill; understand every deadline
- Practice assignment: Submit a mock offer package for broker review
- Production goal: First buyer consultation appointment booked (real prospect)

**Week 7–8: Listings**
- Review the listing presentation; practice with the property description skill
- Shadow a listing appointment with mentor (if possible)
- Learn the pre-listing package preparation and seller prep process
- Practice assignment: Build a mock listing presentation for a practice property
- Production goal: Run a CMA and present it to a sphere contact who owns a home

**Week 9–10: Lead Conversion & Negotiations**
- Review objection handler skill library
- Practice negotiation scenarios with mentor: multiple offers, low appraisal, repair requests
- Review the comparative market analysis skill
- Practice assignment: Handle 5 mock objections in role-play
- Production goal: Make 20 prospecting calls per day (minimum)

**Week 11–12: First Deal Focus**
- Dedicate the majority of time to any active buyer or listing leads
- Weekly pipeline review with mentor or team lead: what's in pipeline, what's blocking progress
- Production goal: First signed buyer agreement OR listing agreement

**Tools / Resources needed:**
None — curriculum generated from profile + brokerage tools.

**Data source:**
Step 1 profile + user-provided brokerage resources.

**Output of this step:**
12-week training curriculum table.

**Cowork behavior:**
PROCEED WITH ANALYSIS AND DRAFTING.

**If this step fails or required data is missing:**
Generate the standard curriculum and note where brokerage-specific training resources should be inserted.

---

### Step 4: Production Ramp Milestones and 90-Day Review Agenda

**What Claude does:**
Define measurable production milestones for 30/60/90 days and the exact 90-day review meeting agenda.

**30-Day Milestones (Activity-Based):**
- 150 contacts in CRM (new agent) / Database fully imported (experienced)
- 10 in-person sphere meetings completed
- 20 prospect calls/day habit established
- Technology fully operational (all systems configured)
- MLS search proficiency demonstrated (CMA without assistance)

**60-Day Milestones (Pipeline-Based):**
- 2 active buyer clients under buyer's agreement
- 1 listing presentation completed (may or may not have converted)
- 50+ prospects in CRM follow-up sequence
- First offer written (even if not accepted)

**90-Day Milestones (Production-Based):**
- New licensee: 1 written contract (signed purchase agreement)
- Experienced transfer: 1 closed transaction OR 1 listing under contract
- Returning agent: 2 active clients in pipeline + 1 pending or closed

**90-Day Review Agenda (30-minute meeting):**
1. Production review: Deals closed? In pipeline? Written but not closed?
2. Activity review: Average daily prospecting calls? Showings conducted? Listing presentations?
3. Technology proficiency: Any system still causing friction?
4. Mentorship feedback: What's been most valuable? What's been missing?
5. Market knowledge: What are the 3 most active price ranges in their target market?
6. Goal setting: What does the next 90 days look like? Revenue goal? Activity commitments?
7. Broker support needed: Commission structure questions, lead source budget, team integration?

**Tools / Resources needed:**
None.

**Data source:**
Step 1 profile.

**Output of this step:**
Milestone table + 90-day review agenda.

**Cowork behavior:**
PROCEED WITH ANALYSIS AND DRAFTING.

**If this step fails or required data is missing:**
Generate the standard milestones with calibration note: "Adjust milestones based on your market conditions and production expectations."

---

## 📤 OUTPUT FORMAT

**Output type:** Agent Onboarding Plan Document  
**Delivery method:** Returned directly in chat — share with new agent, mentor, and management

---

```
90-DAY AGENT ONBOARDING PLAN — Evy Evans
Agent:        Sarah Chen | New Licensee
Brokerage:    Maple Realty Group
Start Date:   06/01/2026
Mentor:       Marcus Johnson
Generated:    05/10/2026 by AI assistant

━━━━━━━━━━━━━━━━ TECHNOLOGY SETUP (WEEK 1) ━━
Day 1:  ☐ Email setup | ☐ MLS application | ☐ Follow Up Boss
        ☐ DotLoop | ☐ ShowingTime | ☐ Slack — #team channel
Days 2-5: ☐ Import contacts to FUB | ☐ DocuSign test send
          ☐ Zillow profile | ☐ Canva brand access
          ☐ Instagram business page

━━━━━━━━━━━━━━━━ 12-WEEK CURRICULUM ━━━━━━━━
Week 1:  Orientation & Systems — zero production, all setup
Week 2:  MLS & Market Knowledge — add 25 sphere contacts
Week 3:  Buyer Consultation & Showings — 2 actual showings
Week 4:  Prospecting Fundamentals — send sphere announcement
Week 5-6: Contracts & Paperwork — mock offer package
Week 7-8: Listing Skills — shadow listing appointment
Week 9-10: Lead Conversion & Negotiations — 20 calls/day
Week 11-12: First Deal Focus — signed agreement goal

━━━━━━━━━━━━━━━━ PRODUCTION MILESTONES ━━━━━
Day 30:  150 contacts in FUB | Tech operational | 10 sphere mtgs
Day 60:  2 buyer agreements | 1 listing pres | 1 offer written
Day 90:  ⭐ 1 signed purchase contract

━━━━━━━━━━━━━━━━ MENTORSHIP PROTOCOL ━━━━━━
Mentor: Marcus Johnson
Weekly: 30-minute check-in (every Monday 9 AM)
Shadow: 2 showings and 1 listing appointment in first 30 days
Support: Available for deal questions via Slack within 4 hours

━━━━━━━━━━━━━━━━ 90-DAY REVIEW AGENDA ━━━━━
Date: 08/31/2026 | Duration: 30 minutes
1. Production review (5 min)
2. Activity review (5 min)
3. Technology friction points (3 min)
4. Mentorship quality check (3 min)
5. Market knowledge assessment (4 min)
6. Next 90-day goals (5 min)
7. Broker support requests (5 min)
```

---

## 🔐 PERMISSIONS & SETUP CHECKLIST

No external permissions required for plan generation.

- [ ] **MLS Application:** File the new agent's MLS membership application on Day 1 — MLS access can take 3–5 business days and is the #1 blocker to productivity.
- [ ] **Technology Access:** Pre-create accounts in Follow Up Boss, DotLoop, and ShowingTime before the agent's first day so they can log in immediately.
- [ ] **Mentor Selection:** Identify a mentor (experienced agent) before the start date. Provide the mentor a copy of this plan and the mentorship protocol section.

---

## ✅ QUALITY SELF-CHECK

Before delivering any output, Claude must internally verify every item below:

- [ ] Plan is calibrated to the correct experience level (new / experienced / returning)
- [ ] Technology setup checklist covers all user-provided tools
- [ ] 12-week curriculum has theme, activities, practice assignment, and production goal for each week
- [ ] Production milestones are specific and measurable — not vague
- [ ] 90-day review agenda has specific questions, not generic topics
- [ ] Plan is immediately shareable with the agent without additional editing
- [ ] Mentor responsibilities are clearly defined

---

## ⚠️ EDGE CASES & ESCALATION RULES

| Scenario | Claude's Exact Response |
|----------|------------------------|
| Agent's license is not yet active at start date | Add to Week 1: "⚠️ License activation is the first priority. Agent cannot show property, write offers, or engage in licensed activities until their license is active with the brokerage. Complete MLS application same day license activates." |
| Agent has no sphere of influence (relocated from another city) | Replace sphere-based activities with geographic farm prospecting: door-knocking, open houses every weekend, Zillow lead acquisition. Adjust production milestones down by 30 days. |
| Agent wants to specialize in investment properties | Incorporate: PropStream training, investor networking events, CCIM or RPAI introductory coursework, and the Evy Evans wholesale deal analyzer and rental underwriting skills. |
| Agent is not meeting 30-day milestones | Flag for broker intervention: "The agent is below production expectations at Day 30. Schedule a 1:1 immediately to identify blockers. Common causes: technology not operational, lack of daily prospecting habit, or unclear value proposition." |
| Agent requests customization not covered in plan | "Add to the plan: [specific request]. Note that any deviation from the standard 12-week curriculum should be discussed with the broker to ensure compliance training is not skipped." |
| Legal or compliance concern | ⚠️ LEGAL FLAG: "New licensees must complete all required state-mandated post-license education within the period specified by their state licensing board. Failure to complete post-license education results in license lapse." |

---

## 📖 DOMAIN GLOSSARY

| Term | Definition |
|------|-----------|
| Independent Contractor Agreement | The contract between a real estate brokerage and an affiliated agent; most agents are independent contractors, not employees |
| Post-License Education | Coursework required by most states after initial licensure — typically 30–45 additional hours in the first license cycle |
| Sphere of Influence | An agent's network of personal and professional contacts who may become clients or referral sources |
| CRM | Customer Relationship Management software — the platform agents use to track leads, contacts, and follow-up activities |
| Geographic Farm | A defined neighborhood or area that an agent systematically markets to in order to build market presence and generate listings |
| MLS | Multiple Listing Service — the cooperative database used by real estate professionals to share property listings |
| Buyer's Agreement | A written contract between a buyer and their agent formalizing the representation relationship; increasingly required by NAR settlement terms (2024+) |
| Transaction Management Platform | Software (DotLoop, SkySlope, Authentisign) used to store, execute, and track transaction documents electronically |

---

*Authored by Evy Evans | Real Estate Agentic Automation*  
*Maintained as part of RealtySkills by Evy Evans. Example dates and figures are illustrative.*
