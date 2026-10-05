<p align="center">
  <img src="assets/realtyskills-banner.svg" alt="RealtySkills — Practical AI skills for real estate professionals. By Evy Evans." width="100%">
</p>

<p align="center">
  <strong>42 practical workflows · 9 categories · Free and open source</strong><br>
  12 starter workflows + 30 detailed playbooks<br>
  Created and maintained by <a href="https://github.com/evyevans">Evy Evans</a>
</p>

<p align="center">
  <a href="docs/getting-started.md">Start here</a> ·
  <a href="docs/catalog.md">Find a skill</a> ·
  <a href="docs/workflows.md">Follow a workflow</a> ·
  <a href="docs/installation.md">Install skills</a> ·
  <a href="https://github.com/evyevans/realtyskills/releases/latest">Download</a>
</p>

# RealtySkills

**Give your AI a clear process for the real estate task in front of you.**

Write listing copy, prepare seller calls, organize follow-ups, explain market data, and evaluate a rental property with reusable instructions. RealtySkills is a library for agents, investors, property managers, brokerage teams, and the engineers who support them.

A **skill** is a set of written instructions you give an AI assistant. It tells the assistant what information to ask for, how to work through a task, and what to return. You can read every instruction before using it.

**No coding is needed for the chat workflow.** Use it with an AI assistant that accepts text or files, including Claude, ChatGPT, and Gemini. Installation is a separate option for tools that support skills. Results and available tools vary by product and account.

## Try your first skill

1. **Choose a task** from the table below. Start with a **Starter** if you're new.
2. **Give the instructions to your AI.** Open the linked file, copy its contents into a new chat, or download and attach it. On GitHub, use **Raw**, then your browser's save option. For a **Detailed** skill, also attach its linked `references/playbook.md` file.
3. **Explain your task and provide the facts.** Ask the assistant to collect missing inputs, then review the result before using it.

Try this with the Listing Content Starter:

```text
Follow the RealtySkills instructions I attached.
Help me draft listing copy for a 2-bedroom, 2-bath condo in Toronto.
Verified facts: 900 sq ft, balcony, one parking space, asking CAD 650,000.
Use a clear, factual tone. Ask me for missing details before writing.
Do not invent amenities, neighborhood claims, or property features.
```

See the [first-use walkthrough](docs/getting-started.md) and [worked examples](examples/README.md).

## What do you need to do?

| Your task | Start here | Provide | Receive |
|---|---|---|---|
| Write a listing | [Listing Content Starter](skills/listings-and-marketing/listing-description-engine/SKILL.md) · Starter | Verified features, price, market, tone | Listing draft, captions, buyer email |
| Follow up with a lead | [Lead Nurture Starter](skills/client-communication-and-referrals/lead-nurture-machine/SKILL.md) · Starter | Lead stage, goals, channel, consent | Email and text sequence drafts |
| Prepare a seller call | [Seller Call Starter](skills/leads-and-prospecting/seller-call-framework/SKILL.md) · Starter | Property context, seller goals, timeline | Call agenda and discovery questions |
| Explain market changes | [Market Report Starter](skills/market-research-and-pricing/market-report-generator/SKILL.md) · Starter | Dated local statistics and their sources | Newsletter and social summary |
| Evaluate a rental | [Rental Property Evaluation](skills/deals-and-investment-analysis/rental-property-underwriting-model/SKILL.md) · Detailed | Price, rents, expenses, vacancy, financing | Cash flow, key ratios, scenarios |

## Browse by category

