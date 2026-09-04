---
kind: implementation-workplan
workplan_id: PROTOCOL-5.15-LANGUAGE-PROFILES-CPP-PERFORMANCE
protocol_version: 5.14.0
---

# Protocol 5.15 Language Profiles, C++ Tooling, and Performance Engineering Workplan

## Objective / problem invariants / non-goals

### Original problem

Protocol 5.14 has a strong language-agnostic product-engineering doctrine, but several operational rules were shaped by Python scientific-software practice. The protocol needs one language/runtime adaptation mechanism that preserves the shared lifecycle, authority, simplicity, testing, scientific-fidelity, and evidence rules while making Python and C++ implementation guidance genuinely appropriate to their different execution models.

The C++ side also needs a high-return development and performance methodology rather than only syntax-level language guidance. That methodology must cover semantic navigation, static/structural analysis, debugger use, memory/lifetime/race guarding, generative/fuzz testing, optimized numerical kernels, compiler/vectorization/SIMD optimization, shared-memory and distributed parallelism, and optional accelerator execution.

The product outcome is a single protocol that can develop Python, C++, and mixed Python/C++ scientific software efficiently and correctly, selecting tools and optimization mechanisms by the engineering claim rather than running a fixed tool pipeline.

### Product invariants

1. **One protocol, shared doctrine.** Language choice must not fork lifecycle, Tier-1/Tier-2 authority, workplan semantics, active simplicity, acceptance, scientific correctness, or development-economy doctrine.
2. **Language/runtime-specific execution semantics are explicit.** Rules whose meaning depends on interpreter, compiler, ABI, memory lifetime, process model, vector ISA, or build configuration route through a language/runtime profile.
3. **Mixed-language composition is first-class.** Python orchestration plus C++ numerical kernels may activate both profiles in one affected surface.
4. **Performance remains measurement-directed and scientifically constrained.** Algorithmic complexity, data representation, data movement, locality, representative profiling, and numerical equivalence outrank low-level optimization fashion.
5. **C++ correctness includes undefined-behavior, lifetime, bounds, initialization, aliasing, and race safety.** Optimizer-dependent success does not excuse invalid semantics.
6. **Compiler/build configuration is part of C++ performance identity.** Debug, sanitizer, coverage, and release/LTO/PGO builds are not interchangeable evidence.
7. **Numerical semantics outrank compiler speed flags.** Fast-math, reassociation, contraction, mixed precision, denormal behavior, and reduction-order changes require accepted scientific equivalence evidence.
8. **Optimized libraries are preferred over reinvention when they satisfy the contract.** Established BLAS/LAPACK/FFT/sparse/kernel libraries should normally precede hand-written low-level kernels.
9. **CPU performance support is ordinary protocol capability.** The protocol must natively reason about compiler optimization, vectorization/SIMD, threads, OpenMP-like shared-memory parallelism, process isolation, and MPI-class distributed execution where the target architecture requires it.
10. **GPU/accelerator execution is architecture-opt-in.** CUDA, HIP, SYCL, OpenCL, or other accelerator backends are activated only when the user/project explicitly includes accelerator support in Tier-1 requirements or Frozen architecture. Mere hardware availability does not create a requirement.
11. **No tool monoculture.** The protocol may recommend high-return defaults, but selection remains capability- and claim-directed with concrete fallbacks.

### Non-goals

- Do not create separate Python and C++ lifecycle roles or parallel protocols.
- Do not require every C++ project to implement threads, OpenMP, MPI, subprocess execution, GPU support, or multiple numerical backends. Protocol support is broader than any one product's required architecture.
- Do not prescribe one build system, compiler, debugger, test framework, profiler, BLAS vendor, FFT library, MPI implementation, or accelerator stack globally.
- Do not require hand-written intrinsics, AVX-512-only binaries, custom allocators, PGO, LTO, GPU kernels, or assembly without representative evidence that they address a material Tier-1 requirement.
- Do not weaken Python-specific guidance merely to obtain superficially language-neutral prose.
- Do not turn sanitizer/analyzer availability into ceremonial mandatory gates unrelated to the affected claim.

