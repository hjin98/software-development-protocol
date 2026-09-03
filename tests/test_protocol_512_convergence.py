from __future__ import annotations

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8").lower()


def paragraph(text: str, *needles: str) -> str:
    needles = tuple(n.lower() for n in needles)
    return next((p for p in text.lower().split("\n\n") if all(n in p for n in needles)), "")


def section(text: str, start: str, end: str) -> str:
    text = text.lower()
    a = text.find(start.lower())
    if a < 0:
        return ""
    b = text.find(end.lower(), a + len(start))
    return text[a : len(text) if b < 0 else b]


def holds(text: str, anchor: str, required: tuple[str, ...], forbidden: tuple[str, ...] = ()) -> bool:
    scope = paragraph(text, anchor)
    return bool(scope) and all(re.search(p, scope, re.DOTALL) for p in required) and not any(
        re.search(p, scope, re.DOTALL) for p in forbidden
    )


def first_local_holds(text: str) -> bool:
    return holds(
        text,
        "first clean local defect",
        (r"first clean local defect.{0,160}(?:owning-layer|local).{0,80}(?:fix|repair)", r"does not require.{0,140}(?:census|matrix|redesign)"),
        (r"first clean local defect.{0,100}(?:must|always).{0,100}(?:family closure|redesign|design reconsideration)",),
    )


def recurrence_holds(text: str) -> bool:
    return holds(
        text,
        "recurs after claimed closure",
        (r"family closure\s+is\s+required.{0,220}recurs after claimed closure",),
        (r"family closure.{0,80}(?:optional|may be skipped|need not occur)",),
    )


def incomplete_family_holds(text: str) -> bool:
    return holds(
        text,
        "incomplete family closure",
        (r"incomplete family closure.{0,220}implementation nonconformance", r"under the current accepted design unless independent redesign evidence"),
        (r"incomplete family closure.{0,120}(?:automatically|always).{0,120}(?:redesign|design reconsideration)",),
    )


def post_family_holds(text: str) -> bool:
    return holds(
        text,
        "same material family survives or reappears",
        (r"genuine family closure", r"route to.{0,80}software design reconsideration"),
        (r"(?:continue|permit|allow).{0,100}(?:another ordinary|one more).{0,80}(?:patch|repair)",),
    )


def mode_r_holds(text: str) -> bool:
    return holds(
        text,
        "normative design change is not predetermined",
        (r"normative design change is not predetermined", r"keep frozen.{0,180}(?:consolidat|refactor|canonical)"),
        (r"(?:always|automatically|must).{0,100}normative (?:design|authority|workplan) revision",),
    )


def family_identity_holds(text: str) -> bool:
    scope = section(text, "### semantic defect families", "### family closure after recurrence") or text.lower()
    return all(
        re.search(p, scope, re.DOTALL)
        for p in (
            r"family membership is not textual similarity",
            r"separate files.{0,180}do not make defects independent",
            r"broad labels.{0,220}not valid families",
            r"do not fragment.{0,120}do not overaggregate",
        )
    )


def saturation_holds(text: str) -> bool:
    return holds(
        text,
        "when a blocker implicates a material family",
        (r"reviewer must.{0,120}proportionate and practical", r"continue.{0,140}cheap, high-information.{0,140}inspection", r"group same-family evidence.{0,160}one family-level closure problem"),
        (r"(?:should|must|may)\s+stop.{0,80}first.{0,80}(?:blocker|example|finding)",),
    )


def saturation_bounds_hold(text: str) -> bool:
    stop = paragraph(text, "reviewer expansion stops")
    suff = paragraph(text, "not proof that no conceivable repository defect exists")
    return bool(stop and suff) and not re.search(r"(?:must|required to).{0,100}(?:exhaustive|whole-repository|every conceivable)", stop + suff, re.DOTALL)


def nonrefusal_holds(text: str) -> bool:
    scope = paragraph(text, "explicitly requested review")
    positive = re.search(r"explicitly requested review.{0,160}(?:still proceeds|must not be refused)", scope, re.DOTALL) or re.search(
        r"do not refuse.{0,120}explicitly requested review", scope, re.DOTALL
    )
    return bool(positive) and not re.search(r"explicitly requested review.{0,120}(?:must|should|may) be refused", scope, re.DOTALL)


def liveness_holds(text: str) -> bool:
    return holds(
        text,
        "patched seam, failpoint, callback",
        (r"trigger actually fired", r"production transition or decision.{0,180}real semantic owner"),
        (r"(?:trigger|failpoint|callback).{0,100}(?:need not|does not need to|may fail to) fire",),
    )


def structural_complement_holds(text: str) -> bool:
    return holds(
        text,
        "structural/negative scans",
        (r"structural/negative scans\s+complement\s+runtime acceptance", r"zero findings.{0,160}not proof of absence"),
        (r"structural/negative scans.{0,120}(?:replace|substitute for).{0,120}(?:runtime|executable) acceptance",),
    )


