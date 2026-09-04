---
kind: implementation-workplan
workplan_id: PROTOCOL-5.15-LANGUAGE-PROFILES-CPP-PERFORMANCE
protocol_version: 5.14.0
---

# Protocol 5.15 Language Engineering Profiles and Cross-Language Performance Workplan

## Objective / problem invariants / non-goals

### Original problem

Protocol 5.14 has a strong language-agnostic engineering doctrine, but it was developed primarily in Python scientific-software work. Most of its governing principles already transfer cleanly to C++, while some operational guidance encodes Python execution assumptions directly and the current Protocol 5.15 draft over-corrects by placing several actually language-agnostic performance concepts inside the C++ profile.

The required outcome is one protocol that is structurally capable of producing excellent Python, C++, and mixed Python/C++ software while preserving all prior Protocol 5 doctrine. Shared references must continue to own the durable engineering principles; language profiles must contain only the justified consequences of each language/runtime/build model. The skills should optimize product performance and engineering quality using the minimum justified code/system complexity rather than either (a) translating Python habits into C++, (b) forcing C++ machinery into Python, or (c) duplicating shared doctrine across language branches.

### Product invariants

1. **One protocol, one doctrine.** Product truth, Tier-1/Frozen/Tier-2 authority, active simplicity, workplan semantics, affected-surface reasoning, proxy-proof acceptance, scientific correctness, security, storage, release, documentation, convergence, and development-economy rules remain language-agnostic and canonical.
2. **Shared owner before language specialization.** A language profile may refine how a shared requirement is realized; it must not redefine, weaken, duplicate, or outrank the shared requirement.
3. **Language-native engineering.** Python code should exploit Python's high-level runtime/library strengths; C++ code should exploit C++'s static type/lifetime/value/compile-time and native-performance strengths. Equivalent product behavior does not imply mechanically similar source structure.
4. **Performance-aware by default, complexity escalation by evidence.** Prefer obviously lower-work/lower-movement/lower-allocation and established optimized primitives when they do not materially increase complexity. Require representative evidence before adding durable complexity such as bespoke SIMD, new parallel runtimes, architecture-specific dispatch, PGO/LTO policy, custom allocators, cross-language rewrites, or accelerator backends.
5. **Minimum justified codebase/system complexity remains lexicographically below product fitness.** Performance improvements that materially complicate ownership, portability, build/release, failure behavior, or scientific semantics must justify their total-system cost; convenience or fewer source lines does not excuse poor runtime fitness.
6. **Mixed-language composition is first-class.** A Python orchestration/API layer plus C++ kernels may activate both profiles. Boundary cost, ownership, error translation, build/package integration, and data movement are part of the architecture rather than incidental glue.
7. **Capability-based tool routing remains shared.** Tool choice follows the relation under the engineering claim. Language profiles map generic capability classes to appropriate language-specific tools and build/runtime evidence.
8. **Scientific semantics remain authoritative over optimization.** Backend replacement, vectorization, parallel reduction, compiler floating-point transforms, mixed precision, and accelerators require accepted exact/tolerance/invariant evidence where they can change scientific results.
9. **CPU performance mechanisms are ordinary supported capabilities, not universal product requirements.** Tuned kernels, vectorization, shared-memory concurrency, process isolation, and distributed execution are selected by workload/architecture, not enabled merely because modern machines support them.
10. **GPU/accelerator support is architecture-gated.** GPU probing, dependencies, implementation, profiling, and qualification activate only when accelerator support is a Tier-1 requirement or explicitly Frozen architecture decision.
11. **Tool/backend identities remain delegated unless independently governed.** Serena, clangd, sanitizers, BLAS vendors, MPI implementations, profilers, and similar mechanisms are preferred or routed because of capability, not promoted into Tier 1 through protocol wording.

### Non-goals

- Do not create separate Python/C++ lifecycle roles, duplicated protocol trees, or language-specific copies of generic architecture/testing/scientific/security doctrine.
- Do not require every C++ project to use OpenMP, MPI, intrinsics, LTO, PGO, sanitizers, multiple numerical backends, or GPU support.
- Do not require every Python project to use NumPy, multiprocessing, JIT compilation, native extensions, or a particular framework when the workload does not justify them.
- Do not prescribe one compiler, standard library, build system, test framework, debugger, profiler, BLAS/FFT implementation, MPI implementation, property-testing library, or accelerator stack globally.
- Do not move clearly language-agnostic principles into profiles merely because their current examples arose in Python or C++.
- Do not retain language-specific hard requirements in generic shared references when the same requirement can be stated generically and specialized in a profile.
- Do not create a reference page per tool or optimization technique without independent methodological value.

