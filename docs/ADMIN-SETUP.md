# Admin-Setup — Schritt für Schritt

Alles, was nicht im Theme liegt, wird hier in Shopify Admin angelegt. Reihenfolge einhalten: Spätere Schritte bauen auf früheren auf (Metafelder vor Produkten, Collections vor Menüs, Seiten vor Menüs).

Store: `dvrt17-hw.myshopify.com` · Theme: unveröffentlichter Entwurf, verbunden mit Branch `main`.

> **Stockfotos sind nur Platzhalter.** Vor dem Launch werden sie durch einheitliche Produktfotos nach festem Bildrezept ersetzt (`CLAUDE.md` Abschnitt 8). Kein Stockfoto bleibt an einem echten Produkt. Stand der Bildauswahl: `docs/BILDQUELLEN.md`.

> **Nichts veröffentlichen.** Keinen Schritt hier schließt „Theme veröffentlichen“ ein.

Begleitdokumente: `docs/STRUKTUR.md` (Handles, Tags, Menüs) · `docs/BESCHREIBUNGSSCHEMA.md` · `content/seiten/` (Seitentexte).

---

## 0. Vorab: Branch in den Theme-Entwurf bringen

Die Arbeit liegt auf dem Branch `claude/charming-curie-ub6fxb`. Der Theme-Entwurf im Store folgt `main`. Erst nach dem Zusammenführen (Pull Request auf GitHub → Merge in `main`) sind die neuen Templates im Theme-Editor sichtbar. Vorher lassen sich in Schritt 5 die Seiten-Templates nicht auswählen.

---

## 1. Metafeld-Definitionen anlegen

**Einstellungen → Metafelder und Metaobjekte → Produkte → Definition hinzufügen.**

Für jede Zeile: Name eintragen → „Namespace und Schlüssel“ prüfen und auf den Wert der Tabelle setzen (Shopify schlägt aus dem Namen etwas vor; **der Schlüssel muss exakt stimmen**, sonst liest das Theme das Feld nicht) → Typ wählen → speichern.

„Storefront“ = Schalter **„Storefront-Zugriff“** in der Definition. „Filter“ = Feld wird später in Search & Discovery als Filter angeboten; dafür muss der Storefront-Zugriff an sein.

