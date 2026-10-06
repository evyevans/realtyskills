> Archived overlapping version. Use the active catalog for maintained skills.

---
name: property-description-generator
description: Creates compelling, MLS-ready property listings with headline formulas, emotional hooks, and multi-platform variants from property details.
version: "1.0"
author: Evykynn
---

# Property Description Generator

Turn a set of property features into a polished, high-converting listing description in minutes. This skill takes your property details — beds, baths, square footage, upgrades, neighborhood highlights — and produces a full suite of listing copy: an MLS-compliant description (with character limits), an extended website description, social media variants for Instagram, Facebook, and Twitter, and an email blast version. Every output uses proven persuasion psychology adapted for real estate buyers, translating raw features into emotional benefits that make buyers picture themselves living there.

## When to Use

- Writing a new MLS listing description for a property you just listed
- Refreshing a stale listing description after 30+ days on market with low showing activity
- Creating social media posts to promote a new listing across all platforms simultaneously
- Drafting listing email blasts for your buyer database or newsletter
- Preparing listing presentation materials — show sellers exactly what their marketing will look like
- Generating description variants for different buyer personas (first-time buyer vs. luxury vs. investor)
- Creating Coming Soon or pocket listing teasers before a property hits the MLS
- Writing descriptions for open house invitations and flyers

## Input Required

| Parameter | Type | Required | Description |
|---|---|---|---|
| property_address | string | Yes | Full street address, city, state, zip |
| property_type | string | Yes | Single-family, condo, townhouse, multi-family, luxury, land |
| bedrooms | number | Yes | Number of bedrooms |
| bathrooms | number | Yes | Number of bathrooms (can include half-baths as .5) |
| square_footage | number | Yes | Total living square footage |
| lot_size | string | No | Lot dimensions or acreage (e.g., "0.25 acres", "50x120 ft") |
| year_built | number | No | Year the property was originally constructed |
| list_price | number | Yes | Listing price in USD |
| key_features | string | Yes | Comma-separated list of standout features (e.g., "chef's kitchen, quartz countertops, walk-in closet, smart home, pool") |
| recent_upgrades | string | No | Upgrades completed in the last 5 years (e.g., "new roof 2024, HVAC 2025, hardwood floors throughout") |
| neighborhood | string | Yes | Neighborhood or subdivision name |
| neighborhood_highlights | string | No | Nearby amenities, schools, parks, dining, transit (e.g., "top-rated elementary school, 5 min to downtown, walking trails") |
| target_buyer | string | No | Primary buyer persona: first-time-buyer, move-up-buyer, luxury-buyer, investor, downsizer, family (default: general) |
| unique_selling_point | string | No | The single most compelling thing about this property in the agent's own words |
| mls_char_limit | number | No | Character limit for MLS description (default: 1000 — varies by MLS) |

## Process

### Step 1: Feature-to-Benefit Translation

Convert every raw feature into an emotional benefit using this translation framework. Buyers do not buy features — they buy the life those features enable.

| Feature Category | Feature Example | Benefit Translation | Emotional Hook |
|---|---|---|---|
| Kitchen | Quartz countertops | Elegant surfaces that stand up to daily life | "Entertain with confidence" |
| Kitchen | Gas range / 6-burner | Professional-grade cooking at home | "Your inner chef finally has the right tools" |
| Kitchen | Open floor plan to living | Cook while staying connected to family | "No more missing the conversation" |
| Outdoor | Fenced backyard | Private retreat for kids, pets, and weekend barbecues | "Your own outdoor sanctuary" |
| Outdoor | Pool | Resort-style living every day of summer | "Skip the crowded public pool" |
| Outdoor | Covered patio | Year-round outdoor enjoyment, rain or shine | "Morning coffee with a view" |
| Primary Suite | Walk-in closet | Space for everything, organized your way | "Finally, room to breathe" |
| Primary Suite | Ensuite with double vanity | Your own morning routine, no sharing required | "Start every day without the rush" |
| Tech | Smart home (Nest, Ring, etc.) | Control your home from anywhere | "Peace of mind, whether you are home or away" |
| Location | Walk to restaurants/shops | Vibrant lifestyle steps from your front door | "Ditch the car for date night" |
| Location | Top-rated school district | Your kids' education secured by your address | "The best investment is the one that grows with your family" |
| Condition | New roof / HVAC | Zero maintenance surprises for years to come | "Move in and live — no repair checklist" |
| Space | Bonus room / flex space | Home office, gym, playroom — you choose | "A room that adapts to your life" |
| Garage | 2+ car garage | Protected parking plus storage and workshop space | "No more morning frost scraping" |

