# Promotion Execution Status

As of 2026-09-12. Local source baseline: `65886fd` on `main`.

The first launch is published. After access was restored, live remote `main` matched the source baseline, GitHub authenticated as the maintainer with push permission, and the package checks passed again. The material commit is [`b674da8`](https://github.com/wgwtest/novel-writing/commit/b674da826dab41950050ba26f4e8a0140bfa2ba4). Two directory PRs and a bilingual announcement are public; directory acceptance and campaign effectiveness remain unproven.

## Actual State

| Item | State | Evidence / next dependency |
| --- | --- | --- |
| English README refresh | Published | [README](../../README.md); includes quick start and an illustrative dialogue excerpt |
| Chinese landing page | Published | [中文介绍](../../README.zh-CN.md); anonymous public content checked against the committed blob |
| Three bilingual teaching cases | Published | [Examples](../../examples/README.md); original AI-assisted illustrations, not measured A/B runs |
| Public-safe feedback intake | Published | [Issue template](../../.github/ISSUE_TEMPLATE/scene_feedback.md); anonymous public content checked |
| Bilingual project announcement | Published | [Discussions #1](https://github.com/wgwtest/novel-writing/discussions/1); anonymous HTTP 200 and both language titles verified |
| X and Chinese-social-platform posts | Not posted | [Copy is prepared](launch-copy.md); browser page navigation still timed out after permissions were restored; no account session established |
| junminhong directory proposal | Submitted, open | [PR #48](https://github.com/junminhong/awesome-agent-skills/pull/48); two matching entries; signed commit verified |
| heilcheng directory proposal | Submitted, open | [PR #487](https://github.com/heilcheng/awesome-agent-skills/pull/487); one-line entry; local website build passed; signed commit verified; hosted preview needs upstream team authorization |
| Repository discovery metadata | Updated | Description refreshed; existing topics retained and two relevant topics added |
| Existing skills.sh presence | Previously indexed | [Directory page](https://skills.sh/wgwtest/novel-writing/novel-writing); not a campaign accomplishment |
| Local validation | Passed | 20 tests; 13 package files checked; 10 Markdown documents with 40 relative links and balanced code fences; `git diff --check` passed |
| Fresh install through skills CLI | Failed on this host | Two isolated attempts failed in Git clone transport (connection reset / connection failure); telemetry disabled; no general installer-success claim |
| Official skill-installer smoke test | Passed | Public-package download to an isolated destination succeeded; all 13 files match after CRLF/LF normalization; the user's installed skill was not changed |
| Independent review | Passed | No critical, important, or minor findings; source package unchanged, example logic and local links checked |

## Resolved Initial Publication Blocker

The initial environment allowed document edits but made Git metadata read-only and blocked GitHub network requests. Browser interaction also timed out. The user subsequently restored access. The working publication route is now Git plus the authenticated GitHub API. An unavailable local proxy is bypassed per command without changing global configuration.

Existing Git credentials are used in process for the GitHub API and are never printed or saved to campaign files. No browser repair or new credential installation is needed for the GitHub portion of the campaign.

The first package-check attempt could not find `python` in the command environment. The check then passed using the application's bundled Python without changing the system installation. The installable `novel-writing/` tree has no diff from the source baseline; this campaign changes public documentation and feedback intake only. Local Markdown checks resolve file paths and code fences, not remote URLs or a rendered GitHub page.

The user has already authorized the agent to own the promotion workflow.

## Remaining Work

1. Respond to the two directory maintainers if they request changes. Use the existing PRs, not duplicate submissions. Neither listing has been accepted at this checkpoint.
   The Vercel bot on heilcheng #487 requests authorization by the upstream Vercel team for its hosted preview. That is separate from the successful local build and must be handled by that team's authorized member; no authorization link was followed and no permissions were changed.
2. Social posting needs a working browser connection and a usable authorized account. No passwords were requested, no new account was created, and no post was sent through an unverified identity.
3. Review actual scene feedback and refine the skill only when a concrete finding warrants it. These documentation updates do not justify a new skill version tag.
4. No recurring monitor or background posting job is configured. Later review requires a resumed or explicitly scheduled run; the ledger does not imply unattended monitoring.

## Measurement

Campaign day zero is 2026-09-12. A live GitHub API observation recorded 36 stars at 2026-09-12T09:37:43Z; this is a checkpoint, not evidence of campaign-attributed growth. Suggested learning target: five independent trials and three actionable feedback reports within two weeks; these are aspirations, not promised outcomes.

- Record GitHub stars and directory installations separately, with source and observation time. Do not fill unavailable metrics with zero.
- Cached search/directory snapshots are not a live growth baseline. No campaign-attributed growth is claimed.
- A useful trial identifies a task, a model/host, a skill revision, an output, and a concrete observation. Count independent trials, not repeated self-installs.
- Track directory state as proposed, submitted, accepted, declined, or withdrawn; preserve the real link and dates.
- Use voluntary feedback for attribution. Do not add tracking pixels, collect private manuscripts, or infer active users from stars.

## Publication Ledger

| Date (UTC) | Channel / account | Actual public artifact | State |
| --- | --- | --- | --- |
| 2026-09-12 | GitHub / wgwtest | [Material commit b674da8](https://github.com/wgwtest/novel-writing/commit/b674da826dab41950050ba26f4e8a0140bfa2ba4) | Pushed to main; public content verified |
| 2026-09-12 09:36:51 | junminhong directory / wgwtest | [PR #48](https://github.com/junminhong/awesome-agent-skills/pull/48) | Open; commit d957313; two lines added; not merged |
| 2026-09-12 | Repository Announcements / wgwtest | [Discussions #1](https://github.com/wgwtest/novel-writing/discussions/1) | Published; links point to the released documentation |
| 2026-09-12 09:44:44 | heilcheng directory / wgwtest | [PR #487](https://github.com/heilcheng/awesome-agent-skills/pull/487) | Open; commit 8dc1deb; one line added; not merged |

The directory forks and signed proposal branches are retained for future maintainer feedback. No stars, votes, testimonials, or third-party endorsements were manufactured or purchased.
