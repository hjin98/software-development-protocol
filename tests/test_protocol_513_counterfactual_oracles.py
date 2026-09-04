from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def norm(text: str) -> str:
    return text.lower().replace("**", "").replace("`", "")


def directional(text: str, required: tuple[str, ...], forbidden: tuple[str, ...]) -> bool:
    value = norm(text)
    return all(item in value for item in required) and not any(item in value for item in forbidden)


def check_pair(test: unittest.TestCase, predicate, positive: str, contradiction: str) -> None:
    test.assertTrue(predicate(positive), f"positive rejected by {predicate.__name__}")
    test.assertFalse(
        predicate(positive + " " + contradiction),
        f"contradiction accepted by {predicate.__name__}",
    )


def pipeline_holds(text: str) -> bool:
    return directional(
        text,
        ("without becoming a mandatory three-tool pipeline",),
        (
            "a mandatory three-tool pipeline is required",
            "form a mandatory three-tool pipeline",
            "must use a mandatory three-tool pipeline",
        ),
    )


ANTI_GAMING = (
    "excessive filtering",
    "assume",
    "over-narrow strategies",
    "exclusions",
    "health-check suppression",
    "disabled useful phases",
    "removed deadlines",
    "reduced exploration",
)


def hypothesis_anti_gaming_holds(text: str) -> bool:
    value = norm(text)
    if "do not use" not in value or "solely to make a property green" not in value:
        return False
    if not all(item in value for item in ANTI_GAMING):
        return False
    for item in ANTI_GAMING:
        if any(
            phrase in value
            for phrase in (
                f"{item} is permitted solely to make a property green",
                f"{item} may be used solely to make a property green",
                f"{item} are allowed solely to make a property green",
                f"{item} is allowed solely to make a property green",
            )
        ):
            return False
    return True


def hypothesis_settings_holds(text: str) -> bool:
    return directional(
        text,
        (
            "change settings when project/test semantics justify it",
            "required coverage remains intact",
        ),
        (
            "required coverage is optional",
            "required coverage need not remain intact",
            "change settings when project/test semantics do not justify it",
            "change settings even when project/test semantics do not justify it",
        ),
    )


def dispatch_holds(text: str) -> bool:
    value = norm(text)
    required = (
        "classify each material engineering question",
        "relation under the claim",
        "not once per task",
        "literal/path/text lookup or small deterministic local inspection",
        "ordinary repository search/read normally remains sufficient",
        "tool-serena.md",
        "tool-semgrep.md",
        "tool-hypothesis.md",
        "tool-codeql.md",
    )
    if not all(item in value for item in required):
        return False
    for ref in ("tool-serena.md", "tool-semgrep.md", "tool-hypothesis.md", "tool-codeql.md"):
        line = next((line for line in value.splitlines() if ref in line), "")
        if "must read" not in line:
            return False
    literal = next((line for line in value.splitlines() if "literal/path/text" in line), "")
    if "must read" in literal:
        return False
    return not any(
        item in value
        for item in (
            "classify once per task",
            "classify the task once",
            "choose one tool for the entire task",
            "use codeql for every question",
            "literal/path/text lookup must read codeql",
        )
    )


def relation_first_holds(text: str) -> bool:
    return directional(
        text,
        (
            "relation under the current material claim",
            "security task is not automatically a codeql task",
            "forbidden-call pattern is structural",
            "source-to-dangerous-sink claim is interprocedural data flow",
            "decompose a multi-relation claim",
        ),
        (
            "all security tasks always route to codeql",
            "security always means codeql",
            "a forbidden-call pattern is codeql",
            "a source-to-dangerous-sink claim is semgrep",
        ),
    )


def fallback_holds(text: str) -> bool:
    return directional(
        text,
        (
            "available, current, supported, and directly models the claim",
            "presumptively use it",
            "fall back for a concrete reason",
            "familiarity with grep/read/shell/tests is not itself a fallback reason",
        ),
        (
            "familiarity with grep/read/shell/tests is a valid fallback reason",
            "familiarity with built-in search/read/shell/tests is a valid fallback reason",
            "skip the specialized capability merely because built-in tools are familiar",
        ),
    )


