# Handover: Emily Cruz's site

For Emily Cruz, from emily.b@SovereignWebsite.dinis, the agent that built the first version. 20 November 2026.

## What is here

- **The site:** https://emily-cruz.artist.sovereignweb.site (the old address emily-cruz.artists.sovereignwebsite.site forwards to it).
- **The repository:** https://github.com/SovereignWebsite/Site__Artist__Emily-Cruz, branch dev. Every push to dev publishes site/.
- **Five designs** of the same facts, with "Choose a design" on every page: 1 Programme (the home page for now), 2 Blue light, 3 Contact sheet, 4 Score, 5 Brief. See them at https://emily-cruz.artist.sovereignweb.site/designs/ .
- **What is on it:** your current tour, ten credits, training, skills, your Spotlight showreels (they load from Spotlight only when someone presses play), 11 credited photographs and stills, and Galloways as the contact for all enquiries.
- **What is not on it:** cookies, tracking, analytics, or anything loaded from another site before a visitor asks.

## The files

- tools/build.py: all the words, credits, skills and the photo list. Edit here, then run `python3 tools/build.py`.
- site/: what is published. index.html (home), designs/ (the five), base.css and designs/d1.css to d5.css (the looks), images/ (photos), reels.js (play on click for the showreels).
- docs/sources.md: where every fact and photo came from.
- docs/questions-for-emily.md: what the site still needs from you.
- docs/prompt-for-your-claude.md: how to connect your own Claude to GitHub, and a prompt to paste in so it can work on the site with you.

## To take it over

1. Make a GitHub account if you do not have one, and send Dinis the username so he can invite you.
2. Follow docs/prompt-for-your-claude.md.
3. Choose a design, and work through docs/questions-for-emily.md with your Claude.
