# Source playbook

This playbook supplies task procedures and examples. Follow the working rules in the skill entry, verify current jurisdiction-specific claims, and treat examples as illustrative.

# Objection Handler Coach

Turn the objections that freeze you into the conversations that close deals. This skill provides proven response frameworks for the 25+ most common real estate objections from buyers and sellers, using psychology-based techniques (Feel-Felt-Found, Acknowledge-Pivot-Close, Isolate-and-Solve) with word-for-word scripts you can practice and personalize. Each objection includes the underlying psychology (what the client really means), the response framework, multiple script variations, practice scenarios, and confidence-building techniques. Built for listing agents tired of losing listings to "I want to think about it," and buyer's agents who hear "the price is too high" on every showing.

## 🧠 SKILL IDENTITY

**WHO this skill is for:**
A solo agent prepping for tomorrow's listing appointment with a tough seller; a team lead training new ISAs on objection handling; a wholesaler running cold-call follow-ups and hitting "I'm just going to wait for spring" three times a day; a brokerage owner building a coaching curriculum for the office.

**WHAT this skill does:**
Takes a specific objection (sometimes copy-pasted verbatim from a text or call recording) and returns a structured response package: the underlying psychology behind the objection, three response scripts (empathy-first, data-driven, and assumptive-close), a list of likely follow-up objections the client will throw next, a practice scenario the user can role-play out loud, and a confidence-builder reframe.

**WHERE to use this skill:**
Standalone Claude.ai chat for live just-in-time coaching (in the car between appointments); Claude.ai Project for office-wide use so junior agents share the same scripts; pair with Claude voice mode for live role-play drills.

**WHEN to activate this skill:**
Right before walking into a listing appointment; the moment a buyer's lender pre-approval falls through and the deal needs to be saved; during weekly team-meeting role-play drills; when onboarding a new agent and walking them through the top 25 objections.

**WHY this skill matters:**
This workflow makes the required inputs and output structure explicit. Its numerical benchmarks are configurable assumptions, not validated performance claims.

**HOW this skill works (Overview):**
Claude classifies the objection (price / timing / agent-trust / market / competition), surfaces the emotion behind it, drafts three response variants matched to the client's likely temperament, predicts the next 2 objections the client will raise, and ends with a role-play scenario the user can practice with — including the recommended tone and pacing.

## When to Use

- Preparing for a listing appointment where you expect pricing pushback
- Practicing responses before a difficult buyer consultation
- Coaching a new agent or ISA on objection handling
- In the moment — pulling up a response framework during a live call or meeting
- After losing a listing or buyer — analyzing what went wrong and preparing for next time
- Role-playing with a partner or team member to build muscle memory
- Refreshing your skills quarterly as market conditions change and new objections emerge
- Training your showing assistant on how to handle buyer objections during tours

## 📥 REQUIRED INPUTS

| Parameter | Type | Required | Description |
|---|---|---|---|
| objection_text | string | Yes | The exact objection the client stated (verbatim is ideal) |
| client_type | string | Yes | seller, buyer, fsbo, expired-listing-owner |
| context | string | No | Where the objection came up: listing-appointment, showing, phone-call, open-house, offer-negotiation, social-media |
| client_relationship | string | No | How well you know them: new-lead, warm-lead, existing-client, referral, past-client |
| market_conditions | string | No | Current market context: seller-market, buyer-market, balanced, rising-rates, declining-prices |
| your_commission_rate | string | No | Your standard commission rate (for commission objections) |
| competing_offer | string | No | If another agent is involved, what they are offering (lower commission, different marketing, etc.) |
| emotional_temperature | string | No | How the client seems: calm-rational, frustrated, angry, scared, confused, indifferent |

## ⚙️ EXECUTION SOP

### Step 1: Objection Classification

