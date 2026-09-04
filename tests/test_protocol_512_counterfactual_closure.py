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
    scope = section(text, "## semantic defect families", "## family closure after recurrence") or text.lower()
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
    return not any(
        x in scope
        for x in (
            "family membership is textual similarity",
            "separate files make defects independent",
            "broad labels are valid families",
        )
    )


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
    return all(x in scope for x in required) and not re.search(
        r"(?:always|required|mandatory).{0,100}(?:whole repository|persistent traceability)", scope, re.S
    )


def reviewer_bounds(text: str) -> bool:
    scope = paragraph(text, "reviewer expansion stops") + "\n" + paragraph(
        text, "not proof that no conceivable repository defect exists"
    )
    return all(x in scope for x in ("reviewer expansion stops", "not proof that no conceivable repository defect exists")) and not re.search(
        r"(?:must|required to).{0,100}(?:exhaustive|whole repository|every conceivable)", scope, re.S
    )


def nonrefusal(text: str) -> bool:
    scope = paragraph(text, "explicitly requested review")
    return "explicitly requested review" in scope and (
        "still proceeds" in scope or "must not be refused" in scope or "do not refuse" in scope
    ) and "explicitly requested review must be refused" not in scope


def broad_review(text: str) -> bool:
    scope = section(text, "## independent review mode", "## convergence-aware review trigger") or text.lower()
    required = (
        "independent engineering challenge",
        "inspect beyond the plan",
        "new independent issue",
        "evidence-directed review is an economy rule, not a scope cap",
    )
    return all(x in scope for x in required) and "independent review is limited to the plan" not in scope


def closure_horizon(text: str) -> bool:
    scope = paragraph(text, "provisional closure horizon")
    return all(x in scope for x in ("not a scope ceiling", "expand it whenever evidence establishes")) and "hard scope ceiling" not in scope


def unrelated_issue(text: str) -> bool:
    scope = paragraph(text, "unrelated pre-existing issue does not block current closure")
    required = ("does not block current closure merely because review discovered it", "only when evidence shows", "materially interacts with it")
    return all(x in scope for x in required) and "always blocks current closure" not in scope


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
    return all(x in stage + "\n" + final for x in required)


def evidence_economy(text: str) -> bool:
    required = (
        "reuse still-valid intermediate evidence",
        "rerun a check when a changed dimension can plausibly alter the result or interpretation",
        "never removes final assembled acceptance requirements",
        "a local coherent behavior change is normally one material implementation stage",
        "several tightly coupled edits may close under one stage",
        "lowest-cost next inspection",
    )
    return all(x in text.lower() for x in required)


def no_forced_acceptance(text: str) -> bool:
    scope = paragraph(text, "no recurrence count, review count")
    return "can force acceptance" in scope and "not the pass threshold" in scope and "fixed review count forces acceptance" not in scope


def check_pair(test: unittest.TestCase, fn, positive: str, contradiction: str) -> None:
    test.assertTrue(fn(positive), f"positive rejected by {fn.__name__}")
    test.assertFalse(fn(positive + " " + contradiction), f"contradiction accepted by {fn.__name__}")