## Frozen high-level architecture and engineering envelope

### Frozen architecture

1. **Shared core + conditional language/runtime profiles.** Existing shared owners continue to govern workflow, architecture, testing, scientific correctness, performance methodology, storage, security, and orchestration. Add compact Python and C++ profile owners plus minimal profile routing.
2. **Profile activation follows the affected semantic/runtime/build surface.** File extension is evidence, not authority. Generated bindings, headers, CUDA/SYCL translation units, embedded interpreters, and mixed targets may activate multiple profiles.
3. **Generic performance remains canonical.** `performance-and-parallelism.md` owns language-neutral optimization order, benchmark discipline, resource budgets, scaling, data movement, and accelerator policy. Python-only and C++-specific execution rules belong in profiles.
4. **Tool routing remains per engineering question.** Semantic navigation, structural relations, interprocedural flow, lifetime/memory safety, races, runtime state, and performance each route to the highest-information available tool that directly models the claim.
5. **High-return C++ tooling is layered, not duplicated.** Reuse Serena, Semgrep, and CodeQL when their C++ support models the question; add compiler-native C++ tools where they provide materially stronger semantic, memory, debugger, or performance evidence.
6. **CPU optimization ladder is first-class.** The protocol explicitly supports tuned numerical kernels, compiler optimization, auto-vectorization/SIMD, shared-memory parallelism, and distributed MPI-class execution where the product architecture requires scaling beyond one process/node.
7. **GPU remains conditional.** Accelerator-specific tooling and implementation are routed only when accelerator support is Tier-1/Frozen. CPU-only work must not inherit CUDA/OpenCL/SYCL obligations.
8. **Protocol 5.15 is a backward-compatible minor strengthening.** Existing workplans remain version-bound.

### C++ engineering envelope

The C++ profile must cover, proportionately to the affected claim:

- optimized versus debug/instrumented build identity;
- compiler/toolchain/version/flags/target ISA/standard-library/runtime identity;
- `compile_commands.json` or equivalent compilation database where semantic tooling needs exact translation-unit configuration;
- RAII, ownership, lifetime, non-owning views, bounds, initialization, aliasing/alignment, exception-safety, and data-race concerns;
- layout/stride/contiguity, AoS/SoA, indirection, allocation/copy/move behavior, cache locality, false sharing, and NUMA effects;
- optimized numerical libraries such as BLAS/LAPACK-family kernels, FFTW-class FFTs, sparse/domain libraries, and vendor-tuned equivalents;
- compiler optimization, inlining, devirtualization, LTO/PGO where justified, and vectorization diagnostics;
- ISA-level optimization including SSE/AVX/AVX2/AVX-512 on x86 and NEON/SVE-class vectorization on Arm, preferably through libraries/autovectorization or safe dispatch before hand intrinsics;
- native C++ threads, task/thread-pool runtimes, OpenMP-like shared-memory execution, subprocess/process isolation, and MPI-class distributed execution;
- optional GPU backends such as CUDA, HIP, SYCL, OpenCL, or project-equivalent accelerator frameworks only when architecture-authorized;
- ABI/API/shared-library/header/template/ODR implications;
- Python/C++ FFI boundaries when present;
- debugger, sanitizer, profiler, hardware-counter, compiler-diagnostic, semantic-analysis, structural-analysis, and interprocedural-analysis evidence.

## Implementation obligations and delegated solution space

### O1 — Refactor generic versus language-specific performance doctrine

**Concern / rationale:** The current generic performance owner contains Python-only GIL, process, NumPy/SciPy, `numpy.vectorize`, and Python-worker guidance alongside universal optimization rules.

**Required end state / constraint:** Keep generic guidance runtime-neutral: remove redundant work; improve asymptotics; improve representation/layout; reduce movement/allocation; prefer optimized kernels; improve locality/vectorization; add concurrency only where it helps; add accelerators only when architecture-authorized and worthwhile. Preserve all Python behavior in the Python profile and add C++ semantics in the C++ profile.