| Category | Workflows | Typical tasks |
|---|---:|---|
| [Leads and prospecting](docs/catalog.md#leads-and-prospecting) | 5 | Qualification, seller calls, outreach |
| [Listings and marketing](docs/catalog.md#listings-and-marketing) | 5 | Listing copy, launch plans, social posts, email |
| [Client communication and referrals](docs/catalog.md#client-communication-and-referrals) | 5 | Follow-ups, objections, client retention |
| [Market research and pricing](docs/catalog.md#market-research-and-pricing) | 5 | CMAs, listing appointments, market reports |
| [Deals and investment analysis](docs/catalog.md#deals-and-investment-analysis) | 6 | Wholesale deals, flips, rentals, multifamily |
| [Transactions and documents](docs/catalog.md#transactions-and-documents) | 6 | Timelines, client updates, document drafts |
| [Property management](docs/catalog.md#property-management) | 2 | Tenant messages, maintenance work orders |
| [Compliance and risk](docs/catalog.md#compliance-and-risk) | 4 | Housing marketing, licensing, transaction risks |
| [Brokerage operations and CRM](docs/catalog.md#brokerage-operations-and-crm) | 4 | Recruiting, onboarding, data cleanup, ROI |

The [full catalog](docs/catalog.md) includes inputs, outputs, jurisdiction, and tool requirements. Use your browser's **Find** feature to search it. **Starter** means a focused workflow; **Detailed** means a longer procedure with more inputs. Neither label promises professional accuracy.

## Start with your role

| Your role | Suggested sequence |
|---|---|
| Agent | [Seller call](skills/leads-and-prospecting/seller-call-framework/SKILL.md) → [Listing appointment](skills/market-research-and-pricing/cma-listing-appointment-prep/SKILL.md) → [Listing content](skills/listings-and-marketing/listing-description-engine/SKILL.md) |
| Investor | [Rental evaluation](skills/deals-and-investment-analysis/rental-property-underwriting-model/SKILL.md) → [Neighborhood research](skills/market-research-and-pricing/neighborhood-investment-climate-report/SKILL.md) → [Transaction risks](skills/compliance-and-risk/transaction-risk-screener/SKILL.md) |
| Property manager | [Tenant and owner messages](skills/property-management/property-management-comms/SKILL.md) → [Maintenance work order](skills/property-management/property-management-work-order-tracker/SKILL.md) |
| Team lead or brokerage | [CRM cleanup](skills/brokerage-operations-and-crm/crm-data-audit-and-cleanup-engine/SKILL.md) → [Lead qualification](skills/leads-and-prospecting/lead-qualification-engine/SKILL.md) → [Agent onboarding](skills/brokerage-operations-and-crm/agent-onboarding-and-training-planner/SKILL.md) |
| AI engineer | [Installation guide](docs/installation.md) → [Machine-readable catalog](catalog.json) → [Contribution guide](CONTRIBUTING.md) |

## Choose your way to use it

| Method | Best for | What to do |
|---|---|---|
| Copy or attach instructions | Trying a task in an AI chat | Follow the [beginner guide](docs/getting-started.md) |
| Download a standalone chat guide | Keeping all instructions in one file | Download `realtyskills-chat-guides-v1.0.0.zip` from [Releases](https://github.com/evyevans/realtyskills/releases/latest), extract it, and attach one guide |
| Upload a Claude skill | Reusing a workflow in Claude | Upload an individual skill ZIP; see [installation](docs/installation.md#claude-skills-upload) |
| Install for Claude Code or Codex | Working with an agent that can read local files | Copy a complete skill folder into its discovery directory; see [installation](docs/installation.md#local-agent-installation) |

The library is free. Your AI product may require a paid plan for particular tools or skill features. Browsing, CRM access, sending, and spreadsheet tools are **not** included with these files.

## Use in your market

Many drafting and planning workflows can be adapted internationally. Some source playbooks use US contracts, laws, taxes, or terminology. Every catalog entry identifies its jurisdiction; **1031 exchanges are US-only**. A US legal checklist does not become a Canadian or other local checklist just by changing the address.

Provide your country, state or province, currency, and units. Check current local requirements with qualified professionals. Market analysis needs dated data; forecasts need explicit assumptions. Legal and financial outputs are working drafts, not legal advice, tax advice, or compliance certification.

See [capabilities and limitations](docs/quality-and-limitations.md). Use fictional or redacted client records when trying a workflow.

## Built to be read, reused, and improved

Every active folder contains a standard `SKILL.md` entry. Detailed playbooks live in `references/`. The [catalog](catalog.json) records all active entries and the [seven archived versions](archive/README.md). Automated checks verify packaging, metadata, internal links, and inventory consistency; they do not establish that AI answers are correct.

Want to improve a workflow or add a market-specific version? Read [CONTRIBUTING.md](CONTRIBUTING.md), [report an issue](https://github.com/evyevans/realtyskills/issues/new/choose), or open a pull request. Please use synthetic examples and cite authoritative sources for jurisdiction-specific changes.

## About the author

I'm **Evy Evans**, an AI engineer sharing reusable workflows for real estate professionals. I built RealtySkills to make useful AI instructions easier to find, understand, and adapt.

If you find a workflow useful, **star the repository** to bookmark it and share the link with a colleague. Tell me which task or market you'd like covered next.

**Free to use and adapt under the [MIT License](LICENSE).** Keep the license notice when redistributing the material.
