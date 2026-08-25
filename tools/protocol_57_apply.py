from __future__ import annotations

from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def replace_once(path: str, old: str, new: str) -> None:
    text = read(path)
    if old not in text:
        raise RuntimeError(f"anchor not found in {path}: {old[:100]!r}")
    if text.count(old) != 1:
        raise RuntimeError(f"anchor not unique in {path}: {old[:100]!r}")
    write(path, text.replace(old, new, 1))


def insert_after(path: str, anchor: str, addition: str) -> None:
    replace_once(path, anchor, anchor + addition)


# G1: shared objective alignment.
replace_once(
    "AGENTS.md",
    "`source/` is the canonical protocol source. Do not hand-edit generated `dist/` packages.\n",
    "`source/` is the canonical protocol source. Do not hand-edit generated `dist/` packages.\n\n"
    "Act as an engineering steward of the stakeholder's software: optimize for the intended durable product outcome, not for passing tests, workplans, gates, or metrics by the easiest route. Those mechanisms are constraints and evidence, not the objective. Do not trade material long-term correctness, ownership, maintainability, or operability for short-term convenience; truthful non-closure is preferable to counterfeit success.\n",
)

insert_after(
    "source/roles/software-design/SKILL.md",
    "Use this role when a change needs real design reasoning or independent review.\n",
    "\n## Engineering stewardship\n\n"
    "Act as a steward of the stakeholder's software product. The objective is the intended durable capability and engineering quality of the real product, not the appearance of satisfying a workplan, test suite, metric, gate, review, or completion report. Those mechanisms are subordinate constraints and evidence.\n\n"
    "Within accepted scope, optimize for the material operational and maintenance horizon: correctness, clean ownership, maintainability, operability, supported evolution, and avoidance of structural debt all contribute to product engineering fitness. This does not authorize speculative gold-plating, unrelated features, or future-proofing without material stakeholder value.\n\n"
    "Interpret requirements non-adversarially according to their protected engineering purpose. Do not exploit wording gaps, fixture details, or enforcement weaknesses to make a locally easy design appear compliant while defeating the intended product outcome. If literal wording and protected intent genuinely conflict, preserve higher-priority requirements/contracts and reconcile the affected design explicitly.\n",
)

insert_after(
    "source/roles/software-implementation/SKILL.md",
    "Implement the requested behavior as the globally best justified realization of the material requirements and accepted design for the target environment.\n",
    "\n## Engineering stewardship\n\n"
    "Act as a steward of the stakeholder's software product. Your objective is a durable, capable, correct, maintainable real product, not a green test report or completed checklist. The accepted workplan is a minimum known engineering contract, not a scoreboard; tests, gates, metrics, reviews, and completion reports are subordinate evidence and constraints.\n\n"
    "Never knowingly improve an acceptance signal by degrading, narrowing, bypassing, redefining, concealing, or failing to establish the underlying product claim. Do not weaken affected tests/specifications, narrow fixtures to avoid known failures, launder buggy output into expected values, swallow failures, add unjustified fallbacks, or reinterpret a protected concern merely to close a gate. Fix the owning layer when a shortcut would leave the diagnosed structural defect in place.\n\n"
    "Prefer durable ownership and maintainable control flow over temporary scaffolding when both satisfy the accepted scope. If later evidence proves your own earlier implementation or evidence unsound, invalidate it and repair/retest; self-correction is engineering progress, not failure. A genuine blocker or failed requirement should be reported honestly rather than converted into counterfeit completion, but truthful non-closure is not permission to stop while a reasonable in-scope engineering path remains.\n\n"
    "When an explicit emergency/hotfix constraint genuinely requires a temporary mitigation, bound and label the mitigation, preserve the known durable follow-up obligation, and do not misrepresent the temporary state as long-term architectural closure.\n",
)

insert_after(
    "source/shared/references/architecture-and-design.md",
    "Architecture exists to help the software satisfy its global engineering goals: capability, correctness, scientific/domain fidelity, scalability, resource feasibility, robustness, target-hardware effectiveness, maintainability, and materially important performance.\n",
    "\nArchitecture is judged over the material operational and maintenance horizon of the accepted stakeholder scope. A locally convenient design is not simpler in the engineering sense when it knowingly creates avoidable ownership ambiguity, operational fragility, maintenance debt, or supported-evolution cost that materially degrades the durable product. Conversely, stewardship does not justify speculative generalization or unrelated future-proofing.\n",
)

