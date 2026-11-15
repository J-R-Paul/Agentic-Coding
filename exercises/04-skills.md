# 04 · Build your plotting skill

**Task:** write down, once, how you like research figures to look, as a skill the agent loads whenever it makes a plot.

## Predict first

When the agent saves the new skill into `.agents/skills/`, will it ask your permission? Why or why not?

## Core

1. > Help me create a project skill called plotting, saved in .agents/skills/plotting/. Interview me first, one question at a time, about how I want research figures to look: colours, lines, labels, titles, source note, file formats. Give me two or three options for each question. If you have a skill-creator skill, use it.

   Answer its questions. **Watch and record:** did saving the skill ask for approval?

2. Open `.agents/skills/plotting/SKILL.md`. Read the description at the top: is that when you'd want it used?
3. Start a **new chat**, then:

   > Make a chart from data/fixtures/care_hours_by_age.csv showing the estimate and its confidence interval for each age group. Tell me which skill files you read.

   Open the figure.

## Check

- Does the figure follow *your* answers from step 1?
- Did the agent read the skill? (Its answer, and the list of actions in the chat, will show you.) If it didn't, what would you change in the skill's description?

## If ahead

- **Stretch:** use the same skill on `data/fixtures/life_satisfaction_by_status.csv`. Does it still work for a different measure and different groups?
- **Stretch:** pick one thing you don't like in the figures. Ask the agent to change **the skill**, not the figure, then make both figures again.
- **Stretch:** browse a skill library (e.g. github.com/anthropics/skills). Read one skill the way you'd review it: what would it make your agent do?
- **Own research:** what task do you repeat in your own work that could be a skill? (A table style, a referencing format, a data-cleaning routine…) Write its name and a one-sentence description.

## In your app

- **Codex:** skills live in `.agents/skills/`. Type `$` to pick a skill by name. `$skill-creator` helps build one.
- **Claude Code:** skills live in `.claude/skills/`. Ask the agent to save it there instead, or to copy it there afterwards.
- **If the skill isn't picked up:** say *"Read .agents/skills/plotting/SKILL.md and follow it."*
