# Bildquellen

**Stand: Es sind noch keine Stockfotos ausgewählt.** In `data/platzhalter-produkte.csv` stehen deshalb keine Bild-URLs; die Muster-Produkte werden ohne Bild importiert und zeigen im Raster eine Sand-Fläche mit dem Produktnamen.

## Warum

Die Vorgabe lautet: nur Bild-URLs verwenden, die tatsächlich aufgerufen und geprüft wurden, mit Quelle und Fotograf pro Bild. Das war in der Bausitzung nicht möglich:

- `unsplash.com` antwortet auf automatisierte Abrufe mit einer Bot-Prüfseite (HTTP 401).
- `www.pexels.com` antwortet mit HTTP 403.
- Die offiziellen Schnittstellen beider Dienste brauchen einen persönlichen API-Schlüssel.

Bot-Sperren wurden nicht umgangen, und es wurden keine URLs aus dem Gedächtnis eingesetzt — ungeprüfte URLs können ins Leere zeigen oder ein anderes Motiv und einen anderen Urheber haben als angenommen.

## So kommen die Bilder rein

Alle benötigten Bilder stehen als Zeilen in `data/platzhalter-bilder.csv` (56 Slots: Hero, Marke, 12 Kategorien, 41 Produktvarianten).

**Weg A — von Hand (ca. 30–45 Minuten)**

1. Auf unsplash.com oder pexels.com passende Fotos suchen (Suchbegriffe unten).
2. Pro Slot in `data/platzhalter-bilder.csv` eintragen:
   - `url` — direkte Bild-URL (`https://images.unsplash.com/photo-…` bzw. `https://images.pexels.com/photos/…`), am besten mit `?w=2000&q=80` am Ende
   - `seite` — Adresse der Fotoseite
   - `fotograf` — Name wie auf der Fotoseite angegeben
   - `quelle` — `Unsplash` oder `Pexels`
   - `geprueft` — `ja`, sobald die URL im Browser geöffnet wurde und das Motiv passt
3. `python3 tools/build_csv.py` ausführen. Nur Zeilen mit `geprueft = ja` landen in der Produkt-CSV.
4. Die Tabelle unten in diesem Dokument aus der CSV ergänzen.

**Weg B — über die offizielle API**

Mit einem kostenlosen API-Schlüssel (Unsplash Developers oder Pexels API) kann Claude Code die Suche, Prüfung und Dokumentation übernehmen. Dafür in einer neuen Sitzung den Schlüssel über das sichere Formular hinterlegen lassen (nicht in den Chat schreiben) und `api.unsplash.com` bzw. `api.pexels.com` in der Umgebung „lampenshop“ erlauben.

## Auswahlkriterien

Die Stockfotos sollen das Raster realistisch füllen, nicht verkaufen.

- Hintergrund ruhig und hell, möglichst neutral (Wand, Studio), kein starker Farbstich.
- Leuchte vollständig im Bild, Hochformat, zum Zuschnitt 4:5 geeignet.
- Keine erkennbaren Marken, Logos oder Personen.
- Pro Produkt je Farbe ein Bild. Wenn es dieselbe Leuchte nicht in mehreren Farben gibt: pro Farbe ein anderes Foto derselben Bauart nehmen — es geht um den Bildwechsel im Layout, nicht um Produktwahrheit.
- Hero und Marke: Raumszene in warmem Licht, viel ruhige Fläche auf der linken unteren Seite für die Überschrift.

Suchbegriffe: `pendant lamp minimal`, `ceiling lamp`, `wall sconce`, `floor lamp interior`, `table lamp`, `desk lamp`, `outdoor wall light`, `garden path light`, `outdoor lantern table`, `scandinavian living room lamp`.

## Lizenz

Unsplash- und Pexels-Fotos dürfen nach den jeweiligen Lizenzbedingungen kostenlos kommerziell genutzt werden; eine Namensnennung ist nicht vorgeschrieben, wird hier aber dokumentiert. Fotos aus den Bezahlbereichen („Unsplash+“) sind ausgenommen. Die Lizenzseiten vor der Nutzung selbst lesen — dieser Absatz ist keine Rechtsauskunft.

## Nur Platzhalter

Diese Fotos zeigen nicht die später verkauften Leuchten. Vor dem Launch werden alle Muster-Produkte gelöscht und alle Stockfotos ersetzt — auch Hero, Marke und Kategoriebilder (`CLAUDE.md` Abschnitte 8 und 16). Ein Stockfoto darf nie an einem echten Produkt hängen.

## Verwendete Bilder

| Slot | Quelle | Fotograf | Fotoseite | Geprüft am |
|---|---|---|---|---|
| — noch keine — | | | | |
