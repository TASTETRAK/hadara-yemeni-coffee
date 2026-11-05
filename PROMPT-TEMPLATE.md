# Reusable prompt: research-then-build a Tastetrak client site

Copy everything below the line, fill in the `[[…]]` fields, attach the logo, and send.

---

Save the attached logo into the repo as `assets/[[slug]]-logo.[[jpg|png]]`, then make the transparent brand-color PNGs from it yourself.

You are building a production website for a new Tastetrak client: **[[BUSINESS NAME]]** ([[native-script name if any]]), a [[type of business]] in [[City, State]]. This repo (`[[repo-name]]`) is empty except for the logo.

## Step 1: Do your own research first (required)

Before writing any code, research the business yourself with web search and web fetch. Look at everything you can reach:

- Google Business / Google Maps listing and Google Images
- Yelp (search "[[Business]] [[City]]")
- TikTok: [[@handle]] · Instagram: [[@handle]] · Facebook: [[page]]
- MapQuest, Giftly, DoorDash, Uber Eats, Grubhub, Toast, Square, and any local news or blog coverage
- The business's own domain if one exists (check WHOIS/parking pages too)

If a site blocks plain fetches (Yelp, TikTok, Instagram usually do), use a structured scraper (Apify Google Maps / TikTok scrapers or equivalent) rather than guessing. Read the business's own social captions and bios: that is where hours, email, opening dates and menu categories usually surface first.

Capture: exact address, phone, hours, menu items and prices, ordering link, email, social handles, photos, interior colors and decor, taglines on signage, and how customers describe the place.

Known facts so far (verify them, don't just trust them):

- Address: [[…]]
- Phone: [[… or "none found"]]
- Hours: [[… or "none found"]]
- Socials: [[…]]
- Positioning / tagline: [[…]]
- Reviews: [[…]]
- Name meaning / story: [[…]]

## Step 2: Brand, taken from the logo

- Colors: [[background]] and [[primary sampled from logo]]. Add [[light contrast color]] for one contrast section and [[accent]] for accents.
- The mark is [[describe the mark and what it references]]. Use this for the design language: [[pattern / shape motifs]].
- Wordmark: [[serif/sans description]] (use [[Google font]] or similar). Subline in [[font]]. [[Other-script]] text: [[font]].
- Make the logo's mark a transparent PNG: build alpha from luminance against the [[black/white]] background, and crop the mark and the wordmark separately.

## Step 3: Build the site

- One self-contained `index.html` with all CSS inlined. It must paste straight into BobCRM, so embed the logo images as base64. No frameworks. Keep JS small and vanilla.
- Design: elegant, bold and distinctive, not a generic template. [[Three or four specific design moves: e.g. big serif headlines, pattern texture, a hero frame drawn in with SVG lines, a marquee band]]. Scroll reveals, respect `prefers-reduced-motion`, fully responsive.
- Sections: sticky nav (mark + name, Order Ahead button) → Hero ([[positioning line]], [[name meaning]]) → Our Story → [[Menu / The Food / The Coffee]] → Gallery → Visit (address, hours, phone, Google Maps embed, directions button, socials) → Footer (wordmark, [[native-script name]], "Site by Tastetrak").
- Gallery photos: if you find real photos you can use (the business's own posts count, with a CONFIRM note), use them. Otherwise make intentional labeled placeholder tiles (pattern + diamond label), not broken image frames.

## Hard rules

- Never invent menu items, prices, hours, or a phone number. If the real menu is not found, label the menu section as an educational guide to [[cuisine]] classics with no prices, and show "Full menu coming soon."
- If sources disagree, trust the business's own pages and Google listing first.
- Mark every unconfirmed item in the HTML with an `<!-- CONFIRM: ... -->` comment.
- Don't add a second floating order button (BobCRM injects one). An in-page styled "Order Ahead" link is fine.

## Step 4: Deliver

1. Commit `index.html`, the `assets/` PNGs, a `build/` template + script so the page can be regenerated, and a short `README.md` listing the research sources you used and every CONFIRM item.
2. Screenshot the page at desktop (1440px) and mobile (390px) with Playwright, check for horizontal overflow and console errors, and fix anything that looks off before you finish.
3. End with a short summary: what you found in research, what's still unconfirmed, and the commit hash.
4. Finally, write a reusable prompt like this one for the next client.
