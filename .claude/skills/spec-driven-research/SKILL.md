---
name: spec-driven-research
description: Plan, carry out and check one piece of research work through written specs. Use when the researcher wants to set up project files (mission, tech stack, roadmap), plan a roadmap item, implement an agreed spec, validate finished work, or pick up the next task in a new session.
---

# Spec-driven research

Work through files, not chat history. A new session must be able to continue from the files alone.

## Files

```
specs/
  mission.md        what the project is for, who it is for, its rules
  tech-stack.md     language, packages, data locations, commands that run things
  roadmap.md        numbered list of small tasks: next, later, done
  log.md            one line per finished task (date, task, result), append only
  YYYY-MM-DD-short-name/      one folder per task
    requirements.md goal, scope (in and out), what done looks like
    plan.md         the steps, in small groups that can each be checked
    validation.md   checks that could fail, with expected values where known
    decisions.md    choices made along the way, who made them, and why
```

Outputs go in `outputs/<short-name>/`, scripts in `scripts/`, as `AGENTS.md` says.

## Asking questions

- Ask **one question at a time** and wait for the answer.
- Ask open questions. **Do not suggest answers, list options or give a recommendation**, unless the researcher explicitly asks for help with that question. If they do, label it as a suggestion and wait for their choice.
- Ask about anything that would change the numbers or the claim: who is in the sample, how each variable is defined, missing and special codes, the method, the output. Do not ask about things that cannot change the result, such as file names or code style.
- Check facts (column names, codes, units) in the codebook yourself instead of asking.
- Record only what the researcher actually decided. If a decision is still open, write it down as open.

## 1. Project files (once per project)

If `specs/mission.md` does not exist, interview the researcher, then write `mission.md`, `tech-stack.md`, `roadmap.md` and an empty `log.md`. Keep each one short. The roadmap is a list of small tasks; each should be doable and checkable in one sitting. Show the files and stop for review.

## 2. Plan one task

1. Read `specs/mission.md`, `tech-stack.md`, `roadmap.md`, `log.md`, and the `requirements.md` and `decisions.md` of any finished task this one depends on.
2. Confirm which roadmap item this is. Create `specs/YYYY-MM-DD-short-name/` (today's date).
3. Interview the researcher as above.
4. Write `requirements.md`, `plan.md` and `validation.md`. Every check in `validation.md` must be able to fail. Prefer checks with a number you can compare against, such as a count from the raw file or one value worked out by hand.
5. Show the three files and stop. **Do not write or run analysis code until the researcher has approved them.**

## 3. Implement

1. Read the task's three files. Follow `plan.md`, one group of steps at a time if asked.
2. If something comes up that would change the research design, stop and ask. Do not decide it yourself.
3. Record any choices in `decisions.md`, with who made them.
4. Run the code from a clean start and report what you ran and what it produced.

## 4. Validate

1. Go through `validation.md` check by check. Add a `## Completed` section with each check, its result (pass / fail / not checked) and the evidence (a number, a file, a line of output).
2. Never mark a check as passed without evidence.
3. If the researcher asks for a change, change the spec files **and** the code together, so they stay in step.

## 5. Close out

1. Add one line to `specs/log.md`.
2. Tick the task in `specs/roadmap.md` and note anything learned that affects later tasks.
3. Ask the researcher whether the next roadmap item still looks right.
