---
kind: implementation-workplan
workplan_id: PROTOCOL-5.4-DEVELOPMENT-ECONOMY
protocol_version: 5.3.0
target_protocol_version: 5.4.0
status: active
---

# Protocol 5.4 Development-Economy and Context-Efficiency Workplan

## Status

**Active for implementation.**

This workplan is governed by Protocol 5.3.0 and targets Protocol 5.4.0. Protocol 5.4.0 does not exist as an accepted protocol contract until this workplan is implemented, validated, independently reviewed as warranted, and the resulting protocol revision is accepted.

## Objective

Revise the Software Development Protocol so that, after all material product requirements and justified product-simplicity decisions are satisfied, the development process avoids unnecessary human, model, context/token, tool, compute, I/O, and wall-time cost without weakening engineering quality, functional acceptance, scientific/domain fidelity, security, reliability, resource feasibility, target-scale behavior, hardware effectiveness, or materially required performance.

The target hierarchy is lexicographic:

```text
1. Product engineering fitness
2. Minimum justified product/system complexity
3. Development economy
```

Development economy is subordinate to the first two objectives. It may remove rediscovery, duplicated reasoning, low-information inspection, invalid reruns, unnecessary design reopening, repeated boilerplate, and other process waste. It must never justify a weaker product, weaker engineering evidence, or narrower required regression/integration coverage.

## Diagnosis

Protocol 5.3 already has the correct engineering-quality foundation:

- material engineering requirements define the feasible product space;
- among engineering-sufficient products, minimum justified total product/system complexity is preferred;
- product simplicity is explicitly distinguished from process minimalism;
- software design and software implementation remain the two lifecycle roles;
- substantial executable work requires focused checks, stage-local affected regression, final affected-surface re-derivation, final affected regression, integration testing, and repository/project-required checks;
- test cost may be optimized only after required coverage is established;
- full production qualification is separate from functional acceptance and is not run by default;
- repository intake is progressive rather than repository-wide by default;
- domain references are modular and already packaged separately from the lifecycle entrypoints.

The remaining inefficiency is primarily a control-plane and reasoning-authority problem rather than a missing testing or engineering rule.

The principal sources of avoidable development cost are:

1. **Repeated design reasoning during implementation.** `software-design` already freezes architecture, ownership, algorithms, invariants, non-goals, affected surfaces, acceptance, and redesign triggers, but `software-implementation` still has broad enough authority that a capable implementation agent may independently reopen settled choices even when a detailed accepted workplan exists.
2. **Workplan boilerplate duplication.** Substantial workplans repeat protocol-wide acceptance doctrine that is already owned by the protocol, increasing long-lived context carried through long agent sessions.
3. **Repeated repository/context discovery.** Progressive inspection exists, but the protocol does not yet explicitly require reuse of still-valid established facts, high-information discriminating inspections, targeted file/range reads, or bounded reasoning context from verbose command output.
4. **Repeated evidence generation.** Performance evidence already follows a compatibility/invalidation rule, but the same principle is not stated generally for intermediate development evidence.
5. **Micro-gating risk.** Stage-local regression is correctly mandatory, but the protocol can more clearly distinguish a coherent material behavior-changing stage from individual helper/file edits so that required regression does not become repetitive low-information rerunning.
6. **Flat reference routing.** Supporting references are modular, but lifecycle entrypoints currently present them largely as flat lists. Agents can load broad cross-cutting guidance when only one bounded domain section is material.
7. **Review rediscovery.** Independent review should remain independent, but independence does not require replaying the original design exploration from zero when final implementation/evidence does not challenge the accepted premises.
8. **Protocol-version inheritance ambiguity.** If future workplans become shorter by inheriting generic protocol requirements, that inheritance must be bound to the workplan's declared governing protocol version so later protocol revisions do not silently change an already-active plan.

## Engineering envelope

### Required product and protocol behavior

The revision must preserve or strengthen all material Protocol 5.3 guarantees, including:

- required functionality/capability first;
- correctness and scientific/domain fidelity;
- reliability, recovery, safety, and security where material;
- required compatibility and migration semantics;
- CPU/RAM/VRAM/storage/I/O/wall-time feasibility;
- target-scale behavior and effective target-hardware use;
- materially required end-to-end performance;
- minimum justified total product/system complexity among engineering-sufficient solutions;
- two-role lifecycle (`software-design -> software-implementation`);
- optional specialists remaining non-mandatory supporting capabilities rather than approval gates;
- affected-surface regression and real-path integration as functional-acceptance requirements;
- mandatory stage-local affected regression after every material behavior-changing implementation stage before dependent implementation proceeds;
- final re-derivation of the affected behavioral surface from the assembled candidate;
- final affected-surface regression and integration on the final candidate;
- repository/project-required broader checks, including the broader/full suite when impact cannot be bounded confidently;
- production qualification remaining separate from functional acceptance;
- no fabricated unavailable hardware/production evidence;
- progressive, evidence-driven repository inspection;
- security, scientific/numerical, persistence, concurrency, configuration, Git, packaging, performance, and documentation protections remaining available and authoritative when their surfaces are material.

### Development-economy objective

Among development processes that preserve the required product, engineering confidence, and acceptance coverage, prefer the process with the lowest justified total development cost. Development cost includes, where material:

- human supervision/rework;
- model reasoning and output;
- fresh and cached context/token processing;
- file/search/tool calls;
- test/benchmark executions;
- CPU/GPU time;
- RAM/VRAM/storage/I/O consumption;
- external-service use;
- wall time.

The protocol must not require token accounting or telemetry for ordinary work merely to optimize these quantities. Measurement is appropriate when evaluating the protocol itself, comparing workflows, diagnosing unusually expensive agent trajectories, or when the environment exposes the metrics cheaply.

### Simplicity constraint

Do not create a parallel development-economy bureaucracy. In particular, this revision must not introduce by default:

- a third lifecycle role;
- a development-economy specialist;
- mandatory task-classification state;
- a persistent gate ledger/database;
- a new evidence database or manifest system;
- mandatory token/context/tool-call accounting;
- arbitrary context, word-count, or tool-call budgets;
- model-specific Sol/Terra/Luna rules;
- a new `development-economy.md` reference unless implementation evidence proves a distinct owner is materially justified.

## Governing doctrine for Protocol 5.4

Freeze the following hierarchy as the target doctrine:

> **Choose the globally best justified engineering-sufficient product. Among engineering-sufficient solutions, prefer the one with the lowest justified total product/system complexity. Among development processes that can establish that result with the required confidence, avoid unnecessary human, model, context/token, tool, compute, I/O, and wall-time cost.**

Interpret this lexicographically, not as a weighted tradeoff:

```text
engineering fitness > product simplicity > development economy
```

`Product engineering fitness` includes required functionality/capability, correctness/scientific fidelity, reliability/recovery/safety/security/compatibility, resource feasibility, target-scale behavior, target-hardware effectiveness, and materially required performance.

Development economy may optimize only inside the process space that still establishes the required product with the required confidence.

## Product design

### A. Accepted-workplan authority

When a governing accepted workplan exists, implementation must treat its material target decisions as the implementation contract rather than reopening them merely because another plausible design exists.

The authority relationship is:

```text
explicit user/task requirements + safety/project instructions
    -> material product requirements and governed contracts
    -> accepted governing workplan target decisions
    -> repository evidence about actual state
    -> implementation-local discretion
```

This ordering requires careful interpretation:

- current repository behavior is evidence of actual state, not automatic authority over an accepted change plan;
- existing specifications/contracts remain authoritative except where the governing workplan explicitly defines their intended change;
- if repository evidence contradicts a workplan assumption, implementation must reconcile the contradiction rather than silently abandoning either source;
- implementation may not silently change a frozen target decision merely because a different local design appears attractive.

### B. Three implementation-deviation levels

#### 1. Implementation realization

No design reopening is required for local mechanics that preserve frozen semantics, such as:

- helper factoring;
- local naming;
- exact fixture mechanics;
- code placement where the workplan intentionally leaves it open;
- adapting prescribed behavior to actual module layout without changing ownership or material semantics.

#### 2. Local reconciliation

Implementation may locally reconcile superficial mismatch between the workplan and repository reality when the frozen target remains unchanged. Record the material reason when it affects interpretation; do not create a new design lifecycle for ordinary realization details.

#### 3. Material redesign

