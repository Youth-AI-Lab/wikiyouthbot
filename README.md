# Youth Ai Lab — WikiYouthBot

Everything produced around the WikiYouthBot intensive week: the chatbots and robot prototypes built by the participants, the documentation of the Claude Projects behind them, and the facilitation kit used to run the week.

Production URL: <https://youth-ai-lab.github.io/wikiyouthbot/>

## Structure

```
wikiyouthbot/
├── README.md
├── index.html                       Landing page: productions, documentation, facilitation kit
├── style.css                        Shared styles for the landing
├── cornicello.svg                   Lucky-charm icon shared by the pages
├── build.py                         Rebuilds the documentation pages from the markdown sources
├── france/                          Lab Les Pacman's, La Rochelle, 27 to 31 July 2026
│   ├── feurisson/index.html         Fire prevention chatbot, answers only in verse
│   ├── superbot/index.html          School bullying chatbot, answers from a sourced base
│   └── robo-caillou/index.html      Robot prototype, wildfire vigilance and ember control
├── projects/
│   ├── source/                      Markdown sources, edit these
│   │   ├── feurisson.md
│   │   ├── superbot.md
│   │   └── feurisson-mascotte.png
│   ├── feurisson/index.html         Generated, do not edit by hand
│   └── superbot/index.html          Generated, do not edit by hand
└── tools/                           Facilitation kit
    ├── mission/index.html           Mission of the week, sealed envelope and roadmap
    ├── press-conference/index.html  Voice AI press conference device
    ├── key-data-cards/index.html    Printable field enquiry cards
    ├── location-sheets/index.html   Printable location sheets
    └── evidence-wall/index.html     Printable press cuttings to sort
```

## Rebuilding the documentation pages

The two documentation pages are generated from `projects/source/*.md`. Edit the markdown, then run:

```
python3 build.py
```

No dependency is needed, the converter is part of the script.

## Notes on the published versions

The productions are published as the groups built them, with the adaptations below made for public hosting.

- **Superbot**: the field inviting a visitor to paste an Anthropic API key is hidden, and the surrounding text explains that this version answers from the base built by the group. The knowledge base, the detection rules and every answer are unchanged.
- **Feurisson**: the page was calling the Anthropic API without any key, which only worked inside the workshop setup. A key panel was added, on the same pattern as Superbot, so that a visitor with their own key can use it. The chatbot's instructions, character and content are unchanged. The dataset block of the page is still empty: the handwritten cards were transcribed after the week and can be found in `projects/source/feurisson.md`.
- **Press conference**: no key is embedded. Each user provides their own, a free Gemini key being enough. The tool works best served from a local machine, because browsers ask for microphone permission again on every reload of a file opened directly.

## Local preview

```
python3 -m http.server 8000
```

Then browse to <http://localhost:8000/>.

## Safety

Neither chatbot is an emergency service. Fire: 18, or 112 in Europe, or 114 by SMS. School bullying: 3018. Child in danger: 119.
