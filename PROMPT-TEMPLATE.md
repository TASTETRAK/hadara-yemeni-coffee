# Universal prompt: research-then-build a Tastetrak client site

Copy everything below the line, fill in the `[[…]]` fields, attach the logo, and send. It bakes in every correction from the Hadara build so the first draft lands close to final.

---

Save the attached logo into the repo as `assets/[[slug]]-logo.[[jpg|png]]`, then cut the mark and the wordmark into transparent PNGs yourself (alpha from luminance against the logo's background).

You are building the final, production website for a Tastetrak client: **[[BUSINESS NAME]]** ([[native-script name, if any]]), a [[type of business]] in [[City, State]]. The repo `[[repo-name]]` is empty except for the logo. This is the final draft, not a mockup. The business is open or opening within days.

## 1. Research before you write any code

Use web search, web fetch, and when a site blocks plain fetches (Yelp, TikTok, Instagram, Google Maps), use a structured scraper. Read, in this order of trust:

1. The business's own accounts: TikTok [[@handle]], Instagram [[@handle]], Facebook [[page]]. Read every caption and the bio. Download their videos and pull frames to see the real interior, signage and food. Download their avatar and posters and sample the colors.
2. Google Business Profile, Yelp, MapQuest, Giftly, Apple Maps.
3. Ordering platforms: DoorDash, Uber Eats, Grubhub, Toast, Square, Clover.
4. Their domain, if any (check for parking pages), and local press.

Capture: exact address, phone, hours, email, menu items and prices, ordering link, review links, social handles, taglines on signage, interior materials and colors, and how customers describe the place. Known facts so far (verify them): [[list]].

**The theme follows their collateral, not the logo file.** If their avatar, posters and storefront are light, build light. If they are dark, build dark. Sample the exact hex values from their own images.

## 2. Hard rules (these come from real client feedback)

- Never invent hours, a phone number, menu items, or prices. If something is unknown, write it so it stays true ("Daily hours on our socials"), and ask for it at the end.
- No "coming soon", "opening soon", "stay tuned", "full menu coming soon" anywhere. Not in copy, labels, or alt text.
- Nothing that looks AI-generated or templated: no curtain or wipe reveals, no plain fades, no gradient blobs, no stock photos, no invented stat boxes ("Est. [[year]]", "100% authentic"), no lorem ipsum, no emoji in copy, no generic "Welcome to our website" lines, no placeholder image frames with broken icons.
- Every repeated link lives in one place: `<body data-order-url="…" data-review-url="…">`, and a few lines of JS fill every Order and Review link from it.
- One order button visible at a time. Desktop: a solid Order Ahead button in the top bar, styled differently from the text links. Phones: a small floating pill, bottom right, that hides whenever another order button is on screen. The hero never has an order button. Every order button carries "Pickup & delivery available" inside it as a bolder second line.
- Real photos only, and the business's own photos count (stills from their posts, re-cropped so the whole subject is in frame, with a note to get their originals). Remaining gallery slots are intentional labeled placeholder tiles in the brand pattern, never broken images.

## 3. Build

One self-contained `index.html`, all CSS inlined, logo images embedded as base64, no frameworks, vanilla JS, pasteable into BobCRM. Keep a `build/template.html` + `build/build.py` so the page can be regenerated.

Layout, top to bottom:

- **Top bar**: mark + name, links (Menu, Gallery, Directions, Follow, Review), Order Ahead button on desktop. A custom menu icon drawn from the brand's own geometry, not three generic lines.
- **A thin marquee strip** directly under the top bar (about 20 px tall): name, native-script name, tagline words from their signage, city. No "pickup and delivery" in it.
- **Hero**: short. Eyebrow line, one big serif headline, two lines of copy, then a row of four small dark diamond buttons: TikTok, Instagram, Directions, Leave a review (five stars in a straight row, never one star). Desktop: the best real photo in a brand-shaped frame on the right, whole subject visible. Phones: that photo full colour, edge to edge under the marquee, whole subject visible, with the text in a frosted panel tucked under its bottom edge.
- **Our Story**: one clean block of two paragraphs. No quotes, no stats row.
- **Menu / The [[food or drink]]**: a horizontal swipe rail of cards shaped from the brand's geometry, auto-advancing every 2 seconds, pausing on touch and resuming after 4 seconds idle, with a segmented progress bar and arrows on desktop. If no real menu exists, make it an educational guide to the cuisine's classics with no prices, and end with a compact "See Menu" button pointing at the order link.
- **Gallery**: a second swipe rail, same behaviour, real photos first.
- **Reviews / Follow**: the one dark contrast band. One real quoted review with attribution, a Leave-us-a-review button, Follow cards for each social, Get directions.
- **Visit**: address with the shopping-center landmark, hours, contact, order, Get Directions button, Google Maps embed.
- **Footer**: wordmark, native-script name, one-line tagline, social icons, "Site by Tastetrak".

Motion: subtle only. Sections land with a quick scale-and-settle, headings ease in a beat later, and the small rule beside each section label draws in. Respect `prefers-reduced-motion`.

SEO: proper title and description, canonical, Open Graph and Twitter cards with a 1200×630 logo card as an absolute URL, and `CafeOrCoffeeShop`/`Restaurant` JSON-LD with address, geo, email, sameAs. Leave a comment at the top listing the absolute URLs to change when the domain moves.

## 4. Deliver

1. Commit `index.html`, `assets/`, `build/`, a `README.md` listing the research sources, the palette with where each value was sampled from, and every item still needed from the owner.
2. Screenshot at 1440 px and 390 px with Playwright, scroll the whole page, check for horizontal overflow and console errors, and look at every section before you call it done.
3. Push, enable GitHub Pages from the branch, confirm the live URL returns the new build.
4. End with: what research found, what the theme is based on, the live link, and the short list of things only the owner can supply (order link, review link, hours, phone).
