---
name: repository-hygiene
description: Perform conservative post-stage repository cleanup after development is formally closed. Remove proven temporary/cache/test residue, archive completed workplans, repair directory-tree drift, and retire proven disposable branches while preserving useful records, recoverable work, and protected branches.
---

# Repository Hygiene

Use this optional specialist **after a development stage is formally closed**, or when the user explicitly requests a repository-hygiene pass.

It is not a lifecycle role, approval gate, design review, or substitute for implementation. It must not interrupt active engineering merely to make the tree look tidy. Its purpose is to restore a structurally sound, comprehensible repository after substantial design/implementation/test cycles while preserving useful work and history.

> **Inspect broadly; delete only with positive proof. When classification is uncertain, retain and report.**

## Hard invariants

1. **Never delete, rename away, force-move, or otherwise remove the `main` branch.** This is absolute.
2. Preserve the repository's configured default branch even when it is not named `main`.
3. Never use cleanup as a reason to rewrite history, force-push, bypass protections, discard uncommitted work, or erase unique commits.
4. Never delete a file, directory, branch, worktree, tag, artifact, or record merely because its name looks temporary, old, generated, deprecated, or unfamiliar.
5. Preserve accepted scientific/engineering evidence, benchmark closeouts, provenance needed to interpret results, durable specifications/manuals, release records, migrations still needed by supported versions, and other useful historical records.
6. Treat pre-existing user/concurrent changes as protected. A hygiene pass does not own them.
7. Product behavior, scientific semantics, public APIs, and architecture are outside this specialist's authority. If cleanup exposes a semantic/design defect, route it to `software-design`/`software-implementation` rather than silently changing the product.
8. Follow `references/git-and-version-control.md`, project `AGENTS.md`, repository policy, generated-file policy, and more specific project instructions. This specialist does not weaken their authorization boundaries.

## Scope and timing

Run hygiene only when at least one of these is true:

- a substantial development stage/workplan has been accepted and closed;
- a release/merge candidate needs repository-state cleanup;
- accumulated temporary diagnostics, test residue, generated scratch, or directory drift has become materially confusing;
- the user explicitly requests a cleanup audit.

Do not perform repository-wide cleanup after every local change. Active workplans, active diagnostic branches, live checkpoints, running-work outputs, and temporary files still required for unresolved debugging are not cleanup candidates.

## Establish a read-only baseline first

Before changing anything, resolve and record compactly:

- repository root, default branch, current branch/HEAD, remotes, upstreams;
- staged, unstaged, untracked, ignored, conflicted, and pre-existing modified paths;
- linked worktrees, nested repositories, and submodules;
- active and archived workplan locations and any repository indexes governing them;
- repository conventions for source, tests, docs, benchmarks/evidence, build outputs, generated artifacts, scratch/cache, release artifacts, and external data;
- local and relevant remote branches, open/merged PR relationships when available, and branch tips;
- project-specific protected or long-lived branch classes.

Do not manufacture a clean baseline by stashing, resetting, cleaning, switching away from user work, or deleting anything.

## Classify before acting

Classify every cleanup candidate into one of five classes:

| Class | Meaning | Default action |
|---|---|---|
| persistent | current source/specification/docs/tests/fixtures or useful durable evidence/history | retain |
| archival | completed workplan, superseded but useful record, release/history material | move to canonical archive location |
| derived/rebuildable | generated product with a canonical source/build rule | regenerate, retain, or remove according to repository policy |
| disposable | positively identified cache, scratch, editor residue, temporary diagnostic/test output, or abandoned scaffolding with no durable value | remove when authorized and safe |
| ambiguous | ownership/value/reachability is not proven | retain and report |

The burden of proof is asymmetric: retention needs no proof; deletion does.

Useful evidence is not temporary merely because it originated from a test. Prefer compact durable summaries/benchmarks over massive raw scratch when the project has already accepted and summarized the result, but never remove the only evidence needed to reproduce or interpret a material conclusion.

## Files, caches, and test residue

Safe candidates commonly include known rebuildable caches, temporary build directories, editor/OS residue, temporary diagnostic scripts created solely for a closed investigation, abandoned scratch outputs, and generated test debris. However:

- inspect tracked versus untracked/ignored status;
- identify the owning tool and whether the artifact is reproducible;
- check references from scripts, docs, tests, manifests, CI, workplans, and package/release rules;
- distinguish fixtures and golden/reference data from transient test output;
- distinguish accepted benchmark/evidence records from raw temporary logs;
- never delete external datasets or read-only/shared inputs;
- never use broad `git clean`, wildcard deletion, or recursive deletion when a path-scoped operation suffices.

Tracked files require stronger evidence than ignored caches. If a tracked file appears obsolete but deleting it changes supported behavior, compatibility, scientific authority, or package contents, cleanup must stop at identification and route the change to the owning lifecycle role.

