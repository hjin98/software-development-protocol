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
        (r"first clean local defect.{0,180}(?:owning-layer|local).{0,100}(?:fix|repair)", r"does not require.{0,160}(?:census|matrix|redesign)"),
        (r"first clean local defect.{0,100}(?:must|always).{0,100}(?:family closure|redesign|design reconsideration)",),
    )


def recurrence_holds(text: str) -> bool:
    return holds(
        text,
        "recurs after claimed closure",
        (r"family closure\s+is\s+required.{0,260}recurs after claimed closure",),
        (r"family closure.{0,80}(?:optional|may be skipped|need not occur)",),
    )


def incomplete_family_holds(text: str) -> bool:
    return holds(
        text,
        "incomplete family closure",
        (r"incomplete family closure.{0,240}implementation nonconformance", r"under the current accepted design unless independent redesign evidence"),
        (r"incomplete family closure.{0,120}(?:automatically|always).{0,120}(?:redesign|design reconsideration)",),
    )


def post_family_holds(text: str) -> bool:
    return holds(
        text,
        "same material family survives or reappears",
        (r"genuine family closure", r"route to.{0,100}software design reconsideration"),
        (r"(?:continue|permit|allow).{0,100}(?:another ordinary|one more).{0,80}(?:patch|repair)",),
    )


def mode_r_holds(text: str) -> bool:
    return holds(
        text,
        "normative design change is not predetermined",
        (r"normative design change is not predetermined", r"keep frozen.{0,220}(?:consolidat|refactor|canonical)"),
        (r"(?:always|automatically|must).{0,100}normative (?:design|authority|workplan) revision",),
    )


def family_identity_holds(text: str) -> bool:
    scope = section(text, "## semantic defect families", "## family closure after recurrence") or text.lower()
    return all(
        re.search(p, scope, re.DOTALL)
        for p in (
            r"family membership is not textual similarity",
            r"separate files.{0,220}do not make defects independent",
            r"broad labels.{0,240}not valid families",
            r"do not fragment.{0,160}do not overaggregate",
        )
    )


def saturation_holds(text: str) -> bool:
    return holds(
        text,
        "when a blocker implicates a material family",
        (r"reviewer.{0,40}must.{0,160}proportionate and practical", r"continue cheap, high-information.{0,160}inspection", r"group same-family evidence.{0,180}one family-level closure problem"),
        (r"(?:should|must|may)\s+stop.{0,80}first.{0,80}(?:blocker|example|finding)",),
    )


def saturation_bounds_hold(text: str) -> bool:
    stop = paragraph(text, "reviewer expansion stops")
    suff = paragraph(text, "not proof that no conceivable repository defect exists")
    return bool(stop and suff) and not re.search(
        r"(?:must|required to).{0,120}(?:exhaustive|whole-repository|every conceivable)", stop + suff, re.DOTALL
    )


def nonrefusal_holds(text: str) -> bool:
    scope = paragraph(text, "explicitly requested review")
    positive = re.search(r"explicitly requested review.{0,180}(?:still proceeds|must not be refused)", scope, re.DOTALL) or re.search(
        r"do not refuse.{0,140}explicitly requested review", scope, re.DOTALL
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
        (r"structural/negative scans\s+complement\s+runtime acceptance", r"zero findings.{0,180}not proof of absence"),
        (r"structural/negative scans.{0,120}(?:replace|substitute for).{0,120}(?:runtime|executable) acceptance",),
    )


def tooling_optional_holds(text: str) -> bool:
    scope = section(text, "## convergence-oriented composition", "## completion discipline") or text.lower()
    return all(
        re.search(p, scope, re.DOTALL)
        for p in (
            r"optional tools",
            r"tool absence does not relax family closure",
            r"tool presence does not make.{0,160}mandatory",
        )
    ) and not re.search(r"(?:must|always|required to).{0,100}(?:serena.{0,80}semgrep.{0,80}hypothesis|four-tool|multi-tool)", scope, re.DOTALL)


def revision_economy_holds(text: str) -> bool:
    return holds(text, "ordinary implementation attempts and review cycles", (r"do not require.{0,100}numbered authority revision",))


def current_authority_holds(text: str) -> bool:
    return holds(
        text,
        "reconcile that semantic into canonical current authority",
        (r"still-binding task-specific consequence.{0,260}reconcile that semantic into canonical current authority", r"before the next design -> implementation handoff"),
    )


def concrete_evidence_holds(text: str) -> bool:
    return holds(
        text,
        "concrete new sites",
        (r"concrete new sites.{0,240}are evidence rather than new normative semantics", r"current supplied invariant/owner authority already governs them"),
    )


