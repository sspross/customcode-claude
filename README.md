# customcode-claude

THE reference **claude home repo** for [customcode](https://github.com/sspross/customcode) — the de facto example of bringing your own user-level Claude Code environment onto every Machine. Point your customcode Rucksack's *claude home* at this repo (or your fork of it, or a repo shaped like it) and every Machine's next config sync carries this environment.

## The structure contract

The repo must contain a top-level `claude/` directory — your Claude home. From it, customcode syncs **only** this allowlist:

```
CLAUDE.md   settings.json   keybindings.json   skills/   agents/   commands/   statusline-render
```

Anything else inside `claude/` is ignored — and named as ignored in the sync-info surface, never silently dropped.

Two things refuse a sync outright:

- a `.credentials.json` anywhere in the repo — a Claude login is machine-local, never a committed secret;
- a missing `claude/` directory — the contract is unmet.

## Files you must not touch

customcode overlays its own machinery on top of your content at every sync. These are **never yours**, and shipping real ones here does nothing (they are ignored/overridden):

- **`statusline.py`** — customcode's Telemetry reporter, always customcode's own. The copy in this repo is a placeholder documenting exactly that.
- **`kimi.sh`** and **`zdotdir/`** — customcode's kimi-mode wrapper machinery.
- **the `statusLine` and `tui` keys in `settings.json`** — force-overridden at sync so Telemetry and the browser viewer can't be broken by repo content. Every *other* settings key you set survives the merge.

## Making the status line yours

Don't touch `statusline.py`; instead ship a `statusline-render` file at the top of `claude/` — Claude Code's own statusline contract (session JSON on stdin, one line on stdout, shebang required). customcode reports Telemetry first, then execs your renderer for the visible line. A broken renderer costs you the pretty line, never the Telemetry.

## What's in here

- `claude/CLAUDE.md` — the in-session ownership rules for a customcode-managed environment.
- `claude/settings.json` — the settings base, with the DO-NOT-TOUCH keys documented in place.
- `claude/skills/` — a set of global skills (the `mp-*` method-pack skills; see `.mattpocock-skills.LICENSE`).
- `claude/statusline.py` — a placeholder marking customcode's overlay spot (see above).

## Auth

Machines clone this repo with plain git over HTTPS. A public repo needs no credentials; a private fork works through the Machine's own `gh auth login` + `gh auth setup-git` — customcode never holds or transports a git credential.