## Frozen high-level architecture and engineering envelope

### Frozen architecture

Protocol 5.15 uses three layers:

```text
shared doctrine / domain owners
        |
        v
thin language-profile routing
        |
        +--> Python engineering profile
        +--> C++ engineering profile
        +--> both for mixed-language boundaries
```

1. **Shared canonical owners remain authoritative.** Existing references continue to own workflow/workplans, architecture/simplicity, testing/acceptance, tool-capability selection, performance/scaling, concurrency/orchestration, scientific fidelity, storage/I/O, security/trust, release/distribution, configuration, documentation, and protocol versioning.
2. **Add one thin language-profile router plus compact Python and C++ engineering profiles.** The router classifies affected runtime/build surfaces and sends only language-dependent questions to the relevant profile(s). It must not become a second policy layer.
3. **Profiles are differential.** They contain language/runtime/build-specific idioms, hazards, tools, packaging, and optimization realizations. They inherit shared doctrine by reference and do not restate it except for short local cross-links needed to explain the specialization.
4. **Shared performance owns the conceptual optimization hierarchy.** Generic performance doctrine owns algorithm/work reduction, data representation/movement/locality, established optimized kernels, vectorization as a capability, parallelism classes and oversubscription, accelerator gating, benchmark comparability, and performance-versus-complexity evidence. Profiles map those concepts into Python- and C++-appropriate realization.
5. **Shared concurrency owns execution-class semantics.** Shared-memory execution, process isolation, distributed-memory execution, nested parallelism, failure/cancellation, resource ownership, and deterministic aggregation are generic concepts. Python and C++ profiles explain how their runtime models change the preferred mechanisms.
6. **Shared tool-assisted engineering owns relation classes.** Semantic navigation, structural analysis, broad invariant generation, interprocedural flow, runtime state, memory/resource diagnosis, race diagnosis, and performance diagnosis are capability classes. Existing generic tool methods remain canonical where cross-language; profile-local methods cover genuinely language-specific evidence.
7. **Language-specific normative content is not allowed to leak into shared references without qualification.** A shared reference may use Python/C++ examples, but the durable rule must be stated generically. Tool-specific references such as Hypothesis may remain intentionally language-specific because their subject is the tool itself.
8. **Mixed-language composition uses simultaneous profiles, not a third lifecycle.** Boundary-specific rules live in the thin router or a compact shared boundary section; they must not duplicate both full profiles.
9. **Protocol 5.15 is a backward-compatible minor strengthening.** It changes no lifecycle or governing doctrine and does not reinterpret older workplans implicitly.

### Shared engineering envelope: performance with minimum justified complexity

The shared performance owner must distinguish two optimization classes.

**Efficiency by construction — no benchmark prerequisite when the choice is clearly semantically equivalent and does not add material complexity:**

- eliminate redundant work, parsing, I/O, copies, allocation, conversions, and synchronization;
- select appropriate asymptotic algorithms/data structures;
- preserve locality and avoid unnecessary materialization;
- reuse established optimized library primitives already compatible with the product;
- batch or stream work where doing so simplifies or preserves the architecture;
- avoid accidental nested oversubscription.

**Complexity-increasing optimization — representative evidence required before durable adoption:**

- new bespoke native kernels or language boundaries;
- explicit SIMD/intrinsics or architecture dispatch machinery;
- additional thread/process/MPI runtimes or hybrid parallel layers;
- custom allocation/pooling solely for speed;
- LTO/PGO as a governed build/release dependency rather than a local compiler experiment;
- backend proliferation or fallback matrices;
- accelerator implementation;
- scientific approximation/precision changes.

The benchmark must measure the user-visible or materially owning path and include the complexity/portability/resource tradeoff, not merely kernel throughput.

### Python engineering profile envelope

The Python profile must optimize for Python's actual strengths and costs rather than emulate C++.

