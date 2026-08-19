# Performance, Memory, Data Movement, Parallelism, and Accelerators

## Optimization order

Optimize in this order unless profiling provides a strong reason otherwise:

1. remove redundant work and repeated I/O/parsing/serialization;
2. improve asymptotic algorithm or search space;
3. improve data representation/layout and reuse/caching with explicit validity;
4. batch work to reduce dispatch and allocation overhead;
5. use vectorized/compiled library kernels;
6. reduce temporary allocations/copies and improve locality;
7. add CPU concurrency for genuinely independent work;
8. add GPU/accelerator execution when transfer/runtime overhead is amortized;
9. consider compiled custom kernels/extensions for remaining dominant irregular paths.

Do not optimize from intuition alone when representative profiling is available.

Treat predicted wall time as an observability/planning estimate unless the user or project explicitly defines it as an SLA/admission contract. A benchmark-derived runtime estimate is not a physical safety limit like memory or disk capacity and should not by itself reject otherwise valid work.

## Hot-path policy

- Avoid Python elementwise loops whose count scales with large dense numerical dimensions (frames*atoms, voxels, pair candidates, matrix rows) when equivalent compiled kernels exist.
- Permit bounded orchestration loops over species, fields, chunks, connected components, stages, or irregular graph states.
- Do not convert irregular sparse/combinatorial algorithms into dense arrays solely to satisfy a "no loops" rule.
- Treat `numpy.vectorize`/`frompyfunc` as convenience wrappers, not acceleration.
- Prefer established NumPy/SciPy/optimized-library primitives before custom native code.
- When replacing a hot path, protect the intended implementation form with an appropriate regression/static check only if that form is a real project contract.

## I/O and data movement

For disk-heavy persistence, caches/checkpoints, scratch sizing, or restart behavior, also read `storage-and-io.md`.

- Parse/read immutable inputs once per logical operation when possible.
- Reuse normalized/canonical intermediate forms rather than reopening files in inner loops.
- Stream/chunk when data exceeds comfortable memory, but ensure chunking does not change reduction semantics or ordering.
- Avoid serializing large intermediates between workers when shared/read-only memory, threads over GIL-releasing kernels, memory mapping, or staged pipelines are more efficient.
- Include host-device transfer and synchronization in accelerator timing.
- Include serialization, cold-load, write-back, cache construction, and recovery time when those costs are part of the user-visible stage.
- Treat I/O concurrency as a separate saturation domain; more CPU workers can make a storage-bound workload slower.

## Resource discovery

Use the effective allocation, not machine marketing specifications.

CPU candidates can include:

- process affinity (`sched_getaffinity` on Linux);
- cgroup or container CPU quota;
- scheduler-provided limits/environment;
- explicit user configuration;
- `os.cpu_count()` only as one upper-bound signal.

Memory candidates can include:

- currently available host RAM;
- cgroup/container available memory;
- explicit job limits;
- per-task measured peak or a conservative estimate.

Accelerator discovery should record device availability, selected device, free/total memory, runtime/library capability, and reason for fallback.

## Default budgets

Use configurable defaults rather than hard-coding machine saturation:

- CPU target: at most about `0.90 * effective_cpu_threads`, rounded conservatively and never below one worker/thread when work exists.
- System RAM admission: keep estimated/measured peak at or below about `0.80 * currently_available_ram` unless the project/user defines a different bound.
- GPU/accelerator memory: keep meaningful headroom; a `<=0.90` fraction of currently free/allocatable VRAM is a reasonable soft ceiling when no project-specific policy exists.

These are upper budgets, not targets. Use fewer resources when throughput saturates, memory estimates are weak, latency/responsiveness matters, CI is shared, or nested parallelism would oversubscribe.

## Nested parallelism

Model the whole stage, not each library independently.

Approximate CPU demand as outer workers multiplied by the dominant inner native/threaded demand. Control BLAS/OpenMP/PyTorch/tree-search threads when spawning process/thread workers. Avoid configurations such as 16 Python workers each launching 16 BLAS threads on a 16-core allocation.

Prefer one explicit stage resource plan containing:

- effective CPU allocation and CPU budget;
- outer Python/process/thread workers;
- inner structural/library workers;
- BLAS/OpenMP threads;
- framework-specific CPU workers;
- concurrent GPU jobs;
- RAM/VRAM budget and per-task estimate;
- I/O worker/concurrency budget, scratch/storage location, and expected peak disk footprint when material.

Print or emit the plan for long-running user-facing workflows, but keep library numerical kernels decoupled from stdout. Use structured progress/diagnostics when available.

## Choosing threads vs processes

- Use threads when dominant work releases the GIL, shares large read-only arrays efficiently, or process serialization would dominate.
- Use processes for CPU-bound Python code when state can be partitioned cheaply and safely.
- Avoid blindly parallelizing tiny tasks; batch to amortize scheduling overhead.
- Maintain deterministic aggregation/order where externally visible.
- Make worker count overrideable and allow serial execution for debugging/reproducibility.

## GPU/accelerator policy

Add an accelerator backend only when:

1. supported hardware/runtime is detected reliably;
2. the workload is sufficiently large/parallel to amortize transfers and launch overhead;
3. required operations are supported without expensive device-host ping-pong;
4. peak VRAM is bounded or adaptive batching/backoff exists;
5. CPU/reference equivalence is verified within accepted tolerance;
6. fallback behavior is explicit and tested;
7. representative benchmark evidence shows a material benefit.

Do not force GPU use merely because a GPU exists. Record backend/device/precision/batch configuration in performance evidence.

For OOM-sensitive pipelines, reduce batch/concurrency on OOM when retry is semantically safe, but cap retries and surface the final failure clearly.

## Benchmark acceptance

Before calling an optimization successful, provide:

- baseline and candidate on the same representative inputs/environment;
- correctness/equivalence result;
- repeated wall-time evidence;
- peak or bounded memory evidence when relevant;
- I/O bytes/footprint and cold/warm/recovery evidence when storage behavior is relevant;
- scaling behavior for at least enough sizes/workers to expose the intended trend;
- explanation of regressions/tradeoffs;
- conservative default/auto-selection rule, if any.

Do not accept speedup obtained by lowering scientific resolution, changing estimator semantics, weakening validation, changing precision policy without approval, omitting output, or moving work outside the timed region.

Existing expensive baseline evidence may be reused instead of rerun when its source/input/benchmark-method/environment identity remains compatible with the current workplan's comparability contract. Record the reused evidence identity explicitly. A new agent session or later date is not by itself a reason to repeat a valid expensive baseline, and a convenient but non-comparable old measurement is not a valid substitute.

## Longitudinal performance regression tracking

For mature hot paths or workflows whose performance materially matters, keep stable benchmark scenarios in addition to one-change before/after measurements.

Record enough baseline identity to compare fairly:

- source/package version and benchmark revision;
- representative input identity/size/distribution;
- hardware/runtime/backend/precision;
- CPU/thread/worker and GPU-job configuration;
- warm-up/repeat methodology;
- wall time/throughput and dispersion;
- peak RAM/VRAM;
- bytes read/written, recovery time, and retained disk footprint when material.

Define an acceptable regression band appropriate to measurement noise and user impact. Do not silently replace the baseline after a regression; record why a new baseline is accepted (intentional tradeoff, hardware/toolchain change, benchmark correction, or genuine new reference implementation).

Track trends separately from gate-local optimization claims so gradual performance loss across many individually small changes remains visible.
