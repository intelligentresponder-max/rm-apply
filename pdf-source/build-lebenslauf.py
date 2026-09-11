import pathlib
from bs4 import BeautifulSoup

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = REPO_ROOT / "lebenslauf.html"
OUT = pathlib.Path(__file__).resolve().parent / "lebenslauf-print.html"

soup = BeautifulSoup(SRC.read_text(encoding="utf-8"), "html.parser")


def text(el):
    return el.get_text(strip=True) if el else ""


def entries_html(container):
    """Render all .entry divs inside a container as print-CV entry blocks."""
    parts = []
    for entry in container.select(":scope > .entry"):
        title = text(entry.select_one(".entry-title"))
        date = text(entry.select_one(".entry-date"))
        org = text(entry.select_one(".entry-org"))
        desc = text(entry.select_one(".entry-desc"))
        parts.append(f"""
        <div class="entry">
          <div class="entry-head"><span class="entry-title">{title}</span><span class="entry-date">{date}</span></div>
          {f'<div class="entry-org">{org}</div>' if org else ''}
          {f'<div class="entry-desc">{desc}</div>' if desc else ''}
        </div>""")
    return "\n".join(parts)


# --- Header ---
cv_tag = text(soup.select_one(".cv-tag"))
cv_name = text(soup.select_one(".cv-name"))
cv_tagline = text(soup.select_one(".cv-tagline"))
contacts = [text(c) for c in soup.select(".cv-contact")]

# --- Left column: section-label + following sibling .entry blocks, grouped ---
left_col = soup.select_one(".cv-body > div:first-child")
left_sections = []
current_label, current_entries = None, []
for child in left_col.find_all(recursive=False):
    if "section-label" in child.get("class", []):
        if current_label is not None:
            left_sections.append((current_label, current_entries))
        current_label = text(child)
        current_entries = []
    elif "entry" in child.get("class", []):
        current_entries.append(child)
if current_label is not None:
    left_sections.append((current_label, current_entries))


def render_entry(entry):
    title = text(entry.select_one(".entry-title"))
    date = text(entry.select_one(".entry-date"))
    org = text(entry.select_one(".entry-org"))
    desc = text(entry.select_one(".entry-desc"))
    return f"""
    <div class="entry">
      <div class="entry-head"><span class="entry-title">{title}</span><span class="entry-date">{date}</span></div>
      {f'<div class="entry-org">{org}</div>' if org else ''}
      {f'<div class="entry-desc">{desc}</div>' if desc else ''}
    </div>"""


left_html = ""
for label, entries in left_sections:
    left_html += f'<h2 class="section-title">{label}</h2>\n'
    left_html += "\n".join(render_entry(e) for e in entries)

# --- Right sidebar: Bildung, Sprachen, Digital, Ehrenamt ---
sidebar = soup.select_one(".cv-body > div:last-child")
sidebar_sections = sidebar.select(".sidebar-section")

bildung_html = ""
sprachen_html = ""
digital_html = ""
ehrenamt_html = ""

for sec in sidebar_sections:
    label = text(sec.select_one(".section-label"))
    if sec.select(".entry"):
        bildung_html += f'<h2 class="section-title">{label}</h2>\n'
        for entry in sec.select(".entry"):
            title = text(entry.select_one(".entry-title"))
            date = text(entry.select_one(".entry-date"))
            org = text(entry.select_one(".entry-org"))
            bildung_html += f"""
        <div class="entry">
          <div class="entry-head"><span class="entry-title">{title}</span><span class="entry-date">{date}</span></div>
          {f'<div class="entry-org">{org}</div>' if org else ''}
        </div>"""
    elif sec.select(".skill-item"):
        sprachen_html += f'<h2 class="section-title">{label}</h2>\n'
        for item in sec.select(".skill-item"):
            skill = text(item.select_one(".skill-label"))
            value = text(item.select_one(".skill-value"))
            sprachen_html += f'<div class="skill-line">{skill} — {value}</div>\n'
    elif sec.select(".tag"):
        digital_html += f'<h2 class="section-title">{label}</h2>\n'
        tags = [text(t) for t in sec.select(".tag")]
        digital_html += f'<div class="tag-line">{" · ".join(tags)}</div>\n'
    elif sec.select(".ehren-item"):
        ehrenamt_html += f'<h2 class="section-title">{label}</h2>\n'
        for item in sec.select(".ehren-item"):
            ehrenamt_html += f'<div class="ehren-line">{text(item.select_one(".ehren-text"))}</div>\n'

full_html = f"""<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="UTF-8">
<title>Lebenslauf Andre Schwarz</title>
<style>
  @page {{ size: A4; margin: 22mm 20mm; }}
  * {{ box-sizing: border-box; }}
  html, body {{
    margin: 0; padding: 0;
    font-family: Georgia, 'Times New Roman', serif;
    font-size: 10pt;
    line-height: 1.5;
    color: #1a1a1a;
  }}
  header {{ border-bottom: 1pt solid #a8854a; padding-bottom: 10pt; margin-bottom: 18pt; }}
  h1 {{ font-size: 22pt; margin: 0 0 4pt 0; }}
  .tagline {{ color: #8a6a37; font-size: 9pt; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 8pt; }}
  .contacts {{ font-size: 9pt; color: #555; }}
  .contacts span {{ margin-right: 14pt; }}
  .cv-tag {{ font-size: 8pt; letter-spacing: 0.05em; text-transform: uppercase; color: #a8854a; }}

  .cols {{ display: flex; gap: 24pt; align-items: flex-start; }}
  .col-main {{ flex: 1.6; }}
  .col-side {{ flex: 1; border-left: 0.75pt solid #ddd; padding-left: 18pt; }}

  .section-title {{
    font-size: 10.5pt; text-transform: uppercase; letter-spacing: 0.08em;
    color: #8a6a37; border-bottom: 0.5pt solid #ddd; padding-bottom: 3pt;
    margin: 16pt 0 8pt 0;
  }}
  .section-title:first-child {{ margin-top: 0; }}

  .entry {{ margin-bottom: 10pt; break-inside: avoid; page-break-inside: avoid; }}
  .entry-head {{ display: flex; justify-content: space-between; font-weight: bold; }}
  .entry-date {{ color: #8a6a37; font-weight: normal; font-size: 9pt; white-space: nowrap; }}
  .entry-org {{ font-style: italic; color: #555; font-size: 9pt; margin: 1pt 0 2pt 0; }}
  .entry-desc {{ font-size: 9.5pt; text-align: justify; }}

  .skill-line, .ehren-line {{ font-size: 9.5pt; margin-bottom: 4pt; }}
  .tag-line {{ font-size: 9.5pt; }}
</style>
</head>
<body>

<header>
  <div class="cv-tag">{cv_tag}</div>
  <h1>{cv_name}</h1>
  <div class="tagline">{cv_tagline}</div>
  <div class="contacts">{''.join(f'<span>{c}</span>' for c in contacts)}</div>
</header>

<div class="cols">
  <div class="col-main">
    {left_html}
  </div>
  <div class="col-side">
    {bildung_html}
    {sprachen_html}
    {digital_html}
    {ehrenamt_html}
  </div>
</div>

</body>
</html>
"""

OUT.write_text(full_html, encoding="utf-8")
print("written", OUT, len(full_html), "chars")
