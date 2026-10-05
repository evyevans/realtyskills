# Source playbook

This playbook supplies task procedures and examples. Follow the working rules in the skill entry, verify current jurisdiction-specific claims, and treat examples as illustrative.

# Social Media Content Planner

Stop staring at a blank screen wondering what to post. This skill generates a complete 30-day social media content calendar tailored to your market, brand, and inventory — with ready-to-post copy for Instagram, Facebook, LinkedIn, and TikTok. Every post includes the caption, hashtag set, visual or video prompt, best posting time, and engagement hook. The content mix is strategically balanced across educational content (30%), listings (20%), personal brand (20%), market updates (15%), and social proof (15%) to build authority, generate leads, and stay top-of-mind without becoming a "listings-only" account that nobody follows.

## 🧠 SKILL IDENTITY

**WHO this skill is for:**
A solo agent, team lead, wholesaler, or brokerage owner who knows social drives leads but spends Sunday nights paralyzed in front of a blank Canva, posting nothing for two weeks at a stretch — losing top-of-funnel attention to competitors who post daily.

**WHAT this skill does:**
Generates a complete 30-day social calendar across Instagram, Facebook, LinkedIn, TikTok, and YouTube Shorts: post copy, hashtag sets sized to platform norms, visual prompts (what to film/photograph), engagement hooks, and a content mix balanced across the 5-pillar model (listings 30%, education 25%, market 15%, lifestyle 15%, personal 15%). Includes weekly themes, reel/short hooks, and CTA per post.

**WHERE to use this skill:**
Standalone chat for individual agents; Claude.ai Project for teams (every agent gets the calendar customized to their farm area); Cowork Task when you want CSV export ready for Buffer/Hootsuite/Later import.

**WHEN to activate this skill:**
First Monday of the month — generate next 30 days at once; biweekly batches if preferred; immediately when a market event (rate cut, big sale in farm area) requires a 7-day reactive calendar.

**WHY this skill matters:**
This workflow makes the required inputs and output structure explicit. Its numerical benchmarks are configurable assumptions, not validated performance claims.

**HOW this skill works (Overview):**
Claude takes the agent's farm area, brand voice, brokerage info, and any active listings, then maps out a 30-day calendar with balanced content mix and weekly thematic arcs. Each post gets fully drafted copy, platform-specific hashtags, a visual brief, and engagement hook. Closes with a content-repurposing guide.

## When to Use

- Planning your social media for the upcoming month (batch creation)
- Launching your presence on a new platform (Instagram, TikTok, LinkedIn)
- Refreshing a stale social media strategy that is not generating leads or engagement
- Onboarding a social media VA or assistant with ready-to-post content
- Preparing content around a new listing launch or open house
- Building a content backlog so you never miss a posting day
- Pivoting your strategy when market conditions change (rate shifts, inventory changes)
- Creating content for a specific campaign (farming area, niche market, seasonal push)

## 📥 REQUIRED INPUTS

| Parameter | Type | Required | Description |
|---|---|---|---|
| agent_name | string | Yes | Your name as it appears on social media |
| market_area | string | Yes | City, neighborhood, or region you serve |
| agent_niche | string | No | Specialty: first-time-buyers, luxury, relocation, investment, military, divorce, seniors (default: general) |
| brand_pillars | string | Yes | 3-4 topics that define your personal brand (e.g., "local market expertise, first-time buyer education, community involvement, family life") |
| active_platforms | string | Yes | Comma-separated: instagram, facebook, linkedin, tiktok, twitter |
| current_listings | string | No | Brief details of active listings to promote (address, price, key feature) |
| recent_closings | string | No | Recent client wins for social proof content (with permission) |
| personal_interests | string | No | Hobbies, community involvement, personal brand elements (e.g., "marathon runner, dog rescue volunteer, coffee lover") |
| posting_frequency | string | No | daily, 5x-week, 3x-week (default: 5x-week) |
| content_tone | string | No | professional, casual-friendly, luxury-refined, educational, humorous (default: casual-friendly) |
| target_audience | string | No | Who follows you: homebuyers, sellers, agents, general-community (default: homebuyers) |
| month | string | No | Target month for seasonal relevance (default: current month) |
| competitor_gap | string | No | Something your competitors do not talk about that you want to own |

## ⚙️ EXECUTION SOP

### Step 1: Content Mix Strategy

