# Novel Writing 开发入口

## 项目定位

本仓库是 `novel-writing` 的独立产品仓，也是唯一可编辑事实源。公开仓库、
安装包和开发工作区在同一个 Git 历史中演进。

## 事实源与边界

- `novel-writing/`：唯一可编辑的 Skill 包。
- `README.md`、`CONTRIBUTING.md`、`.github/`：公开仓库的人类协作层。
- `scripts/`：本地安装、验证和发布辅助工具。
- `%USERPROFILE%\.codex\skills\novel-writing`：运行时入口，应链接到本仓库，不能单独编辑。
- 其他仓库中的同名目录：只允许作为历史记录或派生镜像，不能反向覆盖本仓库。

## 新会话读取顺序

1. 本文件。
2. `README.md` 与 `CONTRIBUTING.md`。
3. `novel-writing/SKILL.md`。
4. 与当前理念或写作问题直接相关的 `novel-writing/references/` 文件。
5. `git status --short --branch` 与最近提交记录。

## 开发循环

1. 在 `novel-writing/` 内修改行为规则、方法和参考资料。
2. 需要公开说明时，同步更新仓库根文档。
3. 执行：

   ```powershell
   powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\check-package.ps1
   git diff --check
   ```

4. 使用本地开发链接在真实小说任务中验证；更新后重新开启 Codex 会话。
5. 记录验证过的具体场景和仍未解决的问题，再提交变更。

禁止把私人小说原文、机器绝对路径、临时会话记录或未验证的泛化结论放入公开 Skill 包。

## 本地开发安装

在仓库根目录执行：

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\install-local-dev-link.ps1
```

脚本会把已有普通目录迁移到带时间戳的备份位置，再建立指向
`novel-writing/` 的目录联接。不要用手工复制来更新本地安装。

## 发布边界

1. 工作区必须干净，包检查与 `git diff --check` 必须通过。
2. 提交并推送 `main`。
3. 以 `vX.Y.Z-public` 形式创建版本标签并推送。
4. 创建对应 GitHub Release；仅推送 tag 不算完成发布。
5. 匿名访问 GitHub `releases/latest` API，确认最新版本确实指向新标签。

没有实际包内容更新时，不为仓库治理或本地链接调整单独制造 Skill 版本。
