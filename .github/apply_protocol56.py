#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8")


def replace_once(path: str, old: str, new: str) -> None:
    text = read(path)
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{path}: expected exactly one anchor, found {count}: {old[:100]!r}")
    write(path, text.replace(old, new, 1))


# G1: normative proxy-proof testing contract.
testing_path = "source/shared/references/testing-and-validation.md"
testing_anchor = (
    "For removal, uniqueness, ownership, or no-legacy-path claims, use structural/source inspection or negative/absence assertions when runtime tests cannot establish the claim directly.\n\n"
    "## Optimize test cost, not coverage"
)
testing_replacement = """For removal, uniqueness, ownership, or no-legacy-path claims, use structural/source inspection or negative/absence assertions when runtime tests cannot establish the claim directly.

## Proxy-proof acceptance and test-double boundaries

For a material integration or acceptance claim, identify the **semantic owner under acceptance**: the production component, state machine, consumer, validator, persistence mechanism, compatibility/migration path, authorization layer, orchestrator, or decision-maker whose real behavior materially constitutes the claim.

An **allowed test-double boundary** lies below or outside that semantic owner. A dependency there may be replaced to bound cost, hardware, external services, data volume, or nondeterminism while the owner's real decision/control/state-transition path still executes. **Proxy-proof acceptance** means that a material defect in the required semantic owner would cause the evidence for that owner claim to fail.

An integration or acceptance test does not establish a production-owner claim if it mocks, stubs, monkeypatches, precomputes, substantially reimplements, or bypasses the owner whose behavior is under acceptance. In particular, evidence is insufficient for the corresponding owner claim when it:

- patches the owner to return the desired result;
- directly invokes a downstream helper when production caller/orchestrator/restart/reconciliation/authorization detection is part of the claim;
- seeds post-decision or post-transition state and skips the required production transition;
- replaces durable/project persistence with a custom or in-memory substitute when persistence, restart, or recovery semantics are the claim;
- reimplements production compatibility, migration, identity, scheduling, authorization, or orchestration logic in the harness;
- proves only a helper-produced plan/result when assembled real-consumer behavior is the claim.

This is **not a global ban on mocks or fakes**. Bounded deterministic fixtures remain preferred. Expensive ML/scientific training or prediction, accelerator execution, reduced scientific data, external services, network calls, and other costly dependencies may be faked or reduced when they lie below/outside the required real boundary. The generic requirement is boundary fidelity, not production-scale execution.

Before relying on material acceptance evidence, ask the counterfactual: **could this evidence remain green while the required semantic owner is materially broken?** If yes, that evidence cannot close the owner claim. A direct helper call cannot prove that its production caller detects the condition and invokes it correctly.

When a workplan explicitly requires a real owner/path, inability to exercise that boundary is an unavailable/blocking acceptance check or an evidence-backed design-reopen condition; do not silently downgrade it to a proxy pass. When the task names forbidden semantic-owner substitutions and a robust inexpensive structural/negative check can prevent recurrence, add that guardrail. Do not require universal AST scanning, mutation testing, one test per function, a global monkeypatch ban, or a new anti-mocking framework merely for protocol compliance.

## Optimize test cost, not coverage"""
replace_once(testing_path, testing_anchor, testing_replacement)

# Strengthen the existing direct-testing rule without duplicating the normative section.
replace_once(
    testing_path,
    "Test through the actual implementation/product path whenever practical. A harness must not substantially reimplement the algorithm, state reconstruction, orchestration, or compatibility logic it is intended to test.\n\nSynthetic fixtures are useful for bounded execution; they do not replace real integration boundaries when those boundaries are part of the functional claim.",
    "Test through the actual implementation/product path whenever practical. A harness must not substantially reimplement the algorithm, state reconstruction, orchestration, compatibility logic, or other semantic owner it is intended to test.\n\nSynthetic fixtures are useful for bounded execution; they do not replace real integration boundaries when those boundaries are part of the functional claim. Fakes below or outside the accepted semantic-owner boundary remain valid bounded-test tools.",
)

