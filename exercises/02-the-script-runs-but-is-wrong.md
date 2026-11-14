# 02 — The script runs. Is the result right?

**30 minutes.** Diagnose an inherited analysis using the data definitions and a hand calculation. The supplied script contains a deliberate teaching error. No hidden instruction asks an agent to behave badly, and the example is not evidence that an AI produced the error.

## Starting files

Read `scripts/02_inherited.py`, `data/README.md`, `data/fixtures/README.md` and `data/fixtures/missing_values_example.csv`. The script produces mean life satisfaction by employment status in `outputs/02-repair/summary.csv` and `outputs/02-repair/summary.png`.

## Task and timing

**0–5 minutes:** Use the eight-row fixture to calculate the number and mean of valid life satisfaction responses by hand. Decide which entries are valid from the codebook. Write your expected count, sum and mean in `notes/02-repair.md` before asking the agent. Explain separately what zero, nonresponse and inapplicability mean.

**5–8 minutes:** Create a git checkpoint for the files you will inspect. If this folder is not yet a repository, run `git init` once. Then run:

```bash
git status --short
git add scripts/02_inherited.py data/README.md
git commit -m "Checkpoint inherited summary before review"
```

If git asks for identity, set a local course identity with the instructor's help; do not change global configuration. These commands stage only the named files and preserve other work.

**8–20 minutes:** Use the prompt below. Read the diagnosis and the proposed code change. Compare its fixture result with your hand calculation. Ask it to preserve valid zeroes and to make no unrelated changes.

**20–27 minutes:** Rebuild the summary, inspect the diff and check the output. Confirm that the fixture check applies the same cleaning function used by the main script. The expected result comes from your independent calculation, not from whatever the script happens to return.

**27–30 minutes:** Record the cause, repair and evidence. Commit the reviewed change if satisfied.

## Starting prompt

> Read AGENTS.md, the data documentation, data/fixtures/missing_values_example.csv and scripts/02_inherited.py. This inherited script contains a deliberate error. Identify the mismatch between its treatment of responses and the codebook, with evidence. Repair only that mismatch, preserving the intended descriptive comparison. Add a small check using the supplied fixture and the same cleaning function used for the main data. Report the fixture's valid count and mean so I can compare them with my hand calculation. Run the repaired script, report the resulting files and the changed sample counts, and show the material diff. Do not change the raw data, redefine the analysis or commit yet.

## Checks and completion

- The codebook, rather than the sign of a number alone, determines treatment.
- Documented nonresponse is excluded from the mean and its denominator; a genuine zero remains valid.
- The fixture agrees with the independently calculated count, sum and mean.
- The full output includes a count for each group's mean and can be rebuilt.
- `git diff -- scripts/02_inherited.py` shows the intended repair and check, with no unrelated redesign.

After review, commit with:

```bash
git add scripts/02_inherited.py notes/02-repair.md
git commit -m "Respect documented missing responses in life satisfaction summary"
```

## Stop point

A verified repair and a record of its evidence are enough. If the check still fails, save the failing evidence and next action; do not mark the work complete.

## Low-usage route

The fixture, codebook and script can all be inspected without an agent. Work out the repair on paper or in the editor, run the script yourself, and review its diff with a partner. Ask the instructor for the completed checkpoint only after attempting the diagnosis; record any supplied work accurately.

## Optional extension

Make a harmless title change, inspect its diff and practise restoring **that named file only** if it contains no work you want to keep. Never use a blanket restore to discard unrelated work. A commit preserves a history of files; it does not independently establish that an analysis is correct.
