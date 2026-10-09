# Telegram Stop 钩子

[AGENTS.zh-CN.md](AGENTS.zh-CN.md) 定义何时通知；本目录提供匹配的[任务隔离脚本](telegram_notify_on_stop.py)。它只发送 Agent 准备的脱敏结果摘要，不读取聊天正文，不接收指令，也不证明任务完成。复制规则不等于安装或启用钩子。

## 安装与启停

需要 Python 3、支持 `fcntl` 的 POSIX 系统（macOS／Linux）及 Telegram 网络访问；此实现不支持 Windows。

1. 将本目录放到 `~/.codex/hooks/telegram-notify-on-stop/`。
2. 将 `allowed-chat-ids.example.json` 复制为同目录的 `allowed-chat-ids.json`，在 `allowed_chat_ids` 数组填入已确认的个人私聊正整数 ID，权限设为 `600`。缺失、空白名单、损坏或目标不匹配均拒绝发送。真实配置已在 `.gitignore` 中排除，不提交 ID 或凭据。
3. 通过获准的本地凭据／环境流程提供 `TG_BOT_TOKEN`、`TG_CHAT_ID` 和 `CODEX_NOTIFY=1`；不要写入钩子配置、命令参数、日志或本仓库。
4. 在 `~/.codex/hooks.json` 的 `hooks.Stop` 数组合并下列条目，保留无关配置；已有 Telegram 通知器时替换其条目，避免双重发送。通过 `/hooks` 审阅并信任，不编辑信任记录。

```json
{"hooks":[{"type":"command","command":"python3 \"${HOME}/.codex/hooks/telegram-notify-on-stop/telegram_notify_on_stop.py\"","timeout":15,"statusMessage":"Sending Telegram stop notification"}]}
```

通过 `/hooks` 停用或仅移除此通知器条目。没有当前任务的就绪记录时不发送；不要用反复测试消息验证安装。

## 任务记录与摘要

- 记录：`~/.codex/notify_on_stop/<session_id>.json`；回执：`~/.codex/notify_on_stop_receipts/<session_id>/<notification_id>.json`。目录权限 `700`，记录与回执权限 `600`。
- `session_id` 来自可信的当前任务上下文，必须对应 Stop 事件的同名字段；可用时取 `CODEX_THREAD_ID`，不可用时不猜测。两个 ID 均仅接受 1–128 位 ASCII 字母、数字、下划线或连字符。
- 每次新申请生成随机 UUID hex 作为 `notification_id`，更新就绪状态及重试时复用该 ID。每个 session 同时只保留一份申请，先完成或取消旧申请。长期对话中的新独立任务可重新申请，但不得换 ID 绕过同一任务的通知次数或不确定送达保护。
- 创建时 `ready:false`；结束前填写实际任务名、状态、结果／具体阻塞及用户待办，再原子更新为 `ready:true`。四个文本字段上限依次为 100、30、600、300 字符，须非空；无待办时明确写“无需操作”。Agent 负责脱敏，不转发完整回复、代码、凭据或私人路径。

```json
{"session_id":"CURRENT_TASK_ID","notification_id":"UUID_HEX","ready":false,"task_title":"更新文档","status":"处理中","summary":"待填写","next_action":"待填写"}
```

原子创建示例；完成时读取本申请、保留两个 ID、更新四个字段及 `ready`，使用相同临时文件替换流程。取消只删除本任务的申请，不删除其他任务记录或回执。

