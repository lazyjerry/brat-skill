# brat-skill

`brat-skill` is a local Codex skill for deliberately bratty, loud, unreasonable Traditional Chinese replies.

It also includes an optional Claude Code `UserPromptSubmit` hook companion that injects the bratty reply style before every user prompt.

## Contents

```text
brat-skill/
├── SKILL.md
├── agents/
│   └── openai.yaml
└── hooks/
    ├── claude-settings.user-prompt-submit.json
    └── user_prompt_submit.py
```

## Codex Skill Install

Copy or link the skill folder into your Codex skills directory:

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R brat-skill "${CODEX_HOME:-$HOME/.codex}/skills/brat-skill"
```

Invoke it explicitly with `$brat-skill`, or ask for a 無理取鬧、大吼大叫、任性崩潰式回覆.

## Claude Code Hook Install

To make Claude Code inject the bratty style on every prompt, merge this file into your Claude Code settings:

```text
brat-skill/hooks/claude-settings.user-prompt-submit.json
```

For user-wide installation, merge the `hooks` block into:

```text
~/.claude/settings.json
```

For a single project, merge it into:

```text
.claude/settings.json
```

The hook command points to:

```text
/Users/lazyjerry/Documents/屁孩skill/brat-skill/hooks/user_prompt_submit.py
```

Adjust that path if you clone the repository somewhere else.

## Limits

- The hook injects style guidance through `additionalContext`.
- It cannot override system, developer, project, safety, or tool instructions.
- Harmful requests should still be refused, but the refusal can keep the bratty tone.
