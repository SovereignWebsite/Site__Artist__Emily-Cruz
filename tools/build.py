#!/usr/bin/env python3
"""Builds site/index.html and site/designs/1-5.html from one set of content.

Every design shows the same facts; only order, layout and style change.
Run: python3 tools/build.py   (no dependencies)
"""
from pathlib import Path
import html

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "site"
CHOSEN = 1  # the design index.html uses until Emily picks one

SPOTLIGHT = "https://app.spotlight.com/5165-0192-6691"
GSA = "https://gsauk.org/2026-ba-hons-actor-musician-graduates"
REEL = "https://mediaviewer.spotlight.com/artist/showreels?artistRef=F179571&startClipId="
REELS = [
    ("df1cff5d-ab84-4925-a414-c1125c5c5087", "Showcase: <em>They All Laughed</em>", "1 min 9 s"),
    ("d802afde-26aa-47e4-86d7-dda00125ae6d", "Instrumental reel", "2 min 5 s"),
]
SIZES = {  # width x height of the 720px versions
    "driving": (720, 922), "harvey-1": (720, 1086), "harvey-2": (720, 1086),
    "headshot": (720, 902), "piano": (720, 960), "reel-double-bass": (720, 1181),
    "reel-harp": (720, 874), "reel-piano-dark": (720, 546), "reel-piano-laugh": (720, 619),
    "reel-piano-smile": (720, 598), "reel-singing": (720, 1224),
}
SHOWCASE = "Still from the showcase reel, <em>They All Laughed</em>"
INSTR = "Still from the instrumental reel"
PHOTOS = [
    ("harvey-1", "Emily Cruz, close portrait against a grey background, smiling softly", "Photo © shot_byharvey"),
    ("piano", "Emily Cruz playing a grand piano in a bright room, smiling at the camera", "Photo © Dinis Cruz"),
    ("harvey-2", "Emily Cruz, close portrait against a grey background, laughing", "Photo © shot_byharvey"),
    ("driving", "Emily Cruz smiling from the driver's seat of a car, window down", "Photo © Dinis Cruz"),
]
STILLS = [
    ("reel-double-bass", "Emily Cruz on stage under blue light, smiling, playing double bass", SHOWCASE),
    ("reel-piano-smile", "Emily Cruz smiling as she plays a digital piano", INSTR),
    ("reel-harp", "Emily Cruz laughing as she leans on a concert harp on stage", SHOWCASE),
    ("reel-piano-dark", "Emily Cruz playing an upright piano against a black background", INSTR),
    ("reel-singing", "Emily Cruz singing on stage under blue light", SHOWCASE),
    ("reel-piano-laugh", "Emily Cruz laughing at the piano", INSTR),
]
CREDITS = [
    ("2026", "Pride and Prejudice* *(sort of)", "Stage, UK tour", "1st Cover: Effie, Flo, Tillie", "Isobel McArthur", "David Pugh"),
    ("2026", "Vinegar Tom", "Stage", "Musical Director/Ensemble", "Amy Wallace", "Guildford School of Acting"),
    ("2026", "Saturday Night", "Musical", "Dino", "Simon Hardwick", "Guildford School of Acting"),
    ("2025", "The All New Adventures of Peter Pan", "Pantomime", "Assistant MD", "Will Kenning/Eoin Mallon", "Evolution Productions"),
    ("2025", "I Should Be So Lucky", "Workshop", "Bonnie", "Stuart Morley", "ATG Productions"),
    ("2025", "Tom's Midnight Garden", "Stage", "Aunt Grace", "Cressida Carré", "Guildford School of Acting"),
    ("2025", "Into The Woods", "Musical", "Keys 2", "Owen White", "Project Theatre Company"),
    ("2025", "She Loves Me", "Musical", "Maraczek", "Phyllida Crowley Smith", "Guildford School of Acting"),
    ("2025", "Twelve Angry Men", "Stage", "Juror 3", "Anna Tringham", "Guildford School of Acting"),
    ("2024", "Coriolanus", "Stage", "Sicinius", "Chris Palmer", "Guildford School of Acting"),
]
SKILLS = [
    ("Music", ["Alto (voice)", "Piano", "Accordion", "Guitar", "Bass guitar", "Double bass", "Alto saxophone", "Tenor saxophone", "Musical director"]),
    ("Dance", ["Commercial", "Jazz", "Tap", "Hip hop"]),
    ("Accents and dialects", ["Standard English", "RP", "Heightened RP", "Cockney", "West Country", "Northern Irish", "American: East Coast", "American: New York", "American: Southern States", "Portuguese", "Spanish"]),
    ("Languages", ["English", "Portuguese", "Spanish"]),
    ("Performance", ["Actor-musician", "Laban training"]),
    ("Other", ["Painting", "Crochet", "Knitting", "Cycling", "Field hockey", "Football", "Netball", "Swimming", "Car driving licence"]),
]
FACTS = [("Playing age", "15 to 25"), ("Height", "5 ft 5 in (165 cm)"), ("Hair", "Light/mid brown, mid length"),
         ("Eyes", "Hazel"), ("Nationalities", "British, Portuguese"), ("Location", "Greater London")]