**What Claude does:** Calculate the balanced post counts across the 5 categories (Educational / Listings / Personal Brand / Market Updates / Social Proof) for the user's posting frequency, then list specific topics per category drawn from `brand_pillars` and `agent_niche`.
**Tools / Resources needed:** 5-pillar mix ratio table; agent's `brand_pillars`; topic-bank by niche.
**Data source:** User-provided `posting_frequency`, `brand_pillars`, `agent_niche`, `competitor_gap`.
**Output of this step:** A content-mix summary table showing post counts per category and topic list.
**Cowork behavior:** PROCEED WITH ANALYSIS AND DRAFTING
**If this step fails or required data is missing:** If `brand_pillars` is empty, ask user for 3 before proceeding — these define the personal-brand 20%; cannot be inferred safely.

Apply the optimal content mix ratio for real estate agents:

| Content Category | Percentage | Posts per 30 Days (5x/week = 22 posts) | Purpose |
|---|---|---|---|
| **Educational** | 30% | 6-7 posts | Build authority, provide value, attract new followers |
| **Listings** | 20% | 4-5 posts | Showcase inventory, generate buyer inquiries |
| **Personal Brand** | 20% | 4-5 posts | Build trust, show personality, create connection |
| **Market Updates** | 15% | 3-4 posts | Demonstrate expertise, provide timely value |
| **Social Proof** | 15% | 3-4 posts | Testimonials, closings, client wins, awards |

**Content Mix Rules:**
- Never post 2 listings in a row (followers will mute you)
- Always follow a listing post with an educational or personal post
- Market update posts work best on Monday/Tuesday (start-of-week mindset)
- Personal posts perform best on weekends (casual scrolling)
- Social proof posts get highest engagement when paired with a personal story

### Step 2: Platform-Specific Formatting

**What Claude does:** For each post on the calendar, produce a platform-native variant respecting that platform's optimal length, hashtag count, format, and CTA conventions.
**Tools / Resources needed:** Platform format specs (below); current trending audio reference if `include_trending_audio` is true.
**Data source:** Step 1 calendar slots + `active_platforms`.
**Output of this step:** Platform-by-platform content variants per calendar slot.
**Cowork behavior:** PROCEED WITH ANALYSIS AND DRAFTING
**If this step fails or required data is missing:** If user did not specify platforms, default to IG + FB; flag that LinkedIn/TikTok are not in scope and offer to add them.

Adapt each post for the target platform:

**Instagram:**
| Element | Specification |
|---|---|
| Caption length | 150-300 words (front-load the hook before the "more" fold) |
| Hashtags | 5-15 (mix of broad, niche, and local) |
| Visual format | Single image, carousel (5-10 slides), or Reel |
| Best posting times | 11am-1pm, 7pm-9pm (local time) |
| CTA style | "Save this for later," "DM me [keyword]," "Share with someone who needs this" |
| Carousel formula | Hook slide -> 5-7 value slides -> CTA slide |

**Facebook:**
| Element | Specification |
|---|---|
| Post length | 100-200 words (shorter than Instagram) |
| Hashtags | 0-3 (Facebook algorithm de-prioritizes heavy hashtags) |
| Visual format | Single image or video (Facebook Groups content encouraged) |
| Best posting times | 9am-11am, 1pm-3pm |
| CTA style | "Share this with someone looking to buy/sell," "Comment [emoji] if you agree" |
| Community angle | Reference local events, businesses, school news |

**LinkedIn:**
| Element | Specification |
|---|---|
| Post length | 200-400 words (longer, thought-leadership style) |
| Hashtags | 3-5 (industry and local) |
| Visual format | Single image or carousel document |
| Best posting times | 8am-10am Tuesday-Thursday |
| CTA style | "What is your experience with [topic]?" "Agree or disagree?" |
| Tone | Professional, data-driven, industry insight |

**TikTok:**
| Element | Specification |
|---|---|
| Video length | 15-60 seconds (hook in first 3 seconds) |
| Hashtags | 3-5 (trending + niche) |
| Format | Talking head, property tour, screen recording, trending audio |
| Best posting times | 7am-9am, 12pm-3pm, 7pm-11pm |
| Hook formula | "Here is what nobody tells you about [topic]" / "Stop scrolling if you want to [benefit]" |
| CTA style | "Follow for more real estate tips," "Comment [word] for my free guide" |

### Step 3: Content Theme Assignment