**Acceptance evidence:** No Python-only execution rule remains phrased as universal; no C++ profile duplicates generic optimization doctrine.

### O2 — Add deterministic language/runtime profile routing

**Required end state / constraint:** Add a compact routing owner that distinguishes Python orchestration, Python numerical/native-library execution, C++ compiled targets, mixed Python/C++ boundaries, and accelerator translation/runtime surfaces. Multiple profiles may activate together.

**Acceptance evidence:** Qualification covers Python-only, C++-only, mixed Python/C++, and architecture-authorized accelerator examples.

### O3 — Preserve and consolidate Python-specific performance rules

Preserve interpreter-loop avoidance for large dense numerical work; NumPy/SciPy/framework-kernel preference; `numpy.vectorize`/`frompyfunc` non-acceleration; GIL-aware thread/process decisions; serialization/process-transfer cost; dtype/stride/materialization concerns; and escalation to JIT/native/custom kernels only after profiling justifies the complexity.

### O4 — Establish the high-return C++ tool-routing stack

**Concern / rationale:** C++ needs different semantic and runtime evidence than Python. The protocol should privilege tools that substantially reduce reasoning ambiguity or catch defect classes ordinary tests miss.

**Required end state / constraint:** Add C++ claim-directed routing with the following priority model.

#### A. Semantic code understanding — highest default return

1. **Serena remains the primary semantic repository-navigation tool** when available. Its C/C++ mode is backed by `clangd` by default and may use `ccls`; prefer a correct compilation database such as `compile_commands.json` so macros, includes, standards, compile definitions, and generated headers match the actual target.
2. **clangd/compiler AST information is the semantic foundation** when Serena is unavailable or a direct compiler-language-server answer is more appropriate.
3. **Semgrep remains the structural-pattern tool** for syntax/AST-pattern questions where its active engine sufficiently supports the project; do not use it for claims requiring full C++ type/lifetime/build semantics that clang-based analysis models better.
4. **CodeQL remains the interprocedural/data-flow tool** for supported C/C++ builds when the claim depends on cross-function source-to-sink or program relations.

Do not replace Serena with a parallel C++ navigation framework merely because C++ has compiler AST tooling; Serena should reuse that tooling through clangd where practical.

#### B. Local C++ static quality and compiler semantics — very high return

Use compiler diagnostics and clang-tidy-like AST-backed checks for local semantic/code-quality classes such as suspicious conversions, lifetime/ownership patterns, misuse of language/library APIs, portability problems, modernize/performance checks, and project-governed style/bug patterns when these checks directly model the risk. Existing GCC/MSVC/vendor equivalents remain valid.

Compiler warnings are evidence, not proof of correctness. Do not globally enable every warning/check if the result is untriageable noise; govern a high-signal project set and prevent newly introduced relevant warnings.

#### C. Memory/lifetime/UB guarding — highest runtime defect return

- **ASan-class instrumentation** for out-of-bounds, use-after-free, use-after-scope/return, double/invalid free, and related memory defects.
- **UBSan-class instrumentation** for relevant undefined-behavior classes.
- **MSan-class instrumentation** when uninitialized-memory behavior is material and the platform/dependency environment can support it economically.
- **Leak analysis** through sanitizer support or a compatible memory checker when leaks are part of the product/resource claim.
- **Valgrind-like dynamic analysis** is a fallback/complement when sanitizer instrumentation is unavailable or when its specific memory/profiling capability provides additional value; it is not the default merely because it is traditional.

Sanitizer builds are correctness builds, not production-performance evidence.

#### D. Concurrency guarding

Use **TSan-class race detection** when changed shared-memory ownership/synchronization creates a material race risk and the platform supports it. Combine with deterministic concurrency tests, stress repetition, and state-transition reasoning from the shared concurrency owner. Race-tool silence does not prove all schedules safe.

#### E. Debugger and crash forensics

