# Source playbook

This playbook supplies task procedures and examples. Follow the working rules in the skill entry, verify current jurisdiction-specific claims, and treat examples as illustrative.

# Listing & Buyer-Rep Agreement Drafter

Draft a complete, jurisdiction-aware Exclusive Right to Sell Listing Agreement or Exclusive Buyer Representation Agreement in the time it takes to brew a coffee. This skill ingests seller (or buyer) details, property data, term, commission structure, and authorized actions; produces a clean executable draft mapped to the controlling state form (CAR-RLA, TREC-1101, FAR-BAR ERS, NY Standard Listing, IL-RES Listing); and generates a parallel redline showing precisely which provisions were customized versus which remain boilerplate. Every output includes a one-page seller-friendly summary the agent can read aloud at the kitchen table, plus a brokerage-policy compliance flag set the supervising broker can scan in under sixty seconds.

**Important Disclaimer:** This skill provides drafting and analytical support for licensed real estate professionals and the attorneys who advise them. It does not constitute legal advice. Final review by a licensed real estate attorney is recommended for any non-standard term, any seller in financial distress, any party not present at signing, and any transaction crossing state lines.

## 🧠 SKILL IDENTITY

**WHO this skill is for:**
A team lead onboarding a new listing at 9pm before a 7am presentation, who needs the agreement, the redline, and the seller summary on the kitchen counter by morning. A high-volume independent agent running 80+ listings a year who cannot afford to retype the same seventeen brokerage-policy clauses. A brokerage owner reviewing junior agents' listing packages for compliance before they hit the MLS. A transaction attorney pre-screening agreements for clients before billing partner-rate review hours — the skill output gives the attorney a structured, redlined starting point rather than a blank page.

**WHAT this skill does:**
Generates a fully executable Exclusive Right to Sell Listing Agreement OR Exclusive Buyer Representation Agreement, mapped to the user's named state-form template, with all parties, property identifiers, term, commission structure, authorized marketing actions, and state-mandatory disclosures pre-filled. Produces a redline overlay showing what was customized away from the state-form boilerplate and a separate compliance memo flagging any term that deviates from typical brokerage policy or post-NAR-Settlement (August 2024) buyer-broker compensation rules. Also outputs a one-page plain-language summary for the seller and a separate "supervising broker review" cover sheet listing every flag the broker must clear before the agreement is signed.

**WHERE to use this skill:**
Standalone Claude.ai chat for one-off listings — the agent attaches the .md, types the trigger phrase, and walks through a four-question intake. Cowork Task when a team lead has a stack of new listings to process in batch (each listing becomes its own subfolder, each with its draft, redline, summary, and broker review sheet). Claude.ai Project for brokerage-wide deployment, where every agent on the team activates the same skill via the trigger phrase and the office manager periodically updates the brokerage-policy block in the Project's knowledge base.

**WHEN to activate this skill:**
The instant a seller (or buyer) verbally commits — before the listing presentation hardens into a signed agreement. Also when a competing brokerage's draft arrives and the user needs to compare it side-by-side against their own brokerage's standard. Also at the moment a referral partner sends a buyer agreement to be signed, and the agent needs to validate that the document matches the state form rather than a non-standard out-of-state template. Also during quarterly brokerage compliance audits, when the broker of record runs the skill against a sample of executed agreements to confirm policy adherence.

**WHY this skill matters:**
This workflow makes the required inputs and output structure explicit. Its numerical benchmarks are configurable assumptions, not validated performance claims.

**HOW this skill works (Overview):**
Claude confirms jurisdiction and state-form template; collects parties, property, term, commission, and authorized-action data via a structured four-question intake; cross-references state-mandatory disclosures and NAR-Settlement compensation rules; drafts the full agreement using the named state form's section numbering as anchors; runs a brokerage-policy compliance pass; generates a parallel redline showing customized versus boilerplate language; and emits four artifacts: the executable draft, the redline, the one-page seller summary, and the supervising broker review cover sheet. Every flagged item carries a `⚠️` tag and references the exact section number from the controlling state form.

## 📥 REQUIRED INPUTS

| Input | Format | Source | Required? | Example |
|---|---|---|---|---|
| `agreement_type` | string | User selects | Yes | `listing_agreement` or `buyer_representation` |
| `state` | string (2-letter) | User states | Yes | `CA`, `TX`, `FL`, `NY`, `IL`, or other (flagged generic) |
| `state_form_template` | string | User selects | Yes | `CAR-RLA`, `TREC-1101`, `FAR-BAR-ERS`, `NY-STD-LIST`, `IL-RES-LIST` |
| `seller_name` (or `buyer_name`) | string | User provides | Yes | `Maria E. Hernandez and Carlos J. Hernandez, husband and wife` |
| `seller_legal_capacity` | string | User states | Yes | `joint tenants`, `community property with right of survivorship`, `tenants in common`, `trust`, `LLC`, `estate` |
| `property_address` | string | User provides | Yes (listing) | `2418 Sunnybrook Lane, Austin, TX 78745` |
| `property_apn` | string | County records | Yes (listing) | `0312-04-2200-0019` |
| `property_legal_description` | string | Title or deed | Yes (listing) | `Lot 19, Block 22, Sunnybrook Section Three, City of Austin, Travis County, Texas` |
| `mls_number` | string | MLS upon listing | No | `TX-1924871` (assigned post-execution) |
| `brokerage_name` | string | User provides | Yes | `Hernandez Realty Group, LLC` |
| `brokerage_license_number` | string | User provides | Yes | `TX-9001482` |
| `agent_name` | string | User provides | Yes | `Maria E. Hernandez` |
| `agent_mls_id` | string | User provides | Yes | `MLS-AGT-42119` |
| `supervising_broker_name` | string | User provides | Yes | `Robert M. Patel` |
| `term_start_date` | date (ISO) | User provides | Yes | `2026-05-15` |
| `term_end_date` | date (ISO) | User provides | Yes | `2026-11-15` |
| `protected_period_days` | integer | User provides | Yes | `90` (typical 60–180) |
| `listing_commission_total_pct` | decimal | User provides | Yes (listing) | `5.0` |
| `commission_to_buyer_broker_pct` | decimal | User provides | Yes (listing, post-NAR) | `2.5` (post-Aug-2024: must be negotiated separately and documented) |
| `commission_floor_dollars` | integer | Brokerage policy | No | `7500` (minimum fee floor) |
| `authorized_actions` | list | User provides | Yes | `["MLS","lockbox","yard_sign","photography","virtual_tour","drone","open_house"]` |
| `seller_disclosures_completed` | boolean | User confirms | Yes (listing) | `true` if state SPD/TDS package is complete |
| `dual_agency_consent` | boolean | User confirms | Yes | `true` or `false` (CA requires written consent on CAR-AD) |
| `attorneys_fees_clause` | boolean | User selects | Yes | `true` (recommended) |
| `brokerage_policy_overrides` | text | Optional | No | `e.g., minimum 4% gross commission; no net listings; no rebates >1% in TX` |