**What Claude does:** Assign each day-of-week a recurring theme (Market Monday / Tip Tuesday / Win Wednesday / etc.) and slot each Step 1 post into the appropriate theme day.
**Tools / Resources needed:** Day-theme mapping table below.
**Data source:** Step 1 mix; `month` for seasonal hooks.
**Output of this step:** A day-by-day calendar with each theme labeled and a topic assigned.
**Cowork behavior:** PROCEED WITH ANALYSIS AND DRAFTING
**If this step fails or required data is missing:** If user prefers different themes, ask for the 7-day weekly arc pattern they want; default to industry-standard themes if no input.

Assign a daily theme to maintain variety and make content creation predictable:

| Day | Theme | Content Category | Example Post Type |
|---|---|---|---|
| Monday | Market Monday | Market Update | Weekly stats, rate update, inventory snapshot |
| Tuesday | Tip Tuesday | Educational | Buyer tip, seller tip, home maintenance, financial |
| Wednesday | Win Wednesday | Social Proof | Client closing story, testimonial, milestone |
| Thursday | Thoughtful Thursday | Personal Brand | Behind-the-scenes, day-in-the-life, community involvement |
| Friday | Feature Friday | Listings | New listing showcase, open house promo, property highlight |
| Saturday | Story Saturday | Educational/Personal | Longer-form story, market deep dive, personal reflection |
| Sunday | Rest or Bonus | Any | Optional post, engagement-focused (poll, question, meme) |

### Step 4: Hashtag Strategy

**What Claude does:** Build three rotating hashtag sets — Broad, Niche, Local — sized to each platform's hashtag economy, drawing from `market_area` and `agent_niche`.
**Tools / Resources needed:** Hashtag bank by city/state; broad-real-estate tag list; niche tag derivatives.
**Data source:** `market_area`, `agent_niche`, sample of high-performing competitor accounts (if user pasted any).
**Output of this step:** Three labeled hashtag sets and a rotation rule per content type.
**Cowork behavior:** PROCEED WITH ANALYSIS AND DRAFTING
**If this step fails or required data is missing:** If `market_area` is too broad (e.g., "USA"), ask for a narrower farm area; hyper-local hashtags drive most of the discovery effect.

Build three hashtag sets to rotate:

**Set A — Broad Real Estate (5-7 tags):**
```
#RealEstate #HomeForSale #DreamHome #RealEstateAgent #HouseHunting #NewHome #RealEstateLife
```

**Set B — Niche/Expertise (5-7 tags):**
```
#FirstTimeBuyer #HomeBuyingTips #RealEstateInvesting #LuxuryRealEstate #RelocationExpert #[YourNiche]Tips #[YourNiche]Agent
```

**Set C — Local/Community (5-7 tags):**
```
#[CityName]RealEstate #[CityName]Homes #[NeighborhoodName] #[CityName]Realtor #MoveTo[CityName] #[CityName]Living #[CityName]Community
```

**Rotation:** Set A + C on listing posts, Set B + C on educational posts, Set A + B on social proof posts.

### Step 5: Engagement Strategy

**What Claude does:** Pick an engagement hook (question / poll / challenge / save prompt / DM trigger / debate / story) for each post, optimized for the post's category and platform.
**Tools / Resources needed:** Engagement hook bank; platform-specific CTA conventions.
**Data source:** Step 2 platform variant + Step 3 theme.
**Output of this step:** A specific engagement hook attached to each post on the calendar.
**Cowork behavior:** PROCEED WITH ANALYSIS AND DRAFTING
**If this step fails or required data is missing:** Default to "save prompt" for educational and "DM trigger" for listings if no other guidance.

Each post includes an engagement hook designed to drive comments and shares:

| Hook Type | Example | Best For |
|---|---|---|
| Question | "What is the first thing you would look for in your dream home?" | Educational, personal |
| Poll | "Hot take: Granite or quartz countertops? Comment below!" | Engagement boosters |
| Challenge | "Tag a friend who is thinking about buying this year" | Social proof, listings |
| Save prompt | "Save this post for when you start your home search" | Educational carousels |
| DM trigger | "DM me 'GUIDE' for my free first-time buyer checklist" | Lead generation |
| Debate | "Agree or disagree: Now is a great time to buy. Here is why..." | Market updates |
| Story | "I just helped a family close on their first home. Here is what happened..." | Social proof |

### Step 6: Visual and Video Prompts