DESIGNS = {
    1: ("Sage", "Quiet: the first page, grown up. Sage green, plain sans, photo and words side by side."),
    2: ("Programme", "Editorial: set like a theatre programme. Cream paper, serif type, credits first."),
    3: ("Blue light", "Bold: the deep blue of her showcase stage, amber type, showreels up front."),
    4: ("Contact sheet", "Gallery: the photographs lead, words come after."),
    5: ("Score", "Unexpected: the page read as a piece of music, in numbered bars."),
}


GALLERY_SIZES = "(min-width: 68rem) 33rem, (min-width: 30rem) 50vw, 100vw"
HERO_SIZES = "(min-width: 46rem) 30rem, 100vw"


def img(name, alt, pre, lazy=True, cls="", sizes=GALLERY_SIZES):
    w, h = SIZES[name]
    lz = ' loading="lazy" decoding="async"' if lazy else ' fetchpriority="high"'
    c = f' class="{cls}"' if cls else ""
    src = f"{pre}images/{name}"
    return (f'<a href="{src}-1400.webp"{c}><img src="{src}-720.webp" '
            f'srcset="{src}-400.webp 400w, {src}-720.webp 720w" sizes="{sizes}" '
            f'alt="{html.escape(alt)}" width="{w}" height="{h}"{lz}></a>')


def fig(item, pre, lazy=True):
    name, alt, cap = item
    return f'<figure>{img(name, alt, pre, lazy)}<figcaption>{cap}</figcaption></figure>'


def hero(pre):
    return f'''<section class="hero" id="top">
  <figure class="hero-photo">{img("headshot", "Emily Cruz, head and shoulders, against a sage green wall", pre, lazy=False, sizes=HERO_SIZES)}<figcaption>Photo © YellowBellyPhoto</figcaption></figure>
  <div class="hero-text">
    <p class="eyebrow">Actor-musician and artist</p>
    <h1>Emily Cruz</h1>
    <p class="pronouns">she/her</p>
    <p class="lead">Emily is in the UK tour of <em>Pride and Prejudice* *(sort of)</em>, as 1st cover for Effie, Flo and Tillie.</p>
    <p>She trained on the BA (Hons) Actor-Musician course at Guildford School of Acting, 2023 to 2026, and is based in Greater London.</p>
    <ul class="actions">
      <li><a class="btn primary" href="#contact">Contact her agent, Galloways</a></li>
      <li><a class="btn" href="{SPOTLIGHT}">Spotlight profile</a></li>
      <li><a class="btn" href="{GSA}">GSA graduates 2026</a></li>
    </ul>
  </div>
</section>'''


def reels():
    items = "".join(f'''
    <article class="reel">
      <div class="frame" data-src="{REEL}{cid}">
        <a class="play" href="{REEL}{cid}"><span class="icon" aria-hidden="true"></span><span>Play on Spotlight</span></a>
      </div>
      <h3>{title}</h3>
      <p class="meta">{dur}</p>
    </article>''' for cid, title, dur in REELS)
    return f'''<section id="reels" aria-labelledby="reels-h">
  <h2 id="reels-h">Showreels</h2>
  <p class="note">Spotlight hosts these reels. Nothing is sent to Spotlight until you press play; then your browser loads Spotlight's player from mediaviewer.spotlight.com, which sees your IP address and may set its own cookies.</p>
  <div class="reels">{items}
  </div>
</section>'''


