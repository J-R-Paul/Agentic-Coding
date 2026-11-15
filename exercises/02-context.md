# 02 · See what fills the context

**Task:** watch the context grow, then shrink it.

## Predict first

Which do you think adds more to the context: the agent reading the whole data file, or the agent writing you a five-line summary of it?

## Core

1. Check how much context your chat is using (see *In your app*). Write the number down.
2. > Summarise data/raw/work_care_wellbeing.csv in five lines: number of rows, the columns, and the special missing-value codes.

   Check the context again.

3. > Now print the first 300 rows of that file in full.

   Check again. **Watch and record:** how much did each step add?

## Check

- What does each tool result cost you for the rest of this chat?

## If ahead

- **Stretch:** compact the chat with `/compact`. (In Claude Code you can add a focus note: `/compact keep only what we learned about missing-value codes`.) Then ask *"What are the missing-value codes?"* Is the answer still right? What got lost?
- **Stretch:** ask *"Which of the files you've read this session were actually needed?"*
- **Own research:** which files in your own project would flood the context if an agent read them whole? (Large data, logs, PDFs…)

## In your app

- **Codex:** type `/status` to see the context used and your remaining limits. Use `/compact` to compact.
- **Claude Code:** `/context` shows a breakdown by part. `/compact` compacts.
