---
kind: implementation-workplan
workplan_id: PROTOCOL-5.15-LANGUAGE-PROFILES-CPP-PERFORMANCE
protocol_version: 5.14.0
---

# Protocol 5.15 Language Profiles and C++ Performance Engineering Workplan

## Objective / problem invariants / non-goals

### Original problem

Protocol 5.14 is architecturally and methodologically strong but was developed primarily against Python scientific-software experience. Its governing doctrine is largely language-agnostic, while several operational rules in performance, parallelism, property testing, tool routing, and runtime guidance encode Python execution assumptions directly. The protocol therefore lacks an explicit mechanism for preserving one shared engineering doctrine while adapting implementation guidance to materially different language/runtime semantics.

The required product outcome is a single software-development protocol that remains equally valid for Python, C++, and mixed Python/C++ scientific software without duplicating lifecycle doctrine or creating language-specific parallel protocols. The protocol must preserve the existing Tier-1/Tier-2 authority model, active simplicity, evidence-based acceptance, scientific-fidelity safeguards, affected-surface reasoning, and development-economy rules while adding only the language/runtime distinctions needed for correct and performant implementation.

### Product invariants

1. **One protocol, shared doctrine.** Language choice must not fork lifecycle, authority, workplan, acceptance, or simplicity doctrine. The existing Protocol 5 hierarchy, two-role lifecycle, three-tier authority boundary, snapshot-complete handoff, stage/final acceptance, proxy-proof testing, and active Tier-2 simplification remain authoritative and language-agnostic.
2. **Language/runtime-specific execution semantics are explicit.** Rules whose correctness or performance meaning depends on interpreter/runtime/compiler/lifetime/ABI/build semantics must be routed through an explicit language/runtime profile rather than stated as if universal.
3. **Mixed-language composition is first-class.** A repository or affected path may activate more than one profile simultaneously. A Python orchestration layer calling C++ numerical kernels must receive both Python boundary rules and C++ kernel/build rules where applicable.
4. **Performance remains measurement-directed and scientifically constrained.** Algorithmic complexity, data movement, locality, representative profiling, benchmark comparability, resource bounds, numerical invariants, and fidelity precede language-specific micro-optimization.
5. **C++ correctness includes undefined-behavior and lifetime safety.** Performance work must not rely on UB, invalid lifetime/aliasing assumptions, data races, unproven alignment, or build-mode artifacts. Sanitizer/static-analysis evidence is claim-directed and configuration-aware rather than ceremonial.
6. **Compiler/build configuration is part of performance identity for compiled code.** C++ performance evidence must identify enough compiler/toolchain/build/ISA configuration to make comparisons meaningful. Debug builds cannot establish optimized-product performance.
7. **Numerical semantics outrank unsafe optimization flags.** Floating-point reassociation, contraction, reduced precision, fast-math behavior, non-deterministic reductions, or other semantics-affecting optimizations require explicit scientific equivalence/tolerance justification; they are not ordinary free speedups.
8. **No tool monoculture.** The protocol may name useful C++-class tools and evidence modes, but must preserve capability-based routing and concrete fallbacks rather than requiring one compiler, profiler, sanitizer, test framework, or build system globally.

### Non-goals

- Do not create separate `software-design-cpp` / `software-implementation-cpp` roles or duplicate the protocol tree by language.
- Do not prescribe one C++ build system, compiler, standard library, testing framework, profiler, accelerator stack, or parallel runtime.
- Do not turn every C++ change into a performance project, sanitizer matrix, cross-compiler qualification, or ABI audit. Apply language-specific checks proportionately to the affected claim and supported product surface.
- Do not weaken Python guidance merely to make wording superficially language-neutral. Preserve Python-specific rules where Python semantics genuinely require them.
- Do not require hand-written SIMD, custom allocators, templates, metaprogramming, native extensions, LTO, PGO, GPU ports, or similar mechanisms without representative evidence that they solve a material Tier-1 performance/resource requirement.
- Do not treat C++ source-level cleverness as performance evidence.

## Frozen high-level architecture and engineering envelope

### Frozen architecture

