---
name: spec
description: Specify one bounded research work item before analysis. Use when a researcher wants to define a single analysis, table, figure, data transformation, or other independently checkable deliverable. Elicit the researcher's unresolved decisions with one open question at a time, write a draft to specs/<work-item>/spec.md, and stop for review. Do not implement the work, write a plan, or specify a whole project.
---

# Specify one work item

Turn the researcher's chosen work item into a specification that another researcher can implement without inventing substantive research decisions.

## Boundaries

- Specify exactly one work item that can be completed, checked, and closed independently. A single regression table and its supporting reproducible script can be one item. A whole study containing data preparation, several analyses, a dashboard, and a final report is a project, not one work item.
- If the request covers a whole project, explain the scope problem and ask: **What single deliverable should we specify first?** Do not produce a project-wide spec or a menu of possible work items. A project brief or roadmap can record broader aims outside this skill.
- Draft only. Do not write or run code, fit models, produce analysis outputs, write an implementation plan, or invoke implement-spec. Use file-reading tools to inspect existing documentation and small relevant excerpts only. If necessary evidence would require analysis, ask for an existing result or leave the issue explicitly unresolved.
- These instructions guide behaviour; they do not grant permissions or create a security boundary.

## Read the context

1. Read the project instructions and the researcher's request. Read `data/README.md`, `notes/exploration.md`, and the relevant codebook if present. Read an existing spec only for the chosen work item.
2. Use verified filenames, columns, units, and documented codes. Distinguish documented facts, researcher decisions, and unresolved questions. Do not turn a guess into a fact.
3. Use the supplied short work-item name. If none is supplied, ask for it when needed; a routine suggested filename is acceptable, but it must not substitute for choosing the substantive scope.

## Elicit decisions

1. Restate the chosen research question or deliverable in one sentence, using only the researcher's stated intent. Identify the intended kind of claim only when clear; otherwise ask.
2. Identify consequential gaps internally. Depending on the work item, these may concern population, inclusion rules, unit of observation, definitions and units, joins or aggregation, weighting, missing or conditional values, model terms, interpretation, outputs, and checks. Do not recite a generic questionnaire or expose a long checklist as the response.
3. Ask **one meaningful open question at a time**, explain briefly why it matters if useful, and wait for the answer. Ask only about a decision still missing. Do not bundle several decisions into one question.
4. **Do not offer options, examples of possible answers, a recommended default, or your own preference unless the researcher explicitly asks for that help.** An open question must not contain a disguised menu. If asked for an explanation, explain the issue in plain language; do not quietly choose for the researcher. If recommendations are requested, label them as recommendations and wait for the researcher's choice or explicit authorization to adopt one.
5. Do not ask about routine syntax or formatting that cannot change the meaning of the result. Do ask when a technical choice changes the sample, measure, estimate, uncertainty, or claim.
6. Record only decisions the researcher actually made or explicitly approved. Never invent rejected alternatives, reasons, or approvals. If the reason was not stated and matters, ask; otherwise write `Reason not supplied`.
7. If the data cannot support the requested question or claim, explain the specific mismatch and ask how the researcher wants to resolve it. Do not silently redefine the question, replace causal language with a different aim, or treat synthetic data as empirical evidence about real people.
8. Continue until material decisions are resolved or the researcher asks for a partial draft. For a partial draft, leave consequential gaps under Open questions and say that implementation is blocked by them. Do not fill gaps to finish faster.

## Write and stop

Using a tool solely to read existing text or save the Markdown spec is allowed. Do not create or execute analysis scripts, run models, make outputs, or write an implementation plan during this drafting step.

Write only `specs/<work-item>/spec.md`, using the structure below. Keep it proportionate to the single work item. Use the actual date. Preserve a prior approved version when revising and mark the revised text as draft. Do not mark the work approved yourself.

```markdown
# Spec: [researcher's work-item title]
Status: draft
Date: [actual date]

## Scope and completion
Single deliverable:
This item is finished when:
Excluded work:

## Question and intended claim
Question:
Type and limits of claim:

## Data and sample
Sources and relevant documentation:
Unit of observation:
Inclusion and exclusion rules, with reasons:
Missing, special-code and conditional-value treatment:
Joins, aggregation and weighting, if applicable:

## Measures
| Measure | Definition or formula | Units | Source columns |
|---|---|---|---|

## Method
Exact comparison, transformation or model:
Model terms, coding and reference categories, if applicable:
Treatment of uncertainty, if applicable:

## Outputs
| File | Required content |
|---|---|

## Checks
- [ ] [Observable check; expected result or rule, source of expectation, and how it will be checked.]

## Researcher decisions
| Decision | Researcher's choice | Stated reason | Source of decision |
|---|---|---|---|

## Open questions
[Unresolved issues, or None.]

## Approval
Awaiting researcher review. Record the researcher's explicit approval and date before implementation.
```

Checks must be independently interpretable. State an exact expected count only when it is established by evidence. Otherwise specify a verifiable relation or a reconciliation, rather than inventing a target. At least one check should address meaning or data interpretation, not merely successful execution.

End by naming the draft file, identifying any unresolved issue, and asking the researcher to review it. **Stop there.** An existing approved spec belongs with implement-spec only when implementation is separately requested; this skill remains a drafting step.