| # | Name | Namespace und Schlüssel | Typ | Storefront | Filter |
|---|---|---|---|---|---|
| 1 | Lichtstrom (lm) | `custom.lichtstrom` | Ganzzahl | ja | nein |
| 2 | Farbtemperatur (K) | `custom.farbtemperatur` | Ganzzahl | ja | **ja** |
| 3 | Leistung (W) | `custom.leistung` | Dezimalzahl | ja | nein |
| 4 | Sockel | `custom.sockel` | Einzeiliger Text | ja | nein |
| 5 | Leuchtmittel | `custom.leuchtmittel` | Einzeiliger Text, „Auf voreingestellte Auswahl beschränken“: `fest verbaut`, `wechselbar` | ja | nein |
| 6 | Leuchtmittel im Lieferumfang | `custom.leuchtmittel_im_lieferumfang` | Wahr oder falsch | ja | nein |
| 7 | Dimmbar | `custom.dimmbar` | Wahr oder falsch | ja | **ja** |
| 8 | IP-Schutzart | `custom.ip_schutzart` | Einzeiliger Text | ja | **ja** |
| 9 | Material | `custom.material` | Einzeiliger Text | ja | **ja** |
| 10 | Maße | `custom.masse` | Mehrzeiliger Text | ja | nein |
| 11 | Kabellänge | `custom.kabellaenge` | Einzeiliger Text | ja | nein |
| 12 | Energieeffizienzklasse | `custom.energieeffizienzklasse` | Einzeiliger Text, Auswahl: `A`, `B`, `C`, `D`, `E`, `F`, `G` | ja | **ja** |
| 13 | Energielabel | `custom.energielabel` | Datei (Bilder und PDF zulassen) | ja | nein |
| 14 | Produktdatenblatt | `custom.produktdatenblatt` | Datei (PDF) | ja | nein |
| 15 | EPREL-Nummer | `custom.eprel_nummer` | Einzeiliger Text | ja | nein |
| 16 | Hersteller | `custom.hersteller` | Mehrzeiliger Text (Name, Anschrift, E-Mail) | ja | nein |
| 17 | EU-verantwortliche Person | `custom.eu_verantwortliche_person` | Mehrzeiliger Text | ja | nein |
| 18 | WEEE-Reg.-Nr. | `custom.weee_nummer` | Einzeiliger Text | ja | nein |
| 19 | Sicherheitshinweise / Anleitung | `custom.sicherheitshinweise` | Datei (PDF) | ja | nein |
| 20 | Lieferzeit | `custom.lieferzeit` | Einzeiliger Text | ja | nein |
| 21 | Kurzbeschreibung *(neu)* | `custom.kurzbeschreibung` | Einzeiliger Text, max. 140 Zeichen | ja | nein |
| 22 | Maßzeichnung *(neu)* | `custom.masszeichnung` | Datei (nur Bilder) | ja | nein |
| 23 | Lieferumfang *(neu)* | `custom.lieferumfang` | Einzeiliger Text → **Liste von Werten** | ja | nein |
| 24 | Versand aus (Land) | `custom.versand_aus` | Einzeiliger Text | **nein** | nein |
| 25 | Lieferant | `custom.lieferant` | Einzeiliger Text | **nein** | nein |
| 26 | Rücksendeadresse | `custom.ruecksendeadresse` | Mehrzeiliger Text | **nein** | nein |

Hinweise:

- **24–26 sind intern.** Storefront-Zugriff ausgeschaltet lassen. Das Theme gibt sie nirgends aus; der ausgeschaltete Zugriff ist die zweite Sicherung.
- **Material als Filter:** Werte einheitlich schreiben („Stahl, pulverbeschichtet“ ist ein anderer Filterwert als „Stahl pulverbeschichtet“). Am besten vorab eine feste Wortliste festlegen.
- **Farbtemperatur als Filter:** Search & Discovery zeigt Zahlen als Bereichs- oder Listenfilter. Wenige feste Stufen (2700, 3000, 4000) ergeben eine lesbare Liste.
- Bei den Muster-Produkten bleiben **alle** diese Felder leer. Im Theme-Editor erscheinen dafür gelbe Marker („[[… fehlt]]“), im Shop nichts.

### Farb-Swatches

Farbkreise auf Produktkarte, Produktseite und im Filter zeigt Shopify nur, wenn die Option „Farbe“ mit dem Kategorie-Metafeld **Farbe** verknüpft ist. Das geht nicht per CSV, sondern nach dem Import (Schritt 2):

1. Ein Produkt öffnen → **Kategorie** setzen (z. B. „Haus & Garten > Beleuchtung > Lampen“ bzw. die passendste Leuchten-Kategorie).
2. Bei Varianten die Option „Farbe“ bearbeiten → **„Mit Metafeld verbinden“ → Farbe**. Shopify legt die Farbwerte als Einträge an; pro Eintrag einmal den Farbton wählen (Schwarz, Weiß, Messing, Sand, Anthrazit, Salbei).
3. Für die übrigen Produkte: Produkte → alle Muster-Produkte markieren → **Massenbearbeitung** → Kategorie setzen; die Option je Produkt verbinden.

Ohne diese Verknüpfung erscheinen Farben als Text-Buttons statt als Swatches. Das Theme hinterlegt bewusst keine eigene Farbtabelle.

---

## 2. Produkt-CSV importieren

