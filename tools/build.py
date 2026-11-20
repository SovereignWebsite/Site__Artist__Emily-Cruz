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
    """A cinematic poster frame; the play control is part of the frame. Nothing loads from Spotlight until pressed."""
    cid, title, dur, poster, alt, cap = r
    p = f"{pre}images/{poster}"
    plain = html.unescape(title.replace("<em>", "").replace("</em>", ""))
    return f'''<figure class="reel">
      <div class="frame" data-src="{REEL}{cid}" data-title="{html.escape(plain)}">
        <a class="play" href="{REEL}{cid}">
          <img src="{p}-640.webp" srcset="{p}-640.webp 640w, {p}-1280.webp 1280w" sizes="(min-width: 46rem) 64rem, 100vw" alt="{html.escape(alt)}" width="1280" height="720" loading="lazy" decoding="async">
          <span class="reel-title">{title}</span>
          <span class="reel-cta"><span class="icon" aria-hidden="true"></span><span>Play on Spotlight</span><span class="dur">{dur}</span></span>
        </a>
      </div>
      <figcaption class="meta">{cap}.</figcaption>
    </figure>'''


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
def spread(items, pre, cls="spread"):
    figs = "".join(f'<figure><a href="{pre}images/{n}-1400.webp">{img(n, a, pre, sizes="(min-width: 46rem) 34vw, 100vw")}</a><figcaption>{c}</figcaption></figure>'
                   for n, a, c in items)
    return f'<div class="{cls} bleed">{figs}</div>'


def programme(pre):
    name, alt, cap = HEADSHOT
    cast = "".join(f'''<li><span class="role">{r}</span><span class="dots" aria-hidden="true"></span><span class="prod"><em>{html.escape(p)}</em></span>
        <span class="by">{c}, {y}. Directed by {d}.</span></li>''' for y, p, t, r, d, c in CREDITS)
    sep = ' <span aria-hidden="true">·</span> '
    notes = "".join(f'<div><h3>{g}</h3><p>{sep.join(items)}</p></div>' for g, items in SKILLS)
    return f'''<section class="cover bleed" id="top" aria-labelledby="name">
  {img(name, alt, pre, lazy=False, sizes="100vw", big=True)}
  <div class="cover-text">
    <p class="kicker">Now on tour <span aria-hidden="true">·</span> <em>Pride and Prejudice* *(sort of)</em></p>
    <h1 id="name">Emily <span>Cruz</span></h1>
    <p class="sub">Actor-musician and artist</p>
  </div>
  <p class="photo-credit">Cover {cap}</p>
</section>
<section class="band bleed" aria-label="Now">
  <p class="lead">{NOW}</p>
  <p class="cta"><a class="btn primary" href="#contact">Contact her agent</a> <span class="links">{links_inline()}</span></p>
</section>
<section id="credits" class="cast-page bleed" aria-labelledby="credits-h">
  <p class="kicker">The company</p>
  <h2 id="credits-h">Credits</h2>
  <ol class="cast">{cast}</ol>
</section>
{spread(PHOTOS[:3], pre)}
<section id="reels" class="screen bleed" aria-labelledby="reels-h">
  <p class="kicker">On screen</p>
  <h2 id="reels-h">Showreels</h2>
  {SPOT_NOTE}
  <div class="reels">{reel(SHOWCASE_REEL, pre)}{reel(INSTR_REEL, pre)}</div>
</section>
<section id="gallery" class="plates" aria-labelledby="gallery-h">
  <p class="kicker">In performance</p>
  <h2 id="gallery-h">Photographs</h2>
  {spread(STILLS + [PHOTOS[3]], pre, cls="mosaic")}
</section>
<section id="skills" class="notes" aria-labelledby="skills-h">
  <p class="kicker">Programme notes</p>
  <h2 id="skills-h">Skills</h2>
  <div class="note-cols">{notes}</div>
  {facts()}
</section>
<section id="company" class="company bleed" aria-labelledby="company-h">
  <p class="kicker">About the company</p>
  <h2 id="company-h">Trained at Guildford School of Acting</h2>
  <p>{TRAINING}</p>
  <p><a href="{GSA}">The 2026 BA (Hons) Actor-Musician graduates, on the GSA site</a></p>
</section>
<section id="contact" class="back bleed" aria-labelledby="contact-h">
  <div class="back-frame">
    <p class="kicker">Representation</p>
    <h2 id="contact-h">Galloways</h2>
    <p>For casting and all enquiries, please contact Emily's agent.</p>
    {address()}
    <p><a href="{SPOTLIGHT}">Spotlight profile</a></p>
  </div>
</section>'''


