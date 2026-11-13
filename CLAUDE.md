# CLAUDE.md — LAMPENSHOP

Projektanweisungen für jede Claude-Code-Sitzung in diesem Repo. Gilt immer, auch wenn ein Prompt etwas anderes nahelegt.

Werte in `[ECKIGEN KLAMMERN]` sind noch nicht entschieden. Nie raten, nie in veröffentlichte Shoptexte übernehmen — im Theme als sichtbarer Marker `[[… — noch festzulegen]]` darstellen.

---

# 1. PROJEKT / ZIEL

Wir bauen einen Shopify-Onlineshop für [MARKENNAME], einen Shop für Leuchten.

Sortiment: zum Start 15–20 Modelle, später erweiterbar. Drei Hauptkategorien: **Innenleuchten**, **Außenleuchten**, **Schreibtischleuchten**.

Zielmarkt: Deutschland.

Bezugsmodell: **Dropshipping ausschließlich aus Lagern innerhalb der EU.** Keine Ware, die zum Zeitpunkt der Bestellung außerhalb der EU lagert. Ein eigenes Lager ist als spätere Option offen (siehe Abschnitt 4) — der Shop wird so gebaut, dass der Wechsel pro Produkt ohne Umbau möglich ist.

Das ist ein **Katalogshop**, kein Einzelproduktshop. Die Collection-Seite ist die wichtigste Seite, nicht die Startseite. Die Startseite routet in Kategorien, sie verkauft nicht selbst ein einzelnes Produkt.

Der Shop soll wie eine etablierte Einrichtungsmarke wirken, nicht wie ein Dropshipping-Store oder eine AI-generierte Website.

---

# 2. MARKE

Name: [MARKENNAME] — im Theme nie hardcoden, immer `shop.name` bzw. Logo-Einstellung
Positionierung: [POSITIONIERUNG]
Support: [SUPPORT-E-MAIL]

Farben (in `config/settings_data.json`, Palette): Hintergrund `#F5F1EA` (warmes Off-White) · Text `#2A2520` · Sekundärtext `#625A50` · Fläche `#EAE3D7` (Sand) · Linien `#D8CEC0`
Typografie: Überschriften Lora, Fließtext DM Sans

Designrichtung: skandinavisch-warm. Viel Weißraum, ruhige Flächen, Material und Licht im Vordergrund, kaum Rundungen (Radius 0–2 px), keine Schatten, keine Verläufe außer dezentem Bild-Overlay.

NICHT:
- generisches Shopify-Design
- Dropshipping-Look
- überladene Gradient-Optik
- billige "AI website"-Ästhetik
- zufällige Animationen
- zu viele Karten, zu viele runde Elemente
- Stock-Website-Ästhetik

---

# 3. SORTIMENTSSTRUKTUR

Hauptkategorien und Unterkategorien (Collection-Handles in Klammern):

- **Innenleuchten** (`innenleuchten`, alle Indoor-Modelle inkl. Schreibtischleuchten)
  - Deckenleuchten (`deckenleuchten`) · Pendelleuchten (`pendelleuchten`) · Wandleuchten (`wandleuchten`) · Stehleuchten (`stehleuchten`) · Tischleuchten (`tischleuchten`)
- **Außenleuchten** (`aussenleuchten`)
  - Außen-Wandleuchten (`aussen-wandleuchten`) · Wegeleuchten (`wegeleuchten`) · Außen-Tischleuchten (`aussen-tischleuchten`)
- **Schreibtischleuchten** (`schreibtischleuchten`) — eigene Hauptkategorie

Ordnungslogik: oben Einsatzort (innen/außen) bzw. Einsatzzweck Schreibtisch, darunter immer Bauart. Keine zusätzliche Raum-Navigation parallel. Schreibtischleuchten stehen nicht zusätzlich unter „Tischleuchten“.

Alle Kategorien sind automatische Collections über Tags (`innen`, `aussen`, `schreibtisch` + Bauart-Tag wie `pendel`, `wand`, `steh`, `tisch`, `decke`, `weg`).

