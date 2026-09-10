# Anlage — CROWN v10, Value-Betting-System (privates Testprojekt)

Ein Analysesystem, das auf Android in Termux läuft: Es wertet Fußballspiele aus, erkennt Value-Wetten und meldet sie über einen Telegram-Bot. Sechs Agenten teilen sich die Arbeit — Quoten abrufen, Erwartungswert berechnen, Live-xG überwachen, Statistik liefern, alles in einer SQLite-Datenbank protokollieren, Alerts versenden. Eingehende Quoten-Screenshots aus Wett-Apps werden per Claude Vision ausgelesen. Der Einsatz folgt dem Kelly-Kriterium mit 25 Prozent fractional Kelly, ein Alert geht erst ab konfigurierbarem Mindest-Erwartungswert raus.

## Die textliche Aufgabe

Sie lag im Handbuch (v1.0, 26 Seiten): Wahrscheinlichkeitsrechnung so erklären, dass sie ein Einsteiger versteht, ohne dass sie dabei falsch wird. Erwartungswert, implizite Wahrscheinlichkeit, Vig-Bereinigung, Kelly-Kriterium — für zwei Lesergruppen gleichzeitig.

Prinzip: Jeder Fachbegriff wird beim ersten Auftreten am Beispiel eingeführt, nicht als Definition. „Quote 2.00 — du setzt 1 €, bekommst 2 € zurück" sagt mehr als jede Formel. Ein Ampelsystem übersetzt den Erwartungswert in drei Farben und damit in eine Handlungsempfehlung.

Die Kernbotschaft verkauft nicht das Tool, sondern eine Haltung: Eine verlorene Wette mit gutem Preis ist besser als eine gewonnene ohne Edge.

## Kelly-Kriterium in der Praxis

Beim ersten eigenen Versuch habe ich das Kelly-Kriterium nicht nur beschrieben, sondern angewendet — kleine Einsätze, keine Vorerfahrung im Wettmarkt. Die Ergebnisse waren als Anfänger überraschend solide, was mich weniger über Sportwetten gelehrt hat als über Einsatzdisziplin: Die Formel funktioniert nur, wenn man sie auch dann befolgt, wenn sie langweilig ist. Diese Erfahrung steckt im Handbuch, weil man einen Prozess besser erklärt, wenn man ihn selbst durchgehalten hat.

## Entstehung

Entwickelt März bis April 2026. Der erste Entwurf war KI-generiert; von dort habe ich das System über zehn Versionen hochgezogen — jede eine Korrektur an dem, was die vorherige nicht konnte. Wichtig ist mir daran nicht der Prompt, sondern die neun Durchgänge danach.

**Technik:** Python, SQLite, Android/Termux, Telegram-Bot, Claude Vision.
**Versionen:** System CROWN v10 · Handbuch v1.0.

## Einordnung

Testprojekt zur Demonstration technischer Textarbeit, kein Geschäft, kein Kunde, keine Ertragsversprechen. Sportwetten bergen finanzielle Risiken; ausschließlich für volljährige Personen.