def tooling_optional_holds(text: str) -> bool:
    scope = section(text, "## convergence-oriented composition", "## completion discipline") or text.lower()
    return all(re.search(p, scope, re.DOTALL) for p in (r"optional tools", r"tool absence does not relax family closure", r"tool presence does not make.{0,100}three-tool sequence mandatory")) and not re.search(
        r"(?:must|required to|always).{0,100}(?:serena|semgrep).{0,180}(?:hypothesis|three-tool)", scope, re.DOTALL
    )


def revision_economy_holds(text: str) -> bool:
    return holds(
        text,
        "ordinary implementation attempts and review cycles",
        (r"do not require.{0,80}numbered authority revision",),
        (r"ordinary implementation attempts and review cycles\s+(?:require|must create).{0,80}numbered authority revision",),
    )


def current_authority_holds(text: str) -> bool:
    return holds(
        text,
        "reconcile that semantic into canonical current authority",
        (r"still-binding task-specific consequence.{0,240}reconcile that semantic into canonical current authority", r"before the next design -> implementation handoff"),
        (r"still-binding task-specific.{0,180}(?:may|can).{0,80}(?:remain|stay).{0,80}(?:history|review notes|conversation)",),
    )


def concrete_evidence_holds(text: str) -> bool:
    return holds(
        text,
        "concrete new sites",
        (r"concrete new sites.{0,220}are evidence rather than new normative semantics", r"current supplied invariant/owner authority already governs them"),
        (r"concrete (?:new )?(?:sites|siblings|examples).{0,180}(?:must|always|required to).{0,120}(?:become|create|enter).{0,80}new normative",),
    )


