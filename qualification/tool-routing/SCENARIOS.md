# Protocol 5.15 Live Tool-Routing Scenarios

These scenarios qualify **observed harness/model/tool behavior**, not generic protocol validity. Run only combinations whose external capability is actually available. A static parser, package validator, or different harness does not establish a live routing claim.

For every scenario, start from a fresh session with the current packaged lifecycle skill. For material Python/C++ executable work, first expect the Protocol 5.15 language-profile route. When the harness exposes a trajectory, capture enough evidence to establish a **direct tool-specific reference read** followed by **specialized tool invocation or concrete permitted fallback**.

Silent preference for built-in search/read/shell/test primitives is **not a permitted fallback** after a specialized trigger. Tool presence does not create a mandatory multi-tool pipeline.

## Serena initiating regression

This remains the **minimum live regression** when a trace-bearing Serena-enabled harness and supported repository are available.

Prerequisite: Serena semantic tools exposed and a nontrivial repository/language supported by the configured backend.

Prompt shape:

> Identify the definition/semantic owner of `<known symbol>` and determine its callers/references or affected semantic chain. Use the repository's development protocol.

Expected evidence:

- direct read of `references/tool-serena.md`;
- if the task is material Python/C++ executable work, the matching language profile read first or as part of the same routing decision;
- a cheap availability/capability probe if Serena availability is not already established;
- Serena semantic symbol/reference/caller operations when supported;
- ordinary text/config/runtime/build cross-checks only where they add coverage for semantic blind spots;
- concrete permitted fallback if Serena cannot reliably model the relation.

For C/C++, a valid fallback/cross-check may be required when the semantic backend lacks the actual compilation database/include/macro configuration.

## Semgrep structural-variant scenario

Prerequisite: Semgrep available for a supported language and repository surface.

Prompt shape:

> A diagnosed construct `<pattern>` violates `<invariant>`. Find structurally equivalent variants across the bounded affected surface and state the scan limitations.

Expected evidence:

- direct read of `references/tool-semgrep.md`;
- Semgrep invocation with a focused rule/configuration when its model fits;
- scan target/exclusion/suppression awareness for a negative/completeness claim;
- known-positive/known-negative validation when a custom acceptance-critical rule is relied upon;
- concrete fallback if Semgrep cannot reliably model language type/lifetime/build semantics required by the claim.

## Hypothesis property/state scenario

Prerequisite: Python test surface with Hypothesis available and governed behavior exposing a meaningful broad/combinatorial input or operation/state space.

Prompt shape:

> Validate `<governed invariant>` over the meaningful input/state space rather than only hand-picked examples.

Expected evidence:

- Python language-profile route for material executable work;
- direct read of `references/tool-hypothesis.md`;
- Hypothesis property/stateful use when generated exploration materially strengthens coverage;
- representative bounded strategies and independent property/oracle semantics;
- no anti-gaming narrowing solely to make the property green;
- concrete fallback for an already-exhaustive finite case or unavailable/inapplicable Hypothesis surface.

## C++ property/generative/fuzz scenario

Prerequisite: a C++ input/state/parser/binary surface where broader exploration materially strengthens evidence and an appropriate project mechanism is available.

Prompt shape:

> Validate `<governed invariant or parser boundary>` across the meaningful C++ input/state space and choose property/generative/fuzz evidence appropriate to the claim.

Expected evidence:

- C++ language-profile read;
- project-appropriate property/generative mechanism, bounded deterministic generation, or libFuzzer/AFL++-class fuzzing according to the actual relation;
- no new testing dependency added solely for protocol symmetry;
- an independent semantic property/oracle when a property claim is made;
- recognition that fuzzing and semantic property testing are complementary rather than interchangeable.

## CodeQL interprocedural-flow scenario

Prerequisite: CodeQL CLI/query support for the repository language and a bounded source-to-sink/data-flow claim whose relation is not sufficiently established by structural search alone.

Prompt shape:

> Determine whether `<source>` can reach `<sink>` through the relevant interprocedural flow and establish the analysis scope/provenance.

Expected evidence:

- direct read of `references/tool-codeql.md`;
- active language-profile read for material Python/C++ executable work;
- availability/query/database probe as needed;
- appropriate database/query execution when feasible;
- candidate/build/extraction/query identity adequate to interpret the result;
- no claim that hosted result storage proves a separate execution;
- concrete fallback if language/build/extraction/query support is unavailable or disproportionate.

## C++ memory/lifetime/UB scenario

Prerequisite: changed C++ executable code with material lifetime, bounds, initialization, aliasing/alignment, or UB risk and relevant compiler/runtime instrumentation available.

Prompt shape:

> Review and validate `<affected C++ path>` for memory/lifetime/UB defects using the repository protocol and the highest-return available evidence.

Expected evidence:

- direct C++ profile read;
- accurate build configuration/compilation database awareness when semantic tooling depends on it;
- ASan/UBSan/compiler/clang-tidy-class evidence selected for the actual defect class, not a ceremonial full matrix;
- optimized/production-like correctness checked separately when build mode can alter behavior;
- no inference that sanitizer silence proves all lifetime or schedule properties.

## C++ race/synchronization scenario

Prerequisite: shared-memory C++ change with material synchronization/race risk and TSan-class or equivalent evidence available.

Expected evidence:

- C++ profile and shared concurrency owner read;
- race-specific instrumentation/stress/state-transition evidence rather than generic profiling;
- nested OpenMP/thread/library-runtime configuration recorded when it affects the test;
- no claim that one race-free execution proves all schedules safe.

## C++ performance/vectorization scenario

Prerequisite: representative C++ hot path with compiler/profiler support.

Prompt shape:

> Improve `<hot path>` under the accepted performance/scientific contract, diagnosing vectorization and avoiding unjustified SIMD complexity.

Expected evidence:

- shared performance + C++ profile route;
- production-like optimized baseline;
- representative sampling/profile and compiler vectorization diagnostics before intrinsics;
- tuned numerical-library mapping considered first where applicable;
- explicit AVX/AVX2/AVX-512/NEON/SVE intrinsics only if the remaining dominant kernel justifies them;
- no portable product silently made ISA-specific;
- quantitative speedup claim only from comparable representative measurements.

## Qualification result format

A release/PR closeout may record, without creating a mandatory persistent ledger:

- harness/model identity;
- active language profile(s), when applicable;
- installed/exposed tool and relevant backend/engine/compiler/CLI version when material;
- repository/candidate used;
- scenario exercised;
- direct reference read observed: yes/no/unobservable;
- specialized invocation observed: yes/no;
- fallback, if any, and why it is permitted;
- overall claim: qualified / failed / unqualified because unavailable.

**Never generalize one result to another harness/model/tool combination.** A correct static Protocol 5.15 implementation may ship with all live combinations marked unqualified when no suitable external environment is available; the release must then limit its claim to protocol-level deterministic routing semantics.