- Prefer clear high-level language/standard-library/project abstractions; use context managers and deterministic resource scopes where they simplify lifetime handling; use iterators/generators/streaming where they reduce materialization; use data classes/protocol/type annotations or equivalent constructs when they improve API clarity without creating parallel schema machinery.
- Avoid unnecessary dynamic metaprogramming, reflection, wrapper layers, object churn, or abstraction whose only effect is indirection.
- Keep large dense numerical work in established compiled/vectorized kernels where practical. Treat NumPy/SciPy/framework operations as compiled execution only when they actually avoid Python elementwise work; `numpy.vectorize`/`frompyfunc` remain convenience, not acceleration.
- Account for dtype, shape, stride, contiguity, broadcasting, temporary arrays, Python-object crossings, serialization, and FFI copies on hot paths.
- Choose threads when dominant work releases the GIL or is I/O/shared-read-heavy; choose processes for genuinely Python-bytecode-bound CPU work when serialization/duplication cost is acceptable; do not copy C++'s thread-first assumptions into Python.
- Escalate to JIT/native extension/Cython-like/custom C++ kernels only when the remaining bottleneck and total integration cost justify it.
- Use Python-appropriate runtime/debug/profiling evidence when needed: debugger-class tools for runtime state, `tracemalloc`/allocation-memory profilers for resource questions, sampling or Python profilers for CPU hotspots, and Hypothesis for broad property/state invariants. Exact tools remain delegated.
- Preserve normal Python packaging/import/environment semantics and test the installed/packaged consumer path where release claims depend on them.

### C++ engineering profile envelope

The C++ profile must optimize for C++'s actual strengths and hazards rather than emulate Python.

- Prefer RAII, explicit ownership, value semantics, const-correct interfaces, moves, spans/views, standard containers/algorithms, and clear lifetime boundaries when they reduce complexity and data movement.
- Prefer stack/value ownership and deterministic destruction when semantically appropriate; do not introduce manual `new`/`delete`, raw owning pointers, custom ownership protocols, or bespoke allocators without a material need.
- Use templates/concepts/static polymorphism when they reduce duplicated code or remove material runtime cost cleanly; avoid template/metaprogramming complexity whose engineering cost exceeds its product benefit. Dynamic polymorphism remains valid when runtime substitution is the actual product model.
- Follow the project's accepted error/API contract (exceptions, expected/status/result types, error codes, assertions) rather than imposing one universal C++ error style; preserve exception safety and resource ownership across failure paths.
- Treat compiler/toolchain/build configuration, ABI, headers/templates, compile definitions, standard library/runtime, and target ISA as part of the affected surface when they can change behavior or performance.
- Treat undefined behavior, lifetime/bounds/initialization defects, invalid alias/alignment promises, signed-overflow dependence, and data races as correctness defects before optimization.
- Prefer tuned numerical libraries and compiler auto-vectorization before explicit intrinsics when they satisfy the contract; use architecture dispatch or target-specific builds only when portability/architecture authority justifies them.
- Prefer native threads/task runtimes or OpenMP-like shared-memory execution according to workload shape; use processes primarily for isolation/process architecture; use MPI-class execution when distributed-memory/multi-node architecture is required. Compose these with BLAS/FFT thread pools explicitly.
- Use compiler-native semantic/static evidence, sanitizer-class runtime checks, debugger-class tools, sampling/hardware-counter profilers, vectorization reports, property/fuzz tools, and existing Serena/Semgrep/CodeQL capabilities according to the claim. Exact tool identity remains delegated.

### Mixed Python/C++ boundary envelope

When both profiles apply:

- keep one clear owner for each object/buffer/resource and define lifetime across the boundary;
- prefer compatible buffer/array views and zero-copy transfer only when lifetime/stride/alignment contracts remain explicit and safe;
- batch calls when language-boundary dispatch dominates;
- account for exception/error translation, GIL acquisition/release, callback direction, thread ownership, and interpreter shutdown where material;
- benchmark end-to-end boundary cost before rewriting large components merely to move language boundaries;
- test the packaged/imported extension or real consumer path, not only direct kernel invocation;
- treat generated binding code as derived unless the project governs it as source.

## Implementation obligations and delegated solution space

### O1 — Perform a protocol-wide language-specificity census before editing

**Concern / rationale:** The current draft focuses mainly on performance, but Python-specific normative wording also exists in tool routing and security examples/rules. A partial extraction would leave inconsistent doctrine ownership.

**Required end state / constraint:** Inspect all canonical shared references and role/README routing surfaces for language-specific normative statements. Classify each occurrence as:

1. genuinely shared and generalizable;
2. a language-specific realization that belongs in a profile;
3. an intentionally language-specific tool/reference (for example Hypothesis);
4. a harmless example whose generic rule is already clear.

Generalize or route categories 1-2. Do not mechanically purge language names from examples.

**Expected surfaces:** at minimum `performance-and-parallelism.md`, `tool-assisted-engineering.md`, both role entrypoints, `source/README.md`, root `README.md`, `PORTABILITY.md`, `security-and-trust-boundaries.md`, `testing-and-validation.md`, `concurrency-and-orchestration.md`, `release-and-distribution.md`, and qualification scenarios.

