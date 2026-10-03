# AGENTS.md · 按需选用的 Agent 工作规则

**中文** · [日本語](README.ja.md) · [English](README.en.md)

让 Agent 清楚知道：什么时候行动、该读什么、哪些边界不能越过，以及怎样交付可信的结果。

这里收集 **11 个独立主题**，每个都有中文原稿与英文译文。它是一份可按需取用的规则目录，**不是要求整仓安装的配置包**。

## 从这里开始

1. 从下表选择真正需要的主题，不必全选。
2. 选一种语言，阅读适用范围、依赖和限制。
3. 将常用规则合并到自己的持久指令文件；低频主题可改为按需读取。保留原有项目约束，不覆盖整个文件。
4. 检查路径及配套文档。复制规则不会安装 Skill、钩子或其他工具，也不会自动获得操作权限。

## 规则目录

| 主题 | 解决什么问题 | 规则正文 |
| --- | --- | --- |
| 回答状态 | 明确完成、未完成和阻塞 | [中文](final-response-status/AGENTS.zh-CN.md) · [English](final-response-status/AGENTS.md) |
| 多 Agent 与模型路由 | 独立子任务、八种常用模型组合、合理等待与复核 | [中文](multi-agent-delegation-and-model-routing/AGENTS.zh-CN.md) · [English](multi-agent-delegation-and-model-routing/AGENTS.md) |
| 开发文档与交接 | README / SPEC / CHANGELOG / TASK / CASE-STUDY 的职责与按需指令 | [中文](development-documentation-and-task-continuity/AGENTS.zh-CN.md) · [English](development-documentation-and-task-continuity/AGENTS.md) |
| 前端设计 | 设计 Skill 分工、紧凑布局与手机 App 式流程 | [中文](frontend-design/AGENTS.zh-CN.md) · [English](frontend-design/AGENTS.md) |
| 临时文件与目录 | 临时产物清理、既有文件保护、根目录稳定 | [中文](temporary-files-and-project-structure-hygiene/AGENTS.zh-CN.md) · [English](temporary-files-and-project-structure-hygiene/AGENTS.md) |
| 长任务保持唤醒 | 临时 Caffeine 的启停与安全限制 | [中文](temporary-caffeine-mode-for-long-running-tasks/AGENTS.zh-CN.md) · [English](temporary-caffeine-mode-for-long-running-tasks/AGENTS.md) |
| Telegram 通知 | 有价值的结束通知、触发条件与每任务一次限制 | [中文](telegram-notify-on-stop/AGENTS.zh-CN.md) · [English](telegram-notify-on-stop/AGENTS.md) |
| GitHub 发布纪律 | 分支、范围隔离及保护其他改动；不授予自动发布权限 | [中文](github-publish-discipline/AGENTS.zh-CN.md) · [English](github-publish-discipline/AGENTS.md) |
| 凭据处理 | 本地 Skill 的安全输入、持久化与禁止泄露 | [中文](api-key-persistence-for-local-skills/AGENTS.zh-CN.md) · [English](api-key-persistence-for-local-skills/AGENTS.md) |
| 网络抓取 | 节流、批量读取和限流处理；区分内部运维 | [中文](network-scraping-discipline/AGENTS.zh-CN.md) · [English](network-scraping-discipline/AGENTS.md) |
| 文档元数据匿名化 | 清理身份字段与本地路径，复检实际交付文件 | [中文](anonymous-document-artifact-metadata/AGENTS.zh-CN.md) · [English](anonymous-document-artifact-metadata/AGENTS.md) |

## 两种接入方式

**直接合并**适合经常适用的规则。把所选正文整合进自己的 `AGENTS.md`、`CLAUDE.md` 或其他实际使用的指令文件；先检查其中的模型、工具和平台假设，不把改文件名当作兼容性保证。

**按需读取**适合较长、低频的主题。将完整正文保存为普通 Markdown，在根指令保留明确的触发条件、路径和必要安全边界。例如，将设计主题正文保存到 `docs/FRONTEND-DESIGN.md` 后加入：

```markdown
仅在界面设计、改版或涉及界面的前端开发时，
先读取 docs/FRONTEND-DESIGN.md；其他任务不读取。
```

路径相对于自己的指令文件调整。链接本身不保证自动读取；配套文档也要携带。不要让同一规则既常驻全文又按需重复加载，也不要把按需文档命名为当前运行环境会自动加载的根指令文件。

公开主题保留完整正文，使用者无需复制作者的本地目录结构。新增内容时，通用约束和安全边界留在入口，较长的任务专属细则按需读取；短规则和用户指定常驻的内容不必拆分。

## 选用前须知

- **来源**：中文取自本地中文底稿及其明确引用的细则，排除私人内容；英文忠实翻译，不反向生成中文，不添加另一套规则。
- **设计**：`finesse-ui`、Taste 的 `redesign-existing-projects` 和 `impeccable` 需在使用环境中可用。本仓库不捆绑这些 Skill，也不启用设计钩子。
- **模型路由**：是用途和成本偏好，不是通用性能排名；实际模型与思考档位须由运行环境支持。
- **保持唤醒**：不能保证阻止手动或受管锁屏，不得绕过密码和安全策略。
- **发布与凭据**：规则不包含作者的自动提交、推送和部署授权；个人凭据、账号配置和私人路径不公开。
- **适用边界**：采用前处理与现有项目规则的冲突，不因复制本文扩大权限；只选一种语言，避免中英文重复加载。

## 可选钩子：规则与实现分开看

| 配套内容 | 当前状态 |
| --- | --- |
| [回答末尾状态检查](final-response-status/README.zh-CN.md) | 检查状态标签格式，不判断任务是否真的完成，也不自动续跑 |
| [Telegram 通知](telegram-notify-on-stop/README.zh-CN.md) | 附带脚本是旧版，尚不满足当前规则的任务隔离和结果摘要契约；不要按新版规则直接启用 |

安装、信任及验证按对应 README 执行；脚本测试通过不代表实际触发或消息送达。

## 维护与复用

每个主题维护 `AGENTS.zh-CN.md` 与 `AGENTS.md`，三语 README 只提供选用说明。规则变化先改中文权威来源，再同步公开正文和译文；同一事实不建立多份互相竞争的来源。

本仓库尚未附带许可证，不代表已授予开源许可；对外再分发前请确认复用条款。
