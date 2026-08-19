# Release and Distribution Qualification

Source-tree correctness is not distribution correctness. Use these checks when a task actually ships or changes a package, build system, entry point, generated distribution artifact, or release process.

## Candidate boundary

Build the intended candidate source. In Git projects, the commit is normally sufficient source identity. Use additional artifact hashes when exact built bytes matter.

Qualification should not modify product source while claiming to test that candidate, but it may create build/install/evidence scratch freely in appropriate locations.

## Build and inspect

As applicable:

- build the supported artifact types;
- inspect expected modules/resources/entry points/package data;
- exclude secrets, caches, checkpoints, accidental datasets, local paths, and developer scratch;
- verify permissions/archive safety where relevant;
- verify package/version metadata when version correctness is part of the release.

## Isolated install

Install the produced artifact into a clean/isolated target and exercise it outside the source checkout.

Check the user-facing import/entry points/resources that matter. A source-tree test is not evidence for installed-artifact behavior.

## Dependencies/platforms

Qualify supported dependency/platform/backend combinations proportionally to release scope. Missing required platforms/backends are `BLOCKED` or not part of current acceptance; do not infer PASS.

## Documentation and version closeout

For a release, ensure shipped specifications/user docs match shipped behavior, required history/release notes/version metadata are correct, and required generated documentation/assets are present.

PDFs or provenance manifests are checked only when the project actually ships/requires them.

## Reproducibility

Record enough to reproduce or diagnose the release: source commit/archive, material build configuration, material build/runtime versions, artifact identity when exact bytes matter, and executed release checks.

Do not require workplan/handoff/report hash chains merely for completeness.

## Hard rules

- Do not call an installable artifact qualified solely because source-tree tests passed.
- Do not publish artifacts with uninspected accidental secrets/data/scratch.
- Do not hide source-checkout imports during installed-package testing.
- Treat wrong package/version metadata as blocking when it is part of the release contract, not when it is merely an unrelated administrative assertion.