**Acceptance evidence:** no remaining unqualified Python/C++ implementation requirement in a generic owner unless the owner itself is intentionally language/tool specific.

### O2 — Implement the thin language-profile router and precedence rule

**Required end state / constraint:** Introduce a compact canonical route stating:

```text
shared domain rule -> active language profile(s) -> implementation-local choice
```

For material executable work, identify every implementation/runtime language materially affected and read the corresponding profile only when language semantics can change the engineering decision. Documentation-only or purely generic architecture questions need not load profiles.

The router must explicitly handle Python-only, C++-only, Python calling C++, C++ embedding Python, generated bindings, and accelerator translation/runtime surfaces. File suffix alone is insufficient.

**Anti-shortcut:** Do not duplicate this routing logic independently in Design and Implementation entrypoints beyond short links to the canonical router.

### O3 — Refactor generic performance doctrine around shared concepts

**Concern / rationale:** Tuned numerical kernels, vectorization, shared/process/distributed parallelism, profiling, and accelerator gating are not C++ doctrines. Python frequently reaches the same optimized backends through different interfaces.

**Required end state / constraint:** Keep these concepts in `performance-and-parallelism.md`:

- work/asymptotic/data-layout/data-movement optimization order;
- efficiency-by-construction versus evidence-required complexity escalation;
- established optimized kernels/libraries before bespoke low-level machinery when they satisfy product constraints;
- vectorization/compiled execution as a capability, not a Python- or C++-specific syntax rule;
- representative profiling before non-obvious optimization;
- shared-memory, process-isolation, distributed-memory, and nested-parallel execution classes;
- benchmark comparability and longitudinal regression;
- GPU/accelerator architecture gate.

Language profiles map these to concrete realizations.

### O4 — Build a full Python engineering profile, not only a performance appendix

**Required end state / constraint:** The Python profile must cover language-native abstraction/API/resource style, interpreter/object-model costs, numerical execution, concurrency, testing/tooling, packaging, and mixed-boundary behavior as defined in the engineering envelope.

It must preserve all valid existing Python rules while explicitly avoiding two failure modes:

- **C++-in-Python:** excessive manual lifecycle/state machinery, low-level loops, thread assumptions, or native rewrites when high-level Python/library code is simpler and sufficient;
- **Python-performance denial:** retaining Python-level work on a dominant numerical path merely because the code is concise when an established compiled/vectorized realization is materially better and no more complex overall.

### O5 — Build a full C++ engineering profile, not only a performance/tool appendix

**Required end state / constraint:** The C++ profile must cover idiomatic ownership/lifetime/value design, compile-time/runtime abstraction choice, error contracts, build/ABI, memory/UB/race safety, numerical kernels, vectorization/SIMD, concurrency, tooling, packaging, and mixed-boundary behavior.

It must explicitly avoid:

- **Python-in-C++:** pervasive heap/dynamic dictionaries/late binding/wrapper layers or process-based parallelism copied from Python where static/value/native C++ constructs are cleaner;
- **C++ cleverness for its own sake:** template metaprogramming, bespoke allocators, intrusive ownership, custom SIMD, or abstraction scaffolding without a material correctness/performance/complexity benefit.

### O6 — Preserve generic optimized-kernel doctrine and specialize the library maps

**Shared rule:** Prefer an established validated optimized primitive when the algorithm maps cleanly and the dependency satisfies precision, portability, licensing, deployment, and ownership requirements.

**Python map:** NumPy/SciPy and established framework kernels, including tuned BLAS/LAPACK/FFT/sparse backends underneath them where relevant. Avoid assuming a Python API is fast merely because it is vector-looking; materialization and Python-object paths still require profiling.

**C++ map:** BLAS/LAPACK-family interfaces, FFTW-class FFTs, sparse/eigensolver/domain libraries, and vendor-tuned equivalents such as OpenBLAS/BLIS/oneMKL/AOCL/Accelerate or project-approved alternatives. Distinguish the mathematical/interface contract from the selected performance backend.

**Acceptance evidence:** the same dense-linear-algebra or FFT product problem routes to the shared optimized-kernel principle, then to different language-specific realizations without duplicating the principle.

### O7 — Preserve generic parallelism classes and specialize runtime selection

**Shared owner:** concurrency/orchestration + performance own resource topology, deterministic aggregation, nested parallelism, failure/cancellation, oversubscription, process isolation, and distributed-memory semantics.

**Python specialization:** GIL-aware thread/process selection; native-library thread pools; serialization/shared-memory costs; MPI through project-appropriate Python interfaces when distributed execution is Frozen.

