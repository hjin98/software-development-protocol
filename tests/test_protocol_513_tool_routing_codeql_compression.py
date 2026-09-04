from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

BASE_DESIGN_BYTES = 15823
BASE_IMPLEMENTATION_BYTES = 16265
BASE_WORKFLOW_BYTES = 26789


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def lower(path: str) -> str:
    return read(path).lower()


class Protocol513ToolRoutingCodeQLCompressionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.design = lower("source/roles/software-design/SKILL.md")
        self.implementation = lower("source/roles/software-implementation/SKILL.md")
        self.common = lower("source/shared/references/tool-assisted-engineering.md")
        self.serena = lower("source/shared/references/tool-serena.md")
        self.semgrep = lower("source/shared/references/tool-semgrep.md")
        self.hypothesis = lower("source/shared/references/tool-hypothesis.md")
        self.codeql = lower("source/shared/references/tool-codeql.md")
        self.workflow = lower("source/shared/references/workflow-and-workplans.md")
        self.convergence = lower("source/shared/references/convergence-and-cycle-economy.md")

    def test_version_is_513(self) -> None:
        self.assertEqual("5.13.0", read("source/PROTOCOL_VERSION").strip())
        self.assertIn("protocol 5.13", lower("source/shared/references/protocol-versioning-and-compatibility.md"))

    def test_dispatch_is_per_question_relation_first_and_direct(self) -> None:
        for text in (self.design, self.implementation):
            self.assertIn("classify each material engineering question", text)
            self.assertIn("relation under the claim", text)
            self.assertIn("literal/path/text", text)
            self.assertIn("tool-serena.md", text)
            self.assertIn("tool-semgrep.md", text)
            self.assertIn("tool-hypothesis.md", text)
            self.assertIn("tool-codeql.md", text)
            self.assertNotIn("when semantic repository navigation/editing, static/structural analysis, or property/stateful testing would materially improve", text)

    def test_trigger_requires_reference_entry_and_non_silent_disposition(self) -> None:
        for text in (self.design, self.implementation):
            for ref in ("tool-serena.md", "tool-semgrep.md", "tool-hypothesis.md", "tool-codeql.md"):
                line = next(line for line in text.splitlines() if ref in line)
                self.assertIn("must read", line)
            self.assertIn("cheap non-mutating capability probe", text)
            self.assertIn("presumptively use it", text)
            self.assertIn("concrete fallback", text)
            self.assertIn("familiarity with built-in", text)
            self.assertIn("not itself a fallback reason", text)

    def test_overlap_classification_is_relation_not_security_label(self) -> None:
        self.assertIn("security task is not automatically a codeql task", self.common)
        self.assertIn("forbidden-call pattern", self.common)
        self.assertIn("source-to-dangerous-sink", self.common)
        self.assertIn("task may activate several classes", self.common)
        self.assertIn("decompose a multi-relation claim", self.common)
        self.assertIn("minimum set of capabilities", self.common)

    def test_serena_semgrep_hypothesis_keep_distinct_positive_and_negative_cases(self) -> None:
        self.assertIn("prefer serena over repeated textual search", self.serena)
        self.assertIn("literal strings, filenames, configuration", self.serena)
        self.assertIn("do not route a purely literal lookup through semgrep", self.semgrep)
        self.assertIn("small deterministic examples and already-exhaustive finite cases do not require hypothesis", self.hypothesis)

    def test_codeql_is_dataflow_specialist_not_generic_security_gate(self) -> None:
        self.assertIn("interprocedural data-flow or taint-flow", self.codeql)
        self.assertIn("source-to-sink reachability", self.codeql)
        self.assertIn("optional specialist analyzer, not a generic security gate", self.codeql)
        self.assertIn("do not route a purely structural pattern to codeql", self.codeql)

    def test_codeql_provenance_distinguishes_execution_from_result_hosting(self) -> None:
        for phrase in (
            "local/external codeql execution",
            "github-managed codeql execution",
            "github code-scanning result/alert surface",
            "not automatically independent execution evidence",
            "uploading sarif from the same local codeql run does not create a second analyzer execution",
            "only a separately executed github-managed/ci analysis is an independent run",
        ):
            self.assertIn(phrase, self.codeql)

    def test_codeql_database_identity_invalidation_and_query_governance(self) -> None:
        for phrase in (
            "candidate/source identity",
            "build mode/build command",
            "query/query-suite/pack identity",
            "invalidate/rebuild",
            "changed source",
            "generated code",
            "build configuration",
            "dependency resolution",
            "stale database results",
            "known-positive and known-negative",
            "moving network-fetched query pack",
            "zero findings are not proof of absence outside that contract",
        ):
            self.assertIn(phrase, self.codeql)

    def test_codeql_build_and_hosted_analysis_obey_trust_and_resource_rules(self) -> None:
        for phrase in (
            "privileged execution",
            "trust, supply-chain, resource, and subprocess rules",
            "bound cpu/ram/disk/wall time",
            "do not upload source, sarif, findings, or credentials",
            "local analysis is the portability baseline",
        ):
            self.assertIn(phrase, self.codeql)

    def test_tool_common_owner_is_smaller_and_specific_methods_are_split(self) -> None:
        common_bytes = (ROOT / "source/shared/references/tool-assisted-engineering.md").stat().st_size
        self.assertLess(common_bytes, 10000)
        for rel in (
            "source/shared/references/tool-serena.md",
            "source/shared/references/tool-semgrep.md",
            "source/shared/references/tool-hypothesis.md",
            "source/shared/references/tool-codeql.md",
        ):
            self.assertTrue((ROOT / rel).is_file())

    def test_entrypoints_are_directionally_compressed_after_new_routing(self) -> None:
        design_bytes = (ROOT / "source/roles/software-design/SKILL.md").stat().st_size
        implementation_bytes = (ROOT / "source/roles/software-implementation/SKILL.md").stat().st_size
        self.assertLess(design_bytes + implementation_bytes, BASE_DESIGN_BYTES + BASE_IMPLEMENTATION_BYTES)

    def test_role_critical_workflow_surface_materially_decreases(self) -> None:
        workflow_bytes = (ROOT / "source/shared/references/workflow-and-workplans.md").stat().st_size
        self.assertLess(workflow_bytes, int(BASE_WORKFLOW_BYTES * 0.85))
        self.assertIn("convergence-and-cycle-economy.md", self.workflow)
        self.assertIn("semantic defect families", self.convergence)
        self.assertIn("review readiness", self.convergence)
        self.assertIn("revision", self.convergence)

    def test_loaded_context_scenarios_are_progressively_disclosed(self) -> None:
        # Ordinary implementation pays only for the entrypoint and role-critical workflow,
        # not every tool or convergence manual.
        ordinary = (ROOT / "source/roles/software-implementation/SKILL.md").stat().st_size + (
            ROOT / "source/shared/references/workflow-and-workplans.md"
        ).stat().st_size
        serena_task = ordinary + (ROOT / "source/shared/references/tool-serena.md").stat().st_size
        recurrence_task = ordinary + (ROOT / "source/shared/references/convergence-and-cycle-economy.md").stat().st_size
        all_tool_manuals = sum(
            (ROOT / f"source/shared/references/{name}").stat().st_size
            for name in ("tool-serena.md", "tool-semgrep.md", "tool-hypothesis.md", "tool-codeql.md")
        )
        self.assertLess(serena_task, ordinary + all_tool_manuals)
        self.assertGreater(recurrence_task, ordinary)
        self.assertNotIn("semantic defect families", self.implementation)

    def test_convergence_extraction_preserves_hard_trigger(self) -> None:
        self.assertIn("first clean local defect remains local", self.workflow)
        self.assertIn("material sibling recurrence", self.workflow)
        self.assertIn("convergence-and-cycle-economy.md", self.workflow)
        self.assertIn("no recurrence/review count can force acceptance", self.workflow)

    def test_no_mandatory_multi_tool_pipeline_or_generic_github_dependency(self) -> None:
        self.assertIn("without becoming a **mandatory three-tool pipeline**", read("source/shared/references/tool-assisted-engineering.md"))
        self.assertIn("generic protocol validity does not require local codeql, github", self.codeql)
        self.assertIn("tool absence does not relax family closure", self.common)


if __name__ == "__main__":
    unittest.main()