Reopen design when implementation evidence would require changing a frozen material decision, including architecture/ownership, algorithm/data representation, product semantics, material resource policy, persistence/compatibility semantics, or another explicitly frozen target.

Material redesign is triggered only by evidence such as:

- a frozen assumption conflicts with actual repository authority in a way that cannot be reconciled locally;
- the frozen design cannot satisfy a material engineering requirement;
- representative profiling/measurement invalidates a material algorithm/resource premise;
- a stated workplan redesign trigger fires;
- repeated local fixes expose a structural ownership/design defect.

### C. Bounded redesign reopening

A material redesign trigger must not restart unrelated accepted work.

When a frozen decision is invalidated:

1. identify the exact invalidated assumption/decision;
2. stop dependent implementation;
3. preserve unrelated accepted stages and still-valid evidence;
4. reopen only the affected design surface;
5. update/reconcile the governing workplan as necessary;
6. invalidate tests/evidence only where the changed decision can plausibly affect their claim;
7. resume from the earliest materially affected stage.

Use minimal dependency-consistent rollback rather than full-process restart.

### D. Version-bound workplan inheritance

A workplan inherits generic protocol requirements from the version declared in its `protocol_version` metadata.

Therefore:

- this workplan is governed by Protocol 5.3.0 while targeting Protocol 5.4.0;
- completed work under older versions remains valid historical work under the version that governed it;
- an active older workplan does not silently acquire 5.4 semantics when 5.4 is released;
- an active plan may explicitly adopt a newer protocol version after reconciling any changed obligations;
- still-valid prior evidence need not be rerun merely because the governing protocol version changes unless the adopted semantic change can affect its claim.

This rule allows future workplans to inherit generic protocol acceptance without repeating it while preserving stable historical meaning.

### E. Compressed workplans

Workplans should be compressed design results rather than copies of the protocol.

For a workplan governed by Protocol 5.4 or later, generic functional-acceptance requirements may be inherited by reference to the declared protocol version. The workplan should then record task-specific information:

- objective/diagnosis;
- engineering envelope and non-goals;
- frozen architecture/ownership/algorithm decisions;
- delegated implementation mechanics where useful;
- provisional affected surface;
- task-specific focused/regression/integration paths;
- numerical/security/resource/compatibility thresholds specific to the task;
- implementation ordering where sequencing matters;
- production-qualification requirement/deferral only when material;
- material risks/redesign triggers.

Do not repeat generic protocol prose merely for completeness.

### F. Workplan implementation-authority index

Revise the implementation workplan template to include a compact authority index:

```markdown
## Implementation authority

### Frozen
<Material decisions implementation must preserve.>

### Delegated
<Implementation-local decisions intentionally left open.>

### Reopen only on evidence
<Explicit redesign triggers or assumptions whose invalidation requires design reconsideration.>
```

This section is an index of authority, not a second copy of the architecture explanation.

### G. Information-gain and context economy

Strengthen repository intake and implementation guidance with the following rule:

> **Choose the lowest-cost next inspection, search, test, benchmark, or other action that most strongly resolves a material uncertainty or establishes required acceptance evidence.**

Apply this without hiding relevant evidence:

- prefer targeted symbol/search/range inspection before loading whole large files when sufficient;
- do not reread unchanged material without a new material question;
- reuse repository facts already established in the current task until later evidence invalidates them;
- use targeted failure excerpts rather than repeatedly ingesting enormous successful command logs;
- preserve full logs externally when materially useful, but reason from the smallest sufficient relevant portion;
- combine closely related read-only queries when doing so reduces turns without broadening scope;
- expand repository scope only through a plausible ownership/impact dependency;
- prefer an inspection/test that discriminates among remaining materially plausible explanations over broad speculative reconnaissance.

Do not formalize this into mandatory Bayesian analysis, hypothesis documents, or another artifact.

### H. Evidence reuse and invalidation

Generalize the existing performance-evidence principle:

> **Rerun evidence when a changed dimension can plausibly affect the result or interpretation; otherwise reuse still-valid evidence.**

Examples:

- documentation-only edits do not invalidate numerical regression evidence;
- executable refactoring invalidates regression evidence for behavior that could be affected;
- serialization changes invalidate relevant persistence/compatibility evidence but not unrelated mathematical oracle evidence;
- GPU policy changes invalidate affected GPU equivalence/performance evidence without automatically invalidating an unchanged CPU reference path.

