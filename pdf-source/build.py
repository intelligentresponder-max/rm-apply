import markdown, re, pathlib

SRC = pathlib.Path(__file__).resolve().parent
OUT = SRC / "bewerbung.html"

def md_to_html(text):
    return markdown.markdown(text, extensions=["sane_lists"])

# --- 1. Anschreiben ---
anschreiben_raw = (SRC / "01-ANSCHREIBEN.md").read_text(encoding="utf-8")
# Strip the top metadata block (title + betreff/adressat/stand + ---), keep body from "Hallo Roman," onward
body_start = anschreiben_raw.index("Hallo Roman,")
anschreiben_body_md = anschreiben_raw[body_start:]
anschreiben_body_html = md_to_html(anschreiben_body_md)

anschreiben_html = f"""
<section class="letter">
  <div class="sender">
    André Schwarz &middot; Am Lausberg 8 &middot; 60435 Frankfurt am Main &middot; andre.schwarz1@t-online.de &middot; 01525 6044541
  </div>
  <div class="letterhead">
    <div class="recipient">
      Roman Mayer GmbH<br>
      Roman Mayer<br>
      Ferdinand-Happ-Stra&szlig;e 53<br>
      60314 Frankfurt am Main
    </div>
    <div class="date">Frankfurt am Main, 10. September 2026</div>
  </div>
  <div class="subject">Bewerbung als Copywriter (m/w/d) &ndash; Frankfurt</div>
  <div class="letter-body">
    {anschreiben_body_html}
  </div>
</section>
"""

# --- Anlagen 2-6, in PDF order ---
anlagen = [
    ("Anlage 1", "Antragsarchiv Ortsbeirat 10", "02-ANLAGE-Antragsarchiv.md"),
    ("Anlage 2", "Arbeitsproben im &Uuml;berblick", "06-ANLAGE-Arbeitsproben.md"),
    ("Anlage 3", "GEO &mdash; Generative Engine Optimization", "03-ANLAGE-GEO.md"),
    ("Anlage 4", "CROWN v10 &mdash; Value-Betting-System", "04-ANLAGE-CROWN.md"),
    ("Anlage 5", "Human Design", "05-ANLAGE-HumanDesign.md"),
]

anlagen_html_parts = []
for label, title, fname in anlagen:
    raw = (SRC / fname).read_text(encoding="utf-8")
    # drop the first H1 line (# Anlage - ...), keep everything after it
    lines = raw.split("\n")
    assert lines[0].startswith("# "), fname
    body_md = "\n".join(lines[1:]).strip()
    body_html = md_to_html(body_md)
    anlagen_html_parts.append(f"""
<section class="anlage">
  <div class="anlage-label">{label}</div>
  <h1 class="anlage-title">{title}</h1>
  {body_html}
</section>
""")

anlagen_html = "\n".join(anlagen_html_parts)

full_html = f"""<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="UTF-8">
<title>Bewerbung Andre Schwarz - Roman Mayer GmbH</title>
<style>
  @page {{
    size: A4;
    margin: 26mm 22mm 22mm 22mm;
  }}
  * {{ box-sizing: border-box; }}
  html, body {{
    margin: 0; padding: 0;
    font-family: Georgia, 'Times New Roman', serif;
    font-size: 11pt;
    line-height: 1.55;
    color: #1a1a1a;
  }}
  section.letter, section.anlage {{
    page-break-after: always;
  }}
  section.anlage:last-of-type {{
    page-break-after: auto;
  }}

  /* Letterhead */
  .sender {{
    font-size: 9pt;
    color: #555;
    padding-bottom: 6pt;
    margin-bottom: 22pt;
    border-bottom: 0.5pt solid #ddd;
  }}
  .letterhead {{
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    margin-bottom: 30pt;
  }}
  .recipient {{
    font-size: 10.5pt;
    line-height: 1.5;
    text-align: left;
  }}
  .date {{
    font-size: 10pt;
    color: #444;
    white-space: nowrap;
  }}
  .subject {{
    font-weight: bold;
    font-size: 12.5pt;
    margin: 18pt 0 20pt 0;
  }}
  .letter-body p {{
    margin: 0 0 11pt 0;
    text-align: justify;
  }}
  .letter-body h2 {{
    font-size: 12pt;
    font-weight: bold;
    margin: 20pt 0 8pt 0;
    color: #111;
  }}
  .letter-body blockquote {{
    margin: 16pt 0 16pt 0;
    padding-left: 14pt;
    border-left: 2pt solid #a8854a;
    font-style: italic;
    color: #333;
  }}
  .letter-body blockquote p {{
    margin: 0;
  }}

  /* Anlagen */
  .anlage-label {{
    font-size: 9pt;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: #888;
    margin-bottom: 4pt;
  }}
  h1.anlage-title {{
    font-size: 16pt;
    font-weight: bold;
    margin: 0 0 16pt 0;
    padding-bottom: 8pt;
    border-bottom: 0.75pt solid #ccc;
  }}
  .anlage h2 {{
    font-size: 12pt;
    font-weight: bold;
    margin: 18pt 0 7pt 0;
  }}
  .anlage p {{
    margin: 0 0 10pt 0;
    text-align: justify;
  }}
  .anlage strong {{ font-weight: bold; }}
  .anlage em {{ font-style: italic; }}
  .anlage hr {{
    border: none;
    border-top: 0.75pt solid #ddd;
    margin: 16pt 0;
  }}
</style>
</head>
<body>
{anschreiben_html}
{anlagen_html}
</body>
</html>
"""

OUT.write_text(full_html, encoding="utf-8")
print("written", OUT, len(full_html), "chars")
