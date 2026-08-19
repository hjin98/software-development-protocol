# Software Development Protocol v3

This directory is the canonical source library for Protocol v3.

Protocol v3 separates four software-development authorities:

- `software-design` — diagnosis, target design, invariants, and acceptance-critical requirements;
- `software-implementation` — product/test/harness construction under the frozen target;
- `software-qualification` — execution of required checks in the needed environment, with harmless harness corrections allowed;
- `software-verification` — final material conformance/evidence review and merge-readiness decision.

The protocol is **materiality-first**: a process condition blocks acceptance only when it can materially affect the code executed, relevant inputs/configuration/environment, correctness/scientific interpretation, recovery/security behavior, installability, performance/resource claim, or regression attribution. Administrative provenance and report-format issues are advisory unless the current task makes them materially important.

A workplan is used for substantial design. A separate qualification run card is used when execution genuinely crosses an environment boundary. Neither is ceremony for its own sake.

`source/` is canonical. `dist/` contains generated self-contained role skills. Do not hand-edit generated packages; rebuild/check them with:

```bash
python build_skills.py --output ../dist
python check_protocol_semantics.py
python check_protocol_lifecycle_cases.py
python build_skills.py --output ../dist --check
```