### Step 2: Headline Generation

Create 3 headline options using proven formulas:

| Formula | Structure | Example |
|---|---|---|
| Benefit + Location | "[Top benefit] in [Neighborhood]" | "Resort-Style Living in Westlake Hills" |
| Lifestyle + Feature | "[Lifestyle promise] with [standout feature]" | "Entertainer's Dream with Chef's Kitchen and Pool" |
| Emotional + Price Anchor | "[Emotional hook] — [beds]/[baths] Under $[price]" | "Your Forever Home — 4BR/3BA Under $600K" |

Select the strongest headline based on the `target_buyer` persona:
- **First-time buyer:** Emphasize affordability, move-in ready, location value
- **Move-up buyer:** Emphasize space, upgrades, lifestyle improvement
- **Luxury buyer:** Emphasize exclusivity, finishes, architectural details
- **Family:** Emphasize schools, yard, safe neighborhood, space
- **Downsizer:** Emphasize low maintenance, walkability, single-story, modern

### Step 3: MLS Description (Character-Limited)

Write the MLS description within `mls_char_limit` characters. Structure:

```
[Opening hook — 1 sentence that stops the scroll]
[Key features paragraph — highlight top 4-5 benefits, not features]
[Lifestyle paragraph — paint a picture of daily life in this home]
[Location value — neighborhood, schools, proximity to key destinations]
[Call to action — urgency driver]
```

**MLS Writing Rules:**
- Never use ALL CAPS (except proper nouns)
- Never use exclamation marks excessively (1 maximum per description)
- Avoid "motivated seller," "must see," "won't last" (overused and ineffective)
- Include measurable claims when possible ("5-minute walk to Metro," not "close to transit")
- Front-load the most compelling benefit in the first sentence
- Use Fair Housing compliant language — no references to race, religion, familial status, national origin, sex, disability, or color

### Step 4: Extended Website Description

Write a longer version (400-600 words) with the same structure but expanded:

- **Opening:** 2-3 sentences that set the scene and emotional tone
- **Home Tour Flow:** Walk the buyer through the home room by room, leading with benefits
- **Outdoor Living:** Describe yard, patio, pool, views in sensory language
- **Neighborhood Story:** 1 paragraph on what it feels like to live in this area
- **Recent Updates:** Bullet list of upgrades with dates (builds buyer confidence)
- **Closing Hook:** One sentence that creates urgency or emotional pull

### Step 5: Social Media Variants

Generate platform-specific versions:

**Instagram (2200 char max, optimized for engagement):**
- Opening hook (first line visible before "more")
- 3-5 short paragraphs with emoji accents (tasteful, not excessive)
- Key stats line: beds | baths | sqft | price
- 5 relevant hashtags (mix of local + real estate)
- CTA: "DM for details" or "Link in bio for photos"

**Facebook (longer form, community-oriented):**
- Story-style opening ("Just listed in [neighborhood]...")
- 2 paragraphs describing the home and lifestyle
- Bullet list of top 5 features
- Price and showing information
- CTA: "Share with someone who has been looking in [area]!"

**Twitter/X (280 char max):**
- One punchy sentence + key stats + link placeholder
- Example: "Just listed: 4BR/3BA stunner in Westlake Hills. Chef's kitchen, pool, top-rated schools. $575K. DM me or link below."

