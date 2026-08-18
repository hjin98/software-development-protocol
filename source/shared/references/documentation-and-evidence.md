# Engineering Documentation, Versioning, and Evidence

Documentation is part of the implementation contract. A code change is not complete while its owning specification, accepted architecture, version/history record, required generated PDF, or PDF provenance manifest still describes a previous accepted system/source revision.

## Document roles and authority

Keep artifact types distinct:

- **Architecture manual** - accepted current architecture: theory/context, ownership, dependency direction, components, invariants, current data/control flow, persistence/resource/security boundaries, and accepted design rationale.
- **Specification** - normative description of behavior the current accepted code base actually implements: data/API/file/CLI contracts, errors, compatibility, persistence, numerical conventions, and acceptance semantics.
- **Implementation Workplan** - temporary execution contract for a proposed transition: diagnosis, frozen design, non-goals, implementation gates, acceptance criteria, handoff revision/base commit, and execution status. Workplans are not product documentation and are normally Markdown-only.
- **User/API guide/runbook** - how to use or operate stable implemented behavior.
- **Benchmark report** - reproducible performance/resource measurements and environment.
- **Audit/qualification report** - evidence that a specific requirement/gate/release passed, failed, or was blocked.
- **History/changelog/release note** - chronological record of completed changes/version transitions; non-normative for current behavior.
- **Proposal/research note** - optional exploratory material before a design is accepted. A proposal must not masquerade as an accepted architecture or implementation workplan.

Assign one normative owner for each current contract. Cross-reference rather than duplicating architecture, workplans, specifications, or history into competing documents.

## Current-state rule

Use this separation consistently:

```text
accepted current structure -> architecture manual
accepted current behavior -> specification
proposed transition + execution gates -> implementation workplan
correctness/performance evidence -> audit/benchmark/evidence artifacts
completed chronology -> history/changelog/release notes
```

Do not put task-local gate tables, "next stage" statements, implementation status, or version-by-version chronology in architecture manuals. Do not put unimplemented future contracts in current normative specifications. Future target behavior belongs in the active workplan until it is implemented and accepted.

## Specification-code parity is mandatory

The owning specification must describe the **real accepted implemented behavior of the current code base**.

When implementation changes a specified API, schema, default, algorithmic contract, numerical convention, error/fallback behavior, persistence format, resource policy, or compatibility promise:

1. update the specification during implementation closeout;
2. compare final signatures/defaults/types/units/error behavior directly against code;
3. revise tests/examples that encode the old contract;
4. update compatibility/deprecation/migration text where needed;
5. do not mark the workplan complete while code and specification disagree.

If an implementation legitimately diverges from the target described in the workplan, the design/review role must first accept a revised workplan or explicitly approve the changed target. Do not mutate the normative specification early to make an unfinished implementation appear accepted.

Historical documents never excuse a stale current specification.

## Architecture-current-state parity

Update a permanent architecture manual only when the **accepted implemented architecture** actually changes.

Examples that justify an architecture update include:

- ownership or dependency-direction changes;
- introduction/removal of an architectural component or backend boundary;
- accepted algorithm/data-flow/persistence/concurrency/security architecture changes;
- durable extension-point or unsupported-regime changes.

Examples that normally do **not** justify an architecture edit include:

- a gate starting or finishing;
- a bug fix within the existing architecture;
- a benchmark run;
- a temporary optimization experiment;
- a version bump with no architectural effect;
- "the next gate is ..." project-management state.

If implementation changes the accepted architecture relative to the workplan target, reconcile the design first, then describe the accepted result in the architecture manual during closeout.

## Workplan documentation policy

Implementation Workplans are intentionally different from permanent engineering documentation:

- keep them concise and link to authoritative files/evidence;
- record `workplan_id`, `plan_revision`, lifecycle status, analyzed base ref/commit, frozen decisions, gates, and evidence references;
- do not copy large logs, diffs, source files, or architecture manuals into them;
- normally store them under a repository coordination location such as `workplans/`;
- normally exclude them from user/runtime distributions;
- **do not require PDF generation for workplans** unless a project explicitly chooses otherwise;
- archive only materially useful completed workplans; mundane completed plans may be deleted after closeout because Git/history retains the transition.

See `workplans-and-agent-handoff.md` for the authority/lifecycle contract.

## Historical records and completed work

History/changelog documents preserve chronological truth while remaining non-normative.

For completed changes/releases, record as appropriate:

- date/version;
- feature/workplan/release identifier when useful;
- concise behavior/contract/architecture changes;
- migrations/deprecations;
- important performance/storage/security changes;
- qualification status and important limitations;
- superseded decisions where future readers could otherwise misinterpret older material.

If a historical artifact preserves an old staged plan, retain the distinction between stages that were only proposed, actually completed, deferred, cancelled, or superseded. Do not rewrite history to imply that an abandoned design shipped.