1. **Shared core + conditional language/runtime profiles.** Keep lifecycle, authority, testing, scientific correctness, generic performance methodology, storage, security, and orchestration doctrine in existing shared owners. Introduce one compact language/runtime adaptation layer that routes only genuinely language-dependent concerns to profiles.
2. **Profile activation is affected-surface based, not repository-label based.** Determine the relevant profile per material implementation/acceptance surface from the code/runtime/build boundary actually under change. Multiple profiles may apply in one workplan or stage.
3. **Generic performance owner remains canonical.** `performance-and-parallelism.md` continues to own language-independent optimization order, profiling/benchmark discipline, resource budgets, data movement, scaling, accelerator policy, and longitudinal performance evidence. Move or delegate Python-only execution details out of the generic sections instead of cloning the document.
4. **Dedicated Python and C++ profile owners.** Add compact canonical references for Python performance/runtime semantics and C++ performance/runtime/build semantics. The profile documents augment generic owners; they do not restate generic lifecycle or testing doctrine.
5. **Language-sensitive tool routing extends the existing capability model.** Hypothesis remains explicitly Python-specific. Broad invariant/generative testing becomes a language-neutral engineering question whose concrete implementation routes to Hypothesis for Python or an available project-appropriate property/fuzz/generative mechanism for C++. Existing Serena, Semgrep, and CodeQL routing remains capability- and language-support aware.
6. **Protocol 5.15 is a backward-compatible minor strengthening.** It changes no role/lifecycle or governing doctrine. Existing 5.14-bound workplans retain their 5.14 meaning unless explicitly upgraded.

### Engineering envelope

The C++ profile must cover at least the following material classes without turning them into unconditional gates:

- optimized versus debug/instrumented build identity;
- compiler/toolchain/version/flags/target ISA and relevant standard-library/runtime identity in performance evidence;
- RAII/lifetime/ownership and non-owning view contracts;
- undefined behavior, signed overflow where relevant, bounds, alignment, aliasing, use-after-free, data races, and uninitialized-state risks;
- contiguous/strided layout, AoS/SoA choices, cache locality, false sharing, NUMA placement where representative profiling makes them material;
- allocation/copy/move behavior and temporary materialization on hot paths;
- vectorization and compiler optimization evidence, including diagnosing missed vectorization when it is actually performance-limiting;
- threads/OpenMP/TBB-like runtimes/MPI or equivalent parallel layers, oversubscription, nested parallelism, synchronization, and deterministic aggregation;
- floating-point contraction/reassociation/fast-math/mixed-precision/reduction-order semantics;
- ABI/API/shared-library/header-template/ODR implications where affected by the change;
- Python/C++ FFI boundaries when present, including copies, ownership/lifetime, exception translation, GIL behavior where applicable, and cross-boundary batching;
- representative profilers/hardware counters, sanitizers, compiler diagnostics, and static/interprocedural analyzers as claim-directed evidence options.

The Python profile must preserve and organize current valid guidance, including interpreter-loop overhead, NumPy/SciPy/compiled-kernel preference, `numpy.vectorize`/`frompyfunc` non-acceleration, GIL-aware thread/process selection, serialization/process-transfer cost, dtype/layout/materialization concerns, and native/JIT/custom-kernel escalation only after profiling shows a remaining dominant path.

## Implementation obligations and delegated solution space

### O1 — Classify and refactor language-agnostic versus Python-specific performance doctrine

**Concern / rationale:** `performance-and-parallelism.md` currently combines universal optimization policy with Python-specific hot-loop, GIL, process, NumPy/SciPy, `os.cpu_count`, and worker-language wording. This makes Python assumptions appear universal and leaves no clean place for C++ semantics.

**Required end state / constraint:** Rewrite the generic reference so its top-level principles are runtime-neutral: eliminate redundant work, improve algorithms, choose representations/layouts, reduce movement/allocation, exploit optimized kernels/vectorization, add parallelism/accelerators only when justified, profile representative workloads, and benchmark with comparable conditions. Route runtime-specific details explicitly to the relevant profile. Preserve all valid Python behavior through the Python profile rather than deleting it.