### Step 6: Email Blast Version

Write a listing announcement email suitable for sending to a buyer database:

- **Subject Line:** 3 options (curiosity, benefit, urgency-based)
- **Preview Text:** 1 sentence that complements the subject line
- **Email Body:**
  - Opening hook (1-2 sentences)
  - Key stats box (beds, baths, sqft, price, neighborhood)
  - 3-4 benefit paragraphs
  - Photo placeholder note ("[Insert hero photo]")
  - CTA button text: "Schedule a Showing" or "See All Photos"
- **P.S. Line:** One additional hook or urgency element

## Output Format

```
# Listing Copy Suite: [property_address]

## Headlines (Pick One)

1. [Benefit + Location headline]
2. [Lifestyle + Feature headline]
3. [Emotional + Price Anchor headline]

**Recommended:** #[N] — [reason based on target buyer]

---

## MLS Description ([X]/[limit] characters)

[MLS-compliant description text]

---

## Extended Website Description

[400-600 word description with full room-by-room tour]

---

## Social Media

### Instagram

[Instagram-optimized post with hashtags]

### Facebook

[Facebook community-style post]

### Twitter/X

[280-character post with key stats]

---

## Email Blast

**Subject Line Options:**
1. [Curiosity-based]
2. [Benefit-based]
3. [Urgency-based]

**Preview Text:** [preview]

**Body:**

[Email body with formatting]

**P.S.** [Additional hook]

---

## Feature-to-Benefit Reference (for this listing)

| Feature | Benefit Translation | Used In |
|---|---|---|
| [feature] | [benefit] | [MLS, Instagram, etc.] |
| ... | ... | ... |
```

## Methodology

**STORY Framework (Scene-Transformation-Outcomes-Reasons-You)**

The STORY framework is adapted from direct-response copywriting and applied to property marketing. Instead of listing features, each description tells a micro-story: sets the SCENE (what daily life looks like), describes the TRANSFORMATION the home enables (from apartment to homeowner, from cramped to spacious), highlights concrete OUTCOMES (specific lifestyle improvements), provides REASONS to believe (upgrades, condition, comps), and speaks directly to YOU — the buyer reading the listing. This approach outperforms feature-dump listings by 3-5x in click-through and inquiry rates because it activates the buyer's imagination rather than their calculator.

## Advanced Configuration

| Parameter | Default | Range | Description |
|---|---|---|---|
| tone | warm-professional | luxury-exclusive, casual-friendly, warm-professional, data-driven | Overall writing tone for all copy |
| mls_char_limit | 1000 | 250-5000 | Character limit for MLS description (varies by MLS board) |
| hashtag_count | 5 | 3-30 | Number of hashtags in Instagram post |
| include_price_in_social | true | true/false | Whether to include list price in social posts |
| email_tone | consultative | consultative, urgent, casual, luxury | Tone for email blast |
| feature_limit | 8 | 4-15 | Maximum features to highlight in any single piece |
| include_fair_housing_disclaimer | false | true/false | Append Equal Housing Opportunity statement |
| language | english | english, spanish, bilingual | Output language(s) for descriptions |
| include_virtual_tour_cta | false | true/false | Add virtual tour link placeholder to outputs |
| seasonal_hooks | auto | auto, spring, summer, fall, winter | Seasonal references in copy ("enjoy summer evenings by the pool") |

## Example

