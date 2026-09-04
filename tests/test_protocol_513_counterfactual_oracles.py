from __future__ import annotations

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def normalized(text: str) -> str:
    return text.lower().replace("**", "").replace("`", "")


def paragraph(text: str, needle: str) -> str:
    needle = normalized(needle)
    for item in normalized(text).split("\n\n"):
        if needle in item:
            return item
    return ""


def clauses(text: str) -> list[str]:
    return [
        clause.strip()
        for clause in re.split(r";\s*|(?<=[.!?])\s+", normalized(text))
        if clause.strip()
    ]


def check_pair(
    test: unittest.TestCase,
    predicate,
    positive: str,
    contradiction: str,
) -> None:
    test.assertTrue(predicate(positive), f"positive rejected by {predicate.__name__}")
    test.assertFalse(
        predicate(positive + " " + contradiction),
        f"contradiction accepted by {predicate.__name__}",
    )


def negative_subject_clause_holds(clause: str, subject: str) -> bool:
    clause = normalized(clause)
    subject_pattern = re.escape(normalized(subject))
    article = r"(?:an?\s+)?"
    patterns = (
        rf"\bwithout\s+(?:becoming|forming|requiring|using)\s+{article}{subject_pattern}\b",
        rf"\b(?:not|never)\s+{article}{subject_pattern}\b",
        rf"\b(?:must|should|do|does|is|are)\s+not\s+"
        rf"(?:(?:be|become|form|require|use)\s+)?{article}{subject_pattern}\b",
        rf"\bnever\s+(?:becomes?|forms?|requires?|uses?)\s+{article}{subject_pattern}\b",
    )
    return any(re.search(pattern, clause) for pattern in patterns)


def no_mandatory_pipeline_holds(text: str) -> bool:
    subject = "mandatory three-tool pipeline"
    scope = paragraph(text, subject)
    if not scope:
        return False
    subject_clauses = [c for c in clauses(scope) if subject in c]
    if not subject_clauses:
        return False
    return all(negative_subject_clause_holds(c, subject) for c in subject_clauses)


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
GREEN_PROPERTY_PURPOSE = r"\b(?:solely|merely)\s+to\s+(?:make|manufacture)\s+(?:a\s+)?property\s+green\b"


def hypothesis_anti_gaming_clause_holds(clause: str) -> bool:
    clause = normalized(clause)
    if not re.search(GREEN_PROPERTY_PURPOSE, clause):
        return False
    present = [m for m in ANTI_GAMING_MECHANISMS if m in clause]
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


def hypothesis_anti_gaming_holds(text: str) -> bool:
    scope = paragraph(text, "health-check suppression")
    if not scope:
        return False
    governed = [
        clause
        for clause in clauses(scope)
        if re.search(GREEN_PROPERTY_PURPOSE, clause)
        and any(mechanism in clause for mechanism in ANTI_GAMING_MECHANISMS)
    ]
    if not governed or not all(hypothesis_anti_gaming_clause_holds(c) for c in governed):
        return False
    covered = {
        mechanism
        for clause in governed
        for mechanism in ANTI_GAMING_MECHANISMS
        if mechanism in clause
    }
    return covered == set(ANTI_GAMING_MECHANISMS)


def hypothesis_settings_clause_holds(clause: str) -> bool:
    clause = normalized(clause)
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


def hypothesis_settings_holds(text: str) -> bool:
    scope = paragraph(text, "change settings")
    if not scope:
        return False
    relevant = [
        clause
        for clause in clauses(scope)
        if "change settings" in clause or "required coverage" in clause
    ]
    governing = [clause for clause in relevant if "change settings" in clause]
    return bool(governing) and all(hypothesis_settings_clause_holds(c) for c in governing) and len(relevant) == len(governing)


def dispatch_holds(text: str) -> bool:
    t = normalized(text)
    required = (
        "classify each material engineering question",
        "relation under the claim",
        "not once per task",
        "literal/path/text lookup or small deterministic local inspection",
        "ordinary repository search/read normally remains sufficient",
    )
    if not all(item in t for item in required):
        return False
    for ref in ("tool-serena.md", "tool-semgrep.md", "tool-hypothesis.md", "tool-codeql.md"):
        line = next((line for line in t.splitlines() if ref in line), "")
        if "must read" not in line:
            return False
    literal_line = next((line for line in t.splitlines() if "literal/path/text" in line), "")
    if "must read" in literal_line or any(name in literal_line for name in ("serena", "semgrep", "hypothesis", "codeql")):
        return False
    forbidden = (
        r"\bclassify\s+(?:the\s+)?task\s+once\b",
        r"\bclassify\s+once\s+per\s+task\b",
        r"\bchoose\s+one\s+tool\s+for\s+the\s+entire\s+task\b",
        r"\buse\s+codeql\s+for\s+every\s+question\b",
    )
    return not any(re.search(pattern, t) for pattern in forbidden)


