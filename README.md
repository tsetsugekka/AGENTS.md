# AGENTS.md

![规则组](https://img.shields.io/badge/AGENTS.md-8%20%E8%A7%84%E5%88%99%E7%BB%84-2563eb)
![语言](https://img.shields.io/badge/README-%E4%B8%AD%E6%96%87%20%7C%20%E6%97%A5%E6%9C%AC%E8%AA%9E%20%7C%20English-16a34a)
![维护](https://img.shields.io/badge/%E6%8C%81%E7%BB%AD%E7%BB%B4%E6%8A%A4-verified-7c3aed)

**中文** · [日本語](README.ja.md) · [English](README.en.md)

> 将一份全局工作说明拆成八个可独立复用的 `AGENTS.md` 规则组，覆盖多 Agent 协作、模型路由、临时文件、Caffeine 保持唤醒、Telegram 通知、GitHub 发布、API key、网络抓取和文档隐私元数据。

## 这是什么

`AGENTS.md` 是放在项目边界内、供 Codex 或其他 coding agent 读取的持久化工作说明。拆分后的每个文件只负责一个稳定主题，既可以单独采用，也可以按需要组合到项目级说明中。

这些规则组明确了：

- 如何根据任务难度选择多 Agent 和模型；
- 临时文件放置、清理和项目根目录治理；
- 长任务期间的临时 Caffeine 保持唤醒，以及对 Computer Use 中断风险的边界说明；
- 长时间任务的 Telegram 通知和“一任务一次”限制；
- GitHub 分支、提交和发布前的检查；
- 本地 Skill 的 API key 持久化与禁止泄露；
- 重复网络抓取的节流、批处理和故障处理；
- 文档类产物的匿名元数据和交付前检查。

## 八个规则组

| 文件 | 主要关注点 | 适合单独复用的场景 |
|---|---|---|
| [`multi-agent-delegation-and-model-routing/AGENTS.md`](multi-agent-delegation-and-model-routing/AGENTS.md) | 多 Agent 委派、Luna/Sol/Terra/Astra 模型路由和主 Agent 复核 | 有独立子任务或不同复杂度任务的工作流 |
| [`temporary-files-and-project-structure-hygiene/AGENTS.md`](temporary-files-and-project-structure-hygiene/AGENTS.md) | 临时目录、任务结束清理和根目录结构 | 需要保持项目树整洁的任何项目 |
| [`temporary-caffeine-mode-for-long-running-tasks/AGENTS.md`](temporary-caffeine-mode-for-long-running-tasks/AGENTS.md) | 长任务临时保持唤醒、Computer Use 中断风险和安全边界 | 需要连续运行或保持前台交互的长任务 |
| [`telegram-notify-on-stop/AGENTS.md`](telegram-notify-on-stop/AGENTS.md) | 长任务停止通知、用户交互判断、一次性 marker 和凭据 | 希望在用户离开期间获得重要结果提醒的工作流 |
| [`github-publish-discipline/AGENTS.md`](github-publish-discipline/AGENTS.md) | 目标分支、发布授权和提交前检查 | 需要稳定 GitHub 发布流程的仓库 |
| [`api-key-persistence-for-local-skills/AGENTS.md`](api-key-persistence-for-local-skills/AGENTS.md) | 本地 Skill 的 key 存储、MX 特例和输出脱敏 | 使用外部 API 的本地 Skill 集合 |
| [`network-scraping-discipline/AGENTS.md`](network-scraping-discipline/AGENTS.md) | 抓取节流、聚合端点和限流故障处理 | 需要重复访问网络数据源的任务 |
| [`anonymous-document-artifact-metadata/AGENTS.md`](anonymous-document-artifact-metadata/AGENTS.md) | Office/PDF 等产物的匿名作者字段和路径隐私 | 生成或转换文档、表格、演示文稿和 PDF |

## 组合方式

八份文件是主题化规则组，而不是互相排斥的配置。通常可以这样组合：

1. 先加入 `temporary-files-and-project-structure-hygiene`，建立所有任务的文件生命周期底线。
2. 长任务或 Computer Use 需要连续运行时，加入 `temporary-caffeine-mode-for-long-running-tasks`。
3. 需要并行处理时加入 `multi-agent-delegation-and-model-routing`。
4. 有 GitHub 变更时加入 `github-publish-discipline`。
5. 使用外部 API 或抓取数据时加入 API key 与网络抓取规则。
6. 生成 Office、PDF 或其他带元数据的文件时加入匿名元数据规则。
7. 只有在确实需要长任务提醒时才加入 Telegram 通知规则。

## 使用注意

- 这些文件来自同一份全局说明的八个一级规则组，文件内容保持对应规则组的完整语义。
- 复制到其他项目时，请检查其中的路径、工具、凭据存储位置和平台假设是否适用。
- Caffeine 规则只能降低闲置睡眠、显示器休眠或部分屏保行为造成的中断风险，不能保证阻止手动锁屏、受管制的锁屏策略、会话切换或注销；不得借此修改密码或其他系统安全设置。
- API key、token、Cookie、个人资料、生产数据和真实私密配置不应进入公开仓库。
- 若项目已有更严格的本地规则，应以项目的权威说明和用户当前请求为准。

## 维护

- 每个目录只放对应的 `AGENTS.md`，目录名与规则组标题保持一致。
- 规则有变化时，只修改相关规则组，并同步更新三个语言版 README 的索引和说明。
- 推送前检查 Markdown、绝对路径、私密值和意外生成文件。
- 保持每次提交聚焦，清楚区分规则、README 和仓库元数据变更。

## Topics

`AGENTS.md` · `codex` · `ai-agents` · `agent-instructions` · `multi-agent` · `prompt-engineering` · `workflow-automation`

## License

仓库默认不附带许可证。只有在维护者确定复用条款后，才应添加明确的许可证文件。
