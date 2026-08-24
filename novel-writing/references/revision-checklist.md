# Revision Checklist

Use this file when reviewing an existing fiction chapter or scene.

## Output Format

Report findings as a structured list. Each finding must include:

- `Location`
- `Problem type`
- `What happens now`
- `Why it fails`
- `Revision direction`
- `Should this become a project rule?`

If there are no findings, say so explicitly and mention any residual uncertainty.

## Recommended Problem Types

- cognition and disclosure
- decision ownership
- dialogue adjacency
- spatial or action causality
- chapter continuity
- character introduction
- scene structure
- style fidelity
- realism constraint
- viewpoint overreach
- pacing
- dialogue clarity
- dialogue embodiment

## Minimum Review Procedure

Report structural, causal, responsibility, and continuity failures before sentence-level polish.

### 1. Check cognition and responsibility

Ask:

- what each consequential character can access and how they classify it
- which fact, judgment, intention, or misrecognition changes the next choice
- who experiences, owns, decides, acts, and coordinates afterward
- whether dialogue reveals only what this speaker would say to this audience

### 2. Check reader anchoring

Ask:

- does the reader know who is present?
- does the reader know where the scene is?
- does the reader know why the current beat matters?

### 3. Check structural progression

Ask:

- what changes from start to finish?
- which segment is redundant?
- where does tension rise or stall?
- does evidence or a failed attempt create a reason for the next explanation?
- can the action occur in the established space and order?

### 4. Check dialogue embodiment

Ask:

- do characters merely take turns delivering information?
- does the listener's reaction change the next line, action, or tactic?
- are nearby actions functional, decorative, or merely procedural?
- does a meeting read like minutes, or a laboratory scene like a technical log?
- have emotion labels and interchangeable gestures been added where a scene-specific response is needed?
- does the viewpoint select reactions, or does narration visit everyone in turn?

### 5. Check chapter interfaces

Ask whether positions, knowledge, ongoing actions, injuries, objects, unresolved questions, and responsibility pass cleanly into and out of adjacent prose.

### 6. Check style preservation

Ask:

- has any concrete material been flattened into summary?
- has voice been replaced with generic polish?
- have emotionally loaded details been neutralized?

### 7. Check realism

Ask:

- can the character observe this?
- can the character understand this?
- can the institution or body support this?
- does a crowd's speech reflect status, information, risk, and speaking cost?
- does spectacle retain a mechanism and a physical or social consequence?

### 8. Check manuscript hygiene when delivering plain text

Run the bundled checker as `python <skill-directory>/scripts/check_manuscript_text.py <file-or-directory>` when the output format and access allow it. Treat heuristic warnings as review prompts, not automatic literary defects.

## High-Frequency False Assumptions

Flag these aggressively:

- "the author knows it, so the reader must know it"
- "there is a clear mental image, so the prose must already show it"
- "the event happens, so the structure must be working"
- "cleaner prose is automatically better prose"
- "because the writer knows a hidden motive, the prose can announce it before the action reveals it"
- "because a detail matters later, a character may speak as if they already know it"
- "adding gestures means the dialogue is now embodied"
- "equipment is moving, so the characters must be active"
- "every important character needs a spoken reaction"

## Example Finding Shape

```markdown
- Location: Chapter 3, first paragraph after the birth announcement
  Problem type: character introduction
  What happens now: family members are named and react before their roles are grounded
  Why it fails: the reader is asked to track emotional significance before they know who these people are
  Revision direction: anchor the family hierarchy and each key relative's relationship to the mother or child before stacking reactions
  Should this become a project rule?: yes
```