**C++ specialization:** native threads/task pools for irregular shared-memory work; OpenMP-like execution for regular loop/data parallelism where appropriate; processes for isolation/process architecture; MPI-class execution for distributed/multi-node architecture; hybrid MPI + threads/OpenMP + BLAS/FFT composition.

**Anti-shortcut:** Do not make MPI or GPU a C++-only concept; both are architecture capabilities usable from Python or C++ through different interfaces.

### O8 — Preserve generic accelerator gating and specialize accelerator realizations

**Shared rule:** No accelerator obligations exist unless Tier-1/Frozen architecture enables accelerator support. When enabled, acceptance requires end-to-end benefit, numerical/reference equivalence, transfer/synchronization cost, memory bounds, backend/device identity, and target-hardware evidence.

**Python examples:** CuPy/JAX/PyTorch/Numba or project-equivalent accelerator execution when already compatible with the architecture.

**C++ examples:** CUDA, HIP, SYCL, OpenCL, Kokkos/RAJA-like portability layers, or project-equivalent execution according to the supported hardware/portability contract.

Prefer optimized accelerator libraries before custom kernels when operations map cleanly. Exact frameworks remain delegated.

### O9 — Generalize tool-capability routing and then map language-specific tools

**Concern / rationale:** The current deterministic route `broad Python input/state invariant -> Hypothesis` encodes a concrete Python tool where the parent engineering question is generic.

**Required end state / constraint:** `tool-assisted-engineering.md` and role routing must express generic relation classes first, then route to concrete methods:

- literal/path/text relation -> ordinary repository search/read;
- symbol owner/definition/reference/caller relation -> Serena or another supported semantic capability according to existing policy;
- AST/syntax/structural relation -> Semgrep where supported;
- broad/combinatorial input/state invariant -> language-appropriate property/generative method; Python -> Hypothesis when available; C++ -> project property/generative method or bounded deterministic generation;
- interprocedural flow/taint/source-to-sink -> CodeQL where supported;
- runtime state/crash -> language-appropriate debugger when it materially reduces uncertainty;
- memory/lifetime/UB/resource -> language-appropriate runtime/static instrumentation;
- race/synchronization -> language-appropriate race/concurrency evidence;
- performance bottleneck/vectorization -> language-appropriate profiler/compiler/hardware evidence.

Existing Serena/Semgrep/CodeQL/Hypothesis references remain canonical for their own tool methods. Do not create a second Serena/clangd navigation architecture.

**Python mapping:** existing Serena/Semgrep/CodeQL/Hypothesis plus Python debugger/profiler/memory tools as appropriate; exact tool names beyond existing governed methods remain delegated.

**C++ mapping:** existing Serena/Semgrep/CodeQL where supported; compiler diagnostics and clang-tidy-class AST checks; ASan/UBSan-class checks for relevant memory/UB risk; TSan-class checks for relevant shared-memory race risk; MSan/leak analysis when material and economically supportable; GDB/LLDB-class debugger for runtime state; sampling profilers/vectorization reports/hardware counters for performance; libFuzzer/AFL++-class fuzzing where the input surface warrants it. These are capability examples, not a fixed pipeline.

### O10 — Add the C++ compiler/vectorization/SIMD realization without moving generic doctrine

The C++ profile should use this evidence-directed realization order after the shared performance owner has selected vectorization/compiled optimization as relevant:

1. production-like optimized compiler baseline;
2. compiler optimization/vectorization diagnostics plus representative profiler evidence;
3. data/loop changes that allow safe auto-vectorization;
4. established portable SIMD/library abstraction or runtime multiversioning when portability matters;
5. explicit SSE/AVX/AVX2/AVX-512 or NEON/SVE-class intrinsics only for a still-dominant kernel with justified complexity;
6. LTO/PGO/target tuning after representative evidence if they become durable build policy.

A portable product must not silently become AVX-512-only because the development machine supports it. An architecture-specific build may use AVX-512 when the target ISA is explicitly product/Frozen authority.

No alias/alignment/restrict-like promise may be introduced solely to induce vectorization without a proved lifetime/layout contract.

### O11 — Make language-native abstraction quality an explicit review dimension

**Concern / rationale:** A protocol can preserve functionality and performance while still generating structurally poor code by translating idioms between languages.

**Required end state / constraint:** Design, Implementation final reconciliation, and independent review must ask for materially affected executable work:

