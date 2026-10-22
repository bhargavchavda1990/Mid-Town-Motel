#!/usr/bin/env python3
"""
Static page generator for the Mid-Town Motel site.

Run:  python3 build.py
Writes index.html, rooms.html, about.html, offers.html, guide.html,
location.html, policies.html, gallery.html and 404.html next to this file.

All copy lives in the data blocks below, so a content change is one edit + one run.
The generated HTML is plain static files (GitHub Pages friendly, SEO friendly).
"""
import json, html, pathlib

ROOT = pathlib.Path(__file__).parent
SITE_URL = "https://midtownmaine.com"          # change when you deploy to a different domain
BOOK_URL = "https://resnexus.com/resnexus/reservations/book/DA784FEB-1E5F-4D53-B257-CAC2A75955D3?bookPackageID=4"
PHONE, PHONE_HREF = "207-633-2206", "tel:+12076332206"
EMAIL = "stay@midtownmaine.com"
ADDRESS = ("96 McKown St", "Boothbay Harbor, ME 04538")
FB = "https://www.facebook.com/midtownmotelboothbay"
IG = "https://www.instagram.com/Mid_town_motel/"
MAPS = "https://www.google.com/maps/search/?api=1&query=96+McKown+St+Boothbay+Harbor+ME+04538"
MAP_EMBED = "https://www.google.com/maps?q=96+McKown+St,+Boothbay+Harbor,+ME+04538&output=embed"
KAYAK = "https://www.kayak.com/Boothbay-Harbor-Hotels-Mid-Town-Motel.2996930.ksp"

e = html.escape

NAV = [("index.html", "Home"), ("rooms.html", "Rooms"), ("about.html", "About"),
       ("offers.html", "Offers"), ("guide.html", "Boothbay Guide"), ("location.html", "Location")]

# ----------------------------------------------------------------- data
ROOMS = [
    {"name": "King", "bed": "King bed", "where": "Parking-lot level", "price": "$159",
     "text": "A classic retro room with a king bed, steps from your car and a two-minute stroll from the harbor.",
     "chips": ["King bed", "Sleeps 2", "Parking-lot level"], "tone": ""},
    {"name": "Queen – Pet Friendly", "bed": "Queen bed", "where": "Adjoining building", "price": "$159",
     "text": "Bring the dog. Dog-friendly Queen rooms have their own exterior entrance and a doggie rest station close by.",
     "chips": ["Queen bed", "Sleeps 2", "Dog friendly", "Exterior entrance"], "tone": "warm", "pet": True},
    {"name": "Two Twins", "bed": "Two twin beds", "where": "Parking-lot level", "price": "$159",
     "text": "Two twin beds for friends or family travelling together, on the same easy parking-lot level.",
     "chips": ["Two twin beds", "Sleeps 2", "Parking-lot level"], "tone": "pink"},
    {"name": "Whole Property", "bed": "Every room", "where": "The whole motel", "price": "$1,495",
     "text": "Take over the entire motor lodge for a reunion, a wedding weekend or a retro getaway with your whole crew.",
     "chips": ["All rooms", "Private getaway"], "tone": "warm"},
]

AMENITIES = [
    ("\U0001F4F6", "High-speed Wi-Fi", "Throughout the property, included in every rate."),
    ("☕", "Guest services area", "Fridge and freezer, ice machine, microwave and a Keurig coffee maker."),
    ("\U0001F415", "Dog friendly", "Three dog-friendly Queen rooms and a doggie rest station with waste bags."),
    ("❄️", "Your own climate", "Individually controlled heating and air conditioning in every room."),
    ("\U0001F6CF️", "Comfy linens", "Linens by The Comphy Company, cloth bath mats and hairdryers."),
    ("\U0001F9F4", "Bath amenities", "Shampoo, conditioner, lotion and soap, plus an iron on request."),
    ("\U0001F50C", "USB ports", "Charge your phone right at the bedside."),
    ("\U0001F697", "Free parking", "On-site parking is included. No valet, no fuss."),
]