## ⚙️ EXECUTION SOP

### Step 1: Confirm Jurisdiction and State-Form Template

**What Claude does:** Confirms the controlling state and selects the matching form template (CAR-RLA for California listings, TREC-1101 for Texas, FAR-BAR ERS for Florida, NY Standard Listing for New York, IL-RES Listing for Illinois). If the state falls outside the named top-five, Claude explicitly switches to a generic national listing template and inserts a `⚠️ NON-STANDARD JURISDICTION` banner instructing the user to have local counsel review every disclosure block.
**Tools / Resources needed:** Internal state-form mapping table; state-bar published form library (e.g., car.org, trec.texas.gov, floridarealtors.org, NYSAR forms, IAR forms).
**Data source:** User-provided `state` and `state_form_template` fields.
**Output of this step:** A confirmed `[STATE: XX]` tag and a confirmed form ID that anchors all subsequent section references.
**Cowork behavior:** PROCEED WITH ANALYSIS AND DRAFTING (after user confirms state once).
**Fallback:** If the user names a form Claude does not recognize, Claude lists the five supported forms and asks the user to select the closest match or explicitly select `generic`. Claude does not invent a form.

> 💡 **Precision Note:** Section numbering varies materially between state forms. CAR-RLA paragraphs are numbered 1–22; TREC-1101 uses Section A–N; FAR-BAR ERS uses paragraphs 1–24 with sub-letters. Claude must match the exact numbering of the controlling form so the agent and the seller can cross-reference the draft against the official blank.

### Step 2: Collect and Validate Parties

**What Claude does:** Collects the full legal name(s) of the seller (or buyer), the legal capacity in which they hold (or will take) title, and the brokerage / agent / MLS / license identifiers. Validates that all signatories with a recorded interest are present — flags joint tenancy, community property with right of survivorship, tenants in common, trust trustees, LLC managing members, and estates with executor/administrator language.
**Tools / Resources needed:** County recorder data (if available); brokerage roster; agent's state license database lookup.
**Data source:** User-provided seller/buyer name, capacity, and brokerage identifiers.
**Output of this step:** A normalized "Parties" block with each signatory's full legal name, capacity, address, and required signature line.
**Cowork behavior:** CONFIRM BEFORE PROCEEDING — show the user the full Parties block before continuing, so missing co-owners are caught before the draft is generated.
**Fallback:** If the user lists only one seller on a property held in joint tenancy or community property, Claude refuses to proceed and asks for the second signatory. Spousal absence on a community-property listing in CA, TX, AZ, NM, NV, ID, LA, WA, WI is a CRITICAL flag.

> 💡 **Precision Note:** A listing agreement signed by only one spouse on a community-property home is unenforceable as to the absent spouse's interest. If the seller insists, Claude inserts a `⚠️ SPOUSAL CONSENT REQUIRED` banner and a deferred-signature line, but does not generate a clean draft.

### Step 3: Capture Subject Property Identification

**What Claude does:** Records the street address, county, APN/parcel number, lot/block/subdivision legal description, and (if assigned) MLS number. Cross-checks the legal description format against state norms — Texas uses lot/block/section; California typically uses lot/tract/map book/page; Florida uses condominium declaration references for condos; NY uses metes-and-bounds for unincorporated areas.
**Tools / Resources needed:** Title commitment if available; county assessor / recorder portal; existing deed copy if seller provides.
**Data source:** User-provided property address, APN, legal description.
**Output of this step:** A property identification block ready to drop into the agreement's "Premises" or "Property" paragraph.
**Cowork behavior:** PROCEED WITH ANALYSIS AND DRAFTING.
**Fallback:** If the user provides only a street address with no APN or legal description, Claude inserts a placeholder marked `⚠️ LEGAL DESCRIPTION TO BE CONFIRMED FROM TITLE COMMITMENT` and instructs the agent to obtain the legal description from the preliminary title report before signing.

> 💡 **Precision Note:** A street address alone is insufficient to convey or list real property in most states. The legal description is the controlling identifier. Skipping this is a documented source of post-closing disputes (parcel mis-identification, especially on rural multi-parcel holdings).

### Step 4: Set Term and Protected Period

**What Claude does:** Records the term start and end dates and the post-expiration protected period (typically 60–180 days; 90 days is the median in the named top-five states). Validates that the protected period does not exceed state caps where a cap exists (some state real estate commissions consider periods over 180 days unconscionable).
**Tools / Resources needed:** State real estate commission rules on protected-period maximums; brokerage policy.
**Data source:** User-provided term dates and protected-period days.
**Output of this step:** A "Term" paragraph with start, end, and protected period clearly stated.
**Cowork behavior:** PROCEED WITH ANALYSIS AND DRAFTING.
**Fallback:** If the user requests a protected period over 180 days, Claude inserts a `⚠️ EXTENDED PROTECTED PERIOD — BROKERAGE REVIEW REQUIRED` flag, generates the clause, and routes to the supervising broker review sheet.

