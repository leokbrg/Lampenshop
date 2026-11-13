# Beschreibungsschema für Produkte

Jede Produktbeschreibung hat dieselben vier Abschnitte in derselben Reihenfolge und vergleichbarer Länge (`CLAUDE.md` Abschnitt 7). So lassen sich Modelle nebeneinander lesen.

Die Beschreibung steht im Shopify-Feld „Beschreibung“ und erscheint auf der Produktseite im ersten Accordion. **Technische Daten gehören nicht hierher**, sondern in die Metafelder — nur dort sind sie filterbar und werden in der Tabelle „Technische Daten“ ausgegeben.

## Aufbau

| # | Abschnitt | Überschrift im Text | Umfang | Inhalt |
|---|---|---|---|---|
| 1 | Einleitung | keine | 2–3 Sätze | Was ist das für eine Leuchte, wofür ist sie gedacht. Kein Superlativ. |
| 2 | Licht & Wirkung | `Licht & Wirkung` (H3) | 2–4 Sätze | Abstrahlrichtung (direkt, indirekt, gestreut), Charakter des Lichts, Blendung. Nur beschreiben, was am Muster oder im Datenblatt belegt ist. |
| 3 | Material & Verarbeitung | `Material & Verarbeitung` (H3) | 2–4 Sätze | Materialien, Oberfläche, Haptik, Details der Montage oder Aufhängung. |
| 4 | Einsatz | `Einsatz` (H3) | 2–3 Sätze | Wo die Leuchte sinnvoll hängt oder steht, worauf zu achten ist (Raumhöhe, Tischgröße, Feuchtraum ja/nein laut IP-Schutzart). |

Gesamtlänge: etwa 90–140 Wörter.

## Vorlage (HTML für das Beschreibungsfeld)

```html
<p>[[Einleitung — 2–3 Sätze]]</p>

<h3>Licht &amp; Wirkung</h3>
<p>[[Licht & Wirkung — 2–4 Sätze]]</p>

<h3>Material &amp; Verarbeitung</h3>
<p>[[Material & Verarbeitung — 2–4 Sätze]]</p>

<h3>Einsatz</h3>
<p>[[Einsatz — 2–3 Sätze]]</p>
```

Die eckigen Klammern sind Arbeitsmaterial. Vor dem Aktivieren eines Produkts die Produktseite im Browser öffnen und nach `[` suchen.

## Regeln

- **Nichts erfinden.** Keine Zahlen, Materialien oder Eigenschaften, die nicht im Datenblatt stehen oder am Muster geprüft wurden.
- **Keine Zahlen doppelt pflegen.** Lumen, Kelvin, Watt, Maße, IP-Schutzart stehen nur in den Metafeldern. Im Fließtext höchstens umschreiben („warmweißes Licht“), damit Text und Tabelle sich nie widersprechen.
- **Keine Zusagen.** Keine Lieferzeit, keine Garantie, keine Lebensdauer-Versprechen, keine Aussagen zu Tests oder Zertifikaten im Fließtext.
- **Keine Wertungen ohne Beleg.** Kein „beste“, „hochwertigste“, „einzigartig“.
- **Ansprache:** `[[Du oder Sie — noch festzulegen]]`. Bis zur Entscheidung unpersönlich formulieren.
- **Eine Leuchte, ein Text.** Varianten (Farben) werden nicht einzeln beschrieben; Farbnamen stehen in der Variantenauswahl.

## Was nicht in die Beschreibung gehört

| Inhalt | Wo stattdessen |
|---|---|
| Kurzer Nutzen-Satz über dem Kaufbereich | Metafeld `custom.kurzbeschreibung` (max. ca. 120 Zeichen) |
| Technische Daten | Metafelder `custom.*` → Accordion „Technische Daten“ |
| Maße, Maßzeichnung | `custom.masse`, `custom.masszeichnung` → Accordion „Maße“ |
| Lieferumfang | `custom.lieferumfang` → Accordion „Lieferumfang“ |
| Hersteller, WEEE, Sicherheitshinweise | Metafelder → Accordion „Hersteller & Sicherheit“ |
| Lieferzeit | `custom.lieferzeit` → Kaufbereich |
| Versand- und Rückgabebedingungen | Shopify-Richtlinien und Seite „Versand“ |

## Zweisprachigkeit

Die deutsche Beschreibung ist die Quelle. Die englische Fassung wird in der App „Translate & Adapt“ gepflegt (Produkte → Beschreibung) und folgt demselben Aufbau mit den Überschriften `Light & effect`, `Material & finish`, `Use`. Automatische Übersetzungen vor dem Aktivieren gegenlesen, vor allem Fachbegriffe (Sockel, Schutzart).

## Muster-Produkte

Die Platzhalter-Produkte aus `data/platzhalter-produkte.csv` tragen die Vorlage oben mit Markern als Beschreibung. Sie enthalten bewusst keinen ausformulierten Text.
