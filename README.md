# Software Development Protocol

**Software Development Protocol** is a role-separated Agent Skills framework for disciplined, evidence-driven software engineering with AI coding agents. It is designed to divide development work between a **design/review role** and an **implementation/qualification role**, allowing expensive repository analysis, debugging, algorithmic redesign, and architectural reasoning to be completed once and handed off cleanly for execution.

The protocol provides two generated Agent Skills:

- **`software-design-review`** — inspects repositories, diagnoses root causes, evaluates algorithms and architecture, defines scientific and engineering invariants, creates Implementation Workplans, and reviews completed changes for conformance.
- **`software-implementation`** — consumes an approved workplan, performs bounded revalidation, implements changes gate by gate, runs focused and broad tests, benchmarks performance, records evidence, and completes specification, documentation, version, and release closeout.

The formal interface between the two roles is an **Implementation Workplan**: a versioned, auditable handoff that freezes design decisions, scope, invariants, acceptance criteria, and implementation gates so the implementation agent does not need to repeat the original investigation.

The shared protocol also defines engineering practices for correctness and testing, scientific/numerical fidelity, CPU/GPU/RAM/VRAM optimization, disk I/O and storage, persistence and recovery, concurrency, configuration, security and trust boundaries, Git safety, documentation governance, versioning, and release qualification.

`source/` contains the canonical shared protocol and role definitions. `dist/` contains the generated, self-contained Agent Skills intended for installation. Generated skills should not be edited independently; changes should be made to the canonical source and rebuilt so both roles remain consistent.
