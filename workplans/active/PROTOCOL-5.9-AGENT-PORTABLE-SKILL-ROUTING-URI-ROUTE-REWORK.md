---
kind: implementation-workplan-amendment
workplan_id: PROTOCOL-5.9-AGENT-PORTABLE-SKILL-ROUTING-URI-ROUTE-REWORK
amends_workplan_id: PROTOCOL-5.9-AGENT-PORTABLE-SKILL-ROUTING
protocol_version: 5.8.0
target_protocol_version: 5.9.0
status: active
created_date: 2026-08-29
review_source: independent-software-design-review-round-2
---

# Protocol 5.9 Routing Workplan — URI/Absolute Route Rework Amendment

This amendment closes the remaining blocking implementation nonconformance found during the second independent Software Design review of the Protocol 5.9 candidate. It does not reopen the accepted routing/distribution architecture, the doctrine/content freeze, or the already completed R1-R3 rework. The governing hierarchy remains exactly:

```text
product engineering fitness > minimum justified product/system complexity > development economy
```

All Protocol 5.4-5.8 hardening remains frozen. Rework is limited to local-resource route classification in the package validator and regression evidence for that classification.

## R4 — Classify local resource routes before generic URI skipping

### Concern

`source/validate_packages.py` currently checks `URI_SCHEME_RE` before determining whether a Markdown target is attempting to address the packaged `references` or `templates` namespace. Windows absolute paths such as `C:\references\outside.md` and `C:/references/outside.md` therefore match the drive-letter prefix as a URI scheme and can be silently ignored. `file:` resource URIs are similarly skipped. This violates R2's requirement that absolute/backslash/local-resource escape forms be rejected rather than omitted from validation.

### Required end state

`validate_resource_routes()` must first determine whether a decoded Markdown link target attempts to address the local packaged `references` or `templates` namespace, then classify that target correctly:

- Windows drive-absolute forms using either slash direction are local/absolute resource routes and must fail validation;
- `file:` URIs that address the packaged resource namespace must fail validation;
- ordinary external URI schemes such as `https:` remain external links and must not be misclassified as local package routes merely because their remote path contains a `references` or `templates` segment;
- encoded, traversal, backslash-relative, deeper, query/fragment-decorated, missing, and packaged-but-unlinked cases retain the existing R2 behavior;
- the strict supported local form remains exactly one-level `references/<safe-name>.md` or `templates/<safe-name>.md`.

The fix belongs in the validator's owning route-classification mechanism. Do not add a second validator, wrapper, or CI-only exception.

### Acceptance evidence

Add focused regression cases that would fail the reviewed candidate:

```text
C:\references\outside.md
C:/references/outside.md
file:///tmp/references/outside.md
```

Also include a positive control showing that a normal external HTTPS link whose remote path contains `/references/` is ignored as external rather than falsely rejected as a local bundle route.

## Required final acceptance

After R4 is implemented:

1. run the focused URI/absolute-route regression cases against the real `validate_resource_routes()` implementation;
2. run the complete unit/regression suite;
3. build all canonical skill bundles;
4. independently validate all generated directory and ZIP bundles;
5. verify committed `dist` parity against the fresh build;
6. run `git diff --check`;
7. independently re-check that no lifecycle/specialist doctrine or Protocol 5.4-5.8 semantic safeguard changed;
8. keep live external harness qualification explicitly unqualified unless actually executed.

The expected outcome remains the same Protocol 5.9 design and semantics, with the final known false-green in static local-resource routing validation removed.
