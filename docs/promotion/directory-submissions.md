# Directory Submission Packet

Prepared 2026-09-12. These are candidate entries and draft PR bodies, **not submitted PRs**. Recheck current upstream rules, section names, and open/closed PRs before sending. Web retrieval can be cached; no duplicate clearance or acceptance is claimed.

## 1. junminhong/awesome-agent-skills

[Repository](https://github.com/junminhong/awesome-agent-skills) · [Contribution rules](https://github.com/junminhong/awesome-agent-skills/blob/main/CONTRIBUTING.md)

Candidate placement: Agent Skills → Communication & Writing, subject to the current README taxonomy. The contribution guide permits self-nominations with disclosed affiliation, requires a neutral listing in both `README.md` and `README_ZH.md`, alphabetical placement, and matching metadata. Every PR commit must display Verified on GitHub. Check for duplicate listings and earlier PRs before editing; if a previous proposal exists, continue that discussion instead of creating another.

English entry:

```markdown
- [Novel Writing](https://github.com/wgwtest/novel-writing) — Guides fiction planning, drafting, and revision with viewpoint, scene-causality, dialogue, and style-preservation checks. `Type: Skill` · `Platforms: Codex`
```

Chinese entry:

```markdown
- [Novel Writing](https://github.com/wgwtest/novel-writing) — 指导小说构思、起草与修订，检查人物视角、场景因果、对白及文风保留。 `Type: Skill` · `Platforms: Codex`
```

Draft PR title: `docs: add Novel Writing`

Draft PR body:

```markdown
## Summary

Proposes Novel Writing in Communication & Writing, with synchronized English
and Chinese entries. It is a single Codex skill, not a collection or SaaS tool.

## Review pointers

- Source: https://github.com/wgwtest/novel-writing
- Installable skill: https://github.com/wgwtest/novel-writing/tree/main/novel-writing
- License: https://github.com/wgwtest/novel-writing/blob/main/LICENSE
- Usage and dependencies: the repository README
- Teaching examples: the repository examples/ directory

Affiliation: project maintainer; prepared with AI assistance.
Examples are constructed editorial illustrations, not benchmark results.
Platform claim: Codex only.
```

The body becomes accurate as a submission only after the two-README diff exists and the example links are public. Respect the upstream PR template and complete only checks actually verified, including the Verified commit requirement.

## 2. heilcheng/awesome-agent-skills

[Repository](https://github.com/heilcheng/awesome-agent-skills) · [Contribution rules](https://github.com/heilcheng/awesome-agent-skills/blob/main/CONTRIBUTING.md)

The guide indexes upstream skill repositories and asks for metadata in the relevant README section. It calls for a usable `SKILL.md`, concrete examples, and a website build before submission. Find the current writing-related section and match its existing entry format. Do not add an unagreed category or copy the skill implementation into the directory.

Candidate description:

```text
Novel Writing — Codex skill for fiction planning, drafting, and revision,
with checks for viewpoint access, scene causality, dialogue behavior,
and preservation of the author's voice. MIT; English and Chinese examples.
```

Draft PR title: `docs: index Novel Writing fiction skill`

Draft PR body:

```markdown
## Proposal

Index https://github.com/wgwtest/novel-writing in the appropriate writing section.
The implementation remains upstream under novel-writing/ and includes SKILL.md,
reference guides, and an optional Python standard-library manuscript checker.

The examples/ directory contains three public, original teaching cases with
source passages, prompts, diagnoses, and possible revisions. They are editorial
illustrations, not measured model comparisons.

Affiliation: project maintainer; prepared with AI assistance.
Documented host: Codex. License: MIT.
```

Before submission, run the build required by the current contribution guide in a permitted checkout and report its real result. It has **not** been run in this campaign preparation. Do not tick a passing-build checkbox based on the upstream project's CI or this repository's unrelated package tests.

## Existing Distribution and Deferred Channels

- [skills.sh listing](https://skills.sh/wgwtest/novel-writing/novel-writing): already discoverable before this campaign. Linking it is not a new listing submission. The [CLI documentation](https://skills.sh/docs/cli) describes installation telemetry; installation counts are not active-writer counts.
- [Hacker News guidelines](https://news.ycombinator.com/newsguidelines.html): exclude from autonomous AI-written posting. Its rules prohibit generated or AI-edited text. No HN copy is supplied for posting.
- Other lists and social platforms: no bulk submission. Review relevance and current posting rules, establish a usable authorized account, and publish one focused contribution before expanding. No paid promotion, account creation, direct-message campaign, or recurring posting job is configured.
