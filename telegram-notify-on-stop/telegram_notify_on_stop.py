#!/usr/bin/env python3
"""Private Stop-hook notifier with a machine-readable stdout contract.

Telegram credentials are read only from TG_BOT_TOKEN/TG_CHAT_ID. The message is
intentionally generic so the hook does not export transcript, project, or Git
content. Operational state is written to a mode-600 redacted receipt.
"""

import json
import os
from pathlib import Path
import sys
import tempfile
from datetime import datetime, timezone
import urllib.error
import urllib.parse
import urllib.request

DEFAULT_RECEIPT_NAME = "notify_on_stop_receipt.json"
REQUEST_TIMEOUT_SECONDS = 8


def utc_now():
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def configured_path(env_name, default_path):
    value = os.environ.get(env_name, "").strip()
    return Path(value).expanduser() if value else default_path


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
    atomic_write_json(receipt_path, payload)


def load_payload():
    raw = sys.stdin.read()
    if not raw.strip():
        return False
    try:
        value = json.loads(raw)
    except Exception:
        return False
    return isinstance(value, dict)


def telegram_send(token, chat_id):
    # The endpoint is fixed in source; token never appears in argv or logs.
    url = "https://api.telegram.org/bot" + token + "/sendMessage"
    body = urllib.parse.urlencode({
        "chat_id": chat_id,
        "text": "Codex has stopped this turn.\n\nCheck the conversation for results or pending decisions.",
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
    if not isinstance(parsed, dict) or parsed.get("ok") is not True:
        raise RuntimeError("api_ok_false")
    return status_code


def run():
    marker = configured_path(
        "CODEX_NOTIFY_ON_STOP_ONCE_FILE",
        Path.home() / ".codex" / "notify_on_stop_once",
    )
    receipt = configured_path(
        "CODEX_NOTIFY_ON_STOP_RECEIPT_FILE",
        Path.home() / ".codex" / DEFAULT_RECEIPT_NAME,
    )
    marker_present = marker.is_file()

    if os.environ.get("CODEX_NOTIFY", "") != "1":
        write_receipt(receipt, "skipped", "disabled", marker_present, False)
        return
    if not marker_present:
        write_receipt(receipt, "skipped", "no_marker", False, False)
        return

    token = os.environ.get("TG_BOT_TOKEN", "").strip()
    chat_id = os.environ.get("TG_CHAT_ID", "").strip()
    if not token or not chat_id:
        write_receipt(receipt, "failed", "missing_credentials", True, False)
        return

    payload_valid = load_payload()
    try:
        status_code = telegram_send(token, chat_id)
    except RuntimeError as exc:
        write_receipt(
            receipt, "failed", "telegram_send_failed", True, True,
            error_type=str(exc), payload_valid=payload_valid,
        )
        return

    # Only confirmed Telegram API ok=true reaches marker consumption.
    marker_consumed = False
    marker_error = None
    try:
        marker.unlink()
        marker_consumed = True
    except FileNotFoundError:
        marker_error = "already_absent"
    except OSError as exc:
        marker_error = type(exc).__name__

    if marker_consumed:
        write_receipt(
            receipt, "delivered", "telegram_ok", True, True,
            api_ok=True, http_status=status_code, marker_consumed=True,
            payload_valid=payload_valid,
        )
    else:
        write_receipt(
            receipt, "delivered_marker_unconsumed", "telegram_ok_marker_not_consumed", True, True,
            api_ok=True, http_status=status_code, marker_consumed=False,
            marker_error=marker_error, payload_valid=payload_valid,
        )


def main():
    try:
        run()
    except Exception as exc:
        receipt = configured_path(
            "CODEX_NOTIFY_ON_STOP_RECEIPT_FILE",
            Path.home() / ".codex" / DEFAULT_RECEIPT_NAME,
        )
        marker = configured_path(
            "CODEX_NOTIFY_ON_STOP_ONCE_FILE",
            Path.home() / ".codex" / "notify_on_stop_once",
        )
        write_receipt(
            receipt, "failed", "internal_error", marker.is_file(), False,
            error_type=type(exc).__name__,
        )


if __name__ == "__main__":
    main()
    # Stop-hook stdout must remain machine-readable and contain no credentials.
    sys.stdout.write('{"continue": true}\n')
