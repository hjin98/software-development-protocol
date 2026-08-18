#!/usr/bin/env python3
"""Render authoritative Markdown documentation to sibling PDFs with provenance.

Default pipeline: Pandoc -> Typst -> PDF.

Markdown remains the source of truth. Each rendered PDF is accompanied by
``<document>.pdf.manifest.json`` binding the exact Markdown SHA-256, PDF
SHA-256, render-policy/configuration identity, and renderer tool versions.
``--check`` validates content provenance rather than filesystem timestamps.

This helper intentionally does not enable arbitrary Pandoc filters, custom
writers, shell execution, or remote templates. It is intended for trusted
project documentation. Render untrusted documents only in an appropriately
isolated environment.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any
from urllib.parse import unquote, urlsplit

MANIFEST_SCHEMA_VERSION = 1
RENDER_POLICY_VERSION = "pandoc-typst-v2"
RENDER_CONFIG: dict[str, Any] = {
    "from": "markdown",
    "pdf_engine": "typst",
    "papersize": "us-letter",
    "margin": "0.75in",
    "fontsize": "10.5pt",
    "lang": "en-US",
    "resource_path": "source-parent",
    "resource_provenance": "pandoc-image-ast-local-files-v1",
    "remote_images": "reject",
    "absolute_images": "reject",
}


def _canonical_json_bytes(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def _sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _render_config_identity() -> str:
    payload = {
        "policy_version": RENDER_POLICY_VERSION,
        "config": RENDER_CONFIG,
    }
    return _sha256_bytes(_canonical_json_bytes(payload))


def _manifest_path(pdf: Path) -> Path:
    return Path(str(pdf) + ".manifest.json")


def _require_tool(name: str, installation_hint: str) -> str:
    path = shutil.which(name)
    if path is None:
        raise SystemExit(
            f"required documentation tool '{name}' was not found in PATH. "
            f"{installation_hint}"
        )
    return path


def _tool_version(executable: str) -> str:
    try:
        result = subprocess.run(
            [executable, "--version"],
            check=True,
            capture_output=True,
            text=True,
        )
    except (OSError, subprocess.CalledProcessError) as exc:
        raise RuntimeError(f"could not query renderer version for {executable}: {exc}") from exc
    lines = (result.stdout or result.stderr).strip().splitlines()
    return lines[0].strip() if lines else "unknown"



def _discover_local_resources(source: Path, pandoc: str) -> list[dict[str, str]]:
    """Return directly referenced local Markdown image resources and digests.

    Pandoc's JSON AST is used so ordinary Markdown image syntax is interpreted
    consistently with the renderer. Remote and absolute image dependencies are
    rejected by the default reproducible/offline policy. Raw HTML <img> is
    rejected because its resource semantics are not tracked by this helper.
    """
    result = subprocess.run(
        [pandoc, str(source), "--from=markdown", "--to=json"],
        cwd=source.parent,
        check=True,
        capture_output=True,
        text=True,
    )
    try:
        ast = json.loads(result.stdout)
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"could not parse Pandoc JSON AST for {source}: {exc}") from exc

    targets: set[str] = set()

    def visit(node: Any) -> None:
        if isinstance(node, dict):
            if node.get("t") == "Image":
                c = node.get("c")
                if isinstance(c, list) and len(c) >= 3 and isinstance(c[2], list) and c[2]:
                    target = c[2][0]
                    if isinstance(target, str):
                        targets.add(target)
            if node.get("t") in {"RawInline", "RawBlock"}:
                c = node.get("c")
                if isinstance(c, list) and len(c) >= 2 and isinstance(c[1], str) and "<img" in c[1].lower():
                    raise RuntimeError(
                        f"raw HTML <img> resource is not provenance-tracked in {source}; "
                        "use Markdown image syntax or a repository renderer with equivalent dependency tracking"
                    )
            for value in node.values():
                visit(value)
        elif isinstance(node, list):
            for value in node:
                visit(value)

    visit(ast)

    resources: list[dict[str, str]] = []
    for target in sorted(targets):
        parsed = urlsplit(target)
        scheme = parsed.scheme.lower()
        if scheme in {"http", "https", "ftp"} or target.startswith("//"):
            raise RuntimeError(f"remote image resources are disabled by default: {target}")
        if scheme == "data":
            # Data URI content is already embedded in the Markdown source bytes.
            continue
        if scheme not in {"", "file"}:
            raise RuntimeError(f"unsupported image resource scheme '{scheme}' in {target}")
        if scheme == "file":
            raise RuntimeError(f"file:// image resources are non-portable and disabled: {target}")
        if parsed.query:
            raise RuntimeError(f"query-bearing local image resource is unsupported: {target}")

        raw_path = unquote(parsed.path)
        candidate = Path(raw_path)
        if candidate.is_absolute():
            raise RuntimeError(f"absolute image resources are non-portable and disabled: {target}")
        resolved = (source.parent / candidate).resolve()
        if not resolved.is_file():
            raise RuntimeError(f"referenced local image resource does not exist: {target}")
        resources.append({
            "path": candidate.as_posix(),
            "sha256": _sha256_file(resolved),
        })
    return resources

def _collect(paths: list[Path], recursive: bool) -> list[Path]:
    found: set[Path] = set()
    for raw in paths:
        path = raw.expanduser().resolve()
        if path.is_file():
            if path.suffix.lower() != ".md":
                raise SystemExit(f"not a Markdown file: {path}")
            found.add(path)
            continue
        if path.is_dir():
            iterator = path.rglob("*.md") if recursive else path.glob("*.md")
            for candidate in iterator:
                if candidate.is_file():
                    found.add(candidate.resolve())
            continue
        raise SystemExit(f"path does not exist: {path}")
    return sorted(found)


def _pdf_is_structurally_present(path: Path) -> bool:
    try:
        if not path.is_file() or path.stat().st_size < 5:
            return False
        with path.open("rb") as handle:
            return handle.read(5) == b"%PDF-"
    except OSError:
        return False


def _load_manifest(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ValueError(f"missing provenance manifest: {path}") from exc
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"invalid provenance manifest {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise ValueError(f"invalid provenance manifest root in {path}: expected object")
    return value


def _check_provenance(source: Path) -> tuple[bool, str]:
    output = source.with_suffix(".pdf")
    manifest_path = _manifest_path(output)
    if not _pdf_is_structurally_present(output):
        return False, f"missing/invalid PDF: {output}"

    try:
        manifest = _load_manifest(manifest_path)
        if manifest.get("schema_version") != MANIFEST_SCHEMA_VERSION:
            return False, f"unsupported/stale manifest schema: {manifest_path}"

        source_record = manifest.get("source")
        pdf_record = manifest.get("pdf")
        renderer_record = manifest.get("renderer")
        if not isinstance(source_record, dict) or not isinstance(pdf_record, dict) or not isinstance(renderer_record, dict):
            return False, f"incomplete provenance manifest: {manifest_path}"

        if source_record.get("name") != source.name:
            return False, f"manifest source name mismatch: {manifest_path}"
        if pdf_record.get("name") != output.name:
            return False, f"manifest PDF name mismatch: {manifest_path}"

        actual_source_sha = _sha256_file(source)
        if source_record.get("sha256") != actual_source_sha:
            return False, f"PDF provenance does not match current Markdown content: {output}"

        actual_pdf_sha = _sha256_file(output)
        if pdf_record.get("sha256") != actual_pdf_sha:
            return False, f"PDF digest does not match provenance manifest: {output}"

        if renderer_record.get("policy_version") != RENDER_POLICY_VERSION:
            return False, f"PDF was produced under an older/different render policy: {output}"
        if renderer_record.get("config_sha256") != _render_config_identity():
            return False, f"PDF render configuration is stale/different: {output}"

        if not renderer_record.get("pandoc_version") or not renderer_record.get("typst_version"):
            return False, f"renderer tool versions missing from provenance manifest: {manifest_path}"

        resources = manifest.get("resources", [])
        if not isinstance(resources, list):
            return False, f"invalid resource provenance list: {manifest_path}"
        for record in resources:
            if not isinstance(record, dict) or not isinstance(record.get("path"), str) or not isinstance(record.get("sha256"), str):
                return False, f"invalid resource provenance entry: {manifest_path}"
            resource_path = Path(record["path"])
            if resource_path.is_absolute():
                return False, f"absolute resource path in provenance manifest: {manifest_path}"
            resolved = (source.parent / resource_path).resolve()
            if not resolved.is_file():
                return False, f"missing documented resource dependency: {record['path']}"
            if _sha256_file(resolved) != record["sha256"]:
                return False, f"document resource provenance changed: {record['path']}"
    except (OSError, ValueError) as exc:
        return False, str(exc)

    return True, f"content provenance verified: {output}"


def _write_json_atomic(path: Path, value: dict[str, Any]) -> None:
    payload = json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    fd, tmp_name = tempfile.mkstemp(prefix=f".{path.name}.", suffix=".tmp", dir=path.parent)
    tmp = Path(tmp_name)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            handle.write(payload)
            handle.flush()
            os.fsync(handle.fileno())
        tmp.replace(path)
    except BaseException:
        tmp.unlink(missing_ok=True)
        raise


def _render(source: Path, pandoc: str, typst: str, pandoc_version: str, typst_version: str) -> Path:
    output = source.with_suffix(".pdf")
    manifest_path = _manifest_path(output)
    output.parent.mkdir(parents=True, exist_ok=True)

    # Publish only a complete renderer result. The PDF is atomically moved into
    # place, then its matching manifest is atomically published. If a process
    # dies between those operations, --check rejects the unmatched pair.
    with tempfile.NamedTemporaryFile(
        prefix=f".{output.stem}.", suffix=".pdf", dir=output.parent, delete=False
    ) as handle:
        tmp_pdf = Path(handle.name)

    cmd = [
        pandoc,
        str(source),
        "--from=markdown",
        "--pdf-engine",
        typst,
        "--variable",
        f"papersize={RENDER_CONFIG['papersize']}",
        "--variable",
        f"margin={RENDER_CONFIG['margin']}",
        "--variable",
        f"fontsize={RENDER_CONFIG['fontsize']}",
        "--metadata",
        f"lang={RENDER_CONFIG['lang']}",
        "--resource-path",
        str(source.parent),
        "-o",
        str(tmp_pdf),
    ]

    try:
        subprocess.run(cmd, cwd=source.parent, check=True)
        if not _pdf_is_structurally_present(tmp_pdf):
            raise RuntimeError(f"renderer did not produce a valid PDF header for {source}")

        source_sha = _sha256_file(source)
        pdf_sha = _sha256_file(tmp_pdf)
        resources = _discover_local_resources(source, pandoc)
        manifest: dict[str, Any] = {
            "schema_version": MANIFEST_SCHEMA_VERSION,
            "source": {
                "name": source.name,
                "sha256": source_sha,
            },
            "pdf": {
                "name": output.name,
                "sha256": pdf_sha,
            },
            "resources": resources,
            "renderer": {
                "driver": "render_markdown_pdfs.py",
                "policy_version": RENDER_POLICY_VERSION,
                "config": RENDER_CONFIG,
                "config_sha256": _render_config_identity(),
                "pandoc_version": pandoc_version,
                "typst_version": typst_version,
            },
        }

        tmp_pdf.replace(output)
        _write_json_atomic(manifest_path, manifest)
    except BaseException:
        tmp_pdf.unlink(missing_ok=True)
        raise

    return output


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Render authoritative Markdown docs to sibling PDFs using Pandoc + Typst with SHA-256 provenance."
    )
    parser.add_argument("paths", nargs="+", type=Path, help="Markdown file(s) or documentation directories")
    parser.add_argument(
        "--recursive",
        action="store_true",
        help="recurse through supplied directories for *.md files",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="do not render; fail unless PDF+manifest match the exact Markdown content and render policy",
    )
    args = parser.parse_args()

    sources = _collect(args.paths, args.recursive)
    if not sources:
        raise SystemExit("no Markdown files found")

    if args.check:
        failures = 0
        for source in sources:
            ok, message = _check_provenance(source)
            if ok:
                print(f"[PASS] {source}: {message}")
            else:
                failures += 1
                print(f"[FAIL] {source}: {message}", file=sys.stderr)
        return 1 if failures else 0

    pandoc = _require_tool(
        "pandoc",
        "Install Pandoc from the Linux distribution package manager or the official Pandoc package.",
    )
    typst = _require_tool(
        "typst",
        "Install the 'typst' package where available, use the Ubuntu Snap, or run "
        "'cargo install --locked typst-cli' with an up-to-date Rust toolchain.",
    )
    pandoc_version = _tool_version(pandoc)
    typst_version = _tool_version(typst)

    failures = 0
    for source in sources:
        try:
            output = _render(source, pandoc, typst, pandoc_version, typst_version)
            print(f"[PASS] {source} -> {output} + {_manifest_path(output)}")
        except subprocess.CalledProcessError as exc:
            failures += 1
            print(f"[FAIL] {source}: renderer exited with {exc.returncode}", file=sys.stderr)
        except Exception as exc:  # noqa: BLE001 - per-document batch reporting
            failures += 1
            print(f"[FAIL] {source}: {exc}", file=sys.stderr)

    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