**What Claude does:** Reads the verbatim objection and assigns it to one of five canonical categories (Stall / Price-Value / Competition / Market Fear / Trust-Authority) so the right response strategy is chosen.
**Tools / Resources needed:** Claude language understanding; the 5-type classification table below.
**Data source:** The user-provided `objection_text` field plus optional `context` and `emotional_temperature`.
**Output of this step:** One line — `Objection Type: [category]` — plus a one-sentence rationale.
**Cowork behavior:** PROCEED WITH ANALYSIS AND DRAFTING
**If this step fails or required data is missing:** If the objection text is ambiguous (could be Stall OR Price), surface both interpretations to the user and ask which best matches the conversation tone before continuing.

Categorize the objection into one of five types, each requiring a different response strategy:

| Objection Type | Description | Response Strategy |
|---|---|---|
| **Stall** | "I need to think about it" / "Not right now" | Create urgency + reduce risk |
| **Price/Value** | "Your commission is too high" / "The price is too high" | Reframe value, not cost |
| **Competition** | "Another agent charges less" / "My friend is an agent" | Differentiate, don't discount |
| **Market Fear** | "I want to wait for prices to drop" / "Rates are too high" | Educate with data |
| **Trust/Authority** | "I can sell it myself" / "I'm not sure you're the right agent" | Demonstrate expertise |

### Step 2: Psychology Diagnosis

**What Claude does:** Translates the surface objection into the underlying emotional or cognitive driver (fear of regret, loyalty conflict, media-fueled market fear, etc.) so the response targets the real concern.
**Tools / Resources needed:** Surface-to-psychology mapping table (below); user-provided `emotional_temperature` if present.
**Data source:** Step 1 classification + objection text + any contextual notes.
**Output of this step:** A 2–3 sentence "what they really mean" diagnosis.
**Cowork behavior:** PROCEED WITH ANALYSIS AND DRAFTING
**If this step fails or required data is missing:** If multiple psychological drivers fit equally, name both and ask the user one clarifying question (e.g., "Did they hesitate before saying it, or say it firmly?").

Identify what the client really means beneath the surface objection:

| Surface Objection | Underlying Psychology | What They Need |
|---|---|---|
| "I need to think about it" | Fear of making a wrong decision | Reassurance + risk reversal |
| "Your commission is too high" | They do not understand your value proposition | Concrete ROI demonstration |
| "Another agent said they would list for less" | Comparison shopping, looking for validation | Differentiation + outcome focus |
| "My friend/family member is an agent" | Loyalty conflict, social obligation | Permission to prioritize their financial outcome |
| "I can sell it myself (FSBO)" | Belief that agents do not earn their fee | Education on net proceeds |
| "I want to wait for prices to drop" | Fear of buying at the peak | Market data + opportunity cost |
| "The market is bad right now" | Media fear, uncertainty | Local data vs. national headlines |
| "I'm not ready yet" | Unresolved concern they have not voiced | Discovery questions to find the real blocker |
| "The house is overpriced" (buyer) | They like the house but need justification | CMA data + negotiation strategy |
| "We just started looking" | Testing agents, gathering information | Provide value without pressure |

### Step 3: Response Framework Selection

**What Claude does:** Picks one of four named response frameworks (Feel-Felt-Found / Acknowledge-Pivot-Close / Isolate-and-Solve / Question Redirect) based on objection type and emotional temperature.
**Tools / Resources needed:** Framework reference cards below.
**Data source:** Step 1 (type) + Step 2 (psychology) + emotional temperature input.
**Output of this step:** Named framework + one-line justification for the choice.
**Cowork behavior:** PROCEED WITH ANALYSIS AND DRAFTING
**If this step fails or required data is missing:** Default to Acknowledge-Pivot-Close (the safest, most flexible framework) and note the default in the output.

Apply the appropriate framework based on objection type and emotional temperature:

**Framework 1: Feel-Felt-Found (Best for emotional objections)**
```
1. FEEL: "I understand how you feel about [specific concern]."
2. FELT: "Many of my clients have felt the same way when [similar situation]."
3. FOUND: "What they found was [positive outcome + specific example]."
```

