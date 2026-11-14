---
name: review-spec
description: Review one work item's implementation and outputs against its approved research specification, using explicit evidence. Use for an independent audit or a fresh-context review. Report definite defects, research judgments, and unverified checks separately. Do not edit code, change the research design, approve your own recommendations, or start an open-ended repair loop.
---

# Review one work item with evidence

1. Read the project instructions, the exact approved work-item spec, the relevant codebook, implementation, outputs, and report. State which files and checks you actually inspected. A producer's assertion that a test passed is not independent evidence.
2. Review only this work item's approved scope. If the spec covers several separately completable tasks, report the scope problem. If a material choice is absent or approval is missing, identify the gap rather than making the decision.
3. Check the population and filters, unit of observation, variable definitions and units, special and conditional codes, missingness, joins or weights when applicable, model terms and uncertainty, required outputs, and interpretation against the spec. Do not assume every item applies.
4. Run only existing, authorized checks or a documented rebuild that writes to designated derived-output locations. Do not edit source files or install dependencies. For an independent calculation, use a separate read-only calculation or the supplied fixture; explain its inputs and expected value. Ask if executing the needed check would exceed permission or overwrite work that needs preserving.
5. For each check, record `pass`, `fail`, or `not checked`, with a file, command, observed value, or short calculation supporting that status. State the source of any expected value. Successful execution alone does not establish scientific correctness.
6. Classify findings:
   - **Defect:** a reproducible mismatch with the approved spec or documented data meaning.
   - **Research judgment:** a substantive concern requiring the researcher's choice; do not silently modify the design.
   - **Evidence gap:** a claim or check that could not be verified.
7. Prioritize findings by their consequence for the result. Do not invent issues to make the review look thorough. Do not call a result verified if meaningful checks remain unperformed. A fresh context does not guarantee an independent or correct judgment.
8. Write only `specs/<work-item>/review.md`, unless the researcher requested the review in chat. Use the report structure below. Do not alter the spec, implementation, or outputs.

```markdown
# Review: [work item]
Scope and artifacts inspected:
Commands actually run:

| Check | Expected result and source | Observed evidence | Status |
|---|---|---|---|

## Defects
[Finding, consequence, exact evidence; or None found in the inspected scope.]

## Research judgments for the researcher
[Concern and why it matters; or None raised.]

## Evidence gaps
[What remains unverified and why.]

## Conclusion
[What the evidence supports; whether the item meets its stated completion criteria.]
```

For the course, perform at most one review and one researcher-authorized repair round before the handover. If an issue remains, record it and stop. Review instructions do not grant access or prove the result correct; the researcher must evaluate the evidence.