class Protocol512ConvergenceTests(unittest.TestCase):
    def setUp(self) -> None:
        self.workflow = read("source/shared/references/workflow-and-workplans.md")
        self.testing = read("source/shared/references/testing-and-validation.md")
        self.architecture = read("source/shared/references/architecture-and-design.md")
        self.intake = read("source/shared/references/repository-intake.md")
        self.tooling = read("source/shared/references/tool-assisted-engineering.md")
        self.design = read("source/roles/software-design/SKILL.md")
        self.implementation = read("source/roles/software-implementation/SKILL.md")
        self.template = read("source/shared/templates/implementation_workplan_template.md")
        self.versioning = read("source/shared/references/protocol-versioning-and-compatibility.md")

    def test_o10_01_03_identity_lifecycle_hierarchy(self) -> None:
        self.assertEqual("5.12.0", read("source/PROTOCOL_VERSION").strip())
        hierarchy = "product engineering fitness > minimum justified product/system complexity > development economy"
        for text in (self.design, self.implementation):
            self.assertIn(hierarchy, text)
        self.assertIn("software-design -> software-implementation", read("source/README.md"))
        self.assertIn("protocol 5.12 is a backward-compatible", self.versioning)

    def test_o10_04_06_24_26_escalation_semantics(self) -> None:
        for check in (first_local_holds, recurrence_holds, incomplete_family_holds, post_family_holds, mode_r_holds):
            self.assertTrue(check(self.workflow), check.__name__)
        self.assertIn("complete/correct that family closure", self.implementation)
        self.assertIn("same authority", self.architecture)

    def test_o10_07_08_23_family_identity_and_bounded_census(self) -> None:
        self.assertTrue(family_identity_holds(self.workflow))
        census = paragraph(self.intake, "switch to a bounded census only when")
        self.assertIn("progressive evidence-directed inspection remains the default", census)
        self.assertIn("bounded census only when", census)
        limits = paragraph(self.intake, "temporary closure maps")
        self.assertIn("not universal persistent traceability artifacts", limits)
        self.assertNotRegex(census + limits, r"whole[- ]repository.{0,80}(?:required|mandatory)")

    def test_o10_09_10_29_review_readiness_and_nonrefusal(self) -> None:
        ready = paragraph(self.workflow, "normal final independent closure review")
        for phrase in ("exact candidate identity", "accepted-contract reconciliation", "final complete affected-surface regression", "real-boundary integration", "repository/project-required checks"):
            self.assertIn(phrase, ready)
        incomplete = paragraph(self.workflow, "missing required closure/evidence")
        self.assertIn("implementation nonconformance", incomplete)
        self.assertIn("not an automatic design revision", incomplete)
        for text in (self.workflow, self.design, self.testing):
            self.assertTrue(nonrefusal_holds(text))

    def test_o10_11_12_31_32_33_revision_and_authority_semantics(self) -> None:
        self.assertTrue(revision_economy_holds(self.workflow))
        self.assertTrue(current_authority_holds(self.workflow))
        self.assertTrue(concrete_evidence_holds(self.workflow))
        self.assertIn("snapshot completeness is preserved", self.workflow)
        self.assertIn("ordinary implementation misses and review cycles do not require numbered authority revisions", self.design)

    def test_o10_13_27_28_30_review_is_broad_saturated_and_bounded(self) -> None:
        for phrase in ("independent engineering challenge", "new independent issue", "evidence-directed review is an economy rule, not a scope cap"):
            self.assertIn(phrase, self.design)
        self.assertTrue(saturation_holds(self.workflow))
        self.assertTrue(saturation_bounds_hold(self.workflow))
        self.assertIn("proportionately saturate the directly implicated family", self.design)
        self.assertIn("evidence-directed sufficiency", self.design)

    def test_o10_14_15_scope_and_unrelated_issue_bounds(self) -> None:
        horizon = paragraph(self.workflow, "provisional **closure horizon**")
        self.assertIn("not a scope ceiling", horizon)
        unrelated = paragraph(self.workflow, "unrelated pre-existing issue does not block current closure")
        self.assertIn("only when evidence shows", unrelated)
        self.assertIn("materially interacts with it", unrelated)

    def test_o10_16_17_liveness_and_structural_complementarity(self) -> None:
        self.assertTrue(liveness_holds(self.testing))
        self.assertTrue(structural_complement_holds(self.testing))
        self.assertIn("real semantic owner", self.testing)

    def test_o10_18_tools_remain_optional(self) -> None:
        self.assertTrue(tooling_optional_holds(self.tooling))
        self.assertIn("tool availability alone is not a reason", self.tooling)
        self.assertIn("tool unavailability is not an acceptance failure", self.tooling)

    def test_o10_19_stage_final_regression_and_integration_remain_mandatory(self) -> None:
        for text in (self.testing, self.implementation):
            self.assertIn("stage-local affected regression", text)
        final = section(self.testing, "## final assembled acceptance", "## prefer direct testing")
        self.assertIn("complete affected-surface regression", final)
        self.assertIn("integration/end-to-end", final)

    def test_o10_20_production_qualification_remains_separate(self) -> None:
        self.assertIn("production qualification is separate", self.implementation)
        self.assertIn("distinct from functional testing", self.testing)
        self.assertIn("production run never substitutes", self.implementation)

    def test_o10_21_evidence_context_and_stage_economy(self) -> None:
        self.assertIn("reuse still-valid intermediate evidence", self.testing)
        self.assertIn("lowest-cost next inspection", self.intake)
        self.assertIn("a local coherent behavior change is normally one material implementation stage", self.implementation)
        self.assertIn("several tightly coupled edits may close under one stage", self.workflow)

    def test_o10_22_no_fixed_count_can_force_acceptance(self) -> None:
        p = paragraph(self.workflow, "no recurrence count, review count")
        self.assertIn("can force acceptance", p)
        self.assertIn("not the pass threshold", p)

    def test_template_guidance_remains_conditional_and_nonbureaucratic(self) -> None:
        self.assertIn("conditional convergence guidance", self.template)
        self.assertIn("does not require a family matrix", self.template)
        self.assertIn("do not require ids, ledgers, persistent closure maps", self.template)

    def test_counterfactual_escalation_inversions_are_rejected(self) -> None:
        cases = (
            (first_local_holds, "A first clean local defect must immediately enter family closure and Design reconsideration; local owning-layer repair is forbidden."),
            (recurrence_holds, "When a defect recurs after claimed closure, another local sibling patch is sufficient and family closure is optional."),
            (incomplete_family_holds, "Incomplete family closure automatically forces redesign and is not implementation nonconformance."),
            (post_family_holds, "If the same material family survives or reappears after a genuine family closure, continue another ordinary patch without Design reconsideration."),
            (mode_r_holds, "Mode R always requires a normative design revision even when frozen target semantics remain sound; same-authority refactoring is forbidden."),
        )
        for check, policy in cases:
            with self.subTest(policy=policy):
                self.assertFalse(check(policy))

    def test_counterfactual_family_review_tool_inversions_are_rejected(self) -> None:
        cases = (
            (family_identity_holds, "Family membership is textual similarity. Separate files make defects independent and broad subsystem labels are valid families. Fragment by file and overaggregate unrelated work."),
            (saturation_holds, "When a blocker implicates a material family, the reviewer should stop at the first cheap blocker even when more high-information sibling inspection is available."),
            (saturation_bounds_hold, "Reviewer expansion is required to be exhaustive across the whole repository and prove every conceivable defect is absent."),
            (nonrefusal_holds, "An explicitly requested review must be refused whenever final review readiness is incomplete."),
            (tooling_optional_holds, "Convergence requires Serena, Semgrep, and Hypothesis as a mandatory three-tool sequence for every recurring family."),
        )
        for check, policy in cases:
            with self.subTest(policy=policy):
                self.assertFalse(check(policy))

    def test_counterfactual_acceptance_authority_inversions_are_rejected(self) -> None:
        cases = (
            (liveness_holds, "A patched seam, failpoint, callback may be accepted even when the trigger need not fire and the production transition owner is bypassed."),
            (structural_complement_holds, "Structural/negative scans replace runtime acceptance; zero findings are proof of absence and executable checks may be skipped."),
            (revision_economy_holds, "Ordinary implementation attempts and review cycles require a new numbered authority revision after every miss."),
            (current_authority_holds, "A still-binding task-specific consequence may remain only in review notes or conversation and need not enter canonical current authority before handoff."),
            (concrete_evidence_holds, "Concrete new sites already governed by the current invariant must always become new normative semantics solely for provenance."),
        )
        for check, policy in cases:
            with self.subTest(policy=policy):
                self.assertFalse(check(policy))


if __name__ == "__main__":
    unittest.main()
