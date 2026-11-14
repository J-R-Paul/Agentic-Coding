# 06 — Review against the spec, with evidence

**30 minutes.** Audit one work item and evaluate the review itself. A fresh conversation, another student's agent, a subagent when available or a human peer can perform the reviewing role. None guarantees independence or correctness.

## Task and timing

**0–5 minutes:** Identify your approved spec, implementation, table and report from Exercise 05. Write down one check you especially want independently verified. If you do not yet have an implementation, use `exercises/review-faults.md`; it is a self-contained, openly prepared review case.

**5–17 minutes:** Start a fresh review context and use the prompt below. Keep the scope narrow and outputs short. Give it the actual artifacts rather than the producing agent's conclusions. The reviewer should inspect evidence, identify unavailable checks and avoid modifying the analysis.

**17–23 minutes:** Read the review yourself. Select one finding and follow its evidence back to the actual file, value or calculation. Distinguish a definite defect, a research judgment and an evidence gap. Reject an unsupported accusation as well as unsupported reassurance.

**23–28 minutes:** If a definite defect is established, authorize one bounded repair. Run the relevant check again and record the result. If the issue requires a research decision, make and record that decision before changing the analysis. Keep to one review and one repair round during the exercise.

**28–30 minutes:** Complete a handover that states what is verified, incomplete or unresolved. Do not claim completion simply because time has ended.

## Review prompt

> Read skills/review-spec/SKILL.md. Review the single work item in specs/05-commute-regression/spec.md against its implementation, outputs and data documentation. Inspect the actual artifacts. Report each meaningful check as pass, fail or not checked, with evidence and the source of the expected result. Independently verify one important calculation or sample rule where feasible. Separate definite defects, research judgments and evidence gaps. Write specs/05-commute-regression/review.md. Do not edit the spec, source code or research design, install packages or start another work item. If you cannot execute a check, say so.

## Prepared-case prompt

> Read skills/review-spec/SKILL.md and exercises/review-faults.md. Audit the prepared case using only its stated spec, fixture, code extract and draft output. Give evidence for each finding and do one hand-checkable calculation. Do not imply that the displayed code was executed or that unseen outputs were inspected. Save the review in notes/06-prepared-case-review.md and stop without editing the case.

## Repair prompt

Replace the sentence naming the finding with the specific defect you have verified:

> I have verified the defect described in the review. Repair that defect only, preserve the approved research design, rerun the relevant checks and record the evidence in the report. Show the material diff and leave other work untouched. Stop after this repair and report anything still unresolved.

## Deliverables and checks

Save the review and handover. If repaired, keep the reviewed diff and evidence from the new run.

- Every `pass` or `fail` has inspectable support.
- A producer's statement is not treated as independent verification.
- The review does not invent a preferred model or change the approved sample.
- Unperformed checks are labelled honestly.
- The interpretation is no stronger than the design and simulated data allow.
- The handover contains one specific next action and the files needed to continue.

## Stop point

A completed review with a clearly documented unresolved issue is acceptable. Record the issue instead of running unlimited cycles until a reviewer says everything is fine.

## Low-usage route

Audit the prepared case with a partner, using `templates/review.md`. The fixture is small enough to check by hand. If your own analysis is complete, exchange projects or inspect one another's table and code. Record peer review accurately; do not call it an agent execution.

## Optional extension

Ask a reviewer to check a different aspect using an independent calculation rather than repeating the same prompt. Explain what genuinely new evidence the additional check contributes before spending more usage.
