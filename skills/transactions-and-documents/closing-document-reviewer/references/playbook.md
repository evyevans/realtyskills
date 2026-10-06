# Source playbook

This playbook supplies task procedures and examples. Follow the working rules in the skill entry, verify current jurisdiction-specific claims, and treat examples as illustrative.

# Closing Document Reviewer

This skill ingests closing disclosure statements, HUD-1 settlement statements, title commitments, deed drafts, and related closing packages — then performs a systematic audit for mathematical errors, fee anomalies, title exceptions, undisclosed encumbrances, and legal red flags. Designed for investors, flippers, and attorneys who cannot afford to close on a deal with an error in the settlement statement or an uncured title defect.

## 🧠 SKILL IDENTITY

**WHO this skill is for:**
A real estate investor, transaction attorney, or active flipper who receives a closing disclosure or settlement statement 24–48 hours before closing and needs a rapid, systematic review to catch mathematical errors, unauthorized fees, title exceptions that weren't disclosed during due diligence, and any provision that could expose them to post-closing liability. Also: a brokerage owner whose commission disbursement authorization (CDA) needs to be verified against the settlement statement.

**WHAT this skill does:**
Produces a structured Closing Document Audit Report containing: a line-by-line fee verification (flagging any charge that deviates from the PSA or loan estimate by more than $50), a mathematical cross-check of all settlement statement totals, a title commitment exception analysis identifying any Schedule B-II exceptions that require action before closing, a deed review for legal description accuracy and vesting, a commission reconciliation, and a prioritized list of issues to resolve before the closing table.

**WHERE to use this skill:**
Paste or upload the closing document text into a Claude.ai chat session (Method A) or Cowork Task (Method B), then type the trigger phrase. Claude works within the 1M token context window — entire multi-document closing packages (CD + title commitment + deed) can be reviewed simultaneously.

**WHEN to activate this skill:**
Activate the moment you receive the closing disclosure from the title company or settlement agent — minimum 24 hours before closing. Never walk into a closing table without running this review. For large multi-property closings, activate 48–72 hours ahead to allow time to cure any title issues.

**WHY this skill matters:**
This workflow makes the required inputs and output structure explicit. Its numerical benchmarks are configurable assumptions, not validated performance claims.

**HOW this skill works (Overview):**
Claude ingests the full closing document package (paste or upload), extracts all line items, identifies the document type (CD, HUD-1, or settlement statement), and performs four sequential audit passes: mathematical verification of all totals, fee legitimacy check against PSA terms, title exception classification, and deed/vesting review. It produces a prioritized findings report — CRITICAL (must resolve before closing) / WARNING (verify before closing) / INFO (note for records) — with specific remediation instructions for each finding.

---

## 📥 REQUIRED INPUTS

| Input | Format | Source | Required? | Example |
|-------|--------|--------|-----------|---------|
| Closing document(s) | Pasted text or uploaded PDF | User provides | Yes | Closing Disclosure, HUD-1, or Settlement Statement |
| Original Purchase and Sale Agreement terms | Pasted text or key fields | User provides | Yes | Purchase price $285,000, seller concessions $5,000, buyer closing costs capped at $8,500 |
| Loan Estimate (if financed) | Pasted text or key figures | User provides | No | LE dated April 15, 2026 showing origination fee of $2,100 |
| Title commitment | Pasted text or uploaded PDF | User provides | No (strongly recommended) | Schedule A + B-I + B-II from title company |
| Commission amounts expected | Dollar amounts | User provides | No | Listing agent: 2.75% ($7,838); buyer agent: 2.75% ($7,838) |
| Closing date | Date | User provides | No | June 15, 2026 |

---

## ⚙️ EXECUTION SOP

### Step 1: Identify Document Types and Extract All Line Items

**What Claude does:**
Read the pasted/uploaded document content and identify which documents are present: Closing Disclosure (CD — TRID-compliant, post-2015), HUD-1 Settlement Statement (pre-2015 or commercial), ALTA Settlement Statement, or a hybrid closing package. Extract every line item from each document into a structured internal table: Section → Line Item → Buyer Amount → Seller Amount → Description.

