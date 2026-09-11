# Eoin's website

Eoin's film editing portfolio, working across Ireland and the UK. This is the permanent website repository; the initial welcome page will grow into the full portfolio.

- Website: https://i-like-cuts.github.io/
- Repository: https://github.com/I-Like-Cuts/I-Like-Cuts.github.io
- Hosting: GitHub Pages, deployed through GitHub Actions.
- Video: Eoin's existing Vimeo account.

The website starts with plain HTML and CSS; no Node dependencies or build step are needed. The design and technology can evolve in this repository without changing its identity or hosting address.

## Start with your agent

Open or clone this repository in your coding agent and say:

> Set up this website locally and show me a preview. Follow AGENTS.md.

Then use everyday requests such as “Update my biography and show me”, “Publish these changes”, or “Undo the last published change”. The agent handles the commands, branches, checks and deployment. It should only need your help for signing in or for missing content and preferences.

`AGENTS.md` supplies the project context and `.agents/skills/site-workflow/SKILL.md` supplies the detailed workflow. Agents that do not automatically load these files can be asked to read them. Previewing or editing does not publish changes; asking to publish authorizes the complete publishing workflow.

## Preview and check

From this folder in WSL (on this machine), or a terminal on another machine with Python 3.9+:

```sh
python3 scripts/check_site.py
python3 -m http.server 8000 --bind 127.0.0.1 --directory public
```

Open <http://localhost:8000>. Stop the server with Ctrl+C. Edit `public/index.html` for text and `public/styles.css` for appearance. Refresh the browser to see changes. The check validates basic document structure and local asset paths; it is not a complete HTML or accessibility validator.

## Ask Codex to help

The repository includes `.agents/skills/site-workflow/SKILL.md`. Open this repository in Codex and use these prompts:

```text
$site-workflow preview the website
$site-workflow change the welcome text and prepare a pull request
$site-workflow publish the approved website changes
$site-workflow undo the last published text change
```

These are skill prompts, not shell commands or custom slash commands. In Codex CLI or the IDE extension, `/skills` can select a skill, or `$` can mention it. If the skill does not appear, restart Codex. See [OpenAI's skill documentation](https://learn.chatgpt.com/docs/build-skills).

## Publishing

The flow is: edit a branch → preview → pull request → checks → merge into `main` → GitHub Pages.

`.github/workflows/pages.yml` checks pull requests and `main`. After checks pass on `main`, it uploads only `public/` and deploys using GitHub's official Pages actions. A manual run from the Actions tab can redeploy `main`. Pull requests do not publish or get their own hosted preview. Source files, skills and documentation stay out of the website artifact.

Hosting configuration for this repository:

1. The repository is public for GitHub Free Pages; `main` is the production branch.
2. **Settings → Pages → Build and deployment** uses **GitHub Actions**.
3. After the initial setup, changes go through pull requests with the **Check website** status required before merge. No second person's approval is required, so Eoin can publish his own work.
4. **Actions → Website** shows checks, deployment and a check that the expected version is live.
5. The `github-pages` environment permits deployment from `main` only.

The repository name `I-Like-Cuts.github.io` gives the permanent address `https://i-like-cuts.github.io/`. A custom domain can be connected later. The workflow uses GitHub's built-in token; it does not need a personal access token stored as a repository secret. Organisation policies can restrict Actions; an organisation owner must resolve any such restriction.

To undo a published change, create a revert commit and publish it through the same workflow. Git keeps the previous versions available.

Hosting references: [Pages overview](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages) and [custom deployment workflows](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages).

## Tomorrow's design session

Replace the welcome page once the visual direction, selected work, accurate credits and Vimeo links are agreed. Eoin already has a paid Vimeo account; the initial setup does not require migrating video or introducing a CMS.
