# Source playbook

This playbook supplies task procedures and examples. Follow the working rules in the skill entry, verify current jurisdiction-specific claims, and treat examples as illustrative.

# Purchase Agreement & LOI Drafter

This skill produces attorney-reviewed-template-quality Letters of Intent (LOIs) and full residential Purchase and Sale Agreements (PSAs) tailored to investor, wholesaler, and institutional buyer use cases. It populates every key field — parties, property, price, terms, contingencies, earnest money, closing timeline, and special provisions — from the deal data you provide. The output is a complete, ready-to-use document, not a partial template requiring manual fill-in.

## 🧠 SKILL IDENTITY

**WHO this skill is for:**
A real estate investor, wholesaler, or institutional buyer who needs to move from verbal agreement to written offer within minutes — without waiting for an attorney or a transaction coordinator to draft the paperwork. Also: a real estate transaction attorney who needs a first-draft starting point for a non-standard acquisition structure (subject-to, assignment, seller finance).

**WHAT this skill does:**
Produces one of two documents based on user selection:
1. **Letter of Intent (LOI):** A 1–2 page non-binding term sheet outlining proposed purchase price, earnest money, financing contingency, due diligence period, closing date, and key deal-specific provisions — formatted for immediate delivery to the seller or seller's agent.
2. **Purchase and Sale Agreement (PSA):** A full residential acquisition contract including all standard sections: parties, property description, purchase price, financing terms, contingencies (inspection, financing, title), earnest money, default provisions, closing date, special provisions, and signature block — formatted for e-signature or attorney review.

**WHERE to use this skill:**
Attach to a Claude.ai chat session and type the trigger phrase with your deal details. Claude returns the complete document in chat — ready to copy into Google Docs, paste into DocuSign, or send to a transaction attorney for final review.

**WHEN to activate this skill:**
Activate immediately after reaching verbal agreement with a motivated seller — before momentum fades, before the seller talks to another buyer, and before you need to wire an EMD. Also use when a wholesaler needs to assign a contract to an end buyer and needs an Assignment of Contract addendum.

**WHY this skill matters:**
This workflow makes the required inputs and output structure explicit. Its numerical benchmarks are configurable assumptions, not validated performance claims.

**HOW this skill works (Overview):**
Claude first confirms whether the user needs an LOI or a full PSA, then collects all required deal fields through a structured intake. It applies standard residential purchase contract language, investor-friendly contingency provisions, and any special provisions the user specifies (assignment clause, subject-to language, seller finance terms). Claude then assembles the complete document, flags any field that requires legal review, and delivers the formatted output ready for immediate use.

---

## 📥 REQUIRED INPUTS

| Input | Format | Source | Required? | Example |
|-------|--------|--------|-----------|---------|
| Document type needed | LOI or PSA | User provides | Yes | PSA |
| Buyer name(s) | Full legal name or entity name | User provides | Yes | Maple Capital LLC |
| Seller name(s) | Full legal name or entity name | User provides | Yes | John & Mary Smith |
| Property address | Full street address + county | User provides | Yes | 4821 Maple Ave, Columbus OH, Franklin County |
| Legal description | From title search or tax record | User provides | No | Lot 14, Block 3, Sunrise Estates |
| Purchase price | Dollar amount | User provides | Yes | $135,000 |
| Earnest money deposit | Dollar amount | User provides | Yes | $2,500 |
| EMD held by | Escrow company or title company name | User provides | Yes | Midland Title & Escrow |
| Financing type | Cash / Hard Money / Conv. / Seller Finance | User provides | Yes | Cash |
| Inspection period | Number of days | User provides | Yes | 10 business days |
| Closing date | Specific date or "X days from execution" | User provides | Yes | June 15, 2026 |
| Special provisions | Assignment clause, subject-to, AS-IS, etc. | User provides | No | Buyer reserves right to assign this contract |
| State of transaction | US state abbreviation | User provides | Yes | OH |

---

## ⚙️ EXECUTION SOP

### Step 1: Confirm Document Type and Collect All Inputs

**What Claude does:**
Ask the user: "Do you need a Letter of Intent (LOI — non-binding term sheet) or a full Purchase and Sale Agreement (PSA — binding contract)?" If the user has already specified in their message, proceed. Then review all inputs against the Required Inputs table above. If any required field is missing, ask for all missing fields in a single consolidated question before proceeding — do not draft partial documents.

**Tools / Resources needed:**
None — conversational intake within Claude context.

**Data source:**
User-provided deal information.

**Output of this step:**
Confirmed document type + complete validated input set, or a single consolidated request for any missing required fields.

