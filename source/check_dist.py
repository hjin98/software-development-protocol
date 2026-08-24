#!/usr/bin/env python3
"""Compare a fresh protocol build with the committed distribution semantically."""

from __future__ import annotations

import argparse
import json
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def zip_contents(path: Path) -> dict[str, bytes]:
    with zipfile.ZipFile(path, "r") as zf:
        return {name: zf.read(name) for name in sorted(zf.namelist())}


def compare(expected: Path, committed: Path) -> list[str]:
    errors: list[str] = []
    if not expected.is_dir():
        return [f"expected distribution directory is missing: {expected}"]
    if not committed.is_dir():
        return [f"committed distribution directory is missing: {committed}"]

    expected_names = sorted(p.name for p in expected.iterdir() if p.is_file())
    committed_names = sorted(p.name for p in committed.iterdir() if p.is_file())
    if committed_names != expected_names:
        errors.append(
            "dist file set mismatch: "
            f"expected={expected_names} committed={committed_names}"
        )
        return errors

    for name in expected_names:
        exp = expected / name
        got = committed / name
        if name.endswith(".zip"):
            try:
                exp_tree = zip_contents(exp)
                got_tree = zip_contents(got)
            except (OSError, zipfile.BadZipFile) as exc:
                errors.append(f"invalid ZIP while comparing {name}: {exc}")
                continue
            if got_tree != exp_tree:
                exp_keys = set(exp_tree)
                got_keys = set(got_tree)
                detail: list[str] = []
                detail.extend(f"missing {item}" for item in sorted(exp_keys - got_keys))
                detail.extend(f"extra {item}" for item in sorted(got_keys - exp_keys))
                detail.extend(
                    f"content differs {item}"
                    for item in sorted(exp_keys & got_keys)
                    if exp_tree[item] != got_tree[item]
                )
                errors.append(f"semantic package mismatch: {name}: " + "; ".join(detail))
        elif name.endswith(".json"):
            try:
                exp_json = json.loads(exp.read_text(encoding="utf-8"))
                got_json = json.loads(got.read_text(encoding="utf-8"))
            except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
                errors.append(f"invalid JSON while comparing {name}: {exc}")
                continue
            if got_json != exp_json:
                errors.append(f"JSON distribution mismatch: {name}")
        else:
            try:
                if got.read_bytes() != exp.read_bytes():
                    errors.append(f"distribution mismatch: {name}")
            except OSError as exc:
                errors.append(f"failed to compare {name}: {exc}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--expected", type=Path, required=True)
    parser.add_argument("--committed", type=Path, default=ROOT / "dist")
    args = parser.parse_args()

    errors = compare(args.expected.resolve(), args.committed.resolve())
    if errors:
        for error in errors:
            print(error)
        return 1
    print("committed dist matches the fresh canonical build semantically")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