Use **GDB/LLDB-class debuggers** for runtime state questions that require stack/frame inspection, breakpoints/watchpoints, core dumps, signals, thread state, or optimized-crash diagnosis. Prefer debugger evidence over speculative logging when the defect is reproducible locally and debugger access directly exposes the failing state.

Do not make interactive debugging a routine gate when tests/static evidence already establish the claim more cheaply.

#### F. Generative/fuzz testing

Keep Hypothesis as the Python-specific property/stateful tool. For native C++, route broad input/state invariants to an available property/generative framework or deterministic generator; route parser/decoder/binary-format/memory-boundary surfaces to libFuzzer/AFL++-class fuzzing when appropriate. Fuzzing and semantic property testing are complementary, not interchangeable.

**Acceptance evidence:** Qualification distinguishes semantic navigation, structural pattern, local compiler-semantic analysis, interprocedural flow, memory/UB, races, debugger state, and fuzz/property questions instead of routing all C++ work through one tool sequence.

### O5 — Make optimized numerical kernels the default implementation tier where applicable

**Concern / rationale:** Scientific C++ should normally exploit mature tuned kernels before reproducing them manually.

**Required end state / constraint:** For dense linear algebra, prefer BLAS/LAPACK-class APIs or an established C++ abstraction backed by tuned BLAS/LAPACK when the operation maps cleanly. For FFTs, prefer FFTW-class or platform/vendor-equivalent tuned implementations. Apply the same principle to sparse solvers, eigensolvers, convolutions, and domain kernels: established validated libraries outrank custom kernels when they satisfy precision, layout, licensing, portability, and deployment requirements.

The protocol must distinguish **reference interfaces** from **performance backends**. Reference BLAS/LAPACK semantics do not imply the untuned reference implementation should be shipped for performance-sensitive work; choose an appropriate tuned backend such as OpenBLAS, BLIS, oneMKL, Accelerate, AOCL, vendor libraries, or project-equivalent according to supported platforms.

Account for library threading. A threaded BLAS/FFT backend nested under OpenMP, native thread pools, MPI ranks, or Python workers can oversubscribe the machine.

**Acceptance evidence:** A numerical-kernel optimization scenario first evaluates mapping to a tuned library before hand-writing SIMD or parallel loops, while allowing custom kernels when the algorithm cannot be expressed efficiently by available primitives.

### O6 — Add a C++ compiler/vectorization/SIMD optimization ladder

**Required end state / constraint:** The C++ profile must apply this order unless representative evidence justifies deviation:

1. correct algorithm and data representation;
2. remove unnecessary allocations, copies, indirection, conversions, virtual dispatch, and synchronization on hot paths;
3. use tuned library kernels where applicable;
4. establish a production-like optimized compiler baseline;
5. inspect compiler optimization/vectorization diagnostics and profiler/hardware evidence;
6. improve loop/data form so the compiler can vectorize safely;
7. use portable C++/library SIMD abstractions or function multiversioning/runtime dispatch when portability matters;
8. use explicit ISA intrinsics only when a dominant kernel remains materially limited and the complexity is justified;
9. consider LTO/PGO and target-specific tuning after representative profiling demonstrates value.

Do not globally compile a portable product for AVX-512 merely because the development machine supports it. When multiple deployed CPUs matter, prefer conservative baseline binaries plus safe runtime dispatch/multiversioning or a library that performs its own dispatch. Hardware-specific builds are valid when target ISA is explicitly part of the product/Frozen architecture.

Compiler flags that change floating-point semantics are scientific/algorithm decisions, not ordinary optimization knobs.

**Acceptance evidence:** Qualification includes a missed-vectorization scenario, an AVX-512 portability scenario, and an architecture-specific build scenario where AVX-512 is legitimately Frozen.

### O7 — Define first-class CPU parallelization selection

**Concern / rationale:** C++ has inexpensive shared-memory concurrency but also multiple parallel runtimes whose composition can degrade correctness and performance.

**Required end state / constraint:** The protocol must understand these mechanisms natively while selecting only those justified by the product architecture and workload.

#### Native threads / task runtimes