class Protocol512CounterfactualClosureTests(unittest.TestCase):
    def setUp(self) -> None:
        self.convergence = read("source/shared/references/convergence-and-cycle-economy.md")
        self.workflow = read("source/shared/references/workflow-and-workplans.md")
        self.testing = read("source/shared/references/testing-and-validation.md")
        self.intake = read("source/shared/references/repository-intake.md")
        self.tooling = read("source/shared/references/tool-assisted-engineering.md")
        self.design = read("source/roles/software-design/SKILL.md")
        self.implementation = read("source/roles/software-implementation/SKILL.md")

    def test_source_policy_direction_is_currently_valid(self) -> None:
        checks = (
            (family_identity, self.convergence),
            (bounded_census, self.intake),
            (reviewer_bounds, self.convergence),
            (nonrefusal, self.convergence),
            (nonrefusal, self.design),
            (nonrefusal, self.testing),
            (broad_review, self.design),
            (closure_horizon, self.convergence),
            (unrelated_issue, self.convergence),
            (regression_mandatory, self.testing),
            (no_forced_acceptance, self.convergence),
        )
        for fn, text in checks:
            with self.subTest(check=fn.__name__):
                self.assertTrue(fn(text))
        economy = "\n\n".join((self.testing, self.workflow, self.implementation, self.intake))
        self.assertTrue(evidence_economy(economy))

    def test_existing_relation_helpers_reject_direct_inversions(self) -> None:
        cases = (
            (first_local_holds, "A first clean local defect receives a local owning-layer fix and does not require a census, matrix, or redesign.", "A first clean local defect must always enter family closure and Design reconsideration."),
            (recurrence_holds, "Family closure is required when a defect recurs after claimed closure.", "Family closure is optional and may be skipped."),
            (incomplete_family_holds, "Incomplete family closure remains implementation nonconformance under the current accepted design unless independent redesign evidence exists.", "Incomplete family closure automatically forces redesign."),
            (post_family_holds, "If the same material family survives or reappears after a genuine family closure, route to bounded Software Design reconsideration.", "Continue another ordinary patch instead."),
            (mode_r_holds, "Normative design change is not predetermined; Design may keep frozen semantics and require consolidation, refactoring, or canonicalization.", "Implementation must always require a normative design revision."),
            (saturation_holds, "When a blocker implicates a material family, the reviewer must, to the degree proportionate and practical, continue cheap, high-information inspection and group same-family evidence into one family-level closure problem.", "The reviewer should stop at the first blocker."),
            (liveness_holds, "For a patched seam, failpoint, callback, show that the trigger actually fired and that the production transition or decision executes the real semantic owner.", "The trigger need not fire."),
            (structural_complement_holds, "Structural/negative scans complement runtime acceptance; zero findings are not proof of absence.", "Structural/negative scans replace runtime acceptance."),
            (revision_economy_holds, "Ordinary implementation attempts and review cycles do not require a numbered authority revision.", "Ordinary implementation attempts and review cycles require a numbered authority revision."),
            (current_authority_holds, "If a still-binding task-specific consequence is discovered, reconcile that semantic into canonical current authority before the next Design -> Implementation handoff.", "A still-binding task-specific consequence may remain only in conversation."),
            (concrete_evidence_holds, "Concrete new sites are evidence rather than new normative semantics when current supplied invariant/owner authority already governs them.", "Concrete new sites must always become new normative semantics."),
        )
        for fn, positive, contradiction in cases:
            with self.subTest(check=fn.__name__):
                check_pair(self, fn, positive, contradiction)

    def test_hardened_directional_rules_are_nonvacuous(self) -> None:
        check_pair(
            self,
            family_identity,
            "## Semantic defect families\nFamily membership is not textual similarity. Separate files do not make defects independent. Broad labels are not valid families. Do not fragment one family and do not overaggregate unrelated defects.\n\n## Family closure after recurrence\n",
            "Family membership is textual similarity.",
        )
        check_pair(
            self,
            reviewer_bounds,
            "Reviewer expansion stops when the sibling space is characterized. Review is not proof that no conceivable repository defect exists.",
            "Reviewer expansion must always continue exhaustively across the whole repository.",
        )
        check_pair(
            self,
            nonrefusal,
            "Review readiness is not a refusal mechanism: an explicitly requested review still proceeds.",
            "An explicitly requested review must be refused.",
        )
        check_pair(
            self,
            closure_horizon,
            "A provisional closure horizon is not a scope ceiling: expand it whenever evidence establishes a plausible affected chain.",
            "It is a hard scope ceiling.",
        )
        check_pair(
            self,
            unrelated_issue,
            "An unrelated pre-existing issue does not block current closure merely because review discovered it; it becomes current-scope material only when evidence shows that the active change materially interacts with it.",
            "An unrelated pre-existing issue always blocks current closure.",
        )
        check_pair(
            self,
            no_forced_acceptance,
            "No recurrence count, review count, cycle budget, or convergence target can force acceptance; escalation changes the engineering method, not the pass threshold.",
            "A fixed review count forces acceptance.",
        )

    def test_tool_family_composition_remains_optional(self) -> None:
        self.assertTrue(tooling_optional_holds(self.tooling))


if __name__ == "__main__":
    unittest.main()