Prefer append/correct-with-note semantics for true historical records. Let version control carry trivial editorial evolution rather than manufacturing permanent revision documents for every plan iteration.

## Version governance

Follow the repository's established versioning scheme. Do not impose a new scheme without an explicit design/release decision.

For a versioned project:

- identify the authoritative version source before editing;
- avoid independently editing duplicated version strings when one should be generated;
- bump project/package versions at the lifecycle point required by repository policy;
- record completed release-bearing changes in history/changelog/release notes;
- update user-visible version output, package metadata, generated docs, schemas/cache/model/protocol versions, and compatibility notes when those have independent version fields;
- distinguish **package/release version** from **schema/cache/model/protocol/workplan version**.

A version bump is not acceptance evidence. Conversely, accepted release-bearing changes must not disappear from version history merely because code is already merged.

## Writing standards

- Author permanent engineering documents in Markdown (`.md`) as the editable source of truth.
- Write terse, precise prose aimed at human maintainers and code agents.
- State conventions before formulas/algorithms that depend on them.
- Use LaTeX math in Markdown for equations where appropriate.
- Include pseudocode/flow diagrams only when they clarify control/data flow beyond prose and code.
- Define types, units, shapes, ranges, ordering, and edge cases for data contracts.
- Explain motive and tradeoffs for non-obvious accepted design decisions.
- Keep prospective implementation details in workplans rather than current architecture/specification documents.
- Avoid stale future tense, task status, and chronology in normative current-state documentation.

## Mandatory Markdown-to-PDF synchronization

For **permanent engineering documents** governed by this protocol (architecture manuals, specifications, substantive user/API manuals, audits, benchmark reports, and history/release documents), Markdown is authoritative and a PDF rendering must be regenerated whenever the Markdown content changes.

Implementation Workplans and other explicitly temporary coordination artifacts are exempt by default.

Default permanent-document policy:

1. edit/create `<document>.md` only as the source;
2. render `<document>.pdf` from that exact Markdown in the same accepted change;
3. generate `<document>.pdf.manifest.json` binding the Markdown SHA-256, PDF SHA-256, directly referenced local image-resource digests, render-policy/configuration identity, and Pandoc/Typst versions;
4. never hand-edit the PDF or generated provenance manifest;
5. verify the PDF exists, opens, contains the expected title/version/headings, and is not visibly clipped/broken;
6. keep the `.md`, `.pdf`, and provenance manifest together or according to the repository's established generated-artifact layout;
7. if generated binaries are intentionally untracked, still build/verify the PDF+manifest as release/documentation artifacts and record that policy;
8. do not report documentation complete while required PDF/provenance is missing, digest-mismatched, or built under a stale render-policy identity.

Do **not** use modification timestamps as proof of source/PDF parity. Copying, archive extraction, Git operations, and `touch` can make stale outputs look newer than their sources. Content identity is the default evidence.

The default lightweight Linux toolchain for projects without an existing renderer is:

```bash
pandoc <document>.md \
  --from=markdown \
  --pdf-engine=typst \
  -V papersize=us-letter \
  -V margin=0.75in \
  -o <document>.pdf
```

Prefer the repository's existing renderer when it already provides equivalent or stronger behavior. Otherwise use `scripts/render_markdown_pdfs.py` from the implementation skill. It renders with Pandoc + Typst and publishes the PDF together with a content-provenance manifest.

For a cheap CI/preflight parity check after rendering:

```bash
python scripts/render_markdown_pdfs.py --check docs/spec.md docs/architecture.md
python scripts/render_markdown_pdfs.py --check --recursive docs/
```

`--check` recomputes the Markdown, PDF, and recorded local-resource SHA-256 values and verifies the manifest's render-policy/configuration identity. It does not depend on mtimes and does **not** replace PDF content/layout verification. Renderer versions are retained in the manifest for audit/reproduction; a local tool upgrade does not by itself invalidate an otherwise matching artifact unless repository policy requires rerendering.

Keep rendering deterministic enough for review: repository-owned templates/assets, explicit metadata, no arbitrary remote build assets, and no unapproved custom executable filters. The default helper records normal Markdown image dependencies and rejects remote, absolute, `file://`, or raw-HTML `<img>` resources rather than claiming provenance it cannot verify. Read `security-and-trust-boundaries.md` before rendering untrusted Markdown/HTML/CSS or enabling custom Pandoc filters/writers.

## PDF rendering environment

The preferred PDF engine is **Typst**, with **Pandoc** as the Markdown converter. This avoids a mandatory full TeX distribution while preserving Pandoc Markdown, tables, code blocks, citations, and mathematical notation through Pandoc's native Typst writer.

Install Pandoc through the Linux distribution package manager (or official Pandoc package). Install Typst as the `typst` package where available; Typst also documents Snap/prebuilt/Cargo installation routes. Do not assume every distribution uses the same package name/version.

