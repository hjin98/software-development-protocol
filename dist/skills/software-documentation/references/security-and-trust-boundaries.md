# Security and Trust Boundaries

Treat every boundary where data, code, credentials, files, processes, networks, plugins, models, or generated artifacts cross ownership as a security boundary. Scientific and internal tools are not exempt: large trusted datasets may still be malformed, while ostensibly "data-only" formats such as Python pickles or model checkpoints can execute code when deserialized.

## Establish the trust model before implementation

For nontrivial input, persistence, plugin, subprocess, network, archive, model-loading, or document-rendering work, identify:

- **asset** - what must be protected: source data, repository state, credentials, compute quota, model weights, generated results, filesystem, remote services;
- **actor/source** - user, repository, dependency, external service, downloaded artifact, collaborator, generated file, cache/checkpoint, plugin;
- **trust level** - trusted, authenticated-but-untrusted-content, untrusted, or unknown;
- **boundary** - parser, archive extraction, deserializer, subprocess, network client, plugin loader, renderer, filesystem write, cache restore, model loader;
- **capability granted** - read files, write files, execute code, access network, allocate resources, use credentials, mutate repository/remote state;
- **failure impact** - code execution, data corruption/loss, secret exposure, path escape, denial of service, scientific-result corruption, supply-chain compromise.

Use least privilege: a component should receive only the files, credentials, network access, write scope, and execution capability it actually needs.

## Input validation is not only type validation

At every user/external boundary, validate both syntax and resource/security properties.

- Bound input byte size, item count, nesting depth, dimensions, decompressed size, and other amplification factors when hostile or malformed input could exhaust CPU/RAM/VRAM/disk.
- Reject impossible or unsupported shapes/ranges before expensive allocation.
- Treat JSON/XML/YAML/text as capable of denial-of-service even when they cannot directly execute code.
- Do not trust filename extensions alone when file content can materially change parser behavior.
- Preserve provenance so a suspicious or invalid result can be traced back to the actual source artifact.

Scientific correctness checks and security checks are complementary. A file can be scientifically plausible while still violating storage, path, parser, or execution constraints.

## Unsafe deserialization and executable data

Do not deserialize untrusted data using mechanisms that can instantiate arbitrary objects or execute code.

Examples requiring explicit trust include Python `pickle`/`shelve`, many Python object checkpoints, and model/package formats whose loader can invoke Python code. Treat an artifact as executable unless the format and loader are documented as data-only for the exact mode being used.

Rules:

- Never unpickle data from an untrusted or unauthenticated source.
- Prefer data-only formats with explicit schemas for interchange.
- When a framework provides a restricted/data-only load mode, prefer it and test the compatibility path.
- Bind trusted checkpoints/caches to provenance and integrity metadata; trust and validity are separate questions.
- Do not weaken loader safety merely because a legacy artifact fails to load. Migrate or re-export trusted artifacts instead.

## Archives and compressed inputs

Archive extraction is a filesystem write operation, not a benign read.

Before extracting untrusted or externally supplied archives:

- reject absolute paths and path traversal outside the designated extraction root;
- reject or constrain symlinks, hard links, device files, FIFOs, and other special entries unless explicitly required;
- bound member count, total expanded bytes, per-member size, compression ratio, and nesting when archive bombs are plausible;
- extract into a run-owned temporary directory, validate contents, then move only approved files into their destination;
- do not overwrite repository files or authoritative user data implicitly;
- use standard-library/library extraction safety filters when available rather than duplicating incomplete path logic.

Do not recursively unpack nested archives without an explicit depth/size policy.

## Filesystem and path boundaries

- Resolve/validate output roots before writes when user-controlled paths are involved.
- Prevent `..`, absolute-path, symlink, mount, or case-normalization tricks from escaping a designated write root.
- Do not follow symlinked directory trees during destructive cleanup or broad repository scans unless explicitly intended.
- Use run-owned temporary directories and restrictive permissions for sensitive intermediates.
- Avoid predictable temporary filenames where another process/user could replace them.
- Publish important artifacts transactionally; never let a partial file look complete.
- Treat external/read-only datasets as immutable even if the operating system technically permits writes.

Before deletion, cleanup, cache eviction, or compaction, prove ownership of the target rather than relying on a broad path pattern.

## Subprocess and shell execution

Prefer argument-vector subprocess APIs over shell command construction.

- Do not concatenate untrusted strings into shell commands.
- Use `shell=False` by default.
- If a shell is genuinely required, strictly define and escape the accepted input domain and document why direct argv execution is insufficient.
- Set the working directory and environment intentionally; do not leak all parent environment variables/credentials to child processes without need.
- Bound runtime/output size for tools that can hang or flood stdout/stderr.
- Check return codes and validate produced artifacts; successful process exit is not sufficient evidence of semantic success.
- Never execute files merely because they were present in an uploaded archive, generated directory, or dependency cache.

Package-manager, compiler, build-hook, and test execution can run arbitrary code and should be treated as privileged execution of the selected dependency/source tree.

## Network, downloads, and remote services

When code fetches models, datasets, packages, schemas, or other external artifacts:

- use authenticated transport where available;
- prefer official/primary distribution sources;
- verify expected digest/signature when the project provides one or reproducibility/security depends on exact identity;
- record source URL/version/digest in provenance when material;
- bound download size and timeout/retry behavior;
- do not automatically follow a downloaded file into an executable/deserialization path without a trust decision;
- avoid sending local files, private data, tokens, or full environment/configuration to remote services unless explicitly required and authorized.

