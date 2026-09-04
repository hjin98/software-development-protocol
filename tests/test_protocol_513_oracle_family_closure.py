from __future__ import annotations

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def norm(text: str) -> str:
    return text.lower().replace("**", "").replace("`", "")


def paragraph_containing(text: str, needle: str) -> str:
    needle = needle.lower()
    for paragraph in text.split("\n\n"):
        if needle in paragraph.lower():
            return paragraph
    raise AssertionError(f"no paragraph contains {needle!r}")


def section_between(text: str, start_heading: str, end_heading: str) -> str:
    lowered = text.lower()
    start = lowered.index(start_heading.lower())
    end = lowered.index(end_heading.lower(), start)
    return text[start:end]


def policy_clauses_in_paragraph(text: str, needle: str) -> list[str]:
    paragraph = paragraph_containing(text, needle).lower()
    return [
        clause.strip()
        for clause in re.split(r";\s*|(?<=[.!?])\s+", paragraph)
        if clause.strip()
    ]


def replace_once(text: str, old: str, new: str) -> str:
    if old not in text:
        raise AssertionError(f"mutation anchor missing: {old!r}")
    return text.replace(old, new, 1)


def mutate_paragraph(text: str, needle: str, contradiction: str) -> str:
    paragraph = paragraph_containing(text, needle)
    mutated = paragraph.rstrip() + " " + contradiction.strip()
    return replace_once(text, paragraph, mutated)


# ---------------------------------------------------------------------------
# Historical Protocol 5.11 directional predicates.
# These intentionally retain the bounded clause-aware behavior of the base
# suite rather than reducing preservation to a small forbidden-word list.
# ---------------------------------------------------------------------------


def negative_subject_clause_holds(clause: str, subject: str) -> bool:
    clause = clause.lower()
    subject_pattern = re.escape(subject.lower())
    article = r"(?:an?\s+)?"
    patterns = (
        rf"\bwithout\s+(?:becoming|forming|requiring|using)\s+{article}{subject_pattern}\b",
        rf"\b(?:not|never)\s+{article}{subject_pattern}\b",
        rf"\b(?:must|should|do|does|is|are)\s+not\s+"
        rf"(?:(?:be|become|form|require|use)\s+)?{article}{subject_pattern}\b",
        rf"\bnever\s+(?:becomes?|forms?|requires?|uses?)\s+{article}{subject_pattern}\b",
    )
    return any(re.search(pattern, clause) for pattern in patterns)


def negative_subject_policy_holds(text: str, subject: str) -> bool:
    clauses = [
        clause
        for clause in policy_clauses_in_paragraph(text, subject)
        if subject.lower() in clause
    ]
    return bool(clauses) and all(
        negative_subject_clause_holds(clause, subject) for clause in clauses
    )


ANTI_GAMING_MECHANISMS = (
    "excessive filtering",
    "assume",
    "over-narrow strategies",
    "exclusions",
    "health-check suppression",
    "disabled useful phases",
    "removed deadlines",
    "reduced exploration",
)
GREEN_PROPERTY_PURPOSE = (
    r"\b(?:solely|merely)\s+to\s+(?:make|manufacture)\s+(?:a\s+)?property\s+green\b"
)


def hypothesis_anti_gaming_clause_holds(clause: str) -> bool:
    clause = clause.lower()
    if not re.search(GREEN_PROPERTY_PURPOSE, clause):
        return False

    present = [mechanism for mechanism in ANTI_GAMING_MECHANISMS if mechanism in clause]
    if not present:
        return False

    prohibition = re.search(
        rf"\b(?:(?:do|does)\s+not|must\s+not|never)\s+"
        rf"(?:use|apply|employ|introduce|rely\s+on)\b"
        rf"(?P<body>.{{0,700}}?{GREEN_PROPERTY_PURPOSE})",
        clause,
    )
    if prohibition is None:
        return False

    body = prohibition.group("body")
    if not all(mechanism in body for mechanism in present):
        return False
    if re.search(r"\b(?:but|however|except|unless)\b", clause):
        return False
    return True


def hypothesis_anti_gaming_policy_holds(text: str) -> bool:
    clauses = policy_clauses_in_paragraph(text, "health-check suppression")
    governed = [
        clause
        for clause in clauses
        if re.search(GREEN_PROPERTY_PURPOSE, clause)
        and any(mechanism in clause for mechanism in ANTI_GAMING_MECHANISMS)
    ]
    if not governed or not all(
        hypothesis_anti_gaming_clause_holds(clause) for clause in governed
    ):
        return False

    covered = {
        mechanism
        for clause in governed
        for mechanism in ANTI_GAMING_MECHANISMS
        if mechanism in clause
    }
    return covered == set(ANTI_GAMING_MECHANISMS)


