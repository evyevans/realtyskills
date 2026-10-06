# Source playbook

This playbook supplies task procedures and examples. Follow the working rules in the skill entry, verify current jurisdiction-specific claims, and treat examples as illustrative.

# Landlord-Tenant Legal Risk Analyzer

This skill analyzes landlord-tenant situations — lease disputes, non-payment of rent, unauthorized occupants, property damage, security deposit disputes, eviction triggers, and habitability complaints — and delivers a structured legal risk assessment with state-specific guidance, required notice periods, legally required procedural steps, and recommended actions to protect the property owner's legal position.

## 🧠 SKILL IDENTITY

**WHO this skill is for:**
A property management company managing 20+ units who needs to triage landlord-tenant situations quickly and consistently. Also: a real estate investor with a problem tenant, a buy-and-hold portfolio operator dealing with non-payment, or a real estate attorney preparing a preliminary assessment before advising a landlord client.

**WHAT this skill does:**
Produces a Landlord-Tenant Legal Risk Assessment containing: (1) Classification of the situation type and applicable legal framework; (2) The landlord's rights and obligations under the applicable state statute; (3) The tenant's rights and legal defenses the tenant may assert; (4) Required notice — the exact type, content, delivery method, and timing required before any legal remedy; (5) Eviction procedure steps if applicable; (6) Security deposit compliance; (7) Habitability and retaliation risk analysis; (8) Recommended immediate actions ranked by legal urgency.

**WHERE to use this skill:**
Attach to a Claude.ai chat session and paste the situation description, relevant lease terms, and any tenant communications. Claude applies state-specific landlord-tenant law to the facts and delivers a structured risk assessment.

**WHEN to activate this skill:**
Activate the moment a tenant situation escalates beyond a routine maintenance request: first missed rent payment, unauthorized occupant discovered, lease violation notice needed, security deposit dispute, tenant threat of habitability complaint, or any communication that hints at legal action.

**WHY this skill matters:**
This workflow makes the required inputs and output structure explicit. Its numerical benchmarks are configurable assumptions, not validated performance claims.

**HOW this skill works (Overview):**
Claude first classifies the situation type (non-payment, lease violation, holdover, illegal activity, habitability, etc.) and identifies the applicable state statute and any applicable local ordinances. It then applies the state's specific notice requirements, cure periods, and eviction procedures to the facts, evaluates the tenant's likely legal defenses, and delivers a prioritized action plan with exact notice language where applicable.

---

## 📥 REQUIRED INPUTS

| Input | Format | Source | Required? | Example |
|-------|--------|--------|-----------|---------|
| State | US state abbreviation | User provides | Yes | OH |
| City / municipality | City name | User provides | No | Columbus (for local ordinance check) |
| Situation description | Plain text narrative | User provides | Yes | Tenant hasn't paid rent for 2 months; owes $3,600 |
| Lease term and type | Month-to-month / fixed term + dates | User provides | Yes | 12-month lease, expires 08/31/2026 |
| Monthly rent amount | Dollar amount | User provides | No | $1,800/month |
| Security deposit amount held | Dollar amount | User provides | No | $1,800 |
| Any prior notices served | Type and date | User provides | No | Verbal reminder on May 1, 2026 |
| Relevant lease provisions | Pasted text | User provides | No | Lease Section 12: late fee of $75 after 5-day grace period |
| Any tenant communications | Pasted text or summary | User provides | No | Tenant texted "I'll have rent by Friday" on May 3 |

---

## ⚙️ EXECUTION SOP

### Step 1: Classify Situation and Identify Applicable Legal Framework

**What Claude does:**
Classify the situation into one of the following categories (may be multiple):
1. **Non-Payment of Rent:** Tenant has not paid rent when due
2. **Lease Violation (Curable):** Tenant violated a lease term that can be corrected (unauthorized pet, unauthorized occupant, noise violation)
3. **Lease Violation (Incurable):** Tenant violated a lease term that cannot be cured (criminal activity, destruction of property, second material violation within 6 months)
4. **Holdover Tenancy:** Lease expired, tenant remains without new agreement
5. **Habitability / Repair Dispute:** Tenant alleges landlord failed to maintain habitable conditions
6. **Security Deposit Dispute:** Dispute over deductions from security deposit
7. **Retaliation Claim Risk:** Tenant may assert that landlord's action is retaliation for a protected activity (reporting code violations, joining a tenant union, asserting repair rights)
8. **Illegal Activity:** Criminal activity on the premises
9. **Domestic Violence Accommodation:** Tenant invokes state domestic violence protections

