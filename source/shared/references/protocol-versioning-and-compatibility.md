# Protocol Versioning, Candidate Identity, and Compatibility

## Protocol version

`PROTOCOL_VERSION` identifies the protocol contract. Use semantic-version intent:

- major: incompatible role/lifecycle authority change;
- minor: backward-compatible capability or doctrine addition;
- patch: clarification or defect correction.

A protocol version is interpretation metadata, not software acceptance evidence.

Protocol v3 uses four authority roles: design, implementation, qualification, and verification.

## Default candidate identity

For a normal Git repository, use:

```text
candidate_commit = <Git commit SHA>
```

plus a check that no unintended product-defining working-tree changes affect execution.

This is the default because Git already content-addresses the tracked tree. Do not add a second universal candidate-content digest merely to duplicate Git.

## When additional identity is material

Use hashes/manifests when they identify a real boundary not sufficiently represented by the candidate commit, for example:

- external datasets or mutable production snapshots;
- model weights/checkpoints supplied outside Git;
- source archives or generated binaries;
- wheels/release artifacts whose exact bytes matter;
- canonical-source/generated-artifact parity;
- configuration snapshots whose exact content materially changes a scientific or performance claim.

Record only the identity needed to interpret the check.

## Administrative metadata

Workplan SHA values, handoff/report digests, evidence-file hashes, repeated protocol-version fields, timestamps, filenames, and policy IDs are optional/advisory unless the current task makes them material to interpretation or an external compliance/release policy requires them.

A defect in advisory metadata does not invalidate otherwise applicable execution evidence and does not create a new candidate.

## Workplan revisions

Increment a workplan revision only for material changes to target design, acceptance criteria, important scope, or material qualification conditions.

Do not revise a workplan merely to fix shell commands, paths, report wording, evidence locations, or other non-material execution details.

## Evidence reuse and invalidation

Use one rule:

> Rerun a check when a changed dimension could plausibly alter that check's result or interpretation.

Examples:

- algorithm change -> rerun affected correctness/integration/performance checks;
- packaging change -> rerun package/build/install checks;
- GPU kernel change -> rerun affected GPU checks; unaffected CPU evidence may remain;
- report typo or evidence-only wording change -> rerun nothing.

When uncertainty concerns an acceptance-critical result, rerun conservatively. Structured dependency manifests are optional for unusually expensive programs.

## Attempts and retries

A repeated attempt remains under the same qualification while candidate behavior and material conditions are unchanged. Record any material differences between attempts.

Changing product code, scientific/dataset/configuration/backend semantics, or acceptance threshold is not a harmless retry; it is a changed candidate or changed contract.

## Evidence and coordination commits

Evidence may be committed after qualification. The evidence should state which candidate commit it applies to. A later evidence-only commit does not require requalification merely because repository `HEAD` changed.

If product source changes, decide affected reruns by materiality rather than by evidence-commit bookkeeping.

## v2 compatibility

Protocol v2 used `software-design-review` and `software-implementation` with a workplan-centered lifecycle.

- completed v2 work remains readable historical evidence;
- active substantial v2 work may migrate to v3 when split qualification is useful;
- do not rewrite completed history merely to conform to v3 artifact shapes;
- a v2 workplan can inform v3 design, but target execution should receive a clear current run contract when a cross-environment handoff is needed.

Protocol v3 is pre-freeze during the current four-role dogfood. Intermediate v3 hardening artifacts may be superseded without a major-version change when the four-role authority model remains intact.

## Materiality rule

No identity, versioning, or provenance mechanism is acceptance-critical solely because it improves traceability. It becomes blocking only when it protects a material software result or an explicitly required external release/compliance boundary.
