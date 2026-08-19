# Software Development Protocol

Software Development Protocol is a role-separated, evidence-driven workflow for AI-assisted software engineering.

Protocol v3 keeps four useful authority boundaries:

```text
software-design -> software-implementation -> software-qualification -> software-verification
```

The guiding rule is materiality: protocol mechanics exist to improve confidence in the software, not to become a second product that must be qualified. A process defect blocks acceptance only when it can materially change what code/input/environment was exercised or how a correctness, scientific, recovery, security, distribution, performance, or regression claim should be interpreted.

For ordinary Git projects, the candidate commit is the default source identity. Extra hashes are used at real external/generated content boundaries, not as universal paperwork. Harmless qualification harness/report errors can be corrected in place without restarting valid software checks.

Use the lightest lifecycle that preserves the needed authority separation. Small work may use `inspect -> implement -> relevant checks -> review`; substantial or cross-environment work uses a workplan and, when useful, a compact qualification run card.

`source/` is canonical. `dist/` contains generated role skill packages.