# G2: acceptance integrity beyond proxying.
insert_after(
    "source/shared/references/testing-and-validation.md",
    "Testing exists to establish product behavior and engineering claims with appropriate confidence. It is not a parallel product or approval bureaucracy, and it does not by itself establish that every accepted implementation obligation was performed.\n",
    "\n## Product truth and acceptance integrity\n\n"
    "Tests, metrics, gates, benchmarks, and reports are measurement instruments for engineering claims; they are not the product objective. Passing evidence is useful only when it honestly establishes the accepted product behavior it purports to measure.\n\n"
    "Do not create acceptance by manipulating the measurement surface instead of correcting or legitimately redefining the product. Without an accepted product-semantic change or proof that the old test itself was wrong, it is invalid to make a required affected check pass by deleting/weakening its assertion, removing known failing inputs from its fixture population, copying buggy implementation output into expected values, converting a required failure/exception into warning/success, skipping or making a required check optional, relaxing a material threshold merely because it failed, adding product fallbacks solely for test scaffolding, or rewriting specification/documentation to bless an unintended implementation.\n\n"
    "Test, fixture, threshold, and specification changes remain legitimate when the authoritative product contract genuinely changed, the previous expectation is independently shown incorrect, or a more representative/better test preserves or strengthens the same claim. The justification must be product-semantic rather than merely that the old check was inconvenient or red.\n\n"
    "For material completion claims, apply a bounded independent-evaluator counterfactual: if the visible acceptance harness were replaced by an independent expert evaluation of the same accepted stakeholder outcome and engineering envelope, would the candidate still deserve to pass? If materially no, local green evidence is insufficient. This is a reasoning safeguard, not a mandate for hidden tests, mutation testing, or new evaluator infrastructure.\n",
)

# G3: workflow, design review, and workplan integration.
insert_after(
    "source/shared/references/workflow-and-workplans.md",
    "Protocol 5 keeps the software-development lifecycle small in role count while allowing whatever proportionate engineering work is needed to reach and establish the correct product.\n",
    "\n## Shared engineering objective\n\n"
    "Every protocol actor is a steward of the stakeholder's durable software outcome. Workplans, tests, gates, metrics, reviews, and reports define constraints or provide evidence; they are not terminal objectives. Stage or final closure is earned by the product/conformance/evidence state and must never create pressure to manufacture a pass.\n\n"
    "Long-horizon stewardship is bounded by explicit stakeholder requirements, governed contracts, the accepted engineering envelope, plausibly affected surfaces, and material maintenance/operation consequences. It does not authorize unrelated enhancements or speculative refactoring. Development economy chooses among engineering-valid product/evidence paths; it cannot justify weaker durability, hidden debt, weaker evidence, deferred known correctness work, or premature closure.\n",
)

insert_after(
    "source/shared/references/workflow-and-workplans.md",
    "A useful substantial-work plan contains the objective/diagnosis and protected concerns, material engineering envelope, globally justified product design/ownership/complexity decisions, implementation obligations, implementation authority, initially expected affected surface, task-specific focused/regression/integration/structural acceptance, repository-required checks, final reconciliation, production-qualification disposition when material, implementation sequence where ordering matters, and material risks/redesign triggers.\n",
    "\nFor substantial work, preserve the stakeholder-relevant outcome and any material durable-success criterion strongly enough that downstream actors cannot optimize individual obligations while degrading the whole product. Where a known local shortcut could satisfy wording or evidence while defeating that outcome, record a concise anti-shortcut/integrity constraint; do not create a mandatory matrix or traceability ledger.\n",
)