1. **Produkte → Importieren → Datei hinzufügen** → `data/platzhalter-produkte.csv`.
2. „Produkte mit übereinstimmenden Handles überschreiben“: beim ersten Import egal, bei Wiederholung anhaken.
3. Vorschau prüfen: 18 Produkte, Option „Farbe“, Status aktiv → **Produkte importieren**.
4. Nach dem Import kontrollieren (Produkte, Filter „Getaggt mit: platzhalter“): 18 Produkte, 41 Varianten.

Was die CSV enthält: Titel „Muster …“, Produkttyp, Tags (`platzhalter` + Einsatzort + Bauart), 2–3 Farbvarianten, runde Platzhalterpreise, Bestand 10 je Variante. **Absichtlich zum Testen:** „Muster Wandleuchte 01“ hat eine ausverkaufte Variante (Schwarz), „Muster Wegeleuchte 02“ ist komplett ausverkauft — daran lässt sich prüfen, dass ausverkaufte Varianten sichtbar bleiben und das Badge erscheint.

Was sie **nicht** enthält: Energieklasse, EPREL, WEEE, Hersteller, Lieferzeit, technische Daten, Gewicht, Vergleichspreise. Nicht nachtragen — für Muster-Produkte wird nichts erfunden.

**Bilder:** Die CSV enthält derzeit keine Bild-URLs (siehe `docs/BILDQUELLEN.md`). Sobald `data/platzhalter-bilder.csv` ausgefüllt ist: `python3 tools/build_csv.py` ausführen und die CSV erneut importieren (mit „überschreiben“). Alternativ Bilder pro Produkt von Hand hochladen und **jeder Variante ihr Bild zuweisen** (Variante öffnen → Bild wählen), sonst wechselt das Bild beim Farbwechsel nicht.

**Hersteller-Feld (Vendor):** In der CSV leer; Shopify trägt beim Import den Shopnamen ein. Das Theme zeigt den Vendor nirgends an.

**Vergleichspreis:** Bei allen Produkten leer lassen. Ein gesetzter Vergleichspreis erzeugt einen durchgestrichenen Preis.

---

## 3. Automatische Collections anlegen

**Produkte → Collections → Collection erstellen.** Zwölf Stück, jeweils:

1. **Titel** laut Tabelle.
2. **Beschreibung:** vorerst leer lassen oder den Marker aus `docs/STRUKTUR.md` einsetzen.
3. **Collection-Typ: Automatisch.**
4. **Bedingungen:** „Produkte müssen **allen** Bedingungen entsprechen“ (Ausnahme: `neu`), je Zeile „Produkt-Tag · ist gleich · …“.
5. **Suchmaschinen-Eintrag → bearbeiten → URL-Handle** kontrollieren (muss exakt stimmen).
6. **Bild:** Kategoriebild im Format 4:5 hochladen (Slots `kategorie-…` in `data/platzhalter-bilder.csv`). Ohne Bild zeigen Kacheln und Mega-Menü eine leere Fläche.
7. Speichern, dann oben **Sortieren** laut Tabelle einstellen.

| Titel | URL-Handle | Bedingungen | Sortieren |
|---|---|---|---|
| Innenleuchten | `innenleuchten` | Tag = `innen` | Manuell |
| Deckenleuchten | `deckenleuchten` | Tag = `innen` UND Tag = `decke` | Manuell |
| Pendelleuchten | `pendelleuchten` | Tag = `innen` UND Tag = `pendel` | Manuell |
| Wandleuchten | `wandleuchten` | Tag = `innen` UND Tag = `wand` | Manuell |
| Stehleuchten | `stehleuchten` | Tag = `innen` UND Tag = `steh` | Manuell |
| Tischleuchten | `tischleuchten` | Tag = `innen` UND Tag = `tisch` | Manuell |
| Außenleuchten | `aussenleuchten` | Tag = `aussen` | Manuell |
| Außen-Wandleuchten | `aussen-wandleuchten` | Tag = `aussen` UND Tag = `wand` | Manuell |
| Wegeleuchten | `wegeleuchten` | Tag = `aussen` UND Tag = `weg` | Manuell |
| Außen-Tischleuchten | `aussen-tischleuchten` | Tag = `aussen` UND Tag = `tisch` | Manuell |
| Schreibtischleuchten | `schreibtischleuchten` | Tag = `schreibtisch` | Manuell |
| Neu | `neu` | „**einer** Bedingung entsprechen“: Tag = `innen` ODER Tag = `aussen` | **Neueste zuerst** |

