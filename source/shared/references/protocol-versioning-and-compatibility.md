# Protocol Versioning, Candidate Identity, and Compatibility

## Purpose

`PROTOCOL_VERSION` identifies the Software Development Protocol contract implemented by the generated role skills and handoff artifacts. It is independent of any project/package/schema/model version governed by a repository using the protocol.

Use semantic-version intent:

- **major** — incompatible role, lifecycle, handoff-artifact, authority, identity, or state-machine change;
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

## Candidate, commit, and evidence identity

Protocol v3 separates three concepts that must not be conflated:

1. **`candidate_commit`** — Git provenance for the feature/release candidate presented to qualification.
2. **`candidate_content_identity`** — the content identity of all product-relevant tracked surfaces that qualification and verification are accepting.
3. **evidence/coordination commits** — later commits that add only declared workplan status, qualification/verification reports, benchmark logs, or other evidence-only artifacts while preserving the candidate content identity.

A Git commit SHA alone is not a sufficient qualified-content identity when repository-resident evidence is committed after execution.

### Candidate content identity policy

Each substantial workplan/handoff must either use the repository's canonical candidate-identity policy or declare the paths/classes included in and excluded from candidate identity.

Candidate identity normally **includes**:

- product/runtime source;
- tests that define/guard the candidate contract;
- current specifications and architecture that are intended to ship as candidate state;
- package/build metadata;
- tracked generated product artifacts;
- configuration/policy/schema files affecting accepted behavior;
- other tracked files whose contents can alter build/runtime/scientific/release behavior.

Candidate identity may **exclude only declared coordination/evidence surfaces**, for example:

- workplan execution-status/evidence-reference-only updates;
- qualification handoffs/reports;
- verification reports;
- benchmark/audit logs that are evidence rather than runtime inputs;
- temporary execution artifacts excluded from the product/release.

Do not exclude a path merely because it is inconvenient to requalify. If a supposedly evidence-only file can affect build, import, runtime, packaging, generated product output, policy resolution, or scientific result, it belongs in candidate identity.

The identity algorithm must be deterministic and recorded. A repository may use a canonical tree/path digest helper; otherwise the handoff records an explicit manifest of included tracked path digests and exclusion policy.

## Working-tree execution identity

Before qualification begins, `HEAD == candidate_commit` is necessary but not sufficient.

Qualification must establish as applicable:

```text
HEAD == candidate_commit
candidate_content_identity == expected identity
no undeclared staged/tracked modifications on candidate surfaces
no undeclared untracked files capable of affecting import/build/runtime
submodule/LFS identities match declared state
working directory and import/source origins are controlled when material
```

After qualification, recompute/verify the candidate content identity and candidate-surface cleanliness. Only declared evidence/build/temp output paths may differ.

An untracked helper, editable install, `PYTHONPATH`, generated module, local dependency substitution, or other shadowing input that can change executed code must be declared in environment/evidence or rejected.

## Generated output classes

Distinguish:

- **`EPHEMERAL_QUALIFICATION_OUTPUT`** — logs, build scratch, temporary wheels, reports, benchmark outputs, profiles, and other declared artifacts that are not part of the tracked candidate product identity.
- **`TRACKED_CANDIDATE_OUTPUT`** — generated PDFs/manifests, generated source/schema/assets, lock/build metadata, or other tracked files that are intended to be part of the accepted candidate.

Qualification may create/modify `EPHEMERAL_QUALIFICATION_OUTPUT` only in declared write paths.

Qualification must not create or change `TRACKED_CANDIDATE_OUTPUT`. If target-runtime/hardware execution is required to generate a tracked candidate output, qualification may produce a proposed artifact in an evidence/output area, then return it to `software-implementation`. Implementation adopts/commits the artifact, creates a new candidate identity and handoff, and affected checks rerun.

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

A major-version bootstrap may legitimately have a v2-governed workplan that builds the first v3 implementation. Once v3 artifacts are sufficiently available, remaining v3 qualification/freeze work should migrate to a v3-governed continuation workplan so the new lifecycle dogfoods itself.

## Handoff identity

For substantial work, every downstream artifact must bind upstream identity.

At minimum:

```text
workplan_id
plan_revision
workplan_sha256
protocol_version
candidate_commit
candidate_content_identity
candidate_identity_policy
```

A Qualification Report also binds the exact Qualification Handoff digest it consumed. A Verification Report binds the exact candidate content identity plus candidate/evidence commit provenance and the workplan/qualification evidence it reviewed.

Do not place a self-referential SHA-256 inside an artifact. The consumer/evidence record stores the digest of the artifact it consumed.

## Evidence dependency and invalidation

Qualification evidence may be reused only when its declared dependency/comparability identity remains compatible.

A check may declare dependencies such as:

```yaml
evidence_dependencies:
  source_paths: []
  candidate_identity_components: []
  config_identity: []
  inputs: []
  environment_dimensions: []
  upstream_checks: []
```

When candidate/product source changes after qualification:

1. the old report remains valid historical evidence for its old candidate identity;
2. verification must not apply it automatically to the new candidate;
3. implementation computes a proposed invalidation/reuse set from the declared dependencies;
4. rerun every mandatory check whose dependency set intersects the changed identity;
5. when dependency is ambiguous or not declared sufficiently, **invalidate by default**;
6. verification audits whether any reused evidence is justified.

`software-design` owns frozen comparability/dependency semantics when they are consequential to acceptance. `software-implementation` may instantiate the dependency mapping for concrete checks. `software-verification` decides whether reuse is acceptable.

An evidence-only/coordination commit that preserves `candidate_content_identity` does not by itself invalidate qualification.

## Retry identity

Each qualification check declares one retry mode:

- `NONE` — no automatic retry;
- `IDENTICAL_RETRY` — rerun with identical candidate/configuration/state policy, normally for transient nondeterministic infrastructure failure or measurement repetition;
- `CLEAN_RETRY` — recreate only explicitly declared ephemeral state, then rerun with otherwise identical candidate/configuration;
- `RESUME_RETRY` — resume from explicitly declared authoritative/checkpoint state to test resumability or continue an approved interrupted run.

A retry that changes scientific/configuration/resource policy, candidate product content, acceptance threshold, backend semantics, dataset scope, or undeclared state is **not** a retry under the same handoff. Return to implementation for a new handoff or to design for `DESIGN_REVISION_REQUIRED`.

## Major-version migration rule

When a major protocol revision changes role or artifact semantics:

- preserve old completed evidence;
- document `READ | MIGRATE | REJECT` behavior for active artifacts;
- update canonical templates/build metadata;
- rebuild all generated role packages;
- add/refresh protocol-level regression checks;
- dogfood the new lifecycle on at least one representative nontrivial workflow before declaring the major version frozen.
