---
name: implement-spec
description: Implement one existing researcher-approved work-item specification, build its requested outputs, and report evidence against its checks. Use only when implementation is requested and a scoped spec exists. Stop on missing approval or consequential research gaps; do not select the design or expand into the whole project.
---

# Implement an approved work item

1. Read the project instructions, the exact `specs/<work-item>/spec.md`, its referenced data documentation, and any existing script for that work item. Do not infer approval from the existence of a spec or from a generic request to continue.
2. Verify that the spec identifies one independently completable deliverable, has explicit researcher approval, and resolves material research decisions. If the researcher explicitly approves the exact draft in the current request, faithfully record that approval and date in the spec before implementing; never record approval that was not given. If approval or a consequential decision is missing, identify the gap and ask one open question. Do not offer a menu or recommendation unless asked. Do not implement a project-wide spec.
3. Inspect existing files before edits. Respect the current permission settings and raw-data restrictions. Report an unavailable runtime or package accurately; do not claim an unrun command passed. Ask before a new dependency or network operation unless the researcher has already authorized it.
4. Implement only the approved scope. Choose routine syntax and code organization yourself. Do not silently change inclusion rules, variable definitions, special-code treatment, controls, reference categories, weighting, uncertainty estimates, or the intended claim. If a new issue requires such a change, stop that part, describe the evidence, and return the choice to the researcher. Keep completed work intact.
5. Keep the pipeline reproducible from the documented inputs. Use relative paths, deterministic settings where appropriate, and a single documented entry command for this item. Write derived data and outputs to their designated directories; do not edit raw inputs. A plotting skill may set presentation conventions but may not override the research spec.
6. Run the checks from the spec. Inspect substantive outputs, not just exit codes. Reconcile sample counts and exclusions; verify special codes and units against the codebook. Perform the independent check the spec requires using its stated evidence. Do not manufacture an expected result after seeing the estimate or weaken a failing check to obtain a pass.
7. Save `specs/<work-item>/report.md` with: the run command; produced files; the analysis sample and exclusions; results relevant to this item; every check and its evidence; remaining limitations or failures; and any researcher-approved deviation. Distinguish executed, inspected, and not checked.
8. Review the final diff and summarize material changes. Do not commit, push, send messages, or publish unless the researcher has requested that action. Leave unrelated files alone.
9. End with the result, the evidence for completion, and any unresolved issue. If the requested checks do not pass, label the work incomplete. Do not start another work item automatically.

Instructions and reviews are not security controls or guarantees of correctness. The researcher remains responsible for the question, design, approval, and final interpretation.
