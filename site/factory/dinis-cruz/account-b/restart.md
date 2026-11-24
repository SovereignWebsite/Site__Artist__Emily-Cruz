# Restarting emily.b

For a fresh Claude Code session started on SovereignWebsite/Site__Artist__Emily-Cruz, branch dev, with the line: "You are emily.b@SovereignWebsite.dinis. Read site/factory/dinis-cruz/account-b/restart.md and follow it."

1. Read CLAUDE.md, then this folder: agent.json (what is open now), role.md, decisions.md, messages.md, learnings.md. Then docs/handover.md and docs/questions-for-emily.md.
2. Make your own key where you run (record 2026-11-24__own-keys-principle): `sgit pki keygen --label emily.b@SovereignWebsite.dinis`, with its passphrase in a 0600 file outside the repository. Never print or commit the private half. Convert the signing key to an OpenSSH key for git (gpg.format ssh, user.signingkey, commit.gpgsign true, gpg.ssh.program ssh-keygen), and load it into an ssh-agent.
3. Publish the public half: replace site/keys/emily.b.json with the new key's public bundle, and nothing else, in a commit of its own signed with the new key, with the trailers Agent: emily.b@SovereignWebsite.dinis and Claude-Session: <your session URL>. The site's signer check (.github/ci/signers.mjs, refreshed in 3a4fa04) reads site/keys/, but it will refuse this: emily.b already has a live key in team/keys.json, a site key for that name with a different key does not count, and a commit may vouch for itself only when it adds a new file. So first ask decisions.b (link only, by a signed request) to record the new key in team/keys.json and mark the old one superseded; push once that is done.
4. Update agent.json: session, key fingerprint, updated (from date -u), active_until (at most 7 days ahead), now.
5. Build and check: `python3 tools/build.py`, then the CI steps in .github/workflows/pages.yml (build.mjs, share-check.mjs, quality.mjs, html-validate with --config). Push to dev only; watch the Pages and Signers runs turn green.
6. Send decisions.b one line: the link to this folder.

Never: push to main; print, commit or read a private key or token; name a private person without consent; invent a fact, a price or a customer; add a server, cookies or tracking.