If multiple documents are present (CD + title commitment + deed), process them as a unified package.

**Tools / Resources needed:**
Claude's 1M token context window — full document text in context. No external API required.

**Data source:**
User-provided document content pasted or uploaded into the chat session.

**Output of this step:**
Internal structured line-item table (used for Steps 2–4). Confirmation message to user: "I've identified [document types] and extracted [N] line items. Beginning audit now."

**Cowork behavior:**
PROCEED WITH ANALYSIS AND DRAFTING — document parsing is analytical and non-destructive.

**If this step fails or required data is missing:**
If the document is a scanned image (non-text PDF), inform the user: "I can read text-based PDFs pasted into this chat. If your document is a scanned image, please type or copy-paste the key line items manually, or use an OCR tool (Adobe Acrobat, Google Drive) to extract the text first."

---

### Step 2: Mathematical Verification of All Totals

**What Claude does:**
For every section of the settlement statement, independently recalculate the subtotals and grand totals from the individual line items. Compare Claude's calculated totals to the document's stated totals. Flag any discrepancy of $1 or more.

Key calculations to verify:
- **Loan charges:** Sum of all Section A–C charges vs. stated total
- **Prepaids:** Per diem interest calculation = (loan balance × rate ÷ 365 × days to first payment)
- **Escrow impounds:** Monthly escrow payment × months in escrow setup, plus initial escrow deposit
- **Prorated property taxes:** (Annual tax ÷ 365) × days seller owned in current tax year
- **Proration HOA dues:** (Monthly HOA ÷ 30) × days in closing month
- **Cash to close (buyer):** Sum of all buyer debits minus all buyer credits
- **Net proceeds (seller):** Purchase price minus payoffs, seller credits, commissions, and seller-side closing costs

**Tools / Resources needed:**
None — arithmetic performed in Claude context.

**Data source:**
Line-item table from Step 1.

**Output of this step:**
Mathematical Verification Table: each section with Claude's calculated total, document's stated total, and variance. Any variance flagged as ⚠️ MATH ERROR.

**Cowork behavior:**
PROCEED WITH ANALYSIS AND DRAFTING — pure calculation, no user action required.

**If this step fails or required data is missing:**
If interest rate or loan balance is not in the document, flag proration as UNVERIFIED and ask the user to provide the loan terms.

> 💡 **Precision Note:** Per diem interest errors are the most common closing statement mistake. Always show the full formula: (Loan Balance × Rate ÷ 365 × Days). A $250K loan at 7% closing on the 15th of a 30-day month = $250,000 × 0.07 ÷ 365 × 16 = $767.12. If the statement shows a materially different amount, flag it before the borrower overpays.

---

### Step 3: Fee Legitimacy Audit Against PSA Terms

**What Claude does:**
Compare every fee on the settlement statement against the user-provided PSA terms. Flag any fee that:
- Appears on the settlement statement but was not disclosed in the PSA or Loan Estimate
- Exceeds the PSA/LE amount by more than $50 (within TRID tolerance rules)
- Is a non-standard fee that requires explanation: "document preparation fee," "settlement fee," "wire transfer fee," "courier fee" — verify these were disclosed
- Represents a seller concession or credit that was agreed in the PSA but is missing from the CD