Use `std::thread`/`std::jthread`/task-pool or project-equivalent execution for irregular task parallelism, long-lived pools, custom ownership/control, asynchronous pipelines, or workloads not naturally expressed as loop parallelism. Prefer bounded pools over thread-per-small-task creation.

#### OpenMP-like shared-memory parallelism

Use OpenMP or an equivalent compiler/runtime model for regular loop/data parallelism and scientific kernels when it materially reduces implementation complexity and performs well on supported toolchains. Treat scheduling, reductions, nested regions, affinity, and library threading as explicit performance/correctness concerns.

#### Processes/subprocesses

Do not use subprocesses as the default C++ CPU-speed mechanism. Use separate processes when isolation, failure containment, independent address spaces, external executables, privilege/runtime boundaries, or project architecture require them. Account for IPC, serialization/copying, startup, NUMA, and duplicated memory.

#### MPI-class distributed memory

Treat MPI as first-class protocol capability for distributed-memory or multi-node HPC. Activate product-level MPI implementation when Tier-1/Frozen architecture includes multi-process or multi-node scaling, or representative single-node limits require Design to select distributed execution. Explicitly reason about domain/data decomposition, communication volume, collectives, synchronization, rank-local threading, I/O, failure assumptions, and MPI + OpenMP/thread hybrid oversubscription.

MPI is not required for ordinary single-node software merely because it is available.

#### Nested parallelism

Model the whole stack: MPI ranks × outer pools/OpenMP threads × BLAS/FFT threads × accelerator jobs. Defaults must not independently claim all cores at each layer.

**Acceptance evidence:** Qualification differentiates irregular native-thread work, regular OpenMP work, process-isolation work, MPI distributed work, and nested BLAS/OpenMP/MPI cases.

### O8 — Keep GPU/accelerator support explicitly architecture-gated

**Required end state / constraint:** Accelerator implementation/tooling is activated only if the user/project explicitly specifies GPU/accelerator support in Tier-1 requirements or Frozen architecture. If absent, the protocol must not require GPU probing, CUDA builds, device tests, or accelerator dependencies.

When activated, select the backend according to the supported hardware/portability contract:

- **CUDA** for NVIDIA-specific/high-control execution;
- **HIP** for AMD-oriented or CUDA-like portability where supported;
- **SYCL** for C++ heterogeneous portability where the product accepts the ecosystem/toolchain;
- **OpenCL** where its device/runtime portability or existing architecture makes it appropriate;
- another established project-specific accelerator framework when already authoritative.

Prefer optimized accelerator libraries (cuBLAS/cuSOLVER/cuFFT, rocBLAS/rocSOLVER/rocFFT, oneMKL/SYCL libraries, etc.) before custom kernels when operations map cleanly.

Accelerator acceptance must include CPU/reference numerical equivalence, host-device transfer/synchronization cost, kernel execution, memory capacity, device/runtime identity, and end-to-end benefit. GPU qualification cannot be inferred from CPU tests.

GPU profiling/debugging tools such as Nsight-class or vendor-equivalent tools become relevant only inside this architecture-gated path.

### O9 — Add performance profiling and hardware-counter routing

**Required end state / constraint:** For C++ performance questions, use representative profiling before optimization. Route according to the bottleneck:

- wall-time/function/call-stack profiling: `perf`/Instruments/VTune/vendor-equivalent sampling tools;
- allocation/heap behavior: allocator profilers, heaptrack/massif-class tools, or project-equivalent evidence;
- CPU microarchitecture: hardware counters for cycles, instructions, cache/TLB misses, branch behavior, vector utilization, memory bandwidth, and stalls where they materially explain the bottleneck;
- compiler vectorization/optimization reports when transformation decisions are the question;
- MPI/OpenMP runtime profiling only when distributed/shared-runtime overhead is material;
- accelerator profilers only when accelerator support is architecture-authorized.

Do not demand hardware counters for a bottleneck already established more cheaply. Sampling profilers should normally precede instrumentation-heavy microarchitectural investigation.

### O10 — Extend compiled-build and benchmark comparability