GUIDE = [
    ("Beaches", "Grimes Cove", "A small rocky beach at the end of Route 96 with views of nearby islands. Popular with photographers and artists.", None, None),
    ("Beaches", "Pemaquid Beach Park", "A sandy beach with a snack bar, restrooms, a beach house for changing and rinsing off, and a picnic area.", None, None),
    ("Beaches", "Reid State Park", "Two miles of hiking trails, a long sandy beach, shaded picnic tables with ocean views and public restrooms.", None, None),
    ("Beaches", "Popham Beach State Park", "Walking, ocean swimming and reading, with ample parking, clean facilities and a picnic area.", None, None),
    ("On the water", "Cabbage Island Clambakes", "Sail the Bennie Alice from Pier 6 to Cabbage Island for a traditional Downeast clambake cooked at the water's edge. Seven days a week from late June through the weekend after Labor Day.", "22 Commercial Street · (207) 633-7200", "https://www.cabbageislandclambake.com/"),
    ("On the water", "Eastwind Schooner", "A two-hour sail aboard a Boothbay Harbor schooner. Bring your own food and drinks, plus a windbreaker.", "20 Commercial Street · (207) 633-6598", "https://www.boothbaysailing.com/"),
    ("On the water", "Monhegan Island", "A day trip about 10 miles offshore: hike some of the highest cliffs on the Maine coast, visit a brewery and galleries, and see a shipwreck. Ferries leave from Port Clyde.", None, "https://monheganboat.com/"),
    ("On the water", "Lighthouse tour", "A self-guided lighthouse tour for boaters, covering the region's five lighthouses.", None, None),
    ("Gardens & art", "Coastal Maine Botanical Gardens", "Founded in 1996 and spread over 270 acres of tidal shoreland, with flower-lined paths and seasonal art exhibits.", "105 Botanical Gardens Drive · (207) 633-8000", "https://www.mainegardens.org/"),
    ("Gardens & art", "Boothbay Region Land Trust", "Nature preserves including Porter Preserve and Ovens Mouth Preserve. Pack a picnic from Trevett Country Store.", "60 Samoset Rd · (207) 633-4818", "https://bbrlt.org/"),
    ("Gardens & art", "Sculpture Boothbay", "Maine's only public sculpture trail, from downtown Boothbay Harbor to East Boothbay and Southport Island. A map at the front desk shows each piece.", "191 Shore Road · (207) 633-2353", "https://www.sculptureboothbay.org/"),
    ("Gardens & art", "The Opera House", "Built in 1894 and open year-round, with youth theater and touring musical performers. A short walk from the motel.", "86 Townsend Avenue · (207) 633-5159", "https://boothbayoperahouse.com/"),
]

EATS = [
    ("Ports of Italy", "Traditional Italian", "A classy spot with a big porch, housemade pasta and wine.", "https://www.portsofitaly.com/"),
    ("Brady's", "American · Family friendly", "Boothbay Harbor's only year-round waterfront restaurant.", "https://bradysboothbayharbor.com/"),
    ("Cabbage Island Clambakes", "Downeast clambake", "Sail to the island for a traditional clambake, late June through the weekend after Labor Day.", "https://www.cabbageislandclambake.com/"),
    ("Dunton's Doghouse", "Lobster rolls · Burgers", "Lobster rolls, haddock sandwiches, burgers and hot dogs, a short walk around the corner.", "https://www.facebook.com/duntonsdoghouse/"),
    ("Harborside 1901", "Breakfast · Seafood · Steak", "An airy waterfront spot with a popular happy hour.", "https://harborside1901.com/"),
    ("Kelly's Cafe", "Breakfast & lunch", "Breakfast and lunch with a view, plus gluten-free, Paleo and other dietary options.", "http://kellyscafebbh.com/"),
]

