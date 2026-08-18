# Repository Intake and Large-Codebase Change Control

## Goal

Build enough authoritative context to make a safe change without loading or rewriting the entire repository.

## Intake sequence

1. Discover and read applicable repository/agent instructions first, including project-native files such as `AGENTS.md`, `CLAUDE.md`, and equivalent scoped instruction files. Re-evaluate when crossing directory boundaries.
2. Identify project manifests, language/toolchain versions, dependency files, build configuration, CI workflows, test configuration, format/lint/type-check settings, packaging/release files, and generated-code rules.
3. Map the target subsystem by following imports/callers/data flow rather than by scanning every file indiscriminately.
4. Find the owning specification/manual for affected public behavior and the tests/benchmarks that encode current behavior.
5. Inspect recent or adjacent implementations for local conventions before introducing a new pattern.
6. Establish repository state before editing. Preserve unrelated user changes and do not use destructive reset/checkout operations to simplify the task.

Use `scripts/repo_inventory.py <repo>` for a fast static inventory, but treat it as discovery only.

## Change-surface map

For a substantial change, record a compact map:

| Surface | Questions |
|---|---|
| Public API | Which imports, functions, classes, CLI flags, config keys, or protocols are externally visible? |
| Data contract | Which types, shapes, units, schemas, ordering rules, file formats, or persisted records can change? |
| Callers | Which modules and external entry points consume the behavior? |
| Tests | Which focused tests are the primary oracle? Which integration tests prove consumer behavior? |
| Docs | Which specification/manual/user guide owns the behavior? Which files are generated? |
| Performance | Is the path hot? Are there baselines, benchmarks, or resource budgets? |
| Storage/state | Which inputs/outputs/caches/checkpoints/scratch artifacts exist? What are their sizes, validity, retention, and recovery roles? |
| Security/trust | Which external/untrusted files, archives, deserializers, subprocesses, plugins, networks, credentials, renderers, or dependency installers cross a trust boundary? What capabilities do they receive? |
| Documentation/version | Which current specification must match accepted code? Does accepted architecture actually change? Which history/version record changes? Which permanent Markdown PDFs/provenance manifests must be regenerated? Is there an active workplan governing execution? |
| Release | Does the change affect packaging, migrations, compatibility, wheels, examples, or installed behavior? |

Do not start broad implementation until the major rows are known or explicitly marked unknown.

## Large-repository tactics

- Start from the user's requested symbol/module/feature and expand one dependency layer at a time.
- Search for definitions, imports, registrations, serialization keys, cache/checkpoint/journal paths, CLI names, test references, and documentation ownership.
- Prefer targeted excerpts over loading huge files wholesale; inspect function/class boundaries and relevant surrounding state.
- Identify "god" or orchestration modules, but do not automatically split them during unrelated work. Separate them only when the requested change benefits and tests can protect the split.
- Distinguish current architecture/specifications from implementation workplans, historical notes, audits, benchmarks, examples, generated output, and stale duplicates. Task-local implementation status belongs in the workplan, not current architecture/specification prose.
- Treat machine-readable dependency graphs, schemas, registries, and generated manuals as first-class current architecture/contract artifacts when present. Keep task-local gate/status state in the implementation workplan unless the project explicitly defines it as a runtime/product state machine.
- Keep a list of touched and intentionally untouched surfaces; use it to detect accidental scope growth at diff review.

## Dependency and ownership rules

- Preserve established dependency direction unless the architecture explicitly changes it.
- Put policy at stable boundaries rather than duplicating it across consumers.
- Keep scientific/business semantics separate from execution backends when multiple backends must remain equivalent.
- Keep I/O normalization at boundaries so downstream code operates on canonical internal representations where feasible. Classify persisted artifacts by ownership/lifecycle instead of treating all files as equivalent outputs.
- Prefer one authoritative current contract owner. Let workplans/history/guides summarize and link rather than fork the same architecture/specification.

## Generated artifacts

Before editing a file, determine whether it is source or generated.

- Edit the source of truth, then run the generator.
- Do not hand-edit generated Markdown, JSON, code, lock data, or PDFs unless repository policy declares them authoritative. Permanent engineering docs governed by this protocol are authored in Markdown; regenerate their PDFs after Markdown edits.
- Verify deterministic generation when reproducibility is part of the contract.
- If generation cannot run, report the generated artifact as stale/blocked; do not fake parity.

## Repository state safety

- Do not delete, revert, overwrite, or reformat unrelated user changes.
- Avoid mass formatting unless explicitly requested or required by the repository.
- Do not change dependency versions merely to make local tooling convenient.
- Do not commit secrets, machine-specific absolute paths, large transient outputs, caches, or benchmark noise.
- Prefer isolated temporary/evidence directories already sanctioned by the project. For large workflows, identify scratch/quota constraints and existing cache/checkpoint locations during intake rather than after allocation fails.
