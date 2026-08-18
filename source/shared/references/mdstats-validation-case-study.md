# mdstats Validation Case Study

This reference documents how the protocol was pressure-tested against the uploaded `mdstats 0.20.239a0` source tree. It is an example, not a project-specific requirement for other repositories.

## Repository scale observed

Static inspection found approximately:

- 361 Python files under `mdstats/`;
- 487 `test_*.py` modules;
- 588 Markdown files under `docs/`;
- 44 Python benchmark programs;
- separate `audits/`, `benchmarks/`, `docs/arch_manuals/`, `docs/specs/`, `release/`, `tests/`, and `tools/` areas;
- several large orchestration modules, including `training_data/campaign_cli.py` at more than 1 MB.

This scale makes indiscriminate whole-repository context loading and broad rewrites unsafe. It motivated the repository-intake/change-surface workflow and progressive reference loading.

## Architecture and workplan lesson

Earlier mdstats architecture manuals often embedded implementation stages directly in the architecture document. The periodic-neighbor work nevertheless demonstrated a strong **execution pattern**: baseline/oracle first, explicit compatible capability second, state reuse after correctness, hard/resource cases next, and automatic/default policy only after equivalence and benchmark evidence.

Protocol v2 preserves that execution discipline but moves the temporary gate sequence into an **Implementation Workplan**. The architecture manual now owns only the accepted current structure and invariants. This avoids growing a permanent architecture manual with every optimization/revision gate while preserving the useful staged acceptance behavior.

## Documentation ownership validated

`docs/specs/documentation/architecture_manual_ownership_spec.md` distinguishes normative architecture parts from descriptive status history and requires source/PDF parity for maintained pairs. `docs/arch_manuals/README.md` separates architecture manuals from module specifications and points MLFF architecture to assembled chapter sources plus a machine-readable dependency graph.

This validates:

- one normative owner per current architecture/contract, with implementation workplans as temporary execution authority;
- history not redefining current architecture;
- generated/assembled source ownership;
- Markdown/PDF regeneration and parity checks where the repository requires them.

## Performance policy validated

`docs/specs/performance/interpreter_hotpath_policy.md` prohibits dense elementwise Python loops in registered numerical hot paths while explicitly allowing bounded orchestration and irregular graph algorithms. It requires correctness equivalence, deterministic ordering, focused tests, representative microbenchmarks, and memory accounting before accepting a rewrite.

This validates the skill's distinction between dense numerical kernels and irregular algorithms, and the rule that vectorization syntax alone is not a performance objective.

## Resource planning validated

`mdstats/training_data/resources.py` detects effective CPU limits using host count, Linux affinity, and cgroup quotas; bounds RAM from host/cgroup availability; detects GPU resources; and represents nested parallelism with an explicit stage resource scope. The project uses configurable resource fractions and avoids independent worker/thread settings multiplying without a stage budget.

This validates revising the source prompt's "use 90% of threads" into a configurable upper budget based on effective allocation, plus explicit nested-thread and memory admission control.

## Observability validated

`docs/specs/progress_spec.md` defines a structured progress port and keeps computational modules decoupled from stdout/logging configuration. Progress is observational and must not influence scientific results, backend selection, or resource admission.

This validates replacing a generic "print informative messages" rule with structured, caller-controlled progress/diagnostics for library-scale code.

## Benchmark discipline validated

`benchmarks/neighbor_search_benchmark.py` warms up before timing, uses repeated measurements with median wall time, compares optimized results to the reference implementation, records workload and memory-related metrics, and states that its threshold is a conservative default rather than a universal hardware result.

This validates the benchmark-evidence and conservative-auto-policy rules.

## Stress-case conclusions

The protocol should therefore require, for large scientific repositories:

- progressive subsystem mapping instead of repository-wide editing;
- explicit ownership between architecture/spec/history/evidence;
- oracle-based numerical equivalence before optimization;
- resource scopes that understand nested parallelism and container/HPC limits;
- final observable regression beyond kernel tests;
- documentation/generated-artifact closeout as a release gate;
- target-hardware qualification kept distinct from development-host validation.

## Storage, cache, and recovery lessons from later mdstats/MLFF work

