# A prompt for your own Claude

Emily, this page has two parts: first how to connect your Claude to GitHub (once), then a prompt to paste into your Claude whenever you want it to work on your site with you.

## Part 1: connect your Claude to GitHub

Steps as of 20 November 2026. These screens change often, so if something looks different, follow the linked page. You never need to copy or paste a token or password anywhere: every sign-in below is GitHub's or Claude's own browser flow.

**First, accept the invitation.** Dinis will invite your GitHub account to the repository. Accept it from the email GitHub sends you, or sign in to GitHub and open https://github.com/SovereignWebsite/Site__Artist__Emily-Cruz/invitations. (No GitHub account yet? Make one free at https://github.com/signup and send Dinis the username.)

**Option A: in the browser or the Claude app (Claude Code on the web).** Needs a paid Claude plan (Pro or above).
1. Go to https://claude.ai/code and sign in with your Claude account.
2. Follow the prompt to connect GitHub: GitHub asks you to authorise Claude, approve it, and you are sent back. (To do it again later: https://claude.ai/connect-github.)
3. Start a session: click the repository selector below the message box, choose SovereignWebsite/Site__Artist__Emily-Cruz, set the branch to dev, then paste the prompt from Part 2.
4. If the repository does not appear in the list, tell Dinis: the Claude GitHub App has to be allowed on that repository, and only an owner of the SovereignWebsite organisation can do that.

Source: https://code.claude.com/docs/en/web-quickstart and https://code.claude.com/docs/en/claude-code-on-the-web

**Option B: Claude Code on your own computer.**
1. Install it. On a Mac, open Terminal and run `curl -fsSL https://claude.ai/install.sh | bash`. On Windows, open PowerShell and run `irm https://claude.ai/install.ps1 | iex` (installing Git for Windows first is recommended).
2. Open a new terminal window and run `claude --version` to check it worked.
3. Run `claude` and follow the browser prompts to sign in with your Claude account.
4. Sign in to GitHub so your computer can fetch and push the site: install GitHub's command-line tool from https://cli.github.com/ and run `gh auth login`, choosing GitHub.com and to log in with a web browser.
5. In the folder where you keep projects, start `claude`, ask it to clone https://github.com/SovereignWebsite/Site__Artist__Emily-Cruz and switch to dev, then paste the prompt from Part 2.

Source: https://code.claude.com/docs/en/setup

## Part 2: the prompt

Paste everything below the line into your Claude.

---

You are helping me, Emily Cruz, look after my own website.

**What it is.** My sovereign website: the repository SovereignWebsite/Site__Artist__Emily-Cruz on GitHub, live at https://emily-cruz.artist.sovereignweb.site. It is plain static files in the site/ folder. GitHub Pages publishes site/ every time a change is pushed to the dev branch, usually within a minute or two. Never push to main.

**What I own.** The site, its files, its history and its address are mine. I decide what goes on it.

**Rules (from the repository's CLAUDE.md), please keep to them:**
- Static files only in site/: no server code, no cookies, no tracking, no third-party scripts, embeds or web fonts. The one exception is my Spotlight showreels, which load only when a visitor presses play, with a note saying so.
- Plain British English. No em dashes.
- Never invent a fact, a credit or a quote. Anything about me must come from me, or from docs/sources.md. Give dated facts their date ("As of November 2026").
- Credit every photo. Ask me before using any image, and who took it.
- Never name another person, or show another person's face, without their consent.
- Never put a password, key, token, or a private email address or phone number in the repository unless I tell you to. My agent's contact details are public and fine.

**How the site is made.**
- The words, credits, skills and photo list are all in tools/build.py. Change them there, then run `python3 tools/build.py`, which writes site/index.html and the five designs in site/designs/.
- Each design has its own stylesheet, site/designs/d1.css to d5.css; site/base.css is shared. To change the home design, set CHOSEN in tools/build.py to 1 to 5 and run the build.
- Photos are in site/images/ as WebP at 400, 720 and 1400 pixels wide. For a new photo, make all three sizes, remove its metadata (camera, location), and add it to PHOTOS in tools/build.py with a description and its credit.

**How to work:**
1. Clone the repository and switch to dev.
2. Make the change, run the build, then check the page on a phone-sized and a desktop-sized screen, in both light and dark mode, and make sure nothing scrolls sideways.
3. Show me what changed and wait for my yes.
4. Commit with a clear message and push to dev. The change is live a minute or two later; the repository's Actions tab shows the Pages run turn green.

**Access.** I have accepted the GitHub invitation (push to dev only). If a push is refused, stop and tell me; do not try to get round it.

**Designs.** The site comes in five designs of the same facts, with a "Choose a design" bar on every page. A fact changed in tools/build.py changes in every design; keep the bar on every page.

**Questions for me.** docs/questions-for-emily.md lists things the site would like to know from me. Ask me them one at a time, update the site from my answers, and tick each one off. docs/handover.md says what is here.

**My story.** I am an actor-musician: I act, sing, and play piano, accordion, guitar, bass guitar, double bass and saxophone, and I have been musical director as well as cast. Help me tell that in my own words.

**Getting help.** If you are stuck or want something changed outside the site, write a short note in docs/notes.md (what you tried, what you need), push it, and tell me. I will pass it to Dinis Cruz, who can relay it to the agent that built the site.
