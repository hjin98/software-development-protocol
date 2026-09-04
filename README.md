# Software Development Protocol

Software Development Protocol 5 is an engineering-fitness-first workflow for AI-assisted software engineering.

## Governing doctrine

```text
product engineering fitness > minimum justified product/system complexity > development economy
```

Protocol 5.14 makes the authority boundary behind that hierarchy explicit:

```text
stakeholder/domain problem truth
        +
explicitly Frozen high-level architecture for the current cycle
        = Tier 1

all lower-level implementation realization
        = Tier 2

development-process cost
        = Tier 3
```

The durable stakeholder product is the objective. Workplans, tests, gates, metrics, reviews, reports, and current implementation machinery are constraints, evidence, or solutions—not product truth.

Implementation details do not become invariants merely because they exist, have dependents, are tested/documented, were named in an earlier plan, or survived previous repairs. If the current realization creates an intermediate problem, the protocol first asks whether simplifying or replacing that realization makes the problem disappear.

## Active simplicity

Tier 2 is an active restoring policy, not a passive preference. A clean local bug still receives a clean local owning-layer fix. But repeated patches, wrappers/fallbacks/special cases, duplicated or synchronized state, competing authorities, repeated reconciliation machinery, or an evident materially simpler realization require Tier-2 simplification/re-derivation before another additive durable repair.

A new mechanism is justified when Tier-1/Frozen requirements need a capability the simplified system cannot provide cleanly, or when one canonical mechanism replaces broader duplicated machinery and lowers total system complexity.

## Two-role lifecycle

```text
software-design -> software-implementation
```

`software-design` separates the original product/problem invariants from cycle-scoped Frozen high-level architecture and delegated solution space. `software-implementation` preserves Tier 1 while remaining free to reduce, consolidate, refactor, or replace Tier-2 machinery. A change crossing the Frozen architecture boundary routes back to Design on evidence rather than being silently substituted.

Affected-surface growth expands implementation/testing impact; it does not by itself create new product requirements or freeze the mechanism that exposed the surface.

## Deterministic progressive disclosure

Protocol 5.14 preserves Protocol 5.13 relation-first optional-tool routing:

```text
literal/path/text -> ordinary repository search/read
symbol owner/definition/reference/caller -> Serena
AST/syntax/structural pattern -> Semgrep
broad Python input/state invariant -> Hypothesis
interprocedural flow/taint/source-to-sink -> CodeQL
```

Specialized tools remain bounded evidence instruments, not lifecycle gates or task authority. Tool availability never creates a mandatory multi-tool pipeline.

## Acceptance and convergence

Executable changes retain focused checks, stage-local affected regression for every material behavior-changing stage, final affected-surface re-derivation/regression, integration through real product/consumer boundaries, repository/project-required checks, proxy-proof real-owner acceptance, and separate production qualification where material.

A first clean local defect remains local. Material sibling recurrence stops repeated instance patching and moves reasoning to the shared owner/mechanism. When recurrence is also evidence of accumulated solution complexity, simplification comes before another additive durable closure. Finite family census remains available when the real correctness claim requires bounded completeness or when it is needed to simplify/canonicalize safely.

Independent review remains Software Design mode, not a third lifecycle role. Ordinary implementation misses and review cycles do not require numbered workplan revisions.

## Repository layout and validation

`source/` is canonical. `dist/skills/<skill-name>/` contains ready-to-install directory bundles; top-level ZIPs remain backward-compatible generated transports. See `PORTABILITY.md` for installation, reference-routing qualification, and live tool-routing qualification.

Before a protocol revision is complete:

```bash
python -m pip install -r source/requirements-validation.txt
python -m unittest discover -s tests -v
python source/build_skills.py --output /tmp/protocol-dist
python source/validate_packages.py --dist /tmp/protocol-dist
python source/check_dist.py --expected /tmp/protocol-dist --committed dist
git diff --check
```
