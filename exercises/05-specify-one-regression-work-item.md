# 05 — Specify and implement one regression work item

**55 minutes.** You will make the research decisions for one small analysis, write a draft spec, approve it after review and ask for implementation. A spec is not a whole-project plan.

## The bounded work item

Produce **one regression table about commuting time and life satisfaction**, with its reproducible script and short interpretation. Use the simulated survey already in the project. This item can be completed and checked independently; it does not include every possible wellbeing analysis or the final capstone project.

For the teaching reference, use ordinary least squares. You decide the precise question, target group and inclusion rules, definitions and units, adjustment variables, missingness treatment, uncertainty calculation and limits of interpretation. The codebook defines the data but does not make those choices for you. Keep the first model modest enough to understand and check.

## Task and timing

**0–8 minutes:** Read `data/README.md` and complete `templates/research-decisions.md` in `notes/05-my-decisions.md`. State what you know and what is unresolved in your own words. Writing several genuine decisions before the dialogue saves turns; it does not authorize the agent to fill missing ones.

**8–20 minutes:** Use the first prompt. The spec skill should ask one meaningful open question at a time. It should not supply a menu or recommendation unless you explicitly ask for help. Answer the questions you can; ask for an explanation when necessary. If it attempts to choose for you, stop and correct that behaviour.

**20–25 minutes:** Read `specs/05-commute-regression/spec.md`. Verify that it records your choices accurately, includes one deliverable and observable checks, and leaves unresolved issues visible. Do not approve it while a material decision remains unclear. The drafting skill stops here without a plan or code.

**25–43 minutes:** When satisfied, use the separate approval-and-implementation prompt. Review any new issue that would change the research design. Ask the agent to stop rather than silently change it.

**43–55 minutes:** Inspect the table, sample accounting and report. Explain one coefficient in its actual units and one limitation. Save a handover if the item is not complete.

## Drafting prompt

> Read skills/spec/SKILL.md and use it to specify ONE work item named 05-commute-regression: a regression table about commuting time and life satisfaction from data/raw/work_care_wellbeing.csv, with a reproducible script and short interpretation. Read data/README.md and notes/05-my-decisions.md. Use the decisions I have actually written. Ask one open question at a time about consequential gaps; do not give me options or a recommendation unless I ask. Write specs/05-commute-regression/spec.md as a draft and stop for my review. Do not write a project-wide spec, an implementation plan or any analysis code.

## Separate approval-and-implementation prompt

Use this only after you have read and approved the draft:

> I have read specs/05-commute-regression/spec.md and approve the research decisions and scope it records. Record my approval and today's date. Read skills/implement-spec/SKILL.md and implement this work item only. Use scripts/05_regression.py as the entry script, outputs/05-regression/ for outputs and specs/05-commute-regression/report.md for the results and check evidence. Ask me if a new issue would change the design. Do not infer decisions from the desired result, run a search for significance or start another work item.

## Deliverables and checks

The spec defines the exact files and checks. At minimum, inspect:

- The approved sample, exclusions and number actually used by the model.
- Treatment of documented nonresponse and inapplicability, while preserving genuine zeroes when included by the spec.
- The model terms, transformations, reference categories and uncertainty calculation against the approved text.
- One numerical check with an independently understood expected result or relation.
- A coefficient interpretation that uses the actual units and avoids unsupported causal or population claims.
- A documented command that reproduces this item from unchanged inputs.

There is no required sign, significance level or dramatic finding. A coefficient that appears uninteresting can still be a correctly executed analysis.

## Stop point and low-usage route

An approved, implementable spec is a valid stopping point if time or usage runs out. Save `specs/05-commute-regression/handover.md` and state that estimation has not been completed. You can draft the spec manually and ask a partner to identify unresolved decisions. An instructor's worked regression demonstrates one possible approved design; it is not a substitute for silently assigning those choices to you.

## Optional extension

Identify one substantive concern that could alter interpretation. Record it as a **new** bounded work item in the project roadmap, with its own future spec. Do not expand the approved item halfway through without recording an explicit scope change.
