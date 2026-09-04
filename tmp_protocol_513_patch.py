from pathlib import Path

path = Path('tests/test_protocol_513_oracle_family_closure.py')
text = path.read_text(encoding='utf-8')


def replace(old: str, new: str) -> None:
    global text
    if old not in text:
        raise SystemExit(f'missing patch anchor:\n{old}')
    text = text.replace(old, new, 1)


old = '''ROUTE_CASES = (
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
'''
replace(old, old + '''\nSPECIALIST_TARGETS = tuple(\n    target for name, _anchor, target in ROUTE_CASES if name != "ordinary"\n)\n''')

replace(
'''    for name, anchor, target in ROUTE_CASES:
        line = route_line(section, anchor)
        if not line or target not in line:
            return False
        if name == "ordinary":
            if "must read" in line or "references/tool-" in line:
                return False
        elif "must read" not in line:
            return False
''',
'''    for name, anchor, target in ROUTE_CASES:
        line = route_line(section, anchor)
        if not line or target not in line:
            return False
        specialist_targets = [ref for ref in SPECIALIST_TARGETS if ref in line]
        if name == "ordinary":
            if "must read" in line or specialist_targets:
                return False
        elif (
            "must read" not in line
            or specialist_targets != [target]
            or line.count(target) != 1
        ):
            return False
''')

replace(
'''    forbidden = (
        "never probe unknown availability",
        "assume the specialized capability is unavailable without checking",
        "silently assume the specialized capability is unavailable",
        "default to ordinary tools without checking",
        "familiarity with built-in search/read/shell/test tools is a valid fallback reason",
        "familiarity with grep/read/shell/tests is a valid fallback reason",
    )
''',
'''    forbidden = (
        "never probe unknown availability",
        "assume the specialized capability is unavailable without checking",
        "silently assume the specialized capability is unavailable",
        "default to ordinary tools without checking",
        "familiarity with built-in search/read/shell/test tools is a valid fallback reason",
        "familiarity with grep/read/shell/tests is a valid fallback reason",
        "may be skipped without a concrete permitted reason",
        "may be skipped without a concrete fallback",
        "may be skipped for no concrete reason",
        "skip it without a concrete permitted reason",
        "skip it without a concrete fallback",
        "always probe even when availability is already known",
        "must always probe even when availability is already known",
        "must probe even when no safe practical cheap probe exists",
        "must probe even when no safe/practical cheap probe exists",
        "always probe even when no safe practical cheap probe exists",
    )
''')

replace(
'''    forbidden = (
        "security always means codeql",
        "all security tasks always route to codeql",
        "a forbidden-call pattern must use codeql",
        "source-to-sink is merely structural and should use semgrep",
    )
''',
'''    forbidden = (
        "security always means codeql",
        "all security tasks always route to codeql",
        "a forbidden-call pattern must use codeql",
        "a forbidden-call pattern must use codeql solely because it is security",
        "source-to-sink is merely structural and should use semgrep",
    )
''')

replace(
'''    forbidden = (
        "specialized analyzer output is exhaustive",
        "specialist output is exhaustive",
        "never needs material cross-checking",
        "never needs cross-checking",
    )
''',
'''    forbidden = (
        "specialized analyzer output is exhaustive",
        "specialist output is exhaustive",
        "never needs material cross-checking",
        "never needs cross-checking",
        "a duplicate analyzer pass is required even when no material blind spot exists",
        "always perform a duplicate analyzer pass even when no material blind spot exists",
        "always cross-check even when no material blind spot exists",
    )
''')

replace(
'''    required_by_name = {
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
''',
'''    required_by_name = {
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
    forbidden_by_name = {
        "serena": (
            "literal strings, filenames, configuration, generated/external surfaces must use serena",
            "serena is required for unsupported language constructs",
        ),
        "semgrep": (
            "semgrep may substitute for interprocedural/data-flow analysis",
            "a purely literal lookup must use semgrep",
        ),
        "hypothesis": (
            "small deterministic examples and already-exhaustive finite cases require hypothesis",
            "a triggered broad/combinatorial state or input case may skip hypothesis without a concrete fallback",
        ),
        "codeql": (
            "a purely structural pattern must use codeql solely because it is security",
            "a security task always requires codeql",
        ),
    }
    return all(item in value for item in required_by_name[name]) and not any(
        item in value for item in forbidden_by_name[name]
    )
''')

replace(
'''    def test_actual_role_direct_entry_mutation_is_rejected(self) -> None:
''',
'''    def test_actual_role_route_rows_reject_additive_wrong_targets(self) -> None:
        mutations = (
            (
                "ordinary-plus-codeql",
                "ordinary repository search/read normally remains sufficient;",
                "ordinary repository search/read normally remains sufficient; "
                "**MUST read** [CodeQL](references/tool-codeql.md);",
            ),
            (
                "serena-plus-semgrep",
                "references/tool-serena.md)",
                "references/tool-serena.md) and **MUST read** [Semgrep](references/tool-semgrep.md)",
            ),
            (
                "semgrep-plus-codeql",
                "references/tool-semgrep.md);",
                "references/tool-semgrep.md) and **MUST read** [CodeQL](references/tool-codeql.md);",
            ),
            (
                "hypothesis-plus-serena",
                "references/tool-hypothesis.md);",
                "references/tool-hypothesis.md) and **MUST read** [Serena](references/tool-serena.md);",
            ),
            (
                "codeql-plus-semgrep",
                "references/tool-codeql.md).",
                "references/tool-codeql.md) and **MUST read** [Semgrep](references/tool-semgrep.md).",
            ),
        )
        for role_name, role in self.roles.items():
            for mutation_name, old, new in mutations:
                mutated = replace_once(role, old, new)
                with self.subTest(role=role_name, mutation=mutation_name):
                    self.assertFalse(route_map_holds(mutated))

    def test_actual_role_direct_entry_mutation_is_rejected(self) -> None:
''')