Subsequent large-data mdstats/MLFF campaign work exposed a resource class not captured by CPU/RAM/GPU/VRAM alone: persisted indexing/caching and restart cost.

Representative failure/pressure patterns included:

- very large neighbor/reference index structures where a cache hit can skip expensive geometry work but still requires substantial file-backed state and recovery/load cost;
- lineage/plan/feature-metric mismatches where stale persisted state must be rejected rather than reused merely because files exist;
- long-running campaign stages where append-only recovery state is useful only if replay/compaction keeps restart time bounded;
- density workflows where a logically dense representation would be enormous even though the scientifically occupied region is sparse, motivating storage/memory representations that preserve the estimator while avoiding full materialization;
- resource schedulers that must account for storage contention and scratch footprint in addition to worker count and memory.

These cases validate the protocol's storage rules:

- classify durable outputs, checkpoints, caches/indexes, and scratch separately;
- bind caches/checkpoints to source/config/schema/algorithm identity;
- measure cache-build, warm-load, cold-load, and restart/recovery time rather than only steady-state kernels;
- preflight expected peak disk footprint and preserve free-space/quota headroom;
- compact journals or secondary state so resume time cannot grow without bound;
- avoid duplicating massive forward/inverse or transformed structures unless the saved computation/recovery time justifies the footprint;
- treat I/O concurrency as a bottleneck that can cap useful CPU parallelism.

## Debugging/state-lineage lessons

The same project repeatedly demonstrated that production failures can originate outside the final exception site. Robust diagnosis therefore traces the entry point, policy/backend resolution, data lineage, cache/checkpoint identity, dependency environment, and final consumer before editing. A successful fallback is not proof that the requested accelerator/backend was qualified, and deleting stale state until a run proceeds is not a root-cause fix. The protocol therefore keeps debugging/state recovery as a dedicated engineering concern rather than folding all failures into generic unit testing.

## Security/trust-boundary lessons from scientific development workflows

The collaboration also repeatedly crosses boundaries that are easy to mistake for ordinary scientific data handling:

- dependency archives and complete source-package ZIP/TAR files are externally supplied archives and should be inspected/extracted into controlled scratch roots rather than blindly unpacked over a working tree;
- Python/Torch/MACE/LAMMPS model/checkpoint artifacts can enter deserialization/code-loading paths, so their provenance/trust is materially different from plain numerical arrays;
- package installation, native extension builds, CUDA/C++ toolchains, and editable/source installs execute third-party build code and therefore are trust/supply-chain operations rather than passive dependency reads;
- very large uploaded trajectories/training sets should be treated as immutable external inputs, with derived caches/indexes written to owned scratch/output locations;
- generated HTML/PDF visualization/document artifacts can reference files/resources and should not be allowed to escape project-approved read/write roots;
- diagnostic bundles, logs, environment dumps, and packaged source archives require a secret/private-data review before sharing or committing.

These cases validate making trust modeling explicit even for an internal research code base. "Scientific input" does not imply "safe to execute or deserialize," and a convenient package/model loader is not automatically a safe boundary for untrusted artifacts.

## Documentation, workplan, and version-history lessons

The mdstats development sequence exposed why the old single-manual model does not scale:

- implementation often proceeds through many named engineering gates and rapidly changing alpha revisions;
- temporary gate status can change much faster than architecture, so recording every `PLANNED`/`IN PROGRESS`/`COMPLETE` state in architecture manuals inflates and destabilizes them;
- later implementation can invalidate a proposed design, so proposed semantics should stay in a revisioned workplan until accepted rather than being written early into current specifications/architecture;
- specifications need to remain a trustworthy description of accepted current behavior, not a mixture of current and future contracts;
- architecture manuals should change when the accepted architecture changes, not merely because another implementation gate completed;
- history/changelog/version records are the durable place to state what actually shipped and when;
- revised permanent Markdown documentation must still be integrated into the complete source package and kept synchronized with generated PDFs/provenance manifests.

These observations motivate the v2 Chat/Codex split: Chat/design-review performs the broad inspection, diagnosis, algorithm selection, and workplan revision; Codex/implementation performs bounded revalidation, code changes, tests/benchmarks, and normative closeout. The workplan is the versioned interface between those roles, while architecture/specification remain current-state authorities.

