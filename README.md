# Hadara Yemeni Coffee — حضارة

Production one-page site for **Hadara Yemeni Coffee**, 5052 West Ln, Ste 4, Stockton, CA 95210. Built by Tastetrak.

## Files

| Path | What it is |
|---|---|
| `index.html` | The whole site. All CSS inlined, logo + two photos embedded as base64, ~290 KB. Paste straight into BobCRM. |
| `assets/hadara-logo.jpg` | The supplied logo (mark + wordmark) on the brand black. |
| `assets/hadara-mark.png` | Transparent gold mark, cut from the JPG (alpha built from luminance against the black). |
| `assets/hadara-wordmark.png` | Transparent gold "HADARA — YEMENI COFFEE" wordmark, same method. |
| `assets/hadara-lockup.png` | Transparent full lockup (mark + wordmark), for social/print use. |
| `assets/photo-sign.jpg`, `assets/photo-window.jpg` | Stills from Hadara's own TikTok posts, used in the gallery. See CONFIRM list. |
| `build/template.html`, `build/build.py` | Source template with `{{MARK}}`-style placeholders and the script that embeds the images. Edit the template, run `python3 build/build.py`, commit `index.html`. |

No floating order button is included; BobCRM injects its own. The in-page "Order Ahead" buttons are plain links.

## Research (Nov 5, 2026)

Sources actually read, in order of trust:

1. **Hadara's own TikTok, @hadara_coffee** ("Hadara coffee حضارة", 8 posts, ~710 followers).
   Bio: "Authentic Yemeni coffee ☕️ / Opening soon — Hadara Coffee / 5052 West Ln #4, Stockton, CA 95210".
   Posts: "Coming soon" (May 16, 2026, with the address) · "Part 1 Of The Journey" (May 21; on-screen text "POV: Your Starting The First Yemeni Coffee Shop In The 209") · "Stay Tuned" (May 23; building it "From The Ground Up") · "Modern Or Traditional… What Do You See First?" (May 26; blade-sign photo) · Eid post (May 27) · "Quick Sneak Peak" (Jun 5) · "#ComingSoon" (Aug 14) · **"WE'RE HIRING | HADARA YEMENI COFFEE"** (Oct 18, 2026: "As we prepare to open our doors…", email **info@hadaracoffee.com**, "send your résumé via Instagram DM", poster lists **Coffee · Crepes · Waffles · Desserts**).
   Storefront vinyl seen in the posts carries the taglines "Sustainably Sourced" and "Made With Passion", plus the Arabic lockup حضارة / قهوة يمنية.
2. **Google Maps** (via a Maps scrape of "Hadara coffee" in Stockton and of the address): **no Google Business listing for Hadara exists yet.** The address resolves to the same center as Wingstop (5052 West Ln Ste 4L) and China Palace (5052 West Ln ste 4c f).
3. **Yelp**: listed as "Hadara", 5.0 stars, 2 reviews, Coffee & Tea. Yelp blocked direct fetches; the data came via Giftly and MapQuest, which syndicate Yelp. Reviews: Linda R. ("Found them on TikTok, first Yemeni Coffee Shop in the 209… So happy I don't have to drive all the way to the bay…") and Kimsean R. ("Looking forward to a Yemeni coffee shop in Stockton. I was going all the way to Manteca for House of Mokha…"). Both read as pre-opening. Yelp photo: a cream "قريباً / coming soon" poster with a brown mark.
4. **MapQuest** (hadara-825549037): address only, no phone, no hours. "Also at this address: Superfish Poke&Tea".
5. **Giftly** (gift-card/hadara-stockton): address "5052 West Ln Ste 4", Coffee & Tea, 5.0 (2) via Yelp, no phone/hours. Map pin 38.00090, -121.28841.
6. **hadaracoffee.com**: registered, but currently a Squarespace "Coming Soon" parking page (noindex). No content.
7. **Instagram**: profile could not be opened (login wall). A local reel (halalbilalll, Aug 11, 2026: "Opening day coming soon!! … @hadara_coffee") and the hiring post both point to an Instagram account, most likely **@hadara_coffee**.
8. **Other TikTok coverage**: @aisha.waqas4, "Hadara Coffee Shop is Coming Soon In Stockton!" (Jun 1, 2026) and "Opening Soon in Stockton!" (Oct 16, 2026).
9. **Not found anywhere**: phone number, hours, menu, prices, ordering link (DoorDash, Uber Eats, Grubhub, Toast all checked), Facebook page, local press (Stockton Record, KCRA, ABC10, CBS13).

Meaning of the name: حضارة (ḥaḍāra) = civilization. The mark is the word حضارة in square Kufic, stacked like a Sana'a tower house.

## Links to set (one place each)

Open `index.html` and find the `<body>` tag near the top:

```html
<body data-order-url="#visit" data-review-url="https://www.yelp.com/biz/hadara-stockton">
```

- `data-order-url`: the online-ordering link (pickup & delivery). Every "Order Ahead" button and the floating button read from it. Until it is set they scroll to the Visit section.
- `data-review-url`: swap the Yelp link for the Google review link once the Google Business Profile exists. Every "Leave a review" link reads from it.

Also near the top: the `<link rel="canonical">`, `og:image`, `twitter:image` and JSON-LD `url` are absolute URLs pointing at the GitHub Pages address. Change them when the site moves to its final domain so link previews keep working.

## Still to supply from the owner

1. **Order link** (above).
2. **Hours.** None published anywhere. The Visit section says "Daily hours on our socials" rather than inventing them.
3. **Phone.** None published, so the site shows email only (info@hadaracoffee.com, from the hiring post).
4. **Google review link** once the Google listing exists (above).
5. **Menu.** The six swipeable "field guide" cards are classic Yemeni coffee-house styles plus a Crepes & Sweets card from the hiring poster's categories. No prices. Replace with real items when supplied.
6. **Gallery photos.** Two tiles are stills from Hadara's own TikTok posts (blade sign, storefront vinyl). Four tiles are labeled placeholders waiting for real photos.
7. **"First Yemeni coffee house in the 209"** appears only inside the quoted Yelp review now; the hero says "Yemeni Coffee House · Stockton, CA · The 209".
8. **Instagram @hadara_coffee** is linked but could not be opened to verify.

## Brand notes

- Colors (light theme, from Hadara's own collateral): cream `#F6F0E2` page, brown `#A07251` mark and headings (both sampled from their Instagram avatar; the same pair appears on the window vinyl and the Coming Soon / Now Hiring posters), dark brown `#2B211B` for the review band and footer, soft gold `#D9B98A` on dark. The original gold-on-black PNGs are kept for the dark footer and the blade sign.
- Interior (from their June 2026 "sneak peak" video): grey stone-block walls, arched niches, vintage lantern sconces, and a hand-drawn mural of Sana'a tower houses on cream plaster. The gallery copy describes this.
- Type: Cormorant Garamond 600/700 (headlines, wordmark feel), Jost 300–500 (body, tracked caps), Reem Kufi (Arabic).
- Motifs: square-Kufic tile pattern (CSS data-URI), qamariya arched-window frame in the hero drawn with SVG `stroke-dashoffset`, diamond markers. `prefers-reduced-motion` disables all animation.

## QA done

- Screenshots at 1440 px and 390 px (Playwright, Chromium): no horizontal overflow, no console errors, mobile menu works, map embed loads.
