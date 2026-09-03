from __future__ import annotations

import re
import unittest
from pathlib import Path

from tests.test_protocol_512_convergence import (
    concrete_evidence_holds,
    current_authority_holds,
    first_local_holds,
    incomplete_family_holds,
    liveness_holds,
    mode_r_holds,
    post_family_holds,
    recurrence_holds,
    revision_economy_holds,
    saturation_holds,
    structural_complement_holds,
    tooling_optional_holds,
)

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8").lower()


def paragraph(text: str, needle: str) -> str:
    needle = needle.lower()
    return next((p for p in text.lower().split("\n\n") if needle in p), "")


def section(text: str, start: str, end: str) -> str:
    text = text.lower()
    a = text.find(start.lower())
    if a < 0:
        return ""
    b = text.find(end.lower(), a + len(start))
    return text[a : len(text) if b < 0 else b]


def clauses(text: str) -> list[str]:
    return [c.strip() for c in re.split(r";\s*|(?<=[.!?])\s+", text.lower()) if c.strip()]


def family_identity(text: str) -> bool:
    scope = section(text, "### semantic defect families", "### family closure after recurrence") or text.lower()
    required = (
        "family membership is not textual similarity",
        "separate files",
        "do not make defects independent",
        "broad labels",
        "not valid families",
        "do not fragment",
        "do not overaggregate",
    )
    if not all(x in scope for x in required):
        return False
    for c in clauses(scope):
        if "family membership is textual similarity" in c:
            return False
        if "separate files make defects independent" in c:
            return False
        if "broad labels are valid families" in c:
            return False
        if "fragment by file" in c or "overaggregate unrelated" in c and "do not overaggregate" not in c:
            return False
    return True


def bounded_census(text: str) -> bool:
    trigger = paragraph(text, "switch to a bounded census only when")
    boundary = paragraph(text, "rather than the whole repository")
    maps = paragraph(text, "temporary closure maps")
    scope = "\n".join((trigger, boundary, maps))
    required = (
        "progressive evidence-directed inspection remains the default",
        "switch to a bounded census only when",
        "rather than the whole repository",
        "not universal persistent traceability artifacts",
    )
    if not all(x in scope for x in required):
        return False
    return not re.search(r"(?:(?:always|required|mandatory).{0,100}(?:whole repository|persistent traceability)|whole repository.{0,100}(?:always|required|mandatory)|persistent traceability.{0,100}(?:always|required|mandatory))", scope, re.S)


def reviewer_bounds(text: str) -> bool:
    scope = paragraph(text, "reviewer expansion stops") + "\n" + paragraph(text, "not proof that no conceivable repository defect exists")
    if not all(x in scope for x in ("reviewer expansion stops", "not proof that no conceivable repository defect exists")):
        return False
    for c in clauses(scope):
        if any(x in c for x in ("whole repository", "exhaustive", "every conceivable")) and any(
            x in c for x in ("always", "must", "required")
        ):
            return False
    return True


def nonrefusal(text: str) -> bool:
    scope = paragraph(text, "explicitly requested review")
    relevant = [c for c in clauses(scope) if "review" in c and ("refus" in c or "proceed" in c)]
    if not any(x in c for c in relevant for x in ("still proceeds", "must not be refused", "do not refuse")):
        return False
    return not any("refus" in c and not any(x in c for x in ("must not be refused", "do not refuse", "not a refusal mechanism", "not a mechanism for refusing review")) for c in relevant)


def broad_review(text: str) -> bool:
    scope = section(text, "## independent review mode", "## convergence-aware independent review") or text.lower()
    required = (
        "independent engineering challenge",
        "inspect beyond the plan",
        "new independent issue",
        "evidence-directed review is an economy rule, not a scope cap",
    )
    if not all(x in scope for x in required):
        return False
    return not any(
        ("scope cap" in c and "not a scope cap" not in c)
        or ("independent review" in c and "limited to" in c and "plan" in c)
        or ("may not" in c and "new independent issue" in c)
        for c in clauses(scope)
    )


def closure_horizon(text: str) -> bool:
    scope = paragraph(text, "not a scope ceiling")
    if not all(x in scope for x in ("closure horizon", "not a scope ceiling", "expand it whenever evidence establishes")):
        return False
    return not any("scope ceiling" in c and "not a scope ceiling" not in c or "never expand" in c for c in clauses(scope))


def unrelated_issue(text: str) -> bool:
    scope = paragraph(text, "unrelated pre-existing issue does not block current closure")
    required = ("does not block current closure merely because review discovered it", "only when evidence shows", "materially interacts with it")
    if not all(x in scope for x in required):
        return False
    return not re.search(r"unrelated pre-existing issue.{0,100}(?:always|automatically|must).{0,80}block", scope, re.S)


