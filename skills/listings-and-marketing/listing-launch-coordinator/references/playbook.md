# Source playbook

This playbook supplies task procedures and examples. Follow the working rules in the skill entry, verify current jurisdiction-specific claims, and treat examples as illustrative.

# Listing Launch Coordinator

This skill builds a complete, sequenced listing launch plan — from the moment the listing agreement is signed to the day the property goes live on MLS and active marketing begins. It produces a day-by-day pre-launch checklist, a photography and showing preparation protocol, a marketing asset deployment schedule, an open house plan, and a price reduction trigger matrix — everything needed to execute a professional, high-impact listing launch without dropping a single task.

## 🧠 SKILL IDENTITY

**WHO this skill is for:**
A high-volume independent agent or team listing coordinator managing multiple simultaneous active listings who needs a standardized, systematic launch process that doesn't depend on memory. Specifically: the agent who has just signed a listing agreement and needs to know exactly what happens in the next 7–14 days to get the property on the market at maximum impact.

**WHAT this skill does:**
Produces a complete Listing Launch Plan containing: (1) 14-day pre-launch timeline with day-by-day tasks; (2) Property preparation and staging checklist; (3) Photography brief for the photographer; (4) MLS input checklist — every field that needs to be completed before going live; (5) Marketing asset deployment schedule (social, email, sphere outreach, just-listed cards); (6) Open house logistics plan; (7) First-30-days price performance monitoring with a price reduction trigger matrix.

**WHERE to use this skill:**
Attach to a Claude.ai chat session and provide the property details below. Works equally well loaded into a Claude.ai Project so your entire listing team uses the same standardized launch protocol.

**WHEN to activate this skill:**
Activate the same day a listing agreement is signed — before any vendor is contacted. The launch plan is the first product of the listing relationship.

**WHY this skill matters:**
This workflow makes the required inputs and output structure explicit. Its numerical benchmarks are configurable assumptions, not validated performance claims.

**HOW this skill works (Overview):**
Claude builds the launch plan from the listing details provided, applying standard best practices for high-impact residential listing launches. It calculates backward from the target MLS go-live date to establish each pre-launch task's deadline, assigns responsible parties, and delivers a complete plan the agent or TC can execute immediately.

---

## 📥 REQUIRED INPUTS

| Input | Format | Source | Required? | Example |
|-------|--------|--------|-----------|---------|
| Property address | Full address | User provides | Yes | 4821 Maple Ave, Columbus OH |
| List price | Dollar amount | User provides | Yes | $285,000 |
| Target MLS go-live date | MM/DD/YYYY | User provides | Yes | 05/24/2026 |
| Listing signed date | MM/DD/YYYY | User provides | Yes | 05/10/2026 |
| Property type | SFR / Condo / Multi / Townhome | User provides | Yes | Single-family residential |
| Property condition | Move-in ready / Needs work / Staged | User provides | Yes | Move-in ready, light staging needed |
| Bedrooms / Bathrooms / Sq Ft | Numbers | User provides | No | 3 bed / 2 bath / 1,850 sqft |
| Seller's timeline | When they need to close | User provides | No | Flexible, prefers 60 days |
| Agent name and contact | Name + phone + email | User provides | No | Marcus Johnson | (614) 555-0142 |
| Open house preference | Yes/No, preferred weekend | User provides | No | Yes, first weekend after live |
| Key selling features | Plain text | User provides | No | Updated kitchen, large backyard, top-rated school district |

---

## ⚙️ EXECUTION SOP

### Step 1: Build the Pre-Launch Timeline (Working Backward from Go-Live)

**What Claude does:**
Calculate the pre-launch task schedule by working backward from the target MLS go-live date. The standard pre-launch window is 10–14 days. Assign each task to a specific day:

**Days −14 to −10 (Week 1 after listing agreement):**
- Day 0 (listing signed): Set up transaction file; input listing into MLS as "Coming Soon" (if broker policy allows)
- Day 1: Call photographer to schedule; order yard sign installation; send seller pre-photography prep checklist
- Day 2: Confirm photography date; order any needed marketing materials (door hangers, just-listed cards)
- Day 3–5: Seller prepares property per prep checklist (declutter, deep clean, minor repairs)

**Days −7 to −5 (Week 2):**
- Day 7: Photography conducted (minimum 7 days before go-live to allow editing time)
- Day 8: Review photos — request retakes for any substandard shots
- Day 9: Receive edited photos; begin writing MLS description
- Day 10: Complete MLS input form; schedule lockbox and showing instructions setup