**What Claude does:** For each post, write a specific visual/video prompt the user (or their VA / videographer) can execute — what to shoot, what to put on screen, what aesthetic to follow.
**Tools / Resources needed:** Visual prompt template by content type; brand color palette if uploaded.
**Data source:** Step 2 platform variant + Step 3 theme + brand assets.
**Output of this step:** One visual brief per post — actionable enough to hand to a videographer or VA.
**Cowork behavior:** PROCEED WITH ANALYSIS AND DRAFTING
**If this step fails or required data is missing:** If brand assets are not uploaded, write generic visual prompts and flag for user to attach brand-kit on next iteration.

For each post, provide a specific visual direction:

| Content Type | Visual Prompt |
|---|---|
| Listing | Hero exterior photo, carousel of interior highlights, video walkthrough |
| Educational | Branded text overlay on solid color, carousel with text slides, infographic |
| Market Update | Chart/graph with market data, side-by-side comparison graphic |
| Social Proof | Photo with client (with permission), closing table photo, before/after |
| Personal Brand | Behind-the-scenes photo, selfie at event, casual lifestyle shot |
| TikTok | Talking head with text overlay, property tour with trending audio, green screen with data |

## 📤 OUTPUT FORMAT

```
# 30-Day Social Media Content Calendar

**Agent:** [agent_name]
**Market:** [market_area]
**Month:** [month/year]
**Platforms:** [active platforms]
**Posting Frequency:** [frequency]

---

## Content Mix Summary

| Category | Posts | % | Topics Covered |
|---|---|---|---|
| Educational | [N] | 30% | [topics] |
| Listings | [N] | 20% | [listings referenced] |
| Personal Brand | [N] | 20% | [brand pillars covered] |
| Market Updates | [N] | 15% | [data points covered] |
| Social Proof | [N] | 15% | [wins referenced] |

---

## Weekly Calendar

### Week 1: [Date Range]

#### Day 1 — Monday, [Date]: Market Monday

**Theme:** [specific topic]
**Category:** Market Update
**Platform(s):** [primary platform + adaptations]

**Instagram Post:**

[Complete caption text — 150-300 words with hook, body, CTA]

**Hashtags:** [5-15 hashtags]

**Visual Prompt:** [Specific description of what image/graphic to create]

**Best Posting Time:** [time]

**Engagement Hook:** [specific question or CTA]

**Facebook Adaptation:** [shorter version for Facebook]

**LinkedIn Adaptation:** [professional version for LinkedIn]

**TikTok Adaptation:** [video concept if applicable]

---

#### Day 2 — Tuesday, [Date]: Tip Tuesday

[Same format as Day 1]

---

[Continue for all days in the month]

---

## Hashtag Sets

**Set A (Broad):** [hashtags]
**Set B (Niche):** [hashtags]
**Set C (Local):** [hashtags]

## Monthly Engagement Goals

| Metric | Target | How to Achieve |
|---|---|---|
| Follower growth | +[N] per platform | Consistent posting + engagement in comments |
| Average engagement rate | [X%] | Question hooks + carousel content |
| DM inquiries | [N] per month | DM triggers in CTAs |
| Listing inquiries from social | [N] per month | Featured listing content + audience targeting |

## Content Repurposing Guide

| Original Post | Repurpose As |
|---|---|
| Instagram carousel | LinkedIn document post, TikTok slides video |
| TikTok video | Instagram Reel, Facebook video, YouTube Short |
| Market update post | Email newsletter section, blog post |
| Client testimonial | Website review, Google Business Profile review |
```

## Methodology

**MAGNET Framework (Mix-Audience-Generate-Nurture-Engage-Track)**

The MAGNET framework is built on the principle that social media for real estate agents serves three overlapping purposes: lead generation (attracting new prospects), brand building (staying top-of-mind with your sphere), and authority positioning (proving expertise to future clients). Most agents fail at social media because they only post listings, which serves none of these purposes for non-buyer audiences. The MAGNET framework ensures every month includes a strategic Mix of content types, targets a specific Audience persona, Generates leads through intentional CTAs, Nurtures existing followers with value-first content, Engages the community to boost algorithmic distribution, and Tracks performance to iterate and improve. Research from NAR shows that 52% of agents cite social media as their top lead source, but only agents who post consistently with varied content see meaningful results.

## Advanced Configuration