**Delegated solution space:** Exact headings and cross-link wording are delegated. Prefer alteration/extraction over adding a second generic performance hierarchy.

**Acceptance evidence:** Source inspection demonstrating no Python-only rule remains phrased as universal in the generic owner; every removed Python-specific rule is preserved in the Python profile or deliberately generalized without semantic loss; role routing still reaches generic performance doctrine and the appropriate profile.

### O2 — Add a minimal language/runtime profile router

**Concern / rationale:** Language adaptation must be deterministic without creating a parallel protocol.

**Required end state / constraint:** Add one canonical shared reference, or an equivalently compact existing-owner extension, that classifies concerns into (a) shared doctrine and (b) language/runtime-sensitive implementation semantics. It must define profile activation by affected semantic/build/runtime surface and allow simultaneous profiles in mixed-language systems.

The router must explicitly distinguish at least:

- interpreted/orchestrating Python code;
- Python numerical code executed predominantly in native/compiled libraries;
- C++ compiled code and libraries;
- mixed Python/C++ boundaries;
- accelerator kernels where device-language/runtime rules may further qualify the host-language profile.

It must state that file extension alone is evidence, not authority: generated code, bindings, embedded interpreters, header-only libraries, CUDA/HIP/SYCL translation units, or mixed build targets may require context-sensitive classification.

**Delegated solution space:** File name and exact taxonomy are delegated. Do not add a manifest/database/profile registry unless needed by the existing skill-build mechanism.

**Acceptance evidence:** Role entrypoints provide a deterministic route to the language profile when implementation/performance/build semantics depend on language/runtime. Qualification or regression scenarios include Python-only, C++-only, and mixed Python/C++ examples and reject the assumption that only one profile may apply.

### O3 — Create the Python performance/runtime profile by preserving existing valid doctrine

**Concern / rationale:** Generalization must not regress Python engineering quality.

**Required end state / constraint:** Consolidate Python-specific rules into a compact profile. Preserve at minimum:

- avoid scalable Python elementwise loops when equivalent compiled/vectorized kernels exist;
- bounded Python orchestration loops remain acceptable;
- `numpy.vectorize`/`frompyfunc` do not constitute acceleration;
- prefer established NumPy/SciPy/framework kernels before custom native code when they satisfy the claim;
- choose threads/processes with explicit GIL, native-kernel release, shared-memory, serialization, and task-granularity reasoning;
- account for dtype, shape/stride/contiguity, broadcasting/materialization, object-dtype and Python-object crossings when they materially affect hot paths;
- avoid process transfer/pickle overhead for large arrays when a lower-movement realization exists;
- escalate to Numba/JIT/Cython/native extension/custom kernels only when representative profiling shows the remaining path warrants the complexity and accepted compatibility envelope permits it.

**Delegated solution space:** Do not canonize a single Python acceleration framework. Existing project dependencies and Tier-1 constraints determine the implementation.

**Acceptance evidence:** Existing Python performance scenarios remain semantically covered after extraction; no regression in current GIL/nested-parallelism/resource-budget guidance.

### O4 — Add the C++ performance/runtime/build profile

**Concern / rationale:** C++ has performance and correctness hazards that do not exist, or do not have the same form, in Python. The protocol currently has no explicit owner for these distinctions.

**Required end state / constraint:** Add a compact C++ profile with the following ordering and safeguards.