Network availability must not silently change scientific semantics. Cache remote inputs only with explicit identity and invalidation rules.

## Credentials and sensitive data

- Never hard-code secrets, tokens, passwords, private keys, or credentials in source, fixtures, examples, docs, manifests, logs, command histories, benchmark output, or generated packages.
- Prefer the repository/platform's established secret provider or environment injection mechanism.
- Pass only the credential required for the current action and scope it as narrowly as possible.
- Redact secrets and sensitive paths/metadata from diagnostics before persistence or user-visible artifacts.
- Review staged diffs and generated archives for accidental credential/private-data inclusion.
- Do not commit `.env`, credential stores, cloud config, SSH material, browser state, or machine-specific authentication caches unless the repository explicitly defines a safe non-secret fixture.

If a secret may have been exposed, do not merely delete it from the latest file: report the exposure so rotation/history remediation can be handled appropriately.

## Dependencies and supply-chain boundaries

A dependency is executable code with the privileges of the process that imports/builds it.

- Reuse established dependencies before adding new ones.
- Prefer maintained packages from authoritative sources with clear licensing and release provenance.
- Pin/lock versions where reproducibility or compatibility requires it; update deliberately rather than through accidental solver drift.
- Inspect dependency changes separately from source changes when they can materially alter behavior or trust.
- Avoid dependency installation from arbitrary Git branches, URLs, local archives, or unofficial mirrors unless explicitly justified and provenance is recorded.
- Keep optional accelerators/plugins optional when the core package can remain functional without granting them universal import/build authority.
- Treat build backends, editable installs, native extensions, post-install hooks, and compiler toolchains as code-execution surfaces.

Security updates may justify dependency changes even when performance/functionality do not, but they still require compatibility validation.

## Plugins, callbacks, filters, and extension points

Plugins and arbitrary callbacks run inside the host process unless sandboxing is explicitly provided.

- Do not describe an in-process plugin API as a security boundary.
- Define which extension points are trusted-code-only.
- Validate declarative plugin configuration before loading implementation code.
- Keep plugin discovery deterministic and avoid executing every file found in user-controlled directories.
- Isolate third-party or untrusted extensions into a lower-privilege process/container when true trust separation is required.

The same rule applies to Pandoc filters/custom writers, notebook execution, template engines with code execution, compiler hooks, and ML framework callbacks.

## Document and PDF rendering boundary

Document rendering is an active processing step. Markdown/HTML/CSS may reference local or remote resources, and custom render filters can execute arbitrary code.

For the default Markdown-to-PDF workflow in this skill:

- render only trusted repository/user-authored Markdown with the normal local toolchain;
- do not enable arbitrary Pandoc filters, custom writers, shell escapes, or user-supplied executable render hooks by default;
- use repository-owned templates/styles rather than downloading render assets implicitly;
- treat remote images/styles and user-controlled HTML/CSS as external inputs requiring the same network/resource policies as other fetches;
- render untrusted documents only in an appropriately isolated environment with restricted filesystem/network access and resource limits;
- verify the generated PDF before publication, and never treat rendering success as proof that source content is safe.

## Resource exhaustion and denial of service

Security includes protecting compute/storage availability.

Apply the existing resource-admission rules to untrusted or unusually large inputs:

- CPU time and worker count;
- RAM and allocation shape;
- GPU/VRAM batch size;
- disk footprint and inode count;
- decompression/materialization amplification;
- network bytes/time;
- log/output size;
- parser recursion/nesting;
- subprocess runtime.

Prefer rejection with an actionable error over allowing a malformed input to consume the entire node or filesystem.

## Security-sensitive tests

When a changed boundary is security-relevant, add focused tests such as:

- `../` and absolute-path archive members;
- symlink/hard-link escape attempts;
- oversized/decompression-bomb admission without actually exhausting the machine;
- malformed deeply nested JSON/XML/config structures;
- shell metacharacters passed as ordinary argv data;
- filenames containing whitespace, newlines, Unicode, or leading dashes;
- stale/tampered cache/checkpoint digest;
- unauthorized output path;
- secret redaction in logs/errors;
- untrusted serialized object rejected before deserialization;
- renderer invocation without unapproved filters/network resources.

Test the defense mechanism, not a single malicious string.

## Security completion check

Before closing a gate that crosses a trust boundary, answer:

1. What input/code is trusted, untrusted, or unknown?
2. What filesystem/network/process/credential capabilities does it receive?
3. Can it cause code execution, path escape, data loss, secret exposure, or unbounded resource use?
4. Where is validation performed, and is it before the dangerous operation/allocation?
5. Are persistence and caches protected against stale/tampered state?
6. Are logs/evidence/packages free of secrets and unintended private data?
7. Are dependencies/plugins/renderers part of the explicit trust model?
8. What security-relevant tests were actually executed?

Do not claim a component is "secure" in absolute terms. Report the boundaries and mitigations that were reviewed and any residual/unverified risks.

## Primary references for implementation details

Use the current official documentation when implementing these controls rather than relying on this summary alone:

- Python `pickle` security warning: https://docs.python.org/3/library/pickle.html
- Python `tarfile` extraction filters and archive handling: https://docs.python.org/3/library/tarfile.html
- Python `zipfile` path-handling notes: https://docs.python.org/3/library/zipfile.html
- Pandoc PDF engines and filter/custom-writer security notes: https://pandoc.org/MANUAL.html
- Typst compiler installation and sandbox/trust model: https://typst.app/open-source/
