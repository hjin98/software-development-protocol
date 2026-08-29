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
        return {name: zf.read(name) for name in sorted(zf.namelist()) if not name.endswith("/")}


def relative_files(root: Path) -> dict[str, Path]:
    return {
        path.relative_to(root).as_posix(): path
        for path in sorted(p for p in root.rglob("*") if p.is_file())
    }


def compare(expected: Path, committed: Path) -> list[str]:
    errors: list[str] = []
    if not expected.is_dir():
        return [f"expected distribution directory is missing: {expected}"]
    if not committed.is_dir():
        return [f"committed distribution directory is missing: {committed}"]

    exp_files = relative_files(expected)
    got_files = relative_files(committed)
    if set(exp_files) != set(got_files):
        return [
            "dist recursive file set mismatch: "
            f"missing={sorted(set(exp_files) - set(got_files))} "
            f"extra={sorted(set(got_files) - set(exp_files))}"
        ]

    for rel in sorted(exp_files):
        exp = exp_files[rel]
        got = got_files[rel]
        if rel.endswith(".zip"):
            try:
                exp_tree = zip_contents(exp)
                got_tree = zip_contents(got)
            except (OSError, zipfile.BadZipFile) as exc:
                errors.append(f"invalid ZIP while comparing {rel}: {exc}")
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
                errors.append(f"semantic package mismatch: {rel}: " + "; ".join(detail))
        elif rel.endswith(".json"):
            try:
                if json.loads(got.read_text(encoding="utf-8")) != json.loads(exp.read_text(encoding="utf-8")):
                    errors.append(f"JSON distribution mismatch: {rel}")
            except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
                errors.append(f"invalid JSON while comparing {rel}: {exc}")
        else:
            try:
                if got.read_bytes() != exp.read_bytes():
                    errors.append(f"distribution mismatch: {rel}")
            except OSError as exc:
                errors.append(f"failed to compare {rel}: {exc}")
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