POLICIES = [
    ("Deposits & payment", [
        "A deposit of 50% of the stay, plus 9% lodging tax, per room guarantees the reservation.",
        "We accept Visa, MasterCard, American Express and Discover. The balance is due at arrival; travelers checks and cash are also accepted.",
        "For one-night stays or bookings made within three days of arrival, the full amount is collected at booking."]),
    ("Cancellations, changes & refunds", [
        "Cancel at least 14 days before arrival to get your deposit back, minus a $25 refund fee.",
        "With less than 14 days' notice, the deposit is refunded only if the room can be resold for all reserved nights.",
        "Shortened stays from date changes fall under the same policy. Late arrivals and early departures are not refunded unless the vacancy is filled.",
        "Prefer a gift certificate? We can issue one for the full deposit, valid 10 years, with no cancellation fee."]),
    ("Availability & rates", [
        "We never overbook: each reservation is for specific dates, rooms and guests.",
        "Booking directly online gives the best rates.",
        "A two- or three-night minimum applies during the short, busy season. Call us about one-night or same-day stays.",
        "Rates are for single or double occupancy and include Maine lodging tax (currently 9%).",
        "Rooms have one queen, one king or two twin beds, with a maximum of two guests. Extra guests are not allowed.",
        "Rates include on-site parking and wireless internet."]),
    ("Check-in & check-out", [
        "Check-in is between 3:00 and 7:00 pm. Arriving later? Call before 7:00 pm and we will arrange self-check-in.",
        "Check-out is at 11:00 am."]),
    ("Pets", [
        "Only dogs are allowed, in our three dog-friendly Queen rooms with exterior entrances. Reserve by calling (207) 633-2206.",
        "The fee is $35 per dog per day. Up to two dogs, each weighing no more than 70 pounds.",
        "Dogs must never be left alone in a room. They are allowed on patios and exterior common areas, on a leash, and never in interior public spaces.",
        "A $250 fee applies if a pet is found in a room not designated dog-friendly, or if a pet causes stains or damage."]),
    ("Smoke-free, vape-free & flame-free", [
        "The whole property is 100% smoke-, vape- and flame-free.",
        "Cooking devices of any kind (hot plates, slow cookers, grills) are not allowed in guest rooms.",
        "A $250 cleaning surcharge applies for burning candles, smoking, vaping or cooking in rooms, on balconies or patios, or anywhere on the property."]),
    ("House rules", [
        "Guests must be 21 or older to consume alcohol. Please drink responsibly and be considerate of others.",
        "Daily light-touch housekeeping is provided. Full-service housekeeping is available on request.",
        "Guests are financially responsible for damages caused by gross negligence."]),
]

GALLERY_COUNT = 14

# Photos are loaded straight from the original site (hotlinked). To host them yourself,
# download each file into assets/img/ and replace the URLs below with local paths.
U = "https://midtownmaine.com/wp-content/uploads/2025/11/"
IMG = {
    "hero": U + "home-hotel-hero.jpg", "history": U + "history-motel.jpg", "rooms": U + "rooms-suites.jpg",
    "about": U + "about-us.jpg", "offers": U + "offers-1.webp", "gallery": U + "gallery.jpg", "guide": U + "boothbaya.jpg",
}
ROOM_IMGS = [U + "21-DSC09886-1024x576.jpg", U + "25-DSC09910-1024x576.jpg",
             U + "03-DSC09683-1024x576.jpg", U + "46-untitled-1-683x1024.jpg"]
GALLERY = [U + n for n in ["gallery-01-scaled.jpg", "gallery-02-scaled.jpg", "gallery-03-scaled.jpg", "gallery-04-scaled.jpg",
          "gallery-05-scaled.jpg", "gallery-06-scaled.jpg", "gallery-07-1-scaled.jpg", "gallery-08-scaled.jpg",
          "gallery-09.jpg", "gallery-10.jpg", "gallery-11.jpg", "gallery-12.jpg", "gallery-13-scaled.jpg", "gallery-14-scaled.jpg"]]

# ----------------------------------------------------------------- helpers
def photo(label, tone="", src=None, alt=""):
    img = ('<img src="%s" alt="%s" loading="lazy" onerror="this.remove()">' % (src, e(alt))) if src else ""
    return '<div class="photo %s"><span class="tag-label">%s</span>%s</div>' % (tone, e(label), img)

def hero_bg(src):
    return '<img class="hero-bg" src="%s" alt="" onerror="this.remove()">' % src if src else ""

def reveal(delay=0, kind=""):
    """One gentle fade-in; delay/kind kept only so older call sites keep working."""
    return 'class="reveal"'

def header(active):
    items = "".join('<a href="%s"%s>%s</a>' % (h, ' class="active" aria-current="page"' if h == active else "", n) for h, n in NAV)
    return ('<header class="site-header"><div class="wrap nav">'
            '<a class="logo" href="index.html" aria-label="Mid-Town Motel home"><b>Mid-Town</b><i>Motel</i></a>'
            '<button class="menu-btn" aria-label="Menu" aria-expanded="false" aria-controls="nav"><span></span></button>'
            '<nav class="nav-links" id="nav" aria-label="Main">' + items +
            '<a class="btn btn-coral btn-sm" href="%s" target="_blank" rel="noopener">Book Now</a></nav></div></header>' % BOOK_URL)