1. **Correct optimized baseline first.** Establish correctness in a suitable checked configuration and performance in an optimized production-like configuration. Record compiler/toolchain and material flags/ISA/runtime conditions for benchmark identity. Never compare a debug/instrumented candidate against an optimized baseline as a speedup claim.
2. **Eliminate UB before exploiting optimizer behavior.** Treat invalid lifetime/ownership, out-of-bounds access, invalid aliasing/alignment assumptions, uninitialized reads, signed-overflow dependence, use-after-free, and data races as correctness defects. Use sanitizers/compiler diagnostics/static analysis when they directly model the risk and are available; instrumentation results are correctness evidence, not production-performance measurements.
3. **Prefer data/algorithm wins over low-level tricks.** Preserve the generic optimization order. For C++, explicitly inspect data layout, indirection, allocation frequency, temporary creation, copies/moves, cache locality, branch behavior, and memory bandwidth before hand-written SIMD or micro-architecture-specific code.
4. **Vectorization is evidence-directed.** When hot loops are expected to vectorize, use compiler optimization/vectorization diagnostics or profiler/hardware evidence to determine whether vectorization matters and why it is missed. Do not add `restrict`-like promises, alignment assumptions, intrinsics, or unsafe casts without a proven contract.
5. **Parallelism follows the whole execution stack.** Account for native thread pools, OpenMP/TBB-like runtimes, BLAS, MPI ranks, accelerator launch streams, and nested parallelism. Detect/avoid oversubscription, false sharing, synchronization hot spots, and materially harmful NUMA placement when the target workload exposes them.
6. **Floating-point optimization is a semantic decision.** Fast-math, reassociation, contraction/FMA differences, reciprocal approximations, mixed precision, reduced denormal handling, and changed reduction order require numerical/scientific equivalence evidence appropriate to the accepted invariants. Do not relax tolerances merely to bless an optimization.
7. **Ownership and views are explicit.** Prefer clear ownership/lifetime boundaries and zero-copy views where they reduce movement without creating dangling/aliasing ambiguity. RAII/value semantics are defaults where they simplify correctness; non-owning spans/views require a lifetime owner that remains unambiguous.
8. **ABI/build boundaries are part of the affected surface when material.** Changes to exported layout, inline/header/template code, compile definitions, visibility, exception/RTTI policy, shared-library boundaries, standard-library/toolchain compatibility, or binary interfaces require corresponding compatibility/build/integration reasoning when the product supports those boundaries.
9. **Mixed Python/C++ boundaries are optimized as boundaries.** Account for conversion/copy cost, ownership transfer, buffer/stride compatibility, call granularity, exception mapping, GIL acquisition/release, and batching. Do not optimize a kernel while cross-language dispatch/data conversion remains dominant.
10. **Advanced compiler optimization remains optional and evidence-backed.** LTO, PGO, architecture-specific tuning, custom allocators, explicit prefetching, hand SIMD, and similar techniques are delegated options only after representative profiling and compatibility requirements justify them.

**Delegated solution space:** The profile must not mandate GCC versus Clang versus MSVC, CMake versus Meson/Bazel/etc., OpenMP versus another parallel library, Catch2/GoogleTest/etc., or one profiler. It may give representative examples while keeping the requirement capability-based.

**Acceptance evidence:** Profile text distinguishes correctness instrumentation from optimized benchmark configuration; includes compiler/build identity in benchmark comparability; explicitly protects scientific floating-point semantics; addresses UB/lifetime/aliasing/data race risk; and covers mixed-language boundaries.

### O5 — Generalize property/generative-testing routing without weakening Hypothesis

**Concern / rationale:** Current deterministic routing encodes `broad Python input/state invariant -> Hypothesis`, which is correct but incomplete for C++ and mixed-language work.

**Required end state / constraint:** Keep Hypothesis as the Python-specific method and add a language-neutral parent rule: broad/combinatorial input/state invariants should use an available property/generative/fuzzing method appropriate to the language and claim. For Python, route to Hypothesis. For C++, route to a project-available property/fuzz/generative mechanism or bounded deterministic generation; do not invent a mandatory framework when none exists. Distinguish semantic property testing from memory-safety fuzzing/sanitizer evidence.

**Delegated solution space:** A dedicated C++ property-testing tool reference is optional only if implementation evidence shows enough reusable methodology to justify it. Prefer a compact generic routing extension over a new tool page with no stable tool commitment.

**Acceptance evidence:** README/role/tool-routing qualification no longer implies broad invariant testing is a Python-only capability; existing Hypothesis trigger remains exact and preserved.

### O6 — Extend performance acceptance for compiled C++ comparability

**Concern / rationale:** Existing benchmark doctrine is strong but does not fully identify compiled-build dimensions that can dominate measured results.

