---
name: software-qualification
description: Execute the checks that materially qualify a software candidate in the required runtime, production-data, hardware, integration, or distribution environment. Keep product-defining candidate content unchanged, repair harmless harness/report errors locally, and return only real product/design/environment blockers.
---

# Software Qualification

Qualification answers: **does the intended candidate pass the acceptance-critical checks under the material conditions that matter?**

Read the workplan and, when execution crossed an environment boundary, the qualification run card.

## Preflight

Confirm the intended candidate commit/source is being exercised and no unintended local product source shadows it. Verify only the inputs/environment that materially affect the checks.

## Execute

Run required checks from cheap to expensive when useful: focused/broad tests, integration/recovery, package/install, production scale, target hardware/backend.

A mandatory check that did not execute cannot PASS.

## Harness correction authority

You may correct non-material execution defects in place: cwd, quoting, activation command, scratch/log paths, unambiguous intended config path, equivalent test-runner syntax, and report metadata. Record what actually ran.

Do **not** silently change product code, scientific/dataset/config/backend semantics, resource policy relevant to a claim, or acceptance thresholds to obtain PASS.

## Routing

- real product/material failure -> `RETURN_TO_IMPLEMENTATION`;
- frozen target/acceptance contradiction -> `DESIGN_REVISION_REQUIRED`;
- required environment/input unavailable -> `BLOCKED`;
- harmless harness/record defect -> correct locally and continue.

## Evidence

Record enough to interpret the result: candidate commit, material inputs/config/environment, actual method/command when useful, measurements, PASS/FAIL/BLOCKED, and important limitations.

Do not reject valid evidence solely for missing advisory hashes, timestamps, filenames, or redundant identity fields.

## Postflight

Verify qualification did not unintentionally modify product-defining candidate content. Build/log/report/scratch outputs are ordinary evidence outputs.

Do not declare `MERGE_READY`; final acceptance belongs to verification.
