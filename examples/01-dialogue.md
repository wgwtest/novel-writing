# Dialogue: An Action That Changes the Next Question

[All examples / 示例目录](README.md)

Original, AI-assisted editorial demonstration—not a measured before/after model run. Context: a small workshop is preparing a model case for delivery. The manager wants it shipped today; his apprentice wants the faulty latch fixed. Keep the apprentice's viewpoint and leave the final delivery outcome unresolved.

## Prompt

```text
Use novel-writing. Review and locally revise the source scene below.
The workshop manager wants today's delivery; the apprentice wants the faulty
latch fixed. Stay with the apprentice's viewpoint. Make the disagreement
affect what they do next, without assigning a gesture to every line.
Do not turn the manager into a villain or resolve the entire delivery.
Give concrete findings before the revision.
```

## Source

```text
The delivery slip lay between the apprentice and the workshop manager.
"We can send it today," he said, nodding.
"The latch still sticks," she said, frowning.
"Then test it again," he said.
"I already did," she said, looking at the case.
"The customer is waiting."
"I know."
The apprentice opened her notebook. They discussed the problem for a while
and decided that it needed fixing.
```

## Diagnosis

- **Location:** the nod and frown. **Type:** dialogue embodiment. They signal mood but do not affect access, tactics, or the next reply. **Revision:** replace only a consequential beat with a scene-specific test; do not add more gestures. **Project rule?** No global gesture ban; inspect function locally.
- **Location:** the final sentence. **Type:** scene causality. The prose summarizes the decision without showing what made the manager reconsider. **Revision:** let the known defect obstruct the requested handoff. **Project rule?** Only if this kind of skipped decision recurs.

## One Possible Revision

```text
"We can send it today." The workshop manager slid the delivery slip toward
his apprentice.

She set the model case on top of it. "Open it."

The latch caught under his thumb.

"It does open," he said.
"After that."
"The customer is waiting."
"I know."

He drew the slip out from under the case. "How long to replace it?"

She put the new latch beside the old one. "If we start now, I can tell you
after the first fitting."
```

The failed opening turns an abstract complaint into an obstacle the manager encounters. Withdrawing the slip changes the immediate task. The apprentice does not promise a completion time she has not tested, and the clean exchange keeps several lines without action tags. The characters have a next step, not a magically completed repair.

## 中文平行示例

同样的场景约束：小作坊即将交付模型箱；主管催交货，学徒要求先修好锁扣。采用学徒视角，不在这段里解决整次交货。

**提示词**

```text
使用 novel-writing。先指出下面片段的具体问题，再做局部改写。
主管想今天交货，学徒想先修好锁扣。保留学徒视角。
让分歧影响下一步行动，不要给每句对白都配动作。
不要把主管写成反派，也不要直接写完修理和交货。
```

**原文**

> 出货单摆在学徒和作坊主管之间。“今天能交。”主管点点头。
>
> “锁扣还会卡。”她皱眉。
>
> “那就再试一次。”“已经试过了。”她看了看箱子。
>
> “客户还等着。”“我知道。”
>
> 学徒翻开记录本。他们讨论了一会儿，决定先把锁扣修好。

**一种修改**

> “今天能交。”作坊主管把出货单推到学徒面前。
>
> 她把模型箱压在单子上。“您开一下。”
>
> 锁扣卡在他拇指底下。
>
> “也不是打不开。”“得先卡这一下。”“客户还等着。”“我知道。”
>
> 他抽回箱底的单子。“换一个要多久？”
>
> 她把新锁扣放在旧的旁边。“现在开始，装上试一次，我才敢说。”

问题不在于“点头”“皱眉”这些词不能用，而在于原文略过了决定如何发生。修改让试开失败改变交涉，同时保留催促、克制和时间不确定性。

## Skill References

- [Dialogue and behavior](../novel-writing/references/dialogue-and-behavior.md)
- [Scene causality and agency](../novel-writing/references/scene-causality-and-agency.md)
