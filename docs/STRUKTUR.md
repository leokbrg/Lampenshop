# Struktur — Collections, Menüs, Tags

Informationsarchitektur des Shops. Alles hier wird in Shopify Admin angelegt (Anleitung: `docs/ADMIN-SETUP.md`), nicht im Theme hardcodiert. Das Theme liest Menüs über ihre Handles und Collections über die Menüziele.

Ordnungslogik (`CLAUDE.md` Abschnitt 3): oben Einsatzort bzw. Einsatzzweck, darunter immer Bauart. Keine Raum-Navigation parallel.

---

## 1. Tag-System

Jedes Produkt bekommt **genau einen Einsatzort-Tag** und **genau einen Bauart-Tag**.

| Gruppe | Tag | Bedeutung |
|---|---|---|
| Einsatzort | `innen` | Innenleuchte (auch jede Schreibtischleuchte bekommt `innen`) |
| Einsatzort | `aussen` | Außenleuchte |
| Einsatzzweck | `schreibtisch` | Schreibtischleuchte — zusätzlich zu `innen`, **ohne** Bauart-Tag `tisch` |
| Bauart | `decke` | Deckenleuchte |
| Bauart | `pendel` | Pendelleuchte |
| Bauart | `wand` | Wandleuchte (innen oder außen, je nach Einsatzort-Tag) |
| Bauart | `steh` | Stehleuchte |
| Bauart | `tisch` | Tischleuchte (innen oder außen) |
| Bauart | `weg` | Wegeleuchte |
| Aufbauphase | `platzhalter` | Muster-Produkt, wird vor dem Launch gelöscht |

Schreibtischleuchten tragen `innen` + `schreibtisch`. Weil sie den Tag `tisch` nicht tragen, erscheinen sie nicht unter „Tischleuchten“, wohl aber unter „Innenleuchten“.

Tags klein, ohne Umlaute, ohne Leerzeichen.

## 2. Produkttyp (= Bauart-Zeile auf Karte und Produktseite)

Der Produkttyp ist zugleich der Filter „Bauart“. Nur diese Werte verwenden, exakt so geschrieben:

| Produkttyp | Tags |
|---|---|
| Deckenleuchte | `innen`, `decke` |
| Pendelleuchte | `innen`, `pendel` |
| Wandleuchte | `innen`, `wand` |
| Stehleuchte | `innen`, `steh` |
| Tischleuchte | `innen`, `tisch` |
| Schreibtischleuchte | `innen`, `schreibtisch` |
| Außen-Wandleuchte | `aussen`, `wand` |
| Wegeleuchte | `aussen`, `weg` |
| Außen-Tischleuchte | `aussen`, `tisch` |

## 3. Collections

Alle Collections sind **automatisch** („Produkte müssen **allen** Bedingungen entsprechen“). Die Beschreibungen unten sind Platzhalter und noch nicht freigegeben.

| Titel | Handle | Bedingungen (Produkt-Tag ist gleich …) | Sortierung | Beschreibung (Platzhalter) |
|---|---|---|---|---|
| Innenleuchten | `innenleuchten` | `innen` | manuell | `[[Kategorietext Innenleuchten — noch festzulegen]]` |
| Deckenleuchten | `deckenleuchten` | `innen` UND `decke` | manuell | `[[Kategorietext Deckenleuchten — noch festzulegen]]` |
| Pendelleuchten | `pendelleuchten` | `innen` UND `pendel` | manuell | `[[Kategorietext Pendelleuchten — noch festzulegen]]` |
| Wandleuchten | `wandleuchten` | `innen` UND `wand` | manuell | `[[Kategorietext Wandleuchten — noch festzulegen]]` |
| Stehleuchten | `stehleuchten` | `innen` UND `steh` | manuell | `[[Kategorietext Stehleuchten — noch festzulegen]]` |
| Tischleuchten | `tischleuchten` | `innen` UND `tisch` | manuell | `[[Kategorietext Tischleuchten — noch festzulegen]]` |
| Außenleuchten | `aussenleuchten` | `aussen` | manuell | `[[Kategorietext Außenleuchten — noch festzulegen]]` |
| Außen-Wandleuchten | `aussen-wandleuchten` | `aussen` UND `wand` | manuell | `[[Kategorietext Außen-Wandleuchten — noch festzulegen]]` |
| Wegeleuchten | `wegeleuchten` | `aussen` UND `weg` | manuell | `[[Kategorietext Wegeleuchten — noch festzulegen]]` |
| Außen-Tischleuchten | `aussen-tischleuchten` | `aussen` UND `tisch` | manuell | `[[Kategorietext Außen-Tischleuchten — noch festzulegen]]` |
| Schreibtischleuchten | `schreibtischleuchten` | `schreibtisch` | manuell | `[[Kategorietext Schreibtischleuchten — noch festzulegen]]` |
| Neu | `neu` | `innen` ODER `aussen` („einer Bedingung entsprechen“) | **Neueste zuerst** | `[[Kategorietext Neu — noch festzulegen]]` |

Hinweise:

- `neu` enthält alle Leuchten, sortiert nach Erstellungsdatum. Es gibt bewusst keinen Tag `neu` — ein Tag müsste von Hand gepflegt werden und würde veralten. Die Startseite zeigt die ersten acht, die Collection-Seite alle.
- „Alle Leuchten“ ist die eingebaute Shopify-Collection `all` (`/collections/all`). Sie muss nicht angelegt werden.
- Den Handle beim Anlegen kontrollieren (Abschnitt „Suchmaschinen-Eintrag“ → URL-Handle). „Außenleuchten“ wird von Shopify zu `aussenleuchten`; das unbedingt prüfen, weil Startseite und Kacheln die Handles referenzieren.

## 4. Hauptmenü — Handle `main-menu`

Zwei Ebenen. Punkte mit Unterpunkten rendert das Theme auf Desktop als Mega-Menü (Spalte mit Unterkategorien, rechts das Kategoriebild der Oberkategorie mit Link), mobil als Akkordeon im Drawer.

| Ebene 1 | Ebene 2 | Ziel (über Auswahlliste) |
|---|---|---|
| Innenleuchten | | Collection `innenleuchten` |
| | Alle Innenleuchten | Collection `innenleuchten` |
| | Deckenleuchten | Collection `deckenleuchten` |
| | Pendelleuchten | Collection `pendelleuchten` |
| | Wandleuchten | Collection `wandleuchten` |
| | Stehleuchten | Collection `stehleuchten` |
| | Tischleuchten | Collection `tischleuchten` |
| Außenleuchten | | Collection `aussenleuchten` |
| | Alle Außenleuchten | Collection `aussenleuchten` |
| | Außen-Wandleuchten | Collection `aussen-wandleuchten` |
| | Wegeleuchten | Collection `wegeleuchten` |
| | Außen-Tischleuchten | Collection `aussen-tischleuchten` |
| Schreibtischleuchten | | Collection `schreibtischleuchten` |
| Neu | | Collection `neu` |
| Hilfe | | Seite `hilfe` |

Das Theme nutzt dieses Menü zusätzlich für die **Unterkategorie-Pills** auf Collection-Seiten: Auf `innenleuchten` erscheinen die Unterpunkte von „Innenleuchten“, auf `pendelleuchten` dieselben Geschwister mit markiertem aktivem Eintrag. Ändert sich das Menü, ändern sich die Pills automatisch mit.

## 5. Footer-Menüs

### `footer-shop` — Überschrift „Shop“

| Eintrag | Ziel |
|---|---|
| Innenleuchten | Collection `innenleuchten` |
| Außenleuchten | Collection `aussenleuchten` |
| Schreibtischleuchten | Collection `schreibtischleuchten` |
| Neu | Collection `neu` |
| Alle Leuchten | Alle Produkte (`/collections/all`) |

### `footer-hilfe` — Überschrift „Hilfe“

| Eintrag | Ziel |
|---|---|
| Kontakt | Seite `kontakt` |
| Versand | Seite `versand` |
| Rückgabe | Seite `rueckgabe` |
| FAQ | Seite `faq` |
| Zahlungsarten | Seite `zahlungsarten` |

### `footer-ratgeber` — Überschrift „Ratgeber“

| Eintrag | Ziel |
|---|---|
| Alle Ratgeber | Blog `ratgeber` |
| (später) einzelne Artikel | Blogartikel, sobald veröffentlicht |

Solange das Menü `footer-ratgeber` nicht existiert oder leer ist, blendet das Theme die Spalte aus.

### Rechtliches

Kein eigenes Menü. Die Unterzeile im Footer listet automatisch alle in Shopify hinterlegten Richtlinien (Einstellungen → Richtlinien): Impressum, Datenschutzerklärung, AGB, Widerrufsbelehrung, Versand. Fehlt eine, fehlt der Link — im Theme-Editor erscheint dann ein Marker.

## 6. Seiten und Templates

| Seite (Titel) | Handle | Template | Inhalt |
|---|---|---|---|
| Hilfe | `hilfe` | `page.hilfe` | Übersicht, im Template gepflegt |
| FAQ | `faq` | `page.faq` | Fragen im Template (Theme-Editor), Entwurf in `content/seiten/faq.md` |
| Kontakt | `kontakt` | `page.kontakt` | `content/seiten/kontakt.md` |
| Versand | `versand` | `page.versand` | `content/seiten/versand.md` |
| Rückgabe | `rueckgabe` | `page.versand` | `content/seiten/rueckgabe.md` |
| Zahlungsarten | `zahlungsarten` | `page.zahlungsarten` | `content/seiten/zahlungsarten.md` |
| Über uns | `ueber-uns` | `page.ueber-uns` | `content/seiten/ueber-uns.md` |

Achtung Handle: Eine Seite mit Titel „FAQs“ bekäme den Handle `faqs`. Titel „FAQ“ verwenden und Handle kontrollieren. Umlaute im Titel („Rückgabe“, „Über uns“) macht Shopify zu `ruckgabe` / `uber-uns` — Handle beim Anlegen von Hand auf `rueckgabe` / `ueber-uns` setzen.

## 7. Blog

| Titel | Handle | Zweck |
|---|---|---|
| Ratgeber | `ratgeber` | Startseiten-Teaser (3 Karten) und Footer-Spalte. Leer → Teaser blendet sich aus. |

Geplante Themen (noch nicht geschrieben): Lichtfarbe und Kelvin · Lumen pro Raum · IP-Schutzarten im Außenbereich.