This optimization principally applies to intermediate work. It does not remove the final Protocol functional-acceptance requirement to rerun the complete affected-surface regression and integration on the final assembled candidate after all material executable changes.

### I. Coherent stage granularity and fail-cheap-first testing

Preserve mandatory stage-local regression while preventing accidental micro-gating.

A material implementation stage is a coherent behavior-changing unit and may contain several tightly coupled edits. Do not treat every helper/file edit as a separate stage unless it independently changes executable behavior or represents a useful risk boundary.

Within each material stage:

```text
coherent implementation edits
    -> cheapest high-signal focused checks
    -> required affected regression subset
    -> stage accepted
```

Required affected regression still runs before dependent implementation proceeds. Cheap focused checks improve fault localization and avoid wasting broader test executions on obvious local failures; they do not substitute for the required stage regression.

### J. Compact working state without new persistent machinery

For long gated sessions, preserve enough compact working state to avoid rediscovery, conceptually including:

- accepted frozen decisions;
- accepted stages;
- affected-surface additions/deltas;
- still-valid evidence;
- invalidated evidence;
- unresolved material risks or redesign triggers.

Do not create a mandatory ledger file, database, manifest, JSON schema, or evidence artifact. Persist such state only when the project independently requires it. Final acceptance must still re-derive the complete affected surface independently from the final implementation.

### K. Trigger-directed reference routing

Preserve the existing modular reference set. Do not remove material domain guidance merely to shrink package size.

Replace flat supporting-reference presentation with trigger-directed routing, for example:

| Material surface | Reference |
| --- | --- |
| architecture/ownership/redesign | `architecture-and-design.md` |
| nontrivial failure/state recovery | `debugging-and-state-recovery.md` |
| API/schema/contracts | `specification-and-implementation.md` |
| configuration/policy | `configuration-and-policy.md` |
| workers/schedulers/retries/cancellation | `concurrency-and-orchestration.md` |
| cache/checkpoint/storage/I/O | `storage-and-io.md` |
| CPU/GPU/scaling/performance | `performance-and-parallelism.md` |
| physics/math/ML/numerical semantics | `scientific-software.md` |
| untrusted inputs/network/subprocess/model loading | `security-and-trust-boundaries.md` |
| branches/worktrees/commits/remotes | `git-and-version-control.md` |
| packages/install/distribution | `release-and-distribution.md` |
| documentation authority/evidence | `documentation-and-evidence.md` |

State explicitly that packaging a reference does not make reading it mandatory. Read it when its owned surface becomes material.

For long, multi-section references, add a concise section index/table of contents where that materially enables targeted reading. Permit reading only the relevant bounded section when the issue is clearly localized; broaden when cross-cutting interaction makes the rest material.

Do not introduce arbitrary line-count requirements for references.

### L. Entrypoint consolidation

Compress duplicated lifecycle-entrypoint prose only where a canonical reference already owns the detailed rule and the hard requirement remains obvious at the entrypoint.

In particular, both lifecycle skills must still state directly that executable changes require, as applicable:

- focused checks;
- stage-local affected regression for every material behavior-changing stage;
- final affected-surface re-derivation;
- final affected regression;
- integration through the assembled product path;
- repository/project-required checks;
- required failures/unexecuted checks block acceptance.

Detailed edge cases may route to `testing-and-validation.md`.

Do not target an arbitrary SKILL.md size. A tentative 20-30% reduction may be useful if achieved through genuine semantic consolidation, but line/token reduction is not an acceptance requirement and must not remove a material guardrail.

### M. Evidence-directed independent review

Independent review remains independent and retains full authority to broaden scope.

Review should start from:

- explicit requirements and governed contracts;
- accepted workplan;
- material final implementation/diff;
- final affected surface;
- regression/integration/benchmark evidence;
- material deviations and unresolved risks.

It should independently challenge the highest-risk assumptions, ownership boundaries, deviations, complexity changes, and acceptance evidence. It need not automatically replay the original architecture search from zero when no evidence challenges the accepted premises.

Reopen broader original design space when implementation or evidence:

- materially deviates from the workplan;
- undermines a design premise;
- exposes unexpected behavior;
- materially regresses product complexity;
- fires a redesign trigger;
- leaves a material unresolved risk.

### N. Optional-specialist alignment

Do not redesign `software-documentation` or `repository-hygiene`. They are already optional and explicitly reject mandatory repository-wide work after ordinary local changes.

Only align their governing wording with the new hierarchy where necessary and let them inherit revised shared references.

## Explicit non-goals

Protocol 5.4 must not:

- weaken focused/regression/integration requirements;
- make final affected-surface reconciliation incremental-only;
- trade correctness, scientific fidelity, security, or resource feasibility for token savings;
- remove domain references needed for material engineering surfaces;
- introduce a third lifecycle role;
- introduce a development-economy specialist;
- require mandatory `local/scoped/architectural/qualification` task classes;
- require a persistent gate ledger;
- require token/context/tool-call accounting for ordinary work;
- create a parallel evidence database;
- impose arbitrary context or tool-call budgets;
- hard-code specific model routing or model names into the protocol;
- force all workplans or role entrypoints to a fixed size;
- automatically upgrade old workplans to Protocol 5.4;
- make implementation blindly obey a demonstrably invalid workplan;
- reduce final acceptance because intermediate evidence was reused.

## Initially expected affected behavioral surface

### Expected mandatory source changes

- `source/PROTOCOL_VERSION`
- root `README.md`
- `source/README.md`
- `source/roles/software-design/SKILL.md`
- `source/roles/software-implementation/SKILL.md`
- `source/shared/references/workflow-and-workplans.md`
- `source/shared/references/repository-intake.md`
- `source/shared/references/testing-and-validation.md`
- `source/shared/references/protocol-versioning-and-compatibility.md`
- `source/shared/templates/implementation_workplan_template.md`
- relevant protocol regression tests
- generated `dist/` packages and `BUILD_INDEX.json`

### Likely small source changes

- `source/shared/references/architecture-and-design.md`
- `source/shared/references/documentation-and-evidence.md`
- `source/shared/references/debugging-and-state-recovery.md`

### Conditional changes

- long cross-cutting references only where a concise index materially improves targeted loading;
- optional-specialist entrypoints only where needed to align the governing hierarchy;
- `source/build_skills.py` only if implementation proves the existing modular packaging/routing mechanism insufficient. Do not change it merely to support prose-level routing.

### Transitive/generated surface

Because `source/` is canonical and `dist/` is committed generated output, all affected skill packages must be rebuilt from canonical source and independently validated. Changes to shared references can affect multiple packaged skills even if only one lifecycle role directly changes.

The final affected surface is provisional here and must be re-derived from the assembled Protocol 5.4 candidate before acceptance.

## Functional acceptance

Protocol 5.3 functional acceptance governs this workplan.

For every material behavior-changing protocol/tooling stage:

- run focused checks appropriate to the changed mechanism;
- run the relevant affected protocol regression subset before dependent implementation proceeds;
- fix newly introduced failures at the stage that introduced them.

Before final completion:

1. re-derive the affected source, packaged-skill, build-tooling, and distribution surface from the final assembled candidate;
2. account for every affected path with regression/package validation or an explicit unavailable/blocking check;
3. run the complete protocol regression suite on the final candidate;
4. build the canonical packages once from the final source;
5. validate the generated packages independently;
6. verify committed `dist/` semantic parity against that exact canonical build;
7. run `git diff --check`;
8. inspect the resulting source/dist changes for unintended scope or missing generated outputs.

### Semantic contract regression

Add small robust tests for instructional contracts where the text itself is executable product behavior. Prefer semantic/structural invariants over exact prose.

Tests should establish, where practical:

- Protocol 5.4 version propagation;
- both lifecycle roles retain the governing engineering-fitness/product-simplicity/development-economy hierarchy;
- implementation includes governing-workplan authority and evidence-triggered reopening semantics;
- the implementation workplan template exposes implementation authority and version-bound protocol inheritance;
- mandatory stage-local/final affected regression and integration doctrine remains present;
- referenced routes resolve and packaged references remain available;
- generated packages retain required metadata/resources;
- build index matches the target protocol version;
- committed distributions match canonical generated content.

Do not create brittle tests for:

