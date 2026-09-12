# Promotion Execution Status

As of 2026-09-12. Local source baseline: `65886fd` on `main`.

Execution resumed after the user restored filesystem and network access. Live remote `main` matched the source baseline, GitHub authenticated as the maintainer with repository push permission, and the package checks passed again. Publication and directory submissions are in progress; the ledger below records only verified outcomes.

## Actual State

| Item | State | Evidence / next dependency |
| --- | --- | --- |
| English README refresh | Written locally | [README](../../README.md); not committed or published |
| Chinese landing page | Written locally | [中文介绍](../../README.zh-CN.md); not committed or published |
| Three bilingual teaching cases | Written locally | [Examples](../../examples/README.md); original AI-assisted illustrations, not measured A/B runs |
| Public-safe feedback intake | Written locally | [Issue template](../../.github/ISSUE_TEMPLATE/scene_feedback.md); requires publication to activate |
| English and Chinese posts | Drafted, not posted | [Publication copy](launch-copy.md) |
| Two directory proposals | Drafted, not submitted | [Submission packet](directory-submissions.md); live duplicate/rule checks still required |
| Existing skills.sh presence | Previously indexed | [Directory page](https://skills.sh/wgwtest/novel-writing/novel-writing); not a campaign accomplishment |
| Local validation | Passed | 20 tests; 13 package files checked; 10 Markdown documents with 41 relative links and balanced code fences; `git diff --check` passed |
| Fresh install through skills CLI | Not run | Command checked against the public directory; network restrictions prevented a new-install smoke test |
| Official skill-installer smoke test | Passed | Downloaded the public package to an isolated temporary destination; the user's installed skill was not changed |
| New remote commit / PR / post | None created | No public publication URL exists for these changes |

## Resolved Initial Publication Blocker

The initial environment allowed document edits but made Git metadata read-only and blocked GitHub network requests. Browser interaction also timed out. The user subsequently restored access. The working publication route is now Git plus the authenticated GitHub API. An unavailable local proxy is bypassed per command without changing global configuration.

Existing Git credentials are used in process for the GitHub API and are never printed or saved to campaign files. No browser repair or new credential installation is needed for the GitHub portion of the campaign.

The first package-check attempt could not find `python` in the command environment. The check then passed using the application's bundled Python without changing the system installation. The installable `novel-writing/` tree has no diff from the source baseline; this campaign changes public documentation and feedback intake only. Local Markdown checks resolve file paths and code fences, not remote URLs or a rendered GitHub page.

The user has already authorized the agent to own the promotion workflow.

## Resume Order

1. Restore a permitted GitHub channel; inspect live `main` and preserve any new upstream or local changes. Review the exact documentation scope before committing. No skill version tag is required for these public-documentation-only changes.
2. Publish the README, examples, and feedback template together. Verify their anonymous public links; record the actual commit URL below. Do not publish posts containing example links before those files are public.
3. Check the two candidate directories for duplicates and current rules. Submit one focused PR per eligible directory, meet each validation/signing requirement, and record the resulting PR URL. A submitted PR is not an accepted listing.
4. On an available authorized social account, check platform/community rules, then publish the matching post. No account creation, paid boost, unsolicited DM, or vote solicitation is part of this packet.
5. Review actual feedback when a follow-up run is requested or explicitly scheduled. No background or recurring job has been created by preparing these documents.

## Measurement

Use the first verified public publication as campaign day zero. Suggested learning target: five independent trials and three actionable feedback reports within two weeks; these are aspirations, not promised outcomes.

- Record GitHub stars and directory installations separately, with source and observation time. Do not fill unavailable metrics with zero.
- Cached search/directory snapshots are not a live growth baseline. No campaign-attributed growth is claimed.
- A useful trial identifies a task, a model/host, a skill revision, an output, and a concrete observation. Count independent trials, not repeated self-installs.
- Track directory state as proposed, submitted, accepted, declined, or withdrawn; preserve the real link and dates.
- Use voluntary feedback for attribution. Do not add tracking pixels, collect private manuscripts, or infer active users from stars.

## Publication Ledger

No entries yet. For each actual publication record: date, channel/account, public URL, source commit, submission versus acceptance state, and any actionable response. Keep draft URLs out of the ledger.