# G1: implementation intake and closure enforcement.
implementation_path = "source/roles/software-implementation/SKILL.md"
implementation_anchor = (
    "The affected surface is broader than the diff when behavior propagates: include directly changed/new code plus callers/consumers, shared utilities, public interfaces, configuration, persistence/caches/checkpoints, state transitions, orchestration/concurrency paths, packaging/entry points, documentation/contracts, and plausible transitive behavioral dependencies.\n\n"
    "## Governing workplan authority and adaptive realization"
)
implementation_section = """The affected surface is broader than the diff when behavior propagates: include directly changed/new code plus callers/consumers, shared utilities, public interfaces, configuration, persistence/caches/checkpoints, state transitions, orchestration/concurrency paths, packaging/entry points, documentation/contracts, and plausible transitive behavioral dependencies.

## Protect the semantic owner under acceptance

For every material integration/acceptance claim whose correctness depends on a real production owner or consumer boundary, identify the **semantic owner under acceptance** and the permitted test-double boundary before treating evidence as acceptance. Read `references/testing-and-validation.md` for the normative boundary rules.

Before relying on that evidence, determine:

1. which production owner/path materially constitutes the claim;
2. which functions/components on that path are mocked, stubbed, bypassed, precomputed, or otherwise replaced;
3. whether every replacement lies below or outside the required real boundary; and
4. whether the evidence could remain green if the required semantic owner were materially broken.

If item 4 is true, that evidence cannot close the obligation. Calling a downstream helper directly does not establish that its production caller, authorization layer, restart reconciler, persistence owner, state machine, or orchestrator detects the condition and invokes it correctly. Likewise, fake persistence cannot establish durable restart/recovery semantics, and helper-only output cannot establish assembled-consumer behavior when those are the claims.

Test doubles remain valid below/outside the owner boundary: expensive external computation, ML/scientific training or prediction, accelerators, external services, and bounded synthetic data may be faked where the real repository-owned decision/control/state transition still executes.

When an accepted workplan explicitly freezes a required real owner/path or forbidden substitution, that acceptance boundary is not a suggested fixture mechanic and must not be weakened as local reconciliation. If the required boundary cannot be exercised, report the check as unavailable/blocking or reopen the affected design on evidence rather than silently accepting a proxy.

## Governing workplan authority and adaptive realization"""
replace_once(implementation_path, implementation_anchor, implementation_section)

replace_once(
    implementation_path,
    "Before dependent work proceeds, establish that every accepted obligation assigned to the stage is implemented or legitimately reconciled; its protected concerns and frozen decisions remain satisfied; required consequences were not mistaken for optional advice; suggested realizations were not unnecessarily frozen when an equivalent realization is used; newly discovered necessary consequences and affected surfaces are accounted for; and no unintended alternate authority, stale superseded product path, unjustified fallback/compatibility path, or material product-complexity regression was introduced.",
    "Before dependent work proceeds, establish that every accepted obligation assigned to the stage is implemented or legitimately reconciled; its protected concerns and frozen decisions remain satisfied; required consequences were not mistaken for optional advice; suggested realizations were not unnecessarily frozen when an equivalent realization is used; newly discovered necessary consequences and affected surfaces are accounted for; no unintended alternate authority, stale superseded product path, unjustified fallback/compatibility path, or material product-complexity regression was introduced; and material acceptance evidence does not replace or bypass the semantic owner whose behavior constitutes the claim.",
)

# G2: Design handoff and independent-review challenge.
design_path = "source/roles/software-design/SKILL.md"
design_anchor = (
    "No material requirement or known design consequence may disappear in that translation. This is a reasoning requirement, not a mandatory persistent traceability artifact.\n\n"
    "## Accepted-workplan authority"
)
design_section = """No material requirement or known design consequence may disappear in that translation. This is a reasoning requirement, not a mandatory persistent traceability artifact.

### Acceptance-boundary fidelity when material

When acceptance materially depends on a real orchestration, persistence/restart/recovery, authorization, compatibility/migration, scientific/configuration identity, policy/selection, state transition, or assembled-consumer boundary, preserve enough task-specific information for implementation to recover, as applicable:

- **acceptance claim** — the material behavior/result being established;
- **required real owner/path** — the production owner(s) or consumer boundary that must actually execute;
- **allowed test doubles** — expensive/external dependencies that may be replaced below/outside that boundary;
- **forbidden substitutions** — owner/path that must not be mocked, bypassed, substantially reimplemented, or precomputed;
- **observable acceptance evidence** — state, output, transition, or consumer result that proves the claim.

These semantics extend the existing implementation obligation; they do not require a mandatory matrix, identifier scheme, or ceremony for ordinary unit tests. Freeze a real-owner/test-double boundary only when it is material to the claim, then make that boundary unambiguous enough that implementation does not need to reconstruct it.

## Accepted-workplan authority"""
replace_once(design_path, design_anchor, design_section)