class Protocol512ConvergenceTests(unittest.TestCase):
    def setUp(self) -> None:
        self.workflow = read("source/shared/references/workflow-and-workplans.md")
        self.convergence = read("source/shared/references/convergence-and-cycle-economy.md")
        self.testing = read("source/shared/references/testing-and-validation.md")
        self.architecture = read("source/shared/references/architecture-and-design.md")
        self.intake = read("source/shared/references/repository-intake.md")
        self.tooling = read("source/shared/references/tool-assisted-engineering.md")
        self.design = read("source/roles/software-design/SKILL.md")
        self.implementation = read("source/roles/software-implementation/SKILL.md")
        self.template = read("source/shared/templates/implementation_workplan_template.md")
        self.versioning = read("source/shared/references/protocol-versioning-and-compatibility.md")

    def test_o10_01_03_identity_lifecycle_hierarchy(self) -> None:
        self.assertIn(read("source/PROTOCOL_VERSION").strip(), ("5.12.0", "5.13.0"))
        hierarchy = "product engineering fitness > minimum justified product/system complexity > development economy"
        for text in (self.design, self.implementation):
            self.assertIn(hierarchy, text)
        self.assertIn("software-design -> software-implementation", read("source/README.md"))

    def test_convergence_detailed_owner_preserves_escalation_semantics(self) -> None:
        for check in (first_local_holds, recurrence_holds, incomplete_family_holds, post_family_holds, mode_r_holds):
            self.assertTrue(check(self.convergence), check.__name__)
        self.assertIn("complete/correct incomplete family closure", self.implementation)
        self.assertIn("same authority", self.architecture)

    def test_workflow_and_roles_keep_direct_convergence_trigger(self) -> None:
        for text in (self.workflow, self.design, self.implementation):
            self.assertIn("convergence-and-cycle-economy.md", text)
        self.assertIn("first clean local defect remains local", self.workflow)
        self.assertIn("material sibling recurrence", self.workflow)
        self.assertIn("same-family recurrence after adequate closure", self.design)

    def test_family_identity_and_bounded_census(self) -> None:
        self.assertTrue(family_identity_holds(self.convergence))
        census = paragraph(self.intake, "switch to a bounded census only when")
        self.assertIn("progressive evidence-directed inspection remains the default", census)
        self.assertIn("bounded census only when", census)
        limits = paragraph(self.intake, "temporary closure maps")
        self.assertIn("not universal persistent traceability artifacts", limits)

    def test_review_readiness_nonrefusal_and_saturation(self) -> None:
        ready = paragraph(self.convergence, "normal final independent closure review")
        for phrase in ("exact candidate identity", "accepted-contract reconciliation", "final complete affected-surface regression", "real-boundary integration", "repository/project-required checks"):
            self.assertIn(phrase, ready)
        self.assertTrue(nonrefusal_holds(self.convergence))
        self.assertTrue(nonrefusal_holds(self.design))
        self.assertTrue(nonrefusal_holds(self.testing))
        self.assertTrue(saturation_holds(self.convergence))
        self.assertTrue(saturation_bounds_hold(self.convergence))

    def test_revision_authority_scope_and_count_semantics(self) -> None:
        self.assertTrue(revision_economy_holds(self.convergence))
        self.assertTrue(current_authority_holds(self.convergence))
        self.assertTrue(concrete_evidence_holds(self.convergence))
        horizon = paragraph(self.convergence, "provisional closure horizon")
        self.assertIn("not a scope ceiling", horizon)
        unrelated = paragraph(self.convergence, "unrelated pre-existing issue does not block current closure")
        self.assertIn("only when evidence shows", unrelated)
        count = paragraph(self.convergence, "no recurrence count, review count")
        self.assertIn("can force acceptance", count)
        self.assertIn("not the pass threshold", count)

    def test_acceptance_liveness_and_structural_complementarity(self) -> None:
        self.assertTrue(liveness_holds(self.testing))
        self.assertTrue(structural_complement_holds(self.testing))

    def test_tools_remain_optional_during_family_closure(self) -> None:
        self.assertTrue(tooling_optional_holds(self.tooling))
        self.assertIn("tool availability alone is not a reason", self.tooling)
        self.assertIn("tool unavailability is not an acceptance failure", self.tooling)

    def test_stage_final_regression_and_economy_remain_mandatory(self) -> None:
        for text in (self.testing, self.implementation):
            self.assertIn("stage-local affected regression", text)
        final = section(self.testing, "## final assembled acceptance", "## prefer direct testing")
        self.assertIn("complete affected-surface regression", final)
        self.assertIn("integration/end-to-end", final)
        self.assertIn("reuse still-valid intermediate evidence", self.testing)
        self.assertIn("lowest-cost next inspection", self.intake)
        self.assertIn("a local coherent behavior change is normally one material implementation stage", self.implementation)
        self.assertIn("several tightly coupled edits may close under one stage", self.workflow)

    def test_production_qualification_remains_separate(self) -> None:
        self.assertIn("production qualification is separate", self.implementation)
        self.assertIn("distinct from functional testing", self.testing)
        self.assertIn("production run never substitutes", self.implementation)

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
            (mode_r_holds, "Normative design change is not predetermined only when convenient; a normative design revision is always required."),
        )
        for check, policy in cases:
            with self.subTest(policy=policy):
                self.assertFalse(check(policy))


if __name__ == "__main__":
    unittest.main()
