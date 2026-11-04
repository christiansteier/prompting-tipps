# Prompting tips for your studies

[Deutsch](README.de.md) · **Live:** https://christiansteier.github.io/prompting-tipps/

A small static web page for students:

- **Build a prompt** from five blocks: context, role, task, format, check request.
- **Templates** for academic writing and exam preparation: fill in the placeholders and copy the result into an AI chat.
- **Brainstorming:** enter topic and goal, choose the AI's role (facilitator, creative partner, ideas for me) and 3–4 of 13 techniques. The copied prompt contains the full facilitation guide and works in any AI chat.
- **Good to know:** four prompting strategies, five tips, rules for coursework (your work stays yours, declare AI use, data protection).

German and English, works offline as a single file, dark mode, keyboard operable. Only your language choice is stored in the browser; your input is not saved.

## Build

Edit `quelle.html`, then run `python3 bauen.py`. It inserts the Lucide icons from `icons/` and the BMad technique icons from `bmad-icons.json` and writes `index.html`.

Colours follow the HSD palette (red, green, petrol, greys) without the HSD logo or typeface.

## Run locally

```bash
python3 -m http.server 8000
# open http://localhost:8000
```

## Licence

CC BY-NC-SA 4.0, Christian-Maximilian Steier, Hochschule Düsseldorf.

The brainstorming part is adapted from the brainstorming skill of [BMad Method](https://github.com/bmad-code-org/BMAD-METHOD) (MIT licence, © 2025 BMad Code, LLC, see `LICENSE-BMAD.txt`).
