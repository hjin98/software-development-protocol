#!/usr/bin/env python3
from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ACTIVE = ROOT / "workplans/active/PROTOCOL-5.6-PROXY-PROOF-ACCEPTANCE.md"
ARCHIVE = ROOT / "workplans/archive/PROTOCOL-5.6-PROXY-PROOF-ACCEPTANCE.md"

text = ACTIVE.read_text(encoding="utf-8")
if text.count("status: active") != 1:
    raise SystemExit("expected exactly one active workplan status")
text = text.replace("status: active", "status: completed\ncompleted_date: 2026-08-25", 1)
run_id = os.environ.get("GITHUB_RUN_ID", "unknown")
completion = f"""

## Completion record

Protocol 5.6 was implemented and independently reviewed under this workplan without reopening the governing Protocol 5 doctrine or two-role lifecycle.

### G0-G3 implementation evidence

The gated implementation workflow applied the canonical source/test transformation and succeeded through regression, package build, package validation, source-to-dist parity, and whitespace checks before creating implementation commit `ee99ad861f62b5cac472d006abbcd3a62823ee2e`. A content-identical reviewed checkpoint used tree `dee32889ecbbed2873c4f37b8044b72f3b5cf95b` at commit `30f64fc3d1a4b972f04e2c349d7d337737a4c58a`.

Implementation workflow evidence: GitHub Actions run `32887845204`, job `97932397376`, conclusion `success`.

### G4 independent assembled review

The final source/diff was reviewed against the accepted contract rather than the implementer's summary. The review found no material doctrine regression, no lifecycle expansion, no global anti-mock policy, no production-qualification inflation, no local-reconciliation loophole for frozen real-owner boundaries, and no authority duplication. Root `AGENTS.md` remains a short authority router rather than a second protocol manual.

Scenario closure:

- S1 owner mock: rejected as insufficient owner acceptance.
- S2 below-owner fake: explicitly permitted for bounded integration while the real owner/control path executes.
- S3 direct helper bypass: rejected when caller/restart/reconciliation/authorization detection is the claim.
- S4 fake persistence: rejected when durable persistence/restart/recovery is the claim.
- S5 helper-only consumer proof: rejected when assembled consumer behavior is the claim.
- S6 unavailable real boundary: unavailable/blocking or evidence-backed design reopen; never silently proxy-passed.

### G5 final repository acceptance

Final closure workflow run `{run_id}` executes the repository-required commands on the assembled candidate before this completion commit is created:

```bash
python -m unittest discover -s tests -v
python source/build_skills.py --output /tmp/protocol-dist
python source/validate_packages.py --dist /tmp/protocol-dist
python source/check_dist.py --expected /tmp/protocol-dist --committed dist
git diff --check
```

This workplan is archived only if every command succeeds. Production qualification remains unnecessary for this protocol/instruction revision.
"""
text += completion
ARCHIVE.parent.mkdir(parents=True, exist_ok=True)
ARCHIVE.write_text(text, encoding="utf-8")
ACTIVE.unlink()
print(f"archived completed workplan; closeout run={run_id}")