def codeql_optional_holds(text: str) -> bool:
    return directional(
        text,
        (
            "optional specialist analyzer, not a generic security gate",
            "generic protocol validity does not require local codeql",
        ),
        (
            "generic protocol validity requires local codeql",
            "codeql is required for every task",
            "codeql is required for every security task",
            "run codeql for every security task",
        ),
    )


def codeql_database_holds(text: str) -> bool:
    return directional(
        text,
        (
            "invalidate/rebuild",
            "changed source",
            "generated code",
            "build configuration",
            "dependency resolution",
            "do not reuse stale database results",
        ),
        (
            "reuse stale database results after changed source",
            "stale database results are acceptable",
            "stale database results remain valid",
            "changed source does not require invalidation",
            "changed source does not require rebuild",
        ),
    )


def codeql_custom_query_holds(text: str) -> bool:
    return directional(
        text,
        (
            "acceptance-critical custom query",
            "known-positive and known-negative",
            "before trusting its positive or zero result",
        ),
        (
            "an acceptance-critical custom query may skip validation",
            "an acceptance-critical custom query needs no validation",
            "trust an acceptance-critical custom query without validation",
        ),
    )


def codeql_zero_holds(text: str) -> bool:
    return directional(
        text,
        (
            "0 results or 0 alerts outcome is meaningful only relative to the actual database and query contract",
            "zero findings are not proof of absence outside that contract",
        ),
        (
            "zero findings are proof of absence outside that contract",
            "0 results prove absence everywhere",
            "0 alerts prove absence everywhere",
            "zero findings prove global absence",
        ),
    )


def codeql_provenance_holds(text: str) -> bool:
    return directional(
        text,
        (
            "local/external codeql execution",
            "github-managed codeql execution",
            "github code-scanning result/alert surface",
            "uploading sarif from the same local codeql run does not create a second analyzer execution",
            "only a separately executed github-managed/ci analysis is an independent run",
            "that exact required check must execute on the intended candidate/configuration",
            "a local run does not silently substitute for a required github-managed check",
        ),
        (
            "uploading sarif creates independent github-managed execution",
            "uploading sarif counts as independent github-managed execution",
            "a local run substitutes for a required github-managed check",
            "local analysis substitutes for a required github-managed check",
            "stale hosted evidence is acceptable",
            "wrong-candidate hosted evidence is acceptable",
        ),
    )


def codeql_build_trust_holds(text: str) -> bool:
    return directional(
        text,
        (
            "treat this as privileged execution",
            "trust, supply-chain, resource, and subprocess rules",
            "avoid executing untrusted build hooks without an appropriate trust decision",
            "bound cpu/ram/disk/wall time",
        ),
        (
            "codeql may execute untrusted build hooks without a trust decision",
            "codeql can bypass trust rules for build hooks",
            "build hooks do not require a trust decision",
        ),
    )


