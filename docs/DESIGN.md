# Design-System

Skandinavisch-warm: viel Weißraum, ruhige Flächen, kaum Rundungen, keine Schatten, keine Verläufe außer dezentem Bild-Overlay im Hero. Quelle der Werte ist `config/settings_data.json` (Theme-Editor → Theme-Einstellungen); dieses Dokument beschreibt, was dort gesetzt ist und warum.

## Farben

| Rolle | Wert | Palette-Slot | CSS-Variable |
|---|---|---|---|
| Hintergrund | `#F5F1EA` | `background` | `--color-background` |
| Text | `#2A2520` | `foreground` | `--color-foreground` |
| Sekundärtext | `#625A50` | `color1` | `--color-text-secondary` |
| Fläche (Sand) | `#EAE3D7` | `color2` | `--color-surface` |
| Linien | `#D8CEC0` | `color3` | `--color-line` |

`--color-surface`, `--color-line` und `--color-text-secondary` werden in `snippets/color-palette.liquid` direkt aus der Palette gesetzt (nicht aus anderen Variablen zusammengesetzt) und stehen auf `:root` zur Verfügung, also auch in Dialogen und Drawern.

Horizons „gedämpfter“ Text (`--color-foreground-muted`) ist Textfarbe mit Deckkraft. Die Deckkraft wurde von 60 % auf **72 %** angehoben, weil 60 % auf beiden Flächen unter 4,5:1 lag (gemessen 3,95 bzw. 3,79).

## Kontraste (gemessen)

Berechnet nach WCAG 2.1 (relative Luminanz) aus den Hex-Werten; halbtransparente Farben wurden vorher auf die jeweilige Fläche gerechnet. Ziel: ≥ 4,5:1 für Fließtext.

| Kombination | Vordergrund / Fläche | Kontrast | Urteil |
|---|---|---|---|
| Text auf Hintergrund | `#2A2520` / `#F5F1EA` | 13,48:1 | ok |
| Text auf Sand | `#2A2520` / `#EAE3D7` | 11,90:1 | ok |
| Sekundärtext auf Hintergrund | `#625A50` / `#F5F1EA` | 6,02:1 | ok |
| Sekundärtext auf Sand | `#625A50` / `#EAE3D7` | 5,32:1 | ok |
| Gedämpfter Text (72 %) auf Hintergrund | `#635E59` / `#F5F1EA` | 5,69:1 | ok |
| Gedämpfter Text (72 %) auf Sand | `#605A53` / `#EAE3D7` | 5,34:1 | ok |
| Abgeschwächter Text (80 %) auf Hintergrund | `#534E48` / `#F5F1EA` | 7,31:1 | ok |
| Abgeschwächter Text (80 %) auf Sand | `#504B45` / `#EAE3D7` | 6,77:1 | ok |
| Primärbutton (hell auf dunkel) | `#F5F1EA` / `#2A2520` | 13,48:1 | ok |
| Primärbutton Hover | `#F5F1EA` / `#554B41` | 7,55:1 | ok |
| Sekundärbutton (Outline) | `#2A2520` / `#F5F1EA` | 13,48:1 | ok |
| „Ausverkauft“-Badge | `#2A2520` / `#EAE3D7` | 11,90:1 | ok |
| Marker im Editor | `#5C4200` / `#FFF4D6` | 8,58:1 | ok |
| Linie auf Hintergrund | `#D8CEC0` / `#F5F1EA` | 1,38:1 | nur Dekor, trägt keine Information |
| Linie auf Sand | `#D8CEC0` / `#EAE3D7` | 1,22:1 | nur Dekor |

Nicht aus Hex-Werten messbar:

- **Text auf dem Hero-Bild.** Hängt vom Foto ab. Das Overlay ist ein Verlauf von unten (`#1B1712`, 60 % Deckkraft). Auf einem mittelgrauen Bild ergibt das rechnerisch 9,04:1 für die helle Schrift; auf sehr hellen Bildbereichen ist es weniger. Nach dem Zuweisen des Hero-Bilds im Editor gerendert prüfen.
- **Energielabel-Pfeil.** Farben und schwarze/weiße Schrift sind durch die EU-Vorgabe festgelegt und werden nicht angepasst.
- **Eingabefelder und Filter-Checkboxen** nutzen die Linienfarbe als Rahmen (1,38:1). Für Bedienelemente wären 3:1 wünschenswert. Bewusst so belassen, weil die Felder zusätzlich über Beschriftung und Fläche erkennbar sind — bei Bedarf in den Theme-Einstellungen „Rahmen Eingabefelder“ auf die Sekundärtextfarbe stellen (6,02:1).