„Manuell“ ist die Sortierung, die im Shop als „Empfohlen“ erscheint. Das Theme bietet Kunden außerdem „Neu“, „Preis aufsteigend“ und „Preis absteigend“ an.

Kontrolle: Innenleuchten 12 Produkte (8 + 4 Schreibtisch), Außenleuchten 6, Schreibtischleuchten 4, Tischleuchten 1 (ohne Schreibtischleuchten), Neu 18.

---

## 4. Menüs anlegen

**Onlineshop → Navigation.** Ziele immer über die **Auswahlliste** setzen (ins Link-Feld klicken → „Collections“ / „Seiten“ → Eintrag wählen), nie eine Adresse eintippen — eingetippte Adressen werden zu absoluten `myshopify.com`-Links.

Seiten-Ziele (Hilfe, Kontakt …) gibt es erst nach Schritt 5. Entweder Schritt 5 vorziehen oder die Seiten-Einträge danach ergänzen.

### 4.1 Hauptmenü

Das vorhandene Menü „Hauptmenü“ (Handle `main-menu`) bearbeiten, alte Einträge löschen. Unterpunkte entstehen, indem ein Eintrag per Drag & Drop **eingerückt** unter einen anderen gezogen wird.

```
Innenleuchten            → Collection Innenleuchten
   Alle Innenleuchten    → Collection Innenleuchten
   Deckenleuchten        → Collection Deckenleuchten
   Pendelleuchten        → Collection Pendelleuchten
   Wandleuchten          → Collection Wandleuchten
   Stehleuchten          → Collection Stehleuchten
   Tischleuchten         → Collection Tischleuchten
Außenleuchten            → Collection Außenleuchten
   Alle Außenleuchten    → Collection Außenleuchten
   Außen-Wandleuchten    → Collection Außen-Wandleuchten
   Wegeleuchten          → Collection Wegeleuchten
   Außen-Tischleuchten   → Collection Außen-Tischleuchten
Schreibtischleuchten     → Collection Schreibtischleuchten
Neu                      → Collection Neu
Hilfe                    → Seite Hilfe
```

Dieses Menü steuert auch die Unterkategorie-Pills auf den Collection-Seiten und den Breadcrumb auf der Produktseite.

### 4.2 Footer-Menüs

Je **Menü hinzufügen**. Der Handle entsteht aus dem Titel — Titel deshalb genau so schreiben und den Handle rechts kontrollieren.

| Titel | Handle | Einträge |
|---|---|---|
| Footer Shop | `footer-shop` | Innenleuchten · Außenleuchten · Schreibtischleuchten · Neu (jeweils Collection) · Alle Leuchten (→ „Alle Produkte“) |
| Footer Hilfe | `footer-hilfe` | Kontakt · Versand · Rückgabe · FAQ · Zahlungsarten (jeweils Seite) |
| Footer Ratgeber | `footer-ratgeber` | Alle Ratgeber (→ Blogs → Ratgeber). Erst anlegen, wenn es Artikel gibt — vorher blendet der Footer die Spalte aus. |

Die Überschriften der Footer-Spalten („Shop“, „Hilfe“, „Ratgeber“) stehen im Theme, nicht im Menü-Titel.

Rechtliches braucht kein Menü: Die Unterzeile listet automatisch alle Richtlinien aus **Einstellungen → Richtlinien**.

---

## 5. Seiten anlegen, Template zuweisen, Inhalte einfügen

**Onlineshop → Seiten → Seite hinzufügen.** Pro Seite:

