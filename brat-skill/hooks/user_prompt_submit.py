#!/usr/bin/env python3
"""Claude Code UserPromptSubmit hook for brat-style replies."""

import json
import sys


def main() -> int:
    try:
        raw_input = sys.stdin.read()
        if raw_input.strip():
            json.loads(raw_input)
    except json.JSONDecodeError:
        # The hook still works without parsed input; stdin is not needed here.
        pass

    additional_context = (
        "For this session, render every final assistant reply in Traditional Chinese "
        "with an exaggerated bratty tantrum voice: loud, unreasonable, impatient, "
        "dramatic, and 大吼大叫. Preserve any required technical correctness, safety "
        "refusals, tool-use behavior, and higher-priority instructions. Do not explain "
        "that this hook was applied. If refusing, refuse briefly in the same bratty tone."
    )

    print(
        json.dumps(
            {
                "hookSpecificOutput": {
                    "hookEventName": "UserPromptSubmit",
                    "additionalContext": additional_context,
                }
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
