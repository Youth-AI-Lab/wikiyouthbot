#!/usr/bin/env python3
"""Build the documented Claude Project pages from the markdown sources.

Usage:  python3 build.py

Reads projects/source/*.md and writes projects/<name>/index.html.
The markdown subset covered is the one used by those sources: headings,
paragraphs, bullet and numbered lists, pipe tables, horizontal rules,
bold, italics, inline code and links.
"""

import html
import os
import re

ROOT = os.path.dirname(os.path.abspath(__file__))

PAGES = [
    {
        "src_fr": "projects/source/feurisson.md",
        "src_en": "projects/source/feurisson.en.md",
        "out": "projects/feurisson/index.html",
        "title": "Feurisson · documented Claude Project",
        "accent": "#f37030",
        "accent_soft": "#ffd5c1",
        "back": "../../",
    },
    {
        "src_fr": "projects/source/superbot.md",
        "src_en": "projects/source/superbot.en.md",
        "out": "projects/superbot/index.html",
        "title": "Superbot · documented Claude Project",
        "accent": "#38b6ff",
        "accent_soft": "#cbecff",
        "back": "../../",
    },
]


def inline(text):
    """Render the inline markdown constructs, escaping everything else."""
    out = []
    pattern = re.compile(
        r"!\[([^\]]*)\]\(([^)]+)\)"         # image
        r"|\[([^\]]+)\]\(([^)]+)\)"          # link
        r"|\*\*([^*]+)\*\*"                  # bold
        r"|`([^`]+)`"                        # code
        r"|\*([^*]+)\*"                      # italics
    )
    pos = 0
    for m in pattern.finditer(text):
        out.append(html.escape(text[pos:m.start()]))
        if m.group(2) is not None:
            src = m.group(2)
            dossier, fichier = src.rsplit("/", 1)
            vignette = dossier + "/thumbs/" + fichier
            out.append(
                '<a class="vignette" href="%s"><img src="%s" alt="%s" loading="lazy"></a>'
                % (html.escape(src, True), html.escape(vignette, True), html.escape(m.group(1)))
            )
        elif m.group(3) is not None:
            out.append('<a href="%s">%s</a>' % (html.escape(m.group(4), True), html.escape(m.group(3))))
        elif m.group(5) is not None:
            out.append("<strong>%s</strong>" % html.escape(m.group(5)))
        elif m.group(6) is not None:
            out.append("<code>%s</code>" % html.escape(m.group(6)))
        else:
            out.append("<em>%s</em>" % html.escape(m.group(7)))
        pos = m.end()
    out.append(html.escape(text[pos:]))
    return "".join(out)


def split_row(line):
    cells = line.strip().strip("|").split("|")
    return [c.strip() for c in cells]


def convert(md):
    lines = md.split("\n")
    out = []
    i = 0
    n = len(lines)
    while i < n:
        line = lines[i]
        stripped = line.strip()

        if not stripped:
            i += 1
            continue

        if stripped.startswith("#"):
            level = len(stripped) - len(stripped.lstrip("#"))
            out.append("<h%d>%s</h%d>" % (level, inline(stripped[level:].strip()), level))
            i += 1
            continue

        if re.fullmatch(r"-{3,}", stripped):
            out.append("<hr>")
            i += 1
            continue

        # table
        if stripped.startswith("|") and i + 1 < n and re.fullmatch(r"\|[\s|:-]+\|", lines[i + 1].strip()):
            head = split_row(stripped)
            i += 2
            rows = []
            while i < n and lines[i].strip().startswith("|"):
                rows.append(split_row(lines[i].strip()))
                i += 1
            out.append('<div class="tablewrap"><table>')
            out.append("<thead><tr>%s</tr></thead>" % "".join("<th>%s</th>" % inline(c) for c in head))
            out.append("<tbody>")
            for r in rows:
                out.append("<tr>%s</tr>" % "".join("<td>%s</td>" % inline(c) for c in r))
            out.append("</tbody></table></div>")
            continue

        # bullet list
        if stripped.startswith("- "):
            items = []
            while i < n and lines[i].strip().startswith("- "):
                items.append(lines[i].strip()[2:])
                i += 1
            out.append("<ul>%s</ul>" % "".join("<li>%s</li>" % inline(it) for it in items))
            continue

        # numbered list
        if re.match(r"\d+\.\s", stripped):
            items = []
            while i < n and re.match(r"\d+\.\s", lines[i].strip()):
                items.append(re.sub(r"^\d+\.\s", "", lines[i].strip()))
                i += 1
            out.append("<ol>%s</ol>" % "".join("<li>%s</li>" % inline(it) for it in items))
            continue

        # paragraph, joining the following non-blank lines
        para = [stripped]
        i += 1
        while i < n and lines[i].strip() and not re.match(r"^(#|-\s|\||\d+\.\s|-{3,})", lines[i].strip()):
            para.append(lines[i].strip())
            i += 1
        out.append("<p>%s</p>" % inline(" ".join(para)))

    return "\n".join(out)


TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<link rel="icon" href="../../favicon.svg">
<meta property="og:type" content="article">
<meta property="og:site_name" content="Youth Ai Lab">
<meta property="og:title" content="{title}">
<meta property="og:image" content="https://youth-ai-lab.github.io/wikiyouthbot/og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="https://youth-ai-lab.github.io/wikiyouthbot/og.png">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:wght@400;700;800&family=Manrope:wght@400;500;600;700&display=swap');
  :root {{ --bg:#ffffff; --ink:#1a1a1a; --soft:#6c6c6c; --accent:{accent}; --accent-soft:{accent_soft}; }}
  * {{ box-sizing:border-box; margin:0; padding:0; }}
  html, body {{ background:var(--bg); color:var(--ink); font-family:'Manrope',system-ui,sans-serif; }}
  .wrap {{ max-width:900px; margin:0 auto; padding:44px 24px 90px; }}
  .back {{ display:inline-block; font-size:.9rem; font-weight:700; text-decoration:none; color:var(--ink);
          background:var(--accent-soft); border:2px solid var(--ink); border-radius:999px; padding:6px 14px; margin-bottom:30px; }}
  h1 {{ font-family:'Bricolage Grotesque',system-ui,sans-serif; font-size:clamp(1.9rem,4.4vw,2.7rem); font-weight:800; line-height:1.1; margin-bottom:22px; }}
  h2 {{ font-family:'Bricolage Grotesque',system-ui,sans-serif; font-size:1.5rem; font-weight:700; margin:44px 0 14px; padding-bottom:8px; border-bottom:3px solid var(--accent); }}
  h3 {{ font-family:'Bricolage Grotesque',system-ui,sans-serif; font-size:1.16rem; font-weight:700; margin:30px 0 10px; }}
  p {{ line-height:1.7; margin:0 0 14px; text-align:justify; text-justify:inter-word; hyphens:auto; }}
  ul, ol {{ margin:0 0 16px 22px; }}
  li {{ line-height:1.7; margin-bottom:6px; text-align:justify; text-justify:inter-word; hyphens:auto; }}
  hr {{ border:0; border-top:2px solid #e6e6e6; margin:34px 0; }}
  code {{ background:#f2f2f2; padding:1px 5px; border-radius:5px; font-size:.92em; }}
  a {{ color:#1a1a1a; }}
  .vignette {{ display:inline-block; margin:4px 0 18px; border:2px solid var(--ink); border-radius:12px;
             overflow:hidden; line-height:0; background:#fff; max-width:320px; }}
  .vignette img {{ display:block; width:100%; height:auto; }}
  .vignette:hover {{ box-shadow:4px 4px 0 var(--ink); transform:translate(-2px,-2px); }}
  .vignette {{ transition:transform .15s ease, box-shadow .15s ease; }}
  .tablewrap {{ overflow-x:auto; margin:0 0 22px; border:2px solid var(--ink); border-radius:14px; background:#fff; }}
  table {{ border-collapse:collapse; width:100%; min-width:520px; font-size:.94rem; }}
  th, td {{ text-align:left; padding:11px 14px; border-bottom:1px solid #e6e6e6; vertical-align:top; line-height:1.55; }}
  th {{ background:var(--accent-soft); font-weight:700; }}
  tbody tr:last-child td {{ border-bottom:0; }}
  .topbar {{ display:flex; flex-wrap:wrap; gap:10px; align-items:center; justify-content:space-between; margin-bottom:28px; }}
  .langbar {{ display:flex; gap:0; border:2px solid var(--ink); border-radius:999px; overflow:hidden; }}
  .langbar button {{ font:inherit; font-size:.86rem; font-weight:700; padding:6px 15px; border:0; background:#fff; color:var(--ink); cursor:pointer; }}
  .langbar button[aria-pressed="true"] {{ background:var(--ink); color:#fff; }}
  .langnote {{ font-size:.86rem; color:var(--soft); margin:-10px 0 26px; }}
  body[data-lang="en"] [lang="fr"], body[data-lang="fr"] [lang="en"] {{ display:none; }}

.haut {{
  position: fixed; right: 20px; bottom: 20px; z-index: 50;
  width: 46px; height: 46px; border-radius: 999px; cursor: pointer;
  border: 2px solid var(--ink); background: #fff; color: var(--ink);
  font: 700 1.15rem/1 'Manrope', system-ui, sans-serif;
  box-shadow: 3px 3px 0 var(--ink);
  opacity: 0; visibility: hidden; transform: translateY(8px);
  transition: opacity .18s ease, transform .18s ease, visibility .18s;
}}
.haut.visible {{ opacity: 1; visibility: visible; transform: none; }}
.haut:hover {{ box-shadow: 5px 5px 0 var(--ink); transform: translate(-2px, -2px); }}
.horstexte {{
  position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px;
  overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; border: 0;
}}
@media (max-width: 620px) {{ .haut {{ right: 14px; bottom: 14px; }} }}

dialog.visionneuse {{ border:0; padding:0; background:transparent; max-width:100vw; max-height:100vh; }}
dialog.visionneuse::backdrop {{ background:rgba(0,0,0,.88); }}
dialog.visionneuse .cadre {{ position:relative; line-height:0; }}
dialog.visionneuse img {{ max-width:92vw; max-height:86vh; width:auto; height:auto; display:block; border-radius:12px; background:#fff; }}
dialog.visionneuse .fermer {{
  position:absolute; top:10px; right:10px; width:42px; height:42px; border-radius:999px; cursor:pointer;
  border:2px solid #1a1a1a; background:#fff; color:#1a1a1a; font:700 1.05rem/1 system-ui, sans-serif;
}}
dialog.visionneuse .fermer:hover {{ background:#f2f2f2; }}
  @media (max-width:640px) {{ .wrap {{ padding:28px 16px 70px; }} }}
</style>
</head>
<body data-lang="en">
<div class="wrap">
<div class="topbar">
  <a class="back" href="{back}"><span lang="en">← Back to the site</span><span lang="fr">← Retour au site</span></a>
  <div class="langbar" role="group" aria-label="Language">
    <button type="button" data-set="en" aria-pressed="true">English</button>
    <button type="button" data-set="fr" aria-pressed="false">Français</button>
  </div>
</div>
<p class="langnote" lang="en">English is a translation. The French version holds the participants' original wording.</p>
<p class="langnote" lang="fr">Version originale. La version anglaise en est une traduction.</p>
<div lang="en">
{body_en}
</div>
<div lang="fr">
{body_fr}
</div>
</div>

<dialog class="visionneuse">
  <div class="cadre">
    <img alt="">
    <button class="fermer" type="button" autofocus>
      <span class="horstexte" lang="en">Close</span>
      <span class="horstexte" lang="fr">Fermer</span>
      <span aria-hidden="true">✕</span>
    </button>
  </div>
</dialog>

<button class="haut" type="button">
  <span class="horstexte" lang="en">Back to top</span>
  <span class="horstexte" lang="fr">Haut de page</span>
  <span aria-hidden="true">↑</span>
</button>

<script>
(function(){{
  var boutons = document.querySelectorAll('.langbar button');
  boutons.forEach(function(b){{
    b.addEventListener('click', function(){{
      var l = b.dataset.set;
      document.body.dataset.lang = l;
      document.documentElement.lang = l;
      boutons.forEach(function(o){{ o.setAttribute('aria-pressed', String(o.dataset.set === l)); }});
      try {{ localStorage.setItem('wyb-lang', l); }} catch (e) {{}}
    }});
  }});
  var memo;
  try {{ memo = localStorage.getItem('wyb-lang'); }} catch (e) {{}}
  if (memo === 'fr' || memo === 'en') {{
    document.body.dataset.lang = memo;
    document.documentElement.lang = memo;
    boutons.forEach(function(o){{ o.setAttribute('aria-pressed', String(o.dataset.set === memo)); }});
  }}

  var haut = document.querySelector('.haut');
  if (haut) {{
    var basculer = function(){{ haut.classList.toggle('visible', window.scrollY > 400); }};
    window.addEventListener('scroll', basculer, {{passive:true}});
    basculer();
    haut.addEventListener('click', function(){{ window.scrollTo({{top:0, behavior:'smooth'}}); }});
  }}

  var visionneuse = document.querySelector('dialog.visionneuse');
  if (visionneuse) {{
    var grande = visionneuse.querySelector('img');
    document.querySelectorAll('a.vignette, button.shot').forEach(function(el){{
      el.addEventListener('click', function(e){{
        e.preventDefault();
        grande.src = el.dataset.full || el.getAttribute('href');
        var img = el.querySelector('img');
        grande.alt = img ? img.alt : '';
        visionneuse.showModal();
      }});
    }});
    visionneuse.querySelector('.fermer').addEventListener('click', function(){{ visionneuse.close(); }});
    visionneuse.addEventListener('click', function(e){{ if (e.target === visionneuse) visionneuse.close(); }});
    visionneuse.addEventListener('close', function(){{ grande.removeAttribute('src'); }});
  }}
}})();
</script>
</body>
</html>
"""


def main():
    for page in PAGES:
        out = os.path.join(ROOT, page["out"])
        bodies = {}
        for lang in ("fr", "en"):
            with open(os.path.join(ROOT, page["src_" + lang]), encoding="utf-8") as f:
                bodies[lang] = convert(f.read())
        os.makedirs(os.path.dirname(out), exist_ok=True)
        with open(out, "w", encoding="utf-8") as f:
            f.write(TEMPLATE.format(
                title=html.escape(page["title"]),
                accent=page["accent"],
                accent_soft=page["accent_soft"],
                back=page["back"],
                body_en=bodies["en"],
                body_fr=bodies["fr"],
            ))
        print("built", page["out"])


if __name__ == "__main__":
    main()
