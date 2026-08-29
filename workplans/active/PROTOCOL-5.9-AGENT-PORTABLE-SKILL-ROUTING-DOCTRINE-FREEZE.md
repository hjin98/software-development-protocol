---
kind: implementation-workplan-amendment
workplan_id: PROTOCOL-5.9-AGENT-PORTABLE-SKILL-ROUTING-DOCTRINE-FREEZE
amends_workplan_id: PROTOCOL-5.9-AGENT-PORTABLE-SKILL-ROUTING
protocol_version: 5.8.0
target_protocol_version: 5.9.0
status: active
created_date: 2026-08-29
---

# Protocol 5.9 Routing Workplan — Doctrine and Content Freeze Amendment

This amendment is part of the governing contract for `PROTOCOL-5.9-AGENT-PORTABLE-SKILL-ROUTING`. It narrows the implementation scope: Protocol 5.9 is a **routing, packaging, discovery, validation, and compatibility functionality upgrade only**. It is not a redesign, simplification, reinterpretation, or rebalance of the Software Development Protocol's engineering doctrine or content discipline.

## Frozen doctrine

The governing hierarchy remains exactly:

```text
product engineering fitness > minimum justified product/system complexity > development economy
```

Its semantics are frozen:

1. **Product engineering fitness first.** Required capability, correctness/scientific fidelity, reliability/recovery/security/compatibility, resource feasibility, target-scale/hardware effectiveness, maintainability/operability, and material end-to-end performance define the feasible solution space. They may not be weakened to reduce complexity, context use, implementation effort, testing effort, or cost.
2. **Minimum justified product/system complexity second.** Among engineering-sufficient solutions, prefer the globally justified solution with the least unnecessary total product/system complexity. This remains solution/product simplicity, not an instruction to choose a locally shorter implementation that degrades the durable system.
3. **Development economy third.** Only after engineering fitness and justified product/system simplicity are preserved may the process optimize model/human reasoning, context, tool calls, tests, compute, I/O, and wall time.

Implementation must preserve this hierarchy verbatim in lifecycle entrypoints wherever Protocol 5.8 currently makes it directly salient. Routing changes must not reorder, soften, collapse, qualify away, or reinterpret these priorities.

## Frozen historical hardening

All material hardening accumulated through Protocol 5.8 remains normative and semantically unchanged. In particular, Protocol 5.9 must preserve:

### Protocol 5.4 development-economy and lifecycle controls

- the two-role lifecycle `software-design -> software-implementation`;
- progressive evidence-directed repository inspection and established-fact reuse;
- coherent material stages rather than file/helper micro-gates;
- stage-local affected regression for every material executable stage;
- final affected-surface re-derivation, regression, real-boundary integration, and repository-required checks;
- still-valid evidence reuse with claim-based invalidation;
- bounded redesign that reopens only the materially invalidated surface;
- version-bound workplan inheritance;
- independent review without unnecessary replay of settled reasoning;
- production qualification remaining distinct from ordinary functional acceptance;
- no mandatory process/evidence/token-accounting bureaucracy without independent product value.

### Protocol 5.5 implementation-fidelity hardening

- lossless Design -> Implementation handoff for material task-specific intent;
- preservation of protected concerns and stakeholder outcome;
- distinction among required end state/constraint, required implementation consequence, suggested realization, and delegated mechanics;
- accepted workplans as minimum known contracts rather than ceilings;
- dual semantic/conformance plus functional stage closure;
- green tests not proving omitted obligations were implemented;
- final accepted-contract reconciliation;
- structural/absence evidence for removal, uniqueness, ownership, and no-legacy-path claims;
- independent review as contract/outcome conformance challenge plus independent engineering challenge;
- lossless rework routing as implementation nonconformance, workplan/design deficiency, or new independent issue.

### Protocol 5.6 proxy-proof acceptance hardening

- identification of the real semantic owner/consumer boundary for material acceptance claims;
- prohibition on closing an owner claim by mocking, bypassing, reimplementing, precomputing, or seeding past the semantic owner under acceptance;
- continued allowance of bounded test doubles below/outside the real owner, including expensive scientific/ML computation, accelerators, external services, and reduced/synthetic data;
- direct helper calls not substituting for required production caller/orchestrator/reconciliation/state-transition behavior;
- unavailable real-owner acceptance remaining unavailable/blocking or a design-reopen condition rather than a proxy pass.

### Protocol 5.7 engineering-stewardship hardening

- the stakeholder's durable product outcome remaining the objective rather than tests, workplans, gates, metrics, reviews, or reports;
- non-adversarial interpretation according to protected engineering purpose;
- prohibition on acceptance gaming, including weakening assertions, narrowing fixtures to evade known failures, laundering buggy output into expectations, swallowing failures, adding unjustified permissive fallbacks, or rewriting specifications merely to bless defective behavior;
- truthful non-closure over counterfeit completion;
- self-correction and invalidation/repair of unsound evidence or implementation;
- bounded long-horizon stewardship without unrelated gold-plating;
- review authority to identify a materially deficient accepted contract rather than accepting literal compliance that defeats the stakeholder outcome.

