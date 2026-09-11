---
name: site-workflow
description: Help maintain Eoin's portfolio website by previewing changes, preparing a GitHub pull request, publishing through GitHub Pages, or reverting a published change. Use for this repository's editing and publishing workflow.
---

# Eoin's website workflow

Read AGENTS.md and the repository README, and inspect the current branch, working tree, and remote before acting. The permanent repository is `I-Like-Cuts/I-Like-Cuts.github.io`; production is `https://i-like-cuts.github.io/`. Explain outcomes in plain language for someone learning Git. Run project commands in WSL on Mark's machine. Use the actual checkout path and operating system on Eoin's machine.

## First-time setup

Inspect available Python 3.9+, Git and GitHub CLI (`gh`). Local preview needs only Python; do not block preview on GitHub authentication. There are no application dependencies to install. If the user asks for setup, handle routine setup within the existing authorizations, and request interactive sign-in only when remote work needs it. Check `gh auth status` and repository access before pushing. Verify `origin` matches this repository; do not silently overwrite a different remote. Explain missing prerequisites with the smallest action needed from the user. Plain-language requests invoke this workflow; skill syntax is optional.

Only `public/` is published. It is plain HTML and CSS with no package installation or build step. Keep asset URLs relative so the website works beneath a repository URL. Videos belong on Vimeo; use confirmed embed URLs when requested. Do not invent film credits or contact information.

## Preview or edit

Preserve existing work. Make the requested changes on a descriptive branch when Git is connected, and run `python3 scripts/check_site.py`. Start `python3 -m http.server 8000 --bind 127.0.0.1 --directory public` from the repository root and give the preview URL. If the port is occupied, choose another port. Inspect desktop and mobile layouts using a browser when available; distinguish browser checks from the script's limited smoke check. A preview request does not request publication.

## Prepare a review

Review the diff and check results. Stage only files belonging to the requested change. Commit and push a feature branch and open a pull request when the user's request includes preparing or submitting a review. Use `gh` with the repository verified from the remote. Explain that the pull request is a proposed update, and the current workflow checks it without creating a hosted preview.

## Publish

An explicit request to publish authorizes completing the relevant commit, push and merge; do not ask again unless the target or content is ambiguous. Inspect current PR checks and the actual diff before merging. Respect repository merge policies. A merge or push to `main` triggers `.github/workflows/pages.yml`; manual dispatch also deploys only from `main`.

Track the workflow for the exact published commit, inspect failures and fix relevant issues. Obtain the live URL from the Pages API or deployment output. Verify an HTTP success response and the expected changed content before reporting publication. If authentication, repository access or Pages configuration blocks deployment, report the concrete missing prerequisite and preserve local work. Do not create another repository or change repository visibility to bypass it.

## Undo

Identify the specific change the user wants undone. Use a new revert commit and the same review/publishing workflow; do not reset or force-push shared history. Inspect parent commits before reverting a merge. Undoing a local edit and publishing a rollback are distinct requests: follow the user's scope. Verify the restored content after a requested rollback deploys.
