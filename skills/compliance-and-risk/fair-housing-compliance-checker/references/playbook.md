# Source playbook

This playbook supplies task procedures and examples. Follow the working rules in the skill entry, verify current jurisdiction-specific claims, and treat examples as illustrative.

# Fair Housing Compliance Checker

This skill performs an automated audit of real estate listing descriptions, marketing copy, rental advertisements, and agent communications for violations of the Fair Housing Act (42 U.S.C. § 3604) and HUD regulations. It flags discriminatory language, steering patterns, and prohibited preferences — then rewrites offending content to be compliant while preserving the listing's marketing effectiveness.

## 🧠 SKILL IDENTITY

**WHO this skill is for:**
A brokerage owner, team lead, or independent agent who publishes listing descriptions, rental ads, social media content, or email campaigns and needs to ensure every piece of published content is free of Fair Housing Act violations before it goes live. Also: a property management company's leasing team that needs to screen rental listing copy before posting.

**WHAT this skill does:**
Scans the submitted text for violations across all seven federally protected classes (race, color, national origin, religion, sex, familial status, disability) plus applicable state-protected classes. For each violation found, it identifies the specific problematic phrase, explains exactly why it violates the FHA or HUD advertising guidelines, assigns a severity level (CRITICAL / WARNING / ADVISORY), and provides a compliant rewrite of the offending passage. Delivers a clean, compliance-verified version of the full text.

**WHERE to use this skill:**
Attach to a Claude.ai chat session and paste the listing description, ad copy, or communication into the chat. Alternatively, load into a Claude.ai Project so every team member can run compliance checks before publishing. This is a fully autonomous skill — no configuration required.

**WHEN to activate this skill:**
Before publishing any listing description to MLS, Zillow, Realtor.com, Facebook Marketplace, or any public platform. Before running any paid social media or Google ad targeting real estate. Before sending any marketing email or newsletter containing property descriptions. Before posting any "For Rent" advertisement.

**WHY this skill matters:**
This workflow makes the required inputs and output structure explicit. Its numerical benchmarks are configurable assumptions, not validated performance claims.

**HOW this skill works (Overview):**
Claude applies a multi-pass compliance audit. Pass 1 scans for explicit prohibited terms — words and phrases that directly reference protected classes. Pass 2 applies contextual analysis to detect implicit steering, coded language, and preference statements that don't use explicit class terms but still violate the FHA by indicating preference, limitation, or discrimination. Pass 3 reviews the overall framing for steering patterns (describing neighborhood demographics, proximity to religious institutions as selling points, etc.). Claude then rewrites any offending content and delivers the verified compliant version.

---

## 📥 REQUIRED INPUTS

| Input | Format | Source | Required? | Example |
|-------|--------|--------|-----------|---------|
| Content to audit | Pasted text | User provides | Yes | Full listing description, ad copy, or email text |
| Content type | Listing / Rental ad / Social post / Email / Other | User provides | No | MLS listing description |
| State of transaction | US state | User provides | No | Ohio (for state-level protected class additions) |

**Note:** This skill is fully autonomous once content is pasted. No additional configuration required.

---

## ⚙️ EXECUTION SOP

### Step 1: Ingest Content and Identify Content Type

**What Claude does:**
Read the full submitted text. Identify whether it is: a property listing description, a rental advertisement, a social media post, a marketing email, or an agent-to-client communication. Establish the applicable regulatory framework: the Fair Housing Act applies to all content types; HUD's advertising guidelines (HUD Circular 29 CFR Part 110) apply specifically to advertising; RESPA applies to referral and settlement service marketing.

**Tools / Resources needed:**
None — works entirely from pasted content in Claude context.

**Data source:**
User-provided text.

**Output of this step:**
Content type identification + applicable regulatory framework noted. Proceed immediately to Pass 1.

**Cowork behavior:**
PROCEED WITH ANALYSIS AND DRAFTING — this skill is fully autonomous.

**If this step fails or required data is missing:**
If no content is provided, ask: "Please paste the listing description, ad copy, or other content you'd like me to review for fair housing compliance."

---

### Step 2: Pass 1 — Explicit Prohibited Terms Scan

**What Claude does:**
Scan the submitted text for any explicit reference — favorable or unfavorable — to the following federally protected classes:

**Federal Protected Classes (FHA, 42 U.S.C. § 3604):**
- Race: Any reference to race, racial identity, or racial demographics
- Color: Any reference to skin color
- National Origin: References to country of birth, ancestry, immigration status, language ability as a qualification
- Religion: References to religious affiliation, proximity to churches/mosques/temples/synagogues as a selling feature (steering), religious holidays
- Sex: References to gender, gender identity, sexual orientation (in jurisdictions covering these), marital status (in many states)
- Familial Status: References to children, "adults only," "mature community," "perfect for empty nesters," "quiet couple," family size limitations
- Disability: References to accessibility needs, mental health status, addiction recovery status; "able-bodied," "normal," language that implies physical requirements

**Additional terms flagged for explicit scan:**
- "Exclusive neighborhood," "desirable area," "nice neighborhood" — implicit demographic steering
- "Safe streets," "quiet community" — may imply racial steering in context
- "Walking distance to [religious institution]" — implies religious preference
- "No children," "adults only" (outside qualifying senior housing) — familial status violation
- "Perfect for professional couple" — sex/marital status implications

**Tools / Resources needed:**
None — comprehensive pattern matching from Claude's training data.

**Data source:**
Submitted text from Step 1.

**Output of this step:**
Explicit Terms Findings Table: each flagged phrase, its location in the text, the protected class implicated, and severity (CRITICAL/WARNING/ADVISORY).

**Cowork behavior:**
PROCEED WITH ANALYSIS AND DRAFTING.

**If this step fails or required data is missing:**
If no explicit violations are found in Pass 1, note "Pass 1: No explicit violations found" and proceed to Pass 2.

> 💡 **Precision Note:** "Walking distance to St. Patrick's Church" is a CRITICAL violation in a listing description — it indicates a religious preference even though no religion is being excluded. HUD's advertising guidelines prohibit using religious landmarks as selling features because it signals a preferred buyer identity. Rewrite as: "Walking distance to local churches and community centers."

---

### Step 3: Pass 2 — Contextual and Coded Language Analysis

**What Claude does:**
Apply contextual analysis to detect implicit steering and coded language. Claude uses extended thinking to evaluate the full text for patterns that don't use explicit class terms but still violate the FHA:

**Coded language patterns to detect:**
- Neighborhood demographic signaling: "up-and-coming area," "gentrifying neighborhood," "changing area," "established neighborhood" — can signal racial composition
- School quality as a proxy: Naming specific schools by reputation without factual basis — can be used as a proxy for racial composition
- Occupancy restrictions: "Maximum 2 occupants" (may violate familial status if not based on legitimate health/safety standards — typically 2 per bedroom is the HUD standard)
- Language proficiency requirements stated for tenants: "Must speak English" — national origin violation
- Income proxies: Requirements that may disparately impact protected classes without legitimate business justification
- Steering language: Describing the property as "perfect for" any specific demographic group not related to the property's features

**Tools / Resources needed:**
None — contextual reasoning within Claude context.

**Data source:**
Submitted text.

**Output of this step:**
Coded Language Findings Table: each flagged pattern, the specific text passage, the protected class implicated, and the mechanism by which it violates the FHA.

**Cowork behavior:**
PROCEED WITH ANALYSIS AND DRAFTING.

**If this step fails or required data is missing:**
If contextual analysis is inconclusive (borderline case), present both interpretations and recommend the conservative compliant rewrite.

---

### Step 4: Pass 3 — Steering Pattern Review

**What Claude does:**
Evaluate the overall framing and emphasis of the content for steering patterns — directing buyers or renters toward or away from properties based on protected class characteristics:

- Does the listing describe the surrounding community in terms that implicitly communicate the racial or ethnic composition?
- Does the listing feature religious landmarks, ethnic restaurants, or cultural institutions in a way that signals a preferred buyer identity?
- Does the rental advertisement use language that would discourage protected-class applicants from applying?
- Does the listing omit legally required equal housing opportunity disclosures or logos?

**EHO Logo Check:** For printed or digital advertisements of significant size (per HUD guidelines), verify that the Equal Housing Opportunity logo or statement is present.

**Tools / Resources needed:**
None.

**Data source:**
Submitted text + findings from Steps 2 and 3.

**Output of this step:**
Steering Pattern Findings and EHO disclosure status.