def regression_mandatory(text: str) -> bool:
    stage = section(text, "## stage-local affected regression", "## evidence reuse and invalidation") or text.lower()
    final = section(text, "## final assembled acceptance", "## prefer direct testing") or text.lower()
    required = (
        "after **each material implementation stage that changes executable behavior**",
        "required **stage-local affected regression**",
        "not optional",
        "rerun the complete affected-surface regression",
        "run integration/end-to-end tests",
    )
    scope = stage + "\n" + final
    if not all(x in scope for x in required):
        return False
    return not any(
        ("stage-local affected regression" in c or "integration/end-to-end" in c)
        and any(x in c for x in ("may be skipped", "need not run", "optional"))
        and "not optional" not in c
        for c in clauses(scope)
    )


def evidence_economy(text: str) -> bool:
    text = text.lower()
    required = (
        "reuse still-valid intermediate evidence",
        "rerun a check when a changed dimension can plausibly alter the result or interpretation",
        "never removes final assembled acceptance requirements",
        "a local coherent behavior change is normally one material implementation stage",
        "several tightly coupled edits may close under one stage",
        "lowest-cost next inspection",
    )
    if not all(x in text for x in required):
        return False
    return not re.search(r"(?:invalidated|stale) evidence.{0,100}(?:may|can) be reused|final assembled acceptance.{0,80}may be skipped", text, re.S)


def no_forced_acceptance(text: str) -> bool:
    scope = paragraph(text, "no recurrence count, review count")
    if "no recurrence count, review count, cycle budget, or convergence target can force acceptance" not in scope or "not the pass threshold" not in scope:
        return False
    return not re.search(r"(?:fixed|preset|\b\d+\b).{0,80}(?:review|cycle|recurrence).{0,80}forces? acceptance", scope, re.S)


def check_pair(test: unittest.TestCase, fn, positive: str, contradiction: str, before: str | None = None) -> None:
    test.assertTrue(fn(positive), f"positive rejected by {fn.__name__}")
    if before:
        test.assertIn(before, positive)
        negative = positive.replace(before, contradiction + "\n\n" + before, 1)
    else:
        negative = positive + " " + contradiction
    test.assertFalse(fn(negative), f"contradiction accepted by {fn.__name__}")