**Days −3 to −1 (Final Pre-Launch):**
- Day 11: Upload photos to MLS; review all MLS data fields for accuracy
- Day 12: Send pre-launch "Coming Soon" email to buyer agent network
- Day 13: Post "Coming Soon" to social media; notify sphere of influence via text blast
- Day 14 (Go-Live): MLS status changes to ACTIVE; listing goes live on Zillow, Realtor.com, Redfin; publish social posts; send just-listed email to database

**Tools / Resources needed:**
None — timeline calculated from user-provided dates.

**Data source:**
User-provided listing and go-live dates.

**Output of this step:**
Day-by-day pre-launch task calendar with exact dates and responsible parties.

**Cowork behavior:**
PROCEED WITH ANALYSIS AND DRAFTING.

**If this step fails or required data is missing:**
If go-live date is fewer than 7 days from signing, flag: "⚠️ Less than 7 days pre-launch window is insufficient for professional photography, MLS preparation, and pre-marketing. Recommend adjusting go-live date to [date + 14 days] for maximum impact."

---

### Step 2: Property Preparation and Staging Checklist

**What Claude does:**
Generate a property preparation checklist tailored to the stated property condition. Deliver this as a printable document the agent can hand directly to the seller.

**Standard prep checklist (adjust for condition):**
**Curb Appeal:**
- [ ] Mow lawn, edge sidewalks, trim hedges
- [ ] Clean or replace front door hardware
- [ ] Power wash driveway, walkways, siding
- [ ] Add fresh mulch to flower beds
- [ ] Remove all vehicles from driveway for photography

**Interior — Declutter:**
- [ ] Remove personal photos and family-specific decor
- [ ] Clear all countertops (kitchen and bathrooms)
- [ ] Remove excess furniture — at most 2 pieces per seating area
- [ ] Empty closets to 50% capacity — buyers look inside
- [ ] Remove all items from refrigerator door

**Deep Clean:**
- [ ] Professional cleaning service (recommend for occupied homes)
- [ ] Steam clean carpets
- [ ] Clean all windows inside and out
- [ ] Detail grout lines in kitchen and bathrooms

**Repairs Before Photography:**
- [ ] Replace all burned-out bulbs with matching color temperature (2700K–3000K warm white)
- [ ] Repair and repaint any visible holes, scuffs, or water stains
- [ ] Ensure all doors and windows open and close smoothly
- [ ] Fix any dripping faucets or running toilets

**Photography Day Protocol:**
- [ ] All lights ON throughout the house
- [ ] All window treatments OPEN to maximize natural light
- [ ] All toilet lids DOWN
- [ ] All pets and pet items removed
- [ ] Fresh towels displayed in bathrooms
- [ ] Fruit bowl or flowers on kitchen counter
- [ ] All trash cans out of sight

**Tools / Resources needed:**
None — generated from property condition input.

**Data source:**
User-provided property condition + standard staging knowledge.

**Output of this step:**
Printable property preparation checklist formatted for seller delivery.

**Cowork behavior:**
PROCEED WITH ANALYSIS AND DRAFTING.

**If this step fails or required data is missing:**
Generate the full standard checklist and note which sections should be adjusted based on property type (condo: no lawn care; multi-family: unit-specific prep for each occupied unit).

---

### Step 3: Photography Brief

**What Claude does:**
Produce a photography brief the agent sends to the photographer before the shoot. The brief specifies: the exact shots required by room, any architectural features to highlight, the listing's top 3 selling features to capture prominently, and any areas to minimize in the shoot (if applicable).

**Standard shot list:**
- Exterior: Front elevation (hero shot), backyard/outdoor space, garage, street view
- Interior: Every room (wide angle), kitchen (2–3 shots: full view + detail of finishes), primary suite (2 shots), primary bathroom, living/family room (2 shots), any special features (fireplace, built-ins, view)
- Additional: Drone/aerial shot (if lot size or location warrants), twilight exterior (optional premium)
- Minimum: 30 photos for a home under 2,000 sqft; 40+ for over 2,000 sqft

**Tools / Resources needed:**
None.

**Data source:**
User-provided key selling features + standard photography best practices.

**Output of this step:**
Photography brief with shot list and seller feature highlights.

**Cowork behavior:**
PROCEED WITH ANALYSIS AND DRAFTING.

**If this step fails or required data is missing:**
Generate standard brief and note: "Add any specific features or areas of concern when sending to your photographer."

---

### Step 4: Marketing Asset Deployment Schedule

**What Claude does:**
Build the marketing deployment schedule — what gets published, where, and when — starting from go-live day through Day 30.

**Pre-Launch (Days −3 to 0):**
- Coming Soon posts: Instagram, Facebook, Nextdoor
- Email to buyer agent network: "New listing hitting MLS [date] — your buyers will want to know"
- SMS/text to sphere: "New listing alert — 3/2 in [neighborhood] hitting market [date]. Know anyone?"

