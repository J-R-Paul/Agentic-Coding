# 04 — Create, apply and revise your own skill

**40 minutes.** You will genuinely create a reusable project-local skill. No completed `research-figure` skill is supplied. The blank authoring worksheet is a starting structure, not the answer.

## Two different inputs

Read `data/fixtures/README.md`. Use both:

1. `data/fixtures/life_satisfaction_by_status.csv`: mean life satisfaction by employment status.
2. `data/fixtures/care_hours_by_age.csv`: mean weekly unpaid care by age group.

The inputs have different outcomes, units, labels and group structures. Both include estimates, group counts and documented 95% intervals. They are synthetic summaries, not raw observations. Preserve their research content; your skill should handle presentation, not recompute the estimates or decide the underlying samples.

## Task and timing

**0–6 minutes — Decide:** Run `python scripts/03_plot_inputs.py` to produce a plain starting figure for each input in `outputs/04-skill/`. Inspect both, then write your own requirements for readable research figures. Include how the reader will identify the measure and units, sample counts, uncertainty, provenance and any limitation. Choose a visual convention you can explain. You may ask for an explanation of a design issue; do not simply accept every default the agent proposes.

**6–17 minutes — Create:** Use the prompt below and `templates/skill-skeleton.txt`. Create:

- `skills/research-figure/SKILL.md` with YAML `name` and `description`, a reusable workflow, limits and checks.
- `skills/research-figure/references/figure-rules.md` containing your actual conventions.

The skill body must link to the reference with `[figure rules](references/figure-rules.md)` and state when to read it. The description should say when to use the skill; the body should explain what to do. Do not hard-code the first outcome or its number of groups.

**17–25 minutes — Apply twice:** Check structure and update this project's discovery copies:

```bash
python tools/check_skill.py research-figure
python tools/sync_skills.py
```

Ask the agent to read the new skill explicitly and apply it to both inputs. Save the plotting code in `scripts/render_research_figures.py` and PNG/PDF outputs under `outputs/04-skill/`. Inspect the trace for the reference-file read when your client exposes it. A structural pass is not a behavioural test.

**25–34 minutes — Inspect and revise:** Open both figures yourself. Find one weakness in your reusable instructions, revise the skill or reference and resync. Apply the revised skill again to both inputs. Check that the change improves the intended feature without corrupting either figure's research content.

**34–40 minutes — Record:** Complete `notes/04-skill-test.md` using `templates/skill-test-record.md`. Record what changed and evidence from both applications.

## Creation prompt

> Help me CREATE a project-local skill named research-figure from my figure requirements. Read AGENTS.md, data/fixtures/README.md and templates/skill-skeleton.txt. My requirements are in my preceding message; ask one meaningful question if an essential preference is missing. Create skills/research-figure/SKILL.md and references/figure-rules.md inside that skill folder. Include useful trigger metadata, a reusable workflow, a linked reference and observable checks. Preserve the supplied research content and document that these data are synthetic. This must work with both plotting inputs named in Exercise 04. Do not install a personal or global skill and do not create finished figures until I inspect the skill.

## Application prompt

> Read skills/research-figure/SKILL.md and its linked reference. Apply my skill to both data/fixtures/life_satisfaction_by_status.csv and data/fixtures/care_hours_by_age.csv. Create reproducible code in scripts/render_research_figures.py and save a PNG and PDF for each input in outputs/04-skill/. Use the actual measure, units, group order, counts and interval endpoints from each input. Preserve their meaning and make the synthetic provenance visible. Report what you ran and what you inspected. Stop after these two figures.

## Checks and stop point

Confirm correct labels and units, all groups and counts, visible intervals with their documented meaning, no clipped content, readable exports and a visible source note. Verify that the reference is genuinely linked and inspect loading evidence where observable. Record `not observable` when appropriate; do not invent a trace.

Stop after one evidence-backed revision and two successful applications. If behaviour remains unreliable, save the weakness and the next test instead of claiming the skill works generally.

## Low-usage route

Write the skill and reference manually, then share one agent run with a partner for both inputs. If agent usage is exhausted but Python works, ask the instructor for the separate `04-research-figure` checkpoint **after you have written your own skill**. It contains a documented example skill and working renderer. Compare its conventions with yours, adapt its renderer in your editor, and run it on both inputs. A program does not interpret a Markdown skill automatically: this route tests the conventions you have manually implemented; agent loading and instruction following remain untested.

The checkpoint README gives the exact copy/run commands. After the renderer is copied into your project, `python scripts/render_research_figures.py` exports both figures as PNG and PDF. Revise one convention in your skill and renderer, run again and record the before/after evidence. Mark any borrowed parts honestly. If Python execution is also unavailable, complete the authoring and annotate both input tables with required output features. Record those applications as untested. The instructor example is deliberately separate from your starter.

## Optional extension

Use the same skill on a figure from a later work item. Ensure it preserves that item's approved sample, estimates and interpretation. A reusable plotting procedure should not silently redesign the research.