For C++ performance evidence record only material dimensions needed for fair comparison, including compiler/toolchain version, optimization/build type, target ISA, LTO/PGO state when used, sanitizer/coverage instrumentation state, relevant standard/runtime libraries, numerical backend, thread/runtime settings, and hardware.

Reject debug-versus-release, sanitizer-versus-native, or materially different backend comparisons as speedup evidence unless the comparison itself is the stated question.

### O11 — Protect scientific semantics across libraries, SIMD, parallel reductions, and compiler optimization

The existing scientific owner remains authoritative. C++ profile guidance must explicitly route numerical backend changes, vectorized reductions, OpenMP/MPI reductions, FMA/reassociation, mixed precision, and accelerator substitutions through accepted exact/tolerance/invariant checks on final scientific observables.

Do not widen tolerances solely because a faster backend changes results. Retain a trusted reference path where practical for bounded equivalence testing.

### O12 — Reconcile compiled packaging/ABI and mixed Python/C++ boundaries

Build and test what users receive. Where governed, validate shared-library dependencies, exported interfaces, ABI compatibility, header/template consumers, and supported compiler/platform combinations. Mixed Python extension artifacts must be tested through packaged import/call boundaries and account for ownership, zero-copy buffers, strides, exceptions, GIL behavior, and batching.

### O13 — Generalize property/generative routing while preserving Hypothesis

Introduce a language-neutral parent rule for broad/combinatorial invariants. Python routes to Hypothesis where appropriate. C++ routes to project-available property/generative/fuzz mechanisms according to the claim. Do not invent a mandatory C++ property-testing dependency solely for protocol symmetry.

### O14 — Package and qualify the new methodology coherently

Implementation must:

- bump target protocol to `5.15.0`;
- update README/versioning summaries;
- add the minimum language/tool profile references needed by core roles;
- update `source/build_skills.py` so routed references ship with installed bundles;
- update routing/qualification tests for Python, C++, mixed-language, sanitizer/debugger/profiler, numerical-kernel, SIMD, CPU-parallel, MPI, and architecture-gated GPU scenarios;
- regenerate `dist/` and preserve source/generated parity.

Do not create one reference page per tool unless the method is substantial enough to justify independent routing. Prefer one compact C++ tooling/performance profile with dedicated pages only for tools already generic across languages (Serena, Semgrep, CodeQL, Hypothesis).

## High-return C++ tool priority

The protocol should communicate this default priority, while still routing by claim:

1. **Serena + clangd + accurate compilation database** — semantic ownership/callers/references and large-repository navigation.
2. **Compiler diagnostics + clang-tidy-class AST analysis** — cheap continuous C++ semantic/quality signal.
3. **ASan + UBSan** on affected executable surfaces — exceptionally high return for C++ memory/UB defects.
4. **TSan** when shared-memory concurrency changes materially affect race risk.
5. **GDB/LLDB** when runtime state/crash diagnosis requires an actual debugger.
6. **Sampling profiler + compiler vectorization reports** for performance work before source-level micro-optimization.
7. **Semgrep** for bounded structural families and forbidden/legacy constructs where its C++ parser/engine is adequate.
8. **CodeQL** for supported interprocedural/data-flow relations and security/quality questions whose value justifies extraction/build cost.
9. **libFuzzer/AFL++-class fuzzing or project property frameworks** for parsers, binary formats, state/input families, and robust boundary exploration.
10. **Valgrind/advanced microarchitectural/vendor profilers** as targeted complements/fallbacks, not automatic baseline steps.

The ordering is not a mandatory pipeline. A TSan question may jump directly to TSan; a structural census may route directly to Semgrep; a performance task may go directly from representative benchmark to profiler.

## Implementation authority

### Frozen