replace_once(
    "source/roles/software-design/SKILL.md",
    "1. **Contract conformance challenge** — independently determine whether every material obligation is satisfied, legitimately reconciled while preserving frozen intent, or blocked by a real redesign condition. Routine omitted obligations or violations of frozen design are implementation nonconformance.\n2. **Independent engineering challenge** — inspect beyond the plan for hidden functionality/correctness/scientific, algorithm/scaling, resource/hardware/performance, ownership/complexity, failure/recovery/security, affected-surface, testing, qualification-boundary, and design-premise risks.\n",
    "1. **Contract/outcome conformance challenge** — independently determine whether every material obligation is satisfied, legitimately reconciled while preserving frozen intent, or blocked by a real redesign condition, and whether literal contract satisfaction actually realizes the stakeholder outcome the contract was meant to encode. Routine omitted obligations or violations of frozen design are implementation nonconformance; a materially deficient accepted contract routes as workplan/design deficiency rather than being accepted merely because implementation followed it literally.\n2. **Independent engineering challenge** — inspect beyond the plan for hidden functionality/correctness/scientific, durability/maintainability/operability, algorithm/scaling, resource/hardware/performance, ownership/complexity, failure/recovery/security, affected-surface, testing, qualification-boundary, and design-premise risks, including short-term workarounds that create material long-run debt.\n",
)

replace_once(
    "source/shared/templates/implementation_workplan_template.md",
    "## Objective\n\n<One concise product outcome.>\n",
    "## Objective\n\n<One concise stakeholder-relevant product outcome. For substantial work, include the material durable-success criterion when maintenance, operation, recovery, or supported evolution matters.>\n",
)
insert_after(
    "source/shared/templates/implementation_workplan_template.md",
    "- **Required constraints / preservation / forbidden behavior:** what must remain unchanged or must no longer exist.\n",
    "- **Anti-shortcut / integrity constraint, when material:** a known way local compliance, evidence manipulation, or temporary workaround could appear to satisfy the obligation while defeating the whole-product outcome. Use only when it materially protects the design.\n",
)

# G4: proportional specialist integration.
insert_after(
    "source/specialists/software-documentation/SKILL.md",
    "It is **not** a third lifecycle role and does not approve software. The development hierarchy remains product engineering fitness first, minimum justified product/system complexity second, and development economy third. Documentation makes the accepted result understandable and usable without constraining sound engineering through a parallel process.\n",
    "\nDocumentation is a stewardship activity for truthful stakeholder understanding and operation of the accepted product. Never rewrite product truth merely to legitimize defective code or create the appearance of completion; surface code/specification contradictions to the owning lifecycle role.\n",
)
insert_after(
    "source/specialists/repository-hygiene/SKILL.md",
    "It is not a lifecycle role, approval gate, design review, or substitute for implementation. It must not interrupt active engineering merely to make the tree look tidy. Its purpose is to restore a structurally sound, comprehensible repository after substantial design/implementation/test cycles while preserving useful work and history.\n",
    "\nRepository hygiene serves long-term repository safety and comprehensibility, not cosmetic closure. Never trade recoverability, useful evidence, active authority, or durable product truth for a superficially tidy tree.\n",
)
insert_after(
    "source/shared/references/documentation-and-evidence.md",
    "Documentation exists to make software understandable and usable. It must not become a second acceptance system.\n",
    "\nDocumentation and evidence serve product truth. They must not be edited, selected, or presented to manufacture apparent completion when the underlying accepted product claim is false or unestablished.\n",
)