**Framework 2: Acknowledge-Pivot-Close (Best for logical/price objections)**
```
1. ACKNOWLEDGE: Validate their concern without agreeing with the premise.
2. PIVOT: Redirect to the real issue or a higher-value perspective.
3. CLOSE: Ask a closing question that moves forward.
```

**Framework 3: Isolate-and-Solve (Best for stalls and vague objections)**
```
1. ISOLATE: "Other than [stated concern], is there anything else holding you back?"
2. CONFIRM: "So if we could [solve stated concern], you would be ready to move forward?"
3. SOLVE: Present the specific solution to the isolated concern.
```

**Framework 4: Question Redirect (Best for trust/authority objections)**
```
1. QUESTION: Ask a question that makes them articulate their real concern.
2. LISTEN: Let them talk — often the real objection is 2-3 layers deep.
3. ADDRESS: Respond to what they actually said, not what you assumed.
```

### Step 4: Script Generation

**What Claude does:** Drafts three response scripts at three tones (Gentle / Consultative / Direct) using the selected framework, each one word-for-word and ready to read aloud.
**Tools / Resources needed:** The selected framework template; market data (national NAR or user-supplied local figures) when objection is data-sensitive.
**Data source:** All prior steps + commission rate / market conditions inputs if relevant.
**Output of this step:** Three labeled scripts with explicit tone tags so the agent can pick the one matching the client.
**Cowork behavior:** PROCEED WITH ANALYSIS AND DRAFTING
**If this step fails or required data is missing:** If the agent's commission rate or specific market data is missing for a data-driven script, write the script using `[YOUR RATE]` and `[LOCAL DOM]` placeholders and flag them clearly so the agent fills them in before delivery.

Generate 2-3 response scripts per objection, ranging from gentle to direct, so the agent can choose based on their personality and the client's emotional temperature.

**Script Tones:**
- **Gentle:** Empathetic, no pressure, relationship-focused (best for scared or confused clients)
- **Consultative:** Balanced, data-backed, advisory (best for rational clients)
- **Direct:** Confident, challenge-oriented, outcome-focused (best for indifferent or testing clients)

### Step 5: Practice Scenario Creation

**What Claude does:** Builds a realistic role-play scenario including setup, the objection delivered with emotional cues, an ideal response walkthrough, common mistakes, and a likely follow-up question — so the agent can drill out loud.
**Tools / Resources needed:** Step 1–4 outputs; optional Claude voice mode for live spoken role-play.
**Data source:** All prior steps + agent's stated context (listing appointment, showing, etc.).
**Output of this step:** A scenario block plus a "Confidence Builder" closing paragraph with one specific drill the agent can do this week.
**Cowork behavior:** PROCEED WITH ANALYSIS AND DRAFTING
**If this step fails or required data is missing:** If no context was given, build a generic scenario in the most common context for the objection type (price objections → listing appointment; market-fear objections → buyer consultation).

For each objection, create a realistic practice scenario that includes:
- Setup (who is the client, what is the situation)
- The objection delivered in context (with emotional cues)
- Ideal response walkthrough
- Common mistakes to avoid
- Follow-up question the client is likely to ask after your response

## 📤 OUTPUT FORMAT

```
# Objection Handler: [objection_text]

## Classification

| Category | Value |
|---|---|
| Objection Type | [stall/price-value/competition/market-fear/trust-authority] |
| Underlying Psychology | [what they really mean] |
| Emotional Temperature | [calm/frustrated/angry/scared/confused/indifferent] |
| Best Framework | [Feel-Felt-Found / Acknowledge-Pivot-Close / Isolate-and-Solve / Question Redirect] |

---

## Response Scripts

### Script 1: Gentle Approach

[Complete response script — word for word]

### Script 2: Consultative Approach

[Complete response script — word for word]

### Script 3: Direct Approach

[Complete response script — word for word]

---

## Follow-Up Questions They May Ask

| Question | Recommended Response |
|---|---|
| [likely follow-up 1] | [response] |
| [likely follow-up 2] | [response] |
| [likely follow-up 3] | [response] |

---

## Practice Scenario

**Setup:** [realistic scenario description]

**Client says:** "[objection in context with emotional cues]"

**Your response:** [walk through the ideal response step by step]

**Common mistakes:**
1. [mistake to avoid]
2. [mistake to avoid]
3. [mistake to avoid]

---

## Confidence Builder

[One paragraph of encouragement + one specific technique to practice this week]
```

