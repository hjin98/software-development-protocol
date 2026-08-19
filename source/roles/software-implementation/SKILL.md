---
name: software-implementation
description: Implement a specified software change, especially from a Protocol v3 workplan. Edit product code/tests/harnesses within frozen material design, run available checks, prepare real cross-environment qualification when needed, and return design contradictions instead of silently changing semantics.
---

# Software Implementation

Use this role as Protocol v3 implementation authority.

## Preflight

Read the governing workplan when one exists and confirm its material assumptions still apply. Do bounded revalidation across changed assumption/contract surfaces; do not repeat broad design work without evidence of staleness.

## Implement

Own local helpers, naming, bounded refactors, test fixtures, instrumentation, vectorization mechanics, and equivalent techniques that preserve the frozen target.

Run cheap/available structural, focused, oracle/property, and integration checks. Do not fabricate unavailable workstation/HPC/production/hardware results.

## Candidate boundary

For normal Git work, the candidate commit plus absence of unintended product-defining working-tree changes is sufficient source identity. Use extra hashes only at real external/generated content boundaries.

Before cross-environment qualification, commit/stage the actual product/spec/package state intended to be tested according to repository policy.

## Qualification preparation

Create a compact Qualification Handoff/run card only when execution genuinely crosses an environment boundary. Freeze:

- candidate commit;
- material checks and acceptance criteria;
- material dataset/config/backend/hardware requirements;
- product-defining things qualification must not change.

Do not try to predict exact shell quoting, cwd, scratch paths, or log destinations unless they are material.

## Failures and reruns

A product/test-contract defect is fixed here and affected material checks rerun. A frozen-target contradiction returns to `software-design`.

Do not create new workplan revisions or requalification solely for report metadata, evidence filenames, hashes, or harmless harness corrections.

Rerun a check when a changed dimension could plausibly affect its result or interpretation.

## Completion

Report candidate commit, implemented material requirements, checks actually run, true external checks still needed, and any substantive blocker. Administrative corrections are not blockers.