Varianten: hauptsächlich Farbe/Oberfläche, teilweise Größe. Farbe immer als Swatch.

Jede Variante mit eigenem Bild verknüpfen, damit der Bildwechsel funktioniert. Ausverkaufte Varianten sichtbar lassen, nicht ausblenden.

---

# 4. BEZUG UND LIEFERANTEN

## 4.1 Grundregel

Ein Modell kommt nur ins Sortiment, wenn **alle** Punkte der Lieferanten-Checkliste (4.2) mit Nachweis erfüllt sind. Fehlt ein Punkt, wird das Modell nicht angelegt — auch nicht als Entwurf „zum Nachtragen".

„EU-Lager" heißt: Die Ware liegt nachweislich in einem EU-Mitgliedstaat und wird von dort an den Kunden versendet. Angaben wie „EU Warehouse" in einem Marktplatzlisting reichen nicht — Lagerland und Versandland schriftlich bestätigen lassen.

Lieferanten: [LIEFERANTEN, je mit Lagerland]

## 4.2 Lieferanten-Checkliste pro Modell

| Punkt | Nachweis |
|---|---|
| Lagerland innerhalb der EU | schriftliche Bestätigung |
| Hersteller: Name, Postanschrift, E-Mail | für GPSR-Angabe im Angebot |
| EU-verantwortliche Person (falls Hersteller außerhalb der EU) | Name, Anschrift, E-Mail |
| WEEE-Reg.-Nr. für Deutschland | im öffentlichen EAR-Verzeichnis selbst geprüft |
| Energieeffizienzklasse, Energielabel als Datei, Produktdatenblatt | Dateien liegen vor |
| EPREL-Registrierungsnummer | in der EPREL-Datenbank selbst geprüft |
| CE-Konformitätserklärung | Dokument liegt vor |
| Deutschsprachige Anleitung und Sicherheitshinweise | Dokument liegt vor |
| Verpackung für Deutschland lizenziert (VerpackG) | schriftliche Bestätigung, sonst eigene LUCID-Pflicht |
| Batterie/Akku enthalten? | falls ja: Registrierung nach BattG prüfen |
| Lieferzeit ab Bestellung bis Zustellung in DE | schriftlich, realistisch |
| Versandkosten und Versanddienstleister | schriftlich |
| Rücksendeadresse in der EU, Ablauf bei Widerruf | schriftlich |
| Umgang mit Transportschäden / Bruch | schriftlich |
| Neutraler Versand (keine Fremdrechnung, keine Fremdwerbung im Paket) | schriftlich |
| Lagerbestand abrufbar (Feed, Liste oder Ansprechpartner) | Weg festgelegt |
| Datenweitergabe an den Lieferanten | Auftragsverarbeitung / Datenschutzerklärung berücksichtigt |

**Warum die WEEE-Nummer selbst prüfen:** Hat der Hersteller keine deutsche EAR-Registrierung, kann die Herstellerpflicht nach ElektroG auf den Shop zurückfallen. Das ist vom Rechtsdienstleister zu bestätigen, nicht selbst zu entscheiden.

## 4.3 Eigenes Lager (Option)

Wird später selbst gelagert, ändern sich pro Produkt: Lieferzeit, Versandkosten, Rücksendeadresse, ggf. LUCID-Pflicht. Deshalb liegen diese Angaben pro Produkt in Metafeldern (Abschnitt 5) und nicht pauschal im Theme. Ware aus EU-Großhandel selbst zu lagern macht den Shop nicht zum Importeur. Eigener Import aus Drittstaaten ist ein anderes Modell und braucht eine eigene Prüfung.

## 4.4 Bestellabwicklung

Bestellweg zum Lieferanten: [MANUELL / APP / SCHNITTSTELLE — noch festzulegen]