## Methodology

**SHIELD Response System (Surface-Hidden-Isolate-Educate-Lead-Decide)**

The SHIELD system is built on the principle that every objection has two layers: the surface statement (what they say) and the hidden concern (what they mean). Most agents respond to the surface and miss the hidden layer entirely. SHIELD trains agents to first identify the hidden concern, then isolate it as the only remaining barrier, educate the client with relevant data or social proof, lead them toward a reframed perspective, and guide them to a decision. This six-step process is adapted from enterprise sales methodology (Sandler, Challenger Sale) and calibrated for the emotional, relationship-driven context of residential real estate.

## Advanced Configuration

| Parameter | Default | Range | Description |
|---|---|---|---|
| tone_preference | consultative | gentle/consultative/direct | Default script tone to generate first |
| include_statistics | true | true/false | Include NAR/market statistics in responses |
| include_stories | true | true/false | Include anonymous client success stories in responses |
| practice_scenario_count | 1 | 1-3 | Number of practice scenarios per objection |
| follow_up_questions | 3 | 1-5 | Number of anticipated follow-up questions |
| include_body_language_tips | true | true/false | Include in-person nonverbal communication tips |
| market_data_region | national | national/state/local | Granularity of market statistics used in responses |
| competitor_analysis | false | true/false | Include analysis of what discount agents sacrifice |
| include_role_play_prompts | true | true/false | Generate role-play prompts for team practice |
| objection_chaining | true | true/false | Address likely chain of follow-up objections |

## Example

**Input:**
```
objection_text: "Your commission is too high. Another agent said they would list my house for 1%."
client_type: seller
context: listing-appointment
client_relationship: new-lead
market_conditions: balanced
your_commission_rate: "2.5% listing side"
competing_offer: "Another agent offering 1% listing commission, full service"
emotional_temperature: calm-rational
```

