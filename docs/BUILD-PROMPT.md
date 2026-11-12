# BAU-PROMPT — VOLLSTÄNDIGER LAMPENSHOP

Diesen Text komplett in Claude Code einfügen, im Repo `leokbrg/Lampenshop`.

---

Du baust in diesem Repo den vollständigen Shopify-Shop für einen Leuchtenshop auf Basis des vorhandenen Horizon-Themes. Lies zuerst `CLAUDE.md` vollständig — sie gilt für alles hier und hat Vorrang vor diesem Prompt, wenn sich etwas widerspricht.

Ziel dieser Sitzung: Ein Shop, der in der Vorschau vollständig und glaubwürdig aussieht — mit Platzhalter-Produkten und Stockfotos —, dessen Struktur aber schon die echte ist. Wenn später echte Produkte kommen, wird nur Content getauscht, nicht das Theme umgebaut.

## Rahmen

- Sortiment: **Innenleuchten**, **Außenleuchten**, **Schreibtischleuchten** als drei eigene Hauptkategorien. Unterkategorien und Handles stehen in `CLAUDE.md`, Abschnitt 3.
- Designrichtung: skandinavisch-warm, Tokens stehen in `CLAUDE.md`, Abschnitt 2.
- Strukturvorlage: neona.store. Übernimm von dort **nur Struktur**: Mega-Menü nach Bauart unter Innen/Außen, Kategorie-Kacheln auf der Startseite, Kurzzeile mit Nutzen auf der Produktkarte, verständliche Filter, Sortierung, Ratgeber-Bereich im Footer. Keine Farben, Layouts, Texte oder Bilder von dort.
- **Nicht** von neona übernehmen: Countdowns, „Fast ausverkauft“-Badges, durchgestrichene Preise und Rabatt-Prozente, Kundenzahlen, Sternebewertungen zum Launch, Garantie- und Lieferversprechen, Versandschutz-Upsell im Warenkorb, Sprachumschalter. Das widerspricht `CLAUDE.md` Abschnitte 11 und 12 oder ist nicht entschieden.
- Theme-Arbeit passiert im Repo. Produkte, Collections, Menüs, Seiten, Metafeld-Definitionen und Richtlinien leben in Shopify Admin — die kannst du nicht direkt anlegen. Dafür erstellst du Import-Dateien und eine Schritt-für-Schritt-Anleitung für mich (Phase 9).
- Jeder Push auf `main` landet im unveröffentlichten Theme-Entwurf. Nie etwas veröffentlichen.

## Arbeitsweise

- Zuerst Codebase untersuchen, dann einen kurzen Plan mit den Phasen unten ausgeben, dann ohne weitere Rückfrage durcharbeiten.
- Nach jeder Phase: `shopify theme check` (neue und geänderte Dateien 0 Offenses), einzeln committen mit aussagekräftiger Nachricht, pushen.
- Vor jeder Änderung an `config/settings_data.json` oder `templates/*.json`: `git pull`, weil der Theme-Editor diese Dateien überschreibt.
- Horizon-Konventionen einhalten: Theme-Blocks in `blocks/`, `{% stylesheet %}` pro Block, Settings über Schema, Texte im Schema auf Deutsch. Bestehende Horizon-Sections erweitern statt parallel neue zu bauen, wo das sauber geht.
- Keine Werte erfinden. Wo eine Entscheidung fehlt: neutrale Lösung bauen und sichtbaren Marker `[[… — noch festzulegen]]` setzen, dokumentieren.
- Fallstricke aus `CLAUDE.md` Abschnitt 13 aktiv vermeiden (CSS-Variablen definiert? Font-Weights definiert? Reveal-Klassen sicher?).

---

## Phase 1 — Informationsarchitektur