The renderer must fail clearly when `pandoc` or `typst` is missing rather than silently skipping PDFs. Prefer an already-installed usable system/user `pandoc` and `typst`; do not repeatedly bootstrap temporary private copies merely because the tool is running in an agent environment. If missing and installation is not authorized, report the prerequisite instead of claiming document parity.

## PDF verification

After rendering a changed permanent document:

- confirm the command exited successfully and produced a non-empty PDF;
- inspect PDF page count/metadata/text or run the project's PDF smoke checker where available;
- visually render representative/all pages for release-significant manuals, especially equations, tables, code blocks, figures, and long lines;
- check that headings, code, equations, tables, links, page breaks, and figures are not clipped or missing;
- verify the PDF reflects the same current version/contract as the Markdown source;
- rerender after every subsequent Markdown edit.

A PDF that merely opens is not sufficient when layout is materially broken.

## Generated and assembled manuals

For manuals assembled from chapters or generated metadata:

- edit chapter/source Markdown rather than only assembled output;
- run the canonical builder;
- render the canonical assembled Markdown to PDF;
- verify deterministic output when declared;
- update machine-readable **current architecture/contract** data in the same change when it is normative;
- keep task-local gate/status data in the workplan rather than injecting it into architectural dependency graphs;
- ensure root-level/legacy duplicates are not left as competing authorities.

If both chapter PDFs and an assembled PDF exist, define which are required products and generate only those; do not inflate storage with redundant derived artifacts without a project need.

## External provenance and citations

Cite external sources when a material non-obvious algorithm, formula, estimator, physical model, standard, security property, or implementation idea is derived from external work.

- Prefer primary literature, standards, official documentation, or original algorithm papers.
- Cite the source actually used; do not add decorative references.
- Distinguish literature-derived theory from project-local engineering choices.
- Do not infer experimental/scientific values and attach a citation that did not explicitly provide them.
- Keep enough bibliographic detail or repository-approved citation form to recover the source.

## Evidence records

A useful gate/audit record contains:

```text
Context/version
Requirement or workplan/gate ID
Workplan ID/revision/SHA-256 when applicable
Changed surfaces
Commands/tests executed
Inputs/fixtures/seeds
Environment/runtime/backend
Observed results
Acceptance decision: PASS/FAIL/BLOCKED
Known limitations/deferred checks
Related specification/architecture/benchmark/history artifacts
Markdown/PDF/provenance-manifest status for permanent docs
```

Performance evidence additionally records timing methodology, repeats/warm-up, input sizes, CPU/GPU/thread configuration, memory metric, and comparison baseline. Storage evidence also records cold/warm behavior, bytes read/written when available, peak/final disk footprint, cache/checkpoint/recovery behavior, storage class, and I/O concurrency.

## Run and evidence manifests

For expensive, resumable, scientifically important, release-significant, or otherwise difficult-to-reproduce workflows, prefer a structured run/evidence manifest over reconstructing provenance from console logs. Record as applicable:

- package/source revision and authoritative version;
- implementation workplan ID/revision/SHA-256;
- input artifact identities/digests;
- resolved configuration/policy digest and redacted snapshot;
- dependency/runtime/backend/device/precision versions;
- random seeds and deterministic-mode settings;
- schema/cache/checkpoint/model/protocol versions;
- output artifact identities/digests;
- gate/requirement IDs and PASS/FAIL/BLOCKED/DEFERRED decisions;
- benchmark/storage/recovery measurements when relevant.

Keep the manifest machine-readable when automation consumes it. Do not place credentials or secrets in it. A useful provenance relation is:

```text
source + workplan + inputs + resolved configuration + environment -> outputs/evidence
```

Do not require heavyweight manifests for trivial unit-test-only edits.

## Documentation closeout

Before a substantial workplan/release is declared complete:

1. compare owning specifications directly with accepted implemented code/API/defaults/errors;
2. update architecture manuals **only for actual accepted architectural changes**, describing current state rather than gate history;
3. update history/changelog/release notes for completed material changes;
4. update authoritative package/release/schema/model/protocol versions according to project policy;
5. search affected current docs/examples for old names/defaults/current-state claims;
6. verify one normative owner exists per contract;
7. regenerate changed permanent Markdown documents to PDF and publish/update content-provenance manifests;
8. run content-provenance checks and verify PDF layout/version parity;
9. update indexes/navigation when new permanent docs are added;
10. keep workplan/audit/benchmark/history material from becoming competing current specifications or architecture;
11. mark/archive/delete the workplan according to its lifecycle policy only after mandatory acceptance has passed.

Documentation closeout is an acceptance check, not optional cleanup after implementation.

## Renderer references

For installation/engine details, use current official documentation:

- Pandoc installation: https://pandoc.org/installing.html
- Pandoc PDF engine documentation: https://pandoc.org/MANUAL.html
- Typst compiler installation: https://typst.app/open-source/