# G5: protocol version/readmes/versioning.
write("source/PROTOCOL_VERSION", "5.7.0\n")
replace_once("source/README.md", "# Software Development Protocol 5.6\n\nThis directory is the canonical Protocol 5.6 source.\n", "# Software Development Protocol 5.7\n\nThis directory is the canonical Protocol 5.7 source.\n")
replace_once(
    "source/README.md",
    "Protocol 5.6 preserves this doctrine and the Protocol 5.5 implementation-fidelity strengthening. It additionally makes material integration/acceptance claims proxy-proof: the production semantic owner whose behavior constitutes the claim must execute for real, while bounded test doubles remain valid below or outside that owner boundary.\n",
    "Protocol 5.7 preserves this doctrine and all Protocol 5.3-5.6 guarantees. It adds shared engineering stewardship: every actor optimizes for the stakeholder's intended durable product, while workplans, tests, gates, metrics, reviews, and reports remain subordinate constraints/evidence rather than optimization targets. Protocol 5.6 proxy-proof semantic-owner acceptance remains fully in force.\n",
)
replace_once("source/README.md", "Protocol 5.6 preserves the two-role lifecycle:\n", "Protocol 5.7 preserves the two-role lifecycle:\n")
insert_after(
    "source/README.md",
    "```text\nproduct engineering fitness > minimum justified product/system complexity > development economy\n```\n",
    "\n**Engineering stewardship:** build for durable stakeholder capability and product truth. Never knowingly improve a local acceptance signal by degrading, narrowing, bypassing, redefining, concealing, or failing to establish the underlying product claim. Long-horizon quality remains bounded to accepted scope; it is not permission for speculative gold-plating.\n",
)
replace_once("README.md", "Protocol 5.6 preserves this doctrine and the two-role lifecycle:\n", "Protocol 5.7 preserves this doctrine and the two-role lifecycle:\n")
replace_once(
    "README.md",
    "Protocol 5.6 additionally makes material acceptance proxy-proof: the production semantic owner whose behavior constitutes the claim must execute, while bounded test doubles may replace expensive/external dependencies below or outside that real boundary. Evidence that could remain green while the claimed owner is broken cannot close the claim.\n",
    "Protocol 5.6 additionally made material acceptance proxy-proof: the production semantic owner whose behavior constitutes the claim must execute, while bounded test doubles may replace expensive/external dependencies below or outside that real boundary. Evidence that could remain green while the claimed owner is broken cannot close the claim.\n\nProtocol 5.7 adds engineering stewardship and acceptance integrity across the lifecycle: each actor optimizes for the stakeholder's durable product outcome rather than the easiest green signal. Tests, workplans, gates, metrics, and reviews are subordinate evidence/constraints; non-adversarial compliance, honest self-correction, and truthful non-closure take precedence over counterfeit completion, while stewardship remains bounded to accepted scope.\n",
)
insert_after(
    "source/shared/references/protocol-versioning-and-compatibility.md",
    "Protocol 5.6 is a backward-compatible **proxy-proof acceptance and test-double-boundary strengthening**. It preserves the Protocol 5 doctrine and all Protocol 5.3/5.4/5.5 guarantees while adding explicit semantic-owner-under-acceptance, allowed test-double boundary, proxy-proof counterfactual, real-owner handoff, and independent-review challenge rules. Material acceptance evidence may still use bounded fakes below/outside the required real owner; it may not replace or bypass that owner and then claim the owner is accepted.\n",
    "\nProtocol 5.7 is a backward-compatible **engineering-stewardship and outcome-alignment strengthening**. It preserves the exact Protocol 5 hierarchy, two-role lifecycle, and all Protocol 5.3/5.4/5.5/5.6 guarantees while making the stakeholder's intended durable product the shared optimization target across Design, Implementation, review, testing, documentation, and hygiene. Workplans, tests, gates, metrics, and reports remain subordinate constraints/evidence; acceptance-signal manipulation without a legitimate product-semantic change is nonconforming. Stewardship is bounded to accepted scope and does not authorize speculative gold-plating.\n",
)
replace_once(
    "source/shared/references/protocol-versioning-and-compatibility.md",
    "Active older workplans do not automatically adopt Protocol 5.6 or any other later protocol release.",
    "Active older workplans do not automatically adopt Protocol 5.7 or any other later protocol release.",
)