replace(
'''            fallback_mutation = mutate_paragraph(
                role,
                "when a specialized trigger fires and availability is unknown",
                "Familiarity with built-in search/read/shell/test tools is a valid fallback reason.",
            )
            with self.subTest(role=role_name, mutation="probe"):
                self.assertFalse(capability_disposition_holds(probe_mutation))
            with self.subTest(role=role_name, mutation="fallback"):
                self.assertFalse(capability_disposition_holds(fallback_mutation))
''',
'''            fallback_mutation = mutate_paragraph(
                role,
                "when a specialized trigger fires and availability is unknown",
                "Familiarity with built-in search/read/shell/test tools is a valid fallback reason.",
            )
            arbitrary_skip_mutation = mutate_paragraph(
                role,
                "when a specialized trigger fires and availability is unknown",
                "An available/current/supported capability that directly models the claim may be skipped without a concrete permitted reason.",
            )
            with self.subTest(role=role_name, mutation="probe"):
                self.assertFalse(capability_disposition_holds(probe_mutation))
            with self.subTest(role=role_name, mutation="fallback"):
                self.assertFalse(capability_disposition_holds(fallback_mutation))
            with self.subTest(role=role_name, mutation="arbitrary-skip"):
                self.assertFalse(capability_disposition_holds(arbitrary_skip_mutation))
''')

replace(
'''            with self.subTest(role=role_name):
                self.assertTrue(capability_disposition_holds(boundary))
''',
'''            overprobe = mutate_paragraph(
                role,
                "when a specialized trigger fires and availability is unknown",
                "Always probe even when availability is already known or no safe practical cheap probe exists.",
            )
            with self.subTest(role=role_name, boundary="valid"):
                self.assertTrue(capability_disposition_holds(boundary))
            with self.subTest(role=role_name, boundary="overprobe"):
                self.assertFalse(capability_disposition_holds(overprobe))
''')

replace(
'''        model_mutation = mutate_paragraph(
            self.common,
            "specialized tools are bounded models",
            "Specialized analyzer output is exhaustive and never needs material cross-checking.",
        )
        pipeline_mutation = mutate_paragraph(
''',
'''        structural_security_mutation = mutate_paragraph(
            self.common,
            "security task is not automatically a codeql task",
            "A forbidden-call pattern must use CodeQL solely because it is security.",
        )
        model_mutation = mutate_paragraph(
            self.common,
            "specialized tools are bounded models",
            "Specialized analyzer output is exhaustive and never needs material cross-checking.",
        )
        pipeline_mutation = mutate_paragraph(
''')

replace(
'''        self.assertFalse(common_relation_policy_holds(overlap_mutation))
        self.assertFalse(model_limit_policy_holds(model_mutation))
''',
'''        self.assertFalse(common_relation_policy_holds(overlap_mutation))
        self.assertFalse(common_relation_policy_holds(structural_security_mutation))
        self.assertFalse(model_limit_policy_holds(model_mutation))
''')

replace(
'''        boundary = mutate_paragraph(
            self.common,
            "specialized tools are bounded models",
            "When no material model blind spot exists, no redundant duplicate analyzer pass is required.",
        )
        self.assertTrue(model_limit_policy_holds(boundary))

    def test_specialist_selection_boundaries_are_live(self) -> None:
        for name, text in self.specialists.items():
            with self.subTest(tool=name):
                self.assertTrue(specialist_owner_holds(name, text))
''',
'''        boundary = mutate_paragraph(
            self.common,
            "specialized tools are bounded models",
            "When no material model blind spot exists, no redundant duplicate analyzer pass is required.",
        )
        overconstraint = mutate_paragraph(
            self.common,
            "specialized tools are bounded models",
            "A duplicate analyzer pass is required even when no material blind spot exists.",
        )
        self.assertTrue(model_limit_policy_holds(boundary))
        self.assertFalse(model_limit_policy_holds(overconstraint))

    def test_specialist_selection_boundaries_are_live(self) -> None:
        mutations = {
            "serena": (
                "literal strings, filenames, configuration, generated/external surfaces",
                "Literal strings, filenames, configuration, generated/external surfaces must use Serena.",
            ),
            "semgrep": (
                "do not route a purely literal lookup through semgrep",
                "Semgrep may substitute for interprocedural/data-flow analysis.",
            ),
            "hypothesis": (
                "small deterministic examples and already-exhaustive finite cases",
                "Small deterministic examples and already-exhaustive finite cases require Hypothesis.",
            ),
            "codeql": (
                "do not route a purely structural pattern to codeql",
                "A purely structural pattern must use CodeQL solely because it is security.",
            ),
        }
        for name, text in self.specialists.items():
            needle, contradiction = mutations[name]
            mutated = mutate_paragraph(text, needle, contradiction)
            with self.subTest(tool=name, case="positive"):
                self.assertTrue(specialist_owner_holds(name, text))
            with self.subTest(tool=name, case="owner-mutation"):
                self.assertFalse(specialist_owner_holds(name, mutated))
            mutated_specialists = dict(self.specialists)
            mutated_specialists[name] = mutated
            for role_name, role in self.roles.items():
                with self.subTest(tool=name, role=role_name, case="composed-chain"):
                    self.assertFalse(
                        routing_chain_holds(role, self.common, mutated_specialists)
                    )
''')

path.write_text(text, encoding='utf-8')
