# Engineering Documentation and Evidence

## Materiality first

Documentation and evidence should make software contracts and decisions understandable. They must not become a parallel acceptance system whose formatting or provenance metadata can invalidate otherwise sound software evidence.

## Document roles

- **Architecture**: accepted current structure, ownership, invariants, data/control flow, persistence/resource/security boundaries.
- **Specification**: accepted current public/data/configuration/persistence/numerical behavior.
- **Implementation Workplan**: temporary transition contract for substantial work.
- **Qualification run card**: optional cross-environment execution contract.
- **Qualification evidence/report**: what actually ran and what happened.
- **Verification record**: material findings and final decision.
- **History/changelog/release notes**: chronology of completed user/release-significant changes.
- **User/API guide/runbook**: stable use/operation instructions.

Keep one normative owner for each current contract. Link rather than duplicate large content.

## Specification-code parity

When implementation materially changes a public API, persisted format, configuration semantics, numerical convention, error/fallback behavior, resource policy, compatibility promise, or other specified contract, update the owning specification before acceptance.

This remains acceptance-critical because stale specifications can cause real downstream misuse.

Do not require specification edits for implementation details that do not change a specified contract.

## Architecture parity

Update architecture documentation only when accepted architecture actually changes: ownership, component boundaries, dependency direction, durable persistence/concurrency/security architecture, or similarly structural behavior.

Do not write gate history or temporary project status into architecture manuals.

## History/version/release notes

Follow repository lifecycle policy. Release-bearing or user-visible completed changes should be reflected in version/history/release notes when the repository relies on them.

A version field is acceptance-critical only when version correctness is part of the deliverable: release artifacts, compatibility negotiation, schema/model/protocol behavior, or user-visible package identity.

A stale administrative version label in an evidence record does not invalidate executed software evidence.

## Markdown and derived formats

Prefer Markdown as editable source for engineering documentation.

Generate PDF or other derived formats when the project actually ships, publishes, archives, or explicitly requires them. PDF generation and provenance manifests are not universal protocol acceptance requirements.

When a derived document is a required shipped artifact, verify it against its source and inspect layout/content proportionally. Content digests are useful at that real source-to-generated-artifact boundary.

## Evidence records

A useful evidence record contains only what is needed to understand the claim:

- candidate/source commit or materially sufficient source identity;
- acceptance requirement/check;
- material input/config/environment conditions;
- command or method actually used when useful for reproduction;
- observed result/measurement;
- PASS/FAIL/BLOCKED;
- important limitations.

For performance, additionally record workload and material hardware/resource/precision conditions. For scientific work, record material data/model/precision/oracle conditions.

Do not require workplan hashes, handoff hashes, evidence-file hashes, timestamps, renderer versions, or structured manifests unless they materially protect interpretation or project/release/compliance policy explicitly requires them.

## Structured run manifests

Machine-readable manifests are useful for expensive, resumable, automated, scientifically important, or release/compliance workflows. They are optional tooling, not a default prerequisite for acceptance.

Record only material provenance dimensions. Do not add fields merely because they can be hashed.

## Evidence correction

Administrative corrections may be made after execution without rerunning product checks when they do not change candidate code, material inputs/environment, acceptance semantics, or interpretation of the observed result.

Never rewrite a failed software result into PASS by editing documentation.

## Closeout

Before accepting substantial work, as applicable:

1. compare material specified contracts with implemented behavior;
2. update architecture only for actual architectural change;
3. update user/release/history/version material required by repository policy;
4. build/verify derived documents only when they are required products;
5. ensure evidence clearly supports the acceptance-critical requirements;
6. keep temporary coordination records from becoming competing product specifications.
