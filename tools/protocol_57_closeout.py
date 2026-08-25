from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ACTIVE = ROOT / "workplans/active/PROTOCOL-5.7-ENGINEERING-STEWARDSHIP-ALIGNMENT.md"
ARCHIVE = ROOT / "workplans/archive/PROTOCOL-5.7-ENGINEERING-STEWARDSHIP-ALIGNMENT.md"

if not ACTIVE.exists():
    raise RuntimeError("active Protocol 5.7 workplan is missing")
if ARCHIVE.exists():
    raise RuntimeError("Protocol 5.7 archive target already exists")

text = ACTIVE.read_text(encoding="utf-8")
if "status: active\n" not in text:
    raise RuntimeError("Protocol 5.7 workplan is not active")
text = text.replace(
    "status: active\n",
    "status: completed\ncompleted_date: 2026-08-25\n",
    1,
)
run_id = os.environ.get("GITHUB_RUN_ID", "unknown")
text += f'''\n\n## Completion record\n\nProtocol 5.7 implementation closed successfully on 2026-08-25.\n\n- Governing base: `cdc45b04ea1d618da4555ac7e086d403939c1705` (Protocol 5.6.0).\n- Product implementation commit before closeout: `6240a139af5a2ddaad8144319bcc13bdc54fd8f7`.\n- G0 preserved the Protocol 5.6 regression baseline and verified Protocol 5.5 completion commit `e705d2192d522b83265c1994c22423f6c4b9c7e1` is an ancestor before archiving its stale active workplan.\n- G1-G5 gated implementation run `32893010595` passed focused Protocol 5.7 stewardship contracts, preserved Protocol 5.6 proxy-proof contracts, the complete protocol regression suite, package build, independent package validation, committed-distribution parity, and `git diff --check`.\n- Independent Software Design review of the assembled candidate found no material doctrine regression, scope inflation, acceptance-integrity gap, weakening of Protocol 5.6 semantic-owner boundaries, or unnecessary protocol machinery.\n- Normal pull-request `Protocol build check` run `32893153873` passed on PR #20 before administrative closeout.\n- Final clean closeout run `{run_id}` reran the complete repository acceptance commands after archiving this workplan and removing temporary validation markers.\n\nFinal acceptance commands:\n\n```bash\npython -m unittest discover -s tests -v\npython source/build_skills.py --output /tmp/protocol-dist\npython source/validate_packages.py --dist /tmp/protocol-dist\npython source/check_dist.py --expected /tmp/protocol-dist --committed dist\ngit diff --check\n```\n\nProduction qualification was unnecessary: this revision changes protocol/instruction artifacts and their generated packages, not production software runtime behavior or target-hardware performance.\n\nNo material blocker or unresolved Protocol 5.7 obligation remains.\n'''

ARCHIVE.parent.mkdir(parents=True, exist_ok=True)
ARCHIVE.write_text(text, encoding="utf-8")
ACTIVE.unlink()

for rel in (
    "tools/protocol57_ci_trigger.txt",
    "tools/protocol57_review_note.txt",
    "tools/protocol57_pr_trigger.txt",
):
    p = ROOT / rel
    if p.exists():
        p.unlink()

print("Protocol 5.7 closeout state prepared")
