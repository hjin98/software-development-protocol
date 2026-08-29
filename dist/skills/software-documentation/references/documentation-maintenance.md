# Documentation Maintenance and Evolution

Documentation is a maintained information architecture for the accepted present system, not an append-only history of how the system evolved.

The governing engineering doctrine remains unchanged: seek the best globally justified solution, satisfy capability/correctness/scientific/resource/performance requirements first, then minimize unnecessary product/system complexity among engineering-sufficient solutions. That simplicity target does not require minimum documentation or development-process length. Documentation makes the resulting system understandable and usable without constraining sound engineering through a parallel process.

## Purpose

For AI-assisted development, documentation closes the gap between rapidly evolving implementation and human interpretation. A technically competent user should be able to understand the major public capabilities, scientific model, algorithms, assumptions, workflows, outputs, and limitations without reverse-engineering source code.

Transparency is therefore a product capability, especially for scientific and technical software.

## Authority model

Keep one current normative owner for each material contract.

Typical ownership:

- architecture — accepted current structure, ownership, important algorithms/data flow, durable extension boundaries;
- specification — accepted current behavior and contracts: API/CLI/configuration, schemas, units, numerical rules, persistence, compatibility, error/fallback semantics;
- guide — current task-oriented usage and interpretation;
- runbook — operational procedure, either current or explicitly release-pinned;
- methods/theory — explanatory and pedagogical material; non-normative unless explicitly assigned otherwise;
- workplan — proposed transition and temporary implementation coordination;
- history/release notes — completed chronology and superseded behavior;
- audits/benchmarks/release evidence — evidence rather than current semantic authority.

If historical/workplan text conflicts with current architecture/specification, the current normative owner controls.

## Reconcile before rewriting

Do not assume that code is automatically the intended contract. Code is evidence of actual behavior; specifications and accepted design may reveal that behavior as a defect.

Classify disagreement before editing:

| Observation | Default interpretation | Action |
|---|---|---|
| code and current specification agree; guide/manual differs | documentation drift | repair documentation |
| code differs from accepted current specification | possible implementation defect | surface contradiction; route semantic decision to design/implementation |
| accepted implementation deliberately changed a governed contract but spec did not | specification drift | update specification and affected consumers/docs |
| architecture differs from accepted implementation structure | architecture drift | update architecture if the structure really changed |
| two current normative documents disagree | authority conflict | resolve ownership/semantics, usually through `software-design` |
| generated output differs from declared canonical source chain | generated-artifact drift | regenerate derived output |
| current navigation points to a release-pinned obsolete runbook | lifecycle/navigation drift | update current runbook or reclassify old one |

When intent is ambiguous, report the discrepancy instead of silently choosing one side.

## Present system, not patch history

Write permanent current documentation as though the accepted current architecture and behavior had been designed in their present form from the beginning.

Do not accumulate:

```text
old explanation
+ amendment
+ exception
+ new algorithm
+ migration note
+ latest override
```

When a substantial conceptual change supersedes older theory, algorithm, architecture, terminology, defaults, or workflow, reconsider the affected document structure and produce one coherent current explanation. Move chronology to history/release notes.

### Rewrite rather than accrete

When conceptual organization changes materially, it is valid and often necessary to:

- reorder, rename, merge, or split sections;
- rewrite introductions, summaries, transitions, definitions, and examples;
- replace superseded derivations or diagrams;
- delete obsolete explanations;
- move historical material to history/release notes;
- rebuild the table of contents around the current conceptual hierarchy.

Do not preserve obsolete wording or section order merely to minimize the textual diff.

### Preserve still-valid substance

A coherent rewrite must not accidentally erase subtle current requirements. Before a large editorial refactor, identify the still-valid scientific, behavioral, architectural, compatibility, limitation, and edge-case content that must survive. After rewriting, verify that it remains represented by the correct current owner.

This is a temporary semantic-preservation check, not a mandate for permanent clause manifests or another evidence system.

## Refactor documentation debt

Substantial changes should trigger proportional editorial review of the affected document. Signals that local patching is no longer sufficient include:

- several sections now require corrective caveats;
- multiple generations of terminology are intermixed;
- the table of contents no longer matches the conceptual hierarchy;
- the same concept is explained differently in several places;
- implementation-stage chronology drives the narrative;
- a reader must mentally override an older explanation to obtain current behavior;
- figures/examples describe superseded architecture or workflows;
- a technically competent new reader cannot follow the document linearly.

