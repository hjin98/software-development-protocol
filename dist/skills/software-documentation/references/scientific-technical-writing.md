# Scientific and Technical Writing

Technical documentation should make sophisticated software reproducible, interpretable, and usable without sacrificing rigor.

## Style

Write clean, terse, direct prose. Prefer short coherent sections, explicit definitions, and meaningful transitions over dense walls of text. Avoid filler, repetitive restatement, implementation chronology, and unexplained internal jargon.

The document should work both for human reading and as reliable AI context: stable terminology, explicit conventions, clear ownership, and enough local context to interpret equations, algorithms, inputs, and outputs.

## Explain motivation and theory

For scientific/algorithmic material, explain:

- what problem the method solves and why the capability exists;
- the physical, mathematical, statistical, or computational basis;
- the modeling/algorithmic choices and their motivation;
- important alternatives when they remain current or materially illuminate the choice;
- approximations, assumptions, validity regime, and limitations.

Use the level of theory appropriate to the document. A user guide may link to deeper methods material; a methods paper should contain enough theory to reproduce the implemented method.

## Mathematical conventions

State conventions before ambiguity can affect interpretation:

- coordinate/cell/vector convention;
- units;
- sign/index/tensor ordering;
- periodicity and boundary assumptions;
- normalization;
- estimator/sample semantics;
- precision/tolerance policy where relevant.

Use LaTeX for mathematical formulas. Define symbols close to first use. Distinguish exact identities from approximations and empirical/heuristic rules.

## Algorithms and reproducibility

Explain the high-level algorithm in prose and use pseudocode or a flow chart when it materially improves understanding. Do not add diagrams mechanically when a paragraph is clearer.

For reproducibility, document as applicable:

- input data types, shapes, units, required fields, and constraints;
- output data types, shapes, units, ordering, and interpretation;
- preprocessing/normalization;
- algorithm stages and important data structures;
- numerical tolerances, cutoffs, convergence/resolution choices;
- random seeds/stochastic semantics;
- backend/dtype/model/schema requirements when material;
- edge cases and failure behavior;
- approximation regime and fallback behavior;
- computational complexity/scaling and material resource behavior.

The reader should have enough information to reproduce the method without reconstructing hidden conventions from source code.

## User guides

A task-oriented guide should bridge concept to operation:

```text
scientific/technical concept
    -> package abstraction
    -> CLI/API/configuration
    -> minimal example
    -> output interpretation
```

Start with the preferred current workflow. Put compatibility paths and advanced alternatives later. Include expected success signs and common failures when useful.

## Methods and theory papers

Methods/theory documents are explanatory by default rather than normative. They should reference the current architecture/specification that owns behavior instead of duplicating independent thresholds, defaults, or compatibility promises.

A useful methods paper often includes:

1. motivation/problem statement;
2. theoretical foundation;
3. definitions/conventions;
4. mathematical formulation;
5. algorithm and data representation;
6. pseudocode/flow diagram when useful;
7. numerical implementation details;
8. input/output contracts for reproducibility;
9. assumptions, limitations, edge cases;
10. scaling/performance where material;
11. validation/interpretation guidance;
12. references.

## Sources and attribution

Cite external literature and sources that materially motivated or supplied algorithmic ideas.

Prefer:

- primary/original scientific source for a standard method where practical;
- official documentation for external software/API behavior;
- explicit language when mdstats/project-specific behavior adapts or modifies an external method.

If a claim or attribution has not been verified, do not fabricate a citation. Distinguish borrowed/standard material from project-specific adaptation when that distinction matters for reproducibility or interpretation.

## Presentation quality

When Markdown is also published as PDF or another rendered format, preserve professional presentation:

- coherent heading hierarchy and table of contents;
- readable equations and tables;
- figures near relevant discussion with explanatory captions;
- code blocks that wrap/render acceptably;
- useful cross-references;
- consistent notation and terminology;
- no clipping, overlapping elements, broken glyphs, orphaned headings, or obviously poor page breaks in representative/all materially changed pages as project policy requires.

A document is not complete merely because the renderer exits successfully; it should remain readable, well structured, well written, and well presented after substantial change.
