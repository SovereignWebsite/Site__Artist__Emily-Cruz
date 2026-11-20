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

# The Sovereign Website credit for a customer's site: the Factory's seed/shared/family-credit.html (f759821),
# unchanged, placed at the far right of the header after "Choose a design" (Dinis Cruz, 20 November 2026).
FAMILY = """<details class="family-credit">
  <summary>Sovereign Website</summary>
  <ul>
    <li><a href="/start/">Start here</a></li>
    <li><a href="/agents/">Use with your AI</a></li>
    <li class="family-gap"><a href="/admin/">How this site was made</a></li>
    <li><a href="https://sovereignwebsite.ai/">Sovereign Website</a></li>
    <li><a href="https://sovereignwebsite.org/">Principles</a></li>
    <li><a href="https://sovereignwebsite.site/">Hosted</a></li>
    <li><a href="https://hub.sovereignweb.site/">Hub</a></li>
    <li><a href="https://agents.sovereignweb.site/">Agents</a></li>
    <li><a href="https://vault.sovereignwebsite.site/">Vault</a></li>
    <li><a href="https://agenticcells.ai/">AgentiCCells</a></li>
    <li><a href="https://riskmandate.ai/">RiskMandate</a></li>
    <li><a href="https://newsroom.sgit.ai/">Newsroom</a></li>
  </ul>
</details>"""  # from SovereignWebsite__Factory seed/shared/family-bar.html

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
  {spread([PHOTOS[3]] + STILLS, pre, cls="mosaic")}
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
    gallery = "".join(fig(s, pre) for s in PHOTOS + STILLS)
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
    plates = "".join(fig(s, pre) for s in PHOTOS + STILLS)
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


# ---------------------------------------------------------------- link previews, start, agents, admin
SITE_URL = "https://emily-cruz.artist.sovereignweb.site/"
DESC = "Emily Cruz, actor-musician and artist. BA (Hons) Actor-Musician, Guildford School of Acting, 2026. Represented by Galloways."


def og(path, title, desc=DESC):
    """Link preview tags (WhatsApp, social media, chat apps). Dinis Cruz, 20 November 2026."""
    return f'''<link rel="canonical" href="{SITE_URL}{path}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Emily Cruz">
<meta property="og:locale" content="en_GB">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{SITE_URL}{path}">
<meta property="og:image" content="{SITE_URL}assets/share/card-1200x630.jpg">
<meta property="og:image:type" content="image/jpeg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Emily Cruz, actor-musician and artist, beside her headshot (photo YellowBellyPhoto)">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{html.escape(title)}">
<meta name="twitter:description" content="{html.escape(desc)}">
<meta name="twitter:image" content="{SITE_URL}assets/share/card-1200x630.jpg">
<meta name="twitter:image:alt" content="Emily Cruz, actor-musician and artist, beside her headshot (photo YellowBellyPhoto)">'''


def footer(pre):
    return f'''<footer>
  <p class="foot-links"><a href="{pre}start/">Start here</a> <span aria-hidden="true">·</span> <a href="{pre}agents/">Use this site with your AI</a> <span aria-hidden="true">·</span> <a href="{pre}llms.txt">llms.txt</a> <span aria-hidden="true">·</span> <a href="{pre}admin/">How this site was made</a> <span aria-hidden="true">·</span> <a href="{pre}designs/">All five designs</a></p>
  <p>A sovereign website: Emily's own files, history and address. No cookies, no tracking, no third-party scripts. The showreels come from Spotlight only when you press play. Text licensed <a href="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a>; photographs remain their photographers'. Source: <a href="https://github.com/SovereignWebsite/Site__Artist__Emily-Cruz">SovereignWebsite/Site__Artist__Emily-Cruz</a>.</p>
</footer>'''


def header_links(pre):
    return f'<p class="head-links"><a href="{pre}start/">Start here</a> <a href="{pre}agents/">Use with your AI</a> <a href="{pre}admin/">How it was made</a></p>'


REPO = "https://github.com/SovereignWebsite/Site__Artist__Emily-Cruz"


