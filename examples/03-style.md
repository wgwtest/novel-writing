# Style: Fix the Staging, Keep the Voice

[All examples / 示例目录](README.md)

Original, AI-assisted editorial demonstration—not a measured model comparison. Context: a first-person narrator is giving an old umbrella back to a former neighbor. Preserve the slightly defensive rhythm, the repeated denial, the ribbon, and the unresolved offer to come upstairs. The local problem is how both characters handle the umbrella at once.

## Prompt

```text
Use novel-writing. Review and minimally revise the source below.
Preserve the first-person narrator's defensive rhythm, repeated denial,
the ribbon detail, and the unanswered invitation. Do not summarize the
relationship or explain what the narrator really feels. Repair only the
unclear umbrella handoff. Give a concrete finding before the revision.
```

## Source

```text
I had not kept his umbrella. Not kept it. It had stood behind the door
for three winters, which was different. The ribbon was still on the handle,
the ridiculous yellow ribbon he said would stop him losing it.

"You found it," he said.

"It wasn't lost."

I opened it between us while his hand was on the handle, then gave it back.

"Tea?" I said. "Since you're here."
```

## Diagnosis

- **Location:** "I opened it ... then gave it back." **Type:** spatial/action clarity. The ownership of the handle and the order of handoff are muddy. **Revision:** give one person the handle, let the other release it, then open the umbrella. **Project rule?** No; this is a local staging repair. The surrounding repetition and offer already carry voice and do not need compression.

## One Possible Revision

```text
I had not kept his umbrella. Not kept it. It had stood behind the door
for three winters, which was different. The ribbon was still on the handle,
the ridiculous yellow ribbon he said would stop him losing it.

"You found it," he said.

"It wasn't lost."

I put the handle into his hand and let go. He stepped back to open it.

"Tea?" I said. "Since you're here."
```

Only the handling sentence changes. "I returned his umbrella and invited him in" would preserve the events but lose the denial, elapsed time, object memory, and defensive offer. The example does not decide whether he accepts or name the feeling the narrator avoids naming.

## 中文平行示例

场景约束：第一人称叙述者把旧伞还给从前的邻居。保留嘴硬、重复、黄绳和没被回答的邀请，只解决递伞动作不清的问题。

**提示词**

```text
使用 novel-writing。先指出具体问题，再最小限度修改下面片段。
保留第一人称嘴硬的语气、“没留着”的重复、黄绳细节和未被回答的邀请。
不要概括人物关系，也不要点明叙述者真正的感情。只修递伞动作。
```

**原文**

> 我没留着他的伞。真没留着。它在门后站了三个冬天，是另一回事。柄上还系着那根黄绳，丑得要命的黄绳，他说这样就丢不了。
>
> “找着了？”他说。“又没丢。”
>
> 他握着伞柄，我在我们中间把伞撑开，再递还给他。
>
> “喝茶吗？”我说，“来都来了。”

**一种修改**

> 我没留着他的伞。真没留着。它在门后站了三个冬天，是另一回事。柄上还系着那根黄绳，丑得要命的黄绳，他说这样就丢不了。
>
> “找着了？”他说。“又没丢。”
>
> 我把伞柄放进他手里，松了手。他退开一步，撑起伞。
>
> “喝茶吗？”我说，“来都来了。”

修改只动递伞的一句，不把原文压成“我把保留多年的伞还给他，并请他喝茶”。后者讲清了事件，却替人物说破了原本不肯承认的东西。

## Skill References

- [Style fidelity](../novel-writing/references/style-fidelity.md)
- [Scene causality and agency](../novel-writing/references/scene-causality-and-agency.md)