> 💡 **Precision Note:** The protected period is the post-expiration window during which the listing agent retains commission rights if a buyer previously introduced to the property closes. To enforce, the agent must register the prospective buyer's name in writing with the seller before expiration. Claude includes a registration-list provision by default.

### Step 5: Set Commission Structure (Post-NAR-Settlement Compliant)

**What Claude does:** Records the total listing-side commission percentage, the dollar floor (if any), and — separately and explicitly — the buyer-broker compensation amount. Per the NAR Settlement effective August 17, 2024, the buyer-broker compensation must be a separately negotiated and separately documented term. Claude does NOT default to "total commission split equally between sides" without an express seller decision.
**Tools / Resources needed:** Brokerage commission policy; NAR Settlement compliance bulletin (post-Aug-2024); state-bar guidance on compensation disclosure.
**Data source:** User-provided commission percentages and floor.
**Output of this step:** A "Compensation" paragraph showing total listing-side commission, separately stated buyer-broker compensation (if any), and floor.
**Cowork behavior:** CONFIRM BEFORE PROCEEDING — explicitly surface the post-NAR-Settlement compensation language for the user to confirm.
**Fallback:** If the seller declines to offer any buyer-broker compensation, Claude generates a clean "Seller offers no compensation to buyer's broker; buyer's broker compensation, if any, is the responsibility of the buyer" clause and inserts a `⚠️ BUYER-BROKER COMPENSATION = $0` advisory in the seller summary.

> 💡 **Precision Note:** A "below-floor" commission request (under 4% in most markets) is a CRITICAL flag. Claude either declines to draft below the brokerage floor, or surfaces an "exception requested" flag routing to the supervising broker. The skill does not silently lower the commission floor.

### Step 6: Configure Authorized Actions

**What Claude does:** Records each authorized marketing action — MLS submission, lockbox, yard sign, photography, virtual tour, drone footage, open houses, social media — and matches each to the state form's checkbox or initial-line equivalents. Also captures any specifically prohibited actions (e.g., "no drone over neighbor's property", "no sign for first 30 days", "do not photograph children's bedrooms").
**Tools / Resources needed:** State form's authorized-actions paragraph; brokerage policy on drone/aerial photography (FAA Part 107 considerations).
**Data source:** User-provided `authorized_actions` list and any prohibitions.
**Output of this step:** A populated "Authorized Actions" / "Marketing" paragraph with affirmative grants and explicit exclusions.
**Cowork behavior:** PROCEED WITH ANALYSIS AND DRAFTING.
**Fallback:** If the seller authorizes drone footage but the user has not provided FAA Part 107 pilot certification status, Claude inserts a `⚠️ FAA Part 107 CERTIFICATION REQUIRED` advisory.

> 💡 **Precision Note:** Authorizing MLS submission also typically authorizes IDX syndication and downstream display on Zillow, Redfin, and Realtor.com. If the seller objects to syndication, Claude must generate a "MLS submission with IDX opt-out" clause and confirm the local MLS supports the opt-out (Bright MLS, MRED, NTREIS, CRMLS, and most major MLSs do).

### Step 7: Insert State-Mandatory Disclosures

**What Claude does:** Inserts the state-mandatory disclosure block. CA: agency relationship disclosure (CAR-AD), Transfer Disclosure Statement (TDS), Natural Hazard Disclosure (NHD), AVID, Megan's Law, Lead-Based Paint (pre-1978). TX: TREC Information About Brokerage Services (IABS), Seller's Disclosure Notice, Lead-Based Paint, MUD/PID notices where applicable. FL: single-agent vs transaction-broker notice, condo pre-sale disclosure (FS 718) for condos, hurricane / wind-mitigation, lead-based paint. NY: NY Disclosure Form, lead-based paint, property condition disclosure (PCD) or $500 statutory credit. IL: Illinois Residential Real Property Disclosure Report, radon disclosure, lead-based paint, Cook County / Chicago additional ordinances where applicable.
**Tools / Resources needed:** Current state-form library; HUD lead-based paint pamphlet "Protect Your Family From Lead in Your Home"; state real estate commission disclosure-form library.
**Data source:** User-confirmed `seller_disclosures_completed` flag plus property year-built (for lead-based paint trigger).
**Output of this step:** A complete "Disclosures" section with each required form named, attached, and cross-referenced.
**Cowork behavior:** CONFIRM BEFORE PROCEEDING — show the user the disclosure list and confirm each is in hand or on the way.
**Fallback:** If a state-mandatory disclosure is missing, Claude inserts a `⚠️ DISCLOSURE NOT YET COMPLETED — HOLD SIGNATURE` flag and does NOT mark the agreement ready to sign.

> 💡 **Precision Note:** The federal Lead-Based Paint Disclosure (24 CFR Part 35, 40 CFR Part 745) applies to ALL pre-1978 housing nationwide. Penalties run up to ~$22,500 per violation. Claude flags every pre-1978 build automatically.

### Step 8: Add Cancellation, Termination, and Attorneys'-Fees Clauses

