# AGENTS.md · 主文件规则与按需专题

**中文** · [日本語](README.ja.md) · [English](README.en.md)

这里提供 **12 个独立主题**。目录中的 `AGENTS.zh-CN.md` 和 `AGENTS.md` 都是**完整主题正文**，分别为中文和英文；文件名不表示它们都应完整写进主 AGENTS。

让 Agent “按这个仓库安装规则”时，按下面两部分接入。未指定主题时采用这个默认方案；明确只选部分主题时，只接入选中的主题。**规则接入不安装 Skill、启用钩子或增加操作权限。**

## 一、正文直接放进主 AGENTS.md

以下 **9 个主题**的完整规则，合并到实际使用的主 `AGENTS.md`。它们是通用约束、短条件规则或需要常驻的委派约定；“常驻”不表示每个任务都要执行相关动作。

| 主题 | 主 AGENTS.md 放什么 | 完整正文 |
| --- | --- | --- |
| 回答结束状态 | 完整规则：如实标记完成、未完成和阻塞 | [中文](final-response-status/AGENTS.zh-CN.md) · [English](final-response-status/AGENTS.md) |
| 多 Agent 与模型路由 | 完整规则：委派边界、模型选择、等待和复核 | [中文](multi-agent-delegation-and-model-routing/AGENTS.zh-CN.md) · [English](multi-agent-delegation-and-model-routing/AGENTS.md) |
| 开发文档与交接 | 完整规则：文档职责、唯一来源和任务连续性；实际项目文档按任务读 | [中文](development-documentation-and-task-continuity/AGENTS.zh-CN.md) · [English](development-documentation-and-task-continuity/AGENTS.md) |
| 临时文件与目录 | 完整规则：临时产物位置、清理与既有文件保护 | [中文](temporary-files-and-project-structure-hygiene/AGENTS.zh-CN.md) · [English](temporary-files-and-project-structure-hygiene/AGENTS.md) |
| 浏览器标签页 | 完整规则：任务页面复用、清理和用户标签页保护 | [中文](browser-tab-hygiene/AGENTS.zh-CN.md) · [English](browser-tab-hygiene/AGENTS.md) |
| 长任务保持唤醒 | 完整规则：仅在适用时临时启用，结束时关闭，不绕过安全限制 | [中文](temporary-caffeine-mode-for-long-running-tasks/AGENTS.zh-CN.md) · [English](temporary-caffeine-mode-for-long-running-tasks/AGENTS.md) |
| Telegram 通知 | 完整触发与安全规则；钩子的执行说明按需读，不默认启用通知 | [中文](telegram-notify-on-stop/AGENTS.zh-CN.md) · [English](telegram-notify-on-stop/AGENTS.md) |
| GitHub 发布纪律 | 完整规则：分支、改动范围和其他工作保护；不授予自动发布权限 | [中文](github-publish-discipline/AGENTS.zh-CN.md) · [English](github-publish-discipline/AGENTS.md) |
| 网络抓取 | 完整规则：外部抓取的节流、限流处理和内部运维边界 | [中文](network-scraping-discipline/AGENTS.zh-CN.md) · [English](network-scraping-discipline/AGENTS.md) |

选一种语言，将所选正文合并到已有主文件，不覆盖整个文件。检查其中模型、工具和平台的支持情况；不把改文件名当成兼容性保证。已有同义规则去重，实际冲突保留并报告，不悄悄覆盖项目约束。

正文中的相对配套链接须调整到实际可读的位置；下方钩子说明可使用对应仓库文档的完整 URL。不能把 `README.md` 原样留成指向用户主文件旁另一份无关 README 的链接。

## 二、主 AGENTS.md 只放触发入口，正文另存后按需读

以下 **3 个主题**的完整正文不合并到主文件。将它们保存为主 `AGENTS.md` 同目录的普通 Markdown，主文件只加入下方对应入口；凭据和元数据入口同时保留必要的安全边界。

| 主题 | 另存的完整正文 | 主文件旁的保存名称 | 何时读 |
| --- | --- | --- | --- |
| 前端设计、性能与页面 SEO | [中文](frontend-design/AGENTS.zh-CN.md) · [English](frontend-design/AGENTS.md) | `FRONTEND-DESIGN.md` | 界面设计、改版、涉及界面的前端开发、网页性能、SEO／分享预览；只读相关章节 |
| 凭据操作 | [中文](api-key-persistence-for-local-skills/AGENTS.zh-CN.md) · [English](api-key-persistence-for-local-skills/AGENTS.md) | `CREDENTIALS.md` | 接收、保存或使用密码、key、token 等凭据之前 |
| 文档元数据 | [中文](anonymous-document-artifact-metadata/AGENTS.zh-CN.md) · [English](anonymous-document-artifact-metadata/AGENTS.md) | `DOCUMENT-METADATA.md` | 创建、编辑、转换、渲染或导出相关文档产物之前 |

### 主文件入口：前端设计、性能与 SEO

将所选语言的前端正文另存为 `FRONTEND-DESIGN.md`，在主 `AGENTS.md` 中加入：

```markdown
## 前端设计按需入口
- 仅在界面设计、改版、涉及界面的前端开发、网页加载与性能优化或 SEO／分享预览任务时，
  按相关章节读取 [前端设计规则](FRONTEND-DESIGN.md)；其他任务不读取。
```

