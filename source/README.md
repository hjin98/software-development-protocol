# Software Development Protocol 5.4

This directory is the canonical Protocol 5.4 source.

## Governing hierarchy

> **Choose the globally best justified engineering-sufficient product. Among engineering-sufficient solutions, prefer the one with the lowest justified total product/system complexity. Among development processes that can establish that result with the required confidence, avoid unnecessary human, model, context/token, tool, compute, I/O, and wall-time cost.**

```text
product engineering fitness > minimum justified product/system complexity > development economy
```

Product engineering fitness defines the feasible solution space: functionality/capability, correctness and scientific/domain fidelity, reliability/recovery/safety/security/compatibility, CPU/RAM/VRAM/storage/I/O/wall-time feasibility, target scale, hardware effectiveness, and materially important end-to-end performance.

Among engineering-sufficient products, minimize unnecessary components, states, interfaces, dependencies, synchronization, duplicated authorities, compatibility paths, runtime/operational stages, special cases, and maintenance surface. Necessary specialization is valid when it provides material engineering value.

Development economy is third-order. Once the required product and acceptance confidence are preserved, eliminate redundant reasoning, rediscovery, low-information inspection, invalid reruns, repeated boilerplate, and unnecessary tool/compute work. Do not weaken a material requirement or required validation merely to reduce development cost.

## Lifecycle roles

Protocol 5.4 preserves the two-role lifecycle:

- `software-design` — diagnosis, engineering-envelope definition, globally justified architecture/algorithm/resource decisions, workplan authority, product-complexity review, validation design, and independent evidence-directed review;
- `software-implementation` — implementation/refactoring under accepted design authority, mandatory stage-local and final affected-surface regression plus integration testing, benchmarking/validation of material claims, cleanup, and delivery.

Testing and production qualification remain engineering activities, not additional lifecycle roles. `software-documentation` and `repository-hygiene` remain optional specialists, not approval gates.

## Accepted workplans

A substantial accepted workplan is a compressed implementation contract. It distinguishes **Frozen**, **Delegated**, and **Reopen only on evidence** decisions. Implementation should not repeat the design search after material choices are settled. Repository evidence can trigger local reconciliation or, when a frozen assumption is materially invalid, a bounded redesign of only the affected surface.

Workplans inherit generic protocol requirements from their declared `protocol_version`. A later protocol release does not silently reinterpret an older plan; adoption of a newer version is explicit and does not invalidate still-valid evidence by itself.

## Development context and evidence economy

Use progressive repository inspection and prefer the lowest-cost next action that most strongly resolves a material uncertainty or establishes required evidence. Reuse established facts and still-valid intermediate evidence until a changed dimension can plausibly invalidate them. Bound large file/log context without hiding relevant failures or affected behavior.

Load packaged references when their owned material surface is relevant; packaging alone does not make every reference mandatory for every task.

## Functional acceptance

Executable changes require:

- focused checks appropriate to changed mechanisms;
- affected regression after every coherent material behavior-changing implementation stage before dependent work proceeds;
- final re-derivation of the affected behavioral surface from the assembled implementation;
- final regression across that complete surface;
- integration testing through the assembled affected product path;
- repository/project-required checks, with the broader/full suite when impact cannot be bounded confidently.

Within a material stage, run cheap high-signal focused checks before the required affected regression. Reuse still-valid intermediate evidence where appropriate, but final assembled affected-surface regression/integration remains a fresh acceptance boundary.

Use bounded fixtures and representative workloads where they preserve required coverage. Test-cost minimization must never become coverage minimization.

## Production qualification

Full production qualification is distinct from functional testing. It characterizes an already functionally accepted candidate with real, long, data-heavy, target-machine/target-hardware execution for production-scale performance, resource use, scaling, recovery, and similar environment-specific properties.

Do not run full production qualification by default during implementation. Run it only when explicitly requested, required by project/release policy, or necessary to establish a material production-scale/resource/performance/hardware claim.

## Independent review

Independent review begins from the accepted requirements/workplan, final implementation/diff, final affected surface, executed evidence, deviations, and unresolved risks. It independently challenges high-risk assumptions and retains unrestricted authority to broaden. It need not replay the original architecture search from zero when no evidence challenges accepted premises.

## Build and repository acceptance

`source/` is canonical. `dist/` contains generated ready-to-install skill packages and is committed for distribution.

Run the protocol regression suite, build skill packages once, validate them independently, compare that exact build with committed `dist/`, and check whitespace:

```bash
python -m unittest discover -s tests -v
python source/build_skills.py --output /tmp/protocol-dist
python source/validate_packages.py --dist /tmp/protocol-dist
python source/check_dist.py --expected /tmp/protocol-dist --committed dist
git diff --check
```

All commands must succeed before a protocol revision is complete. Package validation complements source-to-dist parity: parity detects stale committed output, while independent validation checks that the shipped Skill structure is itself valid.
