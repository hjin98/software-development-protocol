# Concurrency and Orchestration Correctness

Parallelism is not only a throughput problem. Schedulers, worker pools, concurrent jobs, asynchronous pipelines, and resumable stages create correctness obligations around ownership, failure propagation, cancellation, retries, state publication, and deterministic aggregation.

Read `performance-and-parallelism.md` for throughput/resource sizing and `storage-and-io.md` for parallel persistence. This document owns orchestration correctness.

## Define the execution state machine

For a nontrivial orchestrated workflow, make stage/task states explicit enough to reason about transitions. Typical states may include:

```text
QUEUED -> RUNNING -> COMPLETE
                 -> FAILED
                 -> CANCELLED
                 -> BLOCKED
```

Resumable systems may also need durable distinctions such as `PARTIAL`, `RECOVERABLE`, or `INVALID`, but do not proliferate states without a real semantic difference.

Define:

- who owns each task/resource;
- which transitions are durable;
- what constitutes completion;
- how parent/child failure propagates;
- what state is safe to resume;
- what cleanup is required on every terminal path.

Do not infer completion from worker disappearance, file existence, or a progress counter alone.

## Failure classification and retry policy

Classify failures before retrying. Useful classes include:

- transient infrastructure/resource failures where retry can preserve semantics;
- adaptive resource failures with a bounded corrective action, such as retrying an OOM-safe batch at a smaller size;
- external-service/transient I/O failures with bounded backoff where idempotency is established;
- deterministic input/configuration/scientific-invariant failures;
- programmer defects/assertion failures;
- corruption/schema/lineage mismatch;
- user cancellation/preemption.

Only retry classes whose semantics are understood.

A safe retry policy defines:

- maximum attempts;
- backoff/jitter where appropriate;
- what state is discarded or reused;
- whether the operation is idempotent;
- what evidence is retained across attempts;
- final failure behavior.

`retryable failure != arbitrary failure`. Do not hide deterministic defects behind automatic retries.

## Idempotency and publication

Operations that may be retried or resumed should be idempotent or use unique attempt identities plus transactional publication.

- Separate attempt-local temporary state from accepted durable state.
- Publish final artifacts only after validation.
- Prevent duplicate logical outputs from concurrent/retried attempts unless duplicates are an intentional contract.
- Ensure a resumed stage can distinguish already-accepted work from partial or stale work.

For file-backed publication, coordinate with `storage-and-io.md`.

## Cancellation, signals, and preemption

Long-running user/HPC workflows should define behavior for cancellation and common termination signals where the platform permits it.

- Stop scheduling new work once cancellation begins.
- Propagate cancellation to owned children/workers.
- Allow a bounded graceful-cleanup/checkpoint path only when it is safe and fast enough for the environment.
- Do not claim a checkpoint was committed unless publication completed.
- Release GPU contexts, file handles, temporary directories, locks, shared-memory segments, and child processes owned by the stage.
- Preserve externally owned/user input state.

A forced kill can always occur; design durable state so abrupt termination cannot make partial state appear valid.

## Backpressure and bounded queues

Producer/consumer pipelines need bounded in-flight work.

- Bound queues by task count and/or memory footprint.
- Avoid reading/materializing an entire dataset merely because downstream workers are slower.
- Couple admission to RAM/VRAM/I/O/storage budgets where tasks have heterogeneous cost.
- Avoid unbounded futures lists, result buffers, log queues, and pending serialization.

When throughput stalls, distinguish compute saturation from queueing, lock contention, I/O saturation, or downstream backpressure.

## Resource ownership and nested schedulers

Make ownership of scarce resources explicit:

- CPU worker/thread leases;
- GPU/device assignment and concurrent-job limits;
- RAM/VRAM reservations or admission estimates;
- I/O worker budgets;
- scratch directories and cache writers;
- ports/files/locks/shared-memory objects.

Do not allow nested schedulers to independently assume they own the entire machine. A library called from an already-parallel job should be able to run with bounded/serial inner concurrency.

## Determinism and aggregation

Concurrency may change arrival order without permission to change externally visible semantics.

- Define whether result ordering is input order, key-sorted order, stable task order, or intentionally unordered.
- Use deterministic reductions where reproducibility requires them; document accepted floating-point nondeterminism when strict reproducibility is impractical.
- Make random seeds/task seeds independent of worker scheduling when reproducible stochastic behavior is required.
- Avoid stateful global RNG/resource mutation from unordered workers unless explicitly coordinated.

## Locks and shared state

Prefer ownership/partitioning or immutable shared data over broad locking.

When locks are unavoidable:

- define lock scope/order;
- keep critical sections small;
- avoid lock acquisition while performing slow external I/O where possible;
- ensure exceptions release locks;
- test concurrent creation/publication paths;
- avoid stale lock files without ownership/lease semantics.

## Progress and ETA

Progress must describe accepted logical work, not merely submitted tasks. Keep the output convention stable within a project. For resumable workflows, restored completed work should not be double-counted.

ETA is observational: base it on representative completed work, use a consistent project-defined format, and do not let progress reporting materially perturb hot loops or disk I/O.

## Verification

Test concurrency at the state-transition level, not only by comparing final happy-path output:

- serial vs concurrent equivalence;
- deterministic ordering/seed behavior;
- worker failure propagation;
- cancellation during compute and during publication;
- bounded retry/backoff and terminal failure;
- OOM/resource backoff only where semantically safe;
- bounded queue/backpressure behavior;
- concurrent cache/output creation;
- restart after partial worker completion;
- cleanup of children/temp state/locks after failure;
- nested thread/process budget behavior;
- repeated stress runs for races when deterministic unit tests cannot expose them reliably.

## Hard rules

- Do not equate more workers with correctness or performance.
- Do not retry unknown failures indefinitely.
- Do not leave orphan workers or owned temporary resources after normal failure/cancellation paths.
- Do not let task completion race with artifact publication or manifest update.
- Do not make externally visible ordering accidentally depend on scheduler timing.
- Do not allow unbounded queues/futures to become hidden memory/storage buffers.