After classification, apply the applicable state landlord-tenant statute. Key statutes Claude applies:
- Ohio: Ohio Revised Code Chapter 5321
- California: Civil Code §§ 1940–1954 + local ordinances (LA, SF, Oakland, San Jose have additional rent control and just-cause requirements)
- Texas: Texas Property Code Chapter 92
- Florida: Florida Statutes Chapter 83
- New York: Real Property Law + NYC Rent Stabilization Code (NYC)
- Illinois: Landlord and Tenant Act (765 ILCS 720) + RLTO (Chicago)

**Tools / Resources needed:**
Claude's embedded landlord-tenant law knowledge base (current as of May 2026).

**Data source:**
User-provided situation details + Claude's regulatory knowledge.

**Output of this step:**
Situation classification + applicable statute citation + jurisdiction-specific flags (rent control, just-cause eviction, local ordinance overlays).

**Cowork behavior:**
PROCEED WITH ANALYSIS AND DRAFTING.

**If this step fails or required data is missing:**
If state is missing, ask for it before proceeding — landlord-tenant law is entirely state-specific.

---

### Step 2: Landlord Rights and Required Notice Analysis

**What Claude does:**
Based on the situation classification and state, specify:

**A. Notice Type Required:**
- Non-payment of rent: Most states require a "Pay or Quit" notice before filing for eviction
  - Ohio: 3-day notice to pay or vacate (ORC § 5321.17)
  - California: 3-day notice (non-controlled); just-cause cities may require additional steps
  - Texas: 3-day notice (Property Code § 24.005)
  - Florida: 3-day notice (FS § 83.56)
  - New York: 14-day notice (RPL § 753); NYC rent-stabilized: additional requirements

- Curable lease violation: "Cure or Quit" notice with a state-specific cure period
- Incurable violation: "Unconditional Quit" notice (no cure opportunity)
- Holdover: "Notice to Quit" or "Notice of Non-Renewal" (timing varies by tenancy type)

**B. Notice Content Requirements:**
Specify exactly what the notice must contain: property address, amount owed (for non-payment), the specific violation (for lease violations), cure period, what happens if not cured, landlord contact information.

**C. Notice Delivery Requirements:**
Method of service required by state: personal delivery, posted-and-mailed, certified mail, process server. Incorrect service can void the notice.

**D. Cure Period:**
Exact number of days the tenant has to pay, cure, or vacate — and whether calendar days or business days.

**Tools / Resources needed:**
Claude's landlord-tenant law knowledge base.

**Data source:**
Step 1 classification + state statute.

**Output of this step:**
Required Notice Specification: type, content requirements, delivery method, cure period, with a DRAFT of the notice where applicable.

**Cowork behavior:**
PROCEED WITH ANALYSIS AND DRAFTING.

**If this step fails or required data is missing:**
If the state's specific notice requirements are not in Claude's training data, provide the general framework and flag: "⚠️ Verify exact notice requirements with [STATE] statute or a licensed real estate attorney before serving notice."

---

### Step 3: Tenant Defense and Retaliation Risk Analysis

**What Claude does:**
Identify the legal defenses the tenant is likely to assert and assess whether any of the following protections apply:

**Common Tenant Defenses:**
- **Habitability defense:** Has the landlord failed to maintain required repairs? In most states, a landlord cannot evict for non-payment if the unit is uninhabitable. Document all repair requests and responses.
- **Retaliation defense:** If the tenant recently reported a code violation, requested repairs, or organized with other tenants, any adverse action within 60–180 days (state-specific) may be presumed retaliatory.
- **Notice deficiency:** Was prior notice served correctly? An improperly served or improperly worded notice is a procedural defense that can delay or defeat an eviction.
- **Discrimination defense:** Any action that disparately impacts a protected class.
- **Domestic violence protections:** Many states prohibit eviction of domestic violence victims for lease violations related to the abuse.
- **COVID/Local Moratorium Residual:** Verify whether any local moratorium protections are still in effect.

**Retaliation Risk Assessment:**
If any of the following occurred in the 60–180 days before the landlord's current action:
- Tenant requested repairs in writing
- Tenant filed a complaint with a housing agency
- Tenant joined a tenant organization
…flag as RETALIATION RISK and advise documenting the independent legitimate business reason for the action.

**Tools / Resources needed:**
None — legal defense analysis from embedded knowledge.

**Data source:**
User-provided situation details + Step 1 classification.

**Output of this step:**
Tenant Defense Risk Table: each potential defense, its viability based on the facts, and the landlord's countermeasure.

**Cowork behavior:**
PROCEED WITH ANALYSIS AND DRAFTING.

**If this step fails or required data is missing:**
If repair/complaint history is unknown, flag retaliation risk as CANNOT ASSESS and ask the user to confirm whether the tenant has made any recent repair requests or complaints.