1. Titel laut Tabelle.
2. Inhalt aus der Datei in `content/seiten/` kopieren (nur den Teil unter „## Inhalt“). Marker `[[…]]` bleiben vorerst stehen.
3. **Suchmaschinen-Eintrag → URL-Handle** setzen (bei Umlauten von Hand!).
4. Rechts **Theme-Template** wählen. Achtung: Die Auswahlliste zeigt nur Templates des **veröffentlichten** Themes. Solange das Lampenshop-Theme ein Entwurf ist, tauchen `faq`, `kontakt` usw. dort voraussichtlich nicht auf. Dann:
   - Seiten jetzt mit Standard-Template anlegen (Titel, Handle, Inhalt stimmen schon).
   - Zum Prüfen im Entwurf: **Anpassen** → oben im Seitenwähler **Seiten** → das Template (z. B. „faq“) öffnen; die Vorschau zeigt es mit einer Beispielseite.
   - Die Zuweisung in dieser Tabelle direkt nach dem Veröffentlichen des Themes nachholen (Punkt für die Launch-Checkliste). Bis dahin rendern die Seiten im Standard-Template, das ebenfalls im Theme-Design ist.
5. Sichtbarkeit: Sichtbar.

| Titel | URL-Handle | Template | Inhalt aus |
|---|---|---|---|
| Hilfe | `hilfe` | `hilfe` | `hilfe.md` |
| FAQ | `faq` | `faq` | `faq.md` (Fragen selbst stehen im Template) |
| Kontakt | `kontakt` | `kontakt` | `kontakt.md` |
| Versand | `versand` | `versand` | `versand.md` |
| Rückgabe | `rueckgabe` ⚠ | `versand` | `rueckgabe.md` |
| Versand & Rückgabe | `versand-kurz` ⚠ | Standard | `versand-kurz.md` |
| Zahlungsarten | `zahlungsarten` | `zahlungsarten` | `zahlungsarten.md` |
| Über uns | `ueber-uns` ⚠ | `ueber-uns` | `ueber-uns.md` |

⚠ = Shopify schlägt einen anderen Handle vor (`ruckgabe`, `versand-ruckgabe`, `uber-uns`). Von Hand korrigieren, sonst greifen die Links im Theme nicht. FAQ: Titel „FAQ“, nicht „FAQs“.

Das frühere Template „contact“ gibt es nicht mehr; es heißt jetzt „kontakt“.

### Richtlinien

**Einstellungen → Richtlinien.** Impressum, Datenschutzerklärung, AGB, Widerrufsbelehrung und Versandrichtlinie kommen **vom Rechtsdienstleister** — nicht selbst formulieren, nichts umschreiben. Dem Dienstleister Dropshipping-Modell und Lagerländer mitteilen. Nach jedem Einfügen die Seite im Browser öffnen und nach `[` suchen.

Solange die Richtlinien leer sind, fehlen im Footer die Rechtslinks, und der Steuerhinweis am Preis verlinkt nicht auf den Versand. Im Theme-Editor steht dann ein Marker.

---

## 6. Search & Discovery: Filter und Sortierung

1. **Apps → „Shopify Search & Discovery“** suchen und installieren (kostenlos, von Shopify).
2. App öffnen → **Filter** → vorhandene Filter prüfen, fehlende mit **Filter hinzufügen**. Reihenfolge per Drag & Drop **genau so**:

| # | Filter | Quelle | Anzeigename |
|---|---|---|---|
| 1 | Verfügbarkeit | Standard | Verfügbarkeit |
| 2 | Preis | Standard | Preis |
| 3 | Farbe | Variantenoption „Farbe“ (bzw. Kategorie-Metafeld Farbe, wenn verknüpft) | Farbe |
| 4 | Bauart | Produkttyp | Bauart |
| 5 | Material | Metafeld `custom.material` | Material |
| 6 | Dimmbar | Metafeld `custom.dimmbar` | Dimmbar |
| 7 | Farbtemperatur | Metafeld `custom.farbtemperatur` | Farbtemperatur (K) |
| 8 | IP-Schutzart | Metafeld `custom.ip_schutzart` | IP-Schutzart |
| 9 | Energieeffizienzklasse | Metafeld `custom.energieeffizienzklasse` | Energieeffizienzklasse |

3. Filter 5–9 zeigt Shopify im Shop erst an, wenn mindestens ein Produkt der Collection einen Wert hat. Mit den Muster-Produkten (Metafelder leer) sind also nur 1–4 sichtbar — das ist richtig so.
4. **Suche → Produktempfehlungen:** „Verwandte Produkte“ automatisch lassen. Sie speisen den Abschnitt „Passt dazu“ auf der Produktseite.

---

## 7. Theme-Editor: Bilder und offene Einstellungen

**Onlineshop → Themes → Entwurf → Anpassen.**

| Wo | Was |
|---|---|
| Startseite → Hero | „Bild 1“ (16:9, Slot `hero-desktop`) und unter „Benutzerdefinierte mobile Medien“ das Mobilbild (4:5, Slot `hero-mobil`). Danach Lesbarkeit der Überschrift prüfen. |
| Startseite → Marke | Bild im Block „Medien“ (4:5, Slot `marke`). Text ist Marker, bis der Markentext feststeht. |
| Startseite → Kacheln | Brauchen keine Zuweisung; sie zeigen die Collection-Bilder aus Schritt 3. Prüfen, dass alle 3 + 7 Kacheln erscheinen — fehlt eine, stimmt ein Collection-Handle nicht. |
| Header → Logo | Theme-Einstellungen → Logo. Ohne Logo steht der Shopname als Text. |
| Header → Mega-Menü | „Innenleuchten“ überfahren: links Unterkategorien, rechts das Bild der Collection. |
| Produktseite → Accordion „Versand & Rückgabe“ | Block öffnen → Seite „Versand & Rückgabe“ (`versand-kurz`) wählen, falls nicht vorbelegt. |
| Seite Kontakt → Block „Kontaktdaten“ | Support-E-Mail und Reaktionszeit eintragen, sobald entschieden. |
| Theme-Einstellungen → Suche | Optional „Collection für leeren Zustand“ = Neu. |
| Ankündigungsleiste | Bleibt deaktiviert, bis es eine echte, entschiedene Aussage gibt. |

Die gelben Marker „[[…]]“ im Editor sind Absicht: Sie zeigen fehlende Pflichtdaten und erscheinen im Shop nicht (Ausnahme: Marker, die als normaler Text in Templates stehen, etwa der Markentext — die sind auch in der Vorschau sichtbar, damit sie nicht übersehen werden).

---

## 8. Blog „Ratgeber“ anlegen

**Onlineshop → Blogbeiträge → Blogs verwalten → Blog hinzufügen.** Titel „Ratgeber“, Handle `ratgeber` kontrollieren. Vorerst leer lassen.

Solange der Blog leer ist, blendet die Startseite den Ratgeber-Teaser aus, und die Footer-Spalte „Ratgeber“ erscheint nicht (solange das Menü `footer-ratgeber` fehlt). Geplante Themen: Lichtfarbe und Kelvin · Lumen pro Raum · IP-Schutzarten im Außenbereich. Beitragsbilder im Format 16:9.

---

## 9. Sprachen: Deutsch und Englisch

Das Theme ist zweisprachig vorbereitet: Alle festen Theme-Texte liegen in `locales/de.json` und `locales/en.default.json`, der Sprachumschalter im Header erscheint automatisch, sobald zwei Sprachen veröffentlicht sind.

1. **Einstellungen → Sprachen.** Standardsprache muss **Deutsch** sein. → **Sprache hinzufügen → Englisch**.
2. **Einstellungen → Markets** → Markt Deutschland → Sprachen: Englisch aktivieren. Englisch läuft dann unter `/en`.
3. **App „Translate & Adapt“** (kostenlos, von Shopify) installieren. Dort Englisch wählen und übersetzen:

| Bereich in Translate & Adapt | Was |
|---|---|
| Produkte | Titel, Beschreibung, Optionsname „Farbe“ → „Colour“, Farbwerte |
| Collections | Titel, Beschreibung |
| Metafelder | alle sichtbaren Textfelder (Sockel, Material, Maße, Lieferzeit, Kurzbeschreibung, Lieferumfang …) |
| Navigation | alle Menüeinträge |
| Seiten | Titel und Inhalt — Vorlagen in `content/seiten/en/` |
| Theme → Templates | Überschriften und Texte der Startseite, FAQ-Zeilen, Accordion-Titel der Produktseite, Footer-Überschriften |
| Richtlinien | englische Fassung **vom Rechtsdienstleister** |
| Benachrichtigungen | Bestellbestätigung usw. auf Englisch |

4. Englisch erst **veröffentlichen**, wenn die Übersetzung vollständig ist. Unübersetzte Stellen zeigen sonst Deutsch.

Eigene Theme-Texte ändern: `tools/lamp-strings.json` bearbeiten und `python3 tools/locales.py` ausführen — nicht direkt in den Sprachdateien.

Mit dem Rechtsdienstleister zu klären: ob englische Rechtstexte bereitgestellt werden und welche Fassung maßgeblich ist; ob mit der englischen Sprachfassung Verkauf an Kunden außerhalb Deutschlands verbunden ist (das berührt Versand, Steuern und Verbraucherrecht und ist bisher nicht entschieden — Zielmarkt laut `CLAUDE.md` ist Deutschland).

---

## 10. Kontrolle in der Vorschau

Theme-Entwurf → **Vorschau**. Desktop (1440) und mobil (375):

- Startseite: alle Sections in Reihenfolge, Kacheln mit Bildern, keine leeren Raster.
- Collection Innenleuchten: 12 Karten, Pills, Filter links, Sortierung, mobil Filter-Drawer mit „X Produkte anzeigen“.
- Produktseite: Thumbnails, Farbwechsel wechselt das Bild, ausverkaufte Variante sichtbar, mobil Sticky-Leiste.
- Warenkorb-Drawer, Suche (Vorschau mit Bild und Preis), Menü-Drawer mobil.
- Footer: Rechtslinks direkt sichtbar, Zahlungsarten-Icons.
- Sprachumschalter: `/en` zeigt englische Theme-Texte.

---

## 11. Aufräumen vor dem Launch

1. **Produkte** → Filter „Getaggt mit: `platzhalter`“ → alle markieren → **Produkte löschen**. Es dürfen danach keine Produkte mit „Muster“ im Titel übrig sein.
2. **Inhalte → Dateien:** alle Stockfotos löschen (Hero, Marke, Kategoriebilder) und durch eigene Bilder ersetzen. Collection-Bilder austauschen.
3. Im Shop und in `content/seiten/` nach `[` suchen: Jeder Marker `[[…]]` muss durch eine entschiedene Aussage ersetzt oder entfernt sein — Startseite (Markentext), FAQ, Footer (Newsletter-Hinweis), alle Seiten.
4. Jedes echte Produkt: Checkliste `CLAUDE.md` 4.2 vollständig, alle Pflicht-Metafelder gefüllt (im Theme-Editor darf auf der Produktseite kein gelber Marker mehr stehen).
5. Konsistenztabelle aus `CLAUDE.md` Abschnitt 12 durchgehen (Lieferzeit, Rücksendekosten, Rücksendeadresse, Steuerhinweis, Firmendaten, Energieklasse).
6. Pro Lieferant eine Testbestellung komplett durchspielen.
7. Veröffentlichen erst nach ausdrücklicher Freigabe.
