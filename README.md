# AGENTS.md

![规则组](https://img.shields.io/badge/AGENTS.md-10%20%E8%A7%84%E5%88%99%E7%BB%84-2563eb)
![语言](https://img.shields.io/badge/README-%E4%B8%AD%E6%96%87%20%7C%20%E6%97%A5%E6%9C%AC%E8%AA%9E%20%7C%20English-16a34a)
![维护](https://img.shields.io/badge/%E6%8C%81%E7%BB%AD%E7%BB%B4%E6%8A%A4-verified-7c3aed)

**中文** · [日本語](README.ja.md) · [English](README.en.md)

> 从一份中文全局工作说明中选择公开章节，忠实翻译并排除私人内容，形成十个可独立复用的英文 `AGENTS.md` 规则组；本仓库不是全局说明的完整副本。

## 这是什么

`AGENTS.md` 是放在项目边界内、供 Codex 或其他 coding agent 读取的持久化工作说明。拆分后的每个文件只负责一个稳定主题，既可以单独采用，也可以按需要组合到项目级说明中。

这些规则组明确了：

- 最终回答末尾的实际状态，以及未完成事项或阻塞；
- 如何委派边界清晰且值得并行的子任务，从能可靠完成任务的最低能力模型开始，并由主 Agent 复核成果；
- 临时文件放置、清理和项目根目录治理；
- 长任务期间的临时 Caffeine 保持唤醒，以及对 Computer Use 中断风险的边界说明；
- 长时间任务的 Telegram 通知和“一任务一次”限制；
- GitHub 分支、提交和发布前的检查；
- 本地 Skill 的 API key 持久化与禁止泄露；
- 重复网络抓取的节流、批处理和故障处理；
- 文档类产物的匿名元数据和交付前检查；
- 需要持续维护或跨会话交接，且涉及多模块协作、外部服务或部署、分阶段交付、复杂业务约束中的任一项的开发项目，应维护 README、SPEC、CHANGELOG、TASK、CASE-STUDY 五类 Markdown 文档，并按各自职责记录导航、现行契约、变更历史、任务状态和可复用案例。

## 开发文档与任务连续性

当开发项目需要持续维护或跨会话交接，且涉及多模块协作、外部服务/部署、分阶段交付、复杂业务约束中的任一项时，启用 [`development-documentation-and-task-continuity/AGENTS.md`](development-documentation-and-task-continuity/AGENTS.md)。五类文档职责如下；一次性小改动不必补齐整套文件：

- `README.md`：用途、入口和操作；
- `SPEC.md`：现行行为、契约和验收标准；
- `CHANGELOG.md`：重要变化及发布状态；
- `TASK.md`：当前任务、未完成项、阻塞和下一步；
- `CASE-STUDY.md`：真实错误的证据、原因、修复验证和复用经验；没有实际案例时不虚构。

这些职责可由单个 Markdown 或按模块、主题拆分的索引目录承载。案例较多时使用 `case-study/`（或已有等价目录），每个案例一个 Markdown，并由目录内 README 或既有索引导航。

优先复用现有文档、命名与目录。开工读取相关文档，变更时只更新受影响内容；结束、暂停或交接前，将未完成事项写回任务入口。同一事实或状态只维护一个权威来源，其他位置链接引用；区分现行规格、未实现方案、历史记录，以及实现、验证、发布和运行验收。文档同步不扩大操作权限，也不得把凭据或内部记录混入公开产物。

## 十个规则组

| 文件 | 主要关注点 | 适合单独复用的场景 |
|---|---|---|
| [`final-response-status/AGENTS.md`](final-response-status/AGENTS.md) | 明确最终回答的实际状态，有未完成或阻塞时简要说明 | 需要明确标注完成状态的任务 |
| [`development-documentation-and-task-continuity/AGENTS.md`](development-documentation-and-task-continuity/AGENTS.md) | 开发文档连续性，以及 README、SPEC、CHANGELOG、TASK、CASE-STUDY 五类文档的职责 | 需要持续维护或跨会话交接，且涉及多模块协作、外部服务/部署、分阶段交付、复杂业务约束的开发项目 |
| [`multi-agent-delegation-and-model-routing/AGENTS.md`](multi-agent-delegation-and-model-routing/AGENTS.md) | 多 Agent 委派、Luna/Sol/Terra/Astra 模型路由和主 Agent 复核 | 有独立子任务或不同复杂度任务的工作流 |
| [`temporary-files-and-project-structure-hygiene/AGENTS.md`](temporary-files-and-project-structure-hygiene/AGENTS.md) | 临时目录、任务结束清理和根目录结构 | 需要保持项目树整洁的任何项目 |
| [`temporary-caffeine-mode-for-long-running-tasks/AGENTS.md`](temporary-caffeine-mode-for-long-running-tasks/AGENTS.md) | 长任务临时保持唤醒、Computer Use 中断风险和安全边界 | 需要连续运行或保持前台交互的长任务 |
| [`telegram-notify-on-stop/AGENTS.md`](telegram-notify-on-stop/AGENTS.md) | 长任务停止通知、用户交互判断、一次性 marker 和凭据 | 希望在用户离开期间获得重要结果提醒的工作流 |
| [`github-publish-discipline/AGENTS.md`](github-publish-discipline/AGENTS.md) | 分支纪律、范围隔离、暂存状态保护和发布检查 | 需要稳定 GitHub 发布流程的仓库 |
| [`api-key-persistence-for-local-skills/AGENTS.md`](api-key-persistence-for-local-skills/AGENTS.md) | 本地 Skill 的 key 存储、服务特例和输出脱敏 | 使用外部 API 的本地 Skill 集合 |
| [`network-scraping-discipline/AGENTS.md`](network-scraping-discipline/AGENTS.md) | 抓取节流、聚合端点和限流故障处理 | 需要重复访问网络数据源的任务 |
| [`anonymous-document-artifact-metadata/AGENTS.md`](anonymous-document-artifact-metadata/AGENTS.md) | Office/PDF 等产物的匿名作者字段和路径隐私 | 生成或转换文档、表格、演示文稿和 PDF |

## 组合方式

十份文件是主题化规则组，而不是互相排斥的配置。通常可以这样组合：

1. 先加入 `temporary-files-and-project-structure-hygiene`，建立所有任务的文件生命周期底线。
2. 长任务或 Computer Use 需要连续运行时，加入 `temporary-caffeine-mode-for-long-running-tasks`。
3. 需要并行处理时加入 `multi-agent-delegation-and-model-routing`。
4. 有 GitHub 变更时加入 `github-publish-discipline`。
5. 使用外部 API 或抓取数据时加入 API key 与网络抓取规则。
6. 生成 Office、PDF 或其他带元数据的文件时加入匿名元数据规则。
7. 只有在确实需要长任务提醒时才加入 Telegram 通知规则。
8. 开发项目需要持续维护或跨会话交接，且涉及多模块协作、外部服务/部署、分阶段交付、复杂业务约束时，加入开发文档与任务连续性规则；按五类文档的职责分别维护导航、现行规格、变更历史、任务状态和可复用案例。

## 使用注意

- 英文规则忠实表达所选公开章节，排除私人内容；三语 README 介绍同一套十个规则组。
- 复制到其他项目时，请检查其中的路径、工具、凭据存储位置和平台假设是否适用。
- Caffeine 规则只能降低闲置睡眠、显示器休眠或部分屏保行为造成的中断风险，不能保证阻止手动锁屏、受管制的锁屏策略、会话切换或注销；不得借此修改密码或其他系统安全设置。
- API key、token、Cookie、个人资料、生产数据和真实私密配置不应进入公开仓库。
- 若项目已有更严格的本地规则，应以项目的权威说明和用户当前请求为准。

## 维护

- 每个目录只放对应的 `AGENTS.md`，目录名与规则组标题保持一致。
- 中文底稿是唯一规则来源。规则有变化时，先更新底稿，再忠实翻译受影响的公开部分并同步三语 README；不在英文中自行补充或改变规则。
- 推送前检查 Markdown、绝对路径、私密值和意外生成文件。
- 保持每次提交聚焦，清楚区分规则、README 和仓库元数据变更。

## Topics

`AGENTS.md` · `codex` · `ai-agents` · `agent-instructions` · `multi-agent` · `prompt-engineering` · `workflow-automation`

## License

仓库默认不附带许可证。只有在维护者确定复用条款后，才应添加明确的许可证文件。