- exact prose;
- exact word/line counts;
- exact number of bullets;
- stylistic phrasing;
- arbitrary SKILL.md size limits.

### Repository acceptance commands

The final candidate must pass the existing canonical repository sequence:

```bash
python -m unittest discover -s tests -v
python source/build_skills.py --output /tmp/protocol-dist
python source/validate_packages.py --dist /tmp/protocol-dist
python source/check_dist.py --expected /tmp/protocol-dist --committed dist
git diff --check
```

### Production qualification

**Unnecessary.** This is a protocol/instruction/tooling revision. No real long-running target-machine production workload is required to establish functional correctness of the protocol package. Development-economy benefits should not be claimed quantitatively without later representative agent-workflow measurement.

## Implementation sequence

### G0 - Preserve Protocol 5.3 guarantees

Before changing doctrine, capture the current guarantees that must remain true in the new source and tests:

- engineering fitness remains the feasibility boundary;
- product simplicity remains subordinate to material engineering requirements;
- two-role lifecycle remains intact;
- stage-local affected regression remains mandatory;
- final affected-surface re-derivation/regression/integration remains mandatory;
- production qualification remains separate;
- domain-specific engineering references remain available.

Add/identify regression assertions sufficient to catch accidental removal of these guarantees during later stages.

**Stage acceptance:** focused protocol contract tests and existing affected tests pass.

### G1 - Formal three-tier doctrine

Update canonical doctrine and lifecycle roles to establish:

```text
engineering fitness > product simplicity > development economy
```

Define development economy as subordinate optimization of the development process after product/acceptance requirements are satisfied. Do not narrow any material engineering requirement.

Update root/source README and role wording consistently without unnecessary duplication.

**Stage acceptance:** hierarchy contract tests plus affected protocol tests pass.

### G2 - Workplan authority and redesign boundary

Implement:

- accepted-workplan precedence;
- current repository state as evidence rather than automatic authority over intended change;
- frozen/delegated/reopen-only-on-evidence semantics;
- implementation realization vs local reconciliation vs material redesign;
- bounded/minimal dependency-consistent redesign reopening.

Update Design, Implementation, workflow/workplan, architecture/design, and debugging guidance only where each file owns a distinct part of the semantics.

**Stage acceptance:** semantic contract tests for workplan authority/reopening plus affected protocol tests pass.

### G3 - Version-bound compressed workplans

Update protocol versioning and the workplan template so generic protocol requirements can be inherited from the workplan's declared `protocol_version` without changing historical meaning.

Add the compact Implementation Authority index. Remove generic workplan boilerplate only where inherited protocol ownership is explicit and task-specific acceptance remains complete.

Document adoption behavior for older active plans.

**Stage acceptance:** template/versioning semantic tests plus affected package/reference tests pass.

### G4 - Context and information economy

Strengthen repository intake and lifecycle guidance with:

- established-fact reuse;
- information-gain-driven inspection/testing;
- targeted symbol/range/file reads;
- bounded tool/log context;
- evidence-driven scope expansion;
- avoidance of repeated unchanged reads/rediscovery.

Do not permit context minimization to hide required evidence or transitive affected behavior.

**Stage acceptance:** affected protocol/reference tests pass; inspect final wording for no implied coverage narrowing.

### G5 - Evidence and gate economy

Generalize evidence invalidation/reuse beyond performance baselines. Clarify coherent material stage granularity and fail-cheap-first focused testing while preserving mandatory stage regression and final assembled acceptance.

Ensure final acceptance remains a fresh final affected-surface reconciliation/regression/integration boundary even when intermediate evidence is reused.

**Stage acceptance:** testing/versioning/workflow contract tests plus affected tests pass.

### G6 - Reference routing and entrypoint consolidation

Replace flat supporting-reference presentation with trigger-directed routing where it materially improves selection. Add concise section indexes to long references only where useful for bounded targeted reading.

Consolidate duplicated entrypoint prose only where detailed authority remains in canonical references and the hard rule remains directly visible.

Do not modify package topology unless evidence proves it necessary.

**Stage acceptance:** reference-route validation, package-content tests, and affected protocol tests pass.

### G7 - Evidence-directed independent review

Update Software Design review guidance so review remains independent and risk/evidence-directed. It may start from accepted design + final implementation/evidence rather than replaying all original exploration, but retains authority to broaden arbitrarily when evidence challenges a premise or reveals material risk.

