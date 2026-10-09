#!/usr/bin/env python3
"""Task-bound Stop-hook notifier with a machine-readable stdout contract.

Telegram credentials are read only from TG_BOT_TOKEN/TG_CHAT_ID. Only an
agent-prepared, task-bound summary is sent, never the raw transcript.
"""

import json
import os
import fcntl
from pathlib import Path
import re
import sys
import tempfile
from datetime import datetime, timezone
import urllib.error
import urllib.parse
import urllib.request

DEFAULT_RECEIPT_NAME = "notify_on_stop_receipt.json"
REQUEST_TIMEOUT_SECONDS = 8
SAFE_ID_PATTERN = re.compile(r"[A-Za-z0-9_-]{1,128}\Z")
ALLOWED_CHAT_IDS_FILE = Path(__file__).resolve().parent / "allowed-chat-ids.json"


def utc_now():
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def configured_path(env_name, default_path):
    value = os.environ.get(env_name, "").strip()
    return Path(value).expanduser() if value else default_path


def session_paths(session_id):
    """Keep a Stop event within its own filename, receipt, and lock."""
    if not isinstance(session_id, str) or not SAFE_ID_PATTERN.fullmatch(session_id):
        return None
    legacy_marker = configured_path(
        "CODEX_NOTIFY_ON_STOP_ONCE_FILE", Path.home() / ".codex" / "notify_on_stop_once",
    )
    legacy_receipt = configured_path(
        "CODEX_NOTIFY_ON_STOP_RECEIPT_FILE",
        Path.home() / ".codex" / DEFAULT_RECEIPT_NAME,
    )
    marker_dir = legacy_marker.parent / "notify_on_stop"
    receipt_dir = legacy_receipt.parent / "notify_on_stop_receipts"
    return (marker_dir / f"{session_id}.json", receipt_dir / session_id,
            marker_dir / f"{session_id}.lock", legacy_marker, legacy_receipt)


def ensure_private_dir(path):
    path.mkdir(mode=0o700, parents=True, exist_ok=True)
    if not path.is_dir() or path.is_symlink():
        raise OSError("invalid_notification_directory")
    path.chmod(0o700)


def delivered_already(path, session_id, notification_id):
    try:
        if path.is_symlink():
            return False
        data = json.loads(path.read_text(encoding="utf-8"))
        return (data.get("session_id") == session_id and
                data.get("notification_id") == notification_id and
                data.get("status") in (
                    "sending", "delivery_unknown", "delivered", "delivered_marker_unconsumed"))
    except (OSError, ValueError, AttributeError):
        return False