| Parameter | Default | Range | Description |
|---|---|---|---|
| educational_pct | 30% | 20-40% | Percentage of educational content |
| listings_pct | 20% | 10-30% | Percentage of listing content |
| personal_pct | 20% | 10-30% | Percentage of personal brand content |
| market_pct | 15% | 10-25% | Percentage of market update content |
| social_proof_pct | 15% | 10-25% | Percentage of social proof content |
| carousel_frequency | 2x/week | 1-4x/week | How often to post carousel/slide content |
| reel_frequency | 2x/week | 0-5x/week | How often to post Reels/TikTok videos |
| story_posts_per_day | 3-5 | 1-10 | Instagram/Facebook story posts per day |
| include_trending_audio | true | true/false | Reference current trending audio for Reels/TikTok |
| include_seasonal_content | true | true/false | Incorporate seasonal/holiday themes |
| community_spotlight_frequency | biweekly | weekly/biweekly/monthly | How often to feature local businesses/events |
| lead_magnet_promotion | weekly | weekly/biweekly/monthly | How often to promote your free resources |

## Example

**Input:**
```
agent_name: Jessica Palmer
market_area: Scottsdale, AZ
agent_niche: luxury
brand_pillars: "luxury market expertise, Scottsdale lifestyle, interior design eye, client concierge experience"
active_platforms: instagram, facebook, linkedin, tiktok
current_listings: "8401 E Dixileta Dr, $2.1M, desert modern with infinity pool; 10222 E Sundance Trail, $1.4M, Troon North golf course home"
recent_closings: "Just closed $1.8M in DC Ranch for the Martinez family (with permission)"
personal_interests: "hiking Camelback Mountain, wine collecting, interior design, rescue dog Ginger"
posting_frequency: 5x-week
content_tone: luxury-refined
target_audience: homebuyers
month: March 2026
competitor_gap: "Nobody in Scottsdale luxury is doing behind-the-scenes content showing the concierge-level service agents provide"
```

