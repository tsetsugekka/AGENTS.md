"""Local-only Stop hook tests; Telegram transport is always mocked."""

import fcntl
import importlib.machinery
import importlib.util
import io
import json
import multiprocessing
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import time
import unittest
import urllib.error
from unittest.mock import patch


SCRIPT = Path(__file__).resolve().with_name("telegram_notify_on_stop.py")
loader = importlib.machinery.SourceFileLoader("telegram_notify_on_stop", str(SCRIPT))
spec = importlib.util.spec_from_loader(loader.name, loader)
hook = importlib.util.module_from_spec(spec)
loader.exec_module(hook)


def concurrent_worker(base, sent):
    env = {
        "CODEX_NOTIFY": "1", "CODEX_NOTIFY_ON_STOP_ONCE_FILE": str(base / "legacy"),
        "CODEX_NOTIFY_ON_STOP_RECEIPT_FILE": str(base / "receipt.json"),
        "TG_BOT_TOKEN": "dummy", "TG_CHAT_ID": "123",
    }
    def fake_send(*_args):
        with open(sent, "a", encoding="utf-8") as handle:
            handle.write("sent\n")
        time.sleep(0.15)
        return 200
    with patch.dict(os.environ, env), patch.object(hook.sys, "stdin", io.StringIO(json.dumps({
        "hook_event_name": "Stop", "session_id": "same-session", "stop_hook_active": False,
    }))), patch.object(hook, "recipient_allowed", return_value=True), patch.object(
        hook, "telegram_send", side_effect=fake_send,
    ):
        hook.run()


class NotificationTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.env = {
            "CODEX_NOTIFY": "1", "CODEX_NOTIFY_ON_STOP_ONCE_FILE": str(self.base / "legacy"),
            "CODEX_NOTIFY_ON_STOP_RECEIPT_FILE": str(self.base / "receipt.json"),
            "TG_BOT_TOKEN": "dummy", "TG_CHAT_ID": "123",
        }

    def marker(self, session, ready=True, legacy=False, notification_id="request-1"):
        path = self.base / "legacy" if legacy else self.base / "notify_on_stop" / f"{session}.json"
        path.parent.mkdir(exist_ok=True)
        data = {
            "session_id": session, "ready": ready, "task_title": "Task", "status": "done",
            "summary": "Result", "next_action": "None",
        }
        if not legacy:
            data["notification_id"] = notification_id
        path.write_text(json.dumps(data), encoding="utf-8")
        return path

    def run_hook(self, session, send=None, active=False):
        event = {"hook_event_name": "Stop", "session_id": session, "stop_hook_active": active}
        with patch.dict(os.environ, self.env), patch.object(
            hook.sys, "stdin", io.StringIO(json.dumps(event))
        ), patch.object(hook, "recipient_allowed", return_value=True), patch.object(
            hook, "telegram_send", side_effect=send or (lambda *_: 200)
        ) as sender:
            hook.run()
            return sender.call_count

    def receipt(self, session="task", notification_id="request-1"):
        return self.base / "notify_on_stop_receipts" / session / f"{notification_id}.json"

    def event(self, session="task"):
        return patch.object(hook.sys, "stdin", io.StringIO(json.dumps({
            "hook_event_name": "Stop", "session_id": session, "stop_hook_active": False,
        })))

    def test_two_sessions_match_and_consume_independently(self):
        first = self.marker("first")
        second = self.marker("second")
        self.assertEqual(self.run_hook("first"), 1)
        self.assertFalse(first.exists())
        self.assertTrue(second.exists())
        self.assertEqual(self.run_hook("second"), 1)
        self.assertFalse(second.exists())
        for session in ("first", "second"):
            receipt = json.loads((self.base / "notify_on_stop_receipts" / session / "request-1.json").read_text())
            self.assertEqual(receipt["status"], "delivered")

    def test_same_session_new_request_sends_old_request_does_not(self):
        marker = self.marker("long-chat", notification_id="request-1")
        self.assertEqual(self.run_hook("long-chat"), 1)
        self.marker("long-chat", notification_id="request-1")
        self.assertEqual(self.run_hook("long-chat"), 0)
        self.assertTrue(marker.exists())
        self.marker("long-chat", notification_id="request-2")
        self.assertEqual(self.run_hook("long-chat"), 1)
        self.assertFalse(marker.exists())
        receipts = self.base / "notify_on_stop_receipts" / "long-chat"
        self.assertEqual(json.loads((receipts / "request-1.json").read_text())["notification_id"], "request-1")
        self.assertEqual(json.loads((receipts / "request-2.json").read_text())["notification_id"], "request-2")

    def test_unready_failure_and_success(self):
        marker = self.marker("task", ready=False)
        self.assertEqual(self.run_hook("task"), 0)
        self.assertTrue(marker.exists())
        self.assertFalse((self.base / "notify_on_stop_receipts" / "task" / "request-1.json").exists())
        self.marker("task", ready=True)
        self.assertEqual(self.run_hook("task", send=lambda *_: (_ for _ in ()).throw(RuntimeError("http_400"))), 1)
        self.assertTrue(marker.exists())
        self.assertEqual(json.loads((self.base / "notify_on_stop_receipts" / "task" / "request-1.json").read_text())["status"], "failed")
        self.assertEqual(self.run_hook("task"), 1)
        self.assertFalse(marker.exists())
        self.assertEqual(self.run_hook("task"), 0)

    def test_legacy_marker_matching_preserves_other_task(self):
        legacy = self.marker("old", legacy=True)
        self.assertEqual(self.run_hook("other"), 0)
        self.assertTrue(legacy.exists())
        self.assertEqual(self.run_hook("old"), 1)
        self.assertFalse(legacy.exists())
        self.assertEqual(json.loads((self.base / "receipt.json").read_text())["status"], "delivered")

    def test_invalid_session_and_active_stop(self):
        marker = self.marker("safe")
        self.assertEqual(self.run_hook("../safe"), 0)
        self.assertEqual(self.run_hook("safe", active=True), 0)
        self.assertTrue(marker.exists())

    def test_internal_error_receipt_stays_with_parsed_request(self):
        marker = self.marker("task", notification_id="request-7")
        other = self.marker("other", notification_id="request-8")
        event = {"hook_event_name": "Stop", "session_id": "task", "stop_hook_active": False}
        with patch.dict(os.environ, self.env), patch.object(
            hook.sys, "stdin", io.StringIO(json.dumps(event))
        ), patch.object(hook, "notification_text", side_effect=OSError("mock")):
            hook.main()
        receipt = json.loads((self.base / "notify_on_stop_receipts" / "task" / "request-7.json").read_text())
        self.assertEqual((receipt["status"], receipt["reason"]), ("failed", "internal_error"))
        self.assertEqual(receipt["notification_id"], "request-7")
        self.assertTrue(marker.exists())
        self.assertTrue(other.exists())
        self.assertFalse((self.base / "notify_on_stop_receipts" / "other").exists())

    def test_concurrent_same_session_sends_once(self):
        marker = self.marker("same-session")
        sent = self.base / "sent.txt"
        ctx = multiprocessing.get_context("fork")
        processes = [ctx.Process(target=concurrent_worker, args=(self.base, sent)) for _ in range(2)]
        for process in processes:
            process.start()
        for process in processes:
            process.join(5)
            self.assertEqual(process.exitcode, 0)
        self.assertEqual(sent.read_text().splitlines(), ["sent"])
        self.assertFalse(marker.exists())

    def test_locked_writer_waits_for_consumption_and_preserves_new_request(self):
        marker = self.marker("same-session")
        replacement = json.loads(marker.read_text())
        replacement["notification_id"] = "request-2"
        ctx = multiprocessing.get_context("fork")
        sending, waiting = ctx.Event(), ctx.Event()

        def write_replacement():
            if not sending.wait(5):
                raise AssertionError("Stop did not begin sending")
            with open(marker.with_suffix(".lock"), "a", encoding="utf-8") as lock:
                try:
                    fcntl.flock(lock.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
                except BlockingIOError:
                    waiting.set()
                else:
                    raise AssertionError("Writer acquired the lock during sending")
                fcntl.flock(lock.fileno(), fcntl.LOCK_EX)
                if marker.exists():
                    raise AssertionError("Writer acquired the lock before marker consumption")
                if not hook.atomic_write_json(marker, replacement):
                    raise AssertionError("Replacement marker could not be written")

        def fake_send(*_args):
            sending.set()
            self.assertTrue(waiting.wait(5), "Writer did not wait for the session lock")
            return 200

        writer = ctx.Process(target=write_replacement)
        writer.start()
        try:
            self.assertEqual(self.run_hook("same-session", send=fake_send), 1)
        finally:
            writer.join(5)
            if writer.is_alive():
                writer.terminate()
                writer.join(5)
        self.assertEqual(writer.exitcode, 0)
        self.assertEqual(json.loads(marker.read_text())["notification_id"], "request-2")
        self.assertEqual(self.run_hook("same-session"), 1)
        self.assertFalse(marker.exists())
        for notification_id in ("request-1", "request-2"):
            self.assertEqual(json.loads(self.receipt("same-session", notification_id).read_text())["status"],
                             "delivered")

    def test_disabled_invalid_event_and_absent_marker_are_quiet(self):
        marker = self.marker("task")
        cases = [("0", {"hook_event_name": "Stop", "session_id": "task"}),
                 ("1", {"hook_event_name": "Start", "session_id": "task"}),
                 ("1", {"hook_event_name": "Stop", "session_id": "absent"})]
        for enabled, event in cases:
            with self.subTest(event=event, enabled=enabled), patch.dict(
                os.environ, {**self.env, "CODEX_NOTIFY": enabled}
            ), patch.object(hook.sys, "stdin", io.StringIO(json.dumps(event))), patch.object(
                hook, "telegram_send"
            ) as sender:
                hook.run()
                sender.assert_not_called()
        self.assertTrue(marker.exists())
        self.assertFalse(self.receipt().exists())

    def test_missing_credentials_and_denied_recipient_do_not_send(self):
        for token, allowed, reason in [("", True, "missing_credentials"),
                                       ("dummy", False, "recipient_not_allowed")]:
            with self.subTest(reason=reason):
                marker = self.marker("task")
                with patch.dict(os.environ, {**self.env, "TG_BOT_TOKEN": token}), self.event(), patch.object(
                    hook, "recipient_allowed", return_value=allowed
                ), patch.object(hook, "telegram_send") as sender:
                    hook.run()
                    sender.assert_not_called()
                self.assertEqual(json.loads(self.receipt().read_text())["reason"], reason)
                self.assertTrue(marker.exists())

    def test_receipt_write_failure_before_send_keeps_marker(self):
        marker = self.marker("task")
        with patch.object(hook, "atomic_write_json", return_value=False):
            self.assertEqual(self.run_hook("task"), 0)
        self.assertTrue(marker.exists())

    def test_sent_but_receipt_update_fails_does_not_resend(self):
        marker = self.marker("task")
        write = hook.atomic_write_json
        def only_sending(path, payload):
            return write(path, payload) if payload["status"] == "sending" else False
        with patch.object(hook, "atomic_write_json", side_effect=only_sending):
            self.assertEqual(self.run_hook("task"), 1)
        self.assertTrue(marker.exists())
        self.assertEqual(json.loads(self.receipt().read_text())["status"], "sending")
        self.assertEqual(self.run_hook("task"), 0)

    def test_sent_but_marker_consumption_fails_does_not_resend(self):
        marker = self.marker("task")
        with patch.object(Path, "unlink", side_effect=PermissionError("mock")):
            self.assertEqual(self.run_hook("task"), 1)
        self.assertTrue(marker.exists())
        self.assertEqual(json.loads(self.receipt().read_text())["status"], "delivered_marker_unconsumed")
        self.assertEqual(self.run_hook("task"), 0)

    def test_timeout_is_unknown_and_does_not_resend(self):
        marker = self.marker("task")
        with patch.dict(os.environ, self.env), self.event(), patch.object(
            hook, "recipient_allowed", return_value=True
        ), patch.object(hook.urllib.request, "urlopen", side_effect=TimeoutError("dummy")) as transport:
            hook.run()
            transport.assert_called_once()
        self.assertTrue(marker.exists())
        self.assertEqual(json.loads(self.receipt().read_text())["status"], "delivery_unknown")
        self.assertEqual(self.run_hook("task"), 0)

    def test_explicit_api_rejection_is_failed_and_can_retry(self):
        for index, response_error in enumerate((urllib.error.HTTPError("https://example.invalid", 400, "bad", {}, None),
                                               None)):
            with self.subTest(error=response_error):
                session = f"task-{index}"
                self.marker(session)
                with patch.dict(os.environ, self.env), self.event(session), patch.object(
                    hook, "recipient_allowed", return_value=True
                ), patch.object(hook.urllib.request, "urlopen") as transport:
                    if response_error:
                        transport.side_effect = response_error
                    else:
                        response = transport.return_value.__enter__.return_value
                        response.status = 200
                        response.read.return_value = b'{"ok":false}'
                    hook.run()
                self.assertEqual(json.loads(self.receipt(session).read_text())["status"], "failed")
                self.assertEqual(self.run_hook(session), 1)

    def test_allowlist_requires_exact_positive_integer_chat_id(self):
        allowed_file = self.base / "allowed.json"
        with patch.object(hook, "ALLOWED_CHAT_IDS_FILE", allowed_file):
            self.assertFalse(hook.recipient_allowed("123"))
            allowed_file.write_text(json.dumps({"allowed_chat_ids": [123, "456", -7]}))
            self.assertTrue(hook.recipient_allowed("123"))
            for chat_id in ("456", "-7", "999", "not-an-id"):
                self.assertFalse(hook.recipient_allowed(chat_id))
            allowed_file.write_text("invalid JSON")
            self.assertFalse(hook.recipient_allowed("123"))

    def test_transport_requires_confirmed_ok_and_encodes_summary(self):
        with patch.object(hook, "recipient_allowed", return_value=True), patch.object(
            hook.urllib.request, "urlopen"
        ) as transport:
            response = transport.return_value.__enter__.return_value
            response.status = 200
            response.read.return_value = b'{"ok":true}'
            self.assertEqual(hook.telegram_send("dummy", "123", "Task summary"), 200)
            request = transport.call_args.args[0]
            self.assertEqual(hook.urllib.parse.parse_qs(request.data.decode())["text"], ["Task summary"])
            response.read.return_value = b'not JSON'
            with self.assertRaises(RuntimeError):
                hook.telegram_send("dummy", "123", "Task summary")

    def test_receipt_and_stdout_do_not_expose_message_or_credentials(self):
        self.marker("task")
        self.assertEqual(self.run_hook("task"), 1)
        receipt = self.receipt().read_text()
        for private in ("dummy", "Result", "next_action", "task_title"):
            self.assertNotIn(private, receipt)
        result = subprocess.run([sys.executable, "-B", str(SCRIPT)], input="{}", text=True,
                                capture_output=True, env={**os.environ, **self.env, "CODEX_NOTIFY": "0"},
                                check=True)
        self.assertEqual(json.loads(result.stdout), {"continue": True})
        self.assertEqual(result.stderr, "")


if __name__ == "__main__":
    unittest.main()