**What Claude does:** Adds the brokerage's standard cancellation provisions (mutual termination on written notice; seller-only cancellation rights are rare and brokerage-policy-driven), a holdover clause covering buyers introduced during term, mediation/arbitration provisions where required by the state form (CA-RLA paragraph 22 mediation/arbitration is mandatory; TREC includes mediation), and an attorneys'-fees clause (default: prevailing-party recovery).
**Tools / Resources needed:** State form mediation/arbitration paragraph; brokerage policy on cancellation.
**Data source:** User selection on `attorneys_fees_clause` and brokerage policy.
**Output of this step:** A "Termination, Mediation, and Attorneys' Fees" block fully populated.
**Cowork behavior:** PROCEED WITH ANALYSIS AND DRAFTING.
**Fallback:** If the seller demands a unilateral cancellation right, Claude inserts a `⚠️ NON-STANDARD CANCELLATION TERM — BROKERAGE REVIEW REQUIRED` flag and routes to the supervising broker.

> 💡 **Precision Note:** Mediation provisions in CAR-RLA (paragraph 22) and TREC (Section M) are typically initialed by both sides; arbitration is a separate election. Skipping the initial line on the controlling state form is a documented enforceability issue.

### Step 9: Run State-Specific Compliance Pass

**What Claude does:** Runs a final state-specific compliance check covering: agency disclosure form is attached and acknowledged (CA-AD, TX-IABS, FL single-agent notice, NY Disclosure Form, IL Disclosure); fair-housing notice is included; brokerage compensation is stated separately from buyer-broker compensation (post-NAR-Settlement); MLS Clear Cooperation Policy is acknowledged; brokerage license number and supervising broker name are present.
**Tools / Resources needed:** State-bar compliance checklists; NAR Code of Ethics; HUD fair-housing equal-opportunity logo and statement.
**Data source:** Steps 1–8 outputs.
**Output of this step:** A `[STATE: XX] COMPLIANCE PASS — N FLAGS RESOLVED, M FLAGS ESCALATED` summary line.
**Cowork behavior:** PROCEED WITH ANALYSIS AND DRAFTING.
**Fallback:** Any unresolved CRITICAL flag halts delivery. Claude lists the unresolved flags and the specific cure required for each.

> 💡 **Precision Note:** The skill never silently passes a compliance flag. Every flag is either resolved (with citation) or escalated to the supervising broker review sheet.

### Step 10: Generate Redline Against State-Form Template

**What Claude does:** Produces a parallel-column redline showing the state-form boilerplate text on the left and the customized text on the right, with insertions in **green-bold** notation `{+ INSERTED +}` and deletions in **red-strikethrough** notation `{- DELETED -}`. The redline gives the supervising broker and the seller a one-glance view of every customization.
**Tools / Resources needed:** State-form blank as anchor; redline diff logic.
**Data source:** Steps 1–9 outputs.
**Output of this step:** A redline document keyed by paragraph number to the state form.
**Cowork behavior:** PROCEED WITH ANALYSIS AND DRAFTING.
**Fallback:** If the redline cannot anchor a customized clause to a paragraph in the state form (i.e., the clause is non-standard), Claude flags it as a `[NEW CLAUSE — NO STATE-FORM ANALOG]` and lists it in the supervising broker review sheet.

> 💡 **Precision Note:** Redlines must always be keyed by paragraph number to the controlling form so the broker can spot-check in seconds. Free-text redlines without anchor numbers are operationally useless.

### Step 11: Produce Seller Summary and Broker Review Sheet

**What Claude does:** Generates two ancillary outputs: (1) a one-page plain-language seller summary the agent can read aloud at the kitchen table, hitting term, commission, post-NAR-Settlement buyer-broker compensation, protected period, key disclosures, and cancellation rights; (2) a supervising broker review cover sheet listing every `⚠️` flag with the specific cure required and a sign-off line.
**Tools / Resources needed:** Plain-language style guide (Flesch-Kincaid grade 8 target for seller summary).
**Data source:** Steps 1–10 outputs.
**Output of this step:** Two documents — `seller_summary.md` and `broker_review.md`.
**Cowork behavior:** PROCEED WITH ANALYSIS AND DRAFTING.
**Fallback:** If any term cannot be expressed at grade 8, Claude flags it and offers a glossary entry.

> 💡 **Precision Note:** The seller summary is the difference between an executed agreement and an awkward kitchen-table moment. Claude never lets this slide to a footnote.

### Step 12: Final Self-Check and Deliver

**What Claude does:** Runs the Quality Self-Check below before delivering. Verifies zero placeholder text, every signature line is named, every disclosure is attached or flagged, every flag is escalated or cleared, and every `[STATE: XX]` reference resolves.
**Tools / Resources needed:** Quality Self-Check rubric.
**Data source:** All prior steps.
**Output of this step:** Four artifacts delivered to the user — the executable draft, the redline, the seller summary, the broker review sheet.
**Cowork behavior:** PROCEED WITH ANALYSIS AND DRAFTING.
**Fallback:** Any failed Self-Check item halts delivery and surfaces the specific failure to the user.

> 💡 **Precision Note:** Drafts that pass nine of ten checks but fail one are not delivered. The standard is 10 of 10.

## 💻 CODE EXAMPLE