**Output:**
```
# 30-Day Social Media Content Calendar

**Agent:** Jessica Palmer
**Market:** Scottsdale, AZ
**Month:** March 2026
**Platforms:** Instagram, Facebook, LinkedIn, TikTok
**Posting Frequency:** 5x/week (22 posts)

---

## Content Mix Summary

| Category | Posts | % | Topics Covered |
|---|---|---|---|
| Educational | 7 | 32% | Luxury buying process, design trends, investment value, staging |
| Listings | 4 | 18% | Dixileta Dr, Sundance Trail, open house, coming soon |
| Personal Brand | 5 | 23% | Behind-the-scenes, Camelback hike, wine + design, Ginger |
| Market Updates | 3 | 14% | Scottsdale luxury stats, spring market preview, rate impact on luxury |
| Social Proof | 3 | 14% | Martinez closing, client testimonial, year-to-date results |

---

## Week 1: March 2-6, 2026

### Day 1 — Monday, March 2: Market Monday

**Theme:** Scottsdale Luxury Q1 Market Snapshot
**Category:** Market Update
**Platform(s):** Instagram (carousel), LinkedIn (long post), Facebook (summary)

**Instagram Post (Carousel — 7 slides):**

Slide 1 (Hook): "Scottsdale Luxury Market: What $1M+ Buyers Need to Know in March"

Slide 2: "Inventory is up 12% from January, but demand is keeping pace. Here is what the numbers show."

Slide 3: "Average DOM for $1M+: 45 days (down from 58 in Q4)"

Slide 4: "Median price per sqft: $485 (up 3.2% YoY)"

Slide 5: "Most active neighborhoods: DC Ranch, Troon North, Silverleaf, Arcadia"

Slide 6: "What this means for buyers: More options, but the best properties still move in under 30 days. Do not wait to make a move on a home you love."

Slide 7 (CTA): "Thinking about buying or selling in Scottsdale this spring? DM me 'MARKET' and I will send you a detailed report for your specific neighborhood."

**Caption:**
The Scottsdale luxury market is heating up as we enter spring, and the data tells an interesting story.

Inventory is up 12% from January, which means more options for buyers — but do not mistake that for a buyer's market. The best-positioned properties are still selling in under 30 days, and price per square foot continues to climb.

Here is my take: if you have been watching the $1M+ market and waiting for the "right time," this spring is your window. Inventory is healthy, but demand is strong. Waiting for a correction in Scottsdale luxury is like waiting for Camelback to get shorter.

DM me "MARKET" for a detailed breakdown of your target neighborhood.

**Hashtags:** #ScottsdaleRealEstate #LuxuryRealEstate #ScottsdaleHomes #ArizonaLuxury #LuxuryMarketUpdate #ScottsdaleLiving #DesertLuxury

**Visual Prompt:** Branded carousel with desert/gold color scheme. Use a hero photo of Scottsdale skyline with Camelback in background for Slide 1. Clean data graphics for Slides 2-5. Professional headshot on CTA slide.

**Best Posting Time:** Monday 11:30am MST

**Engagement Hook:** "DM me 'MARKET' for your neighborhood-specific report"

**LinkedIn Adaptation:**
Expand into 300-word thought leadership post about luxury market dynamics — reference the data points and add your professional analysis of what spring 2026 holds for the Scottsdale luxury segment. End with: "What trends are you seeing in your luxury market?"

**Facebook Adaptation:**
Shorter version: "Scottsdale luxury market update: inventory up 12%, DOM down to 45 days, price/sqft up 3.2%. Here is what it means for buyers and sellers this spring. [Link to full report]"

---

### Day 2 — Tuesday, March 3: Tip Tuesday

**Theme:** "5 Things That Actually Increase Home Value in the Desert"
**Category:** Educational
**Platform(s):** Instagram (carousel), TikTok (video), Facebook

**Instagram Post (Carousel — 7 slides):**

Slide 1 (Hook): "5 Upgrades That Actually Increase Your Home's Value in Scottsdale"

Slide 2: "1. Shade structures and outdoor living spaces. In the desert, usable outdoor square footage is king. A well-designed covered patio can add $15-30K in perceived value."

Slide 3: "2. Pool renovation (not installation). Updating an existing pool with modern finishes costs $15-25K and adds $30-50K in value for luxury properties."

Slide 4: "3. Smart home climate control. Nest or Lutron systems that manage desert heat efficiently. Buyers expect this in $1M+ homes."

Slide 5: "4. Desert-adapted landscaping. Mature desert plantings signal a home that belongs here. Ripping out grass for low-water xeriscaping can reduce maintenance costs by 60%."

Slide 6: "5. Primary suite spa bathroom. Deep soaking tub, rain shower, natural stone. The most-requested upgrade in every luxury showing."

Slide 7 (CTA): "Save this list for when you are ready to prep your home for sale. And DM me if you want a personalized upgrade checklist for your property."

**Caption:**
Not all upgrades are created equal, especially in the desert.

I see sellers spend $50K on a kitchen remodel and skip the outdoor living space, which in Scottsdale is where buyers fall in love with a home.

Here are the five upgrades I consistently see add the most value in our market — backed by what buyers actually ask about during showings, not just what HGTV says.

Save this for later. And if you want a personalized upgrade list for your specific home, DM me "UPGRADE" — I will send you my checklist.

**Hashtags:** #HomeUpgrades #ScottsdaleRealEstate #LuxuryHome #HomeValueTips #DesertLiving #HomeRenovation #RealEstateTips

**Visual Prompt:** Clean carousel with one high-quality image per slide showing the specific upgrade. Use desert color palette (warm neutrals, terracotta accents). Text overlay with large, readable font.

**Best Posting Time:** Tuesday 12:00pm MST

**TikTok Adaptation:**
30-second talking head video: "Five things that actually increase your home value in the desert — number one might surprise you." Walk through each point quickly with text overlay. Trending audio (instrumental). End with: "Follow for more Scottsdale real estate tips."

---

### Day 3 — Wednesday, March 5: Win Wednesday

**Theme:** Martinez Family Closing at DC Ranch
**Category:** Social Proof
**Platform(s):** Instagram (single image + story), Facebook, LinkedIn

**Instagram Post:**

Another family, another dream home, another chapter.

I am so happy for the Martinez family, who just closed on their beautiful home in DC Ranch. When they first reached out, they were relocating from Chicago and had never been to Scottsdale. Over the course of three months, we explored every corner of this market — from Troon North to Arcadia to DC Ranch — until they walked into this home and I watched their faces light up.

That is the moment I work for.

What makes me proudest is not just finding the right home — it is the experience along the way. Private previews, a dedicated relocation concierge, and a closing process so smooth their biggest stress was choosing which moving boxes to unpack first.

To the Martinez family: welcome home. Scottsdale is better with you in it.

If you or someone you know is thinking about making the move to Arizona, I would love to provide the same experience. DM me or tag a friend below.

**Hashtags:** #JustClosed #DCRanch #ScottsdaleRealEstate #LuxuryRealtor #WelcomeHome #ClientLove #ScottsdaleAZ

**Visual Prompt:** Photo of the Martinez family in front of their new home (with permission). If no photo available, use a beautiful exterior shot of the DC Ranch property with a "SOLD" overlay in your brand colors.

**Best Posting Time:** Wednesday 11:00am MST

**Engagement Hook:** "Tag a friend thinking about moving to Arizona."

---

[Weeks 2-4 continue with the same level of detail, covering the remaining 19 posts across all themes and platforms]

---

## Hashtag Sets

**Set A (Broad Luxury):** #LuxuryRealEstate #LuxuryHomes #DreamHome #LuxuryLifestyle #MillionDollarListing #LuxuryLiving #RealEstateGoals
**Set B (Niche):** #ScottsdaleLuxury #DesertModern #LuxuryBuyer #RelocationExpert #LuxuryInteriors #ConciergeRealEstate #DesertLiving
**Set C (Local):** #ScottsdaleRealEstate #ScottsdaleAZ #ScottsdaleHomes #DCRanch #TroonNorth #CamelbackMountain #ScottsdaleLiving

## Monthly Engagement Goals

| Metric | Target | How to Achieve |
|---|---|---|
| Instagram follower growth | +150-200 | Consistent Reels + carousel saves + community engagement |
| Average engagement rate | 3.5%+ | Question hooks + save-worthy carousels + DM triggers |
| DM inquiries | 8-12 | "DM me [keyword]" CTAs in 50% of posts |
| Listing inquiries from social | 3-5 | Featured listing posts + stories + paid boost on listing posts |

## Content Repurposing Guide

| Original Post | Repurpose As |
|---|---|
| Market Monday carousel | LinkedIn article, email newsletter lead, blog post |
| Tip Tuesday carousel | TikTok slide video, Pinterest pin, email tip |
| Win Wednesday post | Google Business Review prompt, website testimonial, newsletter feature |
| Listing post | Email blast, open house flyer copy, agent tour invite |
| TikTok video | Instagram Reel, YouTube Short, Facebook video |
```