class Protocol512CounterfactualClosureTests(unittest.TestCase):
    def setUp(self) -> None:
        self.workflow = read("source/shared/references/workflow-and-workplans.md")
        self.testing = read("source/shared/references/testing-and-validation.md")
        self.intake = read("source/shared/references/repository-intake.md")
        self.tooling = read("source/shared/references/tool-assisted-engineering.md")
        self.design = read("source/roles/software-design/SKILL.md")
        self.implementation = read("source/roles/software-implementation/SKILL.md")

    def test_source_policy_direction_is_currently_valid(self) -> None:
        checks = (
            (family_identity, self.workflow),
            (bounded_census, self.intake),
            (reviewer_bounds, self.workflow),
            (nonrefusal, self.workflow),
            (nonrefusal, self.design),
            (nonrefusal, self.testing),
            (broad_review, self.design),
            (closure_horizon, self.workflow),
            (unrelated_issue, self.workflow),
            (regression_mandatory, self.testing),
            (no_forced_acceptance, self.workflow),
        )
        for fn, text in checks:
            with self.subTest(check=fn.__name__):
                self.assertTrue(fn(text))
        economy = "\n\n".join((self.testing, self.workflow, self.implementation, self.intake))
        self.assertTrue(evidence_economy(economy))

    def test_existing_relation_helpers_reject_retained_positive_contradictions(self) -> None:
        cases = (
            (first_local_holds, "A first clean local defect receives a local owning-layer fix and does not require a census, matrix, or redesign.", "A first clean local defect must always enter family closure and Design reconsideration."),
            (recurrence_holds, "Family closure is required when a defect recurs after claimed closure.", "Family closure is optional and may be skipped."),
            (incomplete_family_holds, "Incomplete family closure remains implementation nonconformance under the current accepted design unless independent redesign evidence exists.", "Incomplete family closure automatically forces redesign."),
            (post_family_holds, "If the same material family survives or reappears after a genuine family closure, route to bounded Software Design reconsideration.", "Continue another ordinary patch instead."),
            (mode_r_holds, "Normative design change is not predetermined; Design may keep frozen semantics and require consolidation, refactoring, or canonicalization.", "Mode R must always require a normative authority revision."),
            (saturation_holds, "When a blocker implicates a material family, the reviewer must, to the degree proportionate and practical, continue cheap, high-information inspection and group same-family evidence into one family-level closure problem.", "The reviewer should stop at the first blocker."),
            (liveness_holds, "For a patched seam, failpoint, callback, show that the trigger actually fired and that the production transition or decision executes the real semantic owner.", "The trigger need not fire."),
            (structural_complement_holds, "Structural/negative scans complement runtime acceptance; zero findings are not proof of absence.", "Structural/negative scans replace runtime acceptance."),
            (revision_economy_holds, "Ordinary implementation attempts and review cycles do not require a numbered authority revision.", "Ordinary implementation attempts and review cycles require a numbered authority revision."),
            (current_authority_holds, "If a still-binding task-specific consequence is discovered, reconcile that semantic into canonical current authority before the next Design -> Implementation handoff.", "A still-binding task-specific consequence may remain in review notes or conversation."),
            (concrete_evidence_holds, "Concrete new sites are evidence rather than new normative semantics when current supplied invariant/owner authority already governs them.", "Concrete new sites must always become new normative semantics solely for provenance."),
        )
        for fn, positive, contradiction in cases:
            with self.subTest(check=fn.__name__):
                check_pair(self, fn, positive, contradiction)

    def test_hardened_family_review_and_directional_rules_are_nonvacuous(self) -> None:
        family = "### Semantic defect families\nFamily membership is not textual similarity. Separate files do not make defects independent. Broad labels are not valid families. Do not fragment one family and do not overaggregate unrelated defects.\n\n### Family closure after recurrence\n"
        check_pair(self, family_identity, family, "Family membership is textual similarity.", "### Family closure after recurrence")

        census = "Progressive evidence-directed inspection remains the default. Switch to a bounded census only when recurrence establishes a family; bound it rather than the whole repository. Temporary closure maps are allowed; they are not universal persistent traceability artifacts."
        check_pair(self, bounded_census, census, "A whole repository census is always mandatory.")

        bounds = "Reviewer expansion stops when the sibling space is characterized. Review is not proof that no conceivable repository defect exists."
        check_pair(self, reviewer_bounds, bounds, "Reviewer expansion always continues exhaustively across the whole repository.")

        refusal = "Review readiness is not a refusal mechanism: an explicitly requested review still proceeds."
        check_pair(self, nonrefusal, refusal, "That review is always refused when readiness is incomplete.")

        broad = "## Independent review mode\nIndependent engineering challenge means inspect beyond the plan and route a new independent issue when found. Evidence-directed review is an economy rule, not a scope cap.\n\n## Convergence-aware independent review\n"
        check_pair(self, broad_review, broad, "Independent review is limited to the plan and may not surface a new independent issue.", "## Convergence-aware independent review")

        horizon = "A provisional **closure horizon** focuses implementation, but it is not a scope ceiling: expand it whenever evidence establishes a plausible affected chain."
        check_pair(self, closure_horizon, horizon, "The closure horizon is a hard scope ceiling and must never expand.")

        unrelated = "An unrelated pre-existing issue does not block current closure merely because review discovered it; it becomes current-scope material only when evidence shows that the active change exposes, depends on, or materially interacts with it."
        check_pair(self, unrelated_issue, unrelated, "An unrelated pre-existing issue always blocks current closure.")

        regression = "## Stage-local affected regression\nAfter **each material implementation stage that changes executable behavior**, run focused checks and the required **stage-local affected regression**. This requirement is not optional.\n\n## Evidence reuse and invalidation\n\n## Final assembled acceptance\nRerun the complete affected-surface regression and run integration/end-to-end tests.\n\n## Prefer direct testing\n"
        check_pair(self, regression_mandatory, regression, "Stage-local affected regression may be skipped.", "## Evidence reuse and invalidation")

        economy = "Reuse still-valid intermediate evidence. Rerun a check when a changed dimension can plausibly alter the result or interpretation. Evidence reuse never removes final assembled acceptance requirements. A local coherent behavior change is normally one material implementation stage. Several tightly coupled edits may close under one stage. Choose the lowest-cost next inspection."
        check_pair(self, evidence_economy, economy, "Invalidated evidence may be reused and final assembled acceptance may be skipped.")

        count = "No recurrence count, review count, cycle budget, or convergence target can force acceptance; escalation changes the engineering method, not the pass threshold."
        check_pair(self, no_forced_acceptance, count, "A fixed review count forces acceptance.")

    def test_tool_optional_policy_rejects_a_mandatory_pipeline(self) -> None:
        positive = "## Convergence-oriented composition\nThese are optional tools. Tool absence does not relax family closure. Tool presence does not make a three-tool sequence mandatory.\n\n## Completion discipline\n"
        self.assertTrue(tooling_optional_holds(positive))
        contradictory = positive.replace(
            "## Completion discipline",
            "Serena, Semgrep, and Hypothesis must always be used as a mandatory three-tool sequence.\n\n## Completion discipline",
        )
        scope = section(contradictory, "## convergence-oriented composition", "## completion discipline")
        self.assertRegex(scope, r"serena.{0,80}semgrep.{0,80}hypothesis.{0,100}(?:must|mandatory)")
        self.assertNotIn("serena, semgrep, and hypothesis must always", section(self.tooling, "## convergence-oriented composition", "## completion discipline"))


if __name__ == "__main__":
    unittest.main()
