# Novel Writing

[English](README.md) | [简体中文](README.zh-CN.md)

[![GitHub stars](https://img.shields.io/github/stars/wgwtest/novel-writing?style=social)](https://github.com/wgwtest/novel-writing/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![skills.sh](https://skills.sh/b/wgwtest/novel-writing)](https://skills.sh/wgwtest/novel-writing/novel-writing)

让 AI 写小说时，守住人物视角、写清行动因果，并保留作者自己的文风。

Novel Writing 是一个面向 Codex 的小说创作 skill，覆盖构思、起草、续写和审稿。它把“这段有点僵”拆成可以定位、解释和修改的问题：人物从哪里知道这件事？谁有权决定？上一句让对方改变了什么？修改是否抹掉了作者的语气？

## 对白像会议记录，不能只靠加动作

以下是专门编写的讲解片段，不是同模型对照测试。

**原片段**

> “今天能交。”作坊主管说。
>
> “锁扣还会卡。”学徒说。
>
> “那就再试一次。”

**一种修改方式**

> “今天能交。”作坊主管把出货单推到学徒面前。
>
> 她把模型箱压在单子上。“您开一下。”
>
> 锁扣卡在他拇指底下。
>
> 他抽回箱底的单子。“换一个要多久？”

动作有用，是因为它改变了接下来的交涉；不是因为每句话旁边都配了表情。

三个完整示例都有原文、提示词、诊断和修改说明：

- [对白：让动作改变下一步](examples/01-dialogue.md)
- [视角：怀疑不等于已经知道](examples/02-viewpoint.md)
- [文风：保留绕口、重复与未说出口的部分](examples/03-style.md)

## 安装后，先试一小段

已安装 Node.js 和 npm 时，可通过第三方 [skills CLI](https://skills.sh/docs/cli) 安装：

```bash
npx skills add https://github.com/wgwtest/novel-writing --skill novel-writing
```

在安装提示中选择 Codex，检查安装范围。该命令也列在[项目的 skills.sh 页面](https://skills.sh/wgwtest/novel-writing/novel-writing)上；CLI 的依赖和遥测政策以其文档为准。手动安装和 Windows 开发链接方式见[英文安装说明](README.md#install)。

然后试用：

```text
使用 novel-writing。检查下面这段小说的人物视角和对白：
先指出具体位置、问题和原因，再做局部修改。
保留原文的语气、节奏、有意的沉默与不确定性。
不要给每句对白机械添加动作，也不要凭空补出人物的隐藏动机。

【粘贴你有权提供的一小段正文】
```

没有合适片段，可以直接使用[示例原文](examples/README.md)。不同模型和上下文可能产生不同结果，示例不是效果保证。

## 它处理什么

- 构思场景、章节、卷纲或全书梗概，检查事件之间是否有因果连接。
- 起草或续写，避免把关键场面直接压缩成概述。
- 区分人物观察、听说、推测和私下意图，避免作者知道的事自动变成人物共识。
- 检查视角人物、决策者、专业行动者与执行者是否被错误地当成同一个人。
- 调整对白中的行为、停顿和交锋，不强迫每句都有动作或解释。
- 做具体审稿，给出位置、问题、后果及修改方向。
- 修稿时保留对话、心理、旁逸细节、含混和承担节奏的重复。

它不是必须套用的故事公式。设计好的全知叙述、多视角、普通沉默和未解悬念都可以成立；项目自己的文风与设定约束优先。

## 边界、依赖与隐私

当前文档面向 Codex，不将其他宿主标成已验证兼容。核心是 Markdown 指令和参考材料，不是模型、一键完稿程序或小说投稿服务。

可选的稿件文本检查脚本需要 Python 3，仅使用标准库。核心叙事指导不要求额外服务凭据；读取、修改正文仍受宿主的权限与数据处理方式约束。安装本 skill 不等于正文会被完全本地处理，也不构成隐私保证。skill 本身不要求把稿件上传到独立服务。

长篇小说的跨会话恢复、章节状态和多层稿件管理，可搭配 [novel-project-strategy](https://github.com/wgwtest/novel-project-strategy)。

## 反馈与贡献

欢迎提供“哪里确实没改好”的具体反馈：[提交场景反馈](https://github.com/wgwtest/novel-writing/issues/new?template=scene_feedback.md)。附提示词、模型与宿主、skill 版本，以及有问题的位置。无需公开整章；使用你有权公开的短片段或自行编写的复现即可。

如需比较效果，请参考[试用记录方法](examples/README.md#try-it-on-your-own-scene)。Star、安装次数和实际写作质量是不同指标，不用其中一个代替另一个。

贡献说明见 [CONTRIBUTING.md](CONTRIBUTING.md)，许可证为 [MIT](LICENSE)。源码在 `novel-writing/`，公开示例在 `examples/`，示例与推广材料不进入安装包。