**Standard closing fee benchmarks by category:**
- Title insurance (lender's policy): 0.3–0.5% of loan amount
- Title insurance (owner's policy): 0.4–0.6% of purchase price
- Settlement/closing fee: $250–$850 depending on state and company
- Recording fees: $100–$300 (state-specific)
- Transfer tax: state-specific rate (e.g., OH = $1/1,000 of purchase price)
- Wire transfer fee: $25–$45

**Tools / Resources needed:**
None — comparison against user-provided PSA terms and embedded benchmark data.

**Data source:**
PSA terms provided by user + line items from Step 1.

**Output of this step:**
Fee Legitimacy Table: each fee with source (PSA-disclosed / LE-disclosed / NEW/UNEXPLAINED), PSA/LE amount, CD amount, and variance flag.

**Cowork behavior:**
PROCEED WITH ANALYSIS AND DRAFTING.

**If this step fails or required data is missing:**
If PSA terms were not provided, perform the fee benchmarking analysis only and flag: "⚠️ PSA terms not provided — fee verification based on industry benchmarks only. Provide your PSA for contract-specific verification."

---

### Step 4: Title Commitment Exception Analysis (if provided)

**What Claude does:**
If a title commitment is included, review Schedule B-II (exceptions to coverage) and classify each exception:

**Exception Classification:**
- **STANDARD/ACCEPTABLE:** Survey exceptions, mineral rights reservations, utility easements disclosed during due diligence, HOA CC&Rs — normal for the property type
- **REQUIRES CURE BEFORE CLOSING:** Existing liens not being paid at closing (judgment liens, tax liens, mechanic's liens), unresolved easements, boundary disputes, unreleased mortgages from prior owners
- **REQUIRES ATTORNEY REVIEW:** Any exception involving a prior deed restriction, reverter clause, environmental covenant, or easement that encumbers the buildable area of the property
- **CRITICAL — DO NOT CLOSE:** Any cloud on title that prevents delivery of marketable title, or a Schedule B-II exception that was not disclosed during the due diligence period

**Tools / Resources needed:**
None — Claude's legal knowledge of title insurance and real property law applied to exception text.

**Data source:**
Title commitment text from user.

**Output of this step:**
Title Exception Classification Table with disposition recommendation for each exception.

**Cowork behavior:**
CONFIRM BEFORE PROCEEDING — if any CRITICAL exception is found, stop and alert the user before completing the rest of the review.

**If this step fails or required data is missing:**
If no title commitment is provided, note: "⚠️ Title commitment not reviewed. Request Schedule B-II from your title company and run this review before closing."

> 💡 **Precision Note:** A "standard" utility easement across the rear 10 feet of a residential lot is acceptable. An easement across the center of a lot intended for development is CRITICAL — it can render the property unbuildable. Read every easement description carefully before classifying.

---

### Step 5: Deed and Vesting Review (if deed draft provided)

**What Claude does:**
If a deed draft is included, verify:
1. **Grantor (seller) name:** Matches exactly the name on the PSA and title commitment
2. **Grantee (buyer) name and vesting:** Matches exactly the buyer entity name; vesting type is correctly stated (tenants in common, joint tenants, LLC, trust, etc.)
3. **Legal description:** Compare to the legal description in the PSA and prior deed — must match character-for-character
4. **Consideration:** Should state the purchase price or a nominal consideration with transfer tax computed on actual value
5. **Notarization and witness requirements:** Confirm the signature block is state-compliant (some states require two witnesses, some require only notarization)
6. **Recording information:** Grantee mailing address for tax bills is correct

**Tools / Resources needed:**
None — document comparison within Claude context.

**Data source:**
Deed draft text from user.

**Output of this step:**
Deed Verification Table with each item checked and any discrepancies flagged.

**Cowork behavior:**
PROCEED WITH ANALYSIS AND DRAFTING.

**If this step fails or required data is missing:**
If the deed draft is not provided, note: "⚠️ Deed draft not reviewed. Request the prepared deed from your title company for review before signing."

---

### Step 6: Assemble and Deliver the Closing Audit Report

**What Claude does:**
Compile all findings from Steps 1–5 into the formatted Closing Document Audit Report (see Output Format). Organize findings by severity: CRITICAL → WARNING → INFO. For each finding, provide: the specific document location (page/section/line), the exact issue, and the specific remediation action required before closing.

**Tools / Resources needed:**
None — assembled from prior steps.

**Data source:**
Steps 1–5 outputs.

**Output of this step:**
Complete formatted Closing Document Audit Report.

**Cowork behavior:**
CONFIRM BEFORE PROCEEDING — if any CRITICAL finding is present, highlight it prominently at the top of the report and ask: "There is at least one CRITICAL issue that should be resolved before you close. Do you want me to draft a resolution request to send to the title company or lender?"

**If this step fails or required data is missing:**
Deliver partial report with missing audit areas clearly labeled as INCOMPLETE and the reason why.

---

## 📤 OUTPUT FORMAT

**Output type:** Closing Document Audit Report  
**Delivery method:** Returned directly in chat — ready to share with transaction coordinator, attorney, or title company

---

```
CLOSING DOCUMENT AUDIT REPORT — Evykynn
Property:      4821 Maple Ave, Columbus OH 43215
Closing Date:  June 15, 2026
Analyst:       AI assistant via Evykynn Skill Library
Documents Reviewed: Closing Disclosure (dated June 10, 2026)
                    Title Commitment (Midland Title, File #2026-4821)

━━━━━━━━━━━━━━━━ SUMMARY ━━━━━━━━━━━━━━━━━━━
CRITICAL Issues:   1  ← MUST RESOLVE BEFORE CLOSING
WARNING Items:     3  ← Verify before closing table
INFO Notes:        2  ← For your records

━━━━━━━━━━━━━━━━ CRITICAL FINDINGS ━━━━━━━━━
[1] UNRESOLVED MECHANIC'S LIEN — TITLE EXCEPTION
    Location: Title Commitment Schedule B-II, Exception #4
    Issue: $8,450 mechanic's lien filed by ABC Roofing Co. on
           03/15/2026 — NOT scheduled for payoff at closing
    Required Action: Contact title company to confirm lien is
    being satisfied from seller proceeds at closing. Obtain
    lien release before funding.
    ⚠️ DO NOT CLOSE until this lien is cured and removed.

━━━━━━━━━━━━━━━━ WARNING ITEMS ━━━━━━━━━━━━
[2] MATH DISCREPANCY — PROPERTY TAX PRORATION
    Location: CD Page 2, Line K.04
    CD States: $1,847.50 seller credit
    Claude Calculates: $1,923.33 [(Annual tax $8,500 ÷ 365) × 82 days]
    Variance: $75.83 overpayment to seller
    Action: Request correction from settlement agent

[3] UNDISCLOSED FEE — "DOCUMENT PREPARATION FEE"
    Location: CD Page 2, Section A, Line A.09
    Amount: $395
    Status: Not disclosed in Loan Estimate (LE dated April 15)
    Action: Request itemization and tolerance cure from lender

[4] SELLER CONCESSION MISSING
    Location: CD Page 3, Section L
    PSA States: Seller to credit buyer $5,000 toward closing costs
    CD Shows: $0 seller credit
    Action: Contact listing agent — concession must appear on CD

━━━━━━━━━━━━━━━━ INFO NOTES ━━━━━━━━━━━━━━━
[5] Owner's Title Policy: $1,140 — within benchmark range ✅
[6] Recording fees: $185 — consistent with Franklin County rate ✅

━━━━━━━━━━━━━━━━ MATHEMATICAL VERIFICATION ━━
Cash to Close (Buyer):
  CD States:       $47,832.19
  Claude Calculates: $47,907.02 (after correcting proration)
  Variance:         $75.83 ⚠️ pending correction

Net Proceeds (Seller):
  CD States:       $131,245.00
  Claude Calculates: $131,320.83 (after correcting proration)
  Variance:         $75.83 (consistent with proration error)

━━━━━━━━━━━━━━━━ RECOMMENDATION ━━━━━━━━━━━━
❌ DO NOT CLOSE until Critical Finding #1 (mechanic's lien) is
   cured and confirmed in writing by title company.
⚠️ Request CD correction from lender/settlement agent for items
   #2, #3, and #4 before closing table.
```

---

## 🔐 PERMISSIONS & SETUP CHECKLIST

No external permissions or setup required. Attach this file to any Claude.ai chat and type the trigger phrase. This skill runs entirely within Claude's context window.

- [ ] **Document Access:** Ensure closing documents are in text format (not scanned image). If scanned, use Adobe Acrobat or Google Drive OCR to extract text before pasting.
- [ ] **Optional — Title Company Portal:** If your title company provides a web portal, copy-paste the settlement statement directly from the portal into the Claude chat.
- [ ] **Attorney Review:** For CRITICAL findings involving title defects, engage a licensed real estate attorney in the transaction state before proceeding.

---

## ✅ QUALITY SELF-CHECK

Before delivering any output, Claude must internally verify every item below:

- [ ] All documents provided by the user were reviewed — none skipped
- [ ] Every mathematical calculation is shown with its formula and inputs visible
- [ ] Every fee on the settlement statement was compared against PSA/LE terms
- [ ] Title exceptions (if commitment provided) are each classified with a disposition
- [ ] CRITICAL findings are placed at the top of the report and highlighted prominently
- [ ] Zero placeholder text remains in the final output
- [ ] ⚠️ flags are present on every finding that requires action before closing
- [ ] Remediation instructions are specific — not "check with title company" but exactly what to say and request

---

## ⚠️ EDGE CASES & ESCALATION RULES

| Scenario | Claude's Exact Response |
|----------|------------------------|
| Document is a scanned image (not text) | "I can review text-based documents. Please use Adobe Acrobat or Google Drive to extract the text, then paste it here." |
| Legal or title defect found | Insert ⚠️ LEGAL FLAG: "This finding may require legal remedy. Consult a licensed real estate attorney in [STATE] before proceeding to closing." |
| Math error exceeds $500 | Flag as CRITICAL and draft a correction request email to the settlement agent on the user's behalf |
| User asks Claude to "approve" the closing | Respond: "I can identify issues for your review, but closing approval is your decision and your attorney's — not mine. Review all CRITICAL and WARNING items before proceeding." |
| Closing disclosure shows terms different from PSA | Flag every discrepancy and ask: "Your CD shows [X] but your PSA states [Y]. Which is correct? This must be reconciled before closing." |
| User has no PSA to provide | Perform benchmark fee analysis and title review only; flag all unverifiable items |
| Session approaching context limit | Write `_PROGRESS_CHECKPOINT.md` with completed steps before context is exhausted |

---

## 📖 DOMAIN GLOSSARY

| Term | Definition |
|------|-----------|
| Closing Disclosure (CD) | A TRID-compliant 5-page document provided to borrowers 3 business days before closing, disclosing all loan terms and closing costs |
| HUD-1 | Pre-2015 settlement statement format; still used in commercial transactions and cash deals |
| ALTA Settlement Statement | The American Land Title Association's closing statement format used for both buyer and seller in many markets |
| Schedule B-II | The section of a title commitment listing exceptions to title insurance coverage — items the title company will not insure |
| Mechanic's Lien | A legal claim against a property filed by a contractor or supplier who was not paid for labor or materials |
| Proration | The allocation of recurring costs (taxes, HOA, rent) between buyer and seller based on their respective days of ownership in the closing period |
| Title Commitment | A preliminary report from a title company outlining the conditions under which they will issue title insurance |
| Loan Estimate (LE) | A TRID-required document provided within 3 days of loan application disclosing estimated loan terms and closing costs |
| TRID | TILA-RESPA Integrated Disclosure rule — the federal regulation governing mortgage disclosure timing and format for residential loans |
| Per Diem Interest | Daily interest accruing on a mortgage from the closing date to the end of the month; prepaid at closing |
| Vesting | The manner in which title to real property is held — determines ownership rights, transfer rules, and estate planning implications |
| Transfer Tax | A state or local tax imposed on the transfer of real property, typically calculated as a dollar amount per $1,000 of sale price |

---

*Authored by Evykynn | Real Estate Agentic Automation*

*Maintained as part of RealtySkills by Evykynn. Example dates and figures are illustrative.*
