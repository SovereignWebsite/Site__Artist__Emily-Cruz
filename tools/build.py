#!/usr/bin/env python3
"""Builds site/index.html and site/designs/1-5.html from one set of facts.

Each design is a different idea from Emily's own world, built around it:
1 Programme (a theatre programme), 2 Blue light (the showcase stage),
3 Contact sheet (a photographer's proof sheet), 4 Score (a music score),
5 Brief (a plain, printable casting sheet).
Run: python3 tools/build.py   (no dependencies)
"""
from pathlib import Path
import html

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "site"
CHOSEN = 1  # the design index.html uses until Emily picks one

# ---------------------------------------------------------------- facts
SPOTLIGHT = "https://app.spotlight.com/5165-0192-6691"
GSA = "https://gsauk.org/2026-ba-hons-actor-musician-graduates"
REEL = "https://mediaviewer.spotlight.com/artist/showreels?artistRef=F179571&startClipId="
SHOWCASE_REEL = ("df1cff5d-ab84-4925-a414-c1125c5c5087", "Showcase: <em>They All Laughed</em>", "1 min 9 s", "poster-showcase",
                 "Emily Cruz singing with a double bass on a blue-lit stage", "Frame from the showcase reel")
INSTR_REEL = ("d802afde-26aa-47e4-86d7-dda00125ae6d", "Instrumental reel", "2 min 5 s", "poster-instrumental",
              "Emily Cruz playing an upright piano against a black background", "Frame from the instrumental reel")
