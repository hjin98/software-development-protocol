# Resource-Bounded, Autonomous Execution

## Purpose

Potentially expensive development, testing, benchmarking, and qualification must be useful without endangering the machine that runs them. Resource safety and materiality apply together:

> Use the smallest materially sufficient workload, adapt it to the effective machine, plan to finish comfortably inside hard limits, and treat hard-limit activation as exceptional containment rather than normal control flow.

A hard resource boundary is mandatory when a workflow could otherwise consume unsafe RAM, VRAM, storage, CPU, process, or wall-time resources. It is not a utilization target.

## Three resource layers

Keep three concepts distinct:

1. **effective capacity** - the resources actually available to the job after affinity, cgroup/container, scheduler, quota, device, filesystem, and explicit user/project constraints;
2. **hard safety ceiling** - the containment boundary that prevents runaway execution from exhausting the host or allocation;
3. **planned operating envelope** - a smaller workload/resource target with material headroom below the hard ceiling.

Do not hard-code one machine's limits into a general protocol. Discover the effective allocation and honor explicit user/project caps. Missing secondary telemetry is non-blocking when a conservative safe envelope can still be established.

## Admission before execution

Before an uncertain expensive stage, use a cheap calibration or conservative model to estimate the resources that scale with workload: wall time, transient/retained memory, scratch growth, I/O, worker concurrency, or accelerator memory as applicable.

Calibration must itself be bounded and must not perform the full expensive operation merely to estimate it.

Admit the stage only when the selected workload is expected to finish with substantial headroom inside the planned operating envelope. A watchdog remains independent containment if the estimate is wrong.

## Smallest materially sufficient workload

Qualification and benchmarking are measurement experiments, not production replays.

Unless full production scale is itself the property under test, choose the smallest representative workload that can establish the acceptance claim. Prefer focused fixtures plus representative real-data slices, bounded scaling ladders, authenticated compatible prior evidence, or conservative projections over repeating an entire production workflow.

Reduced workloads must preserve the material mechanism or performance regime. Do not shrink a test across an algorithmic phase change, remove the state transition being qualified, weaken scientific fidelity, or change acceptance semantics merely to make it cheap.

Full production-scale qualification requires explicit material justification when a bounded representative check cannot establish the claim.

## Automatic adaptation

Within frozen semantics, a harness should adapt execution mechanics automatically before declaring a resource blocker. Prefer, as applicable:

1. reuse compatible valid evidence;
2. remove redundant copies/materialization and share immutable inputs read-only;
3. reduce unnecessary repetitions once confidence is sufficient;
4. reduce representative sample/rung/problem size while preserving the claim;
5. reduce concurrency, batch size, or in-flight work;
6. chunk or stream instead of materializing;
7. select another semantically equivalent bounded execution method.

Adaptive execution mechanics are allowed. Adaptive acceptance semantics are forbidden.

If the minimum materially sufficient workload cannot be executed safely on the available machine, mark the required check `BLOCKED`. Do not repeatedly collide with hard ceilings or simply raise them.

## Hard-limit activation

A hard-limit hit does not automatically mean the product failed.

- If an oversized or poorly modeled qualification workload reaches containment, treat it as a harness/resource-model defect and redesign or resize the check.
- If a properly designed materially representative measurement demonstrates that the product violates a frozen resource/performance requirement, treat that as a product/material failure.

Do not use watchdog termination as ordinary benchmark flow.

## Autonomous external execution

Nontrivial workstation/HPC/external qualification should be as autonomous as practical. Prefer a standalone, one-command supervisor that can:

- discover the effective resource envelope;
- perform bounded calibration and choose a safe workload;
- execute independent checks without an agent session remaining connected;
- persist compact stage state so completed checks need not rerun unnecessarily;
- continue past non-fatal secondary/advisory defects when safe;
- classify material product failure, environment blocker, and harness defect distinctly;
- emit compact evidence sufficient for later verification.

Do not require continuous human or agent intervention merely to advance ordinary qualification stages.

## Transient-state ownership and cleanup

Separate durable compact evidence from disposable scratch. Every nontrivial run should own its transient paths explicitly.

On PASS, FAIL, BLOCKED, ordinary exceptions, cancellation, and catchable termination signals, remove run-owned large intermediates once compact diagnostic evidence needed for interpretation/restart has been retained. Do not preserve huge scratch trees merely because the run failed.

Because SIGKILL, power loss, kernel failure, and similar events cannot guarantee cleanup handlers, autonomous harnesses that create material scratch should perform safe startup scavenging of abandoned run-owned transient state. Scavenging must require clear ownership; never delete unrelated user data based only on filename or age.

Evidence/logging must itself be bounded. Preserve a small failure capsule such as stage, failure classification, selected workload, resource observations, relevant material identities, final progress position, and useful log tail rather than retaining large intermediates.

## Materiality and graceful degradation

Do not turn observability into an acceptance system.

Only information needed for safe admission, adaptive execution, interpretation of the material claim, or diagnosis is blocking. Missing optional telemetry, advisory estimates, optional benchmark repetitions, report formatting, secondary diagnostics, or provenance fields must not halt an otherwise safe and interpretable execution.

Independent checks should continue after a non-fatal failure when doing so is safe and useful. Optional checks that do not support a current acceptance-critical requirement may be recorded as unavailable/skipped without disqualifying valid executed evidence.

## Sequential confidence acquisition

Prefer acquiring evidence from cheap to expensive and stop when the acceptance claim is already established with adequate confidence. Run additional repetitions or larger scaling points when they could change the decision, not merely because a fixed matrix exists.

This rule does not permit skipping a mandatory material check. It prevents unnecessary work after its material claim is already established.

## Hard rules

- Hard ceilings protect the host; planned workloads should not routinely approach them.
- Do not launch a full production replay when a bounded representative benchmark can establish the same claim.
- Do not automatically raise a resource limit after containment activates.
- Do not weaken product/scientific/acceptance semantics through adaptive qualification.
- Do not let secondary/advisory diagnostics block material execution.
- Do not leave owned large transient data after normal terminal paths when compact evidence is sufficient.
- Do not delete transient data whose ownership is uncertain.
