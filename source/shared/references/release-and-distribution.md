# Release and Distribution

Use release checks only when a change actually affects a package, build system, entry point, generated distributable, installer, or release process.

## Build what users receive

Source-tree correctness does not prove installed-artifact correctness. When materially relevant:

- build the supported artifact;
- inspect expected modules/resources/entry points;
- exclude secrets, caches, local paths, accidental datasets, and developer scratch;
- install into an isolated target;
- exercise the user-facing import/entry points outside the source checkout;
- verify version metadata when version correctness is part of the deliverable.

Do not create a separate qualification lifecycle around these checks.

## Scope proportionally

Test supported platform/backend combinations according to the actual release scope. Do not infer unavailable results.

Use exact artifact hashes only when exact built bytes matter. Otherwise source commit plus material build conditions is usually sufficient.

## Generated outputs

Prefer reproducible generation over version-controlling generated artifacts. Track generated output only when repository/release policy makes it an authoritative shipped source artifact.

## Completion

Record enough to reproduce or diagnose a material release issue, but do not require hash chains, report manifests, or extra evidence documents merely for completeness.