1. Lege `docs/STRUKTUR.md` an mit:
   - allen Collections (Titel, Handle, Tag-Regel für automatische Collection, kurze Beschreibung als Platzhalter)
   - Hauptmenü `main-menu` mit Mega-Menü-Struktur:
     - Innenleuchten → Alle Innenleuchten · Deckenleuchten · Pendelleuchten · Wandleuchten · Stehleuchten · Tischleuchten
     - Außenleuchten → Alle Außenleuchten · Außen-Wandleuchten · Wegeleuchten · Außen-Tischleuchten
     - Schreibtischleuchten
     - Neu (Collection `neu`, sortiert nach Erstellungsdatum)
     - Hilfe (Seite)
   - Footer-Menüs `footer-shop`, `footer-hilfe`, `footer-ratgeber`
   - Tag-System: Einsatzort (`innen`, `aussen`, `schreibtisch`), Bauart (`decke`, `pendel`, `wand`, `steh`, `tisch`, `weg`), `platzhalter` für alle Muster-Produkte
   - Produkttyp-Werte (= Bauart-Zeile auf der Karte), z. B. „Pendelleuchte“, „Außen-Wandleuchte“, „Schreibtischleuchte“
2. Prüfe, ob das Horizon-Header-Menü verschachtelte Menüs als Mega-Menü darstellt, und konfiguriere `sections/header-group.json` dafür.

## Phase 2 — Design-System schärfen

- Bestehende Palette und Schriften aus `config/settings_data.json` übernehmen, nicht neu erfinden.
- Typo-Hierarchie festziehen: H1–H4 in Lora, Normalgewicht, leichte negative Laufweite bei großen Größen. Fließtext DM Sans 15 px, Zeilenhöhe großzügig.
- Buttons: Primär dunkel (`#2A2520`) auf hell, sekundär als Outline. Radius 2 px. Hover dezent.
- Abstände: konsistentes Raster (z. B. 8er-Schritte), großzügige Sektionsabstände Desktop, deutlich kompakter mobil.
- Bildformate festlegen: Produktbilder 4:5 auf Sand-Fläche `#EAE3D7`, Kategoriebilder 4:5, Hero 16:9 Desktop / 4:5 mobil.
- Kontraste aller Text-/Hintergrund-Kombinationen messen und in `docs/DESIGN.md` dokumentieren (≥ 4,5:1 für Fließtext).

## Phase 3 — Header, Navigation, Suche

- Sticky Header mit kompaktem Zustand beim Scrollen.
- Logo links (fällt auf `shop.name` zurück), Mega-Menü, rechts Suche als **sichtbares Suchfeld** auf Desktop, Konto, Warenkorb mit Zähler.
- Mega-Menü: Spalten mit Unterkategorien, rechts optional ein Kategorie-Bild mit Link.
- Mobil: Drawer mit Akkordeon für Innen/Außen, Suche oben im Drawer und als Icon im Header immer erreichbar.
- Predictive Search: Produkte mit Bild, Preis und Energieklasse, dazu Collections.
- Ankündigungsleiste bleibt aus, bis es eine echte, entschiedene Aussage gibt.

## Phase 4 — Startseite (routet, verkauft nicht)

Reihenfolge:

1. **Hero**: großes Stimmungsbild, H1 kurz, zwei Buttons „Innenleuchten“ und „Außenleuchten“.
2. **Hauptkategorien**: drei große Kacheln Innen · Außen · Schreibtisch.
3. **Nach Bauart**: Kacheln Decke, Pendel, Wand, Steh, Tisch, Außen-Wand, Weg (Raster, mobil horizontal scrollbar).
4. **Neu im Sortiment**: Produktliste aus Collection `neu`, 4 Spalten Desktop.
5. **Marke**: Bild + kurzer Text. Text als Marker `[[Markentext — noch festzulegen]]`.
6. **Schreibtischleuchten**: eigene Produktliste mit kurzer Einleitung.
7. **Service-Leiste**: nur Aussagen, die sicher stimmen — „Technische Daten vollständig angegeben“, „Energielabel und Datenblatt zu jeder Leuchte“, Zahlungsarten-Icons (aus Shopify). Keine Lieferzeit, keine Garantie, keine Kundenzahl.
8. **Ratgeber-Teaser**: 3 Karten zu Blogartikeln (Blog `ratgeber`), z. B. Lichtfarbe/Kelvin, Lumen pro Raum, IP-Schutzarten außen. Leer → Section blendet sich aus.

