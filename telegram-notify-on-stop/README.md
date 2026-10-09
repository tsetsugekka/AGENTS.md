# Telegram Stop hook

[AGENTS.md](AGENTS.md) defines when to notify; this directory supplies a matching [task-isolated script](telegram_notify_on_stop.py). It sends only an agent-prepared, redacted result summary, never reads the transcript, accepts no commands, and does not prove task completion. Copying the rules does not install or enable the hook. [中文说明](README.zh-CN.md).

## Installation and enabling/disabling

Requires Python 3, a POSIX system supporting `fcntl` (macOS/Linux), and Telegram network access. This implementation does not support Windows.

1. Place this directory at `~/.codex/hooks/telegram-notify-on-stop/`.
2. Copy `allowed-chat-ids.example.json` to `allowed-chat-ids.json` beside the script. Populate `allowed_chat_ids` with verified positive integer personal-chat IDs and set permissions to `600`. Missing, empty, malformed or nonmatching allowlists deny sending. `.gitignore` excludes the real configuration; do not commit IDs or credentials.
3. Supply `TG_BOT_TOKEN`, `TG_CHAT_ID` and `CODEX_NOTIFY=1` through an approved local credential/environment workflow, not hook configuration, command arguments, logs or this repository.
4. Merge the following entry into the `hooks.Stop` array in `~/.codex/hooks.json`, preserving unrelated configuration. Replace any existing Telegram notifier entry to avoid double sending. Review and trust through `/hooks`; do not edit trust records.

```json
{"hooks":[{"type":"command","command":"python3 \"${HOME}/.codex/hooks/telegram-notify-on-stop/telegram_notify_on_stop.py\"","timeout":15,"statusMessage":"Sending Telegram stop notification"}]}
```

Disable through `/hooks` or remove only this notifier entry. Without a ready record for the current task, nothing is sent; do not verify installation with repeated test messages.

## Task records and summaries

- Record: `~/.codex/notify_on_stop/<session_id>.json`; receipt: `~/.codex/notify_on_stop_receipts/<session_id>/<notification_id>.json`. Directory permissions are `700`; records and receipts are `600`.
- Obtain `session_id` from trusted current-task context; it must match the Stop event's field. Use `CODEX_THREAD_ID` when available; do not guess otherwise. Both IDs accept only 1–128 ASCII letters, digits, underscores or hyphens.
- Generate a random UUID hex `notification_id` for each new request and retain it when updating readiness or retrying. Keep one pending request per session; finish or cancel it first. A later independent task in a long conversation may request another notification, but changing IDs must not bypass the same task's notification limit or uncertain-delivery protection.
- Create with `ready:false`. Before stopping, fill in the actual task title, status, result/specific blocker and user action, then atomically update to `ready:true`. The four text fields must be nonempty and are limited to 100, 30, 600 and 300 characters respectively. State “No action needed” when applicable. The agent must redact content; do not forward full replies, code, credentials or private paths.

```json
{"session_id":"CURRENT_TASK_ID","notification_id":"UUID_HEX","ready":false,"task_title":"Update documentation","status":"In progress","summary":"Pending","next_action":"Pending"}
```

Atomic creation example: on completion, read this request, retain both IDs, update the four fields and `ready`, and use the same temporary-file replacement process. Cancellation removes only this task's request, not other tasks' records or receipts.

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
              "ready": False, "task_title": "Update documentation", "status": "In progress",
              "summary": "Pending", "next_action": "Pending"}
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

Creating, updating or cancelling records, and manually recovering receipts, must hold the same exclusive `<session_id>.lock` as the hook and recheck request identity within the lock. Sole ownership or atomic replacement alone does not prevent races with Stop consumption. The hook does not determine elapsed time, user interaction or summary truthfulness; the agent applies those notification rules.

## Sending, receipts and recovery

Only Stop events with `CODEX_NOTIFY=1`, no active Stop-hook continuation, and a valid ready record matching the session are handled. `<session_id>.lock` serializes sends for the same session; lock files may remain. Requests time out after 8 seconds. stdout always emits `{"continue": true}`, without credentials.

| Receipt status | Behavior |
| --- | --- |
| `sending` | Atomically persisted before sending; a failed write prevents sending. If interrupted, retain this status and do not automatically resend |
| `delivery_unknown` | Timeout, network error, 5xx, unconfirmed response or exception during sending; delivery may have occurred, so do not automatically resend |
| `failed` | Unsent configuration/summary errors or explicit rejection (4xx, API `ok:false`); after correcting the cause, a later Stop may retry, without a tight loop |
| `delivered_marker_unconsumed` | API explicitly returned `ok:true`; persist delivery before consuming the matching request. Failed consumption still prevents resending |
| `delivered` | Delivery confirmed and request consumed; do not resend the same ID |

Receipts contain only bound IDs, time, status and redacted error types, never message text, tokens or recipient IDs. Missing records, unready records, mismatched tasks or disabled notifications do not overwrite existing receipts. Receipts indicate sending outcomes, not task completion.

Telegram offers no idempotency key usable by this script, so strict exactly-once delivery cannot be guaranteed. For `sending`/`delivery_unknown`, first check actual Telegram receipt: if delivered, cancel only the remaining request and keep the receipt; if confirmed not delivered and no hook is concurrent, mark this request unready, atomically update its matching receipt to `failed` with reason `confirmed_not_delivered`, then restore readiness using the same ID. If the outcome cannot be confirmed, retain the resend-blocking state; do not delete the receipt or generate a new ID for a speculative retry.

## Legacy migration and verification

Prefer the task directories above. The legacy single slot `~/.codex/notify_on_stop_once` is considered only when the current session has no separate record; it must still contain session-matching JSON with a complete summary and `ready:true`. Old empty markers do not send. Legacy records may omit `notification_id`; their receipt remains `~/.codex/notify_on_stop_receipt.json`. Do not write both locations. Replace an old notifier rather than enabling both.

`CODEX_NOTIFY_ON_STOP_ONCE_FILE`/`CODEX_NOTIFY_ON_STOP_RECEIPT_FILE` can override legacy single-slot paths; new task directories are located under their respective parent directories for isolated tests, not arbitrary delivery-target configuration.

```sh
python3 -B -m unittest discover -s ~/.codex/hooks/telegram-notify-on-stop -p 'test_telegram_notify_on_stop.py'
```

Included tests always mock transport and cover task isolation, readiness, concurrency, allowlisting, failed and uncertain sends, receipt persistence and redacted output. Passing tests or registering a hook does not prove delivery; verify receipts and actual receipt only when the user authorizes a notification. Allowlisting restricts recipients; it does not hide the bot account.