review_anchor = (
    "2. **Independent engineering challenge** — inspect beyond the plan for hidden functionality/correctness/scientific, algorithm/scaling, resource/hardware/performance, ownership/complexity, failure/recovery/security, affected-surface, testing, qualification-boundary, and design-premise risks.\n\n"
    "A material blocking finding should be actionable enough for lossless rework:"
)
review_replacement = """2. **Independent engineering challenge** — inspect beyond the plan for hidden functionality/correctness/scientific, algorithm/scaling, resource/hardware/performance, ownership/complexity, failure/recovery/security, affected-surface, testing, qualification-boundary, and design-premise risks.

For a material production-owner acceptance claim, challenge proxy evidence explicitly: could the evidence remain green while the claimed semantic owner is materially broken? If yes, the claim is not established. If the accepted workplan already required that owner/path to execute for real, classify the proxy as implementation nonconformance. If a materially necessary real boundary was absent or misstated in the workplan, classify that omission as a workplan/design deficiency before reimplementation.

A material blocking finding should be actionable enough for lossless rework:"""
replace_once(design_path, review_anchor, review_replacement)

# G2: shared workflow and workplan template carry the same boundary semantics.
workflow_path = "source/shared/references/workflow-and-workplans.md"
workflow_anchor = (
    "The format is flexible; IDs/tables/matrices and persistent traceability artifacts are not required. Do not repeat generic protocol prose merely for completeness, but do not omit a known material consequence merely to compress the plan. Do not make administrative provenance, evidence filenames, report schemas, or optional telemetry acceptance requirements unless the project independently needs them.\n\n"
    "Before accepting a substantial plan, Design performs handoff closure:"
)
workflow_replacement = """The format is flexible; IDs/tables/matrices and persistent traceability artifacts are not required. Do not repeat generic protocol prose merely for completeness, but do not omit a known material consequence merely to compress the plan. Do not make administrative provenance, evidence filenames, report schemas, or optional telemetry acceptance requirements unless the project independently needs them.

When a material acceptance claim depends on a real production owner/consumer boundary, preserve the claim, required real owner/path, allowed test doubles, forbidden substitutions, and observable evidence to the degree needed to prevent proxy acceptance. This is task-specific contract content, not a mandatory matrix for ordinary unit tests. An explicitly frozen real-owner boundary is an acceptance decision and cannot be silently weakened as implementation-local reconciliation.

Before accepting a substantial plan, Design performs handoff closure:"""
replace_once(workflow_path, workflow_anchor, workflow_replacement)

replace_once(
    workflow_path,
    "1. **semantic/conformance closure** confirms assigned obligations are implemented or legitimately reconciled, protected concerns/frozen decisions remain satisfied, newly discovered consequences are accounted for, and no unintended authority/obsolete path/material complexity regression was introduced; and",
    "1. **semantic/conformance closure** confirms assigned obligations are implemented or legitimately reconciled, protected concerns/frozen decisions remain satisfied, newly discovered consequences are accounted for, no unintended authority/obsolete path/material complexity regression was introduced, and material acceptance evidence has not replaced or bypassed the semantic owner whose behavior constitutes the claim; and",
)

