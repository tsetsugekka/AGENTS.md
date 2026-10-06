# 回答结束状态钩子

[AGENTS.zh-CN.md](AGENTS.zh-CN.md) 定义状态含义；[check_final_status.py](check_final_status.py) 只检查标签格式。脚本从 stdin 读取 Stop 事件 JSON 并检查 `last_assistant_message`，要求最后一个非空行仅包含六种状态之一：🔴待选择、🔴待讨论、🔴遇阻中断、🟡阶段性完成、🟡待确认、🟢全部完成。不接受与正文同行、旧括号格式或附加标点／Markdown 强调。空消息和无关事件跳过。

无需提醒时输出 `{}`，否则输出 `systemMessage`。它不会重新启动 Agent、调用模型、保存消息、访问网络或判断实际完成情况。只需 Python 3 标准库。

## 安装与停用

将此目录复制到 `~/.codex/hooks/final-response-status/`。把以下条目合并到 `~/.codex/hooks.json` 的 `hooks.Stop` 数组，保留已有条目：

```json
{"hooks":[{"type":"command","command":"python3 \"${HOME}/.codex/hooks/final-response-status/check_final_status.py\"","timeout":3,"statusMessage":"Checking final response status"}]}
```

通过 `/hooks` 审阅并信任新定义，不编辑信任记录。停用时禁用此条目或仅移除此配置条目。

## 验证

用合成 Stop 事件测试六种有效标签、正文同行、位置错误、颜色错误、旧格式、空消息和无关事件；验证合并后的 JSON。本地测试不证明宿主已加载或触发钩子，通过信任审批后另行确认实际触发。

脚本提示文字为英文，同时接受英文规则的六种彩色标签和中文底稿中的对应标签。