**Cowork behavior:**
PROCEED WITH ANALYSIS AND DRAFTING.

**If this step fails or required data is missing:**
If EHO logo status cannot be determined from text alone, note: "Cannot verify EHO logo presence from text submission — confirm EHO logo appears in the published ad."

---

### Step 5: Generate Compliant Rewrites

**What Claude does:**
For every violation found in Passes 1–3, generate a compliant rewrite of the specific passage that:
- Removes the offending language entirely
- Preserves the marketing intent (describe the property's features, not its demographics)
- Uses feature-based, objective language: describe what the property has, not who should live in it
- Maintains the listing's appeal and descriptive quality

Then assemble the FULL compliant rewrite of the entire submitted text — not just the flagged passages — incorporating all corrections.

**Tools / Resources needed:**
None.

**Data source:**
Original text + all findings from Steps 1–4.

**Output of this step:**
(1) Individual rewrite for each flagged passage, (2) Complete compliant version of the full submitted text.

**Cowork behavior:**
PROCEED WITH ANALYSIS AND DRAFTING.

**If this step fails or required data is missing:**
If a passage is ambiguous, provide two rewrite options and ask the user to select.

---

### Step 6: Deliver Final Audit Report

**What Claude does:**
Assemble the complete Fair Housing Compliance Audit Report (see Output Format), including: executive summary with violation count and severity, detailed findings table, the full compliant rewrite, and an advisory note.

**Tools / Resources needed:**
None.

**Data source:**
All prior steps.

**Output of this step:**
Complete formatted compliance report.

**Cowork behavior:**
PROCEED WITH ANALYSIS AND DRAFTING — deliver the complete report without additional confirmation.

**If this step fails or required data is missing:**
Deliver a partial report clearly noting what could not be verified and why.

---

## 📤 OUTPUT FORMAT

**Output type:** Compliance Audit Report + Compliant Rewrite  
**Delivery method:** Returned directly in chat — ready to review and implement

---

```
FAIR HOUSING COMPLIANCE AUDIT — Evy Evans
Content Type:   MLS Listing Description
Property:       4821 Maple Ave, Columbus OH
Analyst:        AI assistant via Evy Evans Skill Library
Date:           May 10, 2026

━━━━━━━━━━━━━━━━ EXECUTIVE SUMMARY ━━━━━━━━━━
VIOLATIONS FOUND: 3
  CRITICAL:   1 (must correct before publishing)
  WARNING:    1 (strongly recommended correction)
  ADVISORY:   1 (best practice recommendation)

━━━━━━━━━━━━━━━━ DETAILED FINDINGS ━━━━━━━━━━

[CRITICAL] Violation #1 — Familial Status
Original text: "Perfect for a young professional couple or empty
nesters — no children in the neighborhood."
Protected Class: Familial Status (42 U.S.C. § 3604(c))
Issue: "No children in the neighborhood" states a preference that
the dwelling not be occupied by families with children. This is a
direct violation of the FHA's prohibition on advertising that
indicates a preference, limitation, or discrimination based on
familial status.
Compliant Rewrite: "A wonderful home in a quiet, established
neighborhood — ideal for anyone looking for tranquil living
with easy access to downtown Columbus."

[WARNING] Violation #2 — National Origin / Language
Original text: "Tenant must be fluent English speaker."
Protected Class: National Origin
Issue: Requiring English language proficiency as a tenant
qualification without a legitimate business necessity constitutes
discrimination based on national origin.
Compliant Rewrite: Remove entirely. Tenant qualification criteria
should be based on financial qualifications (income, credit),
rental history, and legitimate background screening — not language.

[ADVISORY] Violation #3 — EHO Disclosure Missing
Issue: This listing description does not include an Equal Housing
Opportunity statement. HUD guidelines require EHO disclosure in
advertisements of sufficient size.
Recommendation: Add to all printed and digital listings:
"Equal Housing Opportunity" or the EHO logo (🏠 with equal sign).

━━━━━━━━━━━━━━━━ COMPLIANT REWRITE ━━━━━━━━━━
[Full corrected version of the listing description with all
violations removed and marketing quality preserved]

━━━━━━━━━━━━━━━━ ADVISORY NOTE ━━━━━━━━━━━━━━
⚠️ LEGAL DISCLAIMER: This audit was performed by AI assistant
via an Evy Evans automated compliance skill. It is intended to
assist in identifying potential fair housing concerns — not to
provide legal advice. For formal fair housing compliance training
or response to a HUD complaint, consult a licensed real estate
attorney or HUD-certified fair housing organization.
```

---

## 🔐 PERMISSIONS & SETUP CHECKLIST

No external permissions or setup required. Attach this file to any Claude.ai chat and type the trigger phrase. This skill runs entirely within Claude's context window.

- [ ] **Team Deployment:** Upload this skill to a Claude.ai Project so all agents and team members can run compliance checks before publishing any listing.
- [ ] **Optional — Automated Pre-Publish Hook:** Integrate via n8n or Zapier to automatically run this check when new MLS input is added to your listing management system.

---

## ✅ QUALITY SELF-CHECK

Before delivering any output, Claude must internally verify every item below:

- [ ] All three passes (explicit terms, coded language, steering patterns) were completed — none skipped
- [ ] Every violation is assigned a severity level (CRITICAL / WARNING / ADVISORY)
- [ ] Every violation includes a specific compliant rewrite — not just identification
- [ ] The full compliant rewrite of the complete submitted text is provided
- [ ] ⚠️ LEGAL DISCLAIMER is present at the end of the report
- [ ] EHO disclosure status is addressed
- [ ] Zero placeholder text remains in any rewrite
- [ ] Output is immediately actionable — the compliant rewrite can replace the original without further editing

---

## ⚠️ EDGE CASES & ESCALATION RULES

| Scenario | Claude's Exact Response |
|----------|------------------------|
| CRITICAL violation found | Highlight prominently in the report and note: "This content must be corrected before publishing. Publishing with this violation creates significant legal exposure." |
| User insists a flagged phrase is acceptable | Explain the specific regulatory basis for the flag. Do not remove the violation from the report. Note: "You may wish to consult a real estate attorney for a definitive ruling on this specific language." |
| Content is in a language other than English | Translate to English for analysis, perform the audit, then flag: "Non-English content was translated for analysis. Verify the translation is accurate and the compliant rewrite reflects the original intent." |
| User submits a rental application (not a listing) | Analyze for discriminatory screening criteria: protected class questions, income-to-rent ratios that may disparately impact familial status, credit thresholds, etc. |
| Legal or compliance risk detected | ⚠️ LEGAL FLAG: Always recommend attorney consultation for CRITICAL violations. Never advise the user that a violation is "probably fine." |
| Senior housing exemption claimed | Note: "Senior housing exemptions under the Housing for Older Persons Act (HOPA) require formal certification. Verify your property meets HOPA requirements before claiming this exemption." |
| Session approaching context limit | Write `_PROGRESS_CHECKPOINT.md` with completed passes and remaining analysis before context is exhausted |

---

## 📖 DOMAIN GLOSSARY

| Term | Definition |
|------|-----------|
| Fair Housing Act (FHA) | Federal law (42 U.S.C. § 3604) prohibiting discrimination in the sale, rental, or financing of housing based on seven protected classes |
| Protected Class | A group of people protected from discrimination by law; the seven federal classes are: race, color, national origin, religion, sex, familial status, and disability |
| Familial Status | A protected class covering families with children under 18, pregnant women, and persons in the process of adopting a child |
| Steering | The illegal practice of directing homebuyers or renters toward or away from particular neighborhoods based on their protected class |
| EHO | Equal Housing Opportunity — the HUD designation and logo required to be displayed in qualifying real estate advertisements |
| HUD | U.S. Department of Housing and Urban Development — the federal agency that enforces the Fair Housing Act |
| HOPA | Housing for Older Persons Act — provides an exemption to familial status protections for qualifying senior housing communities (80% of units occupied by persons 55+ or 100% 62+) |
| Disparate Impact | A legal theory under which a neutral policy or practice can constitute discrimination if it has a disproportionate adverse effect on a protected class, even without discriminatory intent |
| Coded Language | Words or phrases that appear neutral on their face but are understood to signal preferences about protected class characteristics — e.g., "desirable neighborhood" as a racial proxy |

---

*Authored by Evy Evans | Real Estate Agentic Automation*  
*Maintained as part of RealtySkills by Evy Evans. Example dates and figures are illustrative.*
