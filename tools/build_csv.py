#!/usr/bin/env python3
"""Erzeugt data/platzhalter-produkte.csv (Shopify-Produktimport) aus der Liste unten.

Aufruf im Repo-Root:  python3 tools/build_csv.py

Bilder kommen aus data/platzhalter-bilder.csv (Spalten: slot, url, seite, fotograf, quelle, geprueft).
Ein Slot heißt wie der Produkt-Handle plus Farbe, z. B. "muster-pendelleuchte-01--schwarz".
Zeilen ohne URL oder ohne geprueft=ja werden ignoriert – das Produkt wird dann ohne Bild importiert.

Bewusst leer: Energieklasse, EPREL, WEEE, Hersteller, Lieferzeit, technische Daten, Gewicht.
Nichts davon darf für Muster-Produkte erfunden werden (CLAUDE.md Abschnitte 5 und 16).
"""
import csv
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

BODY = (
    '<p>[[Einleitung — 2–3 Sätze]]</p>'
    '<h3>Licht &amp; Wirkung</h3><p>[[Licht &amp; Wirkung — 2–4 Sätze]]</p>'
    '<h3>Material &amp; Verarbeitung</h3><p>[[Material &amp; Verarbeitung — 2–4 Sätze]]</p>'
    '<h3>Einsatz</h3><p>[[Einsatz — 2–3 Sätze]]</p>'
)

# (Titel, Produkttyp, Tags, Preis, [(Farbe, Bestand)])
PRODUCTS = [
    ('Muster Deckenleuchte 01', 'Deckenleuchte', 'innen, decke', 129, [('Weiß', 10), ('Schwarz', 10)]),
    ('Muster Deckenleuchte 02', 'Deckenleuchte', 'innen, decke', 189, [('Messing', 10), ('Schwarz', 10), ('Weiß', 10)]),
    ('Muster Pendelleuchte 01', 'Pendelleuchte', 'innen, pendel', 149, [('Schwarz', 10), ('Sand', 10), ('Salbei', 10)]),
    ('Muster Pendelleuchte 02', 'Pendelleuchte', 'innen, pendel', 249, [('Messing', 10), ('Schwarz', 10)]),
    ('Muster Wandleuchte 01', 'Wandleuchte', 'innen, wand', 89, [('Weiß', 10), ('Schwarz', 0)]),
    ('Muster Stehleuchte 01', 'Stehleuchte', 'innen, steh', 279, [('Schwarz', 10), ('Messing', 10)]),
    ('Muster Stehleuchte 02', 'Stehleuchte', 'innen, steh', 349, [('Sand', 10), ('Anthrazit', 10)]),
    ('Muster Tischleuchte 01', 'Tischleuchte', 'innen, tisch', 99, [('Sand', 10), ('Salbei', 10), ('Schwarz', 10)]),
    ('Muster Außen-Wandleuchte 01', 'Außen-Wandleuchte', 'aussen, wand', 119, [('Anthrazit', 10), ('Weiß', 10)]),
    ('Muster Außen-Wandleuchte 02', 'Außen-Wandleuchte', 'aussen, wand', 159, [('Schwarz', 10), ('Messing', 10)]),
    ('Muster Außen-Wandleuchte 03', 'Außen-Wandleuchte', 'aussen, wand', 79, [('Anthrazit', 10), ('Schwarz', 10)]),
    ('Muster Wegeleuchte 01', 'Wegeleuchte', 'aussen, weg', 139, [('Anthrazit', 10), ('Schwarz', 10)]),
    ('Muster Wegeleuchte 02', 'Wegeleuchte', 'aussen, weg', 199, [('Schwarz', 0), ('Anthrazit', 0)]),
    ('Muster Außen-Tischleuchte 01', 'Außen-Tischleuchte', 'aussen, tisch', 69, [('Sand', 10), ('Anthrazit', 10), ('Salbei', 10)]),
    ('Muster Schreibtischleuchte 01', 'Schreibtischleuchte', 'innen, schreibtisch', 79, [('Schwarz', 10), ('Weiß', 10)]),
    ('Muster Schreibtischleuchte 02', 'Schreibtischleuchte', 'innen, schreibtisch', 119, [('Messing', 10), ('Schwarz', 10)]),
    ('Muster Schreibtischleuchte 03', 'Schreibtischleuchte', 'innen, schreibtisch', 149, [('Anthrazit', 10), ('Salbei', 10), ('Sand', 10)]),
    ('Muster Schreibtischleuchte 04', 'Schreibtischleuchte', 'innen, schreibtisch', 59, [('Weiß', 10), ('Schwarz', 10)]),
]

