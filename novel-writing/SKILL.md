---
name: novel-writing
description: Use when planning, drafting, revising, or reviewing fiction chapters where character introduction, scene structure, style fidelity, or realism constraints matter.
---

# Novel Writing

## Overview

Use this skill for fiction work that needs narrative craft, not just sentence-level cleanup. It is designed for three stages: planning a chapter, drafting or continuing prose, and reviewing finished fiction for concrete problems.

## When to Use

Use this skill when the user asks to:

- plan a chapter, scene, arc, or reveal sequence
- continue or rewrite fiction prose
- check whether a chapter is structurally sound
- review whether characters are introduced clearly
- preserve an author's original voice while revising
- test whether a scene obeys real-world limits such as visibility, procedure, age, or capability

Do not use this skill for:

- poetry-only requests
- screenplay formatting work
- pure copyediting where narrative judgment is not needed
- non-fiction writing

## Stage Selection

First decide which stage the task belongs to.

### 1. Planning

Use when the user is deciding what a chapter or scene should do before prose is written.

Read:

- `references/planning.md`
- `references/scene-and-structure.md` when chapter flow is the main concern
- `references/realism-constraints.md` when the chapter depends on real-world limits

### 2. Drafting or Continuing

Use when the user wants new fiction prose, a rewrite of prose, or a continuation of an existing chapter.

Read:

- `references/character-introductions.md`
- `references/scene-and-structure.md`
- `references/style-fidelity.md`
- `references/realism-constraints.md` when the scene depends on real-world constraints

### 3. Reviewing

Use when the user wants critique, diagnosis, or revision advice on existing fiction.

Read:

- `references/revision-checklist.md`
- then load the specific reference files that match the problems you find

## Long-Fiction Context Strategy

When the fiction project is long enough that loading the entire formal draft would be wasteful, use context LOD instead of full-text-first reading.

### Load order

- `L0 Task`: the immediate writing or review job
- `L1 Hard constraints`: outline, timeline, setting, issue records, local project rules
- `L2 Near-field full text`: current chapter, adjacent chapters, and linked manuscript layers when fidelity matters
- `L3 Far-field structure`: chapter cards, timeline slices, and outline slices
- `L4 Cold zone`: unrelated future chapters and distant full text, excluded by default

- If you are directly revising a chapter, read that chapter's full text.
- If dialogue rhythm, psychological detail, ambiguity, flirtation, or body-detail writing matters, read the relevant full text instead of relying on summary material.
- If structure cards conflict with prose, trust the prose and update the cards later.
- If the available structured context is insufficient, expand by targeted full-text reads, not by loading the whole novel.
- Future-chapter prose is excluded by default unless a confirmed continuity dependency requires it.

### Collaboration-state discipline

- If the project tracks chapter state, treat chapters as the primary work object and raw-draft batches as source objects.
- Distinguish drafted, confirmed, and synced states instead of collapsing them into a single notion of "done."
- Do not treat generic approvals such as "continue", "ok", or "good" as confirmation unless the project rule explicitly says so.
- Do not promote chapter facts into outline or setting sync unless the user or the local project rule explicitly allows that promotion.
- If chapter-state files and chapter cards exist, read them before inferring workflow status from prose alone.
- If an edit-record overview exists, read the recent records for workflow context, but treat chapter-state files and chapter cards as the source of current truth.

## Hard Rules

### Reader Knowledge Is Not Author Knowledge

Never assume the reader already knows:

- who a character is
- how people are related
- what a place looks like
- why a behavior matters

If the author knows it but the prose has not shown it, treat it as missing.

### Important Characters Cannot Enter Naked

When an important character first enters the story in an effective way, the prose must give the reader enough to anchor them:

- identity or role
- relationship to the current event or viewpoint
- first impression

If the character is a villain, love interest, rival, or core ally, the prose also needs at least one recognisable trait such as:

- appearance
- clothing
- posture
- voice
- habitual gesture
- other people's reaction

### Scene Information Must Obey Access Limits

Characters may only know what the scene allows them to know.

Always separate:

- what they can see
- what they can hear
- what they can physically reach
- what they can correctly infer

Seeing something is not the same as understanding it. Getting close once is not the same as having time to inspect it.

### Every Scene Segment Must Earn Its Place

Every chapter or functional segment should be able to answer:

- What problem is this segment handling?
- Who changes here?
- What moves forward by the end?

If the prose only accumulates content without changing the situation, treat it as structurally weak.

### Protect Style-Bearing Material

Default to preserving the author's:

- dialogue
- inner thoughts
- digressive texture
- observational details
- flirtation or ambiguity
- rhythm-bearing repetition

You may fix wording, punctuation, transcription noise, and paragraph breaks. Do not silently compress concrete material into summary.

### Review Output Must Be Specific

When reviewing fiction, report concrete findings with:

- location
- problem type
- why it fails
- how to revise it

Avoid vague comments such as "a bit stiff" or "could be improved."

### Project Rules Override This Skill

If the fiction project already has local rules, style contracts, or manuscript-layer rules, follow those first. This skill supplies general fiction method, not project-specific law.

## Working Pattern

1. Identify the stage.
2. Identify the minimum context tier needed for the task.
3. Load only the reference files needed for that stage.
4. Load project-local outline, timeline, setting, and issue files before pulling extra prose.
5. Pull near-field full prose when revising language, style, or chapter continuity.
6. Apply the hard rules before proposing prose changes.
7. If reviewing, produce structured findings before any summary.
8. If the task touches sensitive realism constraints and you are unsure, say what must be verified instead of bluffing.

## References

- `references/planning.md`: chapter-task planning and POV control
- `references/character-introductions.md`: first-entry rules for characters
- `references/scene-and-structure.md`: scene progression and chapter shape
- `references/style-fidelity.md`: preserving authorial texture during revision
- `references/realism-constraints.md`: reality checks for institutions, bodies, and access limits
- `references/revision-checklist.md`: structured review output
