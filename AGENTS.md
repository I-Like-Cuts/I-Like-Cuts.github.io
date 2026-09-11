# Eoin's portfolio website

This is the real, ongoing portfolio website for Eoin, a film editor working in Ireland and the UK. The minimal initial page is intentional: design and selected work will be developed with Eoin. Preserve the repository identity and deployment address as the site evolves.

- Repository: `I-Like-Cuts/I-Like-Cuts.github.io`
- Production: `https://i-like-cuts.github.io/`
- Production branch: `main`
- Website files: `public/`
- Deployment: `.github/workflows/pages.yml`
- Workflow guidance: `.agents/skills/site-workflow/SKILL.md`

## Shared instructions across agents

This file is the canonical project guide for every coding agent. Codex reads it directly; Claude Code loads it through the root `CLAUDE.md` import. Other agents should read this file explicitly if they do not discover it automatically. The linked workflow skill is ordinary Markdown and can be read by any agent; native skill support is optional.

Keep project rules here and detailed workflow steps in `.agents/skills/site-workflow/SKILL.md`. Keep `CLAUDE.md` as a thin import so instructions stay consistent. Do not import `CLAUDE.md` back into this file or duplicate the shared workflow into tool-specific files.

## Handle setup and updates for the user

Read the workflow skill for local setup, editing, review, publishing and rollback. Treat plain-language requests as sufficient; the user should not have to remember Git commands or skill names. Explain the result and any necessary user action briefly.

For first-time setup, inspect the environment and existing work before changing anything. This is a static site: require Python 3.9+ for local checks and preview, and Git for version control. GitHub CLI (`gh`) is needed for the agent's remote workflow. Use available tools or their equivalents; do not introduce a framework, package manager, CMS or paid service just to serve the initial site. Help install missing tools when authorized and supported. Interactive account sign-in remains the user's action; do not ask them to paste tokens into chat.

On Mark's Windows/WSL machine, run development commands inside WSL using `/home/mmitchell/workspace/eoin/site`. On Eoin's machine, use the actual checkout and operating system. Never assume Mark's paths or GitHub identity apply to Eoin.

Run from the checkout root:

```sh
python3 scripts/check_site.py
python3 -m http.server 8000 --bind 127.0.0.1 --directory public
```

Use `python` instead of `python3` if that is the available Python 3 command. No dependency installation or build is needed. Serve only `public/`; never serve the repository root. Give the local preview URL and keep the server available while the user reviews it.

## Publishing contract

Use a feature branch and a pull request for routine changes. Check the diff, local checks and GitHub checks before merging. `main` publishes automatically. A request to edit or preview is not a request to publish. A request to publish includes the necessary commit, push and merge; complete those without repeatedly asking for permission already given. No separate reviewer is required by the intended workflow.

Respect existing unrelated work and repository rules. Stage only task files. Do not force-push shared history, recreate the repository, change visibility, delete the site or change organisation settings to resolve routine errors. If a check fails, fix the actual failure and rerun it. Read the exact deployment run for the published commit and verify its live content before declaring success. Report an actual access or authentication block clearly instead of inventing a successful deployment.

Only `public/` is deployed. Keep references relative; retain GitHub Pages compatibility when evolving the implementation. If a future framework is justified, update the checks, artifact directory, preview instructions and workflow together. Public site files and repository history must not contain credentials or private source footage.

## Content and design

Use Eoin's confirmed wording, credited roles and media. Do not infer exact credits from film titles or invent testimonials, awards, contact details or a surname. Keep video on his existing Vimeo account unless he requests another approach. Ask for missing content only when it is needed for the requested change. Prioritize accessible, responsive presentation; let Eoin guide the design.
