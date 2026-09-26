# Manuscript Lifecycle and Author Feedback

Use this reference when setting up a fiction project or when a task crosses manuscript versions: drafting or revising a chapter for delivery, receiving the author's hand-edited or annotated draft, comparing revisions, or reusing earlier feedback. The active agent using `novel-writing` coordinates the workflow; it is not a file watcher. Other writing, review, or de-AI skills may produce or inspect prose when available and relevant, but do not independently choose the formal version or maintain a second case library.

## Set up a new project

Installing this skill does not create a novel project or any manuscript directories. A planning-only discussion does not create them either. When the user asks to create a project that will hold manuscript files:

1. Inspect any destination and conventions the user has already specified. If the storage contract is not yet agreed, show one compact proposal before creating folders or choosing version names. Cover the formal chapter entry, working revisions, frozen AI deliveries and author originals, the feedback/case index, version names, and when a candidate becomes a delivery or an accepted draft. Note whether existing text will be imported or left in place.
2. Ask the user to confirm or adjust only unresolved choices that affect where files will be written or which version is authoritative. If the user already supplied or approved the complete contract in this conversation, use it without another confirmation. Avoid a questionnaire for every chapter.
3. Write the agreed contract to a project-local rule file discoverable in later sessions, such as `AGENTS.md` when that is the host's convention. Create only the directories needed for the authorized project work, then verify and report their paths. Keep book-specific paths, names, and preferences in that project, not in this reusable skill.

For an existing project, read its layout and rules first. Preserve them unless the user requests a migration; propose only the missing or conflicting part before changing it. An example three-layer map may help explain the choice, but is not a fixed directory template.

## Establish the project's contract

Read the current project's rules, chapter status, and source-of-truth files before choosing a mother draft or output path. Resolve three distinct roles, even if a project uses different names or combines storage:

- **Formal reading entry:** the project's current chapter file for the author to read or edit. It may now contain the author's own changes; identify the last actual AI delivery separately. A delivered draft is not necessarily author-approved or published.
- **Working revisions:** drafts, review notes, and candidate edits that must not become formal merely because their revision number is highest.
- **Frozen evidence and learning:** actual AI deliveries, exact author edits/annotations, comparisons, and source-linked feedback cases. A case is an interpretation of evidence, not a substitute for its full versions.

Follow an existing project layout and status protocol. Do not impose a universal directory tree, copy a book's case library into the global skill, or infer the canonical chapter from filenames alone. If the project lacks an explicit rule for a required handoff, present the narrow missing choice and establish it before changing the formal entry; preserve the current source meanwhile. Read-only diagnosis does not authorize prose revision or promotion.

## Deliver a chapter or approved revision

1. Identify the current authoritative mother draft, chapter boundary, and any concurrent changes. Preserve an author-edited mother draft exactly before altering it; a previous AI version is evidence, not a replacement for the author's changes.
2. Work in the project's process layer. Invoke the project's chosen drafting, review, and de-AI tools only for the requested work, passing the same author constraints and chapter facts to each. Review their outputs against the mother draft and adjacent context.
3. For an actual handoff, freeze the **exact text delivered** with enough provenance to identify chapter, source version, time/status, and integrity where the project requires it. Internal candidates and trial drafts are not automatically deliveries.
4. If this is an authorized formal handoff, verify the deliverable, then update the project's formal reading entry and its status/index according to local rules. Check that the formal text equals the recorded delivery, frozen originals remain unchanged, and the process record points to both. If the user requested only a trial or process draft, keep it in the process layer and label it accordingly. Report delivery separately from author acceptance or publication.

If a source changed concurrently or a required version cannot be identified, reconcile the evidence before overwriting a formal file. Never fill an evidence gap by recreating an alleged original from memory.

## Receive an author edit or annotation

1. Where the user's standing instruction or project protocol authorizes archiving, save the exact received file, including comments, before cleanup or text edits. Otherwise, inspect it without writing and explain what needs preservation before any later edit. Compare it with the last **actual AI delivery** to this author, not an internal draft or an unrelated later revision. Label uncertain provenance explicitly.
2. Group meaningful deletions, additions, rewrites, and retained material by narrative function. Examine plot causality, scene and viewpoint choices, dialogue, and sentence patterns; analyze what the old passage did, what still works after the edit, plausible reasons for the change, and contrary evidence. Do not treat untouched text as blanket approval.
3. When the author's note states a reason, record it as stated. When a consequential change remains ambiguous after analysis, ask the author in this revision exchange with the concrete before/after example and the competing interpretations. Do not make the author fill in a database. Until answered, keep the factual difference and editorial analysis separate from confirmed preference; do not promote a guess into a rule.
4. Where the project's feedback protocol authorizes case maintenance, add a reusable case only when its evidence and applicability are clear. Link the exact before/after text or annotation and frozen source versions; distinguish explicit author intent, confirmed explanation, and editorial inference. Record the original function, observed effect, conditions where the lesson applies, and at least one boundary or counterexample. Update an existing case when it fits; do not manufacture a new universal ban from a typo, isolated fact correction, or single deletion. Summarize only recurring, supported preferences in the project's preference file. Otherwise, report a proposed case without writing it.

Receiving feedback authorizes analysis; preservation and case updates follow the user's standing instructions and project protocol. Revise the prose or replace the formal reading entry only when the user has requested that revision and handoff.

## Reuse the learning

Before a relevant review, rewrite, or de-AI pass, search the project's preference index and case library for the current issue. Read the specific case evidence, nearby prose, current book rules, and any counterexample; avoid loading every card as a checklist. Cite the case ID and passage when relying on an author preference. If no case applies, label the advice as this round's editorial judgment. A case suggests a question to test against the current scene; it does not automatically trigger a rewrite.

Ordinary text search is enough while it retrieves relevant cases reliably. A later full-text or vector index may help discovery, but cannot establish the author's motive or decide applicability. Keep the project-local archive and cases as the authority.