def hypothesis_settings_clause_holds(clause: str) -> bool:
    clause = clause.lower()
    change_condition = re.search(r"\bchange settings\b.{0,100}\bwhen\b", clause)
    if change_condition is None:
        return False

    justification = re.search(
        r"\bsemantics\b(?P<link>.{0,40})\bjustif(?:y|ies|ied)\b",
        clause,
    )
    if justification is None:
        return False
    if re.search(
        r"\b(?:not|never|no)\b|\bfail(?:s|ed)?\s+to\b|"
        r"\b(?:don't|doesn't|didn't|cannot|can't)\b",
        justification.group("link"),
    ):
        return False

    coverage = re.search(
        r"\brequired coverage\s+(?:remains?|stays?|is\s+(?:kept|preserved))\s+intact\b",
        clause,
    )
    if coverage is None or coverage.start() < justification.end():
        return False

    tail = clause[coverage.end() :]
    return not re.search(
        r"\b(?:is|are)\s+not\s+(?:required|necessary)\b|"
        r"\bneed(?:s)?\s+not\b|\boptional\b|\bnot\s+(?:required|necessary)\b|"
        r"\b(?:unless|except)\b",
        tail,
    )


def hypothesis_settings_policy_holds(text: str) -> bool:
    clauses = policy_clauses_in_paragraph(text, "change settings")
    relevant = [
        clause
        for clause in clauses
        if "change settings" in clause or "required coverage" in clause
    ]
    governing = [clause for clause in relevant if "change settings" in clause]
    return (
        bool(governing)
        and all(hypothesis_settings_clause_holds(clause) for clause in governing)
        and len(relevant) == len(governing)
    )


# ---------------------------------------------------------------------------
# Protocol 5.13 distributed routing-chain predicates.
# ---------------------------------------------------------------------------

ROUTE_CASES = (
    (
        "ordinary",
        "literal/path/text lookup or small deterministic local inspection",
        "ordinary repository search/read normally remains sufficient",
    ),
    (
        "serena",
        "symbol ownership/definition/callers/references/implementations",
        "references/tool-serena.md",
    ),
    (
        "semgrep",
        "ast/syntax/structural patterns",
        "references/tool-semgrep.md",
    ),
    (
        "hypothesis",
        "broad/combinatorial python input/state invariants",
        "references/tool-hypothesis.md",
    ),
    (
        "codeql",
        "supported interprocedural flow/taint/source-to-sink relations",
        "references/tool-codeql.md",
    ),
)


def dispatch_section(text: str) -> str:
    return section_between(text, "### Per-question tool dispatch", "### Domain-conditional routes")


def route_line(section: str, anchor: str) -> str:
    matches = [line for line in norm(section).splitlines() if anchor in line]
    if len(matches) != 1:
        return ""
    return matches[0]


def route_map_holds(role_text: str) -> bool:
    section = dispatch_section(role_text)
    value = norm(section)
    if "classify each material engineering question by the relation under the claim, not once per task" not in value:
        return False

    for name, anchor, target in ROUTE_CASES:
        line = route_line(section, anchor)
        if not line or target not in line:
            return False
        if name == "ordinary":
            if "must read" in line or "references/tool-" in line:
                return False
        elif "must read" not in line:
            return False

    common_lines = [
        line for line in value.splitlines() if "references/tool-assisted-engineering.md" in line
    ]
    if not common_lines or any("must read" in line or "before" in line for line in common_lines):
        return False
    if any(
        marker in value
        for marker in (
            "must read tool-assisted engineering first",
            "must read [tool-assisted engineering] first",
            "before reading any triggered tool-specific method, must read",
            "common router is a mandatory prerequisite",
        )
    ):
        return False
    return True


def capability_disposition_holds(role_text: str) -> bool:
    value = norm(dispatch_section(role_text))
    required = (
        "when a specialized trigger fires and availability is unknown",
        "cheap non-mutating capability probe when practical",
        "available/current/supported and directly models the claim",
        "presumptively use it",
        "concrete fallback",
        "familiarity with built-in search/read/shell/test tools is not itself a fallback reason",
    )
    if not all(item in value for item in required):
        return False
    forbidden = (
        "never probe unknown availability",
        "assume the specialized capability is unavailable without checking",
        "silently assume the specialized capability is unavailable",
        "default to ordinary tools without checking",
        "familiarity with built-in search/read/shell/test tools is a valid fallback reason",
        "familiarity with grep/read/shell/tests is a valid fallback reason",
    )
    return not any(item in value for item in forbidden)


