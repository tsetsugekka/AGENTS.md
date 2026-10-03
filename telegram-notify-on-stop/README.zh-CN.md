# Telegram Stop 钩子

[AGENTS.zh-CN.md](AGENTS.zh-CN.md) 定义何时通知及当前通知契约。[telegram_notify_on_stop.py](telegram_notify_on_stop.py) 是仍采用空 marker 和通用停止消息的旧版实现，不能满足当前规则的任务隔离、未就绪/就绪记录及脱敏结果摘要契约。不要按当前规则直接启用此脚本；采用当前规则时，需要自行提供匹配实现。停止通知不证明任务已经完成。

## 当前规则要求的执行契约

一次性通知记录必须绑定当前任务，创建时尚未就绪。Agent 在结束前准备包含任务名、实际状态、简短结果或阻塞及用户所需操作的脱敏摘要，再标记就绪。Stop 钩子仅发送就绪记录，成功后消费并保存脱敏回执。此仓库尚未提供匹配实现，因而未定义新版记录路径、字段或安装命令。

## 旧版脚本的现有行为

- 仅在 `CODEX_NOTIFY=1` 且 `~/.codex/notify_on_stop_once` 存在时运行。
- 从环境读取 `TG_BOT_TOKEN` 和 `TG_CHAT_ID`，不得将值写入本仓库或钩子配置。
- 发送通用英文停止消息，不发送聊天、代码或项目正文；此消息不满足当前结果摘要要求。
- Telegram 确认成功后才消费 marker；失败保留 marker。向 `~/.codex/notify_on_stop_receipt.json` 写入权限为 `600` 的脱敏回执。
- 从 stdin 读取事件 JSON，输出机器可读 JSON。需要 Python 3 标准库及 Telegram 网络访问，请求超时为 8 秒。

旧 marker 为用户级而非任务级，并行任务可能消费同一个 marker。脚本不执行自主通知的 15 分钟或每任务一次判定。

## 旧版安装与停用说明

以下是旧版操作说明，不是当前规则的兼容安装方案。旧版目录位置为 `~/.codex/hooks/telegram-notify-on-stop/`，在 `~/.codex/hooks.json` 的 `hooks.Stop` 数组中使用以下条目，保留无关条目；若已有 Telegram 通知器，应替换其条目，避免双重通知：

```json
{"hooks":[{"type":"command","command":"python3 \"${HOME}/.codex/hooks/telegram-notify-on-stop/telegram_notify_on_stop.py\"","timeout":15,"statusMessage":"Sending Telegram stop notification"}]}
```

通过 `/hooks` 审阅并信任，不编辑信任记录。凭据通过获准的本地凭据流程提供。仅在有意启用时设置环境标志。通过 `/hooks` 停用或仅移除此配置条目；没有 marker 时不会发送。

## 验证与限制

用模拟网络请求验证成功、失败和 marker 消费，不实际发送消息。真实送达测试需要已授权的通知，并确认脱敏回执及用户实际收信。注册钩子不等于送达成功。旧版脚本测试不证明当前规则契约已经实现。
