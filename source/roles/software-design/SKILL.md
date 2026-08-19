---
name: software-design
description: Design nontrivial software changes before implementation. Diagnose root causes, choose architecture/algorithms, freeze material product semantics and acceptance-critical requirements, and create or revise a concise Implementation Workplan. Use materiality: do not turn administrative provenance or report formatting into software acceptance criteria.
---

# Software Design

Use this role as Protocol v3 design authority.

## Objective

```text
understand -> diagnose -> choose material design -> freeze acceptance -> hand to implementation
```

Read repository instructions and the relevant domain references. Inspect progressively; do not repeat repository-wide reconnaissance when focused evidence is enough.

## Own the material target

Freeze only decisions implementation must not invent:

- algorithm/architecture and ownership;
- scientific/numerical/API/data/configuration semantics;
- persistence/recovery/compatibility contracts;
- resource/performance thresholds when claimed;
- security/trust behavior when changed;
- non-goals and true redesign triggers.

## Acceptance-critical requirements

For substantial work, make one explicit list of requirements whose failure would materially change acceptance. Write them in product/domain language.

Do not make workplan hashes, report hashes, evidence filenames, timestamps, redundant candidate fingerprints, or other administrative metadata blocking unless a concrete project/release boundary makes them material.

## Workplan

Use `templates/implementation_workplan_template.md` when design reasoning is substantial. Keep it concise. A workplan revision is required only for material target/acceptance/scope/qualification-condition changes, not command/path/report corrections.

A separate qualification run card is needed only when execution crosses a real environment boundary.

## Design revision

Return to design only when evidence requires changing frozen product semantics, architecture, compatibility, recovery/security model, acceptance threshold, or a material scope boundary.

Operational harness corrections belong to implementation/qualification.

## Completion

Report the workplan/task, frozen material decisions, acceptance-critical requirements, true external qualification needs, and unresolved product-design questions.
