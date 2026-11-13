# Seiteninhalte (Entwürfe)

Entwürfe für die Seiten in Shopify Admin (Onlineshop → Seiten). Anleitung: `docs/ADMIN-SETUP.md`, Schritt 5.

- Deutsch liegt in diesem Ordner, Englisch in `en/`. Die deutsche Fassung kommt in die Seite, die englische in die App „Translate & Adapt“.
- Alles in `[[doppelten eckigen Klammern]]` ist **nicht entschieden** und darf so nicht live gehen. Vor dem Launch jede Seite im Browser öffnen und nach `[` suchen.
- Hier stehen **keine Rechtstexte**. Impressum, Datenschutzerklärung, AGB und Widerrufsbelehrung kommen vom Rechtsdienstleister und werden unter Einstellungen → Richtlinien eingetragen, nicht als Seite.
- Lieferzeiten, Versandkosten, Rückgabebedingungen und Rücksendeadresse sind verbindliche Zusagen. Sie kommen aus den schriftlichen Angaben der Lieferanten (`CLAUDE.md` Abschnitt 4.2) und müssen überall gleich lauten (Konsistenztabelle in `CLAUDE.md` Abschnitt 12).

| Datei | Seite (Titel) | Handle | Template |
|---|---|---|---|
| `hilfe.md` | Hilfe | `hilfe` | `page.hilfe` |
| `faq.md` | FAQ | `faq` | `page.faq` |
| `kontakt.md` | Kontakt | `kontakt` | `page.kontakt` |
| `versand.md` | Versand | `versand` | `page.versand` |
| `rueckgabe.md` | Rückgabe | `rueckgabe` | `page.versand` |
| `versand-kurz.md` | Versand & Rückgabe (kurz) | `versand-kurz` | Standard |
| `zahlungsarten.md` | Zahlungsarten | `zahlungsarten` | `page.zahlungsarten` |
| `ueber-uns.md` | Über uns | `ueber-uns` | `page.ueber-uns` |

Der Text unter „Inhalt“ wird in den Editor der Seite kopiert. Überschriften mit `##` als „Überschrift 2“ formatieren.
