# Protocol v3 Freeze and Dogfood Checklist

Protocol v3 should be frozen only after the four-role architecture and materiality-first workflow prove useful on real work.

## Static/build checks

- `PROTOCOL_VERSION` is 3.0.0.
- Exactly four canonical role skills exist.
- Role frontmatter names match package names.
- Referenced resources are packaged.
- Canonical semantic/lifecycle checks pass.
- Generated skill ZIPs rebuild deterministically from canonical source and `dist/` parity passes.

## Material safety cases

Exercise at minimum:

1. mandatory unexecuted check cannot PASS;
2. product/source semantic change invalidates affected evidence;
3. material dataset/config/backend change invalidates affected evidence;
4. administrative report typo does not invalidate otherwise valid evidence;
5. cwd/path/log/scratch harness correction may continue when material intent is unchanged;
6. qualification cannot silently change product/scientific semantics or thresholds to obtain PASS;
7. candidate-caused regression blocks;
8. clearly pre-existing unrelated broad-suite failure does not automatically fail a candidate absent globally-green policy;
9. required environment/input unavailable becomes `BLOCKED`;
10. generated canonical-source/distribution drift is detected.

## MVSEL2 dogfood

Use the current mdstats MVSEL2 workflow as the representative cross-environment dogfood.

Success means the workflow reaches substantive correctness/recovery/distribution/performance results without restarting qualification solely for metadata, report-format, cwd/path, or other harmless harness errors.

Real product failures still return to implementation/design. Missing required workstation/production capabilities still block honestly.

## Freeze decision

Freeze v3 only when:

- four-role authority remains clear;
- material validation remains rigorous;
- administrative mistakes cannot dominate qualification;
- generated distributions match canonical source;
- MVSEL2 dogfood demonstrates the simplified workflow in practice;
- final verification finds no unresolved acceptance-critical issue.