```python
import fcntl
import json
import os
from pathlib import Path
import re
import tempfile
import uuid

session_id = os.environ["CODEX_THREAD_ID"]
if not re.fullmatch(r"[A-Za-z0-9_-]{1,128}", session_id):
    raise ValueError("invalid session_id")
folder = Path.home() / ".codex" / "notify_on_stop"
folder.mkdir(mode=0o700, parents=True, exist_ok=True)
folder.chmod(0o700)
lock_fd = os.open(folder / f"{session_id}.lock", os.O_CREAT | os.O_RDWR | os.O_NOFOLLOW, 0o600)
try:
    fcntl.flock(lock_fd, fcntl.LOCK_EX)
    target = folder / f"{session_id}.json"
    if target.exists():
        raise FileExistsError("pending notification already exists")
    record = {"session_id": session_id, "notification_id": uuid.uuid4().hex,
              "ready": False, "task_title": "更新文档", "status": "处理中",
              "summary": "待填写", "next_action": "待填写"}
    fd, temporary = tempfile.mkstemp(dir=folder, prefix=f".{session_id}.")
    try:
        os.fchmod(fd, 0o600)
        with os.fdopen(fd, "w", encoding="utf-8") as output:
            json.dump(record, output, ensure_ascii=False)
            output.write("\n")
        os.replace(temporary, target)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)
finally:
    os.close(lock_fd)
```

创建、更新、取消记录及人工恢复回执时，均须持有与钩子相同的 `<session_id>.lock` 排他锁，锁内重新核对申请身份后操作；仅有唯一负责人或原子替换不足以防止与 Stop 消费竞态。钩子不判断执行时长、用户交互或摘要真实性；通知条件由 Agent 按规则判断。

## 发送、回执与失败恢复

仅处理 `CODEX_NOTIFY=1`、非钩子续跑的 Stop 事件，以及与该 session 匹配的有效就绪记录。相同 session 用 `<session_id>.lock` 串行发送；锁文件可以留存。请求超时为 8 秒，stdout 固定输出 `{"continue": true}`，不输出凭据。

| 回执状态 | 行为 |
| --- | --- |
| `sending` | 发送前先原子保存；保存失败则不发。进程中断后保留此状态，不自动重发 |
| `delivery_unknown` | 超时、网络异常、5xx、无法确认的响应或发送期间异常；可能已送达，不自动重发 |
| `failed` | 未发送的配置／摘要错误，或明确拒绝（4xx、API `ok:false`）；修正原因后可在后续 Stop 重试，不紧密循环 |
| `delivered_marker_unconsumed` | API 明确 `ok:true`，先保存送达回执，再消费匹配申请；消费失败仍不重发 |
| `delivered` | 送达已确认且申请已消费；同一 ID 不重发 |

回执仅含绑定 ID、时间、状态及脱敏错误类型，不保存消息正文、token 或接收人 ID。无记录、未就绪、任务不匹配或禁用时，不覆盖既有回执。回执表示发送结果，不证明任务完成。

Telegram 没有本脚本可用的幂等键，不能保证严格“恰好一次”。`sending`／`delivery_unknown` 应先核对实际收信：确认已送达时仅取消剩余申请并保留回执；确认未送达、且无并发钩子时，将本申请设为未就绪，将匹配回执原子更新为 `failed`、原因为 `confirmed_not_delivered`，再以原 ID 恢复就绪。不能确认时保留阻止重发状态，不删回执或换 ID 猜测重试。

## 旧版迁移与验证

优先使用上述任务目录。仅在当前 session 无独立记录时兼容旧单槽 `~/.codex/notify_on_stop_once`，它仍必须是 session 匹配、摘要完整且 `ready:true` 的 JSON；旧空 marker 不发送。旧记录可无 `notification_id`，回执仍为 `~/.codex/notify_on_stop_receipt.json`；不要同时写入新旧位置。已有旧 notifier 须替换，不能并存启用。

`CODEX_NOTIFY_ON_STOP_ONCE_FILE`／`CODEX_NOTIFY_ON_STOP_RECEIPT_FILE` 可覆盖旧单槽路径；新任务目录分别位于其父目录下，便于隔离测试，不是任意发送目标配置。

```sh
python3 -B -m unittest discover -s ~/.codex/hooks/telegram-notify-on-stop -p 'test_telegram_notify_on_stop.py'
```

附带测试始终模拟传输，覆盖任务隔离、就绪、并发、白名单、失败与不确定结果、回执持久化及输出脱敏。测试通过或钩子注册不等于实际送达；真实验证仅在用户授权通知时核对回执及实际收信。白名单限制接收功能，不隐藏机器人账号。