```python
"""
Listing Agreement Term Validator
Cross-checks listing terms against state-specific minimums and brokerage policy.
Returns pass/fail with structured issue list.
"""
from datetime import date, timedelta
from typing import TypedDict

class TermValidationIssue(TypedDict):
    severity: str          # "INFO", "WARN", "CRITICAL"
    code: str              # short code, e.g., "COMM_BELOW_FLOOR"
    message: str           # human-readable
    state_citation: str    # e.g., "TX OC §1101.652(b)(20)"

# State-specific commission floors and protected-period caps
STATE_RULES = {
    "CA": {"min_commission_pct": 4.0, "max_protected_days": 180,
           "form": "CAR-RLA", "agency_form": "CAR-AD"},
    "TX": {"min_commission_pct": 4.0, "max_protected_days": 180,
           "form": "TREC-1101", "agency_form": "TREC-IABS"},
    "FL": {"min_commission_pct": 4.0, "max_protected_days": 180,
           "form": "FAR-BAR-ERS", "agency_form": "FL-SA-NOTICE"},
    "NY": {"min_commission_pct": 4.0, "max_protected_days": 180,
           "form": "NY-STD-LIST", "agency_form": "NY-DISCLOSURE"},
    "IL": {"min_commission_pct": 4.0, "max_protected_days": 180,
           "form": "IL-RES-LIST", "agency_form": "IL-DISCLOSURE"},
}

def validate_listing_terms(terms: dict, state: str) -> dict:
    """
    terms: {
        listing_commission_total_pct: float,
        commission_to_buyer_broker_pct: float,
        term_start: date,
        term_end: date,
        protected_period_days: int,
        property_year_built: int,
        seller_count: int,
        community_property: bool,
        spousal_signatures_present: bool,
        nar_settlement_compensation_documented: bool,
    }
    """
    issues: list[TermValidationIssue] = []
    rules = STATE_RULES.get(state.upper())
    if not rules:
        issues.append({
            "severity": "WARN",
            "code": "STATE_NOT_TOP_FIVE",
            "message": (f"State {state} not in top-five mapped jurisdictions. "
                        "Generic template will be used; local counsel review required."),
            "state_citation": "N/A",
        })
        return {"pass": False, "issues": issues}

    # Commission floor
    if terms["listing_commission_total_pct"] < rules["min_commission_pct"]:
        issues.append({
            "severity": "CRITICAL",
            "code": "COMM_BELOW_FLOOR",
            "message": (f"Listing commission {terms['listing_commission_total_pct']}% "
                        f"is below brokerage floor of {rules['min_commission_pct']}%. "
                        "Requires brokerage exception or decline-to-list."),
            "state_citation": f"{state} brokerage policy",
        })

    # Term length
    term_days = (terms["term_end"] - terms["term_start"]).days
    if term_days < 30:
        issues.append({
            "severity": "WARN",
            "code": "TERM_TOO_SHORT",
            "message": f"Term of {term_days} days is below typical 90-day minimum.",
            "state_citation": "Industry norm",
        })

    # Protected period cap
    if terms["protected_period_days"] > rules["max_protected_days"]:
        issues.append({
            "severity": "CRITICAL",
            "code": "PROTECTED_TOO_LONG",
            "message": (f"Protected period of {terms['protected_period_days']} days "
                        f"exceeds {state} cap of {rules['max_protected_days']} days. "
                        "Risk of unconscionability finding."),
            "state_citation": f"{state} real estate commission guidance",
        })

    # NAR Settlement compliance
    if not terms.get("nar_settlement_compensation_documented", False):
        issues.append({
            "severity": "CRITICAL",
            "code": "NAR_SETTLEMENT_NONCOMPLIANT",
            "message": ("Buyer-broker compensation must be separately negotiated and "
                        "documented per NAR Settlement effective Aug 17, 2024."),
            "state_citation": "NAR Settlement Order, MDL No. 3010",
        })

    # Lead-based paint
    if terms["property_year_built"] < 1978:
        issues.append({
            "severity": "INFO",
            "code": "LEAD_PAINT_DISCLOSURE_REQUIRED",
            "message": ("Pre-1978 build — federal Lead-Based Paint Disclosure required. "
                        "HUD pamphlet 'Protect Your Family From Lead' must be delivered."),
            "state_citation": "24 CFR Part 35; 40 CFR Part 745",
        })

    # Spousal consent on community-property states
    if state.upper() in ("CA", "TX", "AZ", "NM", "NV", "ID", "LA", "WA", "WI"):
        if terms.get("community_property") and not terms.get("spousal_signatures_present"):
            issues.append({
                "severity": "CRITICAL",
                "code": "SPOUSAL_CONSENT_MISSING",
                "message": ("Community-property state and spousal signature missing. "
                            "Agreement is unenforceable as to absent spouse's interest."),
                "state_citation": f"{state} community property statute",
            })

    has_critical = any(i["severity"] == "CRITICAL" for i in issues)
    return {"pass": not has_critical, "issues": issues, "rules_applied": rules}


# Example usage
if __name__ == "__main__":
    sample_terms = {
        "listing_commission_total_pct": 5.0,
        "commission_to_buyer_broker_pct": 2.5,
        "term_start": date(2026, 5, 15),
        "term_end": date(2026, 11, 15),
        "protected_period_days": 90,
        "property_year_built": 1972,
        "seller_count": 2,
        "community_property": True,
        "spousal_signatures_present": True,
        "nar_settlement_compensation_documented": True,
    }
    result = validate_listing_terms(sample_terms, "TX")
    print(f"Pass: {result['pass']}")
    for issue in result["issues"]:
        print(f"  [{issue['severity']}] {issue['code']}: {issue['message']}")
    # Expected:
    # Pass: True
    # [INFO] LEAD_PAINT_DISCLOSURE_REQUIRED: Pre-1978 build — federal Lead-Based Paint Disclosure required.
```

## 📤 OUTPUT FORMAT

**Type:** Markdown package containing four artifacts — `01_executable_draft.md`, `02_redline.md`, `03_seller_summary.md`, `04_broker_review.md`.
**Delivery:** All four artifacts displayed inline in chat (Method A) or written to the Cowork session folder (Method B). For Claude.ai Project deployment, the artifacts are produced as Project artifacts the team can fork.

### EXAMPLE OUTPUT