def plain(path, title, h1, body, desc=DESC):
    pre = "../"
    return f'''<!doctype html>
<html lang="en-GB" class="plain">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="Content-Security-Policy" content="default-src 'self'; img-src 'self'; style-src 'self'; base-uri 'none'; form-action 'none'">
<title>{title}</title>
<meta name="description" content="{html.escape(desc)}">
{og(path, title, desc)}
<meta name="color-scheme" content="light dark">
<link rel="icon" href="{pre}favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="{pre}base.css">
<link rel="stylesheet" href="{pre}theme.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="bar">
  <a class="brand" href="{pre}index.html">Emily Cruz</a>
  <nav aria-label="Site"><a href="{pre}start/">Start here</a><a href="{pre}agents/">Use with your AI</a><a href="{pre}admin/">How it was made</a></nav>
  <div class="bar-right">{FAMILY}</div>
</header>
<main id="main" tabindex="-1" class="doc">
<section>
<h1>{h1}</h1>
{body}
</section>
</main>
{footer(pre)}
</body>
</html>
'''


def start_page():
    b = f'''<p class="lead">Emily, this is your site. These steps hand it over to you, so you and your own Claude can change words, add photos and choose a design.</p>
<ol class="steps">
  <li><h2>Get a GitHub account</h2><p>If you do not have one, make one free at <a href="https://github.com/signup">github.com/signup</a>, and send Dinis the username.</p></li>
  <li><h2>Accept both invitations</h2><p>Dinis invites you twice: to the SovereignWebsite organisation (as a member) and to your repository (with write access). Accept the organisation invitation at <a href="https://github.com/orgs/SovereignWebsite/invitation">github.com/orgs/SovereignWebsite/invitation</a>, because the link in GitHub's email may not offer an Accept button. Accept the repository one from GitHub's email, or sign in and open <a href="{REPO}">the repository</a>: GitHub shows the invitation at the top. Claude's GitHub check needs both. You can push to the dev branch; every push publishes the site a minute or two later.</p></li>
  <li><h2>Connect your Claude to GitHub</h2><p>In the browser or the Claude app: go to <a href="https://claude.ai/code">claude.ai/code</a>, sign in, and follow the prompt to connect GitHub (GitHub asks you to authorise Claude). If Claude says it cannot reach the repository, accept both invitations and press "Check again". Then choose the repository SovereignWebsite/Site__Artist__Emily-Cruz and the dev branch. On your own computer instead: install Claude Code from <a href="https://code.claude.com/docs/en/setup">its setup page</a>. You never paste a token or password anywhere.</p></li>
  <li><h2>Paste the prompt</h2><p>Paste the prompt from <a href="{REPO}/blob/dev/docs/prompt-for-your-claude.md">docs/prompt-for-your-claude.md</a> into your Claude. It tells your Claude how the site is made and the rules it keeps to.</p></li>
  <li><h2>Answer the questions</h2><p>Your Claude can go through <a href="{REPO}/blob/dev/docs/questions-for-emily.md">docs/questions-for-emily.md</a> with you: photo credits, a bio, your details, Instagram and TikTok, and which design you like.</p></li>
  <li><h2>Choose a design</h2><p>Press "Choose a design" at the top of any page, or see <a href="../designs/">all five side by side</a>. Tell your Claude which one should be the home page.</p></li>
</ol>
<p>What is here, file by file: <a href="{REPO}/blob/dev/docs/handover.md">docs/handover.md</a>. Where every fact and photo came from: <a href="{REPO}/blob/dev/docs/sources.md">docs/sources.md</a>.</p>'''
    return plain("start/", "Start here, Emily Cruz", "Start here", b, "How Emily takes over her own site and connects her Claude to GitHub.")