## Phase 5 — Collection-Seite (wichtigste Seite)

- Kopf: H1, Beschreibung (aus Collection), Produktanzahl, bei Hauptkategorien darunter Unterkategorie-Pills.
- Filter: Desktop links als Sidebar, mobil als Drawer mit „X Produkte anzeigen“-Button. Filter werden in Search & Discovery konfiguriert — das Theme muss Listen-, Bereichs- und Boolean-Filter sauber darstellen.
- Sortierung: Empfohlen, Neu, Preis aufsteigend, Preis absteigend.
- Raster: 3 Spalten Desktop mit Sidebar (4 ohne), 2 mobil. Mit **mindestens 16 Karten** prüfen.
- Produktkarte (bestehend, erweitern): Bild 4:5 auf Sand-Fläche, zweites Bild bei Hover, Titel, Bauart-Zeile, Preis mit „inkl. MwSt.“-Logik aus Shopify, Energieklasse (klein), Farb-Swatches (max. 5 + „+n“), „Ausverkauft“-Badge nur wenn wirklich nicht verfügbar. Keine Sale-Badges.
- Leere Collection: ruhiger Hinweis mit Link zu „Alle Leuchten“.
- Pagination oder „Mehr laden“ — eins von beiden, konsistent.

## Phase 6 — Produktseite

Bestehende Struktur aus `templates/product.json` vervollständigen:

- Above the fold (Desktop): Galerie links mit sichtbaren Thumbnails, rechts Breadcrumb, Titel, Bauart-Zeile, Preis mit Steuer-/Versandhinweis, Energieklasse mit Label und Datenblatt, kurze Value Proposition (`custom.kurzbeschreibung`, neues Metafeld — leer → nichts), Varianten als Swatches, Verfügbarkeit, Lieferzeit, Menge, In den Warenkorb, Express-Checkout.
- Mobil: Galerie als Wischgalerie mit Zähler, Kaufbereich direkt darunter, Sticky-Add-to-Cart-Leiste beim Scrollen.
- Darunter Accordions: Beschreibung · Technische Daten · Maße (Bild `custom.masszeichnung`, falls vorhanden) · Lieferumfang (`custom.lieferumfang`) · Versand & Rückgabe (Text aus Shopify-Richtlinien bzw. Seite, nicht erfinden) · Hersteller & Sicherheit.
- Abschnitt „Passt dazu“: Shopify-Produktempfehlungen.
- Abschnitt „Zuletzt angesehen“ optional, nur wenn sauber ohne App.
- Beschreibungsschema für alle Produkte: Einleitung (2–3 Sätze), Licht & Wirkung, Material & Verarbeitung, Einsatz. In `docs/BESCHREIBUNGSSCHEMA.md` festhalten.

## Phase 7 — Warenkorb, Seiten, Richtlinien

- Cart-Drawer: Produkte mit Bild, Variante, Menge, Preis, Zwischensumme, Hinweis „Versandkosten werden im Checkout berechnet“, Checkout-Button. Kein Upsell, kein Fortschrittsbalken für Gratisversand (nicht entschieden).
- Seiten-Templates mit eigenem Layout im Theme-Design: `page.faq` (Accordion-Liste), `page.kontakt` (Formular + Kontaktdaten aus Shopify), `page.ueber-uns`, `page.versand`, `page.zahlungsarten`, `page.hilfe` (Übersicht, verlinkt FAQ, Versand, Rückgabe, Kontakt).
- Richtlinien-Seiten (Impressum, Datenschutz, AGB, Widerruf, Versand) im Theme-Design angleichen — sie rendern sonst im Default-Layout.
- Seiteninhalte als Entwürfe in `content/seiten/*.md` ablegen, damit ich sie in Shopify einfügen kann. Alles Unbekannte als Marker. **Keine Rechtstexte schreiben.**
- 404 und Suchergebnisse im gleichen Design.

