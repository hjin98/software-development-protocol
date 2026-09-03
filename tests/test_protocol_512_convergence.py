from __future__ import annotations
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def r(p):return (ROOT/p).read_text(encoding="utf-8").lower()
class Protocol512ConvergenceTests(unittest.TestCase):
 def setUp(self):
  self.w=r("source/shared/references/workflow-and-workplans.md");self.t=r("source/shared/references/testing-and-validation.md");self.a=r("source/shared/references/architecture-and-design.md");self.i=r("source/shared/references/repository-intake.md");self.g=r("source/shared/references/tool-assisted-engineering.md");self.d=r("source/roles/software-design/SKILL.md");self.m=r("source/roles/software-implementation/SKILL.md");self.p=r("source/shared/templates/implementation_workplan_template.md")
 def test_identity_and_preservation(self):
  self.assertEqual("5.12.0",r("source/PROTOCOL_VERSION").strip());h="product engineering fitness > minimum justified product/system complexity > development economy";self.assertIn(h,self.d);self.assertIn(h,self.m);self.assertIn("software-design -> software-implementation",r("source/README.md"))
 def test_escalation_and_family_boundary(self):
  for x in ("a first clean local defect","family closure after recurrence","genuine family closure","bounded software design reconsideration","do not fragment","do not overaggregate"):self.assertIn(x,self.w)
  for x in ("protected invariant / required product claim","semantic owner or authority class","state / transition / lifecycle class","materially equivalent failure mechanism"):self.assertIn(x,self.w)
 def test_incomplete_family_is_not_automatic_redesign(self):
  self.assertIn("incomplete family closure",self.w);self.assertIn("remains implementation nonconformance",self.w);self.assertIn("normative design change is not predetermined",self.w);self.assertIn("does not automatically mean architecture churn",self.a);self.assertIn("complete/correct that family closure",self.m)
 def test_post_family_recurrence_reconsiders_design(self):
  self.assertIn("after a genuine family closure",self.w);self.assertIn("same family materially fails after an adequate family closure",self.m);self.assertIn("triggers bounded design reconsideration",self.d);self.assertIn("same authority",self.a)
 def test_census_is_bounded_and_conditional(self):
  self.assertIn("progressive evidence-directed inspection remains the default",self.i);self.assertIn("switch to a bounded census only when",self.i);self.assertIn("whole-repository inventory remains unnecessary",self.w);self.assertIn("not universal persistent traceability artifacts",self.i)
 def test_acceptance_liveness(self):
  for x in ("patched seam, failpoint, callback","trigger actually fired","real semantic owner","not a universal requirement to check out historical commits","known-positive and known-negative","structural/negative scans complement runtime acceptance"):self.assertIn(x,self.t)
 def test_review_readiness_and_non_refusal(self):
  for x in ("exact candidate identity","final complete affected-surface regression","real-boundary integration","not review-ready","not an automatic design revision","explicitly requested review still proceeds"):self.assertIn(x,self.w)
  self.assertIn("do not refuse an explicitly requested review",self.d);self.assertIn("review readiness is not a mechanism for refusing review",self.t)
 def test_review_saturation_and_stopping(self):
  for x in ("review characterizes and batches the family","implementation owns the systematic family closure","reviewer expansion stops","not proof that no conceivable repository defect exists"):self.assertIn(x,self.w)
  self.assertIn("proportionately saturate the directly implicated family",self.d);self.assertIn("evidence-directed sufficiency",self.d)
 def test_revision_economy_and_snapshot_completeness(self):
  for x in ("do not require a new numbered authority revision","reconcile that semantic into canonical current authority","snapshot completeness is preserved","concrete new sites"):self.assertIn(x,self.w)
  self.assertIn("ordinary implementation misses and review cycles do not require numbered authority revisions",self.d)
 def test_closure_horizon_and_template_are_not_ceiling_or_bureaucracy(self):
  self.assertIn("closure horizon",self.w);self.assertIn("it is not a scope ceiling",self.w);self.assertIn("conditional convergence guidance",self.p);self.assertIn("does not require a family matrix",self.p);self.assertIn("do not require ids, ledgers, persistent closure maps",self.p)
 def test_tools_remain_optional(self):
  self.assertIn("convergence-oriented composition",self.g);self.assertIn("optional tools",self.g);self.assertIn("tool absence does not relax family closure",self.g);self.assertIn("three-tool sequence mandatory",self.g);self.assertIn("tool availability alone is not a reason",self.g)
 def test_regression_integration_qualification_preserved(self):
  self.assertIn("stage-local affected regression",self.t);self.assertIn("stage-local affected regression",self.m);self.assertIn("final complete affected-surface regression",self.t);self.assertIn("integration/end-to-end",self.t);self.assertIn("production qualification is separate",self.m);self.assertIn("distinct from functional testing",self.t)
if __name__=="__main__":unittest.main()