- Protocol 5 hierarchy and two-role lifecycle remain unchanged.
- One shared protocol with conditional Python/C++ profiles; no parallel lifecycle trees.
- Profile activation follows affected runtime/build semantics and may be simultaneous.
- Serena is reused for C++ semantic navigation through supported language-server capability rather than replaced by redundant machinery.
- Compiler-native C++ tooling is first-class where it materially improves semantic correctness, memory safety, debugging, race detection, or performance diagnosis.
- Optimized numerical libraries precede hand-written kernels when they satisfy the scientific/product contract.
- CPU vectorization and shared-memory parallelism are ordinary supported performance mechanisms; MPI is first-class for architecture-relevant distributed execution.
- GPU/accelerator support is activated only when explicitly Tier-1/Frozen by the user/project.
- Scientific semantics remain authoritative over fast-math, backend, SIMD, and parallel-reduction changes.
- Protocol target is 5.15.0 and remains backward-compatible with prior Protocol 5 workplans by explicit version binding.

### Delegated

- Exact compiler, build system, debugger, sanitizer implementation, profiler, property framework, BLAS/LAPACK backend, FFT library, thread pool, OpenMP runtime, MPI implementation, and accelerator backend.
- Whether compiler-native methodology lives entirely in the C++ profile or a small reusable tool reference is extracted after implementation shows repeated cross-profile use.
- Exact SIMD abstraction and runtime dispatch mechanism.
- Whether a downstream product uses threads, OpenMP, MPI, processes, or a hybrid, unless that choice is explicitly Frozen by its own architecture.
- Exact tuned numerical library where multiple conforming backends satisfy the supported platform and licensing envelope.

### Reopen only on evidence

Reopen Design only if implementation evidence shows:

- installed skill packaging cannot support deterministic conditional profile/tool routing without substantial always-loaded duplication;
- Serena/clangd cannot provide the required C++ semantic capability for the intended installed environments and a different primary semantic architecture is materially necessary;
- the CPU-first generic performance hierarchy conflicts with an explicitly accelerator-first product architecture;
- mixed-language projects cannot be represented cleanly through simultaneous profiles;
- a Frozen portability target makes the proposed CPU vectorization/backend strategy infeasible without changing architecture.

Do not reopen for ordinary absence of an optional analyzer, sanitizer, profiler, numerical backend, MPI implementation, or GPU runtime; use the concrete fallback policy.

## Affected surface and task-specific acceptance

Expected canonical source includes:

- `source/PROTOCOL_VERSION`;
- `source/README.md`;
- both core role `SKILL.md` files;
- `source/shared/references/performance-and-parallelism.md`;
- Python and C++ language/runtime profile reference(s);
- `testing-and-validation.md` where sanitizer/generative/build-mode semantics belong;
- `tool-assisted-engineering.md` and relevant existing tool pages;
- `concurrency-and-orchestration.md` for CPU parallel-runtime cross-routing without duplication;
- `scientific-software.md` only for minimal cross-routing if needed; its numerical doctrine remains canonical;
- `release-and-distribution.md` for compiled artifacts;
- `protocol-versioning-and-compatibility.md`;
- `source/build_skills.py`;
- routing/qualification tests and scenarios;
- generated `dist/`.

Task-specific acceptance must demonstrate at least:

1. Python behavior remains reachable and unchanged in substance.
2. C++ semantic navigation routes to Serena/clangd and uses compilation-database semantics where needed.
3. Structural C++ family analysis can route to Semgrep without pretending it has full compiler semantics.
4. Interprocedural C++ flow can route to CodeQL when supported.
5. Memory/lifetime and UB scenarios distinguish ASan/UBSan from ordinary unit tests.
6. Race-risk scenarios distinguish TSan from generic profiling.
7. Crash-state scenarios route to debugger use when debugger evidence is the highest-value model.
8. A dense linear-algebra optimization considers tuned BLAS/LAPACK before custom SIMD.
9. An FFT optimization considers FFTW/vendor-equivalent optimized execution before custom FFT code.
10. A missed-vectorization scenario uses compiler/vectorization evidence before hand intrinsics.
11. A portable x86 product does not silently become AVX-512-only; an explicitly AVX-512 Frozen target may use it.
12. Native-thread, OpenMP, process-isolation, MPI, and nested-parallelism scenarios route differently according to workload/architecture.
13. A CPU-only architecture does not activate CUDA/HIP/SYCL/OpenCL obligations.
14. An explicitly GPU-enabled architecture does activate accelerator numerical-equivalence, transfer, memory, profiling, and target-device evidence.
15. Debug/sanitizer versus release/native benchmark mismatch is rejected as performance evidence.
16. Fast-math/reassociation is rejected without scientific equivalence authority.
17. Generated installed bundles contain every reference they route to.
18. Canonical repository acceptance commands succeed:

```bash
python -m pip install -r source/requirements-validation.txt
python -m unittest discover -s tests -v
python source/build_skills.py --output /tmp/protocol-dist
python source/validate_packages.py --dist /tmp/protocol-dist
python source/check_dist.py --expected /tmp/protocol-dist --committed dist
git diff --check
```

Production qualification is unnecessary for the protocol repository itself. Downstream products require target-machine qualification when their Tier-1 claims depend on actual SIMD ISA, MPI topology, NUMA behavior, accelerator hardware, or production-scale performance.

## Implementation sequence and genuine redesign / simplification triggers

### Stage 1 — Semantic census and ownership boundary

Classify current performance/testing/tool/concurrency/release guidance as shared, Python-specific, C++-missing, or project-specific. Establish the smallest language/profile ownership before adding new documents.

### Stage 2 — Profile routing and Python extraction

Create deterministic profile routing and move/generalize existing Python-only performance rules without semantic regression.

### Stage 3 — C++ semantic/safety/debugger tooling

Add Serena/clangd compilation-database guidance, compiler diagnostics/clang-tidy-class analysis, ASan/UBSan/TSan/MSan-class routing, debugger methodology, C++ generative/fuzzing routing, and precise Semgrep/CodeQL boundaries. Close focused qualification before performance breadth is added.

### Stage 4 — Numerical kernels, compiler optimization, SIMD, and CPU parallelism

Add tuned-library priority, vectorization/ISA portability policy, optimized-build identity, native-thread/OpenMP/process/MPI selection, and nested-parallelism rules. Preserve scientific and generic performance ownership rather than duplicating them.

### Stage 5 — Architecture-gated accelerators

Add a compact accelerator route that remains dormant unless Tier-1/Frozen architecture explicitly enables GPU/accelerator support. Cover CUDA/HIP/SYCL/OpenCL classes without forcing one backend.

### Stage 6 — Packaging/version/final acceptance

Bump to 5.15.0, update summaries, regenerate bundles, re-derive the final affected surface, run complete protocol regression/package checks, and inspect installed bundle routing.

### Active simplification triggers

Before adding another durable tool page, registry, or profile branch, simplify/re-derive if implementation shows:

- duplicated generic doctrine across Python/C++/GPU pages;
- a fixed C++ tool pipeline instead of claim-directed routing;
- separate Serena and clangd navigation architectures doing the same job;
- tool references that merely list commands without a distinct reasoning method;
- duplicated CPU-parallel doctrine across thread/OpenMP/MPI sections;
- one abstraction layer wrapping BLAS/FFT/SIMD only to satisfy protocol wording without reducing product complexity;
- qualification tests freezing exact file/tool names rather than semantic routing;
- accelerator machinery leaking into CPU-only tasks.

### Genuine redesign triggers

Return to Design only if evidence demonstrates that shared doctrine plus conditional profiles cannot represent the required mixed-language/tool behavior, or that the Frozen CPU/GPU portability model itself must change. Ordinary tool/backend availability is not redesign.

## Design verdict

**PASS — ready for implementation.**

The revised plan closes the major missing C++ development-method gap without creating a second protocol. It reuses Serena, Semgrep, and CodeQL where they have genuine C++ value, adds the compiler-native semantic/sanitizer/debugger/profiler stack with higher return for C++ defect classes, makes tuned numerical libraries and compiler/vectorization evidence the default optimization path, treats shared-memory and distributed CPU parallelism as first-class protocol capabilities, and keeps GPU implementation strictly conditional on explicit architectural authority.