## Phase 8 — Footer

- Spalten: Shop (Kategorien) · Hilfe (Kontakt, Versand, Rückgabe, FAQ, Zahlungsarten) · Ratgeber · Newsletter.
- Unterzeile: Zahlungsarten-Icons, Rechtliches (Impressum, Datenschutz, AGB, Widerrufsbelehrung), Copyright mit `shop.name`.
- Mobil: Spalten als Akkordeon.

## Phase 9 — Platzhalter-Content und Admin-Anleitung

1. **Stockfotos**: Suche frei lizenzierte Fotos (Unsplash oder Pexels) passend zur Designrichtung — Innenleuchten, Außenleuchten, Schreibtischleuchten, Raumszenen für Hero und Kategorien. Nur direkte Bild-URLs verwenden, die du tatsächlich aufgerufen und geprüft hast. Quelle und Fotograf pro Bild in `docs/BILDQUELLEN.md` festhalten.
2. **Produkt-CSV** `data/platzhalter-produkte.csv` im Shopify-Produktimport-Format:
   - 18 Produkte: 8 Innen (verschiedene Bauarten), 6 Außen, 4 Schreibtisch
   - Titel klar als Platzhalter erkennbar, z. B. „Muster Pendelleuchte 01“
   - Tag `platzhalter` plus Einsatzort- und Bauart-Tags, Produkttyp gesetzt
   - Varianten über Option „Farbe“ (2–3 Farben), Variant-Bilder zugeordnet
   - Preise als runde Platzhalterwerte
   - Status `active`
   - **Keine** Werte für Energieklasse, EPREL, WEEE, Hersteller, Lieferzeit oder technische Daten — die bleiben leer, damit die Marker sichtbar sind und nichts Erfundenes im Store landet
   - Bild-URLs aus Schritt 1
3. **`docs/ADMIN-SETUP.md`**: exakte Klickanleitung für mich, in dieser Reihenfolge:
   1. Metafeld-Definitionen anlegen (alle aus `CLAUDE.md` Abschnitt 5 plus neue aus Phase 6, je mit Namespace/Key, Typ, „Filtern erlauben“ ja/nein)
   2. CSV importieren
   3. Automatische Collections mit Tag-Regeln anlegen, inkl. Bild aus Schritt 1
   4. Menüs anlegen (Ziele über die Auswahlliste setzen)
   5. Seiten anlegen und Template zuweisen, Inhalte aus `content/seiten/` einfügen
   6. App „Search & Discovery“ installieren und Filter in dieser Reihenfolge konfigurieren
   7. Theme-Editor: Bilder in Hero und Kacheln zuweisen
   8. Blog `ratgeber` anlegen (vorerst leer)
   9. Aufräumen vor Launch: alle Produkte mit Tag `platzhalter` löschen
4. Hinweis in `docs/ADMIN-SETUP.md`: Stockfotos sind nur Platzhalter. Vor dem Launch durch einheitliche Produktfotos ersetzen (`CLAUDE.md` Abschnitt 8).

## Phase 10 — Shop-Einstellungen, Checkout, E-Mails, Datenschutz

Das liegt fast alles in Shopify Admin. Du bereitest es vor und ergänzt `docs/ADMIN-SETUP.md` um einen zweiten Teil „Vor dem Launch“, jeweils mit Klickpfad, was einzustellen ist und was noch entschieden werden muss (als Marker, nicht raten):

