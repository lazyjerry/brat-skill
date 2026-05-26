# brat-skill

`brat-skill` 是一個本機 Codex skill，用來讓最終回覆套用刻意任性、吵鬧、無理取鬧的繁體中文語氣。

這個 skill 的觸發語意已設定為：使用者只要送出任何訊息，就應套用 brat 風格。它也提供 Claude Code `UserPromptSubmit` hook companion，用來在每次 prompt 進入 Claude 前注入同樣的語氣規則。

## 內容

```text
brat-skill/
├── SKILL.md
├── agents/
│   └── openai.yaml
└── hooks/
    ├── claude-settings.user-prompt-submit.json
    └── user_prompt_submit.py
```

## Codex Skill 安裝

將 skill 資料夾複製或連結到 Codex skills 目錄：

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R brat-skill "${CODEX_HOME:-$HOME/.codex}/skills/brat-skill"
```

目前 `agents/openai.yaml` 已設定：

```yaml
policy:
  allow_implicit_invocation: true
```

`SKILL.md` 的 `description` 也已宣告：使用者送出任何訊息、提出任何請求、一般對話、coding、research、文件、摘要或操作協助時，都應使用這個 skill。

## Claude Code Hook 安裝

若要讓 Claude Code 在每次 prompt 前都注入 brat 風格規則，將下列檔案中的 `hooks` 區塊合併到 Claude Code settings：

```text
brat-skill/hooks/claude-settings.user-prompt-submit.json
```

全使用者範圍：

```text
~/.claude/settings.json
```

單一專案範圍：

```text
.claude/settings.json
```

hook command 預設指向：

```text
/Users/lazyjerry/Documents/屁孩skill/brat-skill/hooks/user_prompt_submit.py
```

如果 repository clone 到其他位置，請同步調整這個路徑。

## 測試

測試 hook 是否能輸出 Claude Code 可讀的 `additionalContext`：

```bash
printf '{"hook_event_name":"UserPromptSubmit","prompt":"測試","cwd":"/tmp"}' \
  | brat-skill/hooks/user_prompt_submit.py
```

預期輸出包含：

```json
{
  "hookSpecificOutput": {
    "hookEventName": "UserPromptSubmit",
    "additionalContext": "..."
  }
}
```

## 限制

- Codex skill 的自動觸發取決於宿主工具是否載入並遵守 skill metadata。
- Claude Code hook 透過 `additionalContext` 注入語氣規則，但不能凌駕 system、developer、project、safety 或 tool instructions。
- 有害請求仍應拒絕；拒絕時可保留 brat 語氣。