def gallery(pre):
    photos = "".join(fig(p, pre) for p in PHOTOS)
    stills = "".join(fig(s, pre) for s in STILLS)
    return f'''<section id="gallery" aria-labelledby="gallery-h">
  <h2 id="gallery-h">Gallery</h2>
  <div class="gallery">{photos}</div>
  <h3>From the showreels</h3>
  <div class="gallery stills">{stills}</div>
</section>'''


def credits():
    rows = "".join(f'<tr><td>{y}</td><td><em>{html.escape(p)}</em><span class="type">{t}</span></td><td>{r}</td><td>{d}</td><td>{c}</td></tr>'
                   for y, p, t, r, d, c in CREDITS)
    return f'''<section id="credits" aria-labelledby="credits-h">
  <h2 id="credits-h">Credits</h2>
  <div class="table-wrap" tabindex="0" role="region" aria-label="Credits table">
  <table>
    <thead><tr><th scope="col">Year</th><th scope="col">Production</th><th scope="col">Role</th><th scope="col">Director</th><th scope="col">Company</th></tr></thead>
    <tbody>{rows}</tbody>
  </table>
  </div>
  <h3>Training</h3>
  <p>Guildford School of Acting, BA (Hons) Actor-Musician, 3 years, 2023 to 2026.</p>
</section>'''


def skills():
    groups = "".join(f'<div><h3>{g}</h3><ul class="tags">{"".join(f"<li>{s}</li>" for s in items)}</ul></div>' for g, items in SKILLS)
    facts = "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in FACTS)
    return f'''<section id="skills" aria-labelledby="skills-h">
  <h2 id="skills-h">Skills</h2>
  <div class="skills">{groups}</div>
  <dl class="facts">{facts}</dl>
</section>'''


def contact():
    return f'''<section id="contact" aria-labelledby="contact-h" class="contact">
  <h2 id="contact-h">Representation</h2>
  <p>For casting and all enquiries, please contact Emily's agent.</p>
  <address>
    <strong>Galloways</strong><br>
    Henry Wood House, 4-5 Langham Place<br>
    London W1B 3DG<br>
    <a href="tel:+442076313134">020 7631 3134</a> or <a href="tel:+447752705359">07752 705359</a><br>
    <a href="mailto:agents@gallowaysagency.com">agents@gallowaysagency.com</a>
  </address>
  <p><a class="btn" href="{SPOTLIGHT}">Spotlight profile</a></p>
</section>'''


ORDER = {  # section order per design: the idea, not only the colour
    1: ["hero", "reels", "gallery", "credits", "skills", "contact"],
    2: ["hero", "credits", "reels", "gallery", "skills", "contact"],
    3: ["hero", "reels", "credits", "gallery", "skills", "contact"],
    4: ["hero", "gallery", "reels", "credits", "skills", "contact"],
    5: ["hero", "reels", "credits", "skills", "gallery", "contact"],
}
NAV = [("reels", "Showreels"), ("gallery", "Gallery"), ("credits", "Credits"), ("skills", "Skills"), ("contact", "Contact")]


FAMILY = """<nav class="family" aria-label="The Sovereign Website family">
  <ul>
    <li><a href="https://sovereignwebsite.ai/">Sovereign Website</a></li>
    <li><a href="https://sovereignwebsite.org/">Principles</a></li>
    <li><a href="https://sovereignwebsite.site/">Hosted</a></li>
    <li><a href="https://hub.sovereignweb.site/">Hub</a></li>
    <li><a href="https://agents.sovereignweb.site/">Agents</a></li>
    <li><a href="https://vault.sovereignwebsite.site/">Vault</a></li>
    <li class="family-sep"><a href="https://agenticcells.ai/">AgentiCCells</a></li>
    <li><a href="https://riskmandate.ai/">RiskMandate</a></li>
    <li><a href="https://newsroom.sgit.ai/">Newsroom</a></li>
  </ul>
</nav>"""  # from SovereignWebsite__Factory seed/shared/family-bar.html