template_path = "source/shared/templates/implementation_workplan_template.md"
replace_once(
    template_path,
    "- **Acceptance evidence:** focused/regression/integration, numerical/resource/compatibility threshold, structural/absence check, or other proof.\n- **Stage/dependency:** when ordering materially reduces risk or rework.",
    "- **Acceptance evidence:** focused/regression/integration, numerical/resource/compatibility threshold, structural/absence check, or other proof.\n- **Acceptance boundary, when material:** acceptance claim; required real owner/path; allowed test doubles below/outside that owner; forbidden substitutions; and observable evidence. Do not require this ceremony for ordinary unit tests where no material real-owner boundary is at risk.\n- **Stage/dependency:** when ordering materially reduces risk or rework.",
)
replace_once(
    template_path,
    "<Record only task-specific acceptance mappings or thresholds not already clear in the implementation obligations, including real integration boundaries, repository-required checks, structural/absence claims, and material benchmark/backend requirements. Green runtime tests alone do not prove removal/uniqueness claims that require source/structural evidence.>",
    "<Record only task-specific acceptance mappings or thresholds not already clear in the implementation obligations, including material real-owner/test-double boundaries, repository-required checks, structural/absence claims, and material benchmark/backend requirements. A material owner claim must not be accepted through a mock/bypass that could remain green while that owner is broken. Green runtime tests alone do not prove removal/uniqueness claims that require source/structural evidence.>",
)

# G3: protocol identity, versioning, and concise documentation.
write("source/PROTOCOL_VERSION", "5.6.0\n")

versioning_path = "source/shared/references/protocol-versioning-and-compatibility.md"
versioning_anchor = "The two-role lifecycle remains unchanged."
versioning_insert = """Protocol 5.6 is a backward-compatible **proxy-proof acceptance and test-double-boundary strengthening**. It preserves the Protocol 5 doctrine and all Protocol 5.3/5.4/5.5 guarantees while adding explicit semantic-owner-under-acceptance, allowed test-double boundary, proxy-proof counterfactual, real-owner handoff, and independent-review challenge rules. Material acceptance evidence may still use bounded fakes below/outside the required real owner; it may not replace or bypass that owner and then claim the owner is accepted.

The two-role lifecycle remains unchanged."""
replace_once(versioning_path, versioning_anchor, versioning_insert)
replace_once(
    versioning_path,
    "Completed work under earlier protocol versions remains valid historical work under the version that governed it. Active older workplans do not automatically adopt Protocol 5.5. They may continue under their declared version or explicitly adopt 5.5 after reconciling its implementation-fidelity obligations. A protocol-version change alone does not require repeating still-valid evidence unless a newly adopted requirement or affected dimension invalidates the claim.",
    "Completed work under earlier protocol versions remains valid historical work under the version that governed it. Active older workplans do not automatically adopt Protocol 5.6 or any other later protocol release. They may continue under their declared version or explicitly adopt a newer backward-compatible version after reconciling its changed obligations. A protocol-version change alone does not require repeating still-valid evidence unless a newly adopted requirement or affected dimension invalidates the claim.",
)

source_readme_path = "source/README.md"
replace_once(source_readme_path, "# Software Development Protocol 5.5", "# Software Development Protocol 5.6")
replace_once(source_readme_path, "This directory is the canonical Protocol 5.5 source.", "This directory is the canonical Protocol 5.6 source.")
replace_once(
    source_readme_path,
    "Protocol 5.5 does not change this doctrine. It strengthens the design -> implementation -> review integration so task-specific intent survives handoff and rework without weakening adaptive implementation or independent review.",
    "Protocol 5.6 preserves this doctrine and the Protocol 5.5 implementation-fidelity strengthening. It additionally makes material integration/acceptance claims proxy-proof: the production semantic owner whose behavior constitutes the claim must execute for real, while bounded test doubles remain valid below or outside that owner boundary.",
)
replace_once(source_readme_path, "Protocol 5.5 preserves the two-role lifecycle:", "Protocol 5.6 preserves the two-role lifecycle:")
source_readme_anchor = "## Independent review and rework"
source_readme_insert = """## Proxy-proof acceptance

For material integration/acceptance claims, the real production semantic owner/consumer boundary named by the claim must execute. Mocks/fakes remain valid below or outside that boundary for expensive computation, hardware, services, or bounded data, but evidence that could stay green while the claimed owner is broken cannot close the claim. Detailed rules live in `shared/references/testing-and-validation.md` and the role entrypoints.

## Independent review and rework"""
replace_once(source_readme_path, source_readme_anchor, source_readme_insert)