def common_relation_policy_holds(common_text: str) -> bool:
    value = norm(common_text)
    required = (
        "classify the relation under the current material claim",
        "literal/path/text relation -> ordinary repository search/read",
        "symbol owner/definition/reference/caller relation -> serena",
        "ast/syntax/structural relation -> semgrep",
        "broad python input/state invariant -> hypothesis",
        "interprocedural flow/taint/source-to-sink relation -> codeql",
        "a security task is not automatically a codeql task",
        "a forbidden-call pattern is structural",
        "multi-function untrusted-source-to-dangerous-sink claim is interprocedural data flow",
        "decompose a multi-relation claim",
    )
    if not all(item in value for item in required):
        return False
    forbidden = (
        "security always means codeql",
        "all security tasks always route to codeql",
        "a forbidden-call pattern must use codeql",
        "source-to-sink is merely structural and should use semgrep",
    )
    return not any(item in value for item in forbidden)


def model_limit_policy_holds(common_text: str) -> bool:
    value = norm(common_text)
    required = (
        "specialized tools are bounded models",
        "state negative/completeness claims no more broadly than",
        "cross-check dynamic dispatch",
        "generated code",
        "external consumers",
        "runtime-only behavior",
        "when those can hide material dependencies",
    )
    if not all(item in value for item in required):
        return False
    forbidden = (
        "specialized analyzer output is exhaustive",
        "specialist output is exhaustive",
        "never needs material cross-checking",
        "never needs cross-checking",
    )
    return not any(item in value for item in forbidden)


def specialist_owner_holds(name: str, text: str) -> bool:
    value = norm(text)
    required_by_name = {
        "serena": (
            "semantic repository intake, navigation, reference discovery",
            "literal strings, filenames, configuration, generated/external surfaces",
            "cheap non-mutating availability/capability probe",
            "presumptively use serena",
            "cross-check semantic results",
        ),
        "semgrep": (
            "relation under the claim is structural",
            "do not route a purely literal lookup through semgrep",
            "do not use semgrep as a substitute for interprocedural/data-flow analysis",
            "cheap non-mutating capability probe when practical",
            "presumptively use it",
            "rule and analysis limitations that can create false negatives",
        ),
        "hypothesis": (
            "meaningful input or state space",
            "small deterministic examples and already-exhaustive finite cases do not require hypothesis",
            "cheap non-mutating capability probe when practical",
            "presumptively use generated property/stateful testing",
            "required coverage remains intact",
        ),
        "codeql": (
            "supported interprocedural program relations",
            "do not route a purely structural pattern to codeql",
            "security task is not automatically a codeql task",
            "cheap read-only/non-mutating capability probe when practical",
            "presumptively use it",
            "runtime/dynamic/plugin/external-consumer behavior outside the database model",
        ),
    }
    return all(item in value for item in required_by_name[name])


def routing_chain_holds(role_text: str, common_text: str, specialists: dict[str, str]) -> bool:
    return (
        route_map_holds(role_text)
        and capability_disposition_holds(role_text)
        and common_relation_policy_holds(common_text)
        and model_limit_policy_holds(common_text)
        and negative_subject_policy_holds(common_text, "mandatory three-tool pipeline")
        and all(specialist_owner_holds(name, text) for name, text in specialists.items())
    )