**Cowork behavior:**
CONFIRM BEFORE PROCEEDING — confirm the document type with the user before drafting begins.

**If this step fails or required data is missing:**
List all missing fields and ask for them together: "Before I draft your [LOI/PSA], I need the following: [list]. Please provide these and I'll draft the document immediately."

---

### Step 2: Apply State-Specific Legal Context

**What Claude does:**
Based on the state of transaction, apply the following state-specific awareness to the document:
- **Attorney review states** (NJ, IL, NY, MA, CT, DE): Flag that attorney review period clauses are standard and recommended — insert a 5-business-day attorney review contingency by default.
- **Disclosure-heavy states** (CA, FL, TX): Note applicable mandatory disclosure requirements (Transfer Disclosure Statement in CA, Seller's Disclosure in TX) that must accompany the PSA.
- **Deed of trust vs. mortgage states**: Adjust security instrument reference accordingly.
- For all states: include a governing law clause referencing the transaction state.

⚠️ LEGAL FLAG: Real estate contract law is state-specific. This document is drafted based on general residential purchase contract conventions. A licensed real estate attorney in [STATE] must review this document before execution.

**Tools / Resources needed:**
None — Claude's legal knowledge of US state real estate practice applied from training data.

**Data source:**
User-provided state + Claude's embedded legal knowledge base.

**Output of this step:**
A state-context note appended to the document header and relevant jurisdiction-specific clauses flagged for attorney review.

**Cowork behavior:**
PROCEED WITH ANALYSIS AND DRAFTING — this is an analytical and generative step.

**If this step fails or required data is missing:**
If the state is not provided, ask before proceeding — state law is fundamental to the document's enforceability.

> 💡 **Precision Note:** Never draft language that purports to waive mandatory state disclosures. If a user requests this, insert: "⚠️ LEGAL FLAG: Mandatory seller disclosure requirements in [STATE] cannot be contractually waived. Consult a real estate attorney before attempting to modify disclosure obligations."

---

### Step 3: Draft the Letter of Intent (if LOI selected)

**What Claude does:**
Produce a complete 1–2 page LOI using the following structure:

**LOI STRUCTURE:**
1. Header: Date, Buyer, Seller, Property Address
2. Proposed Purchase Price
3. Earnest Money: Amount, held-by, refund conditions
4. Due Diligence Period: Length, what it covers, termination right
5. Financing Contingency: Type of financing, approval deadline (or waived for cash)
6. Closing Date: Target date or days-from-execution
7. AS-IS condition statement (if applicable)
8. Assignment Rights: Buyer's right to assign contract to a related entity
9. Expiration: LOI expires in 48–72 hours if not countersigned
10. Non-Binding Acknowledgment: Standard clause that LOI is not a binding contract
11. Signature Block: Buyer name, date, signature line; Seller name, date, signature line

**Tools / Resources needed:**
None — fully generated from Step 1 inputs.

**Data source:**
Validated deal inputs from Step 1.

**Output of this step:**
Complete formatted LOI document, ready to send.

**Cowork behavior:**
CONFIRM BEFORE PROCEEDING — present the draft LOI and ask: "Review this LOI draft. Shall I finalize it, or would you like any changes before delivery?"

**If this step fails or required data is missing:**
Flag missing fields inline with [NEEDS ATTORNEY INPUT] markers rather than leaving blanks.

---

### Step 4: Draft the Purchase and Sale Agreement (if PSA selected)

**What Claude does:**
Produce a complete residential PSA using the following full section structure:

**PSA SECTIONS:**
1. **Parties:** Buyer and Seller full legal names, entity type if applicable
2. **Property Description:** Street address, legal description, APN/parcel number if provided
3. **Purchase Price & Payment Terms:** Total price, down payment, financing terms, lender name
4. **Earnest Money Deposit:** Amount, due date (typically 3 business days from execution), held-by, conditions for refund vs. forfeiture
5. **Inspection Contingency:** Period length, scope (physical, environmental, roof, HVAC), termination procedure, repair negotiation deadline
6. **Financing Contingency:** Loan type, loan amount, approval deadline (or WAIVED for cash/hard money)
7. **Title Contingency:** Seller provides marketable title via [title company]; buyer has [X] days to object to title exceptions
8. **Closing Date & Possession:** Target closing date, possession at closing
9. **AS-IS Clause** (if applicable): Property sold in its current condition; seller makes no representations as to condition
10. **Assignment Clause** (if applicable): Buyer reserves the right to assign this agreement to an affiliated entity or third party without seller consent
11. **Subject-To Clause** (if applicable): Buyer acquiring property subject to existing financing remaining in seller's name — full disclosure and attorney review language
12. **Default Provisions:** Buyer default (forfeit EMD), seller default (return EMD + specific performance rights)
13. **Closing Costs:** Allocation between buyer and seller per local custom
14. **Special Provisions:** Any additional terms negotiated by parties
15. **Governing Law:** State of transaction
16. **Entire Agreement / Merger Clause**
17. **Signature Block:** Full execution block for buyer(s) and seller(s)

**Tools / Resources needed:**
None — fully generated from deal inputs.

**Data source:**
Validated deal inputs from Step 1 + state context from Step 2.

**Output of this step:**
Complete formatted PSA document with all 17 sections populated.

**Cowork behavior:**
CONFIRM BEFORE PROCEEDING — present the complete PSA and ask for confirmation before treating it as final. Always remind the user: "⚠️ Have a licensed real estate attorney in [STATE] review this document before execution."

**If this step fails or required data is missing:**
Insert [ATTORNEY INPUT REQUIRED] in any section where the required data was not provided rather than fabricating legal terms.

> 💡 **Precision Note:** The Assignment Clause is investor-critical. Default language: "Buyer shall have the right to assign this Agreement, without Seller's prior written consent, to any entity owned or controlled by Buyer, or to any third party, provided that such assignment shall not relieve Buyer of any obligations hereunder." Include this by default for investor buyers unless the user explicitly requests it be excluded.

---

### Step 5: Flag All Provisions Requiring Attorney Review

**What Claude does:**
Scan the completed document and insert a ⚠️ REVIEW REQUIRED notation adjacent to any of the following provision types:
- Subject-to financing language
- Seller financing terms
- Lease-option or lease-purchase provisions
- Any waiver of mandatory state disclosures
- Default and forfeiture provisions
- Any provision where the user has written custom language not covered by standard templates

At the end of the document, append a consolidated ATTORNEY REVIEW CHECKLIST listing all flagged sections by number.

**Tools / Resources needed:**
None — analytical review of Claude's own generated output.

**Data source:**
Completed document from Steps 3 or 4.

**Output of this step:**
Inline ⚠️ flags + consolidated Attorney Review Checklist appended to document footer.

**Cowork behavior:**
PROCEED WITH ANALYSIS AND DRAFTING — flagging is analytical and does not modify the document's substance.

**If this step fails or required data is missing:**
If the document contains unusual provisions Claude cannot safely evaluate, flag the entire provision: "⚠️ ATTORNEY REVIEW REQUIRED — this provision involves [subject] which requires jurisdiction-specific legal expertise."

---

## 📤 OUTPUT FORMAT

**Output type:** Legal Document (LOI or PSA)  
**Delivery method:** Returned directly in chat — formatted for copy-paste into Google Docs, Word, or DocuSign

---

```
LETTER OF INTENT TO PURCHASE REAL PROPERTY
Date: May 10, 2026

BUYER:  Maple Capital LLC, an Ohio limited liability company
SELLER: John Smith and Mary Smith, husband and wife
PROPERTY: 4821 Maple Ave, Columbus, Ohio 43215
         (Franklin County, Parcel No. 010-123456-00)

This Letter of Intent ("LOI") is submitted by Buyer as an expression
of interest in purchasing the above-referenced property on the
following proposed terms. This LOI is non-binding and is intended
solely to outline the basis for negotiation of a formal Purchase
and Sale Agreement.

1. PURCHASE PRICE: $135,000 (One Hundred Thirty-Five Thousand
   Dollars), payable in cash at closing.

2. EARNEST MONEY: $2,500 deposited with Midland Title & Escrow
   within 3 business days of PSA execution. Fully refundable
   during Due Diligence Period.

3. DUE DILIGENCE PERIOD: 10 business days from PSA execution.
   Buyer may terminate for any reason and receive full EMD refund.

4. FINANCING: All cash — no financing contingency.

5. CLOSING DATE: On or before June 15, 2026.

6. CONDITION: Property purchased AS-IS. Seller makes no
   representations as to property condition.

7. ASSIGNMENT: Buyer reserves the right to assign this agreement
   to any affiliated entity without Seller consent.

8. EXPIRATION: This LOI expires at 5:00 PM Eastern on May 12, 2026
   if not countersigned by Seller.

9. NON-BINDING: This LOI does not constitute a binding contract.
   A fully executed Purchase and Sale Agreement shall govern
   the transaction.

___________________________     Date: __________
Buyer: Maple Capital LLC
By: [Authorized Signatory]

___________________________     Date: __________
Seller: John Smith

___________________________     Date: __________
Seller: Mary Smith

⚠️ ATTORNEY REVIEW: This document was drafted by AI assistant
via Evykynn skill. Have a licensed Ohio real estate attorney
review the final PSA before execution.
```

---

## 🔐 PERMISSIONS & SETUP CHECKLIST

No external permissions or setup required. Attach this file to any Claude.ai chat and type the trigger phrase. This skill runs entirely within Claude's context window.

- [ ] **Optional — DocuSign:** Connect DocuSign API to send the final document for e-signature directly from Cowork. Requires DocuSign account + API key.
- [ ] **Optional — Google Docs:** Paste output into Google Docs for collaborative editing before execution.
- [ ] **Attorney Review:** Budget 30–60 minutes for licensed real estate attorney review before using any PSA in a live transaction.

---

## ✅ QUALITY SELF-CHECK

Before delivering any output, Claude must internally verify every item below:

- [ ] All required inputs were provided or flagged as missing — no fabricated party names, addresses, or terms
- [ ] Document type (LOI vs. PSA) was confirmed with the user before drafting
- [ ] State-specific context was applied and attorney review flag is present
- [ ] All 17 PSA sections (or all 9 LOI sections) are populated — no blank sections
- [ ] Assignment clause is present for investor buyers unless explicitly excluded
- [ ] Zero placeholder text (like "[INSERT NAME]") remains in the final output
- [ ] ⚠️ LEGAL FLAG is present on any non-standard provision
- [ ] Attorney Review Checklist is appended at document footer
- [ ] Output is formatted for immediate copy-paste — no additional editing required

---

## ⚠️ EDGE CASES & ESCALATION RULES

| Scenario | Claude's Exact Response |
|----------|------------------------|
| User requests subject-to language | Draft the subject-to clause AND insert: "⚠️ LEGAL FLAG: Subject-to acquisitions involve significant legal risk — seller's mortgage remains in their name. A real estate attorney in [STATE] must review this provision before execution." |
| User requests waiver of inspection contingency | Include the waiver but flag: "⚠️ Waiving inspection removes your right to terminate based on property condition. Ensure thorough physical due diligence has been completed." |
| Legal description not provided | Use street address only and flag: "⚠️ Legal description not provided — obtain from county recorder or title company and insert before execution." |
| User asks for seller-finance terms | Draft installment purchase language and flag: "⚠️ Seller financing documentation (promissory note, deed of trust/mortgage) must be drafted separately by a real estate attorney." |
| User is in an attorney-review state (NJ, IL, NY, etc.) | Automatically insert 5-business-day attorney review contingency and note: "⚠️ [STATE] standard practice includes an attorney review period — this clause is included by default." |
| User requests document be sent directly to seller | Respond: "I can format this for your delivery, but I cannot send it directly. Copy the document into email, DocuSign, or Google Docs and send from there." |
| Session approaching context limit | Write `_PROGRESS_CHECKPOINT.md` with document type, all inputs collected, and sections completed before session ends |

---

## 📖 DOMAIN GLOSSARY

| Term | Definition |
|------|-----------|
| LOI | Letter of Intent — a non-binding document outlining the proposed terms of a real estate transaction before a formal contract is executed |
| PSA | Purchase and Sale Agreement — the binding contract between buyer and seller detailing price, terms, contingencies, and closing date |
| EMD | Earnest Money Deposit — funds submitted with a purchase offer to demonstrate buyer intent; typically 1–3% of purchase price |
| Contingency | A condition that must be satisfied for the purchase contract to remain binding; common types: inspection, financing, title |
| AS-IS Clause | A provision stating the buyer accepts the property in its current condition without requiring the seller to make repairs |
| Assignment of Contract | The transfer of a purchase contract from the original buyer to a new buyer, with the original buyer earning an assignment fee |
| Subject-To | Acquiring a property "subject to" the existing mortgage remaining in the seller's name — buyer takes title while seller's loan stays in place |
| Governing Law | The clause specifying which state's laws govern the interpretation and enforcement of the contract |
| Merger Clause | A provision stating the written contract supersedes all prior oral or written negotiations and representations |
| Title Commitment | A preliminary report from a title company outlining conditions under which they will issue title insurance |
| Clear-to-Close | Lender confirmation that all underwriting conditions are satisfied and the loan is approved for closing |
| Specific Performance | A legal remedy requiring a defaulting party to fulfill their contractual obligations rather than pay damages |

---

*Authored by Evykynn | Real Estate Agentic Automation*

*Maintained as part of RealtySkills by Evykynn. Example dates and figures are illustrative.*