SIZES = {  # width x height of the 720px versions
    "driving": (720, 922), "harvey-1": (720, 1086), "harvey-2": (720, 1086),
    "headshot": (720, 902), "piano": (720, 960), "reel-double-bass": (720, 1181),
    "reel-harp": (720, 874), "reel-piano-dark": (720, 546), "reel-piano-laugh": (720, 619),
    "reel-piano-smile": (720, 598), "reel-singing": (720, 1224),
}
HEADSHOT = ("headshot", "Emily Cruz, head and shoulders, against a sage green wall", "Photo © YellowBellyPhoto")
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
CREDITS = [  # year, production, type, role, director, company
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
TRAINING = "Guildford School of Acting, BA (Hons) Actor-Musician, 3 years, 2023 to 2026."
NOW = "As of November 2026, Emily is in the UK tour of <em>Pride and Prejudice* *(sort of)</em>, as 1st cover for Effie, Flo and Tillie."

DESIGNS = {
    1: ("Programme", "A theatre programme: a cover with her portrait, the credits as a cast list, the agent on the back page."),
    2: ("Blue light", "The showcase stage: dark first, her portrait lit out of the dark, the showreels as the main act."),
    3: ("Contact sheet", "A photographer's proof sheet: numbered frames on a film strip, each credit as its label; words after."),
    4: ("Score", "A music score: the instrumental reel as the overture, movements for sections, her skills on staves."),
    5: ("Brief", "The plain casting brief: one printable page for a casting director in a hurry."),
}

FAMILY_LINKS = """    <li><a href="https://sovereignwebsite.ai/">Sovereign Website</a></li>
    <li><a href="https://sovereignwebsite.org/">Principles</a></li>
    <li><a href="https://sovereignwebsite.site/">Hosted</a></li>
    <li><a href="https://hub.sovereignweb.site/">Hub</a></li>
    <li><a href="https://agents.sovereignweb.site/">Agents</a></li>
    <li><a href="https://vault.sovereignwebsite.site/">Vault</a></li>
    <li class="family-sep"><a href="https://agenticcells.ai/">AgentiCCells</a></li>
    <li><a href="https://riskmandate.ai/">RiskMandate</a></li>
    <li><a href="https://newsroom.sgit.ai/">Newsroom</a></li>"""  # from SovereignWebsite__Factory seed/shared/family-bar.html
# Full bar on wide screens; on phones it folds into one line (design.b, 20 November 2026). No script.
FAMILY = f"""<nav class="family" aria-label="The Sovereign Website family">
  <ul class="family-wide">
{FAMILY_LINKS}
  </ul>
  <details class="family-narrow"><summary>Sovereign Website family</summary><ul>
{FAMILY_LINKS}
  </ul></details>
</nav>"""  # from SovereignWebsite__Factory seed/shared/family-bar.html

# ---------------------------------------------------------------- pieces
GALLERY_SIZES = "(min-width: 68rem) 22rem, (min-width: 30rem) 50vw, 100vw"


def img(name, alt, pre, lazy=True, sizes=GALLERY_SIZES, big=False):
    w, h = SIZES[name]
    src = f"{pre}images/{name}"
    lz = ' loading="lazy" decoding="async"' if lazy else ' fetchpriority="high"'
    big_src = f", {src}-1400.webp 1400w" if big else ""
    return (f'<img src="{src}-720.webp" srcset="{src}-400.webp 400w, {src}-720.webp 720w{big_src}" sizes="{sizes}" '
            f'alt="{html.escape(alt)}" width="{w}" height="{h}"{lz}>')


def fig(item, pre, cls=""):
    name, alt, cap = item
    c = f' class="{cls}"' if cls else ""
    return f'<figure{c}><a href="{pre}images/{name}-1400.webp">{img(name, alt, pre)}</a><figcaption>{cap}</figcaption></figure>'


def reel(r, pre, h="h3"):
    cid, title, dur, poster, alt, cap = r
    p = f"{pre}images/{poster}"
    return f'''<article class="reel">
      <div class="frame" data-src="{REEL}{cid}">
        <a class="play" href="{REEL}{cid}">
          <img src="{p}-640.webp" srcset="{p}-640.webp 640w, {p}-1280.webp 1280w" sizes="(min-width: 46rem) 40rem, 100vw" alt="{html.escape(alt)}" width="640" height="360" loading="lazy" decoding="async">
          <span class="icon" aria-hidden="true"></span><span class="label">Play on Spotlight</span>
        </a>
      </div>
      <{h}>{title}</{h}>
      <p class="meta">{dur}. {cap}.</p>
    </article>'''


SPOT_NOTE = ('<p class="note">Spotlight hosts these reels. Nothing is sent to Spotlight until you press play; '
             'then your browser loads Spotlight\'s player from mediaviewer.spotlight.com, which sees your IP address '
             'and may set its own cookies.</p>')


def links_inline():
    return f'<a href="{SPOTLIGHT}">Spotlight profile</a> <span aria-hidden="true">·</span> <a href="{GSA}">GSA graduates 2026</a>'


def address():
    return '''<address>
    <strong>Galloways</strong><br>
    Henry Wood House, 4-5 Langham Place<br>
    London W1B 3DG<br>
    <a href="tel:+442076313134">020 7631 3134</a> or <a href="tel:+447752705359">07752 705359</a><br>
    <a href="mailto:agents@gallowaysagency.com">agents@gallowaysagency.com</a>
  </address>'''


def credits_table():
    rows = "".join(f'<tr><td>{y}</td><td><em>{html.escape(p)}</em><span class="type">{t}</span></td><td class="role">{r}</td><td>{d}</td><td>{c}</td></tr>'
                   for y, p, t, r, d, c in CREDITS)
    return f'''<div class="table-wrap" tabindex="0" role="region" aria-label="Credits table">
  <table class="credits">
    <thead><tr><th scope="col">Year</th><th scope="col">Production</th><th scope="col">Role</th><th scope="col">Director</th><th scope="col">Company</th></tr></thead>
    <tbody>{rows}</tbody>
  </table>
  </div>'''


def skills_tags():
    return '<div class="skills">' + "".join(
        f'<div><h3>{g}</h3><ul class="tags">{"".join(f"<li>{s}</li>" for s in items)}</ul></div>' for g, items in SKILLS) + "</div>"


def facts():
    return '<dl class="facts">' + "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in FACTS) + "</dl>"


# ---------------------------------------------------------------- 1 Programme
def programme(pre):
    name, alt, cap = HEADSHOT
    cast = "".join(f'''<li><span class="role">{r}</span><span class="dots" aria-hidden="true"></span><span class="prod"><em>{html.escape(p)}</em></span>
        <span class="by">{t}. {c}, {y}. Directed by {d}.</span></li>''' for y, p, t, r, d, c in CREDITS)
    stills = "".join(fig(s, pre) for s in PHOTOS + STILLS)
    return f'''<section class="cover" id="top" aria-labelledby="name">
  <figure class="cover-art">
    {img(name, alt, pre, lazy=False, sizes="(min-width: 46rem) 36rem, 100vw", big=True)}
    <div class="cover-title">
      <p class="kicker">Now on tour</p>
      <p class="show"><em>Pride and Prejudice* *(sort of)</em></p>
      <h1 id="name">Emily Cruz</h1>
      <p class="sub"><em>Actor-musician and artist</em>, she/her</p>
    </div>
    <figcaption>Cover: {cap}</figcaption>
  </figure>
  <div class="cover-foot">
    <p class="lead">{NOW}</p>
    <p><a class="btn primary" href="#contact">Contact her agent</a></p>
    <p class="links">{links_inline()}</p>
  </div>
</section>
<section id="credits" aria-labelledby="credits-h">
  <p class="kicker">The company</p>
  <h2 id="credits-h">Cast list</h2>
  <ol class="cast">{cast}</ol>
</section>
<section id="reels" aria-labelledby="reels-h">
  <p class="kicker">On screen</p>
  <h2 id="reels-h">Showreels</h2>
  {SPOT_NOTE}
  <div class="reels">{reel(SHOWCASE_REEL, pre)}{reel(INSTR_REEL, pre)}</div>
</section>
<section id="gallery" aria-labelledby="gallery-h">
  <p class="kicker">In rehearsal and on stage</p>
  <h2 id="gallery-h">Photographs</h2>
  <div class="gallery">{stills}</div>
</section>
<section id="skills" aria-labelledby="skills-h">
  <p class="kicker">Programme notes</p>
  <h2 id="skills-h">Skills</h2>
  {skills_tags()}
  {facts()}
</section>
<section id="company" aria-labelledby="company-h">
  <p class="kicker">About the company</p>
  <h2 id="company-h">Trained at Guildford School of Acting</h2>
  <p>{TRAINING}</p>
  <p><a href="{GSA}">The 2026 BA (Hons) Actor-Musician graduates, on the GSA site</a></p>
</section>
<section id="contact" class="back" aria-labelledby="contact-h">
  <p class="kicker">Back page</p>
  <h2 id="contact-h">Representation</h2>
  <p>For casting and all enquiries, please contact Emily's agent.</p>
  {address()}
  <p><a href="{SPOTLIGHT}">Spotlight profile</a></p>
</section>'''


# ---------------------------------------------------------------- 2 Blue light
def bluelight(pre):
    name, alt, cap = HEADSHOT
    gallery = "".join(fig(s, pre) for s in STILLS + PHOTOS)
    return f'''<section class="stage" id="top" aria-labelledby="name">
  <div class="spot">
    <figure>{img(name, alt, pre, lazy=False, sizes="(min-width: 46rem) 26rem, 80vw", big=True)}<figcaption>{cap}</figcaption></figure>
  </div>
  <div class="billing">
    <p class="kicker">Actor-musician and artist, she/her</p>
    <h1 id="name">Emily Cruz</h1>
    <p class="lead">{NOW}</p>
    <p><a class="btn primary" href="#contact">Contact her agent</a></p>
    <p class="links">{links_inline()}</p>
  </div>
</section>
<section id="reels" class="main-act" aria-labelledby="reels-h">
  <p class="kicker">The main act</p>
  <h2 id="reels-h">Showreels</h2>
  {SPOT_NOTE}
  <div class="acts">{reel(SHOWCASE_REEL, pre)}{reel(INSTR_REEL, pre)}</div>
</section>
<section id="gallery" aria-labelledby="gallery-h">
  <h2 id="gallery-h">Under the lights</h2>
  <div class="gallery">{gallery}</div>
</section>
<section id="credits" aria-labelledby="credits-h">
  <h2 id="credits-h">Credits</h2>
  {credits_table()}
  <h3>Training</h3>
  <p>{TRAINING}</p>
</section>
<section id="skills" aria-labelledby="skills-h">
  <h2 id="skills-h">Skills</h2>
  {skills_tags()}
  {facts()}
</section>
<section id="contact" aria-labelledby="contact-h">
  <h2 id="contact-h">Representation</h2>
  <p>For casting and all enquiries, please contact Emily's agent.</p>
  {address()}
</section>'''


# ---------------------------------------------------------------- 3 Contact sheet
def contactsheet(pre):
    frames = "".join(f'''<li class="frame-cell"><a href="{pre}images/{n}-1400.webp">{img(n, a, pre, lazy=i > 3, sizes="(min-width: 68rem) 16rem, (min-width: 30rem) 33vw, 50vw")}</a>
      <p class="label"><span class="no">{i + 1:02d}A</span> {c}</p></li>'''
                     for i, (n, a, c) in enumerate([HEADSHOT] + PHOTOS + STILLS))
    return f'''<section class="sheet" id="top" aria-labelledby="name">
  <header class="sheet-head">
    <h1 id="name">Emily Cruz</h1>
    <p>Roll 1. Actor-musician and artist, she/her. {len(PHOTOS) + len(STILLS) + 1} frames. Tap a frame for the full print.</p>
  </header>
  <ol class="strip">{frames}</ol>
</section>
<section id="about" aria-labelledby="about-h">
  <h2 id="about-h">Notes on the sheet</h2>
  <p class="lead">{NOW}</p>
  <p>{TRAINING} Based in Greater London.</p>
  <p><a class="btn primary" href="#contact">Contact her agent</a> &nbsp; {links_inline()}</p>
</section>
<section id="reels" aria-labelledby="reels-h">
  <h2 id="reels-h">Showreels</h2>
  {SPOT_NOTE}
  <div class="reels">{reel(SHOWCASE_REEL, pre)}{reel(INSTR_REEL, pre)}</div>
</section>
<section id="credits" aria-labelledby="credits-h">
  <h2 id="credits-h">Credits</h2>
  {credits_table()}
</section>
<section id="skills" aria-labelledby="skills-h">
  <h2 id="skills-h">Skills</h2>
  {skills_tags()}
  {facts()}
</section>
<section id="contact" aria-labelledby="contact-h">
  <h2 id="contact-h">Representation</h2>
  <p>For casting and all enquiries, please contact Emily's agent.</p>
  {address()}
</section>'''


# ---------------------------------------------------------------- 4 Score
def score(pre):
    name, alt, cap = HEADSHOT
    staves = "".join(f'''<div class="stave-row"><h3>{g}</h3><ol class="stave">{"".join(f"<li>{s}</li>" for s in items)}</ol></div>'''
                     for g, items in SKILLS)
    repertoire = "".join(f'<li><span class="bar-no">{len(CREDITS) - i}</span><em>{html.escape(p)}</em> <span class="role">{r}</span><span class="by">{c}, {y}. Directed by {d}.</span></li>'
                         for i, (y, p, t, r, d, c) in enumerate(CREDITS))
    stills = "".join(fig(s, pre) for s in STILLS[1::2] + STILLS[0::2] + PHOTOS)
    return f'''<section class="title-page" id="top" aria-labelledby="name">
  <div class="title-text">
    <p class="kicker">A portfolio in five movements</p>
    <h1 id="name">Emily Cruz</h1>
    <p class="for"><em>for voice, piano, accordion, guitar, bass guitar, double bass and saxophones</em></p>
    <p class="lead">{NOW}</p>
    <p><a class="btn primary" href="#contact">Contact her agent</a></p>
    <p class="links">{links_inline()}</p>
  </div>
  <figure class="title-portrait">{img(name, alt, pre, lazy=False, sizes="(min-width: 46rem) 22rem, 70vw", big=True)}<figcaption>{cap}</figcaption></figure>
</section>
<section id="reels" class="movement" aria-labelledby="reels-h">
  <h2 id="reels-h"><span class="mv">I.</span> Overture <span class="tempo">Showreels, instrumental first</span></h2>
  {SPOT_NOTE}
  <div class="reels">{reel(INSTR_REEL, pre)}{reel(SHOWCASE_REEL, pre)}</div>
</section>
<section id="skills" class="movement" aria-labelledby="skills-h">
  <h2 id="skills-h"><span class="mv">II.</span> Instrumentation <span class="tempo">Skills</span></h2>
  <div class="staves">{staves}</div>
  {facts()}
</section>
<section id="credits" class="movement" aria-labelledby="credits-h">
  <h2 id="credits-h"><span class="mv">III.</span> Repertoire <span class="tempo">Credits, latest first</span></h2>
  <ol class="repertoire" reversed>{repertoire}</ol>
  <p class="training"><strong>Training.</strong> {TRAINING}</p>
</section>
<section id="gallery" class="movement" aria-labelledby="gallery-h">
  <h2 id="gallery-h"><span class="mv">IV.</span> Interlude <span class="tempo">Photographs</span></h2>
  <div class="gallery">{stills}</div>
</section>
<section id="contact" class="movement" aria-labelledby="contact-h">
  <h2 id="contact-h"><span class="mv">V.</span> Coda <span class="tempo">Representation</span></h2>
  <p>For casting and all enquiries, please contact Emily's agent.</p>
  {address()}
</section>'''


# ---------------------------------------------------------------- 5 Brief
def brief(pre):
    name, alt, cap = HEADSHOT
    gallery = "".join(fig(s, pre) for s in PHOTOS + STILLS)
    return f'''<section class="brief-top" id="top" aria-labelledby="name">
  <figure>{img(name, alt, pre, lazy=False, sizes="(min-width: 46rem) 16rem, 60vw")}<figcaption>{cap}</figcaption></figure>
  <div>
    <h1 id="name">Emily Cruz</h1>
    <p class="sub">Actor-musician and artist, she/her</p>
    <p>{NOW}</p>
    <dl class="facts brief-facts"><div><dt>Agent</dt><dd><a href="#contact">Galloways</a></dd></div>{"".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in FACTS)}<div><dt>Training</dt><dd>GSA, BA (Hons) Actor-Musician, 2023 to 2026</dd></div></dl>
    <p class="links"><a href="{SPOTLIGHT}">Spotlight profile</a> <span aria-hidden="true">·</span> <a href="#reels">Showreels</a> <span aria-hidden="true">·</span> <a href="{GSA}">GSA graduates 2026</a></p>
  </div>
</section>
<section id="credits" aria-labelledby="credits-h">
  <h2 id="credits-h">Credits</h2>
  {credits_table()}
</section>
<section id="skills" aria-labelledby="skills-h">
  <h2 id="skills-h">Skills</h2>
  <dl class="skill-lines">{"".join(f"<div><dt>{g}</dt><dd>{', '.join(items)}</dd></div>" for g, items in SKILLS)}</dl>
</section>
<section id="contact" aria-labelledby="contact-h">
  <h2 id="contact-h">Representation</h2>
  {address()}
</section>
<section id="reels" class="no-print" aria-labelledby="reels-h">
  <h2 id="reels-h">Showreels</h2>
  {SPOT_NOTE}
  <div class="reels">{reel(SHOWCASE_REEL, pre)}{reel(INSTR_REEL, pre)}</div>
</section>
<section id="gallery" class="no-print" aria-labelledby="gallery-h">
  <h2 id="gallery-h">Photographs</h2>
  <div class="gallery">{gallery}</div>
</section>'''


BODIES = {1: programme, 2: bluelight, 3: contactsheet, 4: score, 5: brief}
NAVS = {
    1: [("credits", "Cast list"), ("reels", "Reels"), ("gallery", "Photos"), ("skills", "Skills"), ("contact", "Contact")],
    2: [("reels", "Reels"), ("gallery", "Photos"), ("credits", "Credits"), ("skills", "Skills"), ("contact", "Contact")],
    3: [("about", "Notes"), ("reels", "Reels"), ("credits", "Credits"), ("skills", "Skills"), ("contact", "Contact")],
    4: [("reels", "I Reels"), ("skills", "II Skills"), ("credits", "III Credits"), ("gallery", "IV Photos"), ("contact", "V Agent")],
    5: [("credits", "Credits"), ("skills", "Skills"), ("contact", "Agent"), ("reels", "Reels"), ("gallery", "Photos")],
}
CSP = ("default-src 'self'; img-src 'self'; style-src 'self'; script-src 'self'; "
       "frame-src https://mediaviewer.spotlight.com; base-uri 'none'; form-action 'none'")


def page(n, pre, switcher):
    nav = "".join(f'<a href="#{i}">{t}</a>' for i, t in NAVS[n])
    name, idea = DESIGNS[n]
    # "Choose a design" on every page, the live one included (Dinis Cruz, 20 November 2026).
    base = "" if switcher else "designs/"
    links = "".join(f'<li><a href="{base}{k}.html"{" aria-current=\"page\"" if k == n and switcher else ""}>{k}. {v[0]}</a></li>' for k, v in DESIGNS.items())
    where = (f'<span class="idea">Design {n} of 5: <strong>{name}</strong>. {idea}</span> <a href="index.html">All five</a> · <a href="../index.html">Home</a>'
             if switcher else f'<span class="idea">You are looking at design {n} of 5, <strong>{name}</strong>.</span> <a href="designs/index.html">All five</a>')
    sw = f'''<nav class="switcher" aria-label="Choose a design">
  <p><strong>Choose a design:</strong> {where}</p>
  <ul>{links}</ul>
</nav>'''
    title = "Emily Cruz" if not switcher else f"Design {n}, {name}, Emily Cruz"
    theme = f"{pre}theme.css" if not switcher else f"d{n}.css"
    return f'''<!doctype html>
<html lang="en-GB" class="d{n}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="Content-Security-Policy" content="{CSP}">
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
<main id="main" tabindex="-1">
{BODIES[n](pre)}
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
<link rel="stylesheet" href="d5.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
{FAMILY}
<header class="bar"><a class="brand" href="../index.html">Emily Cruz</a></header>
<main id="main" tabindex="-1">
<section>
<h1>Five designs</h1>
<p>The same facts and photographs, each built around a different idea from Emily's world. Emily chooses one; it becomes the live site. Until then the live site uses design {CHOSEN}, {DESIGNS[CHOSEN][0]}.</p>
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
    theme = (SITE / "designs" / f"d{CHOSEN}.css").read_text()
    (SITE / "theme.css").write_text(theme)
    print(f"built index.html (design {CHOSEN}, {DESIGNS[CHOSEN][0]}) and designs/1-5.html")
