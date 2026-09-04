# Protocol 5.13 Live Tool-Routing Scenarios

These scenarios qualify **observed harness/model/tool behavior**, not generic protocol validity. Run only combinations whose external capability is actually available. A static parser, package validator, or different harness does not establish a live routing claim.

For every scenario, start from a fresh session with the current packaged lifecycle skill. When the harness exposes a trajectory, capture enough evidence to establish:

```text
material question
-> correct direct tool-specific reference read
-> capability availability/capability check when needed
-> specialized tool invocation OR concrete permitted fallback
```

Silent preference for built-in text search/read/shell/test primitives is not a permitted fallback after a specialized trigger.

## Serena initiating regression

Prerequisite: trace-bearing harness with Serena semantic tools exposed and a nontrivial repository/language supported by the configured backend.

Prompt shape:

> Identify the definition/semantic owner of `<known symbol>` and determine its callers/references or affected semantic chain. Use the repository's development protocol.

Expected evidence:

- direct read of `references/tool-serena.md`;
- a cheap availability/capability probe if Serena availability is not already established;
- one or more Serena semantic symbol/reference/caller operations when supported;
- ordinary text/config/runtime cross-checks only where they add coverage for semantic blind spots;
- if Serena is skipped, a concrete permitted fallback reason visible in the trajectory/response.

This is the minimum live regression for the under-calling behavior that motivated Protocol 5.13 when a suitable Serena-enabled harness is available.

## Semgrep structural-variant scenario

Prerequisite: Semgrep available for a supported language and repository surface.

Prompt shape:

> A diagnosed construct `<pattern>` violates `<invariant>`. Find structurally equivalent variants across the bounded affected surface and state the scan limitations.

Expected evidence:

- direct read of `references/tool-semgrep.md`;
- Semgrep invocation with a focused rule/configuration when its model fits;
- scan target/exclusion/suppression awareness for a negative/completeness claim;
- known-positive/known-negative validation when a custom acceptance-critical rule is relied upon;
- concrete permitted fallback if Semgrep cannot reliably model the relation.

## Hypothesis property/state scenario

Prerequisite: Python test surface with Hypothesis available and governed behavior exposing a meaningful broad/combinatorial input or operation/state space.

Prompt shape:

> Validate `<governed invariant>` over the meaningful input/state space rather than only hand-picked examples.

Expected evidence:

- direct read of `references/tool-hypothesis.md`;
- Hypothesis property/stateful-test use when generated exploration materially strengthens coverage;
- representative bounded strategies and independent property/oracle semantics;
- no anti-gaming narrowing solely to make the property green;
- concrete permitted fallback for an already-exhaustive finite case or unavailable/inapplicable Hypothesis surface.

## CodeQL interprocedural-flow scenario

Prerequisite: CodeQL CLI/query support for the repository language and a bounded source-to-sink/data-flow claim whose relation is not sufficiently established by structural search alone.

Prompt shape:

> Determine whether `<source>` can reach `<sink>` through the relevant interprocedural flow and establish the analysis scope/provenance.

Expected evidence:

- direct read of `references/tool-codeql.md`;
- availability/query/database probe as needed;
- appropriate CodeQL database/query execution when feasible;
- candidate/build/extraction/query identity adequate to interpret the result;
- no claim that GitHub result hosting itself proves a separate execution;
- concrete permitted fallback if language/build/extraction/query support is unavailable or disproportionate for a trivially bounded claim.

## Qualification result format

A release/PR closeout may record, without creating a mandatory persistent ledger:

- harness/model identity;
- installed/exposed tool and relevant backend/engine/CLI version when material;
- repository/candidate used;
- scenario exercised;
- direct reference read observed: yes/no/unobservable;
- specialized invocation observed: yes/no;
- fallback, if any, and why it is permitted;
- overall claim: qualified / failed / unqualified because unavailable.

Never generalize one result to another harness/model/tool combination. A correct static protocol implementation may ship with all live combinations marked unqualified when no suitable external environment is available; the release must then limit its claim to protocol-level deterministic routing semantics.
