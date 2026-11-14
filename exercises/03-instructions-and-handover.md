# 03 — Give the next session a usable briefing

**25 minutes.** Turn the lessons from the repair into durable project context, then test the handover in a fresh session. You do not need an agent to forget or disobey for this exercise to work.

## Task and timing

**0–5 minutes:** Read `AGENTS.md`, `data/README.md`, the repair note and `templates/handover.md`. Identify three distinct kinds of information:

- A project-wide operating rule.
- A data-specific definition that belongs with the codebook.
- The current work item's status, evidence and next action.

**5–12 minutes:** Use the first prompt. Improve the briefing only where the current files are genuinely insufficient; duplication is not an improvement. Write `notes/03-handover.md` using the template. Include the exact working command, the repaired files and the check evidence. If a detail is unknown, say so.

**12–20 minutes:** Save all intended changes. Start a new conversation in the same project folder. Use the second prompt. Compare the new session's account with the saved evidence. You may explicitly direct it to a file; automatic loading differs between tools.

**20–25 minutes:** Correct one omission or ambiguity exposed by the handover. Save the revised note and inspect the diff.

## First prompt

> Read AGENTS.md, data/README.md, notes/02-repair.md and templates/handover.md. Help me leave a short, accurate handover for the repaired summary in notes/03-handover.md. Record the command that actually worked, the checks actually completed and one specific next action. Keep project-wide rules in AGENTS.md, data definitions in data/README.md and current-task status in the handover. Propose only necessary improvements; do not copy the whole codebook into AGENTS.md or invent missing evidence. Do not run a new analysis.

## Prompt for the fresh session

> Read AGENTS.md, data/README.md and notes/03-handover.md. Explain in no more than six sentences what this project contains, what was repaired, what evidence supports the repair and what the next authorized action is. Identify any consequential uncertainty. Do not edit or run anything yet.

## Deliverables and checks

Your deliverables are the useful improvements to the instructions and `notes/03-handover.md`.

- A new session can locate the raw input, relevant documentation, repaired script, output and checks.
- The note distinguishes completed checks from intended checks.
- It records an actual next action and its authorization boundary.
- Rules are short and located where they belong.
- No file claims that instructions themselves provide security or guarantee behaviour.

## Stop point

Stop when the fresh session can reconstruct the work from saved files and you have corrected any important gap. A perfect reproduction of the original conversation is unnecessary.

## Low-usage route

Swap the handover with a partner and ask them to locate the files and explain the next action using only the note. This tests the same documentation problem. If you cannot start another agent session, record that the handover was peer-tested rather than agent-tested.

## Optional extension

Draft a short project roadmap using `templates/project-brief-and-roadmap.md`. It may list several future deliverables, but do not turn it into a whole-project spec. Each future work item will need its own bounded completion criterion.

**Context lesson:** durable files are useful even when a client has conversation history or memory features. Long transcripts are harder to inspect and do not replace a precise research decision record.