### Protocol 5.8 effective-compression hardening

- canonical detailed ownership plus progressive disclosure;
- high-salience role entrypoints retaining the invariants and decision loops whose omission could materially alter behavior;
- task workplans preserving task-specific design intent without copying generic protocol manuals;
- stage proportionality reducing ceremony but never required coverage or evidence quality;
- context/process economy remaining subordinate to all engineering and acceptance safeguards above.

Protocol 5.9 changes **how reliably an agent reaches these rules**, not what these rules mean.

## Permitted content changes

Changes to lifecycle/specialist `SKILL.md` files are permitted only to the extent needed for the routing functionality and coherent version release, including:

- adding/repositioning the deterministic routing section;
- replacing vague progressive-disclosure routing prose with explicit trigger -> exact linked-reference rules;
- adding Markdown links and exact relative paths;
- removing routing prose that becomes strictly redundant after the new routing table is installed;
- minimal connective wording needed so the new routing mechanism integrates cleanly with the unchanged role instructions;
- protocol-version/release wording that accurately describes the routing/portability upgrade.

Changes to canonical reference files are permitted only when required for version-history/compatibility description or to support the routing/packaging mechanism itself. Existing normative engineering doctrine in those references is otherwise preservation territory.

## Prohibited content changes

The implementation must not, under this workplan:

- redefine or rebalance the three-tier hierarchy;
- weaken, strengthen, broaden, narrow, reinterpret, or replace existing software-engineering doctrine merely because different wording seems cleaner;
- delete a Protocol 5.4-5.8 safeguard because the new deterministic routing is expected to make agents behave better;
- merge distinct safeguards into a shorter statement if doing so loses a material failure-mode defense;
- change design/implementation role responsibility, workplan authority, stage semantics, acceptance semantics, proxy-proof boundaries, stewardship semantics, or effective-compression doctrine except where a purely routing/version reference must point to the same existing rule;
- use this portability work as an opportunity for unrelated protocol cleanup, stylistic rewriting, philosophy revision, or further compression/expansion;
- treat improved routing as evidence that existing hardening tests or normative references are now unnecessary.

If implementation discovers a genuine defect in existing doctrine, that is outside this workplan and requires a separately accepted bounded design change. It must not be folded silently into Protocol 5.9 routing work.

## Required acceptance for doctrine preservation

Protocol 5.9 cannot close merely because routing/package tests pass. Final acceptance must also establish that the pre-5.9 protocol semantics survived the change.

Required evidence:

1. Existing Protocol 5.4-5.8 semantic, failure-mode, stewardship, proxy-proof, fidelity, and effective-compression regression tests remain green without weakening their assertions or fixtures.
2. Source review compares the pre-change and assembled lifecycle/specialist entrypoints and confirms that non-routing normative content is unchanged in meaning. Any non-mechanical change outside routing/version/connective text must be explicitly justified as semantically identical; otherwise it is a workplan violation.
3. The exact hierarchy string remains directly present in both lifecycle role entrypoints:

```text
product engineering fitness > minimum justified product/system complexity > development economy
```

4. No existing canonical reference is deleted from a skill merely because routing is now deterministic, unless independent package-role analysis proves it was previously erroneous/unreachable and Design explicitly reopens that surface.
5. The implementation report must identify any normative-looking text changed outside the routing sections. The expected result is **none**, apart from mechanical path/link/version integration. Any substantive doctrine edit blocks acceptance and routes back to Design.
6. Final independent review must treat doctrine/content drift as a blocking **implementation nonconformance**, not as an equivalent implementation preference.

## Implementation authority amendment

### Frozen

In addition to the parent workplan's frozen decisions:

- Protocol 5.9 is strictly a routing/distribution/compatibility functionality upgrade.
- The three-tier hierarchy and its semantics are immutable under this workplan.
- All material Protocol 5.4-5.8 hardening safeguards are immutable under this workplan.
- Existing role responsibilities, design-implementation cycle, workplan authority, acceptance doctrine, proxy-proof boundaries, engineering stewardship, and effective-compression doctrine are not redesign surfaces.
- The target is **same protocol semantics, more reliable access to them across agents**.

### Delegated

Only local routing, packaging, validation, qualification, documentation, and mechanical integration details remain delegated as described by the parent workplan.

### Reopen only on evidence

The doctrine/content freeze itself is not reopenable because of a harness compatibility problem. If a harness cannot execute the frozen protocol efficiently or correctly, redesign the routing/adapter/package surface first. A proposed doctrine change requires a separate Software Design task with its own accepted workplan; it cannot be absorbed into this routing upgrade.

## Handoff closure amendment

Implementation must preserve this additional chain:

```text
Protocol 5.8 doctrine and historical hardening
-> unchanged normative meaning
-> improved deterministic reference reachability
-> cross-agent execution of the same protocol
```

The success criterion is not "a better rewritten protocol." It is **the same mature protocol, with a more reliable routing mechanism and portable skill packaging**.
