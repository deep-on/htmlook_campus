# Step 2 · Erste Datei (HTML / Markdown / PDF / Video)

<p align="center">
  <a href="README.md">English</a> | <a href="README.ko.md">한국어</a> | <a href="README.ja.md">日本語</a> | <b>Deutsch</b> | <a href="README.fr.md">Français</a> | <a href="README.es.md">Español</a> | <a href="README.pt.md">Português</a> | <a href="README.it.md">Italiano</a>
</p>

> Lerne den Kern des HTMLook-*Viewers* — der Teil, der schon ohne AI / MCP
> Sinn ergibt.
> ~ 5 min.

Am Ende dieses Schritts weißt du, wie du jede der vier Dateiarten (md /
html / pdf / Video) liest und mit Split-View, Preview und Outline durch
sie navigierst.

## 2.1 · Markdown — Live-Edit

1. Doppelklick auf eine beliebige `.md` in der Sidebar (z. B.
   [`../05-command/personas/03-dev-pr-docs/docs.md`](../05-command/personas/03-dev-pr-docs/docs.md)).
2. ⌘\\ oder Menü *View → Split* schaltet die Split-View um.
3. Links Source, rechts Preview. Tippst du links, aktualisiert sich rechts
   live.

> Video: [BASIC #3 · Type left. See right. Live.](../videos/features/03-basic-03-md-live-edit.mp4) (30 s)

## 2.2 · HTML — Element anklicken und direkt ändern

1. Doppelklick auf eine `.html` (z. B.
   [`../05-command/personas/01-hf-claude/landing.html`](../05-command/personas/01-hf-claude/landing.html)).
2. Default-Modus ist Preview. In Split-View ein Element direkt anklicken
   → ein Texteditor poppt auf.
3. Zwei-Wege-Sync — Änderungen in der Preview landen sofort in der Source.

> Video: [BASIC #4 · Click anything. Edit it.](../videos/features/04-basic-04-html-split.mp4) (30 s)

## 2.3 · HTML — vier Selection-Modi

In derselben HTML-Datei zykelt ⌘E durch die vier Selection-Modi:

| Modus | Was es nimmt |
|---|---|
| element | einen einzelnen DOM-Knoten |
| range | einen Textbereich |
| region | ein rechteckig gemaltes Areal |
| outline | den Heading-Baum |

Video: [BASIC #6 · Pick what you see.](../videos/features/06-basic-06-html-4mode.mp4) (30 s)

Was immer ein Modus aufgreift, wird in [Step 4 · editing](../04-editing/)
zum cite-anchor-Einstiegspunkt.

## 2.4 · PDF — Seiten + Textebene

1. Doppelklick auf eine beliebige `.pdf` (z. B.
   [`../05-command/personas/05-domain-battery/vendor.pdf`](../05-command/personas/05-domain-battery/vendor.pdf)).
2. Links Thumbnail-Navigator, rechts Seiten-Canvas + auswählbare Textebene.
3. Region per Drag markieren → region cite (in Step 4 verwendet).

## 2.5 · Video — Frame-Thumbnails + Outline

1. Doppelklick auf eine beliebige mp4 (z. B.
   [`../videos/features/01-basic-01-drop-open.mp4`](../videos/features/01-basic-01-drop-open.mp4)).
2. Der Video-Viewer zeigt eine Timeline mit Thumbnail-Previews.
3. ⌘Shift+T oder Hover gibt dir eine 1-Sekunden-Frame-Preview (ohne
   Scrubbing).

> Video: [ADV · Frame check. No scrub.](../videos/features/15-advanced-09-thumbnail.mp4) (30 s, Kategorie advanced)

## 2.6 · Outline — durch lange Dokumente navigieren

Heading-Struktur jeder langen md / html / PDF → Outline-Tab im rechten
Panel. Klick auf ein Heading springt dorthin.

> Video: [ADV · Click §3.2. You're there.](../videos/features/16-advanced-10-outline.mp4) (30 s)

## 2.7 · Split-View / Multi-Pane (⌘1 / ⌘2 / ⌘3 / ⌘J)

| Shortcut | Effekt |
|---|---|
| ⌘1 | nur Preview |
| ⌘2 | nur Source |
| ⌘3 | Split (Preview + Source) |
| ⌘J | Terminal-Panel umschalten |

Video: [ADV · Two keys. Three views.](../videos/features/10-advanced-04-multi-pane.mp4)
(30 s — die *"Two keys"* in der Narration waren im Original ⌘D + ⌘J und
wurden für v1.0 zu ⌘1/⌘2/⌘3 + ⌘J korrigiert. Komplette Linie in
[`../08-extend/PRODUCTION.md`](../08-extend/PRODUCTION.md), Tabelle
*fixed false claims*.)

## ✅ Step 2 Checkpoint

- Du hast je eine md / html / pdf / Video-Datei in Split-View geöffnet.
- Du hast den Unterschied zwischen den vier HTML-Modi (element / range /
  region / outline) durch direktes Klicken gespürt.
- ⌘1 / ⌘2 / ⌘3 / ⌘J fürs Layout-Toggling sitzt im Muskelgedächtnis.

Alle drei? → [Step 3 · BYOM setup](../03-byom-setup/) — einen Anbieter
auswählen und Key hinterlegen.
