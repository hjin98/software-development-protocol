---
name: software-qualification
description: Execute the checks that materially qualify a software candidate in the required runtime, production-data, hardware, integration, or distribution environment. Keep product-defining candidate content unchanged, repair harmless harness/report errors locally, and return only real product/design/environment blockers.
---

# Software Qualification

Qualification answers: **does the intended candidate pass the acceptance-critical checks under the material conditions that matter?**

Read the workplan and, when execution crossed an environment boundary, the qualification run card.

## Preflight

Confirm the intended candidate commit/source is being exercised and no unintended local product source shadows it. Verify only the inputs/environment that materially affect the checks.

For potentially expensive execution, discover enough of the effective CPU/RAM/VRAM/storage/job allocation to establish a safe machine-specific envelope. Missing secondary telemetry is non-blocking when a conservative safe envelope remains possible.

## Execute

Run the smallest materially sufficient checks from cheap to expensive: focused/broad tests, integration/recovery, package/install, representative real-data or target-hardware benchmarks, and full production scale only when scale itself is materially required.

A mandatory check that did not execute cannot PASS. Conversely, optional telemetry, advisory diagnostics, and secondary checks that are not acceptance-critical do not block otherwise valid execution.

Potentially expensive checks should calibrate cheaply when cost is uncertain, select a workload expected to finish comfortably below hard safety ceilings, and adapt non-semantic execution parameters automatically. Do not use watchdog termination as ordinary benchmark flow.

Prefer autonomous one-command execution for nontrivial workstation/HPC runs. Continue independent checks after non-fatal secondary defects when safe and useful; do not require an agent session merely to advance ordinary stages.

## Resource failure classification

- oversized/poorly modeled qualification workload reaches containment -> harness/resource-model defect; resize or redesign within frozen semantics;
- minimum materially sufficient check cannot fit safely after allowed adaptation -> `BLOCKED`;
- properly designed material measurement violates a frozen product resource/performance requirement -> product/material failure.

Do not automatically raise hard resource limits after containment activates.

## Scratch and failure cleanup

Keep compact durable evidence separate from disposable run-owned scratch. On PASS, FAIL, BLOCKED, exceptions, cancellation, and catchable termination, preserve only the compact diagnostic state needed for interpretation/restart and clean owned large intermediates.

Where abrupt termination could bypass cleanup, use safe startup scavenging of abandoned run-owned scratch. Never delete data whose ownership is uncertain.

## Harness correction authority

You may correct non-material execution defects in place: cwd, quoting, activation command, scratch/log paths, unambiguous intended config path, equivalent test-runner syntax, report metadata, safe workload sizing, and equivalent resource-aware execution mechanics. Record what actually ran.

Do **not** silently change product code, scientific/dataset/config/backend semantics, resource policy relevant to a product claim, workload representativeness, or acceptance thresholds to obtain PASS.

## Routing

- real product/material failure -> `RETURN_TO_IMPLEMENTATION`;
- frozen target/acceptance contradiction -> `DESIGN_REVISION_REQUIRED`;
- required environment/input or minimum safe material workload unavailable -> `BLOCKED`;
- harmless harness/record/secondary diagnostic defect -> correct, degrade, record, or skip as appropriate and continue.

## Evidence

Record enough to interpret the result: candidate commit, material inputs/config/environment, actual representative workload/method when useful, measurements, PASS/FAIL/BLOCKED, important limitations, and any resource adaptation that matters to interpretation.

Do not reject valid evidence solely for missing advisory hashes, timestamps, filenames, optional telemetry, redundant identity fields, or unnecessary benchmark repetitions.

## Postflight

Verify qualification did not unintentionally modify product-defining candidate content. Clean run-owned large transient state while retaining compact evidence needed for verification.

Do not declare `MERGE_READY`; final acceptance belongs to verification.