Mehrere Lieferanten bedeuten: Eine Bestellung kann in mehreren Paketen kommen. Das muss in Versandseite und FAQ stehen, wenn es vorkommen kann.

Lagerbestand in Shopify muss den echten Bestand beim Lieferanten abbilden. Nichts verkaufen, was nicht lieferbar ist.

---

# 5. PRODUKTDATEN

Shopify ist die Quelle der Wahrheit für Produktname, Preis, Varianten, Verfügbarkeit, Inventar, Bilder, Vendor, Navigation und Richtlinien. Diese Daten nie im Theme hardcoden und nie durch erfundene Werte kaschieren.

Technische Daten gehören in **Metafelder**, nicht in den Beschreibungstext — nur so sind sie filter- und vergleichbar.

Feld-Set:

| Feld | Typ | sichtbar |
|---|---|---|
| Lichtstrom (lm) | Zahl | ja |
| Farbtemperatur (K) | Zahl | ja |
| Leistung (W) | Zahl | ja |
| Sockel | Text | ja |
| Leuchtmittel fest / wechselbar | Auswahl | ja |
| Leuchtmittel im Lieferumfang | ja/nein | ja |
| Dimmbar | ja/nein | ja |
| IP-Schutzart | Text | ja |
| Material | Text | ja |
| Maße | Text | ja |
| Kabellänge | Text | ja |
| Energieeffizienzklasse | Text | ja |
| Energielabel | Datei | ja |
| Produktdatenblatt | Datei | ja |
| EPREL-Nummer | Text | ja |
| Hersteller (Name, Anschrift, E-Mail) | Text | ja (GPSR) |
| EU-verantwortliche Person | Text | ja (GPSR, falls zutreffend) |
| WEEE-Reg.-Nr. | Text | ja |
| Sicherheitshinweise / Anleitung | Datei | ja |
| Lieferzeit | Text | ja |
| Kurzbeschreibung (eine Zeile) | Text | ja |
| Vorteile (max. 3) | Liste Text | ja |
| Raumbild | Datei (Bild) | ja |
| Maßzeichnung | Datei (Bild) | ja |
| Lieferumfang | mehrzeiliger Text | ja |
| Geeignet für (Räume) | Liste Text | ja |
| Serie | Text | ja |
| Passende Leuchtmittel | Produktreferenz (Liste) | ja |
| Versand aus (Land) | Text | intern |
| Lieferant | Text | intern |
| Rücksendeadresse | Text | intern |

Das Feld-Set steht **vor** dem Anlegen der Produkte. Zwanzig Produkte nachträglich umzustrukturieren ist fehleranfällig.

NIEMALS Produktdaten erfinden. Fehlt ein Wert, bleibt die Stelle leer oder ein sichtbarer Marker — keine Schätzung, keine Näherung. Werte von Lieferantenseiten nicht ungeprüft übernehmen, sondern gegen Datenblatt und EPREL abgleichen.

Interne Felder (Lieferant, Versandland, Rücksendeadresse) nie im Frontend ausgeben.

---

# 6. COLLECTION-SEITE UND PRODUKTKARTE

Die Collection-Seite ist die wichtigste Seite im Shop.

Produktkarte zeigt: Bild auf einheitlichem Hintergrund (Hover: Raumbild mit Licht an), Modellname, Kurzzeile zur Bauart, Preis, Lieferzeit, Varianten-Indikator, Verfügbarkeit, Energieeffizienzklasse.

Die Karte muss zwanzigmal nebeneinander funktionieren, nicht einmal allein. Immer mit vollem Raster prüfen, nie mit drei Testprodukten.

Filter (über die Shopify-App „Search & Discovery“): Verfügbarkeit, Preis, Farbe, Bauart (Produkttyp), Material, Dimmbar, Farbtemperatur, IP-Schutzart (v. a. Außen), Energieeffizienzklasse.
Sortierung: mindestens Preis und Neuheit.

Suche gehört prominent in den Header.

---

# 7. PRODUKTSEITE

Above the fold sofort sichtbar:

- Galerie mit sichtbarer Thumbnail-Reihe, kein Karussell hinter Pfeilen
- Produktname
- Preis mit Steuerhinweis
- Energieeffizienzklasse mit Klassenspektrum und Label
- kurze Value Proposition
- Variantenauswahl
- Verfügbarkeit
- Lieferzeit (aus dem Metafeld, pro Produkt)
- Menge
- Add-to-Cart

Darunter: technische Daten aus den Metafeldern, Maßzeichnung oder Maßangaben, Lieferumfang, Produktdatenblatt, Herstellerangaben nach GPSR, Sicherheitshinweise, passende Produkte.

Der Kaufbereich bleibt kurz. Details in Accordions. Herstellerangaben und Sicherheitsinformationen dürfen im Accordion stehen, müssen aber ohne Umweg auffindbar sein.

Beschreibungsschema für alle Modelle gleich: gleiche Abschnitte, gleiche Reihenfolge, vergleichbare Länge.

---

# 8. BILDER

Ein festes Bildrezept für alle Modelle: gleicher Hintergrund, gleiche Perspektive, gleicher Ausschnitt, gleiche Lichtsituation.

Uneinheitliche Produktbilder sind das stärkste Dropshipping-Signal überhaupt — sichtbarer als jeder Text.

Beim Dropshipping sind Lieferantenbilder der Normalfall. Deshalb:

- Nutzungsrechte an Lieferantenbildern schriftlich bestätigen lassen.
- Lieferanten bevorzugen, deren Bilder bereits einheitlich sind (freigestellt, gleicher Hintergrund).
- Lieferantenbilder angleichen (Hintergrund, Ausschnitt, Format) — aber nur an Hintergrund und Ausschnitt arbeiten, nie am Produkt selbst.
- Wo möglich Muster bestellen und selbst nach Rezept fotografieren. Lieber alle Modelle einheitlich in mittlerer Qualität als einige gute und viele fremde.

Keine erfundenen Produktfeatures visualisieren. Kein Produkt darf anders aussehen als in echt. Keine Raumszenen generieren, die Größe oder Lichtwirkung verfälschen.

---

# 9. NAVIGATION

Das Hauptmenü wird in Shopify Admin gepflegt (Online Store → Navigation), NICHT im Theme. Keine Navigation ins Liquid hardcoden.

Struktur Hauptmenü (Handle `main-menu`): Innenleuchten (Mega-Menü mit Unterkategorien) · Außenleuchten (Mega-Menü) · Schreibtischleuchten · Neu · Hilfe

Menüziele über die Shopify-Auswahlliste setzen, nicht eintippen. Eingetippte Adressen landen als absolute `myshopify.com`-Links und werfen Kunden aus der eigenen Domain.

Header sticky mit subtilem kompaktem Zustand. Suche und Cart immer erreichbar, auch mobil.

---

# 10. FOOTER

SHOP — Kategorien
HILFE — Kontakt, Versand, Rückgabe, FAQ
RECHTLICHES — Impressum, Datenschutzerklärung, AGB, Widerrufsbelehrung, Zahlungsarten, Entsorgung & Rücknahme (ElektroG/BattG-Hinweise, Text vom Rechtsdienstleister)

Alle Links auf echte Shopify-Seiten oder Richtlinien. Fehlende Seiten als sichtbarer Marker `[[NAME — noch festzulegen]]`, nicht verstecken.

Seiten-Handles prüfen: Eine Seite mit dem Titel „FAQs" bekommt den Handle `faqs`, nicht `faq`.

---

# 11. TRUST

NIEMALS erfinden: Bewertungen, Kundenzahlen, Awards, Zertifikate, Tests, Verkaufszahlen, Lieferzeiten, Garantien, Statistiken.

Keine Bewertungen vom Lieferanten oder aus Marktplatzlistings übernehmen. Das sind keine Bewertungen dieses Shops.