def footer():
    cols = "".join('<li><a href="%s">%s</a></li>' % (h, n) for h, n in NAV)
    return ('<footer><div class="wrap"><div class="foot">'
            '<div class="foot-logo"><b>Mid-Town</b><i>Motel</i>'
            '<p style="margin-top:14px;max-width:34ch">A true 1950s classic in the heart of Boothbay Harbor, Maine.</p>'
            '<div class="socials"><a href="%s" target="_blank" rel="noopener" aria-label="Facebook">f</a>'
            '<a href="%s" target="_blank" rel="noopener" aria-label="Instagram">ig</a></div></div>'
            '<div><h4>Explore</h4><ul>%s<li><a href="gallery.html">Photo Tour</a></li><li><a href="policies.html">Policies</a></li></ul></div>'
            '<div><h4>Visit</h4><ul><li>%s</li><li>%s</li><li><a href="%s" target="_blank" rel="noopener">Get directions</a></li></ul></div>'
            '<div><h4>Contact</h4><ul><li><a href="%s">%s</a></li><li><a href="mailto:%s">%s</a></li>'
            '<li><a href="%s" target="_blank" rel="noopener">Kayak travel award</a></li></ul></div></div>'
            '<div class="copy"><span>© <span data-year>2025</span> Mid-Town Motel. All rights reserved.</span>'
            '<span>Concept redesign for review.</span></div></div></footer>'
            '<div class="mbar"><a href="%s">Call</a><a class="go" href="%s" target="_blank" rel="noopener">Book Now</a></div>'
            % (FB, IG, cols, ADDRESS[0], ADDRESS[1], MAPS, PHONE_HREF, PHONE, EMAIL, EMAIL, KAYAK, PHONE_HREF, BOOK_URL))

import re
_TAG = re.compile(r'<([a-zA-Z0-9]+)((?:\s+[^<>]*?)?)>')
def _merge_dupes(markup):
    """Merge duplicate class="" / style="" attributes inside a single tag."""
    def fix(m):
        attrs = m.group(2)
        for attr, sep in (("class", " "), ("style", ";")):
            found = re.findall(r'\s%s="([^"]*)"' % attr, attrs)
            if len(found) > 1:
                attrs = re.sub(r'\s%s="[^"]*"' % attr, "", attrs)
                merged = sep.join(x.strip(sep + " ") for x in found if x.strip())
                attrs += ' %s="%s"' % (attr, merged)
        return "<%s%s>" % (m.group(1), attrs)
    return _TAG.sub(fix, markup)

def page(fname, title, desc, hero, body, extra_head="", active=None):
    doc = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
           '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
           '<title>%s</title>\n<meta name="description" content="%s">\n'
           '<meta name="theme-color" content="#0d2233">\n'
           '<meta property="og:title" content="%s"><meta property="og:description" content="%s"><meta property="og:type" content="website">\n'
           '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
           '<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700;800&family=Fraunces:opsz,wght@9..144,600;9..144,700;9..144,900&family=Monoton&family=Pacifico&display=swap" rel="stylesheet">\n'
           '<link rel="stylesheet" href="assets/css/style.css">\n'
           '<script>document.documentElement.classList.add("js")</script>\n%s</head>\n<body>\n'
           '<a class="skip" href="#main">Skip to content</a>\n%s\n<main id="main">\n%s\n%s\n</main>\n%s\n'
           '<script src="assets/js/main.js"></script>\n</body>\n</html>\n'
           % (e(title), e(desc), e(title), e(desc), extra_head, header(active or fname), hero, body, footer()))
    (ROOT / fname).write_text(_merge_dupes(doc), encoding="utf-8")
    print("wrote", fname)

def inner_hero(crumb, h1, sub, eyebrow="", img=None):
    return ('<div class="page-hero">%s<div class="wrap"><div class="crumbs"><a href="index.html">Home</a> / %s</div>'
            '%s<h1>%s</h1><p>%s</p></div></div>'
            % (hero_bg(img), crumb, ('<span class="eyebrow">%s</span>' % eyebrow) if eyebrow else "", h1, sub))

def room_card(r, i):
    chips = "".join('<span class="chip%s">%s</span>' % (" pet" if c.startswith("Dog") else "", e(c)) for c in r["chips"])
    return ('<article %s><div class="card">%s<div class="card-body"><h3>%s</h3><div class="chips">%s</div>'
            '<p>%s</p><div class="price"><small>from </small>%s<small> / night</small></div>'
            '<div class="card-actions"><a class="btn btn-coral btn-sm" href="%s" target="_blank" rel="noopener">Book Now</a>'
            '<a class="btn btn-outline btn-sm" href="policies.html">Policies</a></div></div></div></article>'
            % (reveal(), photo(r["where"], r["tone"], ROOM_IMGS[i], r["name"]),
               e(r["name"]), chips, e(r["text"]), r["price"], BOOK_URL))

