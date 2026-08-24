# Novel Writing

[![Novel Writing social preview](assets/social-preview.png)](https://github.com/wgwtest/novel-writing)

[![GitHub stars](https://img.shields.io/github/stars/wgwtest/novel-writing?style=social)](https://github.com/wgwtest/novel-writing/stargazers)
[![GitHub release](https://img.shields.io/github/v/release/wgwtest/novel-writing)](https://github.com/wgwtest/novel-writing/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](./LICENSE)

A Codex skill for fiction planning, chapter drafting, scene continuation, and revision that stays concrete about narrative problems instead of giving vague workshop-style feedback.

## Why Use It

This skill is meant for longform fiction work where narrative judgment matters.

It helps Codex:

- plan scenes, chapters, arcs, and whole stories with an explicit causal spine
- draft or continue fiction prose without collapsing everything into summary
- keep dialogue embodied without attaching arbitrary gestures to every line
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

Manual install:

```bash
git clone https://github.com/wgwtest/novel-writing.git
mkdir -p ~/.codex/skills
cp -R novel-writing/novel-writing ~/.codex/skills/novel-writing
```

For local development with easy upgrades:

```bash
git clone https://github.com/wgwtest/novel-writing.git
mkdir -p ~/.codex/skills
ln -s "$(pwd)/novel-writing/novel-writing" ~/.codex/skills/novel-writing
```

Restart Codex after installing or updating the skill.

On Windows, maintainers can install the development checkout as a junction with
backup protection:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\install-local-dev-link.ps1
```

Installer-style inputs:

- repo: `wgwtest/novel-writing`
- path: `novel-writing`

## Repository Layout

- `novel-writing/`: installable skill package
- `scripts/`: local development and package validation helpers
- `CODEX_START_HERE.md`: maintainer startup and release workflow
- `README.md`: landing page for humans
- `.github/`: templates for issues and pull requests

The installable skill lives in a subdirectory so the repository root can hold public-facing files without leaking extra repo metadata into the package.

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
