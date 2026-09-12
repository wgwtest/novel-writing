# Public Fiction Examples / 公开小说示例

These original, AI-assisted editorial examples were prepared for this repository. Both the deliberately flawed sources and the suggested revisions are constructed teaching material. They are **not** captured baseline/skill-enabled model runs, independent reviews, user testimonials, or evidence of a measured improvement. No private manuscript is used.

这些例子的原文和修改稿都是为本仓库专门编写的、由 AI 辅助制作的讲解材料，不是真实用户案例，也不是同模型开关 skill 的实测对照。没有使用私人稿件。中英文采用平行改写，并非逐字翻译。

Prepared against skill source commit `65886fd` on 2026-09-12. Later changes may alter the guidance; record an exact commit when reporting a trial.

## Cases

| Case | Question | What to inspect |
| --- | --- | --- |
| [Dialogue / 对白](01-dialogue.md) | Does the action change the exchange? | A blocked delivery becomes a concrete repair decision. |
| [Viewpoint / 视角](02-viewpoint.md) | How could this person know? | Observation stays distinct from suspicion and author truth. |
| [Style / 文风](03-style.md) | What must survive the edit? | Local clarity improves without summarizing away voice. |

The revisions are possible solutions, not canonical answers. Deliberate silence, unresolved motives, omniscient narration, and a different author's rhythm are not defects by default.

## Try It on Your Own Scene

1. Choose a short source passage you own or have permission to use. Provide only the necessary scene context and narrative constraints.
2. Use a case's **Prompt** and **Source** sections as the input. Do not provide the diagnosis or suggested revision if you want an independent attempt.
3. For a paired experiment, use fresh sessions with the same host, model, settings, source, and task. In one session make this skill unavailable; in the other enable it and add `Use novel-writing.` Do not assume that merely omitting its name disables automatic activation.
4. Keep both full outputs and disclose retries or editorial selection. Do not keep only the most flattering run. Confirm activation using the host's available skill-use evidence; if you cannot, label activation unverified.
5. Evaluate access to information, causal continuity, dialogue behavior, style preservation, and unwanted additions separately. Cite the exact lines supporting your assessment. Shorter output or more gestures is not automatically better.

This is a trial protocol, not a benchmark result. A single preference cannot establish a general performance advantage.

## Feedback Without Exposing a Manuscript

Use the [scene feedback template](https://github.com/wgwtest/novel-writing/issues/new?template=scene_feedback.md). An invented, minimal reproduction is welcome. Do not include private project paths, credentials, personal data, or an unpublished manuscript you do not have permission to share.

Useful record / 建议记录：

```text
Host and version / 宿主与版本:
Model and settings / 模型与设置:
Skill commit or release / skill 提交或版本:
Activation evidence / 启用证据:
Task and scene constraints / 任务及场景约束:
Full prompt and public-safe source / 完整提示词与可公开原文:
Output and retries / 输出及重试次数:
Specific failure or useful change / 具体问题或有效修改:
Any editorial changes / 人工或后续编辑:
```

These files are licensed with the repository under [MIT](../LICENSE). They live outside the installable package so examples and campaign material do not become mandatory runtime instructions.
