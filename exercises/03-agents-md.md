# 03 · Give a folder its own README

**Task:** keep `AGENTS.md` short, and move notes about one folder into that folder.

## Predict first

In a brand-new chat, before it opens anything, does the agent already know that `scripts/02_inherited.py` is a bad script? What would make it know?

## Core

1. Open `AGENTS.md` and read it. Which parts are about the whole project, and which are only about one folder?
2. > AGENTS.md has a long section about the scripts. Move it into scripts/README.md. In AGENTS.md, replace it with one line: "Before working in a folder, read its README.md." Show me both files.

3. Start a **new chat**, then:

   > Which script makes the age histogram, and which script should I not trust? Tell me which files you read to find out.

   **Watch and record:** which files did it open? Did it find the answer?

## Check

- Could someone new to the project (a person or an agent) find what they need from these files alone?
- What does `AGENTS.md` still contain that every chat needs?

## If ahead

- **Stretch:** `AGENTS.md` also has a "Data notes" section, and `data/README.md` already exists. Ask the agent to compare the two and say what's duplicated. Then decide yourself what to keep where.
- **Stretch:** new chat: *"Using only the files in this project, explain what this project is and what I must never do."* Fix anything it got wrong by changing a file, not by telling it in chat.
- **Stretch:** ask the agent to keep a log. *"Create notes/log.md and add one line at the end of each task saying what was done and what's next."* Then do any small task and check the line appears.
- **Own research:** write the first ten lines of an `AGENTS.md` for your own thesis project: what it is, where the data lives, what must never be touched, how to run things. Don't use real data here.

## In your app

- **Codex** reads `AGENTS.md` automatically at the start of each chat. `/init` drafts one for a new project.
- **Claude Code** reads `CLAUDE.md`, which here just points to `AGENTS.md`.
