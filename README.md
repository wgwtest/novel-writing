# Novel Writing

[English](README.md) | [简体中文](README.zh-CN.md)

[![GitHub stars](https://img.shields.io/github/stars/wgwtest/novel-writing?style=social)](https://github.com/wgwtest/novel-writing/stargazers)
[![GitHub release](https://img.shields.io/github/v/release/wgwtest/novel-writing)](https://github.com/wgwtest/novel-writing/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](./LICENSE)
[![skills.sh](https://skills.sh/b/wgwtest/novel-writing)](https://skills.sh/wgwtest/novel-writing/novel-writing)

A Codex skill for fiction with grounded viewpoints, consequential dialogue, and the author's own voice.

When a scene reads like meeting minutes, adding a nod to every line is not enough. The question is: **what does this exchange make someone do differently?**

## See the Difference

An illustrative excerpt, constructed for explanation—not a measured model comparison:

**Before**

> "We can send it today," the workshop manager said.
>
> "The latch still sticks," the apprentice said.
>
> "Then test it again."

**One possible revision**

> "We can send it today." The workshop manager slid the delivery slip toward his apprentice.
>
> She set the model case on top of it. "Open it."
>
> The latch caught under his thumb.
>
> He drew the slip out from under the case. "How long to replace it?"

The failed opening changes the next question. The case is doing more than keeping someone's hands busy.

[Read the full dialogue case](examples/01-dialogue.md), or explore [viewpoint and knowledge](examples/02-viewpoint.md) and [voice-preserving revision](examples/03-style.md). All examples include source passages, prompts, and editorial explanations.

## Quick Start

With Node.js and npm available, install through the [skills CLI](https://skills.sh/docs/cli):

```bash
npx skills add https://github.com/wgwtest/novel-writing --skill novel-writing
```

Select Codex when prompted. This is a third-party installer; inspect its prompts and installation scope. For alternatives, see [Install](#install).

You can also ask Codex's built-in `skill-installer` to install the `novel-writing` folder from `wgwtest/novel-writing`. Its download-based path is an alternative when a Git-based install cannot connect.

Try a small scene first:

```text
Use novel-writing. Review the scene below for viewpoint overreach and
transcript-like dialogue. Give findings with locations, explain why each
matters, then suggest a local revision. Preserve my voice and any deliberate
silence. Do not invent hidden motives or resolve uncertainty for me.

[Paste a scene you are allowed to share.]
```

Not sure what to paste? Use a source passage from the [examples](examples/README.md). These are inspectable teaching cases, not a benchmark or a promise that every model will produce the same output.

## Why Use It

This skill is meant for longform fiction work where narrative judgment matters.

It helps Codex:

- plan scenes, chapters, arcs, and whole stories with an explicit causal spine
- draft or continue fiction prose without collapsing everything into summary
- keep dialogue embodied without attaching arbitrary gestures to every line
- distinguish author-side dialogue checks from prose, preserving natural silence without annotating every response
- review prose with concrete findings instead of soft impressions
- protect style-bearing material during revision
- check whether scenes obey realism and access limits

## Good Fit

Use this repo when the task is mainly about fiction craft:

- scene, chapter, arc, volume, or whole-story planning
- standalone story synopsis or canon-document structure
- prose continuation
- rewrite while preserving voice
- structural review of a chapter
- character introduction quality
- realism constraints inside a scene

If your main problem is project recovery, chapter-state tracking, or workspace governance across a large novel, use [novel-project-strategy](https://github.com/wgwtest/novel-project-strategy) alongside this skill.

## Example Prompts

- `Use novel-writing. Review this chapter and give concrete findings with locations, not vague feedback.`
- `Plan a chapter that introduces the rival clearly and moves the relationship forward.`
- `Build a standalone volume outline that separates pre-story state, causal story, author truth, and reveal boundaries.`
- `Continue this scene without flattening the author's voice or cutting style-bearing detail.`
- `Review this meeting or laboratory scene for transcript-like dialogue, decorative gestures, and procedural action that does not change the human exchange.`

## Install

The quick-start command is also listed on the [skill's directory page](https://skills.sh/wgwtest/novel-writing/novel-writing). The CLI has its own dependencies and telemetry policy; see its [documentation](https://skills.sh/docs/cli).

Manual install with a POSIX shell (use a fresh destination; do not overwrite an existing installation without checking it):

```bash
git clone https://github.com/wgwtest/novel-writing.git
mkdir -p ~/.agents/skills
cp -R novel-writing/novel-writing ~/.agents/skills/novel-writing
```

For local development with easy upgrades:

```bash
git clone https://github.com/wgwtest/novel-writing.git
mkdir -p ~/.agents/skills
ln -s "$(pwd)/novel-writing/novel-writing" ~/.agents/skills/novel-writing
```

These paths follow the current [official local-skill documentation](https://learn.chatgpt.com/docs/build-skills#where-codex-loads-local-skills). Codex detects skills automatically; restart it if the new skill or update does not appear. Avoid installing duplicate copies into multiple discovery locations.

On Windows, the existing maintainer helper installs the development checkout as a junction with backup protection. It targets the repository's legacy `~/.codex/skills` development layout; check the script and your host's discovery settings before using it. The quick-start installer is the general entry point:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\install-local-dev-link.ps1
```

Installer-style inputs:

- repo: `wgwtest/novel-writing`
- path: `novel-writing`

## Repository Layout

- `novel-writing/`: installable skill package
- `examples/`: public, original teaching cases and trial instructions
- `README.zh-CN.md`: Chinese introduction and getting started
- `docs/promotion/`: publication copy, directory candidates, and execution status
- `scripts/`: local development and package validation helpers
- `CODEX_START_HERE.md`: maintainer startup and release workflow
- `README.md`: landing page for humans
- `.github/`: templates for issues and pull requests

The installable skill lives in a subdirectory so the repository root can hold public-facing files without leaking extra repo metadata into the package.

## Scope and Requirements

The documented host is Codex. Other agents may understand the format, but this repository does not claim tested compatibility with every host. The core package is Markdown instructions and references, not a model, autonomous novel generator, or publishing service.

The optional manuscript-text checker uses Python 3 and its standard library. Ordinary narrative guidance requires no additional service credentials. Reading or editing your manuscript still uses the host's normal permissions and data handling; this skill does not make those interactions local-only or private by itself. No manuscript upload to a separate service is required by the skill.

## Help Improve a Real Scene

Have a passage where the guidance fails? [Share a minimal, public-safe example](https://github.com/wgwtest/novel-writing/issues/new?template=scene_feedback.md). Include your prompt, model/host, skill revision, and the specific sentence or choice that went wrong. A short invented reproduction is enough—please do not post a private manuscript or someone else's unpublished work.

If you want to compare runs, follow the [trial protocol](examples/README.md#try-it-on-your-own-scene). Installs, stars, and writing quality are different signals.

## Related Repos

- [novel-project-strategy](https://github.com/wgwtest/novel-project-strategy): longform fiction workflow, reload order, chapter-state, and sync discipline
- [project-engineering-strategy](https://github.com/wgwtest/project-engineering-strategy): engineering workflow governance for code projects

## Contributing

If you want to improve the skill, start with [CONTRIBUTING.md](./CONTRIBUTING.md). The highest-value contributions are better prompts, cleaner narrative diagnostics, and sharper boundaries around when this skill should or should not fire.

## License

MIT. See [LICENSE](./LICENSE).

## Maintainer Note

This repository is the source of truth for `novel-writing`. Edit the installable
package only under `novel-writing/`; local Codex installations and copies in
other repositories are runtime links or derived mirrors, never editable
sources. Run
`powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\check-package.ps1`
before committing or releasing a change.
