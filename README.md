# Software Development Protocol

Software Development Protocol 5 is an engineering-fitness-first workflow for AI-assisted software engineering.

## Governing doctrine

> **Choose the globally best justified engineering-sufficient product. Among engineering-sufficient solutions, prefer the one with the lowest justified total product/system complexity. Among development processes that can establish that result with the required confidence, avoid unnecessary human, model, context/token, tool, compute, I/O, and wall-time cost.**

The hierarchy is lexicographic:

```text
product engineering fitness > minimum justified product/system complexity > development economy
```

Product engineering fitness includes functionality/capability, correctness and scientific/domain fidelity, reliability/recovery/safety/security/compatibility, CPU/RAM/VRAM/storage/I/O/wall-time feasibility, target-scale behavior, hardware effectiveness, and materially important end-to-end performance. These requirements define the feasible product space.

Among engineering-sufficient solutions, minimize unnecessary product mechanisms, duplicated authorities, states, abstractions, interfaces, dependencies, synchronization points, compatibility paths, runtime/operational stages, special cases, and maintenance surface. Necessary specialization remains valid when it buys a material capability or prevents a material failure.

Development economy is subordinate to engineering fitness and product simplicity. Once the required product and acceptance confidence are preserved, avoid redundant reasoning, rediscovery, low-information inspection, invalid reruns, repeated boilerplate, unnecessary tool/compute work, and other process waste. Never save development cost by weakening a material requirement, required validation, or the accepted product.

## Lifecycle

Protocol 5.4 preserves the two-role lifecycle:

```text
software-design -> software-implementation
```

- `software-design` diagnoses root causes, defines the material engineering envelope, chooses the globally justified product design, freezes material implementation authority, controls product complexity, defines validation obligations, and performs independent evidence-directed review when useful.
- `software-implementation` realizes/refactors the accepted product design, reconciles repository reality without silently reopening frozen design, performs mandatory stage-local and final affected-surface regression plus integration testing for executable changes, benchmarks/validates material claims, and delivers the result.

Optional specialists remain supporting capabilities, not approval gates:

- `software-documentation` — reconcile and improve durable documentation;
- `repository-hygiene` — conservative post-stage repository cleanup.

## Workplans and implementation authority

A substantial accepted workplan is a compressed implementation contract. It should distinguish:

- **Frozen** material requirements/design/ownership/algorithm decisions;
- **Delegated** implementation-local mechanics;
- **Reopen only on evidence** assumptions or redesign triggers.

Implementation does not repeat settled architecture merely because alternatives exist. It may locally realize/reconcile the plan while preserving frozen semantics. If evidence invalidates a frozen material decision, reopen only the affected design surface, preserve unrelated accepted work/evidence, and resume from the earliest materially affected dependency.

Workplans inherit generic protocol obligations from the version declared in their `protocol_version`; later protocol releases do not silently reinterpret older active/completed plans.

## Functional acceptance versus production qualification

For executable product changes, functional acceptance requires:

1. focused checks for new/modified mechanisms as appropriate;
2. affected regression after each material behavior-changing implementation stage before dependent work proceeds;
3. re-deriving the affected behavioral surface from the final assembled implementation;
4. final regression coverage across that complete surface;
5. integration testing through the assembled affected product path and real consumer/interface boundaries;
6. repository/project-required checks, using the broader/full available suite when impact cannot be bounded confidently.

Define stages by coherent behavior/risk boundaries rather than individual file/helper edits. Run cheap high-signal focused checks before the required affected regression. Reuse still-valid intermediate evidence until a changed dimension can plausibly invalidate it; final assembled affected-surface regression/integration remains a fresh acceptance boundary.

Use bounded fixtures/workloads where they preserve required behavioral coverage. Optimize test cost without narrowing required coverage.

Full production qualification is distinct. It uses real, long, data-heavy, target-machine/target-hardware runs to characterize an already functionally accepted candidate for production-scale performance/resources/scaling/recovery/hardware behavior. It is not a substitute for regression/integration testing and is not run by default unless explicitly requested, required by project/release policy, or necessary to establish a material production-scale claim.

## Context and reference economy

Repository inspection is progressive and evidence-driven. Prefer the lowest-cost high-information inspection/test that resolves a material uncertainty; reuse established facts; avoid rereading unchanged material without a new question; bound large logs/file reads to the smallest sufficient relevant portion without hiding failures or affected behavior.

Skill references are loaded by material surface rather than merely because they are packaged. Domain-specific security, scientific, concurrency, storage, Git, configuration, packaging, and performance guidance remains fully authoritative when its surface is material.

## Independent review

Independent review remains independent. Start from explicit requirements, accepted workplan, final implementation/diff, final affected surface, acceptance evidence, deviations, and unresolved risks. Challenge the highest-risk assumptions first. Do not automatically replay the entire original design search when evidence does not challenge accepted premises, but broaden without restriction when a premise, deviation, complexity regression, redesign trigger, or unresolved risk warrants it.

## Build and repository acceptance

`source/` is canonical. `dist/` contains generated ready-to-install skill packages and is committed for distribution.

Before a protocol revision is complete:

```bash
python -m unittest discover -s tests -v
python source/build_skills.py --output /tmp/protocol-dist
python source/validate_packages.py --dist /tmp/protocol-dist
python source/check_dist.py --expected /tmp/protocol-dist --committed dist
git diff --check
```

All commands must succeed on the assembled candidate. Package validation checks shipped structure; source-to-dist parity detects stale committed generated output.