**Stage acceptance:** design-role contract tests and affected protocol tests pass.

### G8 - Compatibility and specialist/documentation reconciliation

Record Protocol 5.4 semantics in versioning/compatibility documentation. Align optional specialists only where needed to avoid hierarchy wording drift. Reconcile canonical READMEs and any changed documentation authority language.

Do not redesign optional specialists or introduce new lifecycle machinery.

**Stage acceptance:** compatibility/build-index/package tests and affected protocol tests pass.

### G9 - Final protocol regression and packaged-artifact acceptance

Re-derive the final affected surface from the assembled candidate.

Run:

```bash
python -m unittest discover -s tests -v
python source/build_skills.py --output /tmp/protocol-dist
python source/validate_packages.py --dist /tmp/protocol-dist
python source/check_dist.py --expected /tmp/protocol-dist --committed dist
git diff --check
```

Inspect all source and generated changes for:

- preserved Protocol 5.3 guarantees;
- correct 5.4 version metadata;
- complete generated-package updates;
- no unresolved reference routes;
- no accidental scope expansion;
- no unnecessary new protocol machinery;
- no weakening of regression/integration requirements;
- no model-specific policy leakage;
- no stale Protocol 5.3 wording where it would contradict accepted 5.4 semantics.

**Final acceptance:** all required checks pass on the same assembled candidate and no material unresolved design/compatibility issue remains.

## Risks and redesign triggers

Reopen this workplan only when implementation evidence shows a material issue, including:

1. **Acceptance weakening:** context/evidence economy can be interpreted as permission to skip an affected behavior, required stage regression, final regression, or integration boundary.
2. **Authority inversion:** a workplan can override higher-priority explicit requirements, safety/project policy, or unchanged governed contracts outside its authorized change scope.
3. **Blind-plan obedience:** implementation cannot respond safely when repository evidence proves a frozen plan assumption invalid.
4. **Historical semantic drift:** version-bound workplan inheritance cannot preserve stable meaning for older active/completed plans.
5. **New bureaucracy:** economy optimization requires a persistent ledger, mandatory telemetry, new lifecycle role, or other substantial process machinery to function correctly.
6. **Reference-routing loss:** trigger-directed routing makes a material security/scientific/concurrency/storage/Git/etc. rule effectively undiscoverable.
7. **Entrypoint overcompression:** removal of duplicate prose makes a non-negotiable acceptance/safety rule too easy to miss or changes its meaning.
8. **Review weakening:** evidence-directed independent review becomes implementation-summary acceptance rather than independent challenge.
9. **Build/package mismatch:** the existing canonical build architecture cannot express required routing/version metadata without a real build-tool change.
10. **Protocol regression-test brittleness:** semantic contract tests require exact prose/format and become a maintenance burden rather than protecting behavior.
11. **Economy metric distortion:** implementation starts optimizing visible token/tool counts at the expense of rework, correctness, product quality, or total accepted-result cost.

When a redesign trigger fires, reopen only the affected design surface and preserve unrelated accepted gates/evidence where still valid.

## Completion criteria

Protocol 5.4.0 is complete only when:

- the three-tier hierarchy is explicit and internally consistent;
- accepted-workplan authority and evidence-triggered reopening are unambiguous;
- workplans can inherit protocol-wide acceptance by version without historical drift;
- development/context economy rules reduce unnecessary reasoning opportunities without narrowing required evidence;
- stage-local and final functional acceptance remain at least as strong as Protocol 5.3;
- domain references remain available and are routed proportionally;
- independent review remains genuinely independent;
- no unjustified new lifecycle/process machinery has been introduced;
- the final affected surface has been re-derived and covered;
- all protocol regression/build/package/parity/whitespace checks pass on the assembled candidate;
- `dist/` matches canonical source;
- remaining limitations are explicitly reported rather than hidden.

## Frozen implementation principle

> **Do the necessary reasoning once, freeze what was materially settled, implement against that authority, expand or reopen only on evidence, reuse still-valid knowledge and evidence, keep active context high-information, and retain complete functional acceptance.**

Development economy is achieved by eliminating unnecessary work, not by purchasing speed or lower token use with weaker engineering.
