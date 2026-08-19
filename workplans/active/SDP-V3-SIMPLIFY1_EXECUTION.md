# SDP-V3-SIMPLIFY1 execution status

Governing workplan: `SDP-V3-SIMPLIFY1`, revision 1.

This is an execution record only; it does not revise frozen design or acceptance semantics.

| Gate | Status | Evidence |
|---|---|---|
| S0 | PASS | Materiality-first design and A1-A10 frozen in governing workplan. |
| S1 | PASS | Lifecycle doctrine simplified; four roles retained; artifacts proportional; harness/record defects nonblocking. |
| S2 | PASS | Git commit is default candidate identity; additional hashes conditional at real content boundaries; reruns materiality-based. |
| S3 | PASS | Qualification doctrine preserves strict material tests, broad-failure attribution, and absolute-performance fallback when no trustworthy baseline exists. |
| S4 | PASS | All four role skills simplified around material authority boundaries. |
| S5 | PASS | Workplan/run-card/evidence/verification templates reduced to material fields. |
| S6 | PASS | Semantic/lifecycle checkers rewritten around real safety properties rather than mandatory metadata strings. |
| S7 | PASS | Documentation/version/provenance requirements made proportional; specification-code parity retained where contractual. |
| S8 | PASS | Canonical checkers pass; deterministic generated distributions rebuilt from canonical source and second rebuild matches exactly. |
| S9 | PREPARED | Requires mdstats workstation/production-data dogfood and final verification. |

## S8 deterministic evidence

Executed locally against the canonical reconstructed source tree:

```text
python source/check_protocol_semantics.py
PASS: Protocol v3 materiality semantic invariants

python source/check_protocol_lifecycle_cases.py
PASS: Protocol v3 materiality lifecycle cases

python -m py_compile source/build_skills.py source/check_protocol_semantics.py source/check_protocol_lifecycle_cases.py
PASS

python source/build_skills.py --output dist
python source/build_skills.py --output dist --check
PASS: dist matches canonical protocol source (3.0.0)
```

Generated artifact SHA-256 values:

- `dist/BUILD_INDEX.json`: `d60464817889402300df6d473c2e5077d845478bc924f3fc2c2cdd553ba91985`
- `dist/software-design.zip`: `3f751862106e799ceb5211d209fe96d81a05409d91badaaedd72d72fb526860a`
- `dist/software-implementation.zip`: `3a61ce42efd6e71ec8bc121e969e7cf026448288877991ec8159779874560879`
- `dist/software-qualification.zip`: `c66cfb1f07d8506182f5212d4c5094d6b98af401a809ef69da5cf88f7b45f675`
- `dist/software-verification.zip`: `8fc337f9ea0eb70e05406e5d1f2afe7ebc15776b3804191a7c8d5e9a33501904`

The hashes above protect the real canonical-source-to-generated-package content boundary. They are build evidence, not general lifecycle gating metadata.

## S9 boundary

S9 is the first remaining gate requiring capabilities outside the protocol repository: the actual mdstats workstation and production campaign data. A compact project-local run card should be used; harmless cwd/path/log/report corrections are explicitly permitted in place under the new protocol.