def guide_card(g, i):
    kick, name, text, meta, link = g
    more = ('<a class="more" href="%s" target="_blank" rel="noopener">Visit website →</a>' % link) if link else ""
    m = ('<div class="meta">%s</div>' % e(meta)) if meta else ""
    return ('<article %s><div class="guide-card c%d"><span class="kicker">%s</span><h3>%s</h3><p>%s</p>%s%s</div></article>'
            % (reveal(), i % 3 + 1, e(kick), e(name), e(text), m, more))

def cta(eyebrow="Book direct", h="Book direct for the best rates", p="Skip the middleman. Booking with us gives you our best rate, and a real person on the phone if you need us."):
    return ('<section class="cta"><div class="wrap"><span class="eyebrow" %s>%s</span><h2 %s>%s</h2><p %s>%s</p>'
            '<div class="actions" %s><a class="btn btn-coral" href="%s" target="_blank" rel="noopener">Book Now</a>'
            '<a class="btn btn-light" href="%s">Call %s</a></div></div></section>'
            % (reveal(0), eyebrow, reveal(.05), h, reveal(.1), p, reveal(.15), BOOK_URL, PHONE_HREF, PHONE))


# ----------------------------------------------------------------- pages
def amen_grid(items):
    return "".join('<div %s><div class="amen"><span class="ico">%s</span><h3>%s</h3><p>%s</p></div></div>' % (reveal(), ic, e(t), e(d))
                   for ic, t, d in items)

def build_index():
    hero = ('<div class="hero">%s<div class="wrap"><span class="eyebrow">Boothbay Harbor · Maine</span>'
            '<h1>A true 1950s classic</h1>'
            '<p>A short walk from the waterfront, shops and restaurants, in a quiet, landscaped setting. Your home base for exploring the Boothbay area.</p>'
            '<div class="actions"><a class="btn btn-coral" href="%s" target="_blank" rel="noopener">Book Now</a>'
            '<a class="btn btn-light" href="rooms.html">View Rooms</a></div></div></div>' % (hero_bg(IMG["hero"]), BOOK_URL))

    stats = ('<div class="stats-wrap"><div class="wrap"><div class="stats">'
             '<div class="stat"><strong>10</strong><span>Guest rooms</span></div>'
             '<div class="stat"><strong>2 min</strong><span>Walk to the waterfront</span></div>'
             '<div class="stat"><strong>$159</strong><span>Rooms from / night</span></div>'
             '<div class="stat"><strong>3</strong><span>Dog-friendly rooms</span></div></div></div></div>')

    welcome = ('<section><div class="wrap split"><div %s><span class="eyebrow">Welcome</span><h2>Vintage charm, modern comfort</h2>'
               '<p class="lead">Mid-Town Motel is a vintage motor lodge with 1950s roots and decades of warm hospitality. We are a two-minute walk from Boothbay Harbor\'s waterfront, shops, galleries and restaurants, tucked into a quiet, landscaped setting.</p>'
               '<p style="margin:16px 0 28px;color:var(--muted)">Park the car, stroll to dinner, and come home to a comfy bed. It really is that easy.</p>'
               '<a class="btn btn-outline" href="about.html">Our story</a></div>'
               '<div class="visual" %s>%s</div></div></section>'
               % (reveal(), reveal(), photo("Mid-Town Motel", "", IMG["history"], "Mid-Town Motel in Boothbay Harbor")))

    rooms = ('<section class="bg-white"><div class="wrap"><div class="center"><span class="eyebrow">Rooms &amp; suites</span>'
             '<h2>Pick your room</h2><p class="lead">Ten guest rooms, including dog-friendly options, all near the harbor.</p></div>'
             '<div class="grid-4">%s</div><p class="center" style="margin-top:40px"><a class="btn btn-outline" href="rooms.html">See all rooms</a></p></div></section>'
             % "".join(room_card(r, i) for i, r in enumerate(ROOMS)))

    amen = ('<section class="bg-navy"><div class="wrap"><div class="center"><span class="eyebrow">Good to know</span><h2>Little comforts, big difference</h2></div>'
            '<div class="grid-4">%s</div></div></section>' % amen_grid(AMENITIES[:4]))

    offer = ('<section><div class="wrap"><div class="offer"><div class="big">10%<small>OFF</small></div>'
             '<div><h2>Military &amp; first responder rate</h2><p>Active and retired military personnel and first responders save 10% off the Best Available Rate on leisure stays when booking direct. Present a valid ID at check-in.</p></div>'
             '<a class="btn btn-coral" href="offers.html">See the offer</a></div></div></section>')

    guide = ('<section class="bg-white"><div class="wrap"><div class="center"><span class="eyebrow">Boothbay area guide</span><h2>Seaside scenery, seafood &amp; schooner sails</h2>'
             '<p class="lead">Beaches, villages, gardens and the best of the Maine midcoast, all close to your door.</p></div><div class="grid-3">%s</div>'
             '<p class="center" style="margin-top:40px"><a class="btn btn-outline" href="guide.html">Full guide</a></p></div></section>'
             % "".join(guide_card(g, i) for i, g in enumerate([GUIDE[4], GUIDE[5], GUIDE[8]])))

    loc = ('<section><div class="wrap split"><div class="visual"><div class="map"><iframe title="Map of Mid-Town Motel" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="%s"></iframe></div></div>'
           '<div><span class="eyebrow">Find us</span><h2>Right in downtown Boothbay Harbor</h2>'
           '<p class="lead">%s, %s. A two-minute walk to shops, restaurants, galleries and waterfront activities.</p>'
           '<div class="actions" style="margin-top:26px"><a class="btn btn-coral" href="%s" target="_blank" rel="noopener">Get directions</a>'
           '<a class="btn btn-outline" href="location.html">Location details</a></div></div></div></section>'
           % (MAP_EMBED, ADDRESS[0], ADDRESS[1], MAPS))

    ld = {"@context": "https://schema.org", "@type": "Motel", "name": "Mid-Town Motel", "url": SITE_URL,
          "telephone": "+1-207-633-2206", "email": EMAIL, "priceRange": "from $159",
          "petsAllowed": True, "checkinTime": "15:00", "checkoutTime": "11:00",
          "address": {"@type": "PostalAddress", "streetAddress": "96 McKown St", "addressLocality": "Boothbay Harbor",
                      "addressRegion": "ME", "postalCode": "04538", "addressCountry": "US"},
          "sameAs": [FB, IG]}
    head = '<script type="application/ld+json">%s</script>\n' % json.dumps(ld)
    page("index.html", "Mid-Town Motel | Retro 1950s Motel in Boothbay Harbor, Maine",
         "A true 1950s classic: a vintage motor lodge two minutes from the Boothbay Harbor waterfront. Ten rooms, dog-friendly options, book direct for the best rates.",
         hero, stats + welcome + rooms + amen + offer + guide + loc + cta(), head)

