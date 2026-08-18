# Debugging, Data Lineage, and Stateful Recovery

Use this workflow for nontrivial bugs, failed gates, inconsistent resumed runs, stale-state symptoms, dependency/backend failures, and long-running pipelines whose behavior depends on persisted state.

## Diagnose before patching

1. Reproduce the smallest trustworthy failure without destroying the original evidence.
2. Trace the real execution path from user entry point through orchestration, policy selection, numerical kernels, persistence/caches, and final consumer.
3. Trace data lineage: source identity -> normalization -> derived state -> cache/checkpoint -> consumer.
4. Classify the failure mechanism before editing.
5. Identify the earliest violated invariant, not only the final exception/message.
6. Inspect adjacent assumptions that share the same state or contract.
7. Fix the owning layer and add regression evidence for the mechanism.

Useful failure classes include:

- algorithmic/logical;
- numerical/scientific;
- parser/input-contract;
- configuration/policy;
- stale cache or invalid persisted state;
- schema/version/lineage mismatch;
- dependency/API/ABI/environment;
- CPU/RAM/GPU/VRAM/disk resource admission;
- I/O/storage/corruption/recovery;
- concurrency/race/order/deadlock;
- integration/packaging/installed-artifact behavior.

Do not classify from the exception name alone; confirm with execution and state evidence.

## State and lineage identity

Long-lived derived state should be bound to the inputs and assumptions that produced it. Record a stable identity/manifest for material state such as:

- source dataset or input digest;
- configuration/plan identity;
- schema and algorithm version;
- model/checkpoint identity;
- relevant feature/metric definitions;
- backend/precision when semantically material.

A resume path must reject or explicitly migrate incompatible state. Never override a lineage/digest mismatch merely to continue execution unless the accepted design proves the mismatch irrelevant.

## Stateful stage design

For long-running stages:

- model the stage as explicit states/transitions rather than inferring state from arbitrary files;
- make completed work idempotent or safely discoverable;
- distinguish partial, complete, stale, corrupt, and superseded artifacts;
- publish completion only after required outputs and metadata are validated;
- make retries bounded and semantically safe;
- preserve deterministic aggregation/ordering where it is a contract;
- ensure cancellation/failure does not leave state that looks complete.

When recovery uses checkpoints/caches/journals, read `storage-and-io.md` as well.

## Qualification boundaries

Separate environment/capability qualification from the scientific/algorithm execution path.

- Detect required/optional dependencies and accelerator/backend capabilities early.
- Verify actual backend realization; a silent fallback is not evidence that the requested backend passed.
- Record why a backend was selected, rejected, or degraded.
- Keep CPU-only qualification distinct from target-GPU/HPC qualification.
- Do not patch dependency versions or bypass preflight simply to reach later stages unless the accepted plan explicitly changes the supported environment.

## Regression from a reported production failure

When a real input exposes a bug:

1. preserve/reduce a reproduction fixture where license/size permits;
2. identify the general invariant that failed;
3. add the narrowest regression/property test that captures the mechanism;
4. fix the owning implementation/specification;
5. run focused tests, then affected consumers, then broader gates as warranted;
6. rerun the original production-like workflow when feasible;
7. update persisted schema/cache invalidation rules if old state could reproduce the failure.

Do not patch only the reported fixture when the mechanism affects a broader input class.

## Anti-patterns

- changing a test/reference value to make a failure disappear without revising an accepted contract;
- catching a broad exception and continuing with partial/stale output;
- deleting caches/checkpoints until the bug disappears without identifying invalidation failure;
- treating a successful fallback backend as qualification of the requested backend;
- retrying OOM/I/O failures indefinitely;
- using file existence as proof that a stage completed;
- hiding a blocked environment check behind a later successful unit test;
- symptom-only patches in orchestration when the violated invariant is owned by a lower-level data/persistence contract.

## Completion evidence for a bug fix

Report:

- reproduction and root cause;
- violated invariant/contract;
- owning-layer fix;
- regression test added;
- affected state/cache invalidation or migration;
- focused and integration results;
- environments/backends not reproduced or not qualified;
- whether the original real-world failure was rerun successfully.
