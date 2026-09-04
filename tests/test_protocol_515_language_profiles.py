from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


class Protocol515LanguageProfileTests(unittest.TestCase):
    def setUp(self) -> None:
        self.router = read("source/shared/references/language-profiles.md").lower()
        self.python = read("source/shared/references/python-engineering.md").lower()
        self.cpp = read("source/shared/references/cpp-engineering.md").lower()
        self.performance = read("source/shared/references/performance-and-parallelism.md").lower()
        self.concurrency = read("source/shared/references/concurrency-and-orchestration.md").lower()
        self.tools = read("source/shared/references/tool-assisted-engineering.md").lower()
        self.security = read("source/shared/references/security-and-trust-boundaries.md").lower()
        self.design = read("source/roles/software-design/SKILL.md").lower()
        self.implementation = read("source/roles/software-implementation/SKILL.md").lower()
        self.build = read("source/build_skills.py")

    def test_shared_profile_precedence_and_mixed_composition(self) -> None:
        self.assertIn("shared domain rule -> active language profile(s) -> implementation-local realization", self.router)
        self.assertIn("do not infer a global python-over-c++ or c++-over-python precedence", self.router)
        self.assertIn("shared owners remain canonical", self.router)
        self.assertIn("mixed python/c++ boundaries", self.router)
        self.assertIn("must read both", self.router)

    def test_material_executable_work_routes_deterministically(self) -> None:
        for text in (self.design, self.implementation):
            self.assertIn("language-profile dispatch", text)
            self.assertIn("must read", text)
            self.assertIn("references/language-profiles.md", text)
            self.assertIn("references/python-engineering.md", text)
            self.assertIn("references/cpp-engineering.md", text)
        self.assertIn("tiny literal/text/config-only", self.implementation)

    def test_profiles_are_role_only_package_payload(self) -> None:
        self.assertIn('LANGUAGE_PROFILES = [', self.build)
        self.assertIn('"language-profiles.md"', self.build)
        self.assertIn('"python-engineering.md"', self.build)
        self.assertIn('"cpp-engineering.md"', self.build)
        role_block = self.build.split("ROLE_SPECS =", 1)[1].split("SPECIALIST_SPECS =", 1)[0]
        specialist_block = self.build.split("SPECIALIST_SPECS =", 1)[1]
        self.assertIn("LANGUAGE_PROFILES", role_block)
        self.assertNotIn("LANGUAGE_PROFILES", specialist_block)

    def test_python_profile_is_language_native_and_runtime_sensitive(self) -> None:
        for phrase in (
            "context managers",
            "iterators, generators, streaming",
            "c++-in-python",
            "numpy.vectorize",
            "bounded orchestration loops",
            "actual supported interpreter/runtime mode",
            "free-threaded cpython",
            "asynchronous/event-loop",
            "os.cpu_count()",
            "hypothesis",
        ):
            self.assertIn(phrase, self.python)
        self.assertIn("do not assume one universal python threading model", self.python)
        self.assertIn("distributed-memory/mpi execution is an architecture capability, not a c++ feature", self.python)

    def test_cpp_profile_covers_native_design_and_correctness(self) -> None:
        for phrase in (
            "raii",
            "value semantics",
            "raw owning pointers",
            "python-in-c++",
            "c++ cleverness for its own sake",
            "compilation database",
            "undefined behavior",
            "data races",
            "blas/lapack",
            "fftw",
            "optimized baseline",
            "avx-512",
            "openmp",
            "mpi-class",
        ):
            self.assertIn(phrase, self.cpp)
        self.assertIn("required behavior must not depend on assertions or validation compiled out in production", self.cpp)

    def test_cpp_high_return_tool_stack_is_claim_directed(self) -> None:
        for phrase in (
            "serena",
            "clangd",
            "semgrep",
            "codeql",
            "clang-tidy",
            "asan",
            "ubsan",
            "tsan",
            "msan",
            "gdb/lldb",
            "libfuzzer/afl++",
            "sampling profiling",
            "hardware counters",
        ):
            self.assertIn(phrase, self.cpp)
        self.assertIn("not a mandatory pipeline", self.cpp)
        self.assertIn("exact tool names remain delegated", self.cpp)

    def test_performance_owner_is_language_agnostic(self) -> None:
        for phrase in (
            "efficiency by construction",
            "complexity escalation",
            "optimized kernels and vectorized/compiled execution",
            "effective resource discovery",
            "asynchronous/event-driven",
            "shared-memory concurrency",
            "process isolation",
            "distributed memory",
            "gpu/accelerator policy",
            "quantitative speedup",
        ):
            self.assertIn(phrase, self.performance)
        self.assertIn("hardware_concurrency()", self.performance)
        self.assertIn("os.cpu_count()", self.performance)
        self.assertIn("debug/sanitizer versus production", self.performance)

    def test_parallelism_classes_are_shared_not_cpp_only(self) -> None:
        for phrase in (
            "asynchronous/event-driven",
            "shared-memory concurrency",
            "process isolation",
            "distributed-memory execution",
            "accelerator execution",
            "nested runtimes",
        ):
            self.assertIn(phrase, self.concurrency)
        self.assertIn("mpi is a common realization from both python and c++", self.concurrency)

    def test_property_route_is_generic_then_language_specific(self) -> None:
        self.assertIn("broad/combinatorial input/state invariant -> language-appropriate property/generative method", self.tools)
        self.assertIn("python normally routes this question to hypothesis", self.tools)
        self.assertIn("c++ routes to a project-appropriate property/generative framework", self.tools)
        self.assertIn("fuzzing and semantic property testing are not interchangeable", self.tools)

    def test_security_owner_is_generic_with_language_examples(self) -> None:
        self.assertIn("prefer direct argument-vector/process apis over shell command construction", self.security)
        self.assertIn("shell=false", self.security)
        self.assertIn("one api-specific example", self.security)
        self.assertIn("python `pickle`/`shelve`", self.security)
        self.assertIn("examples of this generic rule", self.security)
        self.assertIn("compiler", self.security)
        self.assertIn("native extension", self.security)

    def test_gpu_is_architecture_gated_in_shared_and_profiles(self) -> None:
        self.assertIn("dormant unless accelerator support is a tier-1 requirement or explicitly frozen architecture decision", self.performance)
        self.assertIn("gpu/accelerator work is dormant unless", self.cpp)
        self.assertNotIn("cuda", self.python)  # Python profile does not force a GPU framework.

    def test_language_boundary_requires_total_path_reasoning(self) -> None:
        for phrase in (
            "one clear owner",
            "zero-copy",
            "batch calls",
            "exception/error translation",
            "end-to-end performance evidence",
            "installed/packaged extension",
        ):
            self.assertIn(phrase, self.router)
        self.assertIn("design-level decision", self.router)

    def test_quantitative_performance_claims_require_measurement(self) -> None:
        self.assertIn("no quantitative speedup or scaling claim may be made without representative measurement", self.router)
        self.assertIn("quantitative speedup/scaling/resource claim", self.performance)
        self.assertIn("quantitative speedup/scaling/resource claims require representative comparable measurement", self.implementation)

    def test_version_binding_and_repository_local_python_are_preserved(self) -> None:
        versioning = read("source/shared/references/protocol-versioning-and-compatibility.md").lower()
        root_readme = read("README.md").lower()
        self.assertIn("protocol 5.15 is a backward-compatible", versioning)
        self.assertIn("active older workplans do not automatically adopt protocol 5.15", versioning)
        self.assertIn("repository-local tier-2 validation machinery", root_readme)
        workplan = read("workplans/active/PROTOCOL-5.15-LANGUAGE-PROFILES-CPP-PERFORMANCE.md")
        self.assertIn("protocol_version: 5.14.0", workplan)


if __name__ == "__main__":
    unittest.main()