def relation_first_holds(text: str) -> bool:
    t = normalized(text)
    required = (
        "relation under the current material claim",
        "security task is not automatically a codeql task",
        "forbidden-call pattern is structural",
        "source-to-dangerous-sink claim is interprocedural data flow",
        "decompose a multi-relation claim",
    )
    if not all(item in t for item in required):
        return False
    forbidden = (
        r"\ball security tasks?\b.{0,80}\bcodeql\b",
        r"\bsecurity\s+(?:always|automatically)\s+(?:means|routes?\s+to|requires?)\s+codeql\b",
        r"\bforbidden-call pattern\b.{0,60}\b(?:is|requires?)\s+codeql\b",
        r"\bsource-to-dangerous-sink\b.{0,80}\b(?:is|requires?)\s+semgrep\b",
    )
    return not any(re.search(pattern, t) for pattern in forbidden)


def fallback_holds(text: str) -> bool:
    t = normalized(text)
    required = (
        "available, current, supported, and directly models the claim",
        "presumptively use it",
        "fall back for a concrete reason",
        "familiarity with grep/read/shell/tests is not itself a fallback reason",
    )
    if not all(item in t for item in required):
        return False
    forbidden = (
        r"\bfamiliarity with (?:built-in )?(?:grep/read/shell/tests|search/read/shell/tests)\b.{0,50}\b(?:is|counts as|is itself)\s+(?:a\s+)?(?:valid\s+)?fallback",
        r"\bprefer built-in (?:search|grep|read|shell|tests?)\b.{0,80}\binstead of\b",
        r"\bskip the specialized (?:tool|capability) merely because\b.{0,80}\bfamiliar",
    )
    return not any(re.search(pattern, t) for pattern in forbidden)


def codeql_optional_holds(text: str) -> bool:
    t = normalized(text)
    if "optional specialist analyzer, not a generic security gate" not in t:
        return False
    if "generic protocol validity does not require local codeql" not in t:
        return False
    forbidden = (
        r"\bgeneric protocol validity requires local codeql\b",
        r"\bcodeql (?:is|required to be) (?:required|run) for every (?:task|security task)\b",
        r"\brun codeql for every (?:task|security task)\b",
    )
    return not any(re.search(pattern, t) for pattern in forbidden)


def codeql_database_freshness_holds(text: str) -> bool:
    t = normalized(text)
    required = (
        "invalidate/rebuild",
        "changed source",
        "generated code",
        "build configuration",
        "dependency resolution",
        "do not reuse stale database results",
    )
    if not all(item in t for item in required):
        return False
    forbidden = (
        r"\breuse stale database results\b",
        r"\bstale database results (?:are|remain) (?:valid|acceptable)\b",
        r"\b(?:do not|need not|never need to) (?:invalidate|rebuild)\b.{0,120}\bchanged source\b",
        r"\bchanged source\b.{0,120}\b(?:does not require|need not require)\b.{0,40}\b(?:invalidate|rebuild)\b",
    )
    return not any(re.search(pattern, t) for pattern in forbidden)


def codeql_custom_query_validation_holds(text: str) -> bool:
    t = normalized(text)
    required = (
        "acceptance-critical custom query",
        "known-positive and known-negative",
        "before trusting its positive or zero result",
    )
    if not all(item in t for item in required):
        return False
    forbidden = (
        r"\bacceptance-critical custom quer(?:y|ies)\b.{0,100}\b(?:need not|do not need to|may skip)\b.{0,80}\bvalidat",
        r"\bcustom query\b.{0,120}\b(?:trusted|relied on) without\b.{0,80}\b(?:validation|known-positive|query test)\b",
        r"\bno (?:known-positive|known-negative|query test)\b.{0,80}\b(?:is|required)\b",
    )
    return not any(re.search(pattern, t) for pattern in forbidden)