# ---------------------------------------------------------------- 2 Blue light
def bluelight(pre):
    name, alt, cap = HEADSHOT
    gallery = "".join(fig(s, pre) for s in STILLS + PHOTOS)
    return f'''<section class="stage bleed" id="top" aria-labelledby="name">
  <div class="haze" aria-hidden="true"></div><div class="cone" aria-hidden="true"></div>
  <figure class="lit">{img(name, alt, pre, lazy=False, sizes="(min-width: 46rem) 30rem, 64vw", big=True)}</figure>
  <div class="billing">
    <p class="kicker">Actor-musician and artist</p>
    <h1 id="name">Emily Cruz</h1>
    <p class="lead">{NOW}</p>
    <p class="cta"><a class="btn primary" href="#contact">Contact her agent</a> <span class="links">{links_inline()}</span></p>
  </div>
  <p class="photo-credit">{cap}</p>
</section>
<section id="reels" class="main-act bleed" aria-labelledby="reels-h">
  <p class="kicker">The main act</p>
  <h2 id="reels-h">Showreels</h2>
  {SPOT_NOTE}
  <div class="acts">{reel(SHOWCASE_REEL, pre)}{reel(INSTR_REEL, pre)}</div>
</section>
<section id="gallery" class="lights bleed" aria-labelledby="gallery-h">
  <h2 id="gallery-h">Under the lights</h2>
  <div class="gallery">{gallery}</div>
</section>
<section id="credits" aria-labelledby="credits-h">
  <h2 id="credits-h">Billing</h2>
  {credits_table()}
  <h3>Training</h3>
  <p>{TRAINING}</p>
</section>
<section id="skills" aria-labelledby="skills-h">
  <h2 id="skills-h">Skills</h2>
  {skills_tags()}
  {facts()}
</section>
<section id="contact" class="stage-door bleed" aria-labelledby="contact-h">
  <h2 id="contact-h">Stage door</h2>
  <p>For casting and all enquiries, please contact Emily's agent.</p>
  {address()}
</section>'''


# ---------------------------------------------------------------- 4 Score
def score(pre):
    name, alt, cap = HEADSHOT
    systems = "".join(f'''<div class="system"><p class="part">{g}</p><div class="staff"><span class="clef" aria-hidden="true">𝄞</span><span class="time" aria-hidden="true"><span>4</span><span>4</span></span><ol class="notes">{"".join(f"<li><span class='lyric'>{s}</span></li>" for s in items)}</ol></div></div>'''
                      for g, items in SKILLS)
    rep = "".join(f'<li><span class="no">No. {len(CREDITS) - i}</span><span class="t"><em>{html.escape(p)}</em> <span class="role">{r}</span></span><span class="dots" aria-hidden="true"></span><span class="yr">{y}</span><span class="by">{c}. Directed by {d}.</span></li>'
                  for i, (y, p, t, r, d, c) in enumerate(CREDITS))
    plates = "".join(fig(s, pre) for s in STILLS[1::2] + STILLS[0::2] + PHOTOS)
    return f'''<div class="sheet">
<section class="title-page" id="top" aria-labelledby="name">
  <p class="dedication"><em>A portfolio in five movements</em></p>
  <h1 id="name">Emily Cruz</h1>
  <p class="for"><em>for voice, piano, accordion, guitar, bass guitar, double bass and saxophones</em></p>
  <figure class="frontis">{img(name, alt, pre, lazy=False, sizes="(min-width: 46rem) 20rem, 60vw", big=True)}<figcaption>{cap}</figcaption></figure>
  <p class="lead">{NOW}</p>
  <p class="cta"><a class="btn primary" href="#contact">Contact her agent</a> <span class="links">{links_inline()}</span></p>
</section>
<section id="reels" class="movement" aria-labelledby="reels-h">
  <h2 id="reels-h"><span class="mark" aria-hidden="true">A</span> I. Overture <span class="tempo">Showreels, the instrumental first</span></h2>
  {SPOT_NOTE}
  <div class="reels">{reel(INSTR_REEL, pre)}{reel(SHOWCASE_REEL, pre)}</div>
</section>
<section id="skills" class="movement" aria-labelledby="skills-h">
  <h2 id="skills-h"><span class="mark" aria-hidden="true">B</span> II. Instrumentation <span class="tempo">Skills, one part per staff</span></h2>
  {systems}
  {facts()}
</section>
<section id="credits" class="movement" aria-labelledby="credits-h">
  <h2 id="credits-h"><span class="mark" aria-hidden="true">C</span> III. Repertoire <span class="tempo">Credits, latest first</span></h2>
  <ol class="repertoire">{rep}</ol>
  <p class="training"><strong>Training.</strong> {TRAINING}</p>
</section>
<section id="gallery" class="movement" aria-labelledby="gallery-h">
  <h2 id="gallery-h"><span class="mark" aria-hidden="true">D</span> IV. Interlude <span class="tempo">Plates</span></h2>
  <div class="gallery">{plates}</div>
</section>
<section id="contact" class="movement coda" aria-labelledby="contact-h">
  <h2 id="contact-h"><span class="mark" aria-hidden="true">E</span> V. Coda <span class="tempo">Representation</span></h2>
  <p>For casting and all enquiries, please contact Emily's agent.</p>
  {address()}
  <p class="fine" aria-hidden="true">Fine</p>
</section>
</div>'''