def build_rooms():
    hero = inner_hero("Rooms", "Rooms &amp; suites", "Ten guest rooms with one queen, one king or two twin beds, each sleeping up to two guests, steps from the Boothbay Harbor waterfront.", "Stay with us", IMG["rooms"])
    cards = '<section><div class="wrap"><div class="grid-2" style="margin-top:0">%s</div></div></section>' % "".join(room_card(r, i) for i, r in enumerate(ROOMS))
    included = ('<section class="bg-white"><div class="wrap split"><div %s><span class="eyebrow">Every stay includes</span><h2>The good stuff, already covered</h2>'
                '<p class="lead">Rates are for single or double occupancy and include Maine lodging tax, on-site parking and wireless internet.</p>'
                '<ul class="info-list" style="margin-top:18px"><li><b>Beds</b>One queen, one king or two twins</li><li><b>Guests</b>Maximum of two per room</li>'
                '<li><b>Check-in</b>3:00 to 7:00 pm</li><li><b>Check-out</b>11:00 am</li></ul></div>'
                '<div class="visual" %s>%s</div></div></section>'
                % (reveal(), reveal(), photo("Guest room", "pink", U + "22-DSC09889-1024x576.jpg", "Guest room")))
    amen = ('<section class="bg-navy"><div class="wrap"><div class="center"><span class="eyebrow">Amenities</span><h2>Comforts in every room</h2></div><div class="grid-4">%s</div></div></section>' % amen_grid(AMENITIES))
    page("rooms.html", "Rooms & Suites | Mid-Town Motel, Boothbay Harbor", "King, Queen (pet friendly), Two Twins and the Whole Property at Mid-Town Motel in Boothbay Harbor, Maine. Rooms from $159 a night.", hero, cards + included + amen + cta())

