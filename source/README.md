# Software Development Protocol 5.7

This directory is the canonical Protocol 5.7 source.

## Governing hierarchy

> **Choose the globally best justified engineering-sufficient product. Among engineering-sufficient solutions, prefer the one with the lowest justified total product/system complexity. Among development processes that can establish that result with the required confidence, avoid unnecessary human, model, context/token, tool, compute, I/O, and wall-time cost.**

```text
product engineering fitness > minimum justified product/system complexity > development economy
```

**Engineering stewardship:** build for durable stakeholder capability and product truth. Never knowingly improve a local acceptance signal by degrading, narrowing, bypassing, redefining, concealing, or failing to establish the underlying product claim. Long-horizon quality remains bounded to accepted scope; it is not permission for speculative gold-plating.

Protocol 5.7 preserves this doctrine and all Protocol 5.3-5.6 guarantees. It adds shared engineering stewardship: every actor optimizes for the stakeholder's intended durable product, while workplans, tests, gates, metrics, reviews, and reports remain subordinate constraints/evidence rather than optimization targets. Protocol 5.6 proxy-proof semantic-owner acceptance remains fully in force.

## Lifecycle roles

Protocol 5.7 preserves the two-role lifecycle:

- `software-design` — diagnosis, engineering-envelope definition, globally justified architecture/algorithm/resource decisions, **lossless translation of accepted design into concrete implementation obligations**, validation design, product-complexity review, and independent evidence-directed review;
- `software-implementation` — adaptive realization under accepted design authority, repository reconciliation, **semantic/conformance closure plus mandatory stage-local and final functional acceptance**, benchmarking/validation, cleanup, and delivery.

Testing, independent review, and production qualification are engineering activities/modes rather than additional lifecycle roles. Optional specialists remain supporting capabilities, not approval gates.

## Lossless accepted workplans

A substantial accepted workplan is a compressed implementation contract. It keeps `Frozen / Delegated / Reopen only on evidence` authority while preserving each material protected concern, required end state/constraint, known required implementation consequence, useful affected surface, adaptable suggestion where appropriate, and acceptance evidence.

Compression removes repeated generic protocol doctrine, not task-specific intent. Before handoff, Design reconciles requirements and known consequences against the implementation obligations and their acceptance evidence.

The plan is the **minimum known contract, not a ceiling**. Implementation incorporates necessary consequences and affected surfaces discovered while realizing frozen design, and reopens design only when evidence shows a frozen material decision must change.

## Closed-loop implementation

A material implementation stage closes only when both:

- semantic/conformance closure establishes that its assigned obligations and protected concerns are satisfied or legitimately reconciled; and
- the existing focused checks and stage-local affected regression pass for executable behavior.

Before handoff, Implementation reconciles the complete accepted contract against the final candidate, inspects structural/absence claims and product-complexity/ownership drift, then re-derives the final affected surface and performs fresh final affected regression, integration, and repository-required checks.

## Proxy-proof acceptance

For material integration/acceptance claims, the real production semantic owner/consumer boundary named by the claim must execute. Mocks/fakes remain valid below or outside that boundary for expensive computation, hardware, services, or bounded data, but evidence that could stay green while the claimed owner is broken cannot close the claim. Detailed rules live in `shared/references/testing-and-validation.md` and the role entrypoints.

## Independent review and rework

Independent review remains a Software Design activity. It first challenges contract conformance, then independently challenges unplanned engineering risk. Material findings must be actionable enough for lossless rework and route separately as implementation nonconformance, workplan/design deficiency, or a genuinely new issue. Equivalent preferences without material engineering benefit do not block acceptance.

## Development context and evidence economy

Protocol 5.4 development-economy rules remain intact: use progressive repository inspection, high-information actions, established-fact reuse, compact task-local state, and evidence invalidation/reuse without narrowing required behavior or validation.

## Production qualification

Full production qualification remains distinct from functional acceptance and is not run by default during ordinary implementation. A production run never substitutes for missing regression/integration coverage.

## Build and repository acceptance

`source/` is canonical. `dist/` contains generated ready-to-install skill packages and is committed for distribution.

Run:

```bash
python -m unittest discover -s tests -v
python source/build_skills.py --output /tmp/protocol-dist
python source/validate_packages.py --dist /tmp/protocol-dist
python source/check_dist.py --expected /tmp/protocol-dist --committed dist
git diff --check
```

All commands must succeed before a protocol revision is complete.