**Input:**
```
property_address: 2847 Sunset Ridge Dr, Austin, TX 78735
property_type: Single-family
bedrooms: 4
bathrooms: 3.5
square_footage: 3200
lot_size: 0.31 acres
year_built: 2019
list_price: 725000
key_features: "open-concept kitchen with waterfall island, primary suite with soaking tub, covered back patio with built-in grill, home office with French doors, smart home (Nest thermostat, Ring cameras, smart locks), energy-efficient windows"
recent_upgrades: "landscape redesign with native plants 2025, epoxy garage floors 2025, added built-in bookshelves in office 2024"
neighborhood: Sunset Ridge at Barton Creek
neighborhood_highlights: "Barton Creek Greenbelt trails 2 min drive, Hill Country Galleria 8 min, top-rated Eanes ISD, Lake Travis 15 min"
target_buyer: move-up-buyer
unique_selling_point: "The back patio setup is incredible — full outdoor kitchen with a built-in grill, beverage fridge, and string lights. It is like having a restaurant patio in your backyard."
mls_char_limit: 1000
```

**Output:**
```
# Listing Copy Suite: 2847 Sunset Ridge Dr, Austin, TX 78735

## Headlines (Pick One)

1. "Entertainer's Paradise in Sunset Ridge at Barton Creek"
2. "Live the Hill Country Dream — 4BR with Outdoor Kitchen and Greenbelt Access"
3. "Your Next Chapter Starts Here — 4BR/3.5BA Under $750K in Eanes ISD"

**Recommended:** #2 — For move-up buyers, the lifestyle upgrade is the key motivator. The outdoor kitchen and Greenbelt access signal a clear step up from their current home.

---

## MLS Description (987/1000 characters)

Live the Hill Country lifestyle you have been waiting for. This 2019-built 4-bedroom, 3.5-bath home in Sunset Ridge at Barton Creek delivers the perfect blend of modern finishes and everyday livability. The open-concept kitchen features a stunning waterfall island where mornings start with coffee and evenings end with conversation. A dedicated home office with French doors gives you a professional workspace without leaving home. Step outside to your private outdoor kitchen — built-in grill, beverage fridge, and covered patio designed for year-round entertaining. The primary suite is your retreat, complete with a soaking tub and walk-in closet. Smart home features throughout. Barton Creek Greenbelt trails are a 2-minute drive, Lake Travis is 15 minutes away, and your kids attend top-rated Eanes ISD schools. Recent upgrades include professional landscaping with native plants and a custom office built-in. Schedule your private showing before this one finds its new family.

---

## Extended Website Description

There is a moment when you walk into a home and feel the shift — from "this is nice" to "this is where I want to live." At 2847 Sunset Ridge Drive, that moment happens before you even reach the kitchen.

Built in 2019 and meticulously maintained, this 3,200 square foot home sits on a generous third-of-an-acre lot in the sought-after Sunset Ridge at Barton Creek community. From the curb, the modern Hill Country architecture and professionally landscaped yard with drought-tolerant native plants set the tone for what is inside.

Walk through the front door and the open floor plan draws you forward — soaring ceilings, natural light flooding through energy-efficient windows, and a layout designed for how families actually live. The kitchen is the centerpiece: a waterfall quartz island large enough for four barstools, premium appliances, and sightlines to both the living room and the back patio. This is where homework happens, where friends gather, where Thanksgiving dinner comes together without anyone feeling stuck in a separate room.

To the left of the main living area, French doors open to a dedicated home office — quiet, private, and finished with custom built-in bookshelves added in 2024. If you work from home even part of the week, this room changes everything.

The primary suite is a genuine retreat. The bedroom is spacious enough for a king bed plus a reading nook, and the ensuite bathroom features a soaking tub, oversized shower, double vanities, and a walk-in closet that will make your mornings effortless. Three additional bedrooms share two full bathrooms upstairs, each with ample closet space.

But the real showstopper? Step through the sliding glass doors onto the covered back patio. This is not a basic concrete slab — it is a full outdoor kitchen with a built-in grill, beverage fridge, bar seating, and string lights that turn every evening into an event. The backyard beyond is fully fenced with room for kids, pets, and weekend football. The 2025 landscape redesign means everything is mature, lush, and designed to thrive in the Texas climate.

The Sunset Ridge community puts you minutes from the best of Austin's outdoor lifestyle — Barton Creek Greenbelt trails are a 2-minute drive, Lake Travis boat ramps are 15 minutes away, and Hill Country Galleria's shopping and dining is just 8 minutes down the road. Your kids will attend Eanes ISD, consistently ranked among the top school districts in Texas.

Smart home features — Nest thermostat, Ring cameras, and smart locks — keep everything connected and secure. New epoxy garage floors, energy-efficient windows, and a 2019 build mean you can move in and simply live.

This is the home you upgrade to — and the one you never want to leave. Schedule your private showing today.

---

## Social Media

### Instagram

Just listed in Sunset Ridge at Barton Creek and this one is special.

4 BR | 3.5 BA | 3,200 sqft | $725,000

The outdoor kitchen alone will stop you in your tracks — built-in grill, beverage fridge, covered patio with string lights. Every evening feels like dining out, except you are already home.

Inside: open-concept kitchen with waterfall island, private home office with French doors, and a primary suite with soaking tub.

2 min to Barton Creek Greenbelt. 15 min to Lake Travis. Eanes ISD schools.

DM me for a private showing or link in bio for all the photos.

#AustinRealEstate #SunsetRidge #EanesISD #AustinHomes #JustListed

### Facebook

Just Listed in Sunset Ridge at Barton Creek!

I am so excited to share this one — 2847 Sunset Ridge Dr is the kind of home that makes you rethink your entire living situation. Built in 2019 with 4 bedrooms, 3.5 baths, and 3,200 sqft of thoughtfully designed space.

The outdoor kitchen is the star: built-in grill, beverage fridge, covered patio, and string lights. But inside is just as impressive — waterfall island kitchen, dedicated home office with French doors, and a primary suite that feels like a spa.

Top features:
- Open-concept living with chef's kitchen
- Private home office with custom built-ins
- Full outdoor kitchen and entertaining patio
- Smart home (Nest, Ring, smart locks)
- Eanes ISD, 2 min to Greenbelt, 15 min to Lake Travis

$725,000 | Schedule a private showing — DM me or call/text [number].

Share this with someone who has been looking for their forever home in the Hill Country!

### Twitter/X

Just listed: 4BR/3.5BA in Sunset Ridge at Barton Creek. Outdoor kitchen, waterfall island, Eanes ISD. $725K. This one is going to move fast — DM for details.

---

## Email Blast

**Subject Line Options:**
1. "The outdoor kitchen on this one... (just listed in Eanes ISD)"
2. "4BR with full outdoor kitchen in Sunset Ridge — just listed at $725K"
3. "New listing alert: Sunset Ridge at Barton Creek"

**Preview Text:** Built-in grill, beverage fridge, and string lights — plus 4BR/3.5BA in Eanes ISD.

**Body:**

Hi [First Name],

I just listed a home in Sunset Ridge at Barton Creek that I wanted you to see first.

[Insert hero photo — back patio with outdoor kitchen and string lights]

**2847 Sunset Ridge Dr, Austin, TX 78735**
4 Bed | 3.5 Bath | 3,200 sqft | 0.31 acres | $725,000

This 2019-built home is designed for the way you actually want to live. The kitchen features a waterfall quartz island open to the living room, and the dedicated home office has French doors and custom built-in bookshelves.

But the back patio is the real story — a full outdoor kitchen with built-in grill, beverage fridge, bar seating, and string lights over a covered entertaining area. It is like having your own private restaurant.

The primary suite includes a soaking tub, double vanity, and a walk-in closet. Smart home features throughout. Eanes ISD schools. Barton Creek Greenbelt 2 minutes away. Lake Travis 15 minutes.

This one is going to get attention fast.

[Schedule a Private Showing]

Talk soon,
[Your Name]

**P.S.** Know someone who has been looking in the Barton Creek area? Forward this along — I am happy to give them a private tour before it hits the open house circuit.

---

## Feature-to-Benefit Reference (for this listing)

| Feature | Benefit Translation | Used In |
|---|---|---|
| Waterfall island | Gathering spot for mornings and evenings | MLS, Website, Instagram |
| Built-in outdoor grill + fridge | Private outdoor restaurant experience | All platforms |
| Home office with French doors | Professional workspace without commute | MLS, Website, Email |
| Soaking tub in primary | Spa-level retreat at home | Website, Instagram |
| Smart home (Nest, Ring, locks) | Control and security from anywhere | MLS, Facebook |
| Energy-efficient windows | Lower bills, comfortable year-round | MLS, Website |
| Eanes ISD | Top-rated education secured by address | All platforms |
| Native plant landscaping | Low-maintenance, mature, climate-adapted | Website, Email |
```