def atomic_write_json(path, payload):
    """Write a redacted receipt atomically with mode 600."""
    path = Path(path)
    if not path.parent.is_dir():
        return False
    fd = None
    tmp_path = None
    try:
        fd, tmp_path = tempfile.mkstemp(prefix=f".{path.name}.", dir=str(path.parent))
        os.fchmod(fd, 0o600)
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            fd = None
            json.dump(payload, handle, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
        os.chmod(tmp_path, 0o600)
        os.replace(tmp_path, path)
        os.chmod(path, 0o600)
        return True
    except Exception:
        if fd is not None:
            try:
                os.close(fd)
            except OSError:
                pass
        if tmp_path:
            try:
                os.unlink(tmp_path)
            except OSError:
                pass
        return False


def write_receipt(receipt_path, status, reason, marker_present, attempted, **extra):
    payload = {
        "schema_version": 1,
        "recorded_at": utc_now(),
        "status": status,
        "reason": reason,
        "marker_present": bool(marker_present),
        "attempted": bool(attempted),
    }
    for key, value in extra.items():
        if value is not None:
            payload[key] = value
    return atomic_write_json(receipt_path, payload)


def load_payload():
    raw = sys.stdin.read()
    if not raw.strip():
        return {}
    try:
        value = json.loads(raw)
    except Exception:
        return {}
    return value if isinstance(value, dict) else {}


def notification_text(marker_data):
    """Validate an explicit notification contract, not arbitrary chat text."""
    limits = {"task_title": 100, "status": 30, "summary": 600, "next_action": 300}
    values = {}
    for field, limit in limits.items():
        value = marker_data.get(field)
        if not isinstance(value, str) or not value.strip() or len(value) > limit:
            raise ValueError("invalid_summary_fields")
        values[field] = value.strip()
    return (f"Codex | {values['task_title']}\n"
            f"Status: {values['status']}\n"
            f"Result: {values['summary']}\n"
            f"Next action: {values['next_action']}")


def recipient_allowed(chat_id):
    """Fail closed unless the numeric private-chat ID is locally allowlisted."""
    try:
        allowed = json.loads(ALLOWED_CHAT_IDS_FILE.read_text(encoding="utf-8"))["allowed_chat_ids"]
        target = int(chat_id)
        return (target > 0 and isinstance(allowed, list)
                and any(type(item) is int and item == target for item in allowed))
    except (OSError, ValueError, KeyError, TypeError):
        return False


def telegram_send(token, chat_id, text):
    if not recipient_allowed(chat_id):
        raise RuntimeError("recipient_not_allowed")
    # The endpoint is fixed in source; token never appears in argv or logs.
    url = "https://api.telegram.org/bot" + token + "/sendMessage"
    body = urllib.parse.urlencode({
        "chat_id": chat_id,
        "text": text,
    }).encode("utf-8")
    request = urllib.request.Request(
        url,
        data=body,
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=REQUEST_TIMEOUT_SECONDS) as response:
            status_code = int(response.status)
            response_body = response.read(1024 * 1024)
    except urllib.error.HTTPError as exc:
        raise RuntimeError(f"http_{exc.code}") from None
    except Exception as exc:
        raise RuntimeError(type(exc).__name__) from None
    if status_code < 200 or status_code >= 300:
        raise RuntimeError(f"http_{status_code}")
    try:
        parsed = json.loads(response_body.decode("utf-8"))
    except Exception:
        raise RuntimeError("invalid_json") from None
    if not isinstance(parsed, dict) or type(parsed.get("ok")) is not bool:
        raise RuntimeError("invalid_response")
    if parsed["ok"] is False:
        raise RuntimeError("api_ok_false")
    return status_code


def run(context=None):
    if os.environ.get("CODEX_NOTIFY", "") != "1":
        return
    payload = load_payload()
    if payload.get("hook_event_name") != "Stop" or payload.get("stop_hook_active"):
        return
    session_id = payload.get("session_id")
    paths = session_paths(session_id)
    if paths is None:
        return
    session_marker, session_receipt_dir, lock_path, legacy_marker, legacy_receipt = paths
    if not session_marker.is_file() and not legacy_marker.is_file():
        return
    ensure_private_dir(lock_path.parent)
    fd = os.open(lock_path, os.O_CREAT | os.O_RDWR | os.O_NOFOLLOW, 0o600)
    try:
        fcntl.flock(fd, fcntl.LOCK_EX)
        run_locked(session_id, session_marker, session_receipt_dir, legacy_marker,
                   legacy_receipt, context)
    finally:
        os.close(fd)


def run_locked(session_id, session_marker, session_receipt_dir, legacy_marker,
               legacy_receipt, context=None):
    marker = session_marker if session_marker.is_file() else legacy_marker
    if not marker.is_file():
        return
    is_legacy = marker == legacy_marker
    if marker.is_symlink():
        return
    try:
        marker_data = json.loads(marker.read_text(encoding="utf-8"))
        if not isinstance(marker_data, dict):
            raise ValueError("invalid_marker")
    except (ValueError, OSError):
        return
    if marker_data.get("session_id") != session_id:
        return
    notification_id = marker_data.get("notification_id")
    if is_legacy:
        if notification_id is not None and (
                not isinstance(notification_id, str) or
                not SAFE_ID_PATTERN.fullmatch(notification_id)):
            return
        receipt = legacy_receipt
    else:
        if not isinstance(notification_id, str) or not SAFE_ID_PATTERN.fullmatch(notification_id):
            return
        receipt = session_receipt_dir / f"{notification_id}.json"
    if delivered_already(receipt, session_id, notification_id):
        return
    if marker_data.get("ready") is not True:
        return
    identity = {"session_id": session_id, "notification_id": notification_id}
    if context is not None:
        context.update(receipt=receipt, marker=marker, identity=identity, attempted=False)
    if not is_legacy:
        ensure_private_dir(receipt.parent)
    try:
        text = notification_text(marker_data)
    except ValueError:
        write_receipt(receipt, "failed", "invalid_summary_fields", True, False, **identity)
        return

    token = os.environ.get("TG_BOT_TOKEN", "").strip()
    chat_id = os.environ.get("TG_CHAT_ID", "").strip()
    if not token or not chat_id:
        write_receipt(receipt, "failed", "missing_credentials", True, False, **identity)
        return
    if not recipient_allowed(chat_id):
        write_receipt(receipt, "failed", "recipient_not_allowed", True, False, **identity)
        return

    # Persist before the POST: a timeout or killed process must not cause a resend.
    if not write_receipt(receipt, "sending", "telegram_pending", True, True, **identity):
        return
    try:
        if context is not None:
            context["attempted"] = True
        status_code = telegram_send(token, chat_id, text)
    except RuntimeError as exc:
        error_type = str(exc)
        rejected = error_type in ("api_ok_false", "recipient_not_allowed") or re.fullmatch(
            r"http_4[0-9]{2}", error_type)
        write_receipt(
            receipt, "failed" if rejected else "delivery_unknown",
            "telegram_send_rejected" if rejected else "telegram_result_unknown", True, True,
            error_type=error_type, **identity,
        )
        return

    # Save confirmed delivery before consuming the request. If this write fails,
    # the durable sending receipt still blocks automatic duplicate delivery.
    if not write_receipt(
        receipt, "delivered_marker_unconsumed", "telegram_ok_marker_not_consumed", True, True,
        api_ok=True, http_status=status_code, marker_consumed=False, **identity,
    ):
        return

    # Only confirmed Telegram API ok=true reaches marker consumption.
    marker_consumed = False
    marker_error = None
    try:
        current = json.loads(marker.read_text(encoding="utf-8"))
        if (current.get("session_id") == session_id and
                current.get("notification_id") == notification_id):
            marker.unlink()
            marker_consumed = True
        else:
            marker_error = "replaced_during_send"
    except FileNotFoundError:
        marker_error = "already_absent"
    except (OSError, ValueError, AttributeError) as exc:
        marker_error = type(exc).__name__

    if marker_consumed:
        write_receipt(
            receipt, "delivered", "telegram_ok", True, True,
            api_ok=True, http_status=status_code, marker_consumed=True,
            **identity,
        )
    else:
        write_receipt(
            receipt, "delivered_marker_unconsumed", "telegram_ok_marker_not_consumed", True, True,
            api_ok=True, http_status=status_code, marker_consumed=False,
            marker_error=marker_error, **identity,
        )


def main():
    context = {}
    try:
        run(context)
    except Exception as exc:
        if context.get("receipt") is not None:
            write_receipt(
                context["receipt"],
                "delivery_unknown" if context["attempted"] else "failed", "internal_error",
                context["marker"].is_file(), context["attempted"],
                error_type=type(exc).__name__, **context["identity"],
            )


if __name__ == "__main__":
    main()
    # Stop-hook stdout must remain machine-readable and contain no credentials.
    sys.stdout.write('{"continue": true}\n')