**Output:**
```
# Objection Handler: "Your commission is too high. Another agent said they would list my house for 1%."

## Classification

| Category | Value |
|---|---|
| Objection Type | Competition + Price/Value |
| Underlying Psychology | They do not see a difference between your service and a discount agent's service. They are evaluating ROI, not loyalty. |
| Emotional Temperature | Calm-rational — this is a logical comparison, not an emotional reaction |
| Best Framework | Acknowledge-Pivot-Close (logic responds to logic) |

---

## Response Scripts

### Script 1: Gentle Approach

"I appreciate you sharing that with me, and I respect that you are doing your homework. That is actually a great sign — it tells me you are serious about getting the best result for your home.

Here is what I have seen in my experience: the homes I sell typically close at 5-8% more than the area average because of the marketing, staging guidance, and negotiation strategy I bring to the table. On a $500,000 home, that is $25,000 to $40,000 more in your pocket — even after the commission difference.

The real question is not what you pay the agent — it is what you walk away with at closing. Would it help if I showed you the actual numbers on my last five listings versus the area averages?"

### Script 2: Consultative Approach

"That is a fair question, and I want to make sure you have the full picture to make the best decision.

Here is the math: my commission is 2.5%, which on your home at $500,000 is $12,500. The 1% agent's commission is $5,000. So the difference between us is $7,500.

Now here is what I want you to think about: my average list-to-sale ratio is 98.5%. The average for discount brokerages in our market is 94.2%. On a $500,000 home, that 4.3% difference is $21,500.

So you can save $7,500 on commission and potentially leave $21,500 on the table. Or you can invest the $7,500 difference and likely net $14,000 more at closing.

I am not asking you to pay more — I am asking you to net more. Which matters more to you: the commission line or the bottom line?"

### Script 3: Direct Approach

"I hear you, and I want to be straightforward: if an agent is willing to discount their own compensation before they have even started working for you, what do you think they will do when a buyer comes in with a low offer on your home?

Commission is not a cost — it is an investment in the outcome. My job is not to list your home. My job is to sell it for the highest possible price in the shortest time with the least hassle to you. I do that through professional photography, targeted digital marketing, my buyer network, and my negotiation skills at the offer table.

The agents who compete on price are telling you they cannot compete on results. I compete on results.

Can I show you exactly what my marketing plan looks like for your home and how it is different from what a 1% agent provides?"

---

## Follow-Up Questions They May Ask

| Question | Recommended Response |
|---|---|
| "But aren't all agents basically doing the same thing?" | "That is like saying all restaurants are the same because they all serve food. The difference is in the quality of execution. Let me show you my marketing plan side by side with what a typical 1% listing includes — you will see the difference immediately." |
| "What if I just try the cheaper agent first?" | "You absolutely can, and I would never pressure you. But here is what I want you to know: the first 14 days on market are when your home gets the most attention. If it is not marketed properly from day one, you are losing the buyers who would have paid top dollar. A second listing always sells for less than a well-marketed first listing." |
| "Can you reduce your commission at all?" | "My commission reflects the investment I make in marketing your home — professional photography, video, staging consultation, targeted ads, and my time negotiating offers. I am happy to walk you through exactly where every dollar goes. What I will not do is cut corners on your marketing to lower my fee — that would hurt your bottom line, not help it." |

---

## Practice Scenario

**Setup:** You are at a listing appointment for a 4-bedroom home in a popular neighborhood. The sellers, Tom and Karen, are in their 50s, downsizing. They have interviewed two other agents. They have been polite and engaged throughout your presentation. At the end, Tom leans back and says:

**Client says:** "Sarah, we like everything you have shown us. But honestly, the agent we talked to yesterday said she would do it for 1%. That is a significant difference on a $500,000 home. Why should we pay you more?"

**Your response (walk-through):**

Step 1 — ACKNOWLEDGE (do not get defensive): "Tom, that is a great question, and I am glad you brought it up. You should absolutely understand what you are paying for."

Step 2 — PIVOT (shift from cost to net proceeds): "Let me ask you this — when you sell this home, what matters more to you: what you pay the agent, or what you deposit in your bank account after closing?"

Step 3 — Wait for answer. They will say "what we net" or something similar.

Step 4 — EDUCATE: "That is exactly right. Here is what the data shows..." [Present your list-to-sale ratio, average DOM, and marketing plan specifics].

Step 5 — CLOSE: "I would love the opportunity to sell your home and prove those numbers. Can we get the listing agreement signed today so I can get the photographer out here this week?"

**Common mistakes:**
1. Getting defensive or badmouthing the discount agent — this makes you look threatened
2. Immediately offering to lower your commission — this confirms their belief that commissions are negotiable and your rate was inflated
3. Focusing only on what you do (activities) instead of what they get (results and net proceeds)

---

## Confidence Builder

You are not selling your time — you are selling your outcome. The average FSBO home sells for $100,000 less than agent-assisted sales (NAR 2025 data). Discount agents have higher average DOM and lower list-to-sale ratios. You have data on your side. This week, practice the consultative script three times in front of a mirror, then once with a colleague playing the seller. By the fourth repetition, the words will feel natural and the numbers will roll off your tongue. Confidence is not the absence of nerves — it is preparation meeting opportunity.
```

---

## Top 25 Real Estate Agent Objections — Quick Reference

### Seller Objections