```
=========================================================
ARTIFACT 1 — EXECUTABLE DRAFT
=========================================================

EXCLUSIVE RIGHT TO SELL LISTING AGREEMENT
[STATE: TX] [FORM: TREC-1101 derived; brokerage-policy customized]

This Exclusive Right to Sell Listing Agreement ("Agreement") is entered into
on May 15, 2026, by and between:

SELLER(S):
  Maria E. Hernandez and Carlos J. Hernandez, husband and wife,
  holding title as community property with right of survivorship,
  whose address is 2418 Sunnybrook Lane, Austin, TX 78745.

BROKER:
  Hernandez Realty Group, LLC, Texas brokerage license no. TX-9001482,
  acting through its supervising broker Robert M. Patel,
  with the assistance of associated agent Maria E. Hernandez (MLS-AGT-42119).

1. PROPERTY (TREC-1101 §A)
   Street address: 2418 Sunnybrook Lane, Austin, TX 78745
   APN/Parcel: 0312-04-2200-0019
   Legal description: Lot 19, Block 22, Sunnybrook Section Three,
     City of Austin, Travis County, Texas, according to the map or plat
     thereof recorded in Cabinet 84, Slide 119, Plat Records of Travis County.

2. TERM (TREC-1101 §B)
   Start: May 15, 2026.  End: November 15, 2026.
   Protected period: 90 days post-expiration. Broker shall deliver to Seller,
   on or before the End date, a written list of prospective buyers introduced
   to the Property during the Term ("Registered Prospects List"). Commission
   is owed if a Registered Prospect closes within the protected period.

3. COMPENSATION (TREC-1101 §H — modified per NAR Settlement effective Aug 17, 2024)
   3.1 Listing-side commission to Broker: 5.0% of gross sales price,
       subject to a floor of $7,500.
   3.2 Buyer-broker compensation: Seller authorizes Broker to offer
       2.5% of gross sales price to a cooperating buyer's broker,
       payable at closing through the title company.
   3.3 Buyer-broker compensation is a separately negotiated term and is
       not a condition of MLS submission. Seller may revoke this offer at
       any time by written notice, subject to commission already earned.

4. AUTHORIZED ACTIONS (TREC-1101 §F, customized)
   Seller authorizes Broker to:
   [X] submit Property to Austin Board of Realtors MLS (ABoR/ACTRIS)
   [X] place a lockbox on the Property
   [X] place a yard sign
   [X] commission professional photography
   [X] commission a 3D virtual tour
   [X] commission drone exterior footage (FAA Part 107 pilot to be retained)
   [X] hold open houses, with Seller's pre-approval of dates
   [ ] (not authorized) photograph interior of children's bedrooms

5. STATE-MANDATORY DISCLOSURES (TREC-1101 §J + statutory schedule)
   5.1 TREC Information About Brokerage Services (IABS) — provided to Seller
       on May 14, 2026; signed acknowledgment attached as Exhibit A.
   5.2 Seller's Disclosure Notice — completed by Seller on May 13, 2026;
       attached as Exhibit B.
   5.3 Federal Lead-Based Paint Disclosure (Property pre-dates 1978):
       Property year built: 1972. Lead-Based Paint Disclosure (24 CFR Part 35;
       40 CFR Part 745) attached as Exhibit C. HUD pamphlet "Protect Your
       Family From Lead in Your Home" delivered to Seller.
   5.4 Notice of any MUD/PID jurisdiction: Property is NOT located within
       a Municipal Utility District or Public Improvement District.
   5.5 Fair Housing notice: Property to be marketed in compliance with the
       Fair Housing Act (42 U.S.C. §§3601–3619) and all state/local
       analogues. Equal Housing Opportunity logo to appear on all marketing.

6. AGENCY RELATIONSHIP (Texas: intermediary status governs)
   Broker shall act as an Intermediary as that term is defined in
   Tex. Occ. Code §1101.559 in any transaction in which Broker also
   represents the buyer. Broker shall obtain written consent of all
   parties before acting as Intermediary. Broker may not act as a "dual
   agent" in Texas; the Intermediary status replaces dual agency.

7. CANCELLATION, MEDIATION, ATTORNEYS' FEES (TREC-1101 §M, customized)
   7.1 Either party may terminate this Agreement upon mutual written
       consent. Unilateral termination by Seller is not permitted absent
       material breach by Broker.
   7.2 Mediation: The parties shall mediate any dispute arising out of
       this Agreement before resorting to litigation, with a mediator
       mutually selected.
   7.3 Attorneys' Fees: In any dispute arising out of this Agreement,
       the prevailing party shall recover reasonable attorneys' fees
       and costs from the non-prevailing party.

8. SIGNATURES
   _______________________________  Date: __________
   Maria E. Hernandez, Seller

   _______________________________  Date: __________
   Carlos J. Hernandez, Seller

   _______________________________  Date: __________
   Maria E. Hernandez, Associated Agent (MLS-AGT-42119)

   _______________________________  Date: __________
   Robert M. Patel, Supervising Broker
   Hernandez Realty Group, LLC (TX-9001482)

=========================================================
ARTIFACT 2 — REDLINE (KEYED TO TREC-1101 PARAGRAPH NUMBERS)
=========================================================

§A PROPERTY
  STATE FORM: "Address: ________  Legal Description: ________"
  CUSTOMIZED: {+ Address, APN, and full lot/block/subdivision legal
              description inserted; map/plat cabinet/slide cited +}

§B TERM
  STATE FORM: "Begins ____ and Ends at 11:59 p.m. on ____.
              Protection period of ____ days."
  CUSTOMIZED: {+ Start: 2026-05-15. End: 2026-11-15. Protected
              period: 90 days. Registered Prospects List provision
              ADDED to specify written-registration mechanism. +}

§F AUTHORIZED ACTIONS
  STATE FORM: Generic checkbox list.
  CUSTOMIZED: {+ Drone footage authorized subject to FAA Part 107 pilot;
              prohibition on photographing children's bedrooms ADDED. +}

§H COMPENSATION
  STATE FORM: "Listing-side: ___%. Cooperating broker: ___%."
  CUSTOMIZED: {+ Listing-side 5.0% / floor $7,500. Cooperating broker
              2.5%. NAR-Settlement compliance language ADDED stating
              compensation is separately negotiated and revocable. +}

§J DISCLOSURES
  STATE FORM: Generic disclosure attachment list.
  CUSTOMIZED: {+ IABS, Seller Disclosure Notice, Lead-Based Paint
              Disclosure, MUD/PID notice, Fair Housing notice
              individually itemized as Exhibits A–C plus statutory
              attachments. +}

§M MEDIATION & ATTORNEYS' FEES
  STATE FORM: "Mediation initialed by both parties: ___"
  CUSTOMIZED: {+ Mediation mandatory pre-litigation; prevailing-party
              attorneys' fees clause ADDED. +}

NEW (NO STATE-FORM ANALOG):
  + Spousal consent confirmation block (community-property compliance)

=========================================================
ARTIFACT 3 — SELLER SUMMARY (ONE PAGE, GRADE-8 PLAIN LANGUAGE)
=========================================================

YOUR LISTING AGREEMENT — PLAIN-LANGUAGE SUMMARY

Property: 2418 Sunnybrook Lane, Austin, TX 78745
Brokerage: Hernandez Realty Group, LLC

WHAT YOU ARE AGREEING TO:
- We will list your home from May 15 to November 15, 2026 (six months).
- You will pay us 5% of the sale price (minimum $7,500 if the sale is small).
- Out of that, we will offer 2.5% to the buyer's agent. Per the NAR
  Settlement that took effect August 17, 2024, this is a separate decision
  you are making, and you can change it at any time in writing.
- For 90 days after the listing ends, you still owe commission if anyone
  we showed the home to during the listing buys it. We will give you a
  written list of those buyers.
- You authorize us to put it on the MLS, place a sign and lockbox, take
  professional photos and a 3D tour, fly a drone for exterior shots, and
  hold open houses you approve in advance.
- You have given us your Texas Seller's Disclosure Notice and the federal
  Lead-Based Paint Disclosure (your home was built in 1972, so federal
  law requires this).

WHAT YOU CANNOT BE FORCED TO DO:
- You are not required to accept any offer.
- You are not required to drop the price.
- You can cancel this agreement if we materially fail to perform.

QUESTIONS BEFORE SIGNING?
Call Maria E. Hernandez at the brokerage. The agent must answer plainly,
in writing if you ask.

=========================================================
ARTIFACT 4 — SUPERVISING BROKER REVIEW SHEET
=========================================================

LISTING: 2418 Sunnybrook Lane, Austin, TX 78745
AGENT: Maria E. Hernandez (MLS-AGT-42119)
TERM: 2026-05-15 → 2026-11-15
COMMISSION: 5.0% / $7,500 floor / 2.5% to cooperating broker

FLAGS RAISED IN DRAFTING:
[CLEARED] Pre-1978 build — Lead-Based Paint Disclosure attached.
[CLEARED] Community property state (TX) — both spouses are signing.
[CLEARED] NAR Settlement compliance — buyer-broker compensation is
          separately documented and revocable.
[CLEARED] Drone authorization — FAA Part 107 pilot will be retained.
[INFO]    Home was on Travis County tax-delinquency watchlist 2023; cleared
          March 2024. Confirm title commitment shows no active tax lien
          before closing.

SUPERVISING BROKER SIGN-OFF:
[ ] I have reviewed this draft and approve for execution.
[ ] I have reviewed this draft and require the following changes:
    _________________________________________________

Signed: ___________________________  Date: __________
        Robert M. Patel, Supervising Broker

=========================================================
DISCLAIMER (mandatory in every output)
=========================================================
This skill provides drafting and analytical support for licensed real
estate professionals. It does not constitute legal advice. Final review
by a licensed real estate attorney is recommended for any non-standard
term, any party not present at signing, any seller in financial distress,
and any transaction crossing state lines.
```

