#!/usr/bin/env python3
"""Verify committed dist packages semantically match canonical source."""

from __future__ import annotations

import json
import tempfile
import zipfile
from pathlib import Path

import build_skills

ROOT = Path(__file__).resolve().parent.parent
COMMITTED_DIST = ROOT / "dist"


def zip_contents(path: Path) -> dict[str, bytes]:
    with zipfile.ZipFile(path, "r") as zf:
        return {name: zf.read(name) for name in sorted(zf.namelist())}


def main() -> int:
    with tempfile.TemporaryDirectory(prefix="protocol-dist-check-") as tmp:
        expected = Path(tmp) / "dist"
        build_skills.build(expected)

        expected_names = sorted(p.name for p in expected.iterdir() if p.is_file())
        committed_names = sorted(p.name for p in COMMITTED_DIST.iterdir() if p.is_file())
        if committed_names != expected_names:
            print("dist file set mismatch")
            print(f"expected:  {expected_names}")
            print(f"committed: {committed_names}")
            return 1

        for name in expected_names:
            exp = expected / name
            got = COMMITTED_DIST / name
            if name.endswith(".zip"):
                exp_tree = zip_contents(exp)
                got_tree = zip_contents(got)
                if got_tree != exp_tree:
                    print(f"semantic package mismatch: {name}")
                    exp_keys = set(exp_tree)
                    got_keys = set(got_tree)
                    for missing in sorted(exp_keys - got_keys):
                        print(f"  missing: {missing}")
                    for extra in sorted(got_keys - exp_keys):
                        print(f"  extra: {extra}")
                    for common in sorted(exp_keys & got_keys):
                        if exp_tree[common] != got_tree[common]:
                            print(f"  content differs: {common}")
                    return 1
            elif name.endswith(".json"):
                if json.loads(got.read_text(encoding="utf-8")) != json.loads(
                    exp.read_text(encoding="utf-8")
                ):
                    print(f"JSON distribution mismatch: {name}")
                    return 1
            elif got.read_bytes() != exp.read_bytes():
                print(f"distribution mismatch: {name}")
                return 1

    print("dist matches canonical source semantically")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