---

### Step 4: Security Deposit Compliance Check (if applicable)

**What Claude does:**
If a security deposit dispute or potential deduction is involved, apply the state's security deposit rules:

- **Return deadline:** Days the landlord has to return the deposit after move-out (varies: OH = 30 days, CA = 21 days, TX = 30 days, FL = 15–60 days depending on whether deductions are claimed)
- **Itemization requirement:** Written itemized statement required if any deductions are taken
- **Allowable deductions:** Unpaid rent, damages beyond normal wear and tear (define "normal wear and tear" for the user's state)
- **Penalty for non-compliance:** Most states impose 2× or 3× the deposit as a penalty for wrongful withholding
- **Pre-move-in condition documentation:** Was a move-in inspection conducted and documented? This is the landlord's primary evidentiary asset.

**Tools / Resources needed:**
None — state deposit law from Claude's knowledge base.

**Data source:**
User-provided deposit amount and situation + state statute.

**Output of this step:**
Security Deposit Compliance Checklist with the return deadline, allowable deductions, itemization requirements, and penalty exposure.

**Cowork behavior:**
PROCEED WITH ANALYSIS AND DRAFTING.

**If this step fails or required data is missing:**
If deposit amount or move-out date is unknown, provide the state's compliance framework as a template.

---

### Step 5: Generate Prioritized Action Plan

**What Claude does:**
Compile all findings into the structured Legal Risk Assessment (see Output Format), with a numbered action plan ranked by legal urgency:
1. Actions that must be taken immediately to preserve legal rights
2. Actions required before filing any court action
3. Documentation to gather
4. Recommended professional consultations

**Tools / Resources needed:**
None.

**Data source:**
All prior steps.

**Output of this step:**
Complete Landlord-Tenant Legal Risk Assessment Report.

**Cowork behavior:**
CONFIRM BEFORE PROCEEDING — if the recommended action involves eviction filing, confirm: "The analysis recommends initiating eviction proceedings. Do you want me to draft the required notice for your review?"

**If this step fails or required data is missing:**
Deliver partial report with incomplete sections labeled.

---

## 📤 OUTPUT FORMAT

**Output type:** Legal Risk Assessment Report  
**Delivery method:** Returned directly in chat

---

```
LANDLORD-TENANT LEGAL RISK ASSESSMENT — Evykynn
Property:     4821 Maple Ave, Columbus OH 43215
Situation:    Non-Payment of Rent — 2 months overdue
State:        Ohio | Governing Statute: ORC Chapter 5321
Date:         May 10, 2026

━━━━━━━━━━━━━━━━ SITUATION SUMMARY ━━━━━━━━━━
Type:          Non-Payment of Rent (Curable)
Amount Owed:  $3,600 (2 months × $1,800)
Late Fees:    $150 (2 months × $75 per lease Section 12)
Total Due:    $3,750
Lease Status: Active — expires 08/31/2026

━━━━━━━━━━━━━━━━ REQUIRED NOTICE ━━━━━━━━━━━━
Notice Type:  3-Day Notice to Pay Rent or Vacate
Authority:    Ohio Revised Code § 5321.17

CONTENT REQUIREMENTS:
✅ Property address
✅ Total amount owed (rent only — $3,600; fees separate)
✅ 3-day cure period (calendar days, excluding weekends: verify)
✅ Statement that failure to pay or vacate will result in
   eviction proceedings
✅ Landlord name and contact information

DELIVERY METHOD: Personal service OR posting on door AND
mailing by first-class mail on the same day (Ohio standard)

DRAFT NOTICE:
"NOTICE TO PAY RENT OR VACATE
Date: May 10, 2026
To: [Tenant Name], 4821 Maple Ave, Columbus OH 43215

You are hereby notified that you are delinquent in the
payment of rent for the premises you occupy at 4821 Maple Ave,
Columbus, Ohio 43215. The amount of rent now past due and
unpaid is $3,600.00 for the months of April and May 2026.

You are required to pay said amount within THREE (3) DAYS
of receipt of this notice, or to surrender possession of
said premises. Failure to do so will result in legal action
to recover possession of the property.

[Landlord Name] | [Address] | [Phone]"

⚠️ Have a licensed Ohio attorney review before serving.

━━━━━━━━━━━━━━━━ TENANT DEFENSE RISKS ━━━━━━
⚠️ Habitability Risk: LOW — no repair requests noted
⚠️ Retaliation Risk: LOW — no protected activity noted
⚠️ Notice Deficiency Risk: MEDIUM — text message from tenant
   on May 3 ("I'll have rent by Friday") may create estoppel
   argument. Document that no payment was received by May 8.
⚠️ Discrimination Risk: NONE IDENTIFIED

━━━━━━━━━━━━━━━━ PRIORITY ACTION PLAN ━━━━━━
1. [IMMEDIATE] Serve 3-Day Notice to Pay or Vacate — today
2. [DAY 4] If unpaid: File eviction complaint with Franklin
   County Municipal Court (filing fee: ~$120; search
   franklincountyohio.gov/municipal-court for current fee)
3. [NOW] Photograph all communications — preserve text thread
4. [NOW] Document all verbal conversations in writing
5. [PRE-FILING] Consult Ohio real estate attorney before filing

Security Deposit: $1,800 held — do not apply to unpaid rent
without legal advice; complicates eviction filing in Ohio.

⚠️ LEGAL DISCLAIMER: This assessment is generated by Claude
an AI assistant via an automated skill. It is not legal advice.
Consult a licensed Ohio real estate attorney before serving
legal notices or filing court actions.
```

---

## 🔐 PERMISSIONS & SETUP CHECKLIST

No external permissions or setup required.

- [ ] **State Statute Verification:** Verify current notice periods and procedures with your state's landlord-tenant statute — laws change frequently.
- [ ] **Attorney Consultation:** Budget for a 1-hour consultation with a licensed real estate attorney in your state before filing any eviction action.
- [ ] **Document Retention:** Preserve all tenant communications (texts, emails, notices) in a secure location.

---

## ✅ QUALITY SELF-CHECK

Before delivering any output, Claude must internally verify every item below:

- [ ] Situation correctly classified and applicable state statute identified
- [ ] Required notice type, content, delivery method, and cure period are all specified
- [ ] Draft notice language is provided where applicable
- [ ] Tenant defense risks are evaluated — not just landlord's rights
- [ ] Retaliation risk is specifically assessed
- [ ] Security deposit compliance is addressed if relevant
- [ ] ⚠️ LEGAL DISCLAIMER is present
- [ ] Action plan is prioritized by legal urgency with specific next steps

---

## ⚠️ EDGE CASES & ESCALATION RULES

| Scenario | Claude's Exact Response |
|----------|------------------------|
| Tenant has Section 8 / housing voucher | Flag: "⚠️ Section 8/HCV tenants have additional federal protections. HUD requires specific notice procedures for voucher holders. Consult your local housing authority and a real estate attorney before proceeding." |
| Property is in rent-controlled jurisdiction | Flag: "⚠️ This jurisdiction may have rent control and just-cause eviction requirements that limit your remedies. Verify local ordinances before taking any action." |
| Tenant reports habitability issues during eviction | Flag as HIGH RISK: "⚠️ A habitability complaint during eviction proceedings may create a retaliatory eviction defense. Document all repair requests and responses immediately." |
| Legal or criminal activity on premises | "⚠️ If illegal activity (drug manufacturing, gang activity) is confirmed on premises, this may be an incurable violation allowing immediate Unconditional Quit notice. Contact a real estate attorney and local law enforcement." |
| Tenant claims domestic violence protections | "⚠️ LEGAL FLAG: Many states prohibit eviction of domestic violence victims for lease violations related to the abuse. Consult a real estate attorney before taking any adverse action." |
| Session approaching context limit | Write `_PROGRESS_CHECKPOINT.md` with completed analysis sections before context is exhausted |

---

## 📖 DOMAIN GLOSSARY

| Term | Definition |
|------|-----------|
| Pay or Quit Notice | A written notice demanding that a tenant pay overdue rent within a specified period or vacate the premises |
| Cure or Quit Notice | A written notice giving a tenant a specified period to correct a lease violation or vacate |
| Unconditional Quit Notice | A notice requiring a tenant to vacate without the option to cure — used for serious or repeated violations |
| Holdover Tenant | A tenant who remains in possession after the lease expires without a new agreement |
| Unlawful Detainer | The legal action for eviction of a tenant who remains in possession without legal right |
| Habitability | The legal standard requiring landlords to maintain rental property in a livable condition — includes heat, water, structural integrity, and absence of pest infestation |
| Retaliatory Eviction | An illegal eviction motivated by the tenant's exercise of a legally protected right (requesting repairs, reporting code violations, organizing with other tenants) |
| Normal Wear and Tear | The gradual deterioration of a rental property resulting from ordinary use — distinguished from damage caused by tenant negligence or abuse; not deductible from security deposit |
| Just-Cause Eviction | A local or state law requiring the landlord to have a legally recognized reason (just cause) before terminating a tenancy or evicting a tenant |

---

*Authored by Evykynn | Real Estate Agentic Automation*

*Maintained as part of RealtySkills by Evykynn. Example dates and figures are illustrative.*
