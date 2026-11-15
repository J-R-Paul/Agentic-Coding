# 05 · Commit, change, undo: all by asking

**Task:** use git as a safety net without typing a single git command.

## Predict first

Will the agent need your approval to make a commit? (Think back to card 01.)

## Core

1. > Is this folder tracked by git? If not, set it up. Then commit everything with a clear message.

   **Watch and record:** which steps asked for approval?

2. > Restyle the age histogram with a dark background, and run the script.

   Open the figure.

3. > Show me exactly what changed since the last commit: first in plain words, then as a diff.

   Also open your app's diff view.

4. > I don't like it. Undo that change, and only that change. Then run the script again so the figure matches.

5. > Show me the history, one line per commit.

## Check

- Is the figure back to how it was?
- Why did step 4 need to re-run the script? (Hint: is `outputs/` in git? Ask the agent about `.gitignore`.)

## If ahead

- **Stretch:** *"Commit scripts/02_inherited.py as it is. Then check how it treats missing values against data/README.md and fix only that."* Read the diff yourself: did it stop counting −8 and −9 as zero, while keeping real zeros? Commit with a clear message.
- **Stretch:** *"Which files would I never want to push to GitHub, and why? Are they in .gitignore?"*
- **Own research:** what in your own project is not in git but should be, and what is in git but shouldn't be?

## In your app

- **Codex desktop app:** it has a diff pane and git buttons next to the project. Use them to see what the agent did.
- **VS Code:** the Source Control panel shows the same diff.
- If git isn't installed, the agent will say so. Ask it how to install git on your computer.