Bewertungen bleiben zum Launch ausgeblendet. Keine leeren Sterne, keine „0 Bewertungen", und keine Section, die das Fehlen erklärt.

Trust entsteht über: vollständige technische Daten, Zahlungsarten mit Käuferschutz, vollständiges Impressum, einheitliche Fotos, ehrliche Lieferzeiten, erreichbarer Support mit realistischer Reaktionszeit.

KEINE DARK PATTERNS: keine Countdowns, keine Verknappungshinweise, keine durchgestrichenen Fantasiepreise.

---

# 12. DEUTSCHES RECHT

NIEMALS selbst formulieren: Impressum, AGB, Widerrufsbelehrung, Datenschutzerklärung. Diese Texte kommen vom Rechtsdienstleister. Dem Dienstleister das Dropshipping-Modell und die Lagerländer ausdrücklich mitteilen.

Die Widerrufsbelehrung folgt dem amtlichen Muster aus Anlage 1 zu Art. 246a EGBGB. Wortlaut nicht ändern, auch nicht aufs Du umschreiben.

NIEMALS erfinden: Lieferzeiten, Versandkosten, Rückgabebedingungen, Garantien. Das sind verbindliche Zusagen. Sie kommen aus den schriftlichen Angaben des Lieferanten (Abschnitt 4.2).

Gewährleistung und Widerruf liegen gegenüber dem Kunden immer beim Shop, nicht beim Lieferanten.

**Lampenspezifisch — vor dem Verkauf zu klären:**

- Energieeffizienzkennzeichnung: Klasse und Klassenspektrum beim Angebot sichtbar, Label und Produktdatenblatt abrufbar. EPREL-Daten vom Lieferanten.
- ElektroG: WEEE-Reg.-Nr. des Herstellers beim Angebot angeben. Mit dem Rechtsdienstleister klären, ob durch das Bezugsmodell eigene Pflichten bei der Stiftung EAR entstehen.
- Verpackungsgesetz: klären, ob der Lieferant die Verpackung für Deutschland lizenziert hat oder ob eigene LUCID-Registrierung und Systembeteiligung nötig sind.
- Batteriegesetz, falls Modelle mit Akku dabei sind.
- GPSR: Hersteller und ggf. EU-verantwortliche Person beim Angebot, Sicherheitsinformationen, CE-Kennzeichnung, Konformitätserklärung, deutschsprachige Anleitung.

**PLATZHALTER-KONTROLLE:** Vorlagen mit eckigen Klammern sind Arbeitsmaterial, kein Veröffentlichungstext. Nach jedem Einfügen eines Rechtstextes die veröffentlichte Seite im Browser aufrufen und nach `[` suchen.

**KONSISTENZPFLICHTEN:**

| Aussage | Muss übereinstimmen in |
|---|---|
| Rücksendekosten | Widerrufsbelehrung · Rückgabeseite |
| Rücksendeadresse | Widerrufsbelehrung · Rückgabeseite · Lieferantenvereinbarung |
| Lieferzeit | FAQ · Versandseite · Produktseite · Lieferantenangabe |
| Teillieferungen | Versandseite · FAQ |
| Steuerhinweis | Produktseite · Collection · AGB |
| Firmendaten | Impressum · Kontaktinformationen · Widerrufsbelehrung · AGB |
| Energieklasse | Produktseite · Produktkarte · Datenblatt · EPREL |

Widersprüche gehen im Zweifel zulasten des Händlers.

Die Widerrufsbelehrung muss zusätzlich in Textform in die Bestellbestätigung (§ 312f BGB).

Kein Online-Widerrufsformular bauen — das löst eine Bestätigungspflicht aus, die Shopify nicht automatisch erfüllt.

Kein Hinweis auf die EU-Streitbeilegungsplattform. Die wurde im Juli 2025 eingestellt.

---

# 13. CODE-PRINZIPIEN

Theme: Horizon 4.5.0 (Shopify), erweitert.