# ---------------------------------------------------------------- 5 Brief
def brief(pre):
    name, alt, cap = HEADSHOT
    gallery = "".join(fig(s, pre) for s in PHOTOS + STILLS)
    rows = "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in FACTS)
    return f'''<section class="card bleed" id="top" aria-labelledby="name">
  <figure class="card-photo">{img(name, alt, pre, lazy=False, sizes="(min-width: 46rem) 40vw, 100vw", big=True)}<figcaption>{cap}</figcaption></figure>
  <div class="card-body">
    <p class="kicker">Casting brief <span aria-hidden="true">·</span> November 2026</p>
    <h1 id="name">Emily Cruz</h1>
    <p class="sub">Actor-musician and artist, she/her</p>
    <p class="lead">{NOW}</p>
    <dl class="facts card-facts"><div><dt>Agent</dt><dd><a href="#contact">Galloways</a></dd></div>{rows}<div><dt>Training</dt><dd>GSA, BA (Hons) Actor-Musician, 2023 to 2026</dd></div></dl>
    <p class="cta"><a class="btn primary" href="#contact">Contact her agent</a> <span class="links"><a href="{SPOTLIGHT}">Spotlight</a> <span aria-hidden="true">·</span> <a href="#reels">Showreels</a></span></p>
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
<section id="contact" class="agent" aria-labelledby="contact-h">
  <h2 id="contact-h">Agent</h2>
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


BODIES = {1: programme, 2: bluelight, 3: contactsheet, 4: score, 5: brief}
NAVS = {
    1: [("credits", "Cast list"), ("reels", "Reels"), ("gallery", "Photos"), ("skills", "Skills"), ("contact", "Contact")],
    2: [("reels", "Reels"), ("gallery", "Photos"), ("credits", "Credits"), ("skills", "Skills"), ("contact", "Contact")],
    3: [("about", "Notes"), ("reels", "Reels"), ("credits", "Credits"), ("skills", "Skills"), ("contact", "Contact")],
    4: [("reels", "I"), ("skills", "II"), ("credits", "III"), ("gallery", "IV"), ("contact", "V")],
    5: [("credits", "Credits"), ("skills", "Skills"), ("contact", "Agent"), ("reels", "Reels"), ("gallery", "Photos")],
}
CSP = ("default-src 'self'; img-src 'self'; style-src 'self'; script-src 'self'; "
       "frame-src https://mediaviewer.spotlight.com; base-uri 'none'; form-action 'none'")


LINES = {  # one line per design, for the chooser cards
    1: "A West End programme", 2: "The showcase stage", 3: "A photographer's proof sheet",
    4: "An engraved score", 5: "A casting brief",
}


def cards(pre, current, on_home):
    out = []
    for k, (nm, _) in DESIGNS.items():
        href = f"{pre}designs/{k}.html" if on_home else f"{k}.html"
        cur = ' aria-current="page"' if k == current else ""
        shot = f"{pre}images/shots/d{k}"
        out.append(f'<li><a href="{href}"{cur}><img src="{shot}-640.webp" alt="" width="640" height="400" loading="lazy" decoding="async">'
                   f'<strong>{k}. {nm}</strong><span>{LINES[k]}</span></a></li>')
    return "".join(out)


def page(n, pre, switcher):
    nav = "".join(f'<a href="#{i}">{t}</a>' for i, t in NAVS[n])
    on_home = not switcher
    pre_root = pre  # path to site root
    # "Choose a design" on every page (Dinis Cruz, 20 November 2026): one button in the header, opening five cards. No script.
    chooser = f'''<details class="chooser">
    <summary>Choose a design</summary>
    <div class="chooser-panel">
      <ul class="cards">{cards(pre_root if on_home else "../", n, on_home)}</ul>
      <p class="all"><a href="{"designs/" if on_home else ""}index.html">All five, side by side</a></p>
    </div>
  </details>'''
    title = "Emily Cruz" if on_home else f"{DESIGNS[n][0]} design, Emily Cruz"
    theme = f"{pre}theme.css" if on_home else f"d{n}.css"
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
<header class="bar">
  <a class="brand" href="{"#top" if on_home else "../index.html"}">Emily Cruz</a>
  <nav aria-label="Sections">{nav}</nav>
  {chooser}
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
    big = "".join(f'<li><a href="{k}.html"><img src="../images/shots/d{k}-960.webp" alt="" width="960" height="600" loading="lazy" decoding="async">'
                  f'<strong>{k}. {v[0]}</strong><span>{v[1]}</span></a></li>' for k, v in DESIGNS.items())
    return f'''<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="Content-Security-Policy" content="default-src 'self'; img-src 'self'; style-src 'self'; base-uri 'none'; form-action 'none'">
<title>Five designs, Emily Cruz</title>
<meta name="color-scheme" content="light dark">
<link rel="icon" href="../favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="../base.css">
<link rel="stylesheet" href="d5.css">
</head>
<body class="designs-page">
<a class="skip" href="#main">Skip to content</a>
{FAMILY}
<header class="bar"><a class="brand" href="../index.html">Emily Cruz</a></header>
<main id="main" tabindex="-1">
<section>
<h1>Choose a design</h1>
<p>The same facts and photographs, set five ways. The home page uses {DESIGNS[CHOSEN][0]}; Emily chooses which one stays.</p>
<ol class="design-cards">{big}</ol>
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