## 🔐 PERMISSIONS & SETUP CHECKLIST

- [ ] **State and form template confirmation (one-time per state):** On first activation, tell Claude the state and the controlling form (CAR-RLA, TREC-1101, FAR-BAR ERS, NY Standard, IL-RES). Claude will refuse to draft in unconfirmed jurisdictions without an explicit `generic` selection plus local counsel disclaimer.
- [ ] **Brokerage policy block (one-time, recommended):** Paste the brokerage's commission floor, minimum protected period, dual-agency policy, and any unacceptable terms list. Claude auto-flags violations on every subsequent draft.
- [ ] **Agent and supervising-broker identifiers (one-time):** MLS ID, brokerage license number, supervising broker name. These populate every signature block.
- [ ] **State-mandatory disclosure forms in hand (per listing):** TDS/SPD/seller disclosure, lead-based paint pamphlet for pre-1978, agency disclosure (CAR-AD/TX-IABS/FL-SA/NY-Disclosure/IL-Disclosure). Claude will halt if any is unavailable.
- [ ] **Title/legal description source (per listing):** Preliminary title commitment OR existing recorded deed. Street address alone is insufficient.
- [ ] **Disclaimer (mandatory):** This skill provides drafting support, not legal advice. Output is for licensed agent / attorney review only. The skill includes this disclaimer in every output by default.

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