def build_about():
    hero = inner_hero("About", "A true 1950s classic", "A vintage motor lodge that has truly stood the test of time, and still treats every guest like a neighbor.", "Our story", IMG["about"])
    story = ('<section><div class="wrap split"><div %s><span class="eyebrow">Since the 1950s</span><h2>Warm hospitality, retro style</h2>'
             '<p class="lead">Mid-Town Motel is a vintage motor lodge with 1950s origins and decades of friendly service. We are a two-minute walk from the Boothbay Harbor waterfront, shops and restaurants, in a quiet, landscaped setting.</p>'
             '<p style="margin-top:16px;color:var(--muted)">Our goal is simple: warm, friendly service and real comfort, so Mid-Town is the perfect home base for exploring midcoast Maine.</p></div>'
             '<div class="visual" %s>%s</div></div></section>' % (reveal(), reveal(), photo("Mid-Town Motel", "warm", IMG["history"], "Mid-Town Motel")))
    amen = ('<section class="bg-navy"><div class="wrap"><div class="center"><span class="eyebrow">What you will find</span><h2>Amenities</h2></div><div class="grid-4">%s</div></div></section>' % amen_grid(AMENITIES))
    pets = ('<section><div class="wrap split"><div class="visual" %s>%s</div><div %s><span class="eyebrow">Four-legged guests</span><h2>Dogs are welcome</h2>'
            '<p class="lead">Pet-friendly accommodations are available in select Queen rooms with exterior entrances, and we have a doggie rest station with waste bags and a trash can.</p>'
            '<p style="margin:14px 0 26px;color:var(--muted)">Please call to reserve a dog-friendly room and read our pet policy first.</p>'
            '<div class="actions"><a class="btn btn-coral" href="policies.html">Pet policy</a><a class="btn btn-outline" href="%s">Call %s</a></div></div></div></section>'
            % (reveal(), photo("Dog-friendly rooms", "pink", U + "27-DSC09922-1024x576.jpg", "Dog-friendly Queen room"), reveal(), PHONE_HREF, PHONE))
    page("about.html", "About | Mid-Town Motel, Boothbay Harbor", "The story of Mid-Town Motel, a vintage 1950s motor lodge two minutes from the Boothbay Harbor waterfront.", hero, story + amen + pets + cta())

def build_offers():
    hero = inner_hero("Offers", "Make your stay extra special", "Book direct and save. Here is what is on right now.", "Specials", IMG["offers"])
    terms = ["Subject to availability and minimum-night requirements.", "Holiday weekends and other blackout periods may apply.",
             "Valid for guests with a current US or Canadian military and/or first responder ID, including active duty, reserve and retired service members, plus spouses and family sharing the same room.",
             "Present a current, valid ID card at check-in.", "Cannot be combined with any other discount or promotion."]
    body = ('<section><div class="wrap"><div class="offer"><div class="big">10%%<small>OFF</small></div>'
            '<div><h2>Military &amp; first responder</h2><p><b>Relax and unwind away from it all.</b> Active and retired military personnel and first responders get 10%% off the Best Available Rate on leisure stays. Book directly with us and the THANK YOU promo code is applied for you when you click through, or mention the discount when you call.</p></div>'
            '<a class="btn btn-coral" href="%s" target="_blank" rel="noopener">Book Now</a></div>'
            '<div class="faq" style="margin-top:56px"><details open><summary>Offer terms</summary><div class="ans"><ul>%s</ul></div></details></div></div></section>'
            % (BOOK_URL, "".join("<li>%s</li>" % e(t) for t in terms)))
    page("offers.html", "Offers | Mid-Town Motel, Boothbay Harbor", "10% off for military and first responders when you book direct at Mid-Town Motel in Boothbay Harbor, Maine.", hero, body + cta())