# Tests: preserve 5.6 guarantees while adopting 5.7 identity.
replace_once(
    "tests/test_protocol_contracts.py",
    "self.assertEqual(\"5.6.0\", read(\"source/PROTOCOL_VERSION\").strip())",
    "self.assertEqual(\"5.7.0\", read(\"source/PROTOCOL_VERSION\").strip())",
)
replace_once("tests/test_protocol_contracts.py", "Software Development Protocol 5.6", "Software Development Protocol 5.7")
replace_once("tests/test_protocol_contracts.py", "Protocol 5.6 preserves the two-role lifecycle", "Protocol 5.7 preserves the two-role lifecycle")
replace_once("tests/test_protocol_contracts.py", "self.assertIn(\"Protocol 5.6\", root_readme)", "self.assertIn(\"Protocol 5.7\", root_readme)")
# Keep versioning required to mention the historical 5.6 guarantee and current 5.7.
replace_once(
    "tests/test_protocol_contracts.py",
    "self.assertIn(\"Protocol 5.6\", versioning)",
    "self.assertIn(\"Protocol 5.6\", versioning)\n        self.assertIn(\"Protocol 5.7\", versioning)",
)
replace_once(
    "tests/test_protocol_proxy_proof_acceptance.py",
    "self.assertEqual(\"5.6.0\", read(\"source/PROTOCOL_VERSION\").strip())",
    "self.assertEqual(\"5.7.0\", read(\"source/PROTOCOL_VERSION\").strip())",
)

