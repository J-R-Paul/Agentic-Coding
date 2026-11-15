# Agentic coding for social scientists: course project

This is the project you will work in during the course (Heriot-Watt, Thursday 26 November 2026). It holds a **simulated** survey of 2,000 adults covering work, care and wellbeing, a few small scripts, and the exercise cards.

You won't need to type commands. You ask the agent, it proposes what to run, and you approve or decline.

## Before the course (about 20 minutes)

### 1. Get the project

On the course's GitHub page choose **Code → Download ZIP**, then unzip it somewhere you can find, such as `Documents`. Keep it apart from your real research files.

(Can't install software on your laptop? Use [the browser-only route](CODESPACES.md) instead.)

### 2. Install an agent

Install the **ChatGPT desktop app** and sign in with your ChatGPT account. A free account is enough. Open Codex in the app.

If you already use Claude Code, or Codex in VS Code, you can use that instead. Each exercise card says where your app differs.

### 3. Open the project

In the app, open this folder (the one containing this README) as your project. When it asks whether to **trust** the folder, say yes.

### 4. Paste the setup prompt

Copy this into the chat:

> Set up this project for the course. Find a Python 3.10 or newer on this computer. Create a Python environment called `.venv` inside this folder and install `requirements.txt` into it. Then use that environment to run `scripts/00_check_environment.py`, `scripts/check_data.py` and `scripts/01_first_output.py`. Also check whether git is installed. Tell me in plain words what worked, what didn't, and what I need to do.

The agent will ask to use the internet to download packages. Read the request, then approve it.

If Python or git is missing, ask the agent to explain how to install it on your computer, then follow its steps. It can't install system software for you without your approval.

### 5. Check it worked

You're ready when:

- `outputs/01-first-output/age_distribution.png` exists. Open it: it's a histogram of ages.
- The agent reports that the environment check and the data check passed.
- The agent reports a git version.

If you get stuck, copy the agent's last message and email it to us before the course. Please don't spend your free allowance asking it to retry the same thing over and over.

## On the day

The exercise cards are in `exercises/`. We'll tell you when to start each one. Every card has a **Core** part, plus **If ahead** parts for anyone who finishes early.

## What's in here

| Path | What it is |
|---|---|
| `AGENTS.md` | Instructions the agent reads at the start of every chat (`CLAUDE.md` points to it) |
| `data/raw/work_care_wellbeing.csv` | The survey. Never edit it. |
| `data/README.md` | The codebook. Read it before trusting any number. |
| `data/fixtures/` | Small tables for plotting and hand checks |
| `scripts/` | Small analysis scripts. One of them is deliberately wrong. |
| `exercises/` | The exercise cards |
| `permissions/ask-first.toml` | Strict permission settings, used in Exercise 01 |
| `.agents/skills/` | Skills for Codex (`.claude/skills/` is the same, for Claude Code) |
| `specs/`, `notes/` | Where your specs and notes go |

All the data are invented. Don't bring real or confidential research data to these exercises.