def build_guide():
    hero = inner_hero("Boothbay Guide", "Boothbay Harbor guide", "Seaside scenery, fresh seafood, schooner sails, beaches and villages: the best of the area, picked for you.", "Things to do", IMG["guide"])
    groups = {}
    for g in GUIDE:
        groups.setdefault(g[0], []).append(g)
    sections = ""
    for gi, (name, items) in enumerate(groups.items()):
        bg = ' class="bg-white"' if gi % 2 else ""
        sections += ('<section%s id="%s"><div class="wrap"><span class="eyebrow">Around Boothbay</span><h2>%s</h2><div class="grid-3" style="margin-top:30px">%s</div></div></section>'
                     % (bg, name.lower().replace(" & ", "-").replace(" ", "-"), e(name), "".join(guide_card(g, i) for i, g in enumerate(items))))
    eats = "".join('<article %s><div class="guide-card c%d"><span class="kicker">%s</span><h3>%s</h3><p>%s</p><a class="more" href="%s" target="_blank" rel="noopener">Visit website →</a></div></article>'
                   % (reveal(), i % 3 + 1, e(k), e(n), e(d), l) for i, (n, k, d, l) in enumerate(EATS))
    eats_sec = '<section class="bg-navy" id="local-eats"><div class="wrap"><span class="eyebrow">Local eats</span><h2>Where to eat</h2><div class="grid-3" style="margin-top:30px">%s</div></div></section>' % eats
    page("guide.html", "Boothbay Harbor Guide & Local Eats | Mid-Town Motel", "Things to do near Mid-Town Motel in Boothbay Harbor: beaches, clambakes, schooner sails, gardens, Monhegan Island and local restaurants.", hero, sections + eats_sec + cta())

def build_location():
    hero = inner_hero("Location", "Right in downtown Boothbay Harbor", "A two-minute walk from the waterfront, shops, galleries and restaurants.", "Find us", IMG["history"])
    body = ('<section><div class="wrap split"><div class="visual"><div class="map"><iframe title="Map of Mid-Town Motel" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="%s"></iframe></div></div>'
            '<div><h2>Visit Mid-Town Motel</h2><ul class="info-list">'
            '<li><b>Address</b><span>%s<br>%s</span></li><li><b>Phone</b><a href="%s">%s</a></li><li><b>Email</b><a href="mailto:%s">%s</a></li>'
            '<li><b>Walk</b><span>Two minutes to the waterfront, shops and restaurants</span></li><li><b>Parking</b><span>On-site parking is included with your stay</span></li></ul>'
            '<div class="actions" style="margin-top:26px"><a class="btn btn-coral" href="%s" target="_blank" rel="noopener">Driving directions</a></div></div></div></section>'
            % (MAP_EMBED, ADDRESS[0], ADDRESS[1], PHONE_HREF, PHONE, EMAIL, EMAIL, MAPS))
    page("location.html", "Location | Mid-Town Motel, Boothbay Harbor", "Mid-Town Motel, 96 McKown St, Boothbay Harbor, Maine, two minutes from the waterfront.", hero, body + cta())

def build_policies():
    hero = inner_hero("Policies", "Good to know before you go", "Deposits, cancellations, pets and house rules in plain English.", "Policies")
    det = "".join('<details%s><summary>%s</summary><div class="ans"><ul>%s</ul></div></details>'
                  % (" open" if i == 0 else "", e(t), "".join("<li>%s</li>" % e(x) for x in items)) for i, (t, items) in enumerate(POLICIES))
    body = '<section><div class="wrap"><div class="faq" style="margin-top:0">%s</div></div></section>' % det
    page("policies.html", "Policies | Mid-Town Motel, Boothbay Harbor", "Deposit, cancellation, pet, check-in and house policies for Mid-Town Motel in Boothbay Harbor, Maine.", hero, body + cta())

def build_gallery():
    hero = inner_hero("Photo Tour", "Boothbay Harbor &amp; property photo tour", "Click a photo to see it bigger.", "Take a look", IMG["gallery"])
    tiles = "".join('<div class="tile"><span>Photo %02d</span><img src="%s" alt="Mid-Town Motel photo %d" loading="lazy" onerror="this.remove()"></div>' % (i + 1, u, i + 1)
                    for i, u in enumerate(GALLERY))
    body = ('<section><div class="wrap"><div class="gallery">%s</div></div></section>'
            '<div class="lightbox" role="dialog" aria-label="Photo viewer"><button aria-label="Close">×</button><img alt=""></div>' % tiles)
    page("gallery.html", "Photo Tour | Mid-Town Motel, Boothbay Harbor", "Photos of Mid-Town Motel and Boothbay Harbor, Maine.", hero, body + cta())

def build_404():
    hero = inner_hero("Not found", "Looks like you took a wrong turn", "That page has checked out. Let's get you back to the lobby.", "404")
    page("404.html", "Page not found | Mid-Town Motel", "Page not found.", hero,
         '<section><div class="wrap center"><div class="actions" style="justify-content:center"><a class="btn btn-coral" href="index.html">Back home</a><a class="btn btn-outline" href="rooms.html">See rooms</a></div></div></section>')

if __name__ == "__main__":
    build_index(); build_rooms(); build_about(); build_offers(); build_guide()
    build_location(); build_policies(); build_gallery(); build_404()