**Go-Live Day:**
- MLS goes ACTIVE
- Social media: Full photo carousel post (Instagram/Facebook) with key stats and price
- Email blast to database: Just-Listed announcement with photos, key features, and showing link
- Paid social: Launch Facebook/Instagram ads targeting buyers in the city + surrounding areas
- Google Business: Post new listing
- Nextdoor: Post in the neighborhood

**Week 1 (Days 1–7):**
- Day 3: Story highlights on Instagram — behind-the-scenes prep video or feature walkthrough
- Day 5: "Still available" market update if no offers received
- Day 7: First open house (if applicable)

**Week 2–4 (Days 8–30):**
- Second open house (if first didn't produce offers)
- Showing feedback collection and summary to seller
- Market update email to database
- Price adjustment evaluation at Day 14 (see Step 5)

**Tools / Resources needed:**
Canva or Adobe Express for social graphics. Facebook Ads Manager for paid social. Gmail/Mailchimp for email blasts.

**Data source:**
User-provided property details and go-live date.

**Output of this step:**
Marketing deployment calendar with channel, content type, and scheduled date for each touchpoint.

**Cowork behavior:**
PROCEED WITH ANALYSIS AND DRAFTING.

**If this step fails or required data is missing:**
Generate the full schedule and note where specific tools are recommended for execution.

---

### Step 5: Price Performance Monitor and Reduction Trigger Matrix

**What Claude does:**
Produce a price monitoring schedule and a price reduction trigger matrix — the specific benchmarks that signal when a price reduction discussion should be initiated with the seller.

**Week-by-Week Performance Benchmarks:**
- **Days 1–7:** Expect 60%+ of total showings. Minimum benchmark: 5 showings in first 7 days for this price range and market type. Fewer than 3 = price may be too high.
- **Days 8–14:** If no offers and fewer than 8 total showings, initiate price discussion. Average DOM in [market] is [X] days.
- **Days 15–21:** Second price evaluation. If showings dropped below 2/week, price reduction is indicated.
- **Days 22–30:** If still no offers, conduct competitive market review — has anything sold in the past 30 days that changes the comp set?

**Price Reduction Trigger Matrix:**
| Signal | Threshold | Recommended Action |
|--------|-----------|-------------------|
| Showings | <5 in first 7 days | Schedule seller call; review price |
| Online views | <500 on Zillow in first 3 days | Review photos and description first |
| Showing-to-offer ratio | 10 showings, 0 offers | Price is above market — reduce |
| DOM vs. market average | 1.5× average DOM, no offers | Reduce by 3–5% |
| Feedback pattern | "Priced too high" from 3+ agents | Reduce to next pricing tier |

**Tools / Resources needed:**
None — metrics monitoring framework for agent use.

**Data source:**
Standard market performance benchmarks + user-provided market type.

**Output of this step:**
Price performance monitoring schedule + reduction trigger matrix.

**Cowork behavior:**
PROCEED WITH ANALYSIS AND DRAFTING.

**If this step fails or required data is missing:**
Use the standard benchmarks and note: "Adjust thresholds based on your specific market's average DOM and typical showing patterns."

---

## 📤 OUTPUT FORMAT

**Output type:** Listing Launch Plan  
**Delivery method:** Returned directly in chat — ready to use immediately

---

```
LISTING LAUNCH PLAN — Evy Evans
Property:      4821 Maple Ave, Columbus OH 43215
List Price:    $285,000
Listing Signed: 05/10/2026 | MLS Go-Live: 05/24/2026
Agent:         Marcus Johnson | (614) 555-0142

PRE-LAUNCH TIMELINE (14-day window)
Date        Task                                  Owner
05/10 (D+0) Sign listing; open file; MLS "Coming Soon"  Agent/TC
05/11 (D+1) Schedule photographer for 05/17             Agent
05/11 (D+1) Order yard sign + lockbox                   TC
05/11 (D+1) Send seller prep checklist                  Agent
05/13 (D+3) Confirm photography appointment             TC
05/15 (D+5) Seller prep complete (deadline)             Seller
05/17 (D+7) PHOTOGRAPHY — 10 AM | Arrive early          Agent
05/18 (D+8) Review photos; approve or request retakes   Agent
05/20 (D+10) Receive edited photos; draft MLS copy      Agent
05/21 (D+11) Complete MLS input; upload photos          TC
05/21 (D+11) Coming Soon email to buyer agent network   Agent
05/22 (D+12) Coming Soon social posts (IG/FB/ND)        Agent
05/23 (D+13) SMS blast to sphere: "Hits MLS tomorrow"  Agent
05/24 (D+14) ⭐ MLS GOES ACTIVE — launch all marketing  Agent/TC

GO-LIVE DAY MARKETING CHECKLIST
☐ MLS status: Coming Soon → Active
☐ Instagram/Facebook full photo post with price + link
☐ Just-Listed email to full database
☐ Paid Facebook/Instagram ad launched
☐ Google Business listing updated
☐ Nextdoor post published
☐ Showing schedule opened in ShowingTime/CSS

OPEN HOUSE PLAN
Date:        05/30/2026 (Sat) | 12:00 PM – 3:00 PM
Prep:        Arrive 45 min early; set up sign riders at 3 intersections
Marketing:   Boost Facebook ad for open house 3 days prior
             Post on Nextdoor same day at 8 AM
             Send reminder email to buyer agent network 05/28
Capture:     Sign-in sheet required; follow up all attendees within 24 hrs

PRICE PERFORMANCE TRIGGERS
  ☐ Day 7 check: Need ≥5 showings. If <3 → call seller TODAY
  ☐ Day 14 check: No offer with 10 showings → price discussion
  ☐ Day 21 check: Still no offer → reduce by 3–5%
  ☐ Day 30 review: Full CMA refresh if no accepted offer
```

---

## 🔐 PERMISSIONS & SETUP CHECKLIST

No external permissions required for plan generation.

- [ ] **MLS Access:** Ensure you have active MLS membership and input access for the listing's MLS board.
- [ ] **ShowingTime / CSS:** Set up showing instructions in your showing management platform before go-live.
- [ ] **Facebook Business Manager:** Have an active ad account ready for paid social launch on go-live day.
- [ ] **Email Platform:** Have database ready in Mailchimp, Constant Contact, or kvCORE for just-listed blast.

---

## ✅ QUALITY SELF-CHECK

Before delivering any output, Claude must internally verify every item below:

- [ ] All pre-launch task dates are calculated from the actual listing signed date and go-live date
- [ ] Photography is scheduled minimum 7 days before go-live to allow editing time
- [ ] Seller prep checklist is complete and formatted for direct delivery to seller
- [ ] Marketing deployment schedule covers pre-launch, go-live, and first 30 days
- [ ] Open house logistics are included if requested
- [ ] Price reduction trigger matrix has specific, measurable thresholds — not vague guidance
- [ ] Output is formatted for immediate use without further editing

---

## ⚠️ EDGE CASES & ESCALATION RULES

| Scenario | Claude's Exact Response |
|----------|------------------------|
| Go-live date is fewer than 7 days from signing | "⚠️ Compressed timeline alert: 7+ days pre-launch is strongly recommended for professional photography and MLS preparation. Suggest adjusting go-live to [date + 10 days]." |
| Property needs significant repairs before listing | Add a repair phase to the timeline: flag "⚠️ Property preparation may extend pre-launch window. Prioritize the top 3 repairs with the highest ROI: paint, flooring, and curb appeal." |
| Seller refuses staging or prep recommendations | "Document the seller's decision in writing. Note that properties with professional photos sell for 3–11% more on average (NAR 2025). If photos are poor, results will reflect that." |
| Competing listing at same price launches same week | Add a competitive response to the marketing plan: increase open house frequency, add twilight photography, add video tour. |
| Legal disclosure issue discovered during prep | ⚠️ LEGAL FLAG: "If a material defect is discovered during property preparation, the seller has a legal disclosure obligation. Consult a real estate attorney before proceeding to list." |
| Session approaching context limit | Write `_PROGRESS_CHECKPOINT.md` noting completed plan sections |

---

## 📖 DOMAIN GLOSSARY

| Term | Definition |
|------|-----------|
| Coming Soon | A pre-market MLS status allowing limited marketing before the listing goes active; rules vary by MLS board |
| DOM | Days on Market — the number of days a listing has been active on MLS; high DOM relative to market average signals pricing or marketing issues |
| ShowingTime / CSS | Centralized Showing Service — the two primary showing management platforms used by agents to schedule and track property showings |
| IDX | Internet Data Exchange — the protocol allowing MLS listings to be displayed on third-party websites (Zillow, Realtor.com, agent websites) |
| Sphere of Influence | A real estate agent's network of personal and professional contacts who may become clients or referral sources |
| Buyer Agent Network | The pool of buyer's agents active in the local market; direct outreach to this network is one of the most effective pre-launch marketing strategies |
| Price Tier | A psychological price bracket in buyer search filters (e.g., $250,000–$300,000); reducing from $305,000 to $299,000 opens a new buyer pool |

---

*Authored by Evy Evans | Real Estate Agentic Automation*  
*Maintained as part of RealtySkills by Evy Evans. Example dates and figures are illustrative.*