三个设计 Skill 的分工、compact、手机流程、图表与交互检查，以及加载性能、SEO 正文交付、元信息和分享预览要求，都在专题正文里，**不要再把这些细则复制到主文件**。

### 主文件入口：凭据操作

将所选语言的凭据正文另存为 `CREDENTIALS.md`，在主文件中加入：

```markdown
## 凭据操作按需入口
- 接收、保存或使用密码、key、token 等凭据前，先读取 [凭据操作规则](CREDENTIALS.md)；
  项目或服务有更严格规范时从其规定。
- 不要求用户把凭据发到聊天或普通 shell 提示符；明文不得进入命令参数、
  历史、日志、工具输出、回复或 Skill 文件。
```

### 主文件入口：文档元数据

将所选语言的元数据正文另存为 `DOCUMENT-METADATA.md`，在主文件中加入：

```markdown
## 文档元数据按需入口
- 创建、编辑、转换、渲染或导出 Office、PDF、OpenDocument、
  带元数据图像等文档产物前，先读取 [文档元数据规则](DOCUMENT-METADATA.md)。
- 除非用户在当前任务明确要求该确切值，不嵌入或暴露身份信息和本地路径；
  交付前清理继承的个人元数据及本地路径，并检查实际产物、复检清理结果。
```

这里的入口是复制到主文件的文字；表格链接才是需要另存的完整正文。路径相对于主 `AGENTS.md`。如果改存到 `docs/` 或其他目录，同时修改入口路径。**只复制入口而没有保存专题正文，接入不完整。** 不要让同一主题既常驻全文又按需重复加载，也不要把专题文档命名为运行环境会自动加载的主指令文件。

## 给新电脑上的 Agent 的安装步骤

1. 确认运行环境实际读取的主指令路径。Codex 默认使用 `~/.codex/AGENTS.md`；若配置了其他 Codex 主目录，则以实际配置为准。其他 Agent 核实其持久指令入口，不猜路径、不凭改名宣称兼容。
2. 读取并保护已有主文件及相邻文档。选一种语言，按上面两部分合并常驻正文、保存三份专题正文并写入对应入口；只处理选中的主题。没有既有文件时创建所需文件，不添加个人凭据或作者的私人配置。
3. 校验入口相对路径都能打开，配套链接可读，专题正文未重复内联到主文件。用户指定常驻或其他接入方式时服从用户要求；有实际不兼容冲突时说明具体位置。
4. 分别说明规则接入、Skill 可用性和钩子状态。读取规则不等于安装工具；前端的三个设计 Skill 按专题所列来源另行准备；SEO、分享预览与性能规则直接按专题执行，不要求安装对应 Skill。钩子按下节处理。
5. 报告实际主文件路径、合并的主题、三份专题文件路径、触发入口验证结果，以及未完成的依赖。文件存在和链接通过，只代表规则接入完成，不代表未来任务已正确执行。

例如采用 Codex 默认目录及全部主题后：

```text
~/.codex/
├── AGENTS.md             # 第一部分的正文 + 第二部分的三个短入口
├── FRONTEND-DESIGN.md    # 前端设计、手机经验、加载性能、页面 SEO；按相关章节读
├── CREDENTIALS.md        # 凭据操作细则；涉及凭据前读
└── DOCUMENT-METADATA.md  # 文档元数据细则；相关产物操作前读
```

复制项目级规则时，相同结构也可放在项目指令旁；不会替用户将全局与项目两层重复安装。

## 依赖与可选钩子

- **来源**：中文取自本地中文底稿及其明确引用的细则，排除私人内容；英文忠实翻译。完整主题正文与入口不维护另一套相互竞争的规则。
- **前端设计**：[finesse-ui](https://github.com/mouse-lin/finesse-skill)、[redesign-existing-projects](https://github.com/Leonxlnx/taste-skill)、[impeccable](https://github.com/pbakaus/impeccable) 的设计方法由各 Skill 维护。本仓库不捆绑 Skill、不启用设计钩子；按任务阶段只读取所需内容。SEO、分享预览与加载性能的触发条件、规则和验收要求已写入前端专题，可独立执行，不要求安装另一个 Skill。
- **模型与平台**：模型路由是用途和成本偏好，实际模型、思考档位与工具须由运行环境支持。复制规则不扩大权限，不带作者的自动提交、推送、部署授权。
- **保持唤醒**：不能保证阻止手动或受管锁屏，不得绕过密码和安全策略。

| 配套内容 | 当前状态 |
| --- | --- |
| [回答末尾状态检查](final-response-status/README.zh-CN.md) | 检查状态标签格式，不判断任务是否真的完成，也不自动续跑 |
| [Telegram 通知](telegram-notify-on-stop/README.zh-CN.md) | 附带脚本是旧版，尚不满足当前规则的任务隔离和结果摘要契约；不要按新版规则直接启用 |

安装、信任及验证按对应 README 执行；脚本测试通过不代表实际触发或消息送达。

## 维护与复用

保留各主题的独立目录及完整中英文正文。规则先更新中文权威来源，再同步公开正文、译文和本 README 的接入说明；同一事实只维护一个权威来源。

本仓库尚未附带许可证，不代表已授予开源许可；对外再分发前请确认复用条款。