| # | Objection | Type | Key Response Pivot |
|---|---|---|---|
| 1 | "Your commission is too high" | Price/Value | Net proceeds, not commission cost |
| 2 | "Another agent said they'd list for less" | Competition | Results, not rates |
| 3 | "I can sell it myself (FSBO)" | Trust/Authority | Net proceeds gap: FSBO vs. agent |
| 4 | "My friend/family member is an agent" | Competition | "Your home deserves the best outcome, not the most comfortable choice" |
| 5 | "I need to think about it" | Stall | Isolate the real concern |
| 6 | "I'm not ready to sell yet" | Stall | Discover the real timeline |
| 7 | "I want to wait for spring/summer market" | Market Fear | Seasonal data + current demand |
| 8 | "Your pricing is too low — my home is worth more" | Price/Value | CMA data + overpricing risks |
| 9 | "I don't want to do repairs/staging" | Stall | ROI on preparation vs. price reduction |
| 10 | "We tried selling before and it didn't work" | Trust/Authority | "What was different then? Here is what I do differently." |
| 11 | "I want to wait and see what the market does" | Market Fear | Opportunity cost + current buyer demand |
| 12 | "We need to find a place first before we sell" | Stall | Bridge strategies, contingent offers, timing |

### Buyer Objections

| # | Objection | Type | Key Response Pivot |
|---|---|---|---|
| 13 | "The asking price is too high" | Price/Value | CMA + negotiation strategy |
| 14 | "I want to wait for prices to drop" | Market Fear | Rates + appreciation + wait cost |
| 15 | "I want to wait for interest rates to drop" | Market Fear | "Marry the house, date the rate" + refinance math |
| 16 | "We just started looking" | Stall | Provide value, build trust, no pressure |
| 17 | "We found a house on Zillow, do we need an agent?" | Trust/Authority | Negotiation value + process protection |
| 18 | "This house needs too much work" | Price/Value | Renovation ROI + negotiation leverage |
| 19 | "The neighborhood doesn't feel right" | Stall | Discover actual concern (safety? schools? commute?) |
| 20 | "My parents/advisor said now is a bad time to buy" | Market Fear | Specific data vs. general sentiment |
| 21 | "I want to keep looking" (after showing) | Stall | "What would the perfect home have that this one doesn't?" |

### FSBO & Expired Listing Objections

| # | Objection | Type | Key Response Pivot |
|---|---|---|---|
| 22 | "I've had bad experiences with agents" | Trust/Authority | Acknowledge + differentiate your approach |
| 23 | "I already have a buyer interested" | Competition | Contract protection + negotiation expertise |
| 24 | "Agents just put it on MLS and wait" | Trust/Authority | Walk through your full marketing plan |
| 25 | "My listing expired — agents can't sell my home" | Trust/Authority | "The previous approach didn't work. Here is what I do differently." |

## Edge Cases & Best Practices

- **Angry or Hostile Clients:** When the emotional temperature is "angry," do not attempt to overcome the objection. Instead, de-escalate: "I can hear this is really frustrating for you, and I do not want to add to that. Can I ask — what would make this situation better for you?" Let them vent, then address the underlying concern once they have calmed down.

- **Objections That Are Actually Deal-Breakers:** Not every objection is solvable. If a buyer says "I cannot get pre-approved" or a seller says "I owe more than the home is worth and will not bring cash to closing," these are not objections — they are factual barriers. Acknowledge the reality, offer what help you can (short sale referral, credit repair referral), and do not try to "overcome" something that is not overcomeable.

- **Cultural Sensitivity in Objection Handling:** Different cultures have different norms around negotiation, directness, and decision-making timelines. "I need to think about it" from a client whose culture values consensus decision-making is not a stall — it is a genuine process. Adjust your response to provide supporting materials they can share with family or advisors rather than pushing for an immediate decision.

- **Commission Objections After NAR Settlement (2024):** The real estate industry shifted after the NAR settlement changed how buyer agent commissions are handled. Be prepared to explain the new landscape clearly: what has changed, what has not, and how your compensation structure works. Transparency builds trust.