## Typografie

| Stil | Schrift | Größe | Zeilenhöhe | Laufweite |
|---|---|---|---|---|
| H1 | Lora 400 | 52 px (fließend, min. ca. 40 px) | 1,1 | −0,015 em |
| H2 | Lora 400 | 36 px | 1,1 | −0,015 em |
| H3 | Lora 400 | 28 px | 1,2 | 0 |
| H4 | Lora 400 | 22 px | 1,2 | 0 |
| H5 | DM Sans 500 | 14 px | 1,2 | 0 |
| H6 | DM Sans 500 | 12 px | 1,2 | 0 |
| Fließtext | DM Sans 400 | 15 px | 1,6 | 0 |

- Überschriften immer im Normalgewicht, nie fett. Lora wird nur in 400 geladen, DM Sans in 400 und 500 — andere Gewichte sind nicht definiert und dürfen nicht verwendet werden.
- Die Größen 15, 22, 28, 36 und 52 px gab es in Horizon nicht als Option; sie wurden in `config/settings_schema.json` ergänzt. Vorher standen 15/22/28/52 in den Einstellungen, ohne im Schema zu existieren.
- „Laufweite eng“ (`--letter-spacing--heading-tight`) wurde von −0,03 em auf −0,015 em reduziert; −0,03 em ist für eine Serifenschrift zu viel.
- Überschriften brechen ausgeglichen um (`text-wrap: balance`), H1/H2 dürfen silbentrennen, damit lange Komposita mobil nicht überlaufen.

## Buttons

| Typ | Fläche | Text | Rahmen | Radius |
|---|---|---|---|---|
| Primär | `#2A2520` | `#F5F1EA` | keiner | 2 px |
| Sekundär | transparent/Hintergrund | `#2A2520` | 1 px `#2A2520` | 2 px |

Mindesthöhe 48 px (Touch-Ziel). Hover: Fläche wird leicht aufgehellt (`#554B41`), keine Bewegung, kein Schatten.

## Formen

Radius überall 0–2 px: Buttons 2, Eingabefelder 2, Badges 2, Pills 2, Popover 2, Karten und Produktbilder 0. Einzige runde Elemente sind die Farb-Swatches (Kreis, 28 px), weil das die erwartete Form für Farbwahl ist. Popover und Drawer haben einen 1-px-Rahmen in Linienfarbe statt Schatten.

## Abstände

8er-Raster. Verwendete Werte: 8 · 16 · 24 · 32 · 48 · 64 · 96 px.

| Einsatz | Desktop | Mobil |
|---|---|---|
| Abstand zwischen Sections (oben/unten je) | 64–96 px | × 0,6, mindestens 20 px |
| Seitenrand | 40 px | 16 px |
| Raster-Abstand Produktkarten | 16 px horizontal, 32 px vertikal | 8 px / 24 px |
| Abstand in Textgruppen | 8–16 px | gleich |

Horizon skaliert Section-Abstände über `--spacing-scale` (unter 750 px). Der Faktor wurde von 0,7 auf **0,6** gesenkt, damit mobil deutlich kompakter gestapelt wird. Seitenbreite: „schmal“ = maximal 1440 px Inhalt.

## Bildformate

| Einsatz | Format | Hinweis |
|---|---|---|
| Produktbild (Karte, Galerie) | 4:5 | immer auf Sand `#EAE3D7`; freigestellte Bilder stehen direkt auf der Fläche |
| Kategoriebild (Kacheln, Mega-Menü) | 4:5 | |
| Hero | 16:9 Desktop / 4:5 mobil | eigenes Mobilbild im Editor zuweisbar |
| Marke (Bild + Text) | 4:5 | |
| Ratgeber-Karte | 3:2 | |

Empfohlene Upload-Größe für Produktbilder: 2000 × 2500 px.

## Bewegung

Seitenübergänge, „Fly to cart“ und Hover-Effekte auf Karten sind aus. Es bleiben: Farbwechsel bei Hover (Buttons, Links), Bildwechsel auf der Produktkarte, Öffnen/Schließen von Drawern und Accordions.