Workflow: Das Repo `leokbrg/Lampenshop`, Branch `main`, ist per Shopify-GitHub-Integration mit einem **unveröffentlichten** Theme-Entwurf im Store `dvrt17-hw.myshopify.com` verbunden. Jeder Push auf `main` landet automatisch in diesem Entwurf. Niemals veröffentlichen. Lokal optional: `shopify theme dev --store dvrt17-hw`.

`config/settings_data.json` und `templates/*.json` können vom Theme-Editor überschrieben werden — vor Änderungen `git pull`, damit Editor-Änderungen nicht verloren gehen.

Innerhalb der bestehenden Theme-Struktur arbeiten. Liquid sauber schreiben, Schemas Shopify-kompatibel, JSON valide. Keine unnötigen Dependencies oder Apps. Keine Hardcoding-Lösungen, wenn Shopify-Daten verfügbar sind.

Lieferzeit, Herstellerangaben, Energieklasse und Label immer aus Metafeldern rendern. Fehlt ein Pflicht-Metafeld, sichtbaren Marker im Preview zeigen, nicht still überspringen.

Bekannte Fehlerquellen:

- `shop.policies` ist eine Liste, keine Zuordnung. Richtig: `shop.privacy_policy`, `shop.refund_policy`, `shop.shipping_policy`, `shop.terms_of_service`.
- CSS-Variablen, die aus anderen Variablen zusammengesetzt werden, können garantiert ungültig sein und vererben sich dann leer.
- Variablen aus Farbschemata stehen außerhalb dieser Schemata nicht zur Verfügung, etwa bei `<dialog>`-Backdrops.
- Reveal-Klassen nach der Beobachtungsschleife setzen, sonst bleibt bei einem Fehler die Seite unsichtbar.
- Font-Weight-Tokens müssen tatsächlich definiert sein.
- Policy- und Page-Templates rendern im Default-Layout und müssen separat angeglichen werden.

Nach Änderungen: `shopify theme check` → 0 offenses.

---

# 14. VISUAL QA

Code, der validiert, sieht nicht automatisch gut aus.

Nach jeder Designrunde gerendert prüfen:

DESKTOP 1440: Startseite, Collection mit vollem Raster, Produktseite, Cart
MOBILE 375: dieselben plus Navigation und Filter

Prüfen: Spacing, Alignment, Typografie, Bildausschnitte, CTA-Sichtbarkeit, Textumbruch, Overflow, Kontraste.

Kontraste messen, nicht schätzen.

Mobile darf nicht wie zusammengeschobenes Desktop wirken.

Nie behaupten, etwas sei visuell geprüft, wenn es nicht gerendert angesehen wurde.

---

# 15. STAGING / LIVE

NIEMALS automatisch live pushen.

Workflow: lokal entwickeln → theme check → Preview → visuelle Prüfung → Funktionsprüfung → Admin-Daten prüfen → erst nach ausdrücklicher Freigabe live.

Vor dem Launch zusätzlich: eine Testbestellung pro Lieferant komplett durchspielen — Bestellung, Weiterleitung, Versand, Zustellzeit messen, Rücksendung.

Nach jedem Arbeitsschritt einzeln committen.

---

# 16. ARBEITSWEISE

Eigenständig arbeiten, nicht bei jeder kleinen Designentscheidung nachfragen.

Reihenfolge: Codebase untersuchen → planen → implementieren → validieren → visuell prüfen → Fehler beheben.

Wenn Informationen fehlen: keine Fakten erfinden, bestmögliche neutrale Lösung bauen, offen dokumentieren, was fehlt.

Mit drei bis fünf vollständig gepflegten Produkten anfangen — Checkliste 4.2 komplett erfüllt —, Schema prüfen, dann den Rest nachziehen. Nicht zwanzig halbfertige Produkte anlegen.

