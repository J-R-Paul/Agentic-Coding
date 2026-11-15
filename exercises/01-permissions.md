# 01 · Explore your permission settings

**Task:** watch which of the agent's actions ask for your approval, and work out why.

## Predict first

Before you start, tick the actions you think will **ask you** before they happen:

- [ ] (a) reading the data file
- [ ] (b) editing `scripts/01_first_output.py`
- [ ] (c) running that script
- [ ] (d) downloading a web page
- [ ] (e) saving a file to your Desktop

## Core

1. > Read AGENTS.md and scripts/01_first_output.py. Add a caption to the age histogram saying how many records were read, counted from the data, not typed in. Run the script and tell me where the figure is.

   **Watch and record:** which actions asked, and which just happened? Open the figure.

2. > Explain the change you made, line by line, for someone who doesn't read Python. Then list every action you took, and say which ones needed my approval and why.

3. > Save a copy of the figure to my Desktop.

   > Download https://www.gov.scot/ into data/.

   **Watch and record:** what happened? Decline both if asked.

4. > Read permissions/ask-first.toml and explain each line. Then switch it on for this project.

   Approve, then **start a new chat** so the settings take effect.

5. > Change the histogram bars to grey and run the script again.

   **Watch and record:** what asked this time? Count the approvals.

6. > Switch the ask-first settings off again.

   Approve, then **start a new chat**. The rest of the day uses the normal settings.

## Check

- Compare what happened with your predictions. Which ones surprised you?
- Why did the same kind of edit behave differently in step 1 and step 5?

## If ahead

- **Stretch:** open the app's settings and find its permission modes. Is there one where another AI reviews approval requests for you? What would you lose by using it?
- **Stretch:** ask the agent: *"What is your sandbox, and what can't you do inside it?"* Then check its answer against what you saw in steps 1–5.
- **Own research:** list three actions on your own project that you'd always want to approve by hand. Use the "sensitive × undoable" slide to decide.

## In your app

- **Codex (desktop app or VS Code):** approval requests appear in the chat. Start a new chat with the **+** / New chat button.
- **Claude Code:** it asks before edits by default and doesn't read `ask-first.toml`, so do steps 1–3 only. Then use `/permissions` to look at its rules.
