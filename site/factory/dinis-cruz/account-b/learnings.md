# emily.b: learnings

- Spotlight showreels: embed with a click-to-load iframe (reels.js) and a CSP allowing only frame-src https://mediaviewer.spotlight.com; nothing reaches Spotlight until a visitor presses play.
- Long URLs overflow on phones: overflow-wrap:anywhere on links and code.
- html-validate 8.24.0 rejects --preset=standard: use --config .github/ci/htmlvalidate.json.
- Header crowding: group the design chooser and the family credit in one bar-right block; on phones the credit becomes a compact "SW" button, keeping its text as the accessible name.
- The ssh-agent dies when the shell resets: restart it and re-add the key before each signed commit; a failed signature shows as "incorrect passphrase".
- A link to a page that does not exist yet fails the quality check: push the link only with, or after, its page.
- The policy reserves site/policy/**, .github/**, site/CNAME and CLAUDE.md for the owner's yes: ask, do not act on a relayed request.
- A person's commits need no Agent: trailer: GitHub-verified commits pass the signer check as theirs.
- Take times from date -u, never estimate them.
- Since 3a4fa04 (Org apply, 24 Nov) the signer check also reads site/keys/<name>.json, but a restarted emily.b cannot replace its key there by itself while its old key is live in team/keys.json (see restart.md, step 3).