Apply the documentation analogue of software refactoring: consolidate duplicate explanation, remove obsolete authority, restore clear ownership, and simplify the conceptual model without losing still-valid substance.

## Natural flow and progressive disclosure

Organize by the reader's conceptual/task flow rather than the order features were implemented.

A scientific architecture or methods document will often flow naturally through:

1. purpose and problem;
2. physical/mathematical foundations;
3. definitions and conventions;
4. conceptual model;
5. architecture/algorithm;
6. data/control flow;
7. numerical implementation;
8. inputs and outputs;
9. validity, assumptions, limitations, and edge cases;
10. scaling/performance where relevant;
11. interfaces/extension points;
12. examples/interpretation;
13. references.

A user guide often flows through:

1. what the capability does;
2. prerequisites;
3. minimal working workflow;
4. inputs/configuration;
5. running it;
6. interpreting results;
7. common variants;
8. troubleshooting;
9. advanced options;
10. related theory/references.

Use progressive disclosure: explain what/why first, then use, then theory/algorithm, then detailed numerical/edge-case material. Do not force every reader through implementation detail to discover basic capability.

## Concept-first terminology

Internal stage/class identifiers remain useful for traceability, but they should not define the user's ontology unless they are themselves meaningful public concepts.

Prefer:

```text
Multi-view subset selection (MVSEL2)
```

followed by purpose, theory, role in the workflow, inputs/outputs, and algorithm, rather than a heading that exposes only `MVSEL2` with no conceptual bridge.

Choose one preferred current term for each concept. Mention retired names only where compatibility or migration actually requires it. Avoid mixing old names, abbreviations, internal class names, and current user-facing names indefinitely.

## Current, pinned, and historical documents

Classify documents deliberately:

- current — expected to describe the current accepted software;
- release-pinned — intentionally describes one specific release/environment and states that identity explicitly;
- historical — describes past behavior/lineage;
- proposed — workplan or future design, not accepted current behavior.

Do not update a release-pinned runbook by blindly replacing version strings. Either regenerate/validate it for the current release or move/reclassify the old document while preserving historical truth.

## Canonical source chains and generated artifacts

Discover the true editable source before editing. Common source graphs include:

```text
canonical.md -> pdf
chapters/* -> assembler -> assembled.md -> pdf
API/schema/code -> generator -> markdown -> pdf
diagram source -> rendered figure -> markdown -> pdf
```

Edit the highest authoritative source and regenerate descendants. Do not independently patch an assembled Markdown file, PDF, rendered diagram, or other derived artifact when an upstream source exists.

Only document families that the project actually ships or needs should have generated formats. README/index/workplans need not acquire PDFs merely for symmetry.

If a repository tracks generated documents, use one reproducible renderer/build policy and record only the provenance necessary to establish the real source/output boundary. Avoid universal hashes and manifests unrelated to an actual generated-artifact contract.

## Mechanical versus semantic validation

Automation may fail objectively on affected document-chain integrity, for example:

- canonical source missing;
- generator failure;
- assembled Markdown stale relative to source;
- tracked PDF not derived from its declared source chain;
- required local figure/resource missing;
- directly affected internal link/index target missing;
- registered generated output orphaned.

Automation cannot determine by itself that a scientific equation matches the implemented estimator, an architecture description is conceptually correct, or a behavior change was intended. Treat those as semantic review findings and route genuine ambiguity to `software-design`/`software-implementation`.

Scope checks proportionally to changed documentation, generated descendants, and directly affected navigation. Repository-wide audit is an explicit maintenance/release activity, not the default response to a local code change.

## Executable examples and figures

Where inexpensive and meaningful, verify guide examples through the real public interface:

- CLI command/flag existence;
- public import paths/signatures;
- configuration keys/defaults;
- lightweight examples.

Do not launch an expensive production/GPU campaign merely to validate shell spelling when a smaller structural check answers the question.

Figures, diagrams, plots, captions, and navigation are part of the information architecture. Update them when their conceptual content changes. Preserve editable/generative figure sources where practical and avoid surrounding an obsolete figure with corrective prose.

## Documentation impact in normal development

Before completing an accepted software change, ask whether it materially altered a public capability, scientific interpretation, durable architecture, API/configuration contract, workflow, or existing explanation.

- no material documentation impact -> finish;
- small/local impact -> implementation may update the affected documentation directly;
- substantive synthesis/reconciliation/refactoring/theory/publication work -> use `software-documentation`.

Documentation maintenance must not become a mandatory third lifecycle step or unrelated release blocker.