def codeql_zero_scope_holds(text: str) -> bool:
    t = normalized(text)
    if "0 results or 0 alerts outcome is meaningful only relative to the actual database and query contract" not in t:
        return False
    if "zero findings are not proof of absence outside that contract" not in t:
        return False
    forbidden = (
        "zero findings are proof of absence outside that contract",
        "0 results prove absence everywhere",
        "0 alerts prove absence everywhere",
        "zero findings prove global absence",
    )
    return not any(item in t for item in forbidden)


def codeql_provenance_holds(text: str) -> bool:
    t = normalized(text)
    required = (
        "local/external codeql execution",
        "github-managed codeql execution",
        "github code-scanning result/alert surface",
        "uploading sarif from the same local codeql run does not create a second analyzer execution",
        "only a separately executed github-managed/ci analysis is an independent run",
        "that exact required check must execute on the intended candidate/configuration",
        "a local run does not silently substitute for a required github-managed check",
    )
    if not all(item in t for item in required):
        return False
    forbidden = (
        r"\buploading sarif\b.{0,120}\b(?:creates?|counts as|is)\b.{0,80}\bindependent (?:github-managed )?(?:execution|analysis|run)\b",
        r"\blocal (?:run|analysis)\b.{0,100}\b(?:substitutes?|may substitute|is sufficient)\b.{0,100}\brequired github-managed check\b",
        r"\b(?:stale|wrong-candidate|unrelated branch) hosted (?:result|evidence|alert)\b.{0,80}\b(?:is|remains|counts as) (?:valid|acceptable)\b",
    )
    return not any(re.search(pattern, t) for pattern in forbidden)


def codeql_build_trust_holds(text: str) -> bool:
    t = normalized(text)
    required = (
        "treat this as privileged execution",
        "trust, supply-chain, resource, and subprocess rules",
        "avoid executing untrusted build hooks without an appropriate trust decision",
        "bound cpu/ram/disk/wall time",
    )
    if not all(item in t for item in required):
        return False
    forbidden = (
        r"\b(?:may|can|should) execute untrusted build hooks without\b.{0,80}\btrust\b",
        r"\bcodeql (?:may|can) bypass\b.{0,80}\btrust\b",
        r"\bbuild hooks do not require\b.{0,80}\btrust\b",
    )
    return not any(re.search(pattern, t) for pattern in forbidden)


def compression_ownership_holds(owners: dict[str, str]) -> bool:
    design = normalized(owners["design"])
    implementation = normalized(owners["implementation"])
    common = normalized(owners["common"])
    workflow = normalized(owners["workflow"])

    for role in (design, implementation):
        for ref in ("tool-serena.md", "tool-semgrep.md", "tool-hypothesis.md", "tool-codeql.md"):
            if ref not in role:
                return False

    if "convergence-and-cycle-economy.md" not in workflow:
        return False

    tool_detail_markers = (
        ".semgrepignore",
        "health-check suppression",
        "database creation success is not product correctness evidence",
    )
    convergence_detail_markers = (
        "family membership is not textual similarity",
        "bounded closure basis",
    )
    if any(marker in design or marker in implementation for marker in tool_detail_markers + convergence_detail_markers):
        return False
    if any(marker in common for marker in tool_detail_markers):
        return False
    if any(marker in workflow for marker in convergence_detail_markers):
        return False
    return True