**Required end state / constraint:** Extend generic benchmark identity, with profile-specific details where appropriate, so C++ performance claims record material dimensions such as compiler/toolchain version, optimization/build type, target ISA/architecture flags, LTO/PGO state when used, sanitizer/instrumentation absence or presence, relevant parallel runtime/thread settings, and library/backend versions. Only record dimensions that can materially change the claim.

For Python, preserve interpreter/package/backend/dtype/thread/runtime identity where material.

Warm-up, repeated timing, dispersion, same-input comparison, memory/I/O/scaling evidence, and scientific equivalence remain shared requirements.

**Acceptance evidence:** A qualification scenario rejects a C++ benchmark comparison where baseline and candidate use materially incomparable build modes, while allowing still-valid evidence reuse when only irrelevant dimensions changed.

### O7 — Add C++-specific correctness and concurrency validation guidance without creating universal gates

**Concern / rationale:** C++ optimization frequently exposes defects through UB, race, aliasing, or lifetime behavior that ordinary unit tests may miss.

**Required end state / constraint:** Update testing/performance/tool guidance so affected C++ claims consider, proportionately:

- AddressSanitizer-like memory/lifetime/bounds checking;
- UndefinedBehaviorSanitizer-like UB checking;
- ThreadSanitizer-like race checking for material threaded ownership/synchronization changes;
- compiler high-warning/static diagnostics and existing project analyzers;
- Semgrep for structural patterns where supported;
- CodeQL when supported extraction/data-flow/interprocedural relations directly model the claim;
- fuzz/property/generative testing for broad input/state surfaces.

No sanitizer/analyzer is globally mandatory. A tool becomes required only when project policy or an accepted task-specific claim makes it so. Unsupported toolchain/platform combinations require explicit fallback evidence, not counterfeit pass status.

**Acceptance evidence:** Role/tool guidance can distinguish (a) ordinary C++ feature work, (b) memory/lifetime-risk work, (c) threaded race-risk work, and (d) performance-only benchmarking, without routing all four through the same fixed pipeline.

### O8 — Reconcile packaging/build/ABI guidance for compiled artifacts

**Concern / rationale:** `release-and-distribution.md` correctly requires validating what users receive, but compiled products have build/link/load/ABI dimensions absent from pure Python package flows.

**Required end state / constraint:** Add concise compiled-artifact guidance: build the supported optimized artifact, exercise the installed/linked/loaded consumer path, validate required runtime/shared-library dependencies and exported interfaces where governed, and test supported compiler/platform/ABI combinations according to actual release scope. Header-only/template changes require rebuilding affected consumers where needed to establish compatibility. Mixed Python extension artifacts must be tested through the packaged Python import/call path rather than source-tree-only execution.

**Delegated solution space:** Do not prescribe wheel format, CMake, Conan/vcpkg, package managers, symbol-versioning schemes, or universal ABI stability where the project does not promise them.

**Acceptance evidence:** Release guidance has a compiled-artifact path while retaining existing language-neutral shipped-artifact rules.

### O9 — Update skill packaging, routing text, qualification, and protocol version coherently

**Concern / rationale:** New canonical references must actually ship with relevant skills and routing must be exercised, not merely documented.

**Required end state / constraint:**

- bump protocol source to `5.15.0`;
- update protocol-versioning/README summaries to identify 5.15 as a backward-compatible language/runtime-profile and C++ performance-engineering strengthening;
- include new profile references in the minimum relevant role bundles through `source/build_skills.py` without duplicating them into unrelated specialists unless their routing requires them;
- update role entrypoints so performance/build/runtime-sensitive work reads the generic owner and relevant language profile;
- update portability/tool-routing qualification/tests for Python-only, C++-only, and mixed-language routing;
- regenerate committed `dist/` artifacts from canonical `source/` and preserve source-to-generated parity.

**Delegated solution space:** Whether both profiles ship to both core roles or a compact router plus both profiles is smaller overall should be decided by package-size/context-economy evidence. Prefer the simplest arrangement that allows deterministic local routing in installed skill bundles.

**Acceptance evidence:** Repository canonical acceptance sequence succeeds, generated distributions contain every routed reference they need, and no role links to an absent profile.