- Is the realization idiomatic for the active language/runtime and compatible with the project's existing style/architecture?
- Does it use the language's simpler native ownership/resource/data/abstraction mechanisms instead of reproducing another language's compensating machinery?
- Does an abstraction reduce total complexity or duplicate it?
- Is a performance-critical abstraction actually zero/low-cost enough for its role, or is the runtime cost accepted by Tier-1 requirements?
- Would a simpler language-native realization satisfy the same product/Frozen contract?

This is an engineering challenge, not a style-policing gate. Equivalent stylistic preferences with no material correctness/performance/maintenance benefit do not block acceptance.

### O12 — Generalize security wording where the current shared owner leaks Python APIs

**Concern / rationale:** `security-and-trust-boundaries.md` correctly owns generic trust doctrine but currently contains Python-specific normative wording such as `shell=False` and pickle-specific hard rules.

**Required end state / constraint:** Keep generic rules in the shared security owner:

- prefer direct argument-vector/process APIs over shell interpretation;
- do not execute untrusted deserialization/object-construction formats;
- bound parser/input/resource amplification;
- treat compiler/build/package hooks as privileged execution.

Language-specific examples may remain, but Python-specific API directives belong in the Python profile or must be clearly examples of the generic rule. C++ profile may add relevant parser/loader/system-call/build-hook consequences without duplicating trust doctrine.

### O13 — Preserve scientific doctrine as shared authority across both profiles

Do not move numerical invariants/tolerances/reference-oracle/approximation/provenance rules into a language profile. Profiles only map where language/runtime/compiler choices can perturb those semantics.

Python profile examples include dtype/backend changes, compiled library replacement, multiprocessing ordering, JIT, and accelerator substitutions.

C++ profile examples include floating-point contraction/reassociation, `fast-math`-class flags, vector reductions, OpenMP/MPI reduction order, vendor BLAS/FFT changes, mixed precision, and accelerator substitutions.

Do not widen tolerances merely to bless a faster realization.

### O14 — Reconcile release/build/package integration without duplicating the release doctrine

`release-and-distribution.md` remains language-agnostic: build what users receive and exercise the supported consumer path.

Python profile specializes interpreter/package/import/environment and native-extension packaging when present.

C++ profile specializes compiler/build configuration, shared/static libraries, exported interfaces, headers/templates, runtime dependencies, ABI compatibility only where the product promises it, and supported platform/toolchain combinations.

Mixed Python/C++ products must test the installed extension through the packaged Python import/call path plus any direct C++ consumer boundary that is independently supported.

### O15 — Reconcile documentation, portability, qualification, and package generation

Implementation must update every duplicated/exposed routing surface, including:

- `source/PROTOCOL_VERSION`;
- `source/README.md` and root `README.md`;
- both core role `SKILL.md` files;
- `PORTABILITY.md`;
- `source/shared/references/performance-and-parallelism.md`;
- `source/shared/references/concurrency-and-orchestration.md` where generic parallelism routing needs clarification;
- `source/shared/references/tool-assisted-engineering.md` and existing tool method pages as needed;
- `source/shared/references/security-and-trust-boundaries.md` for genericized language leakage;
- `source/shared/references/testing-and-validation.md` only where generic property/runtime/tool evidence semantics need clarification;
- `source/shared/references/scientific-software.md` only for minimal cross-links if required; do not duplicate its doctrine;
- `source/shared/references/release-and-distribution.md` only for generic compiled-artifact wording that belongs there;
- new thin language router + Python/C++ profile references;
- `source/shared/references/protocol-versioning-and-compatibility.md`;
- `source/build_skills.py`;
- `qualification/tool-routing/SCENARIOS.md`, portability/reference-routing qualification where affected, and repository tests such as `tests/test_protocol_portability.py`;
- generated `dist/` artifacts and indexes.

Bundle the minimum references required for deterministic routing. Do not put every language/tool reference into unrelated specialists solely for completeness.

## Implementation authority

### Frozen

- Protocol 5 governing hierarchy, two-role lifecycle, accepted-workplan semantics, active simplicity, convergence, snapshot completeness, proxy-proof acceptance, and development-economy doctrine remain unchanged.
- Shared canonical domain owners outrank and constrain language profiles.
- One thin language router plus differential Python/C++ engineering profiles; no parallel protocols.
- Language profiles cover general language-native engineering, not only performance.
- Shared performance owns common optimization concepts; profiles own language-specific realization.
- Shared concurrency owns execution classes; profiles own runtime-specific selection.
- Shared tool-assisted engineering owns relation/capability classes; profiles/tool references own language/tool-specific methods.
- Mixed Python/C++ surfaces activate both profiles and explicit boundary reasoning.
- GPU/accelerator obligations are activated only by Tier-1/Frozen architecture.
- Scientific semantics remain shared authority over all language/backend/compiler optimizations.
- Protocol target is 5.15.0 and is backward-compatible under existing version-binding rules.

