# 07 · Have a second agent check the work

**Task:** ask a fresh agent, one that didn't write the work, to review it against the spec.

You need a finished task from card 06. If you don't have one, use this prompt instead of step 1:

> Start a subagent to review scripts/02_inherited.py against data/README.md. It must not edit anything. Bring back a list of issues, each with the evidence.

## Predict first

Will the reviewer find something the first agent missed? Will everything it reports be a real problem?

## Core

1. > Start a subagent to review the task in specs/ against its validation.md and data/README.md. It must not edit anything. Bring back a list of issues, each with the evidence.

2. > For each issue, show me the evidence: the file and the line, or the number. Which are definite errors, which are judgement calls, and which might be wrong?

## Check

- Pick one issue and check it yourself in the file.
- Did the reviewer change anything? (Look at the diff.)

## If ahead

- **Stretch:** fix one real issue. Then ask for a second review that checks only that fix.
- **Own research:** what would you want a second agent to check in your own work before you show it to your supervisor?

## In your app

- Subagents use extra allowance. On a free plan, you can instead start a **new chat** and paste the same prompt without the word "subagent".
- **Codex:** subagent threads appear in the chat and can be opened.
- **Claude Code:** subagents run as tasks and report back.