def agents_page():
    b = f'''<p class="lead">Use this site with your AI assistant. Everything about Emily on this site is in one plain text file, made for AI assistants to read: <a href="../llms.txt">llms.txt</a>.</p>
<h2>Try asking your AI</h2>
<ul class="asks">
  <li>"Read {SITE_URL}llms.txt and summarise Emily Cruz's stage credits."</li>
  <li>"From {SITE_URL}llms.txt, which instruments does Emily Cruz play, and has she worked as a musical director?"</li>
  <li>"Using {SITE_URL}llms.txt, how do I contact Emily Cruz's agent about casting?"</li>
</ul>
<h2>What the file holds</h2>
<p>Her current work (dated), credits, training, skills, accents, languages, the playing details from her Spotlight profile, links to her showreels, and her agent's public contact details. Nothing in it is guessed: it comes from her Spotlight profile, as supplied on 20 November 2026.</p>
<h2>For AI agents</h2>
<p>This is a static site: no forms, no API, no cookies. Please quote facts as written, keep their dates, and send casting enquiries to her agent, Galloways. The source is public at <a href="{REPO}">{REPO}</a>.</p>'''
    return plain("agents/", "Use with your AI, Emily Cruz", "Use this site with your AI", b, "Emily Cruz's facts in one plain text file for AI assistants: llms.txt.")


def llms_txt():
    lines = ["# Emily Cruz", "", "> Actor-musician and artist (she/her). BA (Hons) Actor-Musician, Guildford School of Acting, 2023 to 2026. Based in Greater London. Represented by Galloways.", "",
             "Facts from Emily's Spotlight profile, as supplied on 20 November 2026. Please keep dates with facts.", "",
             "## Now", "", "- As of November 2026: UK tour of Pride and Prejudice* *(sort of), 1st Cover: Effie, Flo, Tillie (director Isobel McArthur; company David Pugh).", "",
             "## Credits", ""]
    lines += [f"- {y}: {p} ({t}). Role: {r}. Director: {d}. Company: {c}." for y, p, t, r, d, c in CREDITS]
    lines += ["", "## Training", "", f"- {TRAINING}", "", "## Skills", ""]
    lines += [f"- {g}: {', '.join(items)}." for g, items in SKILLS]
    lines += ["", "## Details", ""] + [f"- {k}: {v}." for k, v in FACTS]
    lines += ["", "## Showreels (hosted by Spotlight)", "",
              f"- Showcase, They All Laughed (1 min 9 s): {REEL}{SHOWCASE_REEL[0]}",
              f"- Instrumental reel (2 min 5 s): {REEL}{INSTR_REEL[0]}", "",
              "## Representation", "", "- Galloways, Henry Wood House, 4-5 Langham Place, London W1B 3DG. 020 7631 3134 or 07752 705359. agents@gallowaysagency.com", "",
              "## Links", "", f"- Site: {SITE_URL}", f"- Spotlight: {SPOTLIGHT}", f"- GSA graduates 2026: {GSA}", f"- Source: {REPO}", ""]
    return "\n".join(lines)


ROUNDS = [
    ("e409581", "sites.b", "First page: headshot, role, training, links."),
    ("e770480", "emily.b", "Full portfolio from her Spotlight profile: reels on click, credited gallery, credits, skills, agent."),
    ("bd1166c", "emily.b", "Five designs (first set) and design guideline fixes, at design.b's request."),
    ("c9f0f45", "emily.b", "design.b round 1: each design rebuilt around an idea from Emily's world; Programme goes live."),
    ("c5b7ac2", "emily.b", "Dinis's founder and personal site guidelines: choose a design on every page, handover documents."),
    ("af957fd", "emily.b", "design.b round 2: 24px targets, focusable main. Rated 3."),
    ("d5c475f", "emily.b", "Round 3 after Dinis's review: scaffolding removed, screenshot chooser, every design rebuilt to be visual."),
    ("f85a9e2", "emily.b", "design.b round 3 fixes. Synthetic users: 4, 4, 4, 4, 4."),
    ("8675c1d", "emily.b", "Family strip removed at Dinis's request; family links in a top-right menu."),
]