### Delegated

- Exact names and internal structure of the thin router and two profile files, provided canonical ownership and progressive disclosure remain clear.
- Exact compiler, build system, sanitizer, debugger, profiler, property/fuzz framework, BLAS/LAPACK/FFT backend, thread/task runtime, MPI implementation, accelerator framework, SIMD abstraction, and package manager.
- Serena versus another equally reliable supported semantic backend in a concrete environment, subject to existing deterministic capability-routing policy; reuse existing Serena capability when it is available/suitable rather than building duplicate machinery.
- Exact C++ exception/result/error style when project/product authority has not already fixed it.
- Exact Python type/data-class/protocol mechanisms when project architecture has not already fixed them.
- Whether a downstream product uses serial execution, threads, OpenMP-like runtime, processes, MPI, or a hybrid unless that product's architecture freezes the choice.
- Exact architecture dispatch and CPU feature-selection mechanism.

### Reopen only on evidence

Reopen Design only if implementation evidence shows:

- shared doctrine cannot be kept canonical without materially duplicating it in language profiles;
- deterministic profile routing cannot be packaged without unacceptable always-loaded duplication or ambiguity;
- mixed-language boundaries require a materially different authority/lifecycle model rather than simultaneous profiles;
- a Frozen platform/portability requirement makes the shared optimization model infeasible;
- an explicitly accelerator-first architecture conflicts irreconcilably with the shared CPU/default route and requires a different high-level performance architecture.

Ordinary absence or weakness of a tool/backend is not redesign; use capability fallback. Ordinary project preference for a different idiom/tool is delegated unless it changes product/Frozen architecture.

## Affected surface and task-specific acceptance

The affected surface must be re-derived after implementation. Initial expected surfaces are those listed in O15 plus generated skill bundles.

Task-specific acceptance must demonstrate:

1. **Doctrine preservation:** no change weakens Tier-1 product truth, Frozen architecture semantics, active simplification, acceptance integrity, convergence, snapshot completeness, or development-economy guarantees.
2. **Shared/profile precedence:** a profile cannot override a shared scientific/security/testing/performance requirement.
3. **Shared-reference purity:** generic references express durable rules independently of Python/C++, with language names appearing only as examples, explicit routes, or intentionally language/tool-specific sections.
4. **Python-native design scenario:** a representative numerical/data task yields high-level Python orchestration plus appropriate compiled/vectorized primitives rather than a literal C++-style low-level translation.
5. **C++-native design scenario:** the analogous task yields clear value/lifetime/resource semantics and native compiled execution rather than Python-like dynamic/process machinery.
6. **Performance-versus-complexity scenario:** an obvious zero/low-complexity efficiency improvement is allowed without benchmark ceremony, while a complexity-increasing optimization requires representative evidence and total-system justification.
7. **Common optimized-kernel scenario:** the same BLAS/FFT-class requirement routes through one shared optimized-library principle and then to different Python/C++ realizations.
8. **Common parallelism scenario:** shared-memory, process isolation, and MPI/distributed execution are treated as generic architecture classes; Python and C++ choose different runtime mechanisms where justified.
9. **Nested parallelism scenario:** Python/C++ outer execution plus BLAS/FFT/OpenMP/MPI layers cannot each independently claim the full machine.
10. **Tool-routing scenario:** semantic, structural, property/generative, interprocedural, runtime-state, memory/UB, race, and performance questions route by capability and language rather than one fixed C++ stack.
11. **C++ safety scenario:** memory/lifetime/UB/race risk can route to sanitizer/compiler/runtime evidence without making those tools universal gates.
12. **C++ vectorization scenario:** missed vectorization is diagnosed before intrinsics; portable code does not become AVX-512-only without architecture authority.
13. **Python performance scenario:** Python elementwise hot loops are challenged when compiled primitives exist, while bounded orchestration loops remain valid.
14. **Security transfer scenario:** shared shell/deserialization/trust rules remain language-agnostic; Python/C++ profiles provide justified API-specific consequences without duplicating the trust model.
15. **Scientific-equivalence scenario:** `fast-math`, dtype/precision/backend changes, vector/parallel reductions, and accelerators cannot obtain a pass by relaxing tolerances without authority.
16. **Mixed-language scenario:** Python/C++ binding performance, copies, ownership, GIL/threading, exceptions, packaging, and real-boundary integration are evaluated together.
17. **GPU gating:** CPU-only architecture loads no GPU implementation/tooling obligations; explicitly GPU-enabled architecture activates target-device numerical/performance/resource evidence in either Python or C++.
18. **Documentation/routing parity:** root/source README, role entrypoints, PORTABILITY, qualification scenarios, and built skill bundles agree on the new routing model.
19. **Package integrity:** every routed reference exists in each role bundle that links to it; unrelated specialists do not acquire unnecessary profile payload.
20. **Repository-required final checks:** run the canonical Protocol 5.15 equivalent of:

```bash
python -m pip install -r source/requirements-validation.txt
python -m unittest discover -s tests -v
python source/build_skills.py --output /tmp/protocol-dist
python source/validate_packages.py --dist /tmp/protocol-dist
python source/check_dist.py --expected /tmp/protocol-dist --committed dist
git diff --check
```

Production qualification is unnecessary for the protocol repository itself. Downstream products require target-machine qualification when their Tier-1 claims depend on actual CPU ISA, NUMA topology, MPI/network topology, accelerator hardware, production-scale I/O, or production-scale performance.

## Implementation sequence and genuine redesign / simplification triggers

### Stage 1 — Protocol-wide language-specificity census

Audit canonical shared references and exposed routing/docs. Produce the minimal ownership map: shared rule, Python specialization, C++ specialization, or intentional tool-specific rule. Generalize shared language leakage before adding new language content.

Close with focused documentation/routing tests proving that existing Protocol 5.14 doctrine is still represented.

### Stage 2 — Install the three-layer routing architecture

Add the thin language router and compact Python/C++ engineering profiles. Update role routing and skill packaging. Establish the shared > profile > implementation-local precedence rule and mixed-profile composition.

Close routing/package tests before substantive profile expansion.

### Stage 3 — Refactor shared performance/concurrency/tool/security ownership

Move common concepts out of C++-specific wording: optimized kernels, vectorization capability, parallelism classes, profiling, GPU gating, generic property relation, shell/deserialization wording. Preserve current valid Python behavior through the profile.

### Stage 4 — Complete Python and C++ language-native engineering profiles

Add general idiomatic engineering, performance realization, runtime/build/package semantics, tooling maps, and mixed-boundary consequences. Add C++ compiler/sanitizer/debugger/SIMD detail only here or in justified tool-specific references; keep generic owners clean.

### Stage 5 — Qualification integration

Add counterfactual scenarios for language-native design, shared-versus-profile ownership, performance-versus-complexity escalation, tool routing, optimized kernels, parallelism, security transfer, mixed Python/C++, and GPU gating. Update root/source documentation and portability qualification.

### Stage 6 — Version/package/final acceptance

Bump to 5.15.0, reconcile version history, regenerate `dist/`, re-derive final affected surfaces, run complete repository checks, and inspect built bundles for routing completeness and unnecessary duplication.

### Active simplification triggers

Before adding another durable file/tool abstraction/route, simplify or re-derive if implementation shows:

- shared doctrine copied into both profiles;
- separate Python/C++ versions of performance, concurrency, security, or testing references;
- a language router that becomes a policy owner instead of a thin selector;
- a fixed C++ tool pipeline instead of relation-directed selection;
- separate Serena and clangd semantic-navigation architectures solving the same problem;
- one page per compiler/sanitizer/profiler with no distinct method;
- duplicated MPI/GPU doctrine across Python and C++ profiles;
- wrappers around BLAS/FFT/SIMD created only to satisfy protocol wording rather than reduce product complexity;
- language profiles prescribing style preferences without material engineering effect;
- qualification tests freezing exact prose/file/tool identity rather than semantic routing;
- accelerator machinery leaking into CPU-only tasks;
- cross-language rewrites being proposed before boundary/data-movement/algorithm simplification has been considered.

### Genuine redesign triggers

Return to Software Design only if evidence demonstrates that shared doctrine plus differential simultaneous profiles cannot represent the required product, or that the Frozen portability/accelerator architecture itself must change. Individual tool/backend availability, compiler choice, library choice, or idiomatic implementation preference is not redesign.

## Design verdict

**PASS — ready for implementation after this integration revision.**

The reviewed plan now preserves prior Protocol 5 doctrine as the sole shared authority, treats Python and C++ as language-native realizations rather than parallel protocols, moves common performance/parallelism/tool concepts back to shared owners, broadens profiles from performance appendices into complete engineering profiles, removes accidental tool/backend freezing, and makes performance-versus-complexity optimization explicit. This structure is intended to produce high-performance code with the minimum justified total code/system complexity in either language while remaining capable of clean mixed Python/C++ scientific software.