## Edge Cases & Best Practices

- **Older Homes with Character but No Updates:** For homes built before 1980 with original kitchens and baths, lean into the "character" and "bones" angle. Phrases like "solid mid-century construction," "original hardwood floors with decades of patina," and "a canvas for your vision" work better than trying to hide the age. Always be honest — never describe a dated kitchen as "charming" if it needs a full renovation.

- **Condos and Townhouses:** Shift focus from yard and lot to lifestyle amenities (pool, gym, concierge, rooftop), walkability, and low-maintenance living. Emphasize HOA-covered maintenance as a benefit ("more weekends for yourself, less time on a mower"). Always disclose the HOA fee range and what it covers.

- **Luxury Properties ($1M+):** Use more restrained, sophisticated language. Avoid exclamation marks entirely. Use sensory words (appointed, curated, bespoke). Reference architectural style by name (Mediterranean, contemporary, Craftsman). Mention the architect or builder if notable. Quality over quantity in feature highlights.

- **Investor-Targeted Listings:** When `target_buyer` is "investor," replace emotional hooks with financial metrics: cap rate potential, rent comps, price per square foot vs. area average, and any value-add opportunities. Still write compelling copy, but lead with ROI instead of lifestyle.

- **Fair Housing Compliance:** Never describe the demographics of a neighborhood. Avoid phrases like "family-friendly" (familial status), "walking distance to [specific church/temple]" (religion), "safe neighborhood" (can imply racial composition). Instead: "top-rated schools nearby" (factual), "low crime statistics per city data" (data-backed), "vibrant community with parks and dining."

