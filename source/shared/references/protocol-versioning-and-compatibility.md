# Protocol Versioning and Compatibility

## Purpose

`PROTOCOL_VERSION` identifies the Software Development Protocol contract implemented by the generated role skills and handoff artifacts. It is independent of any project/package/schema/model version governed by a repository using the protocol.

Use semantic-version intent:

- **major** — incompatible role, lifecycle, handoff-artifact, authority, or state-machine change;
- **minor** — backward-compatible role capability, optional artifact field, doctrine, or validation addition;
- **patch** — clarification, defect correction, or non-semantic builder/documentation fix.

A version bump is not acceptance evidence. Generated skill manifests and handoff artifacts must bind the actual protocol version used.

## Protocol v3 role boundary

Protocol v3 replaces the v2 two-role model with four authority roles:

```text
software-design
software-implementation
software-qualification
software-verification
```

The split is an authority boundary, not a statement that four different products or humans must be used.

## v2 artifact compatibility

Protocol v2 used `software-design-review` plus `software-implementation` and an Implementation Workplan as the primary cross-role artifact.

Use the following compatibility rules:

| v2 artifact/state | v3 handling |
|---|---|
| completed/archived v2 workplan | `READ` as historical/acceptance evidence |
| implementation produced under a completed v2 workplan | `READ` during v3 verification; do not rewrite history merely to migrate |
| active v2 workplan before substantial new implementation | `MIGRATE` through `software-design` to a v3 revision/workplan before using split qualification |
| v2 workplan already substantially implemented but not qualified | design may issue a narrow v3 continuation/hardening workplan; preserve v2 lineage |
| v2 workplan presented directly to `software-qualification` | `REJECT` as a qualification execution contract; implementation/design must produce a v3 Qualification Handoff |
| v2 generated skill package | legacy tool artifact; not a v3 role package |

Do not mechanically rewrite completed historical v2 artifacts. Compatibility means v3 can interpret their provenance and review their results, not that old coordination records must be mutated.

## Handoff identity

For substantial work, every downstream artifact must bind upstream identity.

At minimum:

```text
workplan_id
plan_revision
workplan_sha256
protocol_version
source_commit
```

A Qualification Report also binds the exact Qualification Handoff digest it consumed. A Verification Report binds the exact candidate source and the workplan/qualification evidence it reviewed.

Do not place a self-referential SHA-256 inside an artifact. The consumer/evidence record stores the digest of the artifact it consumed.

## Source-bound evidence invalidation

Qualification evidence is valid only for the exact source revision and relevant inputs/environment declared by the governing handoff/report.

If product source changes after qualification:

1. the old report remains valid historical evidence for its old source;
2. verification must not apply it automatically to the new source;
3. implementation/design determines the affected qualification dependency set;
4. rerun all mandatory checks whose evidence could be changed by the source delta.

A source change does not require blindly rerunning unrelated expensive checks when the evidence dependency is explicit and unchanged.

## Major-version migration rule

When a major protocol revision changes role or artifact semantics:

- preserve old completed evidence;
- document `READ | MIGRATE | REJECT` behavior for active artifacts;
- update canonical templates/build metadata;
- rebuild all generated role packages;
- add/refresh protocol-level regression checks;
- dogfood the new lifecycle on at least one representative nontrivial workflow before declaring the major version frozen.
