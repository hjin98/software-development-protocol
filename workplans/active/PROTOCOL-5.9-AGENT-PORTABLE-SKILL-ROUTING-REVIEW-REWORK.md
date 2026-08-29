---
kind: implementation-workplan-amendment
workplan_id: PROTOCOL-5.9-AGENT-PORTABLE-SKILL-ROUTING-REVIEW-REWORK
amends_workplan_id: PROTOCOL-5.9-AGENT-PORTABLE-SKILL-ROUTING
protocol_version: 5.8.0
target_protocol_version: 5.9.0
status: active
created_date: 2026-08-29
review_source: independent-software-design-review
---

# Protocol 5.9 Routing Workplan — Independent Review Rework Amendment

This amendment closes the two blocking implementation nonconformances found during independent Software Design review of the Protocol 5.9 candidate. It does not reopen the accepted routing/distribution architecture or the doctrine/content freeze. The governing hierarchy remains exactly:

```text
product engineering fitness > minimum justified product/system complexity > development economy
```

All Protocol 5.4-5.8 hardening remains frozen. Rework is limited to validator correctness/evidence and stale workplan lifecycle state.

## R1 — Validate Agent Skills frontmatter semantically, not by tolerant text scanning

### Concern

The candidate validator recognizes top-level frontmatter keys but does not actually parse YAML semantics. Indented `metadata` content is ignored, so malformed or type-invalid optional fields can falsely pass while CI claims portable Agent Skills validation.

### Required end state

`source/validate_packages.py` must parse frontmatter with a real YAML parser and validate the supported Agent Skills field contract on the parsed object.

At minimum:

- frontmatter must parse as one mapping;
- top-level keys must be strings and limited to the supported standard keys;
- `name` and `description` remain required strings with the existing portable name/length rules;
- `license`, when present, must be a string;
- `compatibility`, when present, must be a non-empty string no longer than 500 characters;
- `metadata`, when present, must be a mapping whose keys and values are strings;
- `allowed-tools`, when present, must be a non-empty scalar string rather than a YAML sequence/mapping;
- malformed YAML or type-invalid standard fields must fail validation rather than being skipped.

A small validation dependency is justified because semantic YAML parsing is the owning mechanism; do not replace it with another ad-hoc indentation scanner. Keep the dependency scoped to repository validation tooling and install it explicitly in the documented/CI acceptance path.

### Acceptance evidence

Add positive/negative regression cases covering valid nested metadata plus malformed YAML, invalid `compatibility` type/length, non-string metadata keys/values, and non-string `allowed-tools`.

## R2 — Reject unsafe or escaped bundled-resource routes

### Concern

The candidate recognizes only already-safe `references/<file>.md` and `templates/<file>.md` patterns. A traversal/escaped resource-like Markdown link can fall outside the regex and therefore be ignored rather than rejected.

### Required end state

Validation must inspect actual Markdown link targets. Any link attempting to address the packaged `references` or `templates` namespace must use exactly the supported one-level relative form:

```text
references/<safe-name>.md
templates/<safe-name>.md
```

Reject absolute paths, `..` traversal, backslash variants, deeper paths, fragments/query-decorated resource paths, or other resource-like escape forms. Continue requiring every packaged Markdown reference/template to have a direct valid link from `SKILL.md`, and continue rejecting validly shaped links whose target is not packaged.

### Acceptance evidence

Add negative fixtures for at least `references/../outside.md`, `../references/outside.md`, and a backslash resource path. Existing broken-route and packaged-but-unlinked tests must remain green.

## R3 — Close stale Protocol 5.8 workplan lifecycle state

### Concern

`workplans/active/PROTOCOL-5.8-EFFECTIVE-COMPRESSION.md` still declares itself active even though Protocol 5.8 was released and its own terminal gate required archival. This leaves an unnecessary competing lifecycle state in a repository whose files are consumed by agents.

### Required end state

Move the Protocol 5.8 workplan to `workplans/archive/PROTOCOL-5.8-EFFECTIVE-COMPRESSION.md`, mark it completed, and record the completed date. Do not rewrite its historical design content.

### Acceptance evidence

- no Protocol 5.8 effective-compression workplan remains under `workplans/active/`;
- the archived file preserves the historical workplan body with only lifecycle metadata changed;
- active workplans after rework are only the still-open Protocol 5.9 routing workplan and its amendments.

## Required final acceptance

After R1-R3 are implemented:

1. run the complete unit/regression suite;
2. build all canonical skill bundles;
3. independently validate all generated directory and ZIP bundles;
4. verify committed `dist` parity against the fresh build;
5. run `git diff --check`;
6. independently re-check doctrine/content preservation and confirm no Protocol 5.4-5.8 semantic safeguard changed;
7. keep live external harness qualification explicitly unqualified unless actually executed.

The expected rework outcome is the same Protocol 5.9 design with stronger truthful validation evidence and correct repository lifecycle state, not a broader protocol revision.
