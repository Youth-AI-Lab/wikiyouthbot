# Youth Ai Lab — WikiYouthBot

Chatbots and robot prototypes built by young people during the WikiYouthBot intensive weeks. Each production is a self-contained HTML page, published as the group left it at the end of the week.

Production URL: <https://youth-ai-lab.github.io/wikiyouthbot/>

## Structure

```
wikiyouthbot/
├── README.md
├── index.html                       Landing page, one section per lab
├── cornicello.svg                   Lucky-charm icon shared by the pages
└── france/                          Lab Les Pacman's, La Rochelle, 27 to 31 July 2026
    ├── feurisson/index.html         Fire prevention chatbot, answers only in verse
    ├── superbot/index.html          School bullying chatbot, answers from a sourced base
    └── robo-caillou/index.html      Robot prototype, wildfire vigilance and ember control
```

## Notes on the published versions

The pages are published as the groups built them, with two adaptations made for public hosting and documented here.

- **Superbot**: the field inviting a visitor to paste an Anthropic API key is hidden, and the surrounding text now explains that this version answers from the base built by the group. The knowledge base, the detection rules and every answer are unchanged. Open the original file locally to use the free-question mode with your own key.
- **Feurisson**: the published page runs in offline demonstration mode. The exchanges shown are real answers produced by the chatbot during the workshop and frozen into the page, so that the production can be consulted without an API key.

## Local preview

Open `index.html` directly in a browser, or serve the folder:

```
python3 -m http.server 8000
```

Then browse to <http://localhost:8000/>.

## Safety

Neither chatbot is an emergency service. Fire: 18, or 112 in Europe, or 114 by SMS. School bullying: 3018. Child in danger: 119.