## Edge Cases & Best Practices

- **No Active Listings:** If you have no current listings to promote, replace listing content with "dream home" showcases (share other agents' listings you love with proper credit), neighborhood spotlights, or "just sold" recaps. Never go more than 2 weeks without any property content — it is what reminds followers you are an active agent.

- **Negative Market News:** When headlines scream "housing crash" or "rates surge," address it proactively with a calm, data-backed post. Do not ignore it — your followers will see the headlines and wonder what you think. Frame your market update with local data that may tell a different story than national headlines.

- **Content Fatigue (Running Out of Ideas):** When you hit a creative wall, use the "3R Method": Respond (answer a question you received this week), Repurpose (turn an old post into a new format), Relate (share a personal story connected to real estate). Also: browse your DMs and comments for content ideas — the questions people ask you are the content your audience wants.

- **Platform Algorithm Changes:** Social media algorithms change constantly. The calendar structure remains effective regardless of algorithm shifts because it is built on content diversity and engagement triggers — both of which every platform rewards. If a specific format stops performing (e.g., static images on Instagram), shift more posts to the formats the algorithm currently favors (Reels, carousels).

- **Luxury vs. Entry-Level Tone:** Luxury content should feel aspirational but accessible. Entry-level content should feel empowering and educational. Avoid condescending language in either direction. "First-time buyer? Here is what you need to know" works. "If you can only afford a starter home..." does not.

- **Balancing Personal and Professional:** Show personality without oversharing. The 80/20 rule applies: 80% of personal content should tie back to your professional identity or values. Posting about hiking Camelback (healthy, active, knows the area) connects to your brand. Posting about a political argument does not.

- **Holiday and Cultural Sensitivity:** Include diverse holidays and cultural celebrations when appropriate, but only if you genuinely celebrate or support them. Generic "Happy Diwali" posts from agents with no connection to the holiday feel performative. When in doubt, focus on universal themes: gratitude, family, community.

- **Video Content Anxiety:** If you are uncomfortable on camera, start with voiceover content (screen recordings, photo slideshows with narration) and work up to talking-head format. Authenticity beats production quality — a genuine 30-second selfie video outperforms a polished but stiff studio clip.

## 🔐 PERMISSIONS & SETUP CHECKLIST

No external permissions required. Optional one-time setup:

- [ ] **Brand voice profile (recommended):** On first use, paste 3–5 of your highest-performing past posts so Claude can mirror your voice. For teams, upload the brokerage's social brand guide to a Claude.ai Project alongside this skill.
- [ ] **Active listings list (optional):** Paste your current 5 active listings (address, price, key feature) so Claude can weave listing posts into the 30-day calendar at the correct cadence (~30%).
- [ ] **Buffer / Hootsuite / Later (optional, for export):** If you schedule via these tools, mention it in the activation message — Claude formats the calendar as a CSV/JSON the platform can import directly.
- [ ] **Compliance one-time:** Confirm Fair Housing review person/process for any ad-style listing posts; flag posts hitting that threshold for review pre-publish.

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
|----------|------------------------|
| Required input not provided by user | Ask for the specific missing input before proceeding — do not guess or fabricate |
| Data is ambiguous or has multiple valid interpretations | Present both interpretations, state which Claude used, and why |
| Calculation produces a negative or nonsensical result | Flag it explicitly, show the math, and ask user to verify inputs |
| Legal or compliance risk is detected in the output | Insert a ⚠️ LEGAL FLAG block, describe the risk plainly, recommend consulting a licensed professional |
| Output would require information Claude cannot access (live MLS, locked database) | Deliver the maximum output possible with available data, list exactly what's missing and where to get it |
| Conflicting instructions between user input and skill SOP | Follow the SOP — flag the conflict to the user at the end of the output |
| Session approaching context limit mid-task (Cowork) | Write a `_PROGRESS_CHECKPOINT.md` file noting completed steps, current position, and what remains before the session ends |
| Agent operates in a Fair-Housing-sensitive farm area (religious neighborhood, ethnic enclave) | Run an extra pass scrubbing implicit steering language; surface any flagged post for human review before scheduling |
| Account is brand-new (<500 followers) | Skew 20% more toward "engagement-bait" formats (questions, polls, AMAs) and recommend Reels-first to leverage the algorithm's new-account boost |

## 📖 DOMAIN GLOSSARY

| Term | Definition |
|------|-----------|
| MLS | Multiple Listing Service — the regional database of active and sold listings used by licensed agents |
| FSBO | For Sale By Owner — a property sold without a listing agent |
| Expired Listing | A property whose listing agreement ended without a sale, often a high-intent re-list opportunity |
| Fair Housing Act | Federal law prohibiting discrimination in housing based on protected classes (race, color, religion, sex, national origin, familial status, disability) |
| Days on Market (DOM) | The number of days a property is actively listed before going under contract |
| Reel Hook | The first 1.5 seconds of a vertical video; >70% of retention is decided here. Hooks should pose a question, name a number, or break a pattern. |
| CMA | Comparative Market Analysis — an evaluation of a property's value based on recent sales of similar nearby properties |
| HOA | Homeowners Association — entity that enforces covenants and collects dues for shared community amenities |

## 🚀 HOW TO USE THIS SKILL

**Method A — Standalone Claude.ai Chat (recommended for most users):**
1. Open claude.ai → start a new conversation
2. Click the paperclip / attachment icon → attach this .md file
3. Type the trigger phrase shown in the front matter
4. Provide the Required Inputs when Claude asks
5. Review output before any live use

**Method B — Claude Cowork Task (for multi-step skills):**
1. Open Claude Cowork on Mac → grant folder access
2. Reference this file in your task description
3. Type the trigger phrase as your task instruction
4. Approve Claude's plan; confirm any "CONFIRM BEFORE PROCEEDING" steps

**Method D — Claude.ai Project (for team-wide deployment):**
1. Open your Claude.ai Project → upload this .md to the knowledge base
2. Any team member can now activate the skill via the trigger phrase in Project chat

## Integration

This skill connects with the broader real estate agent toolkit:

- **Skill 01 (Lead Qualification Engine):** When social media generates DM inquiries, immediately score those leads with the Qualification Engine to determine follow-up priority and sequence assignment.
- **Skill 02 (Property Description Generator):** Pull listing descriptions from the Description Generator to create social media listing posts — the Instagram and Facebook variants are already formatted for social use.
- **Skill 03 (Market Analysis Reporter):** Use CMA data and market trends from the Reporter to fuel your Market Monday posts with real, local data instead of generic national statistics.
- **Skill 04 (Client Follow-Up Sequencer):** Coordinate your social posting schedule with your follow-up sequences — when you post a "just listed" on social, your email sequence should be promoting the same listing to your database that same day.
- **Skill 05 (Objection Handler Coach):** Create educational social content that preemptively addresses common objections — "Should you wait for rates to drop?" posts educate your audience and prevent the objection before it happens in a sales conversation.
- **Skill 06 (Contract Review Assistant):** Create "Did you know?" social content about contract clauses and buyer/seller protections — educational content about the transaction process positions you as a knowledgeable agent who protects clients.
