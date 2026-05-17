# Tutorials

> Guided in-app walkthroughs. Open **Help → Tutorials** to pick one.

## What a tutorial is

A tutorial is a step-by-step recipe that runs *inside HTMLook* — no switching tabs to a blog post, no copying-pasting screenshots. Each step highlights the exact button or pane you should click next, optionally loads a sample file for you to practise on, and (if it involves AI) drops a ready-to-send prompt into the assistant.

You can pause, resume across sessions, skip ahead, or stop at any time. Completed tutorials show ✅; pending ones show ▶.

## Where to find them

- **Help menu → Tutorials** — full library
- **First-launch onboarding** — HTMLook asks "what do you mostly do?" and suggests the most relevant tutorial for that role
- **Sidebar (when a sample workspace is open)** — the tutorial that matches the sample is offered at the top

## Library (built-in)

The library covers concrete workflows for 13 personas. Each unit is ~5 minutes.

| # | Tutorial | What you'll do |
|---|---|---|
| 01 | Markdown notes from a meeting transcript | Drop a transcript file, ask the assistant to clean it up speaker-by-speaker, export as PDF |
| 02 | Polish a one-page PDF report | Annotate, add citations, regenerate the layout |
| 03 | Storyboard a short video | Import the video, mark scenes, drop chapter titles |
| 04 | Comment on a contract clause | Open the PDF, highlight the clause, attach a Paint sketch, ask for a redline suggestion |
| 05 | Summarise a research paper | Open the PDF, ask for an outline + a 3-bullet abstract, save as Markdown |
| 06 | Build a slide deck from notes | Open a Markdown file, use Heading 1 as slide titles, export as `.pptx` |
| 07 | Voice memo → action items | Record a memo, transcribe, ask the assistant to extract action items |
| 08 | Compare two report drafts in dual view | Open both, ⌘⇧D, sync scroll, mark differences with Paint |
| 09 | Annotate a screenshot of a UI bug | Drop the image in, Paint to circle, ask for likely fix |
| 10 | Translate a document section | Select the text, ask the assistant to translate to a target language, paste back inline |
| 11 | Build a Mermaid diagram from a hand-drawn sketch | Drop the sketch image in, ask the assistant to produce Mermaid for it |
| 12 | Turn a workspace into a shareable bundle | Select files, Export → HTML self-contained, attach to email |
| 13 | Save your favourite prompt as a reusable button | Type the prompt in a terminal, click the bookmark icon to save it as a preset |

## What each tutorial actually does

Every step has up to four ingredients:

1. **What to click** — the target button/menu is highlighted with a soft pulse and an arrow
2. **Sample file** *(optional)* — a *Load sample* button drops a known-good file into your workspace's `__wizard__/` subfolder so you don't have to find your own
3. **Ready prompt** *(optional)* — a one-click button pastes a pre-written prompt into the active terminal or AI Assistant
4. **Next / Skip / Stop** at the bottom

## Sample workspaces

Some tutorials install a tiny sample workspace as a sibling folder so the lesson and your real files don't mix. Sample folders are prefixed `htmlook-sample-<slug>/` and are safe to delete after the tutorial.

## Resume + reset

Progress is saved automatically. Closing the app and re-opening it offers to resume where you stopped. If you'd rather start over, the *Reset* button next to each tutorial in the library wipes its progress.

## Next

- [Wizards →](Wizards.md)
- [Quick Start →](Quick-Start.md)
