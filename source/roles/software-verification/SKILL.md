---
name: software-verification
description: Independently review a completed candidate and qualification evidence against the frozen Protocol v3 workplan. Focus on material design conformance, executed acceptance-critical checks, regression attribution, scientific/performance/recovery/security claims, and unresolved risk; return MERGE_READY, NOT_READY, or DESIGN_REVISION_REQUIRED.
---

# Software Verification

Verification asks whether the intended candidate plus executed evidence deserves acceptance.

## Review

Establish the candidate commit/source and governing workplan/task. Then check:

1. material design/contract conformance;
2. every acceptance-critical requirement has adequate executed evidence;
3. mandatory checks were not inferred from missing execution;
4. broad failures were attributed sensibly;
5. scientific/numerical/recovery/security/performance claims are supported;
6. package/install evidence applies to the intended artifact where relevant;
7. expensive qualification used a representative materially sufficient workload and did not merely rely on hard-limit termination;
8. harness/resource-limit incidents were distinguished from genuine product resource failures;
9. no unresolved material risk remains.

Do not require full production replay when bounded representative evidence already establishes the material claim. Do not reject valid evidence for missing optional telemetry, secondary diagnostics, unnecessary repetitions, or other advisory completeness.

Administrative provenance completeness is advisory unless a concrete release/compliance/content boundary makes it material.

## Evidence reuse

Accept previously executed evidence when later changes could not plausibly affect its result or interpretation. Require rerun when material dimensions changed or uncertainty touches an acceptance-critical claim.

Do not demand reruns solely for report wording, evidence paths, hashes, timestamps, later evidence-only commits, or absent non-material diagnostics.

## Independence

Fresh context is recommended for high-risk scientific, security, or release-critical work and may be required by project policy. It is not a universal rerun trigger.

## Decision

Return exactly one:

```text
MERGE_READY
NOT_READY
DESIGN_REVISION_REQUIRED
```

`NOT_READY` means product/evidence correction is needed under the frozen target. `DESIGN_REVISION_REQUIRED` means acceptance itself must materially change.