root_readme_path = "README.md"
replace_once(root_readme_path, "Protocol 5.5 preserves this doctrine and the two-role lifecycle:", "Protocol 5.6 preserves this doctrine and the two-role lifecycle:")
root_anchor = "Executable changes still require focused checks, stage-local affected regression after every material behavior-changing stage, final affected-surface re-derivation/regression, integration, and repository/project-required checks. Semantic conformance never substitutes for executable testing, and green tests never prove a material omitted obligation was implemented. Production qualification remains separate from functional acceptance."
root_replacement = root_anchor + "\n\nProtocol 5.6 additionally makes material acceptance proxy-proof: the production semantic owner whose behavior constitutes the claim must execute, while bounded test doubles may replace expensive/external dependencies below or outside that real boundary. Evidence that could remain green while the claimed owner is broken cannot close the claim."
replace_once(root_readme_path, root_anchor, root_replacement)

# Compact root router, intentionally not a second protocol manual.
agents = """# Repository agent instructions

`source/` is the canonical protocol source. Do not hand-edit generated `dist/` packages.

Follow explicit user/task requirements first. When a task names or establishes a governing workplan, use that workplan under the protocol's authority rules; do not assume every file under `workplans/active/` governs every task merely because it is in that directory.

For design or independent review, read `source/roles/software-design/SKILL.md`.

For implementation, read `source/roles/software-implementation/SKILL.md`.

For regression, integration, acceptance boundaries, mocks/fakes, evidence reuse, or qualification, use `source/shared/references/testing-and-validation.md`.

For lifecycle/workplan authority use `source/shared/references/workflow-and-workplans.md`. For protocol-version inheritance use `source/shared/references/protocol-versioning-and-compatibility.md`.

When acceptance requires a real production semantic owner or consumer, do not replace or bypass that owner and then claim its behavior is accepted; follow the governing workplan and testing reference for the permitted test-double boundary.

Before protocol completion, run the repository acceptance workflow documented in `README.md` and `.github/workflows/protocol-check.yml`, including protocol tests, package build/validation, committed-dist parity, and `git diff --check`.
"""
write("AGENTS.md", agents)

# Existing 5.5 regression suite must follow the current protocol identity while retaining historical 5.5 contracts.
contracts_path = "tests/test_protocol_contracts.py"
replace_once(contracts_path, 'self.assertEqual("5.5.0", read("source/PROTOCOL_VERSION").strip())', 'self.assertEqual("5.6.0", read("source/PROTOCOL_VERSION").strip())')
replace_once(contracts_path, 'self.assertIn("Software Development Protocol 5.5", source_readme)', 'self.assertIn("Software Development Protocol 5.6", source_readme)')
replace_once(contracts_path, 'self.assertIn("Protocol 5.5 preserves the two-role lifecycle", source_readme)', 'self.assertIn("Protocol 5.6 preserves the two-role lifecycle", source_readme)')
replace_once(contracts_path, 'self.assertIn("Protocol 5.5", root_readme)', 'self.assertIn("Protocol 5.6", root_readme)')
replace_once(contracts_path, 'self.assertIn("Protocol 5.5", versioning)', 'self.assertIn("Protocol 5.6", versioning)')

