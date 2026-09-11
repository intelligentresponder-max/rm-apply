# PDF-Quellen für Anschreiben_Andre_Schwarz.pdf und Lebenslauf_Andre_Schwarz.pdf

Diese Dateien erzeugen beide PDF-Bewerbungsdokumente im Repo-Root.

## Anschreiben_Andre_Schwarz.pdf (Anschreiben + fünf Anlagen)

- `01-ANSCHREIBEN.md` — Anschreiben-Text (Quelle für die Website-Fassung
  in `../anschreiben.html` ist identisch zu halten)
- `02-ANLAGE-Antragsarchiv.md` — Anlage 1
- `06-ANLAGE-Arbeitsproben.md` — Anlage 2 (Arbeitsproben-Überblick)
- `03-ANLAGE-GEO.md` — Anlage 3 (Generative Engine Optimization)
- `04-ANLAGE-CROWN.md` — Anlage 4 (CROWN v10 / Value-Betting-System)
- `05-ANLAGE-HumanDesign.md` — Anlage 5
- `build.py` — liest die Markdown-Dateien, baut `bewerbung.html`
- `render.js` — rendert `bewerbung.html` per Playwright/Chromium zu
  `Anschreiben_Andre_Schwarz.pdf` (landet in diesem Ordner)

```bash
pip install markdown
cd pdf-source
python3 build.py          # erzeugt bewerbung.html
node render.js            # erzeugt Anschreiben_Andre_Schwarz.pdf
cp Anschreiben_Andre_Schwarz.pdf ../Anschreiben_Andre_Schwarz.pdf
```

## Lebenslauf_Andre_Schwarz.pdf

Hier gibt es **keine eigene Markdown-Quelle** — `build-lebenslauf.py` liest
die Inhalte direkt aus `../lebenslauf.html` (per BeautifulSoup-Parsing der
`.entry`/`.sidebar-section`-Elemente) und baut daraus ein separates,
druckfertiges Layout (`lebenslauf-print.html`, helles Business-Dokument-Design,
nicht das dunkle Website-Theme). Dadurch kann Lebenslauf.html nie mit der
PDF auseinanderlaufen, ohne dass man es bemerkt: die PDF wird immer frisch
aus der Website-Quelle erzeugt, es gibt keine zweite Stelle, die man
vergessen könnte zu pflegen.

- `build-lebenslauf.py` — parst `../lebenslauf.html`, baut `lebenslauf-print.html`
- `render-lebenslauf.js` — rendert `lebenslauf-print.html` per
  Playwright/Chromium direkt zu `../Lebenslauf_Andre_Schwarz.pdf`
  (schreibt sofort ins Repo-Root, kein Kopierschritt nötig)

```bash
pip install beautifulsoup4
cd pdf-source
python3 build-lebenslauf.py   # erzeugt lebenslauf-print.html
node render-lebenslauf.js     # erzeugt ../Lebenslauf_Andre_Schwarz.pdf
```

`render.js`/`render-lebenslauf.js` brauchen Playwright mit Chromium
(`npm install playwright && npx playwright install chromium`, oder einen
vorhandenen Chromium-Pfad in `executablePath` eintragen).

## Wichtig

Nach jeder inhaltlichen Änderung an `01-ANSCHREIBEN.md` bzw. den
Anlagen-Dateien (oder am Anschreiben-Text in `../anschreiben.html`, falls
der Website-Text geändert wird) den Anschreiben-Build erneut ausführen.

Nach jeder inhaltlichen Änderung an `../lebenslauf.html` den
Lebenslauf-Build erneut ausführen — sonst laufen Website und PDF wieder
auseinander.