**Ausnahme Aufbauphase:** Solange der Shop nicht live ist, dürfen Muster-Produkte mit Stockfotos angelegt werden, um Layout und Raster zu prüfen. Bedingungen: Titel beginnt mit „Muster“, Tag `platzhalter`, keine erfundenen technischen oder rechtlichen Werte (Energieklasse, EPREL, WEEE, Hersteller, Lieferzeit, technische Daten bleiben leer). Vor dem Launch werden alle Produkte mit Tag `platzhalter` gelöscht und alle Stockfotos ersetzt.

---

# 17. REPORTING

Nach größeren Arbeitsphasen:

CHANGED · VERIFIED · REMAINING · CONTENT-TODO · LIEFERANTEN-TODO · SHOPIFY ADMIN · LIVE

---

# 18. PROJEKTKONTEXT

Ein Chat lädt Projektanweisungen und Projektdokumente beim Start. Ein Chat, der vor einer Aktualisierung geöffnet wurde, arbeitet weiter mit dem alten Stand.

Nach jeder Aktualisierung in laufende Chats „Projektkontext aktualisiert" schreiben, damit sie neu einlesen.

[Falls wieder mit mehreren Chats gearbeitet wird: Übergabeprotokoll aus dem alten Projekt übernehmen.]

---

# 19. GOLDEN RULE

Das Ziel ist nicht, einen Shopify-Store mit viel Code zu bauen.

Das Ziel ist ein glaubwürdiger Leuchtenshop, in dem ein Kunde zwischen 15–20 Modellen sicher das richtige findet, ohne Zögern kauft — und die Lampe pünktlich, unbeschädigt und rechtssicher bekommt.

Jede technische und gestalterische Entscheidung dient diesem Ziel.

---

# 20. QUALITÄTSMASSSTAB

`docs/REFERENZANALYSE.md` ist der Maßstab für Aufbau und Qualität von Startseite und Produktseite. Abschnitt 6 legt die Module fest, Abschnitt 5 zeigt die leuchtenspezifischen Muster (Lampenwelt), Abschnitt 4 was nicht übernommen wird, Abschnitt 7 die Prüffragen für jede visuelle Prüfung.

Kurzfassung: Einheitliche Produktbilder mit festen Bildrollen vor allem anderen (freigestellt, Licht an, Maßzeichnung). Leuchtmittel enthalten ja/nein und Sockel immer am Kaufbutton. Erster Bildschirm führt in Kategorien. Pro Sektion eine Aussage. Kauf-Button ist das auffälligste Element. Lieferzeit direkt am Button. Produkt-Raster und großflächige Stimmungsbilder wechseln sich ab. Jede Seite endet mit einem Weg weiter.

---

# 21. AKTUELLER STAND DES THEMES

Bereits vorhanden (nicht neu bauen, sondern erweitern):

- `blocks/energy-class.liquid` — EU-Energiepfeil mit Spektrum A–G, Klick öffnet Label (`custom.energielabel`), optional Datenblatt-Link. In Produktkarten und Produktseite eingebunden.
- `blocks/lamp-specs.liquid` — technische Daten aus `custom.*`
- `blocks/delivery-time.liquid` — Lieferzeit aus `custom.lieferzeit`
- `blocks/product-safety-info.liquid` — Hersteller, EU-verantwortliche Person, WEEE, Dokumente
- `.lamp-marker` in `assets/base.css` — Marker für fehlende Pflichtdaten, nur im Theme-Editor (`request.design_mode`)
- Produktkarten mit Bauart-Zeile (`product.type`), Energieklasse, Swatches
- Produktseite mit Thumbnail-Galerie, Accordions (Beschreibung, Technische Daten, Hersteller & Sicherheit)
- Startseite: Hero, „Nach Bauart“-Kacheln, „Neu im Sortiment“ — wird gemäß Bau-Prompt umgebaut
- Footer: Menüs `footer-shop`, `footer-hilfe`, Policy-Liste

`shopify theme check`: 7 Warnungen stammen aus unverändertem Horizon-Code (header, divider, product-media-gallery-content). Neue Dateien müssen 0 Offenses haben.