COLUMNS = [
    'Handle', 'Title', 'Body (HTML)', 'Vendor', 'Product Category', 'Type', 'Tags', 'Published',
    'Option1 Name', 'Option1 Value', 'Option2 Name', 'Option2 Value', 'Option3 Name', 'Option3 Value',
    'Variant SKU', 'Variant Grams', 'Variant Inventory Tracker', 'Variant Inventory Qty',
    'Variant Inventory Policy', 'Variant Fulfillment Service', 'Variant Price', 'Variant Compare At Price',
    'Variant Requires Shipping', 'Variant Taxable', 'Variant Barcode', 'Image Src', 'Image Position',
    'Image Alt Text', 'Gift Card', 'SEO Title', 'SEO Description', 'Variant Image', 'Variant Weight Unit',
    'Cost per item', 'Status',
]


def slug(text):
    for a, b in (('ä', 'ae'), ('ö', 'oe'), ('ü', 'ue'), ('ß', 'ss')):
        text = text.lower().replace(a, b)
    return '-'.join(text.replace('-', ' ').split())


def load_images():
    path = os.path.join(ROOT, 'data', 'platzhalter-bilder.csv')
    images = {}
    if os.path.exists(path):
        for row in csv.DictReader(open(path, encoding='utf-8')):
            if row.get('url', '').strip() and row.get('geprueft', '').strip().lower() == 'ja':
                images[row['slot'].strip()] = row['url'].strip()
    return images


def main():
    images = load_images()
    rows, with_image, total = [], 0, 0
    for title, ptype, tags, price, variants in PRODUCTS:
        handle = slug(title)
        for index, (color, qty) in enumerate(variants):
            total += 1
            row = dict.fromkeys(COLUMNS, '')
            row['Handle'] = handle
            if index == 0:
                row.update({
                    'Title': title, 'Body (HTML)': BODY, 'Type': ptype,
                    'Tags': 'platzhalter, ' + tags, 'Published': 'TRUE',
                    'Option1 Name': 'Farbe', 'Gift Card': 'FALSE', 'Status': 'active',
                })
            url = images.get(handle + '--' + slug(color), '')
            if url:
                with_image += 1
            row.update({
                'Option1 Value': color,
                'Variant SKU': 'MUSTER-' + handle.replace('muster-', '').upper() + '-' + slug(color).upper(),
                'Variant Inventory Tracker': 'shopify', 'Variant Inventory Qty': qty,
                'Variant Inventory Policy': 'deny', 'Variant Fulfillment Service': 'manual',
                'Variant Price': '%d.00' % price, 'Variant Requires Shipping': 'TRUE', 'Variant Taxable': 'TRUE',
                'Image Src': url, 'Image Position': index + 1 if url else '',
                'Image Alt Text': '%s, %s (Platzhalterbild)' % (title, color) if url else '',
                'Variant Image': url,
            })
            rows.append(row)
    out = os.path.join(ROOT, 'data', 'platzhalter-produkte.csv')
    with open(out, 'w', encoding='utf-8', newline='') as fh:
        writer = csv.DictWriter(fh, fieldnames=COLUMNS)
        writer.writeheader()
        writer.writerows(rows)
    print('%d Produkte, %d Varianten, %d davon mit Bild -> %s' % (len(PRODUCTS), total, with_image, out))


if __name__ == '__main__':
    main()