## Completed workplans

Move a workplan from `active` to `archive` only when the plan itself and accepted project state establish that it is complete. Verify that:

1. its terminal status is complete/accepted/done according to repository convention;
2. no unresolved gate, blocker, deferred acceptance requirement, or active implementation still depends on treating it as active;
3. any durable closeout result has been preserved in the plan, benchmark/history record, or other canonical owner;
4. references/indexes are updated if the repository maintains them.

Move rather than duplicate when active/archive are mutually exclusive lifecycle locations. Never archive a plan simply because work has paused.

## Directory-tree structural repair

Correct obvious hierarchy drift only when the canonical destination is supported by repository structure or policy. Examples include misplaced workplans, docs, fixtures, benchmarks, scripts, generated artifacts, or source modules.

Before moving a tracked path:

- establish its semantic owner and canonical directory;
- search for imports, references, links, manifests, CI paths, package-data rules, and external/user-facing paths that may depend on the old location;
- preserve history with a normal move/rename rather than copy-and-delete where practical;
- update directly affected references and run proportionate checks.

Do not reorganize directories for aesthetic symmetry. If the correct hierarchy is genuinely ambiguous or a move implies architectural/module-boundary changes, report it for design review instead.

## Branch hygiene: high-risk procedure

Branch deletion is a separate high-risk cleanup action. It must follow the Git authorization policy and is never inferred merely from the existence of a hygiene task.

### Absolute protected set

Never delete:

- `main`;
- the repository default branch;
- the currently checked-out branch;
- a branch checked out in any linked worktree;
- a branch with an open PR or active workplan unless the user explicitly resolves that conflict;
- a branch containing commits not proven reachable from a retained durable ref;
- a branch whose purpose/status is ambiguous;
- a project-declared protected, release, stable, production, or other long-lived branch without a separate explicit retention decision.

### Triple-check every candidate

For each proposed deletion, perform three independent checks:

**Check 1 — identity and lifecycle**
- exact branch name and tip SHA;
- purpose is positively identified as temporary/diagnostic/superseded;
- not in the protected set and not referenced by active work.

**Check 2 — reachability and integration**
- inspect comparison/merge-base/merged-PR evidence;
- prove there are no unique commits that would become unrecoverable;
- confirm the intended durable replacement/integration branch contains the needed work.

**Check 3 — immediate pre-delete verification**
- refresh/re-read the exact branch target and tip immediately before deletion;
- re-confirm default branch, current/worktree use, open-PR state where available, and zero material unique work;
- record the tip SHA in the cleanup report before deleting so an accidental remote/UI mismatch can be diagnosed.

Delete branches **one at a time**, never through broad patterns. If exact-target destructive authorization is required by repository/tool policy and has not been granted, stop after presenting the verified candidate list for approval.

Remote and local branch deletion are separate actions and require the corresponding authorization. Deleting one never implies permission to delete the other.

## Deprecated and superseded material

Separate three cases:

- **historical but useful**: archive/retain;
- **supported compatibility/deprecation path**: retain until its support/migration obligation expires;
- **truly useless residue**: remove only after proving no active references, unique information, compatibility obligation, or recovery value remains.

Do not convert a hygiene pass into a broad dead-code refactor. Obsolete product machinery that requires semantic reasoning belongs to implementation/design; this specialist may identify it as a cleanup opportunity.

## Final structural validation

After cleanup, inspect the repository again and verify proportionally:

- only intended paths changed;
- pre-existing user/concurrent changes are preserved;
- no accidental large binaries, caches, logs, checkpoints, secrets, editor files, or machine-specific paths remain among task-owned changes;
- active/archive workplan state is coherent;
- moved files have no broken directly affected imports/links/manifests/package paths;
- generated artifacts match their canonical-source policy where applicable;
- branch list still contains `main`, the default branch, all protected/long-lived branches, and every branch carrying unique or active work;
- each deleted branch had all three recorded checks;
- repository status is actually inspected before describing it as clean.

Run the smallest relevant tests/build/index checks required by the paths moved or regenerated. A hygiene pass should not rerun an expensive scientific or production qualification unless cleanup changed an input that could plausibly invalidate it.

## Completion report

Report concisely:

- retained persistent/ambiguous material that was intentionally not deleted;
- temporary/cache/test residue removed;
- workplans archived and indexes updated;
- structural moves and directly affected references repaired;
- branches deleted, with their recorded tip SHAs and evidence that they were disposable/integrated;
- verified deletion candidates intentionally left pending authorization;
- checks actually run and any unresolved structural ambiguity.

A successful hygiene pass leaves the repository easier to navigate and safer to continue from, without losing useful work, evidence, history, or branch recoverability and without changing the accepted engineering doctrine.