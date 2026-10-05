# Your first RealtySkills workflow

You need an AI assistant that accepts text or files. You do not need Git, a terminal, or an API key to use the chat instructions.

## 1. Pick one task

Choose a **Starter** from the [catalog](catalog.md). The [Listing Content Starter](../skills/listings-and-marketing/listing-description-engine/SKILL.md) is a useful first example. A starter includes its full instructions in one file.

## 2. Give your AI the instructions

On GitHub, open the linked file, choose **Raw**, and copy the full text. Paste it into a new chat, or save the file and attach it using your assistant's file upload button. You can also extract a standalone Markdown guide from the chat-guide ZIP on the [release page](https://github.com/evyevans/realtyskills/releases/latest).

For a **Detailed** entry, attach both `SKILL.md` and the `references/playbook.md` linked inside it. A chat attachment does not automatically fetch another file. The standalone release guide combines both, so only one attachment is needed.

Paste this message after providing the instructions:

```text
Use the attached RealtySkills instructions for this task.
First tell me what information you need, and ask only for missing inputs.
Use my verified facts. If information or a tool is unavailable, explain the gap.
Show assumptions and give me a draft to review.
My task: [describe what you need]
My location: [country and state or province]
Currency and units: [for example, CAD and square feet]
```

If your assistant cannot accept files, paste the full instructions and the request into the chat. If the text exceeds its limits, choose a starter or use a tool with enough context for the detailed playbook.

## 3. Supply the facts

For the listing starter, try these fictional facts:

```text
Task: create a listing description and social caption.
Location: Toronto, Ontario, Canada.
Property: 2-bedroom, 2-bath condo; 900 sq ft.
Verified features: balcony, one parking space, in-unit laundry.
Asking price: CAD 650,000.
Tone: straightforward and welcoming.
MLS character limit: 1,000 characters for this exercise.
Do not claim nearby amenities, renovation dates, views, or accessibility features.
```

An appropriate result uses those facts, stays within the requested limit, and asks about missing details before adding them. Compare the [worked listing example](../examples/listing-copy.md).

## 4. Review and refine

Read the output before sharing it. Verify names, numbers, dates, features, claims, and local requirements. Ask for a revision such as “shorten this to 700 characters” or “make the next action clearer.” Do not send a client message until you've reviewed its facts and recipient.

## Troubleshooting

| What happens | What to try |
|---|---|
| The AI gives a generic answer | Ask it to name the selected skill, list its required inputs, and follow the requested output format |
| It cannot find a reference | Attach the linked playbook or use the combined chat guide |
| It invents local market figures | Supply dated statistics; ask it to mark gaps instead of estimating them |
| It cannot create a spreadsheet or read a CSV | Use a product with file/calculation tools, or request a small table and verify calculations |
| It follows US examples in another country | State your jurisdiction and request local professional review; do not reuse a US legal form as a local form |
| You only have a repository URL | Open or download the actual instructions; an AI may not be able to browse the link |

For repeated use, see [installation](installation.md). For connected tasks, see [workflows](workflows.md).
