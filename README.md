# Agentic coding for social scientists: student project

This is the working project for the six guided exercises. You will use an agent to make a small output, inspect and repair inherited code, organise project instructions, **create a reusable skill**, specify one regression task, and check the result.

The data describe **2,000 simulated adults**. They are invented for teaching. They support practice with quantitative analysis and agent workflows; they are not evidence about a real population. Preserve the raw CSV and consult its codebook before recoding any values.

## Before the course

**Unable to install software locally?** [Create your own copy of the course template](https://github.com/J-R-Paul/Agentic-Coding/generate), then follow [the browser-only Codespaces route](CODESPACES.md). It installs Python, the course packages and Codex CLI in the cloud. You still need your own eligible accounts and available usage. If using Codespaces, complete its setup and login checks, then continue at “Start the guided exercises” below.

Use **Python 3.10 or later**, git, and an editor or agent client that can open a project folder. The Python reference uses numpy, pandas, matplotlib and scipy. Setup is a pre-course activity; internet access is needed to install packages and use a cloud agent, but the exercises do not download data or call a research API.

Check that you can sign into and use the exact agent client you plan to bring. A ChatGPT subscription or browser login does not, by itself, verify access in every coding client. If access or your allowance is uncertain, tell the instructor before the day. Paired and prepared-output routes are available. You do not need to buy an upgrade to work through the research decisions.

Open **this `student-project` folder** as the project, rather than its parent folder. Keep it separate from other research, personal files and any full instructor archive.

### Install the reference environment

Open a terminal in this folder. Run the commands for your operating system. They create a project-local environment; you do not need to change global Python packages.

**macOS or Linux:**

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python scripts/00_check_environment.py
.venv/bin/python scripts/check_data.py
.venv/bin/python scripts/01_first_output.py
```

**Windows PowerShell:**

```powershell
py -3 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe scripts/00_check_environment.py
.\.venv\Scripts\python.exe scripts/check_data.py
.\.venv\Scripts\python.exe scripts/01_first_output.py
```

If your Python command differs, use the Python 3.10+ interpreter configured on your machine. If you already have a suitable environment, you can use it instead. In the exercises, `python` means **that interpreter**. Select the same interpreter in your editor and tell your agent which command works.

A successful check prints `Environment check passed`, verifies 2,000 rows and unique respondent IDs, and creates `outputs/01-first-output/age_distribution.png`. Open the figure. This verifies local execution, not your AI account access.

Also run:

```bash
git --version
```

If anything fails, save the exact command and error for the instructor. Do not spend your AI allowance repeatedly asking it to reinstall packages. Self-sufficient R users may follow the same research tasks in R, but the supplied scripts and tested reference environment are Python.

## Start the guided exercises

Follow the exercise briefs in `exercises/` in the order given by the instructor. Read `AGENTS.md` and the data notes first. The main input is:

```text
data/raw/work_care_wellbeing.csv
```

The first working script is `scripts/01_first_output.py`. The inherited analysis in `scripts/02_inherited.py` is an intentional teaching exercise: treat it as work to inspect, not as a trusted answer. Later tasks build on your own decisions and changes.

Keep the code and evidence for each task. You should be able to explain what the agent changed, why it changed it, and how you checked the result. Running without an error is only one check.

## Project-local skills

The starter includes three procedures:

- `spec`: clarify and record **one bounded work item**, leaving research choices to you.
- `implement-spec`: implement an agreed work item and record checks and decisions.
- `review-spec`: review the work against its specification and report evidence and remaining issues.

The canonical skill files live in `skills/`. Discovery copies for supported clients live in `.agents/skills/` and `.claude/skills/`. Client behaviour differs; the instructor will explain invocation for your client. If a skill is not discovered automatically, explicitly ask the agent to read the relevant `skills/<name>/SKILL.md` and follow it for the task.

**A finished `research-figure` skill is deliberately not included.** You create it in Exercise 04, apply it to two different inputs, inspect what it did, and revise it.

After creating or editing the canonical skill, run:

```bash
python tools/check_skill.py research-figure
python tools/sync_skills.py
```

Use the environment's Python command described above. The first command checks basic file structure and linked references; it cannot verify that the instructions are good or that an agent followed them. The second updates only this project's discovery copies. Edit `skills/`, then sync, rather than editing several copies separately. Begin a fresh agent session if your client needs one to discover a changed skill.

## Research choices and missing values

Read the variable-specific definitions. In the survey, `-8` and `-9` identify special missing responses; `-7` marks a documented inapplicable value in a conditional field. Do not assume every negative number has the same meaning. Zero can be a substantive value: for example, no paid hours or no commute for a remote worker.

A specification is not a complete project plan. It should name one deliverable, its scope, the research decisions it depends on, and its checks. A project can contain several such work items. Do not let an agent silently choose the analysis group, missing-value treatment or model on your behalf.

## When an agent pauses or your allowance runs out

Read the request before approving it. Explain the task boundary or ask the instructor if you cannot judge the action. Keep the work within this isolated teaching project.

If usage is unavailable, keep working with the supplied files and any outputs you already have. Read the codebook, inspect the script, write a specification, verify a small calculation, or prepare a handover. Ask about paired work or a checkpoint. Record which work you completed and which results you personally checked.

Before closing a session, save the agreed decisions, the commands that work, completed checks and the next action in project files. The next session should be able to continue from those files.

## The final challenge uses a new project

The Northbridge capstone has a separate client pack and new simulated data. Start it from an **empty folder outside this starter**. You will decide how to organise and configure that project, which skills to reuse or create, and how to divide the commission into bounded work items. Do not begin by copying the whole starter project.