1. **Steuern und Preisanzeige**: Preise inkl. MwSt. anzeigen, Steuerhinweis „inkl. MwSt., zzgl. Versandkosten“ mit Link zur Versandseite — prüfen, dass das Theme das auf Produktseite, Karte und Warenkorb konsistent ausgibt.
2. **Versand**: Versandzonen und -raten pro Lieferant/Lagerland. Werte als Marker, sie kommen vom Lieferanten.
3. **Zahlungsarten**: Shopify Payments, PayPal, Klarna/Rechnung — nur als Checkliste, Entscheidung liegt bei mir. Zahlungsarten-Icons im Theme aus Shopify, nicht hardcoden.
4. **Checkout**: Checkout-Editor an Farben und Schriften angleichen (Werte aus `CLAUDE.md`), Rechtslinks im Checkout-Footer, Pflichtfelder sinnvoll, Telefonnummer optional.
5. **Bestellbestätigung und Benachrichtigungen**: Vorlage für die Bestellbestätigung so anpassen, dass die Widerrufsbelehrung in Textform enthalten ist (§ 312f BGB) und der Wortlaut zum Vertragsschluss in den AGB passt. Liquid-Snippet für die E-Mail in `content/emails/bestellbestaetigung.liquid` vorbereiten, Rechtstext selbst als Platzhalter `[[Widerrufsbelehrung vom Rechtsdienstleister einfügen]]`. Versand- und Stornierungsmails auf Deutsch und im Markenton prüfen.
6. **Cookie-Banner und Einwilligung**: Shopify-Datenschutzeinstellungen (Customer Privacy / Cookie-Banner) für Deutschland aktivieren, Banner im Theme-Design prüfen. Keine Tracking-Pixel oder Analytics ohne Einwilligung.
7. **Newsletter**: Double-Opt-in in den Kundeneinstellungen aktivieren. Anmeldeformular im Theme mit Hinweis auf Datenschutzerklärung.
8. **Kundenkonten**: Entscheidung neue/klassische Kundenkonten als Marker, Konto-Icon im Header nur, wenn aktiviert.
9. **Bewertungen**: Bewertungs-App (z. B. Judge.me) vor dem ersten Verkauf einrichten, aber im Theme ausgeblendet lassen (`CLAUDE.md` Abschnitt 11). Nur als Checklistenpunkt.
10. **SEO und Basis**: Shop-Titel und Meta-Beschreibung (Marker), Meta-Titel-Muster für Kategorien und Produkte, Alt-Texte aus Produkttiteln, Favicon und Social-Sharing-Bild (Marker), strukturierte Produktdaten des Themes prüfen. Passwortseite im Shop-Design gestalten, solange der Shop nicht offen ist.
11. **Bestellabwicklung Dropshipping**: Abschnitt mit offenen Entscheidungen — wie Bestellungen an Lieferanten gehen, wie Lagerbestand synchron bleibt, wie Sendungsnummern zurückkommen. Nichts davon technisch umsetzen, nur dokumentieren.
12. **Rechtstexte**: Checkliste, welche Texte vom Rechtsdienstleister kommen und wo sie in Shopify eingefügt werden (Richtlinien: Impressum, Datenschutz, AGB, Widerruf, Versand). Danach jede Seite im Browser öffnen und nach `[` suchen.

## Phase 11 — QA

- `shopify theme check` → keine neuen Offenses.
- JSON aller Templates valide.
- Visuell prüfen, falls du die Vorschau rendern kannst (Browser-Tool oder `shopify theme dev`): Desktop 1440 und Mobil 375 für Startseite, Collection mit vollem Raster, Produktseite, Warenkorb, Navigation, Filter-Drawer, Suche. Wenn du nicht rendern kannst: ausdrücklich sagen, dass nicht visuell geprüft wurde, und mir eine Liste der Seiten und Breakpoints geben, von denen ich Screenshots schicken soll.
- Nach `[` in allen Templates und Content-Dateien suchen und jede Fundstelle als bewussten Marker bestätigen oder entfernen.

## Abschluss-Report

Format aus `CLAUDE.md` Abschnitt 17:

CHANGED · VERIFIED · REMAINING · CONTENT-TODO · LIEFERANTEN-TODO · SHOPIFY ADMIN · LIVE

Unter VERIFIED nur, was tatsächlich geprüft wurde, mit Angabe wie. Unter LIVE: „Nichts veröffentlicht.“