proxy_tests = r'''from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


class ProxyProofAcceptanceContractTests(unittest.TestCase):
    def test_testing_reference_defines_real_owner_and_counterfactual(self) -> None:
        text = read("source/shared/references/testing-and-validation.md").lower()
        for phrase in (
            "semantic owner under acceptance",
            "allowed test-double boundary",
            "proxy-proof acceptance",
            "could this evidence remain green",
            "cannot close the owner claim",
        ):
            self.assertIn(phrase, text)

    def test_owner_mock_and_bypass_cannot_establish_owner_claim(self) -> None:
        text = read("source/shared/references/testing-and-validation.md").lower()
        self.assertIn("mocks, stubs, monkeypatches", text)
        self.assertIn("directly invokes a downstream helper", text)
        self.assertIn("seeds post-decision or post-transition state", text)
        self.assertIn("reimplements production compatibility", text)
        self.assertIn("helper-produced plan/result", text)

    def test_real_persistence_is_required_when_restart_is_the_claim(self) -> None:
        text = read("source/shared/references/testing-and-validation.md").lower()
        self.assertIn("replaces durable/project persistence", text)
        self.assertIn("persistence, restart, or recovery semantics are the claim", text)

    def test_bounded_fakes_below_owner_remain_valid(self) -> None:
        testing = read("source/shared/references/testing-and-validation.md").lower()
        implementation = read("source/roles/software-implementation/SKILL.md").lower()
        self.assertIn("not a global ban on mocks or fakes", testing)
        self.assertIn("bounded deterministic fixtures remain preferred", testing)
        self.assertIn("below/outside the owner boundary", implementation)
        self.assertIn("expensive external computation", implementation)
        self.assertIn("production-scale execution", testing)

    def test_unavailable_real_boundary_is_not_proxy_passed(self) -> None:
        testing = read("source/shared/references/testing-and-validation.md").lower()
        implementation = read("source/roles/software-implementation/SKILL.md").lower()
        for text in (testing, implementation):
            self.assertIn("unavailable/blocking", text)
            self.assertIn("silently", text)
            self.assertIn("proxy", text)

    def test_implementation_audits_acceptance_path_and_frozen_boundary(self) -> None:
        text = read("source/roles/software-implementation/SKILL.md").lower()
        self.assertIn("protect the semantic owner under acceptance", text)
        self.assertIn("which production owner/path", text)
        self.assertIn("which functions/components", text)
        self.assertIn("every replacement lies below or outside", text)
        self.assertIn("could remain green", text)
        self.assertIn("not a suggested fixture mechanic", text)
        self.assertIn("must not be weakened as local reconciliation", text)

    def test_design_and_workplan_preserve_material_acceptance_boundary(self) -> None:
        design = read("source/roles/software-design/SKILL.md").lower()
        workflow = read("source/shared/references/workflow-and-workplans.md").lower()
        template = read("source/shared/templates/implementation_workplan_template.md").lower()
        for text in (design, workflow, template):
            self.assertIn("required real owner/path", text)
            self.assertIn("allowed test doubles", text)
            self.assertIn("forbidden substitutions", text)
        self.assertIn("observable acceptance evidence", design)
        self.assertIn("ordinary unit tests", design)
        self.assertIn("ordinary unit tests", template)

    def test_independent_review_routes_proxy_failure_correctly(self) -> None:
        text = read("source/roles/software-design/SKILL.md").lower()
        self.assertIn("could the evidence remain green", text)
        self.assertIn("implementation nonconformance", text)
        self.assertIn("workplan/design deficiency", text)
        self.assertIn("semantic owner", text)

    def test_targeted_guardrail_does_not_create_global_anti_mock_bureaucracy(self) -> None:
        text = read("source/shared/references/testing-and-validation.md").lower()
        self.assertIn("robust inexpensive structural/negative check", text)
        self.assertIn("do not require universal ast scanning", text)
        self.assertIn("global monkeypatch ban", text)
        self.assertIn("new anti-mocking framework", text)

    def test_root_agents_is_compact_authority_router(self) -> None:
        agents = read("AGENTS.md")
        implementation = read("source/roles/software-implementation/SKILL.md")
        lower = agents.lower()
        self.assertIn("`source/` is the canonical protocol source", lower)
        self.assertIn("source/roles/software-design/skill.md", lower)
        self.assertIn("source/roles/software-implementation/skill.md", lower)
        self.assertIn("testing-and-validation.md", lower)
        self.assertIn("workflow-and-workplans.md", lower)
        self.assertIn("protocol-versioning-and-compatibility.md", lower)
        self.assertIn("do not assume every file under `workplans/active/` governs every task", lower)
        self.assertIn("semantic owner", lower)
        self.assertIn("protocol-check.yml", lower)
        self.assertLess(len(agents), len(implementation) // 3)
        self.assertNotIn("## governing doctrine", lower)
        self.assertNotIn("## product design", lower)

    def test_protocol_56_versioning_is_backward_compatible_and_version_bound(self) -> None:
        versioning = read("source/shared/references/protocol-versioning-and-compatibility.md").lower()
        self.assertEqual("5.6.0", read("source/PROTOCOL_VERSION").strip())
        self.assertIn("protocol 5.6 is a backward-compatible", versioning)
        self.assertIn("proxy-proof acceptance", versioning)
        self.assertIn("do not automatically adopt protocol 5.6", versioning)
        self.assertIn("declared version", versioning)


if __name__ == "__main__":
    unittest.main()
'''
write("tests/test_protocol_proxy_proof_acceptance.py", proxy_tests)

print("Protocol 5.6 source/test transformation applied successfully")
