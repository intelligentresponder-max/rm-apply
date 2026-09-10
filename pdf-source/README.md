# PDF-Quellen für Anschreiben_Andre_Schwarz.pdf

Diese Dateien erzeugen die PDF-Bewerbungsmappe im Repo-Root
(`../Anschreiben_Andre_Schwarz.pdf`): Anschreiben plus fünf Anlagen.

## Dateien

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

## Build ausführen

```bash
pip install markdown
cd pdf-source
python3 build.py          # erzeugt bewerbung.html
node render.js            # erzeugt Anschreiben_Andre_Schwarz.pdf
cp Anschreiben_Andre_Schwarz.pdf ../Anschreiben_Andre_Schwarz.pdf
```

`render.js` braucht Playwright mit Chromium (`npm install playwright &&
npx playwright install chromium`, oder einen vorhandenen
Chromium-Pfad in `executablePath` eintragen).

## Wichtig

Nach jeder inhaltlichen Änderung an einer dieser Markdown-Dateien (oder
am Anschreiben-Text in `../anschreiben.html`, falls der Website-Text
geändert wird) den Build erneut ausführen und die PDF im Repo-Root
ersetzen — sonst laufen Website und PDF wieder auseinander.