- **Spouse/Partner Not Present:** When one half of a couple raises an objection "on behalf of" the absent partner ("My husband thinks prices are too high"), avoid trying to overcome it through the present person. Instead: "I would love to address [partner's] concerns directly — would it be possible for all three of us to meet briefly?" The absent decision-maker must hear your response firsthand.

- **Written vs. Verbal Objections:** Email and text objections require different handling than verbal ones. You lose tone of voice and cannot read body language. Keep written responses shorter, use bullet points instead of paragraphs, and always end with a question to continue the dialogue. Never send a 500-word rebuttal essay via text.

## Integration

This skill connects with the broader real estate agent toolkit:

- **Skill 01 (Lead Qualification Engine):** When leads are scored as WARMING UP, anticipate objections based on their profile — first-time buyers will object on price and process, sellers from expired listings will object on agent trust. Pre-load relevant objection responses before your call.
- **Skill 02 (Property Description Generator):** Strong listing descriptions can preempt buyer objections about price — when a listing clearly communicates value, "the price is too high" becomes less common.
- **Skill 03 (Market Analysis Reporter):** CMA data is your most powerful tool against pricing objections from both buyers ("too high") and sellers ("too low"). Reference specific CMA figures in your objection responses.
- **Skill 04 (Client Follow-Up Sequencer):** When a lead raises an objection and you overcome it, the next follow-up touchpoint should reference the resolution: "I'm glad we talked through the commission question — here's the marketing plan I mentioned..."
- **Skill 06 (Contract Review Assistant):** During offer negotiations, buyers may object to contract terms. Use the Contract Review to identify the specific clause at issue and craft a response that addresses the risk without derailing the deal.
- **Skill 07 (Social Media Content Planner):** Create social media content that preemptively addresses common objections — posts about "why FSBO homes sell for less" or "the real cost of waiting for rates to drop" educate your audience before the objection ever comes up.

## 🔐 PERMISSIONS & SETUP CHECKLIST

No external permissions required. Attach this file to any Claude.ai chat and type the trigger phrase. Optional:

- [ ] **Voice mode (recommended for role-play):** Activate Claude voice mode for live spoken role-play; the skill includes "rehearsal scripts" the user can read aloud and Claude will respond as the prospect.
- [ ] **Past objection log (optional):** Paste a list of objections you hear most often in your market; Claude will tailor responses to your local language and pain points.
- [ ] **Brokerage scripts (optional):** If your brokerage has approved scripts, paste them; the skill will harmonize new responses with the established voice.

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
| Objection contains discriminatory or Fair-Housing-violating language from the client | Do not validate or normalize; surface a ⚠️ FAIR HOUSING flag, recommend the agent decline the request and document the exchange, and offer scripted exit language |
| Objection is actually a hidden financial-distress disclosure (foreclosure, divorce, bankruptcy) | Switch from sales mode to support mode; recommend pausing the close, providing resources, and consulting brokerage compliance / a real estate attorney before proceeding |

## 📖 DOMAIN GLOSSARY

| Term | Definition |
|---|---|
| **CMA (Comparative Market Analysis)** | A pricing report that compares the subject property to recently sold, active, and pending listings nearby — the agent's primary defense against both "your price is too high" and "your price is too low" objections. |
| **FSBO (For Sale By Owner)** | A homeowner attempting to sell without an agent. NAR data shows FSBOs sell on average for ~$100K less than agent-assisted sales. |
| **Expired Listing** | A property whose listing agreement ended without a sale. Owners are typically frustrated with their previous agent and need a Trust/Authority response framework. |
| **DOM (Days on Market)** | How long a listing has been active. High DOM weakens seller pricing power and is referenced in market-fear objection responses. |
| **ARV (After-Repair Value)** | The estimated value of a property after renovations. Used by wholesalers and flippers when handling "this needs too much work" buyer objections. |
| **Loop Close** | A response pattern that acknowledges the objection, isolates the decision criterion, and "loops" the prospect back to the underlying need (e.g., "If we could solve X, would Y be the next step?"). |

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
