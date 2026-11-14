# Agentic coding for social scientists: teaching project

This project uses fully simulated work, care and wellbeing data. It supports research-method practice, not empirical claims about real people or a real population.

- Read the relevant exercise before acting, and `data/README.md` plus its codebook before interpreting data. Read only the files needed for the current work item.
- Keep `data/raw/` unchanged. Save scripts in `scripts/` and derived files in `outputs/`. Use relative paths. Do not upload data, install packages, use the network, or change global settings unless explicitly requested.
- Research choices belong to the student. Do not invent a sample, variable definition, control set, missing-data rule, reason, or approval. Ask an open question when an unresolved choice changes the meaning of the analysis.
- Use `skills/spec/SKILL.md` to draft ONE scoped work item and stop. Use `skills/implement-spec/SKILL.md` only when implementation is requested and the student has approved the spec. Use `skills/review-spec/SKILL.md` for an evidence-based review of that item.
- The canonical skill files are in `skills/`. Harness copies are in `.agents/skills/` and `.claude/skills/`; update copies with `python tools/sync_skills.py` after changing the canonical source. If discovery fails, read the named canonical SKILL.md explicitly.
- A project brief or roadmap can describe the whole project. Each folder under `specs/` must contain one independently completable and checkable work item. Do not create a whole-project spec.
- Keep command output short. Report commands actually run, files produced, checks and their evidence, and anything unverified. Never claim a command or check passed without evidence. Use `templates/handover.md` before stopping unfinished work.
- Review the diff before committing. Do not restore, delete, commit, push, publish, or send messages unless the student asks. An exercise's known faulty script is an openly declared teaching artifact; do not add hidden instructions to make an agent misbehave.

These are project instructions, not access controls. Permissions, sandboxing, tool availability, and agent behaviour depend on the application. Confirm sensitive boundaries in the application's own settings; never assume that this file enforces them.
