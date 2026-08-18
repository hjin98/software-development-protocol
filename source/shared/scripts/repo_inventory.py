#!/usr/bin/env python3
"""Produce a lightweight, dependency-free repository inventory.

This script is a discovery aid for large repositories. It deliberately prunes
ignored trees before traversal so reconnaissance does not create unnecessary
metadata I/O in build, VCS, environment, or dependency directories. It does
not infer architecture or contract ownership; inspect authoritative source/docs
after use.
"""
from __future__ import annotations

import argparse
import json
import os
from collections import Counter
from pathlib import Path
from typing import Iterable, NamedTuple

IGNORE_DIRS = {
    ".git",
    ".hg",
    ".svn",
    ".mypy_cache",
    ".pytest_cache",
    ".ruff_cache",
    ".tox",
    ".venv",
    "venv",
    "node_modules",
    "__pycache__",
    "build",
    "dist",
}

MANIFEST_NAMES = {
    "pyproject.toml",
    "setup.py",
    "setup.cfg",
    "requirements.txt",
    "environment.yml",
    "environment.yaml",
    "package.json",
    "Cargo.toml",
    "go.mod",
    "CMakeLists.txt",
    "Makefile",
    "meson.build",
}


class FileRecord(NamedTuple):
    path: Path
    size: int


def walk_files(root: Path) -> Iterable[FileRecord]:
    """Yield regular non-symlink files while pruning ignored trees in-place."""
    for dirpath, dirnames, filenames in os.walk(root, topdown=True, followlinks=False):
        base = Path(dirpath)

        # Prune before os.walk descends. Filtering only after rglob discovery can
        # still traverse very large .git/node_modules/build trees and defeat the
        # purpose of a lightweight inventory.
        kept_dirs: list[str] = []
        for dirname in dirnames:
            if dirname in IGNORE_DIRS:
                continue
            child = base / dirname
            try:
                if child.is_symlink():
                    continue
            except OSError:
                continue
            kept_dirs.append(dirname)
        dirnames[:] = kept_dirs

        for filename in filenames:
            path = base / filename
            try:
                if path.is_symlink() or not path.is_file():
                    continue
                size = path.stat().st_size
            except OSError:
                # Inventory is best-effort discovery. Unreadable/racing files
                # should not abort repository reconnaissance.
                continue
            yield FileRecord(path=path, size=size)


def classify(path: Path, root: Path) -> str:
    rel = path.relative_to(root)
    parts = {part.lower() for part in rel.parts}
    name = path.name.lower()
    if "tests" in parts or "test" in parts or name.startswith("test_") or name.endswith("_test.py"):
        return "tests"
    if "benchmarks" in parts or "benchmark" in parts or "perf" in parts:
        return "benchmarks"
    if "docs" in parts or "doc" in parts or path.suffix.lower() in {".md", ".rst"}:
        return "docs"
    if ".github" in parts or "ci" in parts or name in {"jenkinsfile", ".gitlab-ci.yml"}:
        return "ci"
    return "other"


def inventory(root: Path, largest: int) -> dict[str, object]:
    records = list(walk_files(root))
    paths = [record.path for record in records]
    ext_counts = Counter((path.suffix.lower() or "<none>") for path in paths)
    category_counts = Counter(classify(path, root) for path in paths)
    top_dirs = Counter(
        (path.relative_to(root).parts[0] if len(path.relative_to(root).parts) > 1 else "<root>")
        for path in paths
    )
    manifests = sorted(
        str(path.relative_to(root))
        for path in paths
        if path.name in MANIFEST_NAMES
        or path.name.lower() in {"tox.ini", "pytest.ini", "ruff.toml", "mypy.ini"}
    )
    largest_files = [
        {"path": str(record.path.relative_to(root)), "bytes": record.size}
        for record in sorted(records, key=lambda record: record.size, reverse=True)[:largest]
    ]
    return {
        "root": str(root.resolve()),
        "file_count": len(records),
        "total_file_bytes": sum(record.size for record in records),
        "extension_counts": dict(ext_counts.most_common()),
        "category_counts": dict(category_counts.most_common()),
        "top_level_file_counts": dict(top_dirs.most_common()),
        "manifests_and_tooling": manifests,
        "largest_files": largest_files,
    }


def render_text(data: dict[str, object]) -> str:
    lines = [
        f"Repository: {data['root']}",
        f"Files: {data['file_count']}",
        f"Total bytes (scanned files): {data['total_file_bytes']}",
    ]
    for key, title in (
        ("category_counts", "Categories"),
        ("top_level_file_counts", "Top-level file counts"),
        ("extension_counts", "Extensions"),
    ):
        lines.append(f"\n{title}:")
        for name, count in data[key].items():  # type: ignore[union-attr]
            lines.append(f"  {name}: {count}")
    lines.append("\nManifests/tooling:")
    for item in data["manifests_and_tooling"]:  # type: ignore[union-attr]
        lines.append(f"  {item}")
    lines.append("\nLargest files:")
    for item in data["largest_files"]:  # type: ignore[union-attr]
        lines.append(f"  {item['bytes']:>10}  {item['path']}")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repo", nargs="?", default=".", help="repository root")
    parser.add_argument("--largest", type=int, default=20, help="number of largest files")
    parser.add_argument("--json", action="store_true", help="emit JSON")
    args = parser.parse_args()

    root = Path(args.repo).expanduser().resolve()
    if not root.is_dir():
        parser.error(f"not a directory: {root}")
    if args.largest < 0:
        parser.error("--largest must be nonnegative")

    data = inventory(root, args.largest)
    if args.json:
        print(json.dumps(data, indent=2, sort_keys=True))
    else:
        print(render_text(data))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
