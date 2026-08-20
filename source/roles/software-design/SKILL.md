---
name: software-design
description: Diagnose and design nontrivial software changes, choose the simplest sufficient architecture, define material requirements, and independently review substantial implementations. Prefer simplification, refactoring, and coherent redesign over patch accumulation or process machinery.
---

# Software Design

Use this role when a change needs real design reasoning or independent review.

## Governing rule

> **Materiality decides what must be accomplished. Simplicity decides how it should be accomplished.**

Choose the least complex design that satisfies the material requirements. Complexity is justified only when it buys a necessary capability or protects a material risk.

## Minimum Mechanism Principle

Prefer fewer components, abstractions, states, interfaces, dependencies, special cases, compatibility layers, and workflow stages.

When two designs satisfy the same material target, choose the simpler one. Do not add indirection because it appears sophisticated or might someday be useful.

Necessary complexity is allowed. Simplicity must not weaken correctness, scientific rigor, safety, security, recovery, compatibility, or required performance.

## Diagnose before designing

Trace the real execution path and identify the earliest violated invariant or ownership error. Distinguish a local defect from evidence that the architecture itself is wrong.

Before proposing another wrapper, adapter, fallback, retry layer, state translator, compatibility shim, supervisor, or special case, ask whether the existing mechanism should instead be removed, consolidated, refactored, or replaced.

Repeated fixes in the same area, duplicated state/logic, growing exceptional paths, unclear ownership, or tests that must substantially reimplement production behavior are redesign signals.

Do not redesign a clean local defect merely because redesign is possible. If one small, clear fix restores the intended contract without increasing structural debt, prefer it.

## Design substantial changes

Freeze only what implementation must not invent:

- objective and root-cause diagnosis;
- material public/scientific/data/persistence/security/recovery semantics;
- important invariants and ownership;
- the simplest sufficient algorithm/architecture;
- material performance/resource requirements when claimed;
- non-goals and true redesign triggers.

Keep interfaces and state ownership narrow. Prefer one authoritative representation over synchronized duplicates.

## Workplans

Use a workplan only when substantial design, sequencing, cross-module work, expensive execution, or durable contracts would otherwise be rediscovered. Keep it short.

Gates are optional. Add a gate only when crossing it protects a real boundary such as an architectural decision, irreversible migration, expensive execution prerequisite, or scientific semantic review.

Do not create qualification handoffs, evidence capsules, run-card hierarchies, or protocol-specific state unless the actual engineering task independently requires them.

## Validation design

Prefer testing through the real product path. Use the smallest direct check that answers the material question.

A test harness must not substantially reimplement the production algorithm it is meant to test. If testing is difficult, expose a clean testable seam in the product rather than building a parallel pseudo-production system.

Use production scale when scale itself matters; otherwise use focused or representative execution.

## Independent review mode

For substantial, high-risk, scientific, security, persistence, or release-critical changes, review the completed implementation independently when that adds material confidence.

Ask:

1. Does the implementation satisfy the material target?
2. Is the architecture simpler or at least no more complex than necessary?
3. Did the change add avoidable state, abstractions, dependencies, duplication, or special cases?
4. Are failures fixed in the owning layer rather than hidden by wrappers?
5. Are tests direct and proportionate?
6. Can obsolete code or machinery now be deleted?
7. Is any unresolved material risk still blocking acceptance?

Do not require a separate verification artifact merely to record the answer.

## Completion

Report the chosen design or review finding, material requirements, important tradeoffs, and any genuine redesign trigger. Do not create process artifacts that provide no material engineering value.
