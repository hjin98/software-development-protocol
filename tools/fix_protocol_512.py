#!/usr/bin/env python3
from pathlib import Path
p = Path(__file__).resolve().parents[1] / "source/shared/references/workflow-and-workplans.md"
s = p.read_text(encoding="utf-8")
old = "Ordinary implementation attempts and review cycles do **not** require a new numbered authority revision."
new = "Ordinary implementation attempts and review cycles do not require a new numbered authority revision."
if new not in s:
    if old not in s:
        raise SystemExit("Protocol 5.12 revision-economy sentence not found")
    p.write_text(s.replace(old, new, 1), encoding="utf-8")