class Protocol513CounterfactualOracleTests(unittest.TestCase):
    def setUp(self) -> None:
        self.design = read("source/roles/software-design/SKILL.md")
        self.implementation = read("source/roles/software-implementation/SKILL.md")
        self.common = read("source/shared/references/tool-assisted-engineering.md")
        self.hypothesis = read("source/shared/references/tool-hypothesis.md")
        self.codeql = read("source/shared/references/tool-codeql.md")
        self.workflow = read("source/shared/references/workflow-and-workplans.md")

    def test_actual_canonical_source_is_governed_by_directional_oracles(self) -> None:
        for role in (self.design, self.implementation):
            self.assertTrue(dispatch_holds(role))
        self.assertTrue(relation_first_holds(self.common))
        self.assertTrue(fallback_holds(self.common))
        self.assertTrue(no_mandatory_pipeline_holds(self.common))
        self.assertTrue(hypothesis_anti_gaming_holds(self.hypothesis))
        self.assertTrue(hypothesis_settings_holds(self.hypothesis))
        self.assertTrue(codeql_optional_holds(self.codeql))
        self.assertTrue(codeql_database_freshness_holds(self.codeql))
        self.assertTrue(codeql_custom_query_validation_holds(self.codeql))
        self.assertTrue(codeql_zero_scope_holds(self.codeql))
        self.assertTrue(codeql_provenance_holds(self.codeql))
        self.assertTrue(codeql_build_trust_holds(self.codeql))
        self.assertTrue(
            compression_ownership_holds(
                {
                    "design": self.design,
                    "implementation": self.implementation,
                    "common": self.common,
                    "workflow": self.workflow,
                }
            )
        )

    def test_protocol_511_historical_pipeline_oracle_is_nonvacuous(self) -> None:
        check_pair(
            self,
            no_mandatory_pipeline_holds,
            "The tools can reinforce one another without becoming a mandatory three-tool pipeline.",
            "A mandatory three-tool pipeline is required.",
        )
        self.assertTrue(
            no_mandatory_pipeline_holds(
                "Serena, Semgrep, and Hypothesis may be combined when useful without becoming a mandatory three-tool pipeline."
            )
        )

    def test_protocol_511_hypothesis_anti_gaming_oracle_is_nonvacuous(self) -> None:
        positive = (
            "Do not use excessive filtering or assume, over-narrow strategies, exclusions, "
            "health-check suppression, disabled useful phases, removed deadlines, or reduced "
            "exploration solely to make a property green."
        )
        check_pair(
            self,
            hypothesis_anti_gaming_holds,
            positive,
            "Health-check suppression is permitted solely to make a property green.",
        )
        self.assertTrue(
            hypothesis_anti_gaming_holds(
                positive + " Filtering may still be used when the governed input contract genuinely requires it."
            )
        )

    def test_protocol_511_hypothesis_settings_oracle_is_nonvacuous(self) -> None:
        positive = "Change settings when project/test semantics justify it and required coverage remains intact."
        check_pair(
            self,
            hypothesis_settings_holds,
            positive,
            "Required coverage is optional.",
        )
        self.assertTrue(
            hypothesis_settings_holds(
                positive + " Keep default settings when project/test semantics do not justify a change."
            )
        )

    def test_dispatch_and_relation_first_oracles_reject_direct_inversions(self) -> None:
        dispatch = (
            "Classify each material engineering question by the relation under the claim, not once per task.\n"
            "- literal/path/text lookup or small deterministic local inspection -> ordinary repository search/read normally remains sufficient;\n"
            "- symbols -> MUST read references/tool-serena.md;\n"
            "- structure -> MUST read references/tool-semgrep.md;\n"
            "- broad Python state -> MUST read references/tool-hypothesis.md;\n"
            "- interprocedural flow -> MUST read references/tool-codeql.md."
        )
        check_pair(self, dispatch_holds, dispatch, "Classify once per task and use CodeQL for every question.")
        self.assertTrue(dispatch_holds(dispatch))

        relation = (
            "Classify the relation under the current material claim. A security task is not automatically a CodeQL task: "
            "a forbidden-call pattern is structural, while a source-to-dangerous-sink claim is interprocedural data flow. "
            "Decompose a multi-relation claim when practical."
        )
        check_pair(self, relation_first_holds, relation, "All security tasks always route to CodeQL.")

    def test_fallback_oracle_preserves_legitimate_boundary(self) -> None:
        positive = (
            "When the specialized capability is available, current, supported, and directly models the claim, presumptively use it. "
            "Fall back for a concrete reason such as unsupported language. Familiarity with Grep/Read/shell/tests is not itself a fallback reason."
        )
        check_pair(
            self,
            fallback_holds,
            positive,
            "Familiarity with Grep/Read/shell/tests is a valid fallback reason.",
        )
        self.assertTrue(
            fallback_holds(
                positive + " Fall back when the language is unsupported or the tool surface is unavailable."
            )
        )

    def test_codeql_optional_gate_oracle_preserves_project_required_boundary(self) -> None:
        positive = (
            "CodeQL is an optional specialist analyzer, not a generic security gate. Generic protocol validity does not require local CodeQL. "
            "Project/task authority may independently require CodeQL for a specific repository."
        )
        check_pair(self, codeql_optional_holds, positive, "Generic protocol validity requires local CodeQL.")
        self.assertTrue(codeql_optional_holds(positive))

    def test_codeql_database_oracle_rejects_stale_acceptance_and_allows_valid_reuse(self) -> None:
        positive = (
            "Invalidate/rebuild when changed source, generated code, build configuration, dependency resolution, or another relevant dimension can alter the relation. "
            "Do not reuse stale database results. Reuse is allowed when no relevant candidate/extraction/query dimension changed."
        )
        check_pair(self, codeql_database_freshness_holds, positive, "Reuse stale database results after changed source.")
        self.assertTrue(codeql_database_freshness_holds(positive))

    def test_codeql_custom_query_oracle_preserves_builtin_boundary(self) -> None:
        positive = (
            "For an acceptance-critical custom query, provide known-positive and known-negative validation before trusting its positive or zero result. "
            "Built-in or project-governed queries need not each receive bespoke fixtures unless their acceptance role independently requires it."
        )
        check_pair(
            self,
            codeql_custom_query_validation_holds,
            positive,
            "An acceptance-critical custom query may skip validation.",
        )
        self.assertTrue(codeql_custom_query_validation_holds(positive))

    def test_codeql_zero_result_oracle_rejects_overbroad_absence(self) -> None:
        positive = (
            "A 0 results or 0 alerts outcome is meaningful only relative to the actual database and query contract. "
            "Zero findings are not proof of absence outside that contract."
        )
        check_pair(self, codeql_zero_scope_holds, positive, "Zero findings are proof of absence outside that contract.")

    def test_codeql_provenance_oracle_rejects_each_independence_inversion(self) -> None:
        positive = (
            "Local/external CodeQL execution, GitHub-managed CodeQL execution, and the GitHub code-scanning result/alert surface are distinct. "
            "Uploading SARIF from the same local CodeQL run does not create a second analyzer execution. Only a separately executed GitHub-managed/CI analysis is an independent run. "
            "When project policy requires a hosted check, that exact required check must execute on the intended candidate/configuration; a local run does not silently substitute for a required GitHub-managed check. "
            "Local analysis remains sufficient when no hosted execution is required."
        )
        contradictions = (
            "Uploading SARIF creates independent GitHub-managed execution.",
            "A local run substitutes for a required GitHub-managed check.",
            "Stale hosted evidence is acceptable for the intended candidate.",
        )
        self.assertTrue(codeql_provenance_holds(positive))
        for contradiction in contradictions:
            with self.subTest(contradiction=contradiction):
                self.assertFalse(codeql_provenance_holds(positive + " " + contradiction))

    def test_codeql_build_trust_oracle_rejects_privilege_bypass(self) -> None:
        positive = (
            "Treat this as privileged execution under trust, supply-chain, resource, and subprocess rules. "
            "Avoid executing untrusted build hooks without an appropriate trust decision. Bound CPU/RAM/disk/wall time."
        )
        check_pair(
            self,
            codeql_build_trust_holds,
            positive,
            "CodeQL may execute untrusted build hooks without a trust decision.",
        )
        self.assertTrue(
            codeql_build_trust_holds(
                positive + " Trusted, authorized project build hooks may execute when required for extraction."
            )
        )

    def test_compression_ownership_oracle_is_source_scoped_and_nonvacuous(self) -> None:
        owners = {
            "design": "tool-serena.md tool-semgrep.md tool-hypothesis.md tool-codeql.md compact dispatch",
            "implementation": "tool-serena.md tool-semgrep.md tool-hypothesis.md tool-codeql.md compact dispatch",
            "common": "compact cross-tool policy",
            "workflow": "route detailed recurrence to convergence-and-cycle-economy.md",
        }
        self.assertTrue(compression_ownership_holds(owners))

        mutations = (
            ("design", " .semgrepignore detailed mechanics"),
            ("common", " database creation success is not product correctness evidence"),
            ("workflow", " family membership is not textual similarity"),
        )
        for key, extra in mutations:
            mutated = dict(owners)
            mutated[key] += extra
            with self.subTest(owner=key):
                self.assertFalse(compression_ownership_holds(mutated))

        # Generated distribution copies are intentionally outside this canonical-source ownership oracle.
        generated_copy = dict(owners)
        self.assertTrue(compression_ownership_holds(generated_copy))


if __name__ == "__main__":
    unittest.main()
