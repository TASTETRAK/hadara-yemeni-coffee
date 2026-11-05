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

## CONFIRM before go-live

Every one of these is also marked in `index.html` with an `<!-- CONFIRM: … -->` comment.

1. **Opening status / date.** Site says "Opening soon on West Lane". Their last post (Oct 18, 2026) still said preparing to open. Update once open.
2. **"The first Yemeni coffee house in the 209."** Hadara's own claim. Sahara Coffee House in Merced has been promoted with a similar claim. Keep, soften, or drop per the owner.
3. **Order Ahead link.** No ordering platform found. Both "Order Ahead" buttons currently point to `#visit`. Replace with the real URL.
4. **Hours.** None published. Site shows "Posted at opening".
5. **Phone.** None published. Site shows "Phone number coming soon". Do not invent one.
6. **Email info@hadaracoffee.com.** From the hiring post. Confirm it is monitored.
7. **Instagram @hadara_coffee.** Linked but unverified.
8. **Menu.** The six "field guide" cards are classic Yemeni coffee-house styles (qishr, Adeni chai, mufawar, jubani, Sana'ani) plus a "Crepes & Sweets" card based on the hiring poster's categories (Coffee, Crepes, Waffles, Desserts). No prices. Swap in the real menu when supplied.
9. **Gallery photos.** Two tiles are stills from Hadara's own TikTok posts (blade sign, Aug 2026; storefront vinyl, May 2026). Get the owner's OK or their originals. The other four tiles are intentional labeled placeholders.
10. **Yelp quote.** Linda R.'s public review is quoted with attribution in Our Story. Ask the owner whether they want it.
11. **Google Maps embed** uses the street address, not a place ID, because no listing exists yet. When the owner creates a Google Business Profile, switch to the place link.
12. **"Same center as China Palace and Wingstop"** is confirmed by Google Maps; "West Lane at Hammer Lane" is from the map and should be sanity-checked by someone local.

## Brand notes

- Colors: black `#0A0A0A`, sand gold `#E2C790` (sampled from the logo), light sand `#F1E6CC` (Visit section), deep gold `#B89A5E` (accents). The shop's print collateral also uses cream with a brown/terracotta mark.
- Type: Cormorant Garamond 600/700 (headlines, wordmark feel), Jost 300–500 (body, tracked caps), Reem Kufi (Arabic).
- Motifs: square-Kufic tile pattern (CSS data-URI), qamariya arched-window frame in the hero drawn with SVG `stroke-dashoffset`, diamond markers. `prefers-reduced-motion` disables all animation.

## QA done

- Screenshots at 1440 px and 390 px (Playwright, Chromium): no horizontal overflow, no console errors, mobile menu works, map embed loads.