- **Price Reductions:** When refreshing a listing after a price reduction, do not just add "PRICE REDUCED!" — rewrite the description with fresh angles. Highlight a benefit that was buried in the original copy. New description = new first impression on MLS alerts.

- **Photos Not Available Yet:** If writing the description before professional photos are taken, include notes like "[Insert hero exterior shot]" and write copy that sets up expectations the photos will fulfill. Do not describe visual details you cannot verify without seeing the property.

- **Multi-Offer Situations:** When you expect multiple offers, adjust the CTA to create urgency without desperation. "Private showings available through [date]" or "Offers reviewed on [date]" is more effective than "Won't last long!"

## Integration

This skill connects with the broader real estate agent toolkit:

- **Skill 01 (Lead Qualification Engine):** Use lead scoring data to customize listing descriptions — if your buyer database is heavy on first-time buyers, adjust the target_buyer persona in your listing descriptions to speak directly to them.
- **Skill 03 (Market Analysis Reporter):** Pull CMA data to include market context in extended descriptions — "priced below the neighborhood average of $X/sqft" adds credibility and urgency.
- **Skill 04 (Client Follow-Up Sequencer):** After publishing a new listing, use the Sequencer to generate a "just listed" outreach sequence to your buyer database, sphere of influence, and past clients.
- **Skill 05 (Objection Handler Coach):** When buyers or their agents object to pricing after reading your listing, use the Objection Handler to craft responses that reference specific value points from the description.
- **Skill 07 (Social Media Content Planner):** Feed new listing descriptions into your 30-day content calendar — the Social Media Planner can distribute listing content across platforms with optimal timing and variety.
