# Release and Distribution Qualification

Source-tree correctness is not distribution correctness. A package can pass repository tests yet ship missing modules, stale generated documents, wrong version metadata, undeclared dependencies, or artifacts that work only because the source checkout is on `sys.path`.

Use this protocol for releases, package-format changes, build-system changes, entry-point changes, generated-artifact packaging, or any gate intended to produce a user-installable artifact.

## Release inputs and identity

Identify before building:

- authoritative package/version source;
- source revision/commit or source-archive identity;
- build configuration and supported artifact types;
- dependency/build-backend versions where they materially affect output;
- generated documentation/assets that are required in the distribution;
- expected CLI entry points and package data;
- release exclusions: caches, local datasets, credentials, temporary files, developer-only evidence, private paths.

A release artifact should have a stable digest recorded in release/evidence metadata after it is produced and accepted.

## Build from a clean source state

Where practical, qualify release artifacts from a clean checkout/worktree/source archive rather than a developer tree containing untracked helpers or locally generated dependencies.

- Regenerate required generated artifacts from authoritative sources before packaging.
- Fail if required generated documentation is stale according to its provenance check.
- Avoid release behavior that depends on files outside the declared build context.
- Record deliberate local patches or unreleased dependency substitutions if a clean official environment cannot be reproduced.

Do not silently clean or discard unrelated user work merely to obtain a clean tree; use a separate worktree/copy/build context when needed.

## Inspect the produced artifact

After building, inspect the distribution contents rather than assuming the manifest is correct.

Verify as applicable:

- expected modules/packages/tools/examples/templates/specifications/manuals/PDFs are present;
- package metadata/version is correct;
- CLI entry points are declared;
- required non-code resources are included;
- generated files correspond to authoritative sources;
- no caches, checkpoints, secrets, credentials, local absolute paths, large accidental datasets, build scratch, or unrelated developer artifacts are included;
- file permissions/executable bits are appropriate;
- archive paths are normalized and safe.

For Python projects publishing both wheel and source distribution, inspect and test both because inclusion/build behavior can differ.

## Clean-install verification

Install the produced artifact into a fresh/isolated environment and test it outside the source tree.

At minimum, as applicable:

1. install using the supported user-facing mechanism;
2. import the installed package from a directory unrelated to the checkout;
3. verify reported package version;
4. invoke expected CLI entry points/help/version;
5. execute a minimal representative workflow using only packaged resources and declared dependencies;
6. verify optional-dependency failure messages/fallbacks when relevant;
7. confirm documentation/assets expected by runtime consumers are discoverable after installation.

A successful source-tree test is not evidence for any of these installed-artifact behaviors.

## Dependency and platform qualification

Test the supported environment matrix proportionally to release scope.

- Use the project's minimum/maximum or pinned dependency policy rather than only the developer environment.
- Distinguish unavailable platform/backend checks as `BLOCKED` or `NOT RUN` rather than passing them by inference.
- Record accelerator/native-library/ABI qualification separately from pure-Python package installation.
- Avoid undeclared reliance on shell tools, environment variables, working-directory layout, or user-site packages.

## Documentation/version closeout

Before accepting a release:

- specifications match the shipped implementation;
- current architecture documentation reflects the accepted shipped architecture where it changed;
- history/changelog/release notes record material completed changes and version transition;
- package version and independent schema/protocol/model versions are not conflated;
- authoritative Markdown and generated PDFs pass content-provenance checks;
- release artifacts contain the documentation/assets required by repository policy.

Read `documentation-and-evidence.md` for document roles and version history.

## Reproducibility and retention

Perfect byte-for-byte reproducible builds may not be practical for every project, but avoid gratuitous nondeterminism.

Record enough build evidence to reproduce or diagnose the artifact:

- source revision;
- governing workplan ID/revision/SHA-256 when implementation was workplan-driven;
- resolved build configuration;
- build tool/runtime versions where material;
- artifact filename/type/version;
- artifact SHA-256;
- executed qualification results.

Retain accepted release artifacts according to project policy; do not confuse transient build directories with release records.

## Release failure modes to test

Representative qualification should catch:

- missing package/module/data file;
- stale or omitted generated PDF/manual;
- wrong version metadata;
- broken entry point;
- implicit source-tree import;
- undeclared runtime dependency;
- missing optional-dependency diagnostic;
- accidental inclusion of cache/checkpoint/data/secret files;
- sdist that cannot build a wheel in isolation;
- installed workflow that assumes repository-relative paths.

## Hard rules

- Do not call a package/release qualified because tests passed only in the source checkout.
- Do not publish an artifact whose contents have not been inspected or at least mechanically verified against repository policy.
- Do not infer wheel behavior from sdist behavior or vice versa when both are distributed.
- Do not ship stale generated documentation, local caches/checkpoints, credentials, or accidental large datasets.
- Do not overwrite/replace an accepted release artifact without changing identity or recording the replacement according to project policy.