class Protocol513OracleFamilyClosureTests(unittest.TestCase):
    def setUp(self) -> None:
        self.roles = {
            "design": read("source/roles/software-design/SKILL.md"),
            "implementation": read("source/roles/software-implementation/SKILL.md"),
        }
        self.common = read("source/shared/references/tool-assisted-engineering.md")
        self.specialists = {
            "serena": read("source/shared/references/tool-serena.md"),
            "semgrep": read("source/shared/references/tool-semgrep.md"),
            "hypothesis": read("source/shared/references/tool-hypothesis.md"),
            "codeql": read("source/shared/references/tool-codeql.md"),
        }

    def test_historical_511_current_split_owners_are_accepted(self) -> None:
        self.assertTrue(negative_subject_policy_holds(self.common, "mandatory three-tool pipeline"))
        self.assertTrue(hypothesis_anti_gaming_policy_holds(self.specialists["hypothesis"]))
        self.assertTrue(hypothesis_settings_policy_holds(self.specialists["hypothesis"]))

    def test_historical_511_actual_owner_mutations_are_rejected(self) -> None:
        mutated_common = mutate_paragraph(
            self.common,
            "mandatory three-tool pipeline",
            "This is a mandatory three-tool pipeline.",
        )
        self.assertFalse(
            negative_subject_policy_holds(mutated_common, "mandatory three-tool pipeline")
        )

        mutated_hypothesis = mutate_paragraph(
            self.specialists["hypothesis"],
            "health-check suppression",
            "Health-check suppression should be used solely to make a property green.",
        )
        self.assertFalse(hypothesis_anti_gaming_policy_holds(mutated_hypothesis))

        mutated_settings = mutate_paragraph(
            self.specialists["hypothesis"],
            "change settings",
            "Required coverage may then be discarded.",
        )
        self.assertFalse(hypothesis_settings_policy_holds(mutated_settings))

    def test_historical_511_mandatory_pipeline_inversion_basis(self) -> None:
        subject = "mandatory three-tool pipeline"
        inverted = (
            "The tools can reinforce one another and form a mandatory three-tool pipeline.",
            "This is a mandatory three-tool pipeline. Do not duplicate evidence.",
            "The tools form a mandatory three-tool pipeline without extra ceremony.",
            "The tools can reinforce one another without becoming a mandatory three-tool pipeline; "
            "a mandatory three-tool pipeline is required.",
        )
        for policy in inverted:
            with self.subTest(policy=policy):
                self.assertFalse(negative_subject_policy_holds(policy, subject))

        valid = "The tools can reinforce one another without becoming a mandatory three-tool pipeline."
        self.assertTrue(negative_subject_policy_holds(valid, subject))

    def test_historical_511_hypothesis_anti_gaming_inversion_basis(self) -> None:
        complete = (
            "Do not use excessive filtering or assume, over-narrow strategies, exclusions, "
            "health-check suppression, disabled useful phases, removed deadlines, or reduced "
            "exploration solely to make a property green. "
        )
        inverted = (
            "Do not use excessive filtering, but health-check suppression is permitted solely to make a property green. "
            "Disabled useful phases, removed deadlines, and reduced exploration are also prohibited.",
            "Do not use excessive filtering, disabled useful phases, removed deadlines, or reduced exploration solely "
            "to make a property green. Health-check suppression may be used solely to make a property green.",
            "Do not use excessive filtering, health-check suppression, disabled useful phases, removed deadlines, or "
            "reduced exploration solely to make a property green. Health-check suppression may be used solely to make "
            "a property green when failures are inconvenient.",
            "Do not prohibit excessive filtering, health-check suppression, disabled useful phases, removed deadlines, "
            "or reduced exploration solely to make a property green.",
            "Do not worry; use excessive filtering, health-check suppression, disabled useful phases, removed deadlines, "
            "or reduced exploration solely to make a property green.",
            "Do not use excessive filtering, health-check suppression, disabled useful phases, removed deadlines, or "
            "reduced exploration solely to make a property green. Health-check suppression should be used solely to "
            "make a property green.",
            "Do not use excessive filtering, health-check suppression, disabled useful phases, removed deadlines, or "
            "reduced exploration unless solely to make a property green.",
            "Do not use excessive filtering, health-check suppression, disabled useful phases, removed deadlines, or "
            "reduced exploration solely to make a property green; health-check suppression should be used solely to "
            "make a property green.",
            complete + "Health-check suppression is acceptable solely to make a property green.",
            complete + "Assume may be used solely to make a property green.",
            complete + "Over-narrow strategies are allowed solely to make a property green.",
            complete + "Exclusions are permitted solely to make a property green.",
        )
        for policy in inverted:
            with self.subTest(policy=policy):
                self.assertFalse(hypothesis_anti_gaming_policy_holds(policy))

        self.assertTrue(hypothesis_anti_gaming_policy_holds(complete))
        self.assertTrue(
            hypothesis_anti_gaming_policy_holds(
                complete
                + "Filtering may be used when the governed input-domain contract genuinely requires it."
            )
        )

    def test_historical_511_hypothesis_settings_inversion_basis(self) -> None:
        inverted = (
            "Change settings when project/test semantics do not justify it and required coverage remains intact.",
            "Change settings when project/test semantics fail to justify it and required coverage remains intact.",
            "Change settings when project/test semantics justify it, although required coverage remains intact is not required.",
            "Change settings when project/test semantics justify it and required coverage remains intact unless maintaining it is inconvenient.",
            "Change settings when project/test semantics justify it and required coverage remains intact; required coverage may then be discarded.",
            "Change settings when project/test semantics justify it and required coverage remains intact; required coverage is no longer necessary.",
            "Change settings when project/test semantics justify it and required coverage remains intact; required coverage may be sacrificed.",
        )
        for policy in inverted:
            with self.subTest(policy=policy):
                self.assertFalse(hypothesis_settings_policy_holds(policy))

        valid = "Change settings when project/test semantics justify it and required coverage remains intact."
        self.assertTrue(hypothesis_settings_policy_holds(valid))

    def test_current_distributed_routing_chain_is_accepted_for_both_roles(self) -> None:
        for name, role in self.roles.items():
            with self.subTest(role=name):
                self.assertTrue(routing_chain_holds(role, self.common, self.specialists))

    def test_actual_role_route_mutations_reject_every_relation_class(self) -> None:
        mutations = (
            (
                "ordinary-to-specialist",
                "ordinary repository search/read normally remains sufficient;",
                "**MUST read** [CodeQL](references/tool-codeql.md);",
            ),
            (
                "serena-to-semgrep",
                "references/tool-serena.md",
                "references/tool-semgrep.md",
            ),
            (
                "semgrep-to-serena",
                "references/tool-semgrep.md",
                "references/tool-serena.md",
            ),
            (
                "hypothesis-to-serena",
                "references/tool-hypothesis.md",
                "references/tool-serena.md",
            ),
            (
                "codeql-to-semgrep",
                "references/tool-codeql.md",
                "references/tool-semgrep.md",
            ),
        )
        for role_name, role in self.roles.items():
            for mutation_name, old, new in mutations:
                mutated = replace_once(role, old, new)
                with self.subTest(role=role_name, mutation=mutation_name):
                    self.assertFalse(route_map_holds(mutated))

    def test_actual_role_direct_entry_mutation_is_rejected(self) -> None:
        for role_name, role in self.roles.items():
            mutated = replace_once(
                role,
                "### Per-question tool dispatch",
                "### Per-question tool dispatch\n\nBefore reading any triggered tool-specific method, "
                "**MUST read** [Tool-assisted engineering](references/tool-assisted-engineering.md) first.",
            )
            with self.subTest(role=role_name):
                self.assertFalse(route_map_holds(mutated))

    def test_actual_role_capability_probe_and_fallback_mutations_are_rejected(self) -> None:
        for role_name, role in self.roles.items():
            probe_mutation = mutate_paragraph(
                role,
                "when a specialized trigger fires and availability is unknown",
                "Never probe unknown availability; silently assume the specialized capability is unavailable.",
            )
            fallback_mutation = mutate_paragraph(
                role,
                "when a specialized trigger fires and availability is unknown",
                "Familiarity with built-in search/read/shell/test tools is a valid fallback reason.",
            )
            with self.subTest(role=role_name, mutation="probe"):
                self.assertFalse(capability_disposition_holds(probe_mutation))
            with self.subTest(role=role_name, mutation="fallback"):
                self.assertFalse(capability_disposition_holds(fallback_mutation))

    def test_capability_probe_and_fallback_boundaries_remain_conditional(self) -> None:
        for role_name, role in self.roles.items():
            boundary = mutate_paragraph(
                role,
                "when a specialized trigger fires and availability is unknown",
                "A capability already known unavailable need not be probed again, and a host with no safe practical cheap probe may take a concrete fallback.",
            )
            with self.subTest(role=role_name):
                self.assertTrue(capability_disposition_holds(boundary))

    def test_actual_common_overlap_and_model_limit_mutations_are_rejected(self) -> None:
        overlap_mutation = mutate_paragraph(
            self.common,
            "security task is not automatically a codeql task",
            "Security always means CodeQL.",
        )
        model_mutation = mutate_paragraph(
            self.common,
            "specialized tools are bounded models",
            "Specialized analyzer output is exhaustive and never needs material cross-checking.",
        )
        pipeline_mutation = mutate_paragraph(
            self.common,
            "mandatory three-tool pipeline",
            "A mandatory three-tool pipeline is required.",
        )
        self.assertFalse(common_relation_policy_holds(overlap_mutation))
        self.assertFalse(model_limit_policy_holds(model_mutation))
        self.assertFalse(
            negative_subject_policy_holds(pipeline_mutation, "mandatory three-tool pipeline")
        )

    def test_model_limit_cross_check_boundary_remains_proportionate(self) -> None:
        boundary = mutate_paragraph(
            self.common,
            "specialized tools are bounded models",
            "When no material model blind spot exists, no redundant duplicate analyzer pass is required.",
        )
        self.assertTrue(model_limit_policy_holds(boundary))

    def test_specialist_selection_boundaries_are_live(self) -> None:
        for name, text in self.specialists.items():
            with self.subTest(tool=name):
                self.assertTrue(specialist_owner_holds(name, text))


if __name__ == "__main__":
    unittest.main()