## Implementation authority

### Frozen

- Protocol 5 hierarchy and two-role lifecycle remain unchanged.
- One shared language-agnostic doctrine with conditional language/runtime profiles; no parallel Python/C++ protocols.
- Profile activation follows affected semantic/runtime/build surfaces and may activate multiple profiles in mixed-language work.
- Generic performance/scientific/testing doctrine remains canonical; profiles augment rather than duplicate it.
- Python-specific performance behavior currently relied on remains preserved after refactoring.
- C++ profile must cover optimized-build identity, UB/lifetime/race safety, data layout/allocation/locality, vectorization evidence, whole-stack parallelism, numerical/fast-math semantics, ABI/build boundaries, and Python/C++ FFI performance/correctness.
- Protocol target is 5.15.0 and is backward-compatible with earlier Protocol 5 workplans by explicit version binding.

### Delegated

- Exact reference file names, headings, examples, and cross-link wording.
- Exact C++ tools/frameworks used as examples.
- Whether generative/property guidance receives a new dedicated generic reference or remains in testing/tool-assisted engineering, provided deterministic routing is clear and Hypothesis remains correctly scoped.
- Whether Python and C++ profiles are separate files or one clearly partitioned language-runtime reference, provided progressive disclosure and context economy remain strong. Separate compact profiles are preferred if they reduce irrelevant load.
- Specific C++ optimization techniques, allocators, SIMD mechanisms, build systems, profilers, and parallel frameworks for any downstream project.

### Reopen only on evidence

Reopen Design only if implementation evidence shows one of these Frozen decisions cannot be satisfied cleanly:

- installed skill packaging cannot support deterministic conditional profile routing without materially duplicating always-loaded context;
- a shared generic performance owner cannot be disentangled from Python semantics without substantial semantic regression;
- mixed-language routing requires a materially different lifecycle/authority model rather than simultaneous profiles;
- protocol packaging constraints make separate profiles materially more complex than a single partitioned owner.

Do not reopen merely because one C++ project uses an unusual compiler/build system or lacks a named optional tool; those are delegated/tool-fallback concerns.

## Affected surface and task-specific acceptance

Expected affected canonical source:

- `source/PROTOCOL_VERSION`;
- `source/README.md`;
- `source/roles/software-design/SKILL.md`;
- `source/roles/software-implementation/SKILL.md`;
- `source/shared/references/performance-and-parallelism.md`;
- new or refactored language/runtime profile reference(s);
- `source/shared/references/testing-and-validation.md` where generative/sanitizer/build-mode acceptance needs language-sensitive qualification;
- `source/shared/references/tool-assisted-engineering.md` and `tool-hypothesis.md` as needed for generalized invariant routing while preserving Python specificity;
- `source/shared/references/release-and-distribution.md` for compiled-artifact integration/ABI scope;
- `source/shared/references/protocol-versioning-and-compatibility.md`;
- `source/build_skills.py`;
- affected portability/qualification tests and scenarios;
- generated `dist/` bundles and indexes.

Potentially affected, only if implementation reveals real ownership:

- `scientific-software.md` for floating-point optimization cross-routing, though generic numerical invariants/tolerances should remain there rather than moving into C++;
- `concurrency-and-orchestration.md` for a cross-link to C++ native-thread/runtime concerns, without duplicating orchestration correctness;
- Semgrep/CodeQL method pages only if C++ support/fallback wording is materially ambiguous after profile integration;
- repository README/PORTABILITY documentation if user-facing routing examples become stale.

Task-specific acceptance must include:

1. **Doctrine preservation review:** verify no language profile redefines Tier-1/Tier-2, lifecycle, simplicity, workplan, or acceptance rules.
2. **Python regression:** existing Python performance/GIL/NumPy/process guidance remains reachable and semantically intact.
3. **C++ routing scenario:** a representative C++ numerical-kernel performance task reaches generic performance + C++ profile + scientific fidelity, without loading Python-only Hypothesis/GIL rules as universal requirements.
4. **Mixed-language scenario:** a Python binding over a C++ kernel activates Python boundary concerns and C++ compiled-kernel/build concerns simultaneously.
5. **Build-comparability scenario:** reject a benchmark conclusion based on debug/instrumented versus optimized build mismatch.
6. **Numerical-semantics scenario:** reject enabling fast-math/reassociation solely for speed when accepted scientific equivalence has not been established.
7. **Safety-tool routing scenario:** a C++ lifetime/memory-risk question may route to available sanitizer/static-analysis evidence without making sanitizers universal; a threaded race-risk question distinguishes race tooling from ordinary performance profiling.
8. **Package-integrity checks:** build/validate/check generated skill bundles and ensure all routed references ship in every role that references them.
9. **Repository-required final commands:** run the canonical Protocol 5.15 equivalent of:

```bash
python -m pip install -r source/requirements-validation.txt
python -m unittest discover -s tests -v
python source/build_skills.py --output /tmp/protocol-dist
python source/validate_packages.py --dist /tmp/protocol-dist
python source/check_dist.py --expected /tmp/protocol-dist --committed dist
git diff --check
```

Production qualification: unnecessary for the protocol repository itself. Representative routing/semantic qualification is required; downstream C++ products inherit their own target-hardware performance qualification requirements from generic protocol doctrine.

## Implementation sequence and genuine redesign / simplification triggers

### Stage 1 — Semantic census and extraction boundary

Re-read the current canonical references and classify every language-sensitive sentence in performance/tool/testing/release guidance as shared, Python-specific, C++-missing, or project-specific. Establish the smallest profile boundary before editing. Do not begin by adding C++ rules beside Python rules in the generic owner.

Close the stage with source-level conformance review and targeted protocol tests for existing generic/Python semantics.

### Stage 2 — Introduce profile routing and refactor Python guidance

Create the router/profile ownership structure, move/generalize Python-only rules out of the generic owner, update role routing, and preserve current Python semantics. Close focused routing/packaging tests before adding C++ breadth so regressions remain attributable.

### Stage 3 — Add C++ profile and compiled-artifact acceptance

Implement the C++ runtime/build/performance rules and minimal release/testing cross-links. Add qualification scenarios for optimized build identity, UB/lifetime/race routing, numerical semantics, mixed-language boundaries, and benchmark comparability.

### Stage 4 — Generalize invariant/property routing

Introduce the language-neutral parent routing for broad/combinatorial invariants while retaining Hypothesis as the Python-specific concrete method. Avoid inventing a mandatory C++ property framework.

### Stage 5 — Version/package reconciliation and final acceptance

Bump to 5.15.0, update version history/README/user-facing routing examples, regenerate `dist/`, re-derive the final affected surface, run complete affected regression and repository-required integration/package checks, and inspect generated bundles for reference completeness.

### Active simplification triggers

Before adding another reference, router, registry, or tool page, simplify/re-derive if implementation begins to show any of:

- duplicated generic doctrine across Python and C++ profiles;
- two parallel role-routing trees differing mostly by language;
- a growing language-profile registry whose only purpose is dispatching markdown;
- repeated cross-links required because ownership is unclear;
- generic performance guidance still containing Python branches intermixed with C++ branches after profiles exist;
- qualification tests asserting exact wording/file identity rather than semantic routing, causing documentation structure to ossify.

Prefer consolidating ownership or reducing profile machinery over preserving such structures.

### Genuine redesign triggers

Return to Software Design only if evidence demonstrates that mixed-language projects cannot be represented as shared doctrine plus simultaneous profiles, or that installed-skill progressive disclosure cannot deliver profiles without unacceptable context duplication. An individual compiler/tool/framework incompatibility is not a redesign trigger.

## Design verdict

**PASS — ready for implementation.**

The plan preserves Protocol 5.14's governing architecture and solves the actual gap by separating universal engineering doctrine from runtime-specific execution semantics. The critical constraint is to refactor existing Python assumptions into a profile rather than layering C++ exceptions into the generic performance document. The C++ additions are intentionally capability- and evidence-based: they strengthen performance, numerical integrity, memory/lifetime correctness, build comparability, and mixed-language engineering without imposing one toolchain or creating a second protocol.
