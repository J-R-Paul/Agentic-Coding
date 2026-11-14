# 01 — A bounded first output

**25 minutes.** You will inspect an agent's work while making a small, reproducible figure. A useful result is a saved artifact you can explain, not merely a reassuring answer in chat.

## Starting files

- `AGENTS.md` and `data/README.md`.
- `data/raw/work_care_wellbeing.csv`: 2,000 simulated adults.
- `scripts/01_first_output.py`: a working age histogram.
- `templates/task-boundary.md`: an optional task card.

Work from `student-project`. Use the Python interpreter that passed the setup check.

## Task and timing

**0–4 minutes:** Read the script and its data definition. Predict the files the agent needs to read, the file it will edit and the output it will write. In your client's settings, identify the current approval mode and workspace boundary. Do not grant unrestricted access just to complete this exercise.

**4–14 minutes:** Use the starting prompt below. Observe at least one file read, edit or execution in the interface. Record whether it ran, asked, or was blocked. Exact behaviour differs between clients and configurations; a missing approval prompt is an observation, not automatically an error.

**14–20 minutes:** Open the saved PNG yourself. Check what the bins count, the axis units, the actual source row count and whether the synthetic source is visible. Inspect the script diff. Check that only the intended script and derived output changed.

**20–25 minutes:** Tell your partner what you authorized, what actually happened and what you checked. If the instructor demonstrates a second approval mode, predict how the same bounded action might be treated and compare with the observed trace.

## Starting prompt

> Read AGENTS.md, data/README.md and scripts/01_first_output.py. Make one bounded improvement to that script: add a caption stating the actual number of records read and “Synthetic course survey, release 1.0.0”. Derive the count from the data, not a typed constant. Keep the same age bins and research content. You may edit only scripts/01_first_output.py and write its derived output in outputs/01-first-output/. Run the script with the working Python interpreter, inspect the saved figure if your tools support it, and report the command, output path, count and checks you actually performed. Keep the raw data unchanged. Stop after this output; do not install packages or use the network.

## Deliverables and checks

Save the changed script and `outputs/01-first-output/age_distribution.png`. Record the observed read/edit/run actions and two checks in `notes/01-first-output.md`.

- The plot has age in years on the horizontal axis and counts on the vertical axis.
- All 2,000 raw rows are represented; no age lies outside the documented bins.
- The caption's count comes from the data and the synthetic provenance is visible.
- The report distinguishes an actual image inspection from a check the agent could not perform.

## Stop point

Stop when the figure is saved, the diff is inspected and you can explain the count. If execution fails, retain the exact command and error; do not spend the whole exercise reinstalling software.

## Low-usage route

Run `python scripts/01_first_output.py` yourself. Make the caption edit in the editor, or pair with one agent user. Inspect the existing script, resulting image and the instructor's recorded action trace. Record which actions you observed live and which were a demonstration.

## Optional extension

Add a PDF export of the same figure and check that it has the same content. Do not change the research question or begin analysing a new variable.

**Key distinction:** AGENTS.md gives instructions. It does not enforce a filesystem sandbox or control which data a provider processes.