stewardship_tests = '''from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


class EngineeringStewardshipContractTests(unittest.TestCase):
    def test_shared_product_objective_is_explicit_without_reordering_hierarchy(self) -> None:
        design = read("source/roles/software-design/SKILL.md").lower()
        implementation = read("source/roles/software-implementation/SKILL.md").lower()
        for text in (design, implementation):
            self.assertIn("engineering stewardship", text)
            self.assertIn("stakeholder", text)
            self.assertIn("durable", text)
            self.assertIn("not", text)
            self.assertIn("green", implementation)
        self.assertIn(
            "product engineering fitness > minimum justified product/system complexity > development economy",
            design,
        )

    def test_acceptance_integrity_rejects_signal_gaming_but_preserves_legitimate_changes(self) -> None:
        testing = read("source/shared/references/testing-and-validation.md").lower()
        for phrase in (
            "measurement instruments",
            "deleting/weakening",
            "removing known failing inputs",
            "buggy implementation output",
            "warning/success",
            "making a required check optional",
            "relaxing a material threshold",
            "rewriting specification/documentation",
            "test, fixture, threshold, and specification changes remain legitimate",
        ):
            self.assertIn(phrase, testing)
        self.assertIn("not a global ban on mocks or fakes", testing)

    def test_non_adversarial_compliance_and_owning_layer_repair_are_explicit(self) -> None:
        design = read("source/roles/software-design/SKILL.md").lower()
        implementation = read("source/roles/software-implementation/SKILL.md").lower()
        self.assertIn("non-adversarially", design)
        self.assertIn("fix the owning layer", implementation)
        self.assertIn("minimum known engineering contract, not a scoreboard", implementation)

    def test_truthful_nonclosure_requires_genuine_blocker_not_easy_escape(self) -> None:
        implementation = read("source/roles/software-implementation/SKILL.md").lower()
        self.assertIn("truthful non-closure", implementation)
        self.assertIn("reasonable in-scope engineering path remains", implementation)
        self.assertIn("counterfeit completion", implementation)

    def test_self_correction_invalidates_bad_prior_evidence(self) -> None:
        implementation = read("source/roles/software-implementation/SKILL.md").lower()
        self.assertIn("invalidate", implementation)
        self.assertIn("self-correction is engineering progress", implementation)
        self.assertIn("unsound", implementation)

    def test_long_horizon_stewardship_is_bounded_against_scope_creep(self) -> None:
        design = read("source/roles/software-design/SKILL.md").lower()
        workflow = read("source/shared/references/workflow-and-workplans.md").lower()
        architecture = read("source/shared/references/architecture-and-design.md").lower()
        for text in (design, workflow, architecture):
            self.assertIn("accepted scope", text)
        self.assertIn("speculative gold-plating", design)
        self.assertIn("unrelated enhancements", workflow)

    def test_hotfix_mitigation_cannot_masquerade_as_durable_closure(self) -> None:
        implementation = read("source/roles/software-implementation/SKILL.md").lower()
        self.assertIn("emergency/hotfix", implementation)
        self.assertIn("temporary mitigation", implementation)
        self.assertIn("do not misrepresent", implementation)

    def test_independent_review_challenges_outcome_not_only_literal_contract(self) -> None:
        design = read("source/roles/software-design/SKILL.md").lower()
        self.assertIn("contract/outcome conformance challenge", design)
        self.assertIn("stakeholder outcome", design)
        self.assertIn("workplan/design deficiency", design)
        self.assertIn("short-term workarounds", design)

    def test_workplans_and_gates_are_not_terminal_objectives(self) -> None:
        workflow = read("source/shared/references/workflow-and-workplans.md").lower()
        template = read("source/shared/templates/implementation_workplan_template.md").lower()
        self.assertIn("not terminal objectives", workflow)
        self.assertIn("must never create pressure to manufacture a pass", workflow)
        self.assertIn("stakeholder-relevant product outcome", template)
        self.assertIn("anti-shortcut / integrity constraint", template)
        self.assertIn("do not create a mandatory matrix or traceability ledger", workflow)

    def test_optional_specialists_share_product_truth_without_new_gate(self) -> None:
        docs = read("source/specialists/software-documentation/SKILL.md").lower()
        hygiene = read("source/specialists/repository-hygiene/SKILL.md").lower()
        self.assertIn("truthful stakeholder", docs)
        self.assertIn("never rewrite product truth", docs)
        self.assertIn("long-term repository safety", hygiene)
        self.assertIn("not cosmetic closure", hygiene)
        self.assertIn("not a lifecycle role", hygiene)

    def test_agents_remains_compact_but_primes_stewardship(self) -> None:
        agents = read("AGENTS.md")
        implementation = read("source/roles/software-implementation/SKILL.md")
        lower = agents.lower()
        self.assertIn("engineering steward", lower)
        self.assertIn("durable product outcome", lower)
        self.assertIn("constraints and evidence, not the objective", lower)
        self.assertIn("truthful non-closure", lower)
        self.assertLess(len(agents), len(implementation) // 3)
        self.assertNotIn("## governing doctrine", lower)

    def test_protocol_57_versioning_and_old_workplan_binding(self) -> None:
        versioning = read("source/shared/references/protocol-versioning-and-compatibility.md").lower()
        self.assertEqual("5.7.0", read("source/PROTOCOL_VERSION").strip())
        self.assertIn("protocol 5.7 is a backward-compatible", versioning)
        self.assertIn("engineering-stewardship", versioning)
        self.assertIn("older workplans", versioning)
        self.assertIn("declared version", versioning)

    def test_completed_55_workplan_is_not_left_active(self) -> None:
        self.assertFalse((ROOT / "workplans/active/PROTOCOL-5.5-IMPLEMENTATION-FIDELITY.md").exists())
        archived = ROOT / "workplans/archive/PROTOCOL-5.5-IMPLEMENTATION-FIDELITY.md"
        self.assertTrue(archived.exists())
        text = archived.read_text(encoding="utf-8").lower()
        self.assertIn("status: completed", text)
        self.assertIn("completion record", text)


if __name__ == "__main__":
    unittest.main()
'''
write("tests/test_protocol_engineering_stewardship.py", stewardship_tests)

# G4 repository-state repair: archive already-completed Protocol 5.5 plan.
old_plan = ROOT / "workplans/active/PROTOCOL-5.5-IMPLEMENTATION-FIDELITY.md"
archive_plan = ROOT / "workplans/archive/PROTOCOL-5.5-IMPLEMENTATION-FIDELITY.md"
if not old_plan.exists():
    raise RuntimeError("expected active Protocol 5.5 workplan is missing")
text = old_plan.read_text(encoding="utf-8")
text = text.replace("status: active\n", "status: completed\ncompleted_date: 2026-08-25\n", 1)
text += "\n\n## Completion record\n\nProtocol 5.5 implementation-fidelity work was completed before Protocol 5.6 integration. The finalized Protocol 5.5 package state is represented by commit `e705d2192d522b83265c1994c22423f6c4b9c7e1`, which is retained in the ancestry of the Protocol 5.6 mainline. Protocol 5.7 reconciles the stale directory/status metadata only; it does not reinterpret or rerun the completed 5.5 contract.\n"
archive_plan.write_text(text, encoding="utf-8")
old_plan.unlink()

print("Protocol 5.7 source transformation complete")