def page(n, pre, switcher):
    parts = {"hero": lambda: hero(pre), "reels": reels, "gallery": lambda: gallery(pre),
             "credits": credits, "skills": skills, "contact": contact}
    body = "\n".join(parts[s]() for s in ORDER[n])
    nav = "".join(f'<a href="#{i}">{t}</a>' for i, t in NAV)
    name, idea = DESIGNS[n]
    sw = ""
    if switcher:
        links = "".join(f'<li><a href="{k}.html"{" aria-current=\"page\"" if k == n else ""}>{k}. {v[0]}</a></li>' for k, v in DESIGNS.items())
        sw = f'''<aside class="switcher" aria-label="Design choices">
  <p><strong>Design {n} of 5: {name}.</strong> <span class="idea">{idea}</span> <a href="index.html">All five</a> · <a href="../index.html">Live site</a></p>
  <ul>{links}</ul>
</aside>'''
    title = "Emily Cruz" if not switcher else f"Design {n}, {name}, Emily Cruz"
    theme = f"{pre}theme.css" if not switcher else f"d{n}.css"
    return f'''<!doctype html>
<html lang="en-GB" class="d{n}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="Content-Security-Policy" content="default-src 'self'; img-src 'self'; style-src 'self'; script-src 'self'; frame-src https://mediaviewer.spotlight.com; base-uri 'none'; form-action 'none'">
<meta name="referrer" content="strict-origin-when-cross-origin">
<title>{title}</title>
<meta name="description" content="Emily Cruz, actor-musician and artist. BA (Hons) Actor-Musician, Guildford School of Acting, 2026. Represented by Galloways.">
<meta name="color-scheme" content="light dark">
<link rel="icon" href="{pre}favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="{pre}base.css">
<link rel="stylesheet" href="{theme}">
<script src="{pre}reels.js" defer></script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
{FAMILY}
{sw}
<header class="bar">
  <a class="brand" href="#top">Emily Cruz</a>
  <nav aria-label="Sections">{nav}</nav>
</header>
<main id="main">
{body}
</main>
<footer>
  <p>A sovereign website: Emily's own files, history and address. No cookies, no tracking, no third-party scripts. The showreels come from Spotlight only when you press play. Text licensed <a href="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a>; photographs remain their photographers'. Source: <a href="https://github.com/SovereignWebsite/Site__Artist__Emily-Cruz">SovereignWebsite/Site__Artist__Emily-Cruz</a>.</p>
</footer>
</body>
</html>
'''


def designs_index():
    cards = "".join(f'<li><a href="{k}.html"><strong>{k}. {v[0]}</strong></a><p>{v[1]}</p></li>' for k, v in DESIGNS.items())
    return f'''<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="Content-Security-Policy" content="default-src 'self'; style-src 'self'; base-uri 'none'; form-action 'none'">
<title>Five designs, Emily Cruz</title>
<meta name="color-scheme" content="light dark">
<link rel="icon" href="../favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="../base.css">
<link rel="stylesheet" href="d1.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="bar"><a class="brand" href="../index.html">Emily Cruz</a></header>
<main id="main">
<section>
<h1>Five designs</h1>
<p>The same facts and photographs, set five ways. Emily chooses one; it becomes the live site. The live site uses design {CHOSEN} until then.</p>
<ol class="design-list">{cards}</ol>
</section>
</main>
</body>
</html>
'''


if __name__ == "__main__":
    (SITE / "designs").mkdir(exist_ok=True)
    (SITE / "index.html").write_text(page(CHOSEN, "", switcher=False))
    for n in DESIGNS:
        (SITE / "designs" / f"{n}.html").write_text(page(n, "../", switcher=True))
    (SITE / "designs" / "index.html").write_text(designs_index())
    (SITE / "theme.css").write_text((SITE / "designs" / f"d{CHOSEN}.css").read_text())
    print("built index.html (design", CHOSEN, ") and designs/1-5.html")
