# 06 · Spec-driven development

**Task:** set up the project's spec files, then take one task from plan to checked result.

We go one step at a time: the instructor shows a step, then you do it. Stuck on a step? Ask for the catch-up files for that step and carry on from there.

**Your project, in three sentences** (use these when the agent interviews you):

> We use a simulated survey of 2,000 adults to describe how work arrangements relate to commuting and wellbeing. The audience is a policy team who want clear descriptive tables first, then one simple regression. All results must say they come from simulated data.

Roadmap items to give it:

1. commute time by work arrangement (a table and a figure);
2. commute time and life satisfaction (a simple regression).

## a · Project files

> Use the spec-driven-research skill. Interview me, one question at a time, to write specs/mission.md, specs/tech-stack.md and specs/roadmap.md. Don't suggest answers.

Read the three files. Ask the agent to fix anything that's wrong; don't edit them yourself.

## b · Plan task 1

Start a **new chat**, then:

> Use the spec-driven-research skill to plan roadmap item 1. Ask me about every decision that would change the numbers.

**Predict first:** which decisions will it need from you? (Look at `commute_minutes` in `data/README.md`.)

Read `requirements.md`, `plan.md` and `validation.md`. Could each check in `validation.md` actually fail?

## c · Implement

Start a **new chat**, then:

> Implement the spec in specs/ for roadmap item 1. Commit when done.

## d · Validate and fix

> Go through validation.md check by check, fill in the Completed section with the evidence for each, and tell me anything that failed.

Then find one thing in the result you want changed, and ask the agent to change **the spec and the code together**.

## Check

- Does the table say which people it includes, and how many?
- What happened to the −7, −8 and −9 codes, and to the zeros?
- Is every pass in `validation.md` backed by a number or a file?

## If ahead

- **Stretch: the next task, in a fresh session.** Start a **new chat**: *"Use the spec-driven-research skill to plan the next roadmap item."* Watch which files it reads to find out where things stand. Then plan, implement and validate item 2.
- **Stretch:** ask the agent to close out task 1: a line in `specs/log.md` and a tick on the roadmap.
- **Own research:** write a `mission.md` and the first three roadmap items for your own thesis project. Don't use real data.

## In your app

- **Codex:** type `$spec-driven-research` to call the skill by name.
- **Claude Code:** type `/spec-driven-research`, or just name the skill.
- **If it isn't found:** say *"Read .agents/skills/spec-driven-research/SKILL.md and follow it."*