def admin_page():
    rows = "".join(f'<tr><td><a href="{REPO}/commit/{c}"><code>{c}</code></a></td><td>{who}</td><td>{what}</td></tr>' for c, who, what in ROUNDS)
    b = f'''<p class="lead">How this site was made, and by whom. Everything here is public, like the site.</p>
<h2>Who made it</h2>
<ul>
  <li><strong>Dinis Cruz</strong> asked for it, with Emily's agreement, supplied the photos and the facts from her Spotlight profile, and reviewed the designs.</li>
  <li><strong>emily.b</strong>, an AI agent (Claude), built and maintains the site. Every commit is signed with its own published key.</li>
  <li><strong>design.b</strong> reviewed each design round against the Sovereign Website design guidelines, ran accessibility checks and synthetic users.</li>
  <li><strong>sites.b</strong> made the first page; <strong>factory.b</strong> set up the repository, address and publishing; <strong>hub.b</strong> lists it in the showroom; <strong>conductor.b</strong> registered the signing key.</li>
</ul>
<h2>The rounds</h2>
<div class="table-wrap" tabindex="0" role="region" aria-label="Commits"><table><thead><tr><th scope="col">Commit</th><th scope="col">By</th><th scope="col">What changed</th></tr></thead><tbody>{rows}</tbody></table></div>
<p>The full history: <a href="{REPO}/commits/dev">every commit on dev</a>.</p>
<h2>How it is checked</h2>
<ul>
  <li>axe-core accessibility checks on every page, at phone (390 px) and desktop (1366 px) widths, in light and dark mode.</li>
  <li>No request to another site on load, no cookies, no storage, no horizontal scroll; first load well under 1 MB.</li>
  <li>Synthetic users (design.b, round 3, 20 November 2026): five visitors each rated the home page 4 (design.b's scale); all five would show it to a friend.</li>
</ul>
<h2>How it is built</h2>
<p>Static files only. tools/build.py writes every page from one set of facts; tools/social_card.py makes the link preview image. The showreels are Spotlight's player, loaded only when a visitor presses play.</p>'''
    return plain("admin/", "How this site was made, Emily Cruz", "How this site was made", b, "Who made Emily Cruz's site, the design rounds and commits, and how it is checked.")


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
{og("" if on_home else f"designs/{n}.html", title)}
<meta name="color-scheme" content="light dark">
<link rel="icon" href="{pre}favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="{pre}base.css">
<link rel="stylesheet" href="{theme}">
<script src="{pre}reels.js" defer></script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="bar">
  <a class="brand" href="{"#top" if on_home else "../index.html"}">Emily Cruz</a>
  <nav aria-label="Sections">{nav}</nav>
  {header_links(pre)}
  <div class="bar-right">{chooser}
  {FAMILY}</div>
</header>
<main id="main" tabindex="-1">
{BODIES[n](pre)}
</main>
{footer(pre)}
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
<meta name="description" content="Emily Cruz's site in five designs.">
{og("designs/", "Five designs, Emily Cruz")}
<meta name="color-scheme" content="light dark">
<link rel="icon" href="../favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="../base.css">
<link rel="stylesheet" href="d5.css">
</head>
<body class="designs-page">
<a class="skip" href="#main">Skip to content</a>
<header class="bar"><a class="brand" href="../index.html">Emily Cruz</a>
  <div class="bar-right">{FAMILY}</div>
</header>
<main id="main" tabindex="-1">
<section>
<h1>Choose a design</h1>
<p>The same facts and photographs, set five ways. The home page uses {DESIGNS[CHOSEN][0]}; Emily chooses which one stays.</p>
<ol class="design-cards">{big}</ol>
</section>
</main>
{footer("../")}
</body>
</html>
'''


if __name__ == "__main__":
    (SITE / "designs").mkdir(exist_ok=True)
    (SITE / "index.html").write_text(page(CHOSEN, "", switcher=False))
    for n in DESIGNS:
        (SITE / "designs" / f"{n}.html").write_text(page(n, "../", switcher=True))
    (SITE / "designs" / "index.html").write_text(designs_index())
    for d, fn in (("start", start_page), ("agents", agents_page), ("admin", admin_page)):
        (SITE / d).mkdir(exist_ok=True)
        (SITE / d / "index.html").write_text(fn())
    (SITE / "llms.txt").write_text(llms_txt())
    theme = (SITE / "designs" / f"d{CHOSEN}.css").read_text()
    (SITE / "theme.css").write_text(theme)
    print(f"built index.html (design {CHOSEN}, {DESIGNS[CHOSEN][0]}) and designs/1-5.html")
