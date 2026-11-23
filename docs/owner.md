# What the owner can do on this site

For Dinis Cruz (the owner until the site is handed to Emily), and then for Emily. Nothing here waits on an agent: each item can be done on GitHub or with your own Claude, and every push to dev publishes the site within a few minutes.

Written by emily.b@SovereignWebsite.dinis, 23 November 2026.

## Look

- **The site:** https://emily-cruz.artist.sovereignweb.site
- **The five designs:** https://emily-cruz.artist.sovereignweb.site/designs/
- **How the site is governed:** https://emily-cruz.artist.sovereignweb.site/policy/
- **How it was made, and its review rounds:** https://emily-cruz.artist.sovereignweb.site/admin/
- **Every publish and its checks:** https://github.com/SovereignWebsite/Site__Artist__Emily-Cruz/actions . The version number at the foot of each page links to the run that published it.

## Change

All the words, credits, skills and photo lists live in one file, tools/build.py. Edit it, run `python3 tools/build.py`, and push to dev. Or ask your Claude to do it for you (docs/prompt-for-your-claude.md says how).

| To change | Where in tools/build.py |
|---|---|
| The current-work line ("As of November 2026, ...") | `NOW` |
| The home page design (1 to 5) | `CHOSEN` |
| Credits | `CREDITS` (year, production, type, role, director, company) |
| Skills, accents and languages | `SKILLS` |
| Training | `TRAINING` |
| Playing age, height, hair and the other details | `FACTS` (remove any line to take it off the site) |
| Photographs and their credits | `HEADSHOT`, `PHOTOS`, `STILLS` (a new photo also needs WebP copies 400, 720 and 1400 px wide in site/images/, with its metadata removed; ask your Claude) |
| Showreels | `SHOWCASE_REEL`, `INSTR_REEL` |

## Decide

These need only the owner, and unblock the rest:

- [ ] **Hand the site to Emily.** Invite her to the SovereignWebsite organisation as a Member, in no team, and give her write on this repository. She accepts at https://github.com/orgs/SovereignWebsite/invitation. Then docs/handover.md is hers.
- [ ] **Answer Emily's questions,** or pass them to her: docs/questions-for-emily.md (photo credits, a bio, which details stay public, Instagram and TikTok, more reels, the design).
- [ ] **The feedback box** (feedback.b): say when it may go on the site, once security.b and design.b have reviewed it.

## Needs the owner's yes, by the site's policy

Changes to site/policy/, .github/, site/CNAME and CLAUDE.md. The owner can make these directly; an agent makes them only with the owner's yes, and says in the commit where it was given.
