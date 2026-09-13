# Directory Submission Packet

Initial proposals submitted 2026-09-12: [junminhong #48](https://github.com/junminhong/awesome-agent-skills/pull/48) and [heilcheng #487](https://github.com/heilcheng/awesome-agent-skills/pull/487). Follow-up submitted 2026-09-13: [VoltAgent #1052](https://github.com/VoltAgent/awesome-agent-skills/pull/1052). All three were open and unmerged at the 2026-09-13 check; submission is not acceptance. The preparation notes below are retained for context; the linked PRs contain the actual entries and bodies. Live README and issue/PR checks found no duplicate before each submission.

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

Executed as a two-line, two-README change with matching metadata and alphabetical placement. The Chinese description was adapted to the target README's traditional Chinese. GitHub verified the signature of commit `d957313bbf5254140d1ac8a7dff8a98559e66911`; the public example links were checked before the PR was opened.

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

Executed as a one-line addition beside the existing community prose-writing entry, without introducing a category. In the upstream `website/` checkout, dependency installation and `npm run build` passed, including TypeScript and five generated static pages. The initial dependency download stalled; a retry with bounded fetch settings completed. No website code or lockfile changes were included. GitHub verified the signature of commit `8dc1deba1f911b9136889df7195c206741d366d9`.

## 3. VoltAgent/awesome-agent-skills

[Repository](https://github.com/VoltAgent/awesome-agent-skills) · [Contribution rules](https://github.com/VoltAgent/awesome-agent-skills/blob/main/CONTRIBUTING.md) · [Submitted PR #1052](https://github.com/VoltAgent/awesome-agent-skills/pull/1052)

Submitted 2026-09-13 at 14:37:18 UTC. The guide requires an upstream link at the end of a matching community category, an author prefix, a description of at most ten words, and evidence of real community use. The README additionally requests third-person descriptions. Productivity and Collaboration already includes writing and book-related skills, so no new category was created.

Actual entry:

```markdown
- **[wgwtest/novel-writing](https://github.com/wgwtest/novel-writing)** - Plans and revises fiction with viewpoint, dialogue, and style checks.
```

Title: `Add skill: wgwtest/novel-writing`. GitHub verified the signature of commit `291a0adb02ebeefb7198b1b4e161401f46fc439a`. An anonymous API read confirmed the public PR, expected fork and commit, and exactly one README addition with no deletions. It remained open and unmerged.

The proposal discloses maintainer affiliation and AI assistance, limits the documented host to Codex, and distinguishes editorial examples from benchmarks. Public evidence supplied for maintainer review:

- [Totechnology/ensemble-novel-writing attribution](https://github.com/Totechnology/ensemble-novel-writing#design-and-attribution) explicitly identifies this project as a source for its adaptation. This is public reuse evidence, not an endorsement or a measured user outcome.
- [Previously merged Codex directory PR #29](https://github.com/composio-community/awesome-codex-skills/pull/29), merged on 2026-04-22. This is historical curation, not a new campaign result or an independent usage test.
- Public releases date to April 2026 and continue through [v0.4.1-public](https://github.com/wgwtest/novel-writing/releases/tag/v0.4.1-public). Fresh source checks passed: 20 tests and 13 package files.

Whether this evidence satisfies VoltAgent's community-use threshold remains the maintainers' decision. No acceptance or exposure outcome is claimed.

## Existing Distribution and Deferred Channels

- [skills.sh listing](https://skills.sh/wgwtest/novel-writing/novel-writing): already discoverable before this campaign. Linking it is not a new listing submission. The [CLI documentation](https://skills.sh/docs/cli) describes installation telemetry; installation counts are not active-writer counts.
- [SkillsMP FAQ](https://skillsmp.com/docs/faq), checked 2026-09-13: describes automatic GitHub indexing, a public `SKILL.md` with `name` and `description`, and a `claude-skills` or `claude-code-skill` topic. It says manual submission is coming later. This repository has the public manifest, but its documented host is Codex; no unverified Claude-compatibility topic was added. No manual submission was made. Public search did not establish whether it is indexed; absence from search is not proof of absence.
- [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code): not submitted automatically. Its current recommendation rules require a human-authored submission through the web interface; an autonomous AI-authored recommendation is outside that route.
- [Hacker News guidelines](https://news.ycombinator.com/newsguidelines.html): exclude from autonomous AI-written posting. Its rules prohibit generated or AI-edited text. No HN copy is supplied for posting.
- Personal social promotion and account registration were stopped at the user's request. No new email or social account was created. Other directories require an individually relevant, rules-compliant proposal; no bulk submission, paid promotion, direct-message campaign, or recurring posting job is configured.