def compression_ownership_holds(owners: dict[str, str]) -> bool:
    design = norm(owners["design"])
    implementation = norm(owners["implementation"])
    common = norm(owners["common"])
    workflow = norm(owners["workflow"])
    for role in (design, implementation):
        if not all(ref in role for ref in ("tool-serena.md", "tool-semgrep.md", "tool-hypothesis.md", "tool-codeql.md")):
            return False
    if "convergence-and-cycle-economy.md" not in workflow:
        return False
    tool_detail = (
        ".semgrepignore",
        "health-check suppression",
        "database creation success is not product correctness evidence",
    )
    convergence_detail = (
        "family membership is not textual similarity",
        "bounded closure basis",
    )
    if any(marker in design or marker in implementation for marker in tool_detail + convergence_detail):
        return False
    if any(marker in common for marker in tool_detail):
        return False
    if any(marker in workflow for marker in convergence_detail):
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

    def test_actual_canonical_source_is_linked_to_every_directional_oracle(self) -> None:
        for role in (self.design, self.implementation):
            self.assertTrue(dispatch_holds(role))
        self.assertTrue(relation_first_holds(self.common))
        self.assertTrue(fallback_holds(self.common))
        self.assertTrue(pipeline_holds(self.common))
        self.assertTrue(hypothesis_anti_gaming_holds(self.hypothesis))
        self.assertTrue(hypothesis_settings_holds(self.hypothesis))
        self.assertTrue(codeql_optional_holds(self.codeql))
        self.assertTrue(codeql_database_holds(self.codeql))
        self.assertTrue(codeql_custom_query_holds(self.codeql))
        self.assertTrue(codeql_zero_holds(self.codeql))
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

    def test_protocol_511_pipeline_polarity_and_optional_composition(self) -> None:
        positive = "The tools can reinforce one another without becoming a mandatory three-tool pipeline."
        check_pair(self, pipeline_holds, positive, "A mandatory three-tool pipeline is required.")
        self.assertTrue(pipeline_holds(positive + " Combine tools when that materially improves evidence."))

    def test_protocol_511_hypothesis_anti_gaming_polarity(self) -> None:
        positive = (
            "Do not use excessive filtering or assume, over-narrow strategies, exclusions, health-check suppression, "
            "disabled useful phases, removed deadlines, or reduced exploration solely to make a property green."
        )
        self.assertTrue(hypothesis_anti_gaming_holds(positive))
        for mechanism in ANTI_GAMING:
            with self.subTest(mechanism=mechanism):
                self.assertFalse(
                    hypothesis_anti_gaming_holds(
                        positive + f" {mechanism} may be used solely to make a property green."
                    )
                )
        self.assertTrue(
            hypothesis_anti_gaming_holds(
                positive + " Filtering may be used when the governed domain contract genuinely requires it."
            )
        )

    def test_protocol_511_hypothesis_settings_polarity_and_boundary(self) -> None:
        positive = "Change settings when project/test semantics justify it and required coverage remains intact."
        check_pair(self, hypothesis_settings_holds, positive, "Required coverage is optional.")
        self.assertTrue(
            hypothesis_settings_holds(
                positive + " Keep default settings when project/test semantics do not justify a change."
            )
        )

    def test_dispatch_polarity_preserves_ordinary_local_work(self) -> None:
        positive = (
            "Classify each material engineering question by the relation under the claim, not once per task.\n"
            "- literal/path/text lookup or small deterministic local inspection -> ordinary repository search/read normally remains sufficient;\n"
            "- symbols -> MUST read references/tool-serena.md;\n"
            "- structure -> MUST read references/tool-semgrep.md;\n"
            "- broad Python state -> MUST read references/tool-hypothesis.md;\n"
            "- interprocedural flow -> MUST read references/tool-codeql.md."
        )
        check_pair(self, dispatch_holds, positive, "Classify once per task and use CodeQL for every question.")
        self.assertTrue(dispatch_holds(positive))

    def test_relation_first_overlap_polarity(self) -> None:
        positive = (
            "Classify the relation under the current material claim. A security task is not automatically a CodeQL task: "
            "a forbidden-call pattern is structural, while a source-to-dangerous-sink claim is interprocedural data flow. "
            "Decompose a multi-relation claim when practical."
        )
        check_pair(self, relation_first_holds, positive, "All security tasks always route to CodeQL.")

    def test_fallback_polarity_preserves_concrete_fallbacks(self) -> None:
        positive = (
            "When the specialized capability is available, current, supported, and directly models the claim, presumptively use it. "
            "Fall back for a concrete reason such as unsupported language. Familiarity with Grep/Read/shell/tests is not itself a fallback reason."
        )
        check_pair(self, fallback_holds, positive, "Familiarity with Grep/Read/shell/tests is a valid fallback reason.")
        self.assertTrue(fallback_holds(positive + " An unsupported language remains a valid concrete fallback."))

    def test_codeql_optional_gate_preserves_project_specific_requirements(self) -> None:
        positive = (
            "CodeQL is an optional specialist analyzer, not a generic security gate. Generic protocol validity does not require local CodeQL. "
            "Project/task authority may independently require CodeQL for a specific repository."
        )
        check_pair(self, codeql_optional_holds, positive, "Generic protocol validity requires local CodeQL.")

    def test_codeql_database_polarity_preserves_unchanged_reuse(self) -> None:
        positive = (
            "Invalidate/rebuild when changed source, generated code, build configuration, dependency resolution, or another relevant dimension can alter the relation. "
            "Do not reuse stale database results. Reuse is allowed when no relevant candidate/extraction/query dimension changed."
        )
        check_pair(self, codeql_database_holds, positive, "Reuse stale database results after changed source.")
        self.assertTrue(codeql_database_holds(positive))

    def test_custom_query_validation_preserves_builtin_boundary(self) -> None:
        positive = (
            "For an acceptance-critical custom query, provide known-positive and known-negative validation before trusting its positive or zero result. "
            "Built-in or project-governed queries do not automatically require bespoke fixtures."
        )
        check_pair(self, codeql_custom_query_holds, positive, "An acceptance-critical custom query may skip validation.")

    def test_zero_result_scope_polarity(self) -> None:
        positive = (
            "A 0 results or 0 alerts outcome is meaningful only relative to the actual database and query contract. "
            "Zero findings are not proof of absence outside that contract."
        )
        check_pair(self, codeql_zero_holds, positive, "Zero findings are proof of absence outside that contract.")

    def test_codeql_provenance_rejects_all_required_inversions(self) -> None:
        positive = (
            "Local/external CodeQL execution, GitHub-managed CodeQL execution, and the GitHub code-scanning result/alert surface are distinct. "
            "Uploading SARIF from the same local CodeQL run does not create a second analyzer execution. Only a separately executed GitHub-managed/CI analysis is an independent run. "
            "When project policy requires a hosted check, that exact required check must execute on the intended candidate/configuration; a local run does not silently substitute for a required GitHub-managed check. "
            "Local analysis may be sufficient when no hosted execution is required."
        )
        self.assertTrue(codeql_provenance_holds(positive))
        for contradiction in (
            "Uploading SARIF creates independent GitHub-managed execution.",
            "A local run substitutes for a required GitHub-managed check.",
            "Stale hosted evidence is acceptable.",
            "Wrong-candidate hosted evidence is acceptable.",
        ):
            with self.subTest(contradiction=contradiction):
                self.assertFalse(codeql_provenance_holds(positive + " " + contradiction))

    def test_codeql_build_trust_polarity_preserves_authorized_builds(self) -> None:
        positive = (
            "Treat this as privileged execution under trust, supply-chain, resource, and subprocess rules. "
            "Avoid executing untrusted build hooks without an appropriate trust decision. Bound CPU/RAM/disk/wall time."
        )
        check_pair(self, codeql_build_trust_holds, positive, "CodeQL may execute untrusted build hooks without a trust decision.")
        self.assertTrue(
            codeql_build_trust_holds(
                positive + " Trusted, authorized project build hooks may execute when extraction requires them."
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
        for key, extra in (
            ("design", " .semgrepignore detailed mechanics"),
            ("common", " database creation success is not product correctness evidence"),
            ("workflow", " family membership is not textual similarity"),
        ):
            mutated = dict(owners)
            mutated[key] += extra
            with self.subTest(owner=key):
                self.assertFalse(compression_ownership_holds(mutated))
        # Generated dist copies are intentionally outside the canonical source ownership predicate.
        self.assertTrue(compression_ownership_holds(dict(owners)))


if __name__ == "__main__":
    unittest.main()