| Scenario | Claude's Exact Response |
|---|---|
| Required input not provided by user | Ask for the specific missing input before proceeding — do not guess or fabricate |
| Data is ambiguous or has multiple valid interpretations | Present both interpretations, state which Claude used, and why |
| Calculation produces a negative or nonsensical result | Flag it explicitly, show the math, and ask user to verify inputs |
| Legal or compliance risk is detected in the output | Insert a ⚠️ LEGAL FLAG block, describe the risk plainly, recommend consulting a licensed professional |
| Output would require information Claude cannot access (live MLS, locked database) | Deliver the maximum output possible with available data, list exactly what's missing and where to get it |
| Conflicting instructions between user input and skill SOP | Follow the SOP — flag the conflict to the user at the end of the output |
| Session approaching context limit mid-task (Cowork) | Write a `_PROGRESS_CHECKPOINT.md` file noting completed steps, current position, and what remains before the session ends |
| Seller demands commission below brokerage floor (typically <4%) | Flag CRITICAL; recommend either declining the listing or running a brokerage exception process; surface NAR Settlement implications (post-Aug 2024 buyer-broker compensation must be negotiated separately) and document the exception in the broker review sheet |
| Property is co-owned and a non-cooperating spouse / co-tenant has not signed | Insert a ⚠️ SPOUSAL/CO-OWNER CONSENT REQUIRED banner; require signature from every owner of record; in community-property states (CA, TX, AZ, NM, NV, ID, LA, WA, WI), refuse to deliver as ready-to-sign |
| Seller is in active bankruptcy or probate | Halt drafting; require court approval (bankruptcy court §363 sale order, probate court letters testamentary or administrator authority) before any listing is executed; cite the controlling jurisdiction's procedural rule and route to attorney review |

## 📖 DOMAIN GLOSSARY

| Term | Definition |
|---|---|
| **PSA (Purchase & Sale Agreement)** | The binding contract between buyer and seller setting price, terms, contingencies, and closing date. |
| **LOI (Letter of Intent)** | Pre-contract document outlining proposed terms; usually non-binding but creates negotiation expectations. |
| **EMD (Earnest Money Deposit)** | Cash the buyer puts up to demonstrate good faith. Typically 1–3% of purchase price; held in escrow until closing or default. |
| **RESPA (Real Estate Settlement Procedures Act)** | Federal law governing closing-cost disclosure and prohibiting kickbacks on settlement services. |
| **TRID (TILA-RESPA Integrated Disclosure)** | Federal rule requiring the Loan Estimate (within 3 days of application) and Closing Disclosure (3 business days before closing). |
| **Fair Housing Act** | Federal law (42 U.S.C. §§3601–3619) prohibiting discrimination in housing on the basis of race, color, religion, sex, national origin, familial status, or disability. |
| **Title Commitment** | Preliminary report from a title company outlining the conditions under which it will issue title insurance. |
| **Concession** | A seller-paid credit to the buyer at closing (closing costs, repairs, rate buy-down). |
| **Contingency** | A condition that must be satisfied for the contract to proceed (financing, inspection, appraisal, title). |
| **Clear-to-Close (CTC)** | Lender confirmation that all underwriting conditions are met and the loan is ready to fund. |
| **MLS (Multiple Listing Service)** | The cooperating-broker database (e.g., Bright MLS, ABoR/ACTRIS, MRED, NTREIS, CRMLS) where listings are syndicated to participating brokers and IDX feeds. |
| **Procuring Cause** | The agent who, through unbroken series of events, brought about the sale; relevant when commission disputes arise between cooperating brokers. |
| **Protected Period** | Post-expiration window during which the listing agent retains commission rights if a previously-shown buyer purchases the property; enforceable only if the prospective-buyer list was registered in writing with the seller before expiration. |
| **Net Listing** | A listing structure where the agent's commission equals sales price minus a seller's net target. Banned in most states (including CA, NY, IL); strictly limited and disclosure-heavy where permitted. |
| **Buyer-Broker Compensation Agreement** | A separately negotiated written agreement governing how (and by whom) the buyer's broker is compensated. Required in writing as of August 17, 2024, per the NAR Settlement. |
| **Dual Agency / Intermediary Status** | Representation of both buyer and seller by the same brokerage. Texas uses statutory "intermediary" status (Tex. Occ. Code §1101.559) rather than dual agency. California requires written consent on CAR-AD. Banned outright in some states (e.g., FL transaction-broker default). |
| **Clear Cooperation Policy** | NAR rule requiring listings to be submitted to the MLS within one business day of public marketing; restricts "pocket listings." |
| **CAR-RLA, TREC-1101, FAR-BAR ERS, NY-STD-LIST, IL-RES-LIST** | The controlling state-form listing agreements published by, respectively, the California Association of Realtors, the Texas Real Estate Commission, the Florida Association of Realtors / Florida Bar joint form, the New York State Association of Realtors, and the Illinois Association of Realtors. |
| **TDS / SPD / IABS / Disclosure Form** | Mandatory state-specific disclosure forms — California Transfer Disclosure Statement, generic Seller Property Disclosure, Texas Information About Brokerage Services, NY/IL agency-relationship disclosures. |
| **IDX (Internet Data Exchange)** | The MLS-controlled feed that syndicates listings to public-facing portals like Zillow, Redfin, and Realtor.com; opt-out is supported by most major MLSs. |

## 🚀 HOW TO USE THIS SKILL

**Method A — Standalone Claude.ai Chat (recommended for one-off listings):**
1. Open claude.ai → start a new conversation.
2. Click the paperclip icon → attach this `.md` file.
3. Type the trigger phrase: *"Draft me a listing agreement for this seller"*.
4. Provide the Required Inputs when Claude asks (state and form first, then parties, then property, then term/commission).
5. Review the four-artifact output (draft, redline, seller summary, broker review) before any live use.

**Method B — Claude Cowork Task (for batch processing or team-lead workflows):**
1. Open Claude Cowork on Mac → grant folder access for `/Listings/` directory.
2. Reference this file in your task description.
3. Type the trigger phrase as your task instruction; supply a CSV or pasted list of pending listings.
4. Approve Claude's plan; confirm any "CONFIRM BEFORE PROCEEDING" steps.
5. Each listing is written to its own subfolder with all four artifacts.

**Method D — Claude.ai Project (for brokerage-wide deployment):**
1. Open your Claude.ai Project → upload this `.md` to the knowledge base.
2. Add the brokerage's commission policy and unacceptable-terms list to the Project knowledge.
3. Any team member can now activate the skill via the trigger phrase in Project chat.
4. The supervising broker reviews the broker-review-sheet artifact before any agreement is executed.
