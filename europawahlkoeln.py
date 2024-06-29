#!/usr/bin/env python
# coding: utf-8
import streamlit as st
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

import locale
locale.setlocale(locale.LC_ALL, "de_DE")
pd.options.display.float_format = '{:n}'.format

font = {'fontname':'Inter'}

# Wahldaten einlesen
daten = pd.read_csv("https://wahlen.stadt-koeln.de/prod/EUW2024/05315000/daten/opendata/Open-Data-05315000-Wahl-zum-10.-Europaeischen-Parlament-Stadtteil.csv", sep = ";")
# daten = pd.read_csv("https://wahlen.regioit.de/1/eu2024/05334000/daten/opendata/Open-Data-05334000-Europawahl-Gemeinde.csv?ts=1719565670005", sep = ";")
# daten = pd.read_csv("https://wahlen.regioit.de/1/eu2024/05334002/daten/opendata/Open-Data-05334002-Europawahl-Stadtbezirk.csv?ts=1719566093086", sep = ";")

# Spalten mit absoluten Stimmen umbenennen
mapping = {"D1": "CDU Stimmen", "D2": "Grüne Stimmen", "D3": "SPD Stimmen", "D4" : "AfD Stimmen", "D5" : "FDP Stimmen", "D6" : "Linke Stimmen", "D7" : "Die PARTEI Stimmen", "D8" : "Tierschutz Stimmen", "D9" : "Piraten Stimmen", "D10" : "Volt Stimmen", "D11" : "Familie Stimmen", "D12" : "Freie Wähler Stimmen", "D13" : "ÖDP Stimmen", "D14" : "BIG Stimmen", "D15" : "Mera25 Stimmen", "D16" : "Tierschutz hier Stimmen", "D17" : "PdH Stimmen", "D18" : "Heimat Stimmen", "D19" : "Bündnis C Stimmen", "D20" : "Verjüngungsforschung Stimmen", "D21" : "Menschliche Welt Stimmen", "D22" : "MLPD Stimmen", "D23" : "DKP Stimmen", "D24" : "SGP Stimmen", "D25" : "ABG Stimmen", "D26" : "dieBasis Stimmen", "D27" : "Bündnis D Stimmen", "D28" : "BSW Stimmen", "D29" : "DAVA Stimmen", "D30" : "Klimaliste Stimmen", "D31" : "Letzte Gen. Stimmen", "D32" : "PDV Stimmen", "D33" : "PdF Stimmen", "D34" : "V-Partei Stimmen"}
daten = daten.rename(columns = mapping)

# Spalten mit Prozentangaben der Stimmen anlegen und errechnen
daten["CDU"] = round(daten["CDU Stimmen"] / daten["D"]  * 100, 2) # D1
daten["Grüne"] = round(daten["Grüne Stimmen"] / daten["D"]  * 100, 2) # D2
daten["SPD"] = round(daten["SPD Stimmen"] / daten["D"]  * 100, 2) # D3
daten["AfD"] = round(daten["AfD Stimmen"] / daten["D"]  * 100, 2) # D4
daten["FDP"] = round(daten["FDP Stimmen"] / daten["D"]  * 100, 2) # D5
daten["Linke"] = round(daten["Linke Stimmen"] / daten["D"]  * 100, 2) # D6
daten["Die PARTEI"] = round(daten["Die PARTEI Stimmen"] / daten["D"]  * 100, 2) # D7
daten["Tierschutz"] = round(daten["Tierschutz Stimmen"] / daten["D"]  * 100, 2) # D8
daten["Piraten"] = round(daten["Piraten Stimmen"] / daten["D"]  * 100, 2) # D9
daten["Volt"] = round(daten["Volt Stimmen"] / daten["D"]  * 100, 2) # D10
daten["Familie"] = round(daten["Familie Stimmen"] / daten["D"]  * 100, 2) # D11
daten["Freie Wähler"] = round(daten["Freie Wähler Stimmen"] / daten["D"]  * 100, 2) # D12
daten["ÖDP"] = round(daten["ÖDP Stimmen"] / daten["D"]  * 100, 2) # D13
daten["BIG"] = round(daten["BIG Stimmen"] / daten["D"]  * 100, 2) # D14
daten["Mera25"] = round(daten["Mera25 Stimmen"] / daten["D"]  * 100, 2) # D15
daten["Tierschutz hier"] = round(daten["Tierschutz hier Stimmen"] / daten["D"]  * 100, 2) # D16
daten["PdH"] = round(daten["PdH Stimmen"] / daten["D"]  * 100, 2) # D17
daten["Heimat"] = round(daten["Heimat Stimmen"] / daten["D"]  * 100, 2) # D18
daten["Bündnis C"] = round(daten["Bündnis C Stimmen"] / daten["D"]  * 100, 2) # D19
daten["Verjüngungsforschung"] = round(daten["Verjüngungsforschung Stimmen"] / daten["D"]  * 100, 2) # D20
daten["Menschliche Welt"] = round(daten["Menschliche Welt Stimmen"] / daten["D"]  * 100, 2) # D21
daten["MLPD"] = round(daten["MLPD Stimmen"] / daten["D"]  * 100, 2) # D22
daten["DKP"] = round(daten["DKP Stimmen"] / daten["D"]  * 100, 2) # D23
daten["SGP"] = round(daten["SGP Stimmen"] / daten["D"]  * 100, 2) # D24
daten["ABG"] = round(daten["ABG Stimmen"] / daten["D"]  * 100, 2) # D25
daten["dieBasis"] = round(daten["dieBasis Stimmen"] / daten["D"]  * 100, 2) # D26
daten["Bündnis D"] = round(daten["Bündnis D Stimmen"] / daten["D"]  * 100, 2) # D27
daten["BSW"] = round(daten["BSW Stimmen"] / daten["D"]  * 100, 2) # D28
daten["DAVA"] = round(daten["DAVA Stimmen"] / daten["D"]  * 100, 2) # D29
daten["Klimaliste"] = round(daten["Klimaliste Stimmen"] / daten["D"]  * 100, 2) # D30
daten["Letzte Gen."] = round(daten["Letzte Gen. Stimmen"] / daten["D"]  * 100, 2) # D31
daten["PDV"] = round(daten["PDV Stimmen"] / daten["D"]  * 100, 2) # D32
daten["PdF"] = round(daten["PdF Stimmen"] / daten["D"]  * 100, 2) # D33
daten["V-Partei"] = round(daten["V-Partei Stimmen"] / daten["D"]  * 100, 2) # D34

# Zwischenschritt: Kontrollsumme sollte 100 Prozent ergeben (bis auf Rundungen)
daten["Kontrollsumme"] = daten.iloc[:, 49:83].sum(axis=1)

# Zwiwschenberechnung: Prozentsumme der einzelnen angezeigten Parteien
daten["Großparteien"] = daten.iloc[:, 49:55].sum(axis=1) + daten.iloc[:, 58:59].sum(axis=1) # Großparteien: CDU, Grüne, SPD, AfD, FDP, Die Linke, Volt

# Zwischenberechnung: Prozentsumme aller übrigen Parteien
daten["Sonstige"] = daten.iloc[:, 55:58].sum(axis=1) + daten.iloc[:, 59:83].sum(axis=1) # Sonstige: Alle Parteien außer Großparteien

# Tabelle nur mit den Ergebnissen der Sonstigen-Parteien
Sonstige = daten.iloc[:,[4]+list(range(55,58))+list(range(59,83))].set_index("gebiet-name") # Sonstige zur Einzelansicht

# Zweite Kontrollsumme, ob Summe aus einzeln angezeigten Parteien und Sonstigen zusammen auch 100 % eribt (bis auf Rundungseffekte)
daten["Kontrollsumme2"] = daten["Sonstige"] + daten ["Großparteien"]

# Überflüssige Spalten für die Visualisierungen löschen
Spaltenlöschen = {"gebiet-nr", "ags", "wahl", "datum", "max-schnellmeldungen", "anz-schnellmeldungen", "A1", "A2", "A3", "A", "B", "B1", "C", "D", "CDU Stimmen", "Grüne Stimmen", "SPD Stimmen", "AfD Stimmen", "FDP Stimmen", "Linke Stimmen", "Die PARTEI Stimmen", "Tierschutz Stimmen", "Piraten Stimmen", "Volt Stimmen", "Familie Stimmen", "Freie Wähler Stimmen", "ÖDP Stimmen", "BIG Stimmen", "Mera25 Stimmen", "Tierschutz hier Stimmen", "PdH Stimmen", "Heimat Stimmen", "Bündnis C Stimmen", "Verjüngungsforschung Stimmen", "Menschliche Welt Stimmen", "MLPD Stimmen", "DKP Stimmen", "SGP Stimmen", "ABG Stimmen", "dieBasis Stimmen", "Bündnis D Stimmen", "BSW Stimmen", "DAVA Stimmen", "Klimaliste Stimmen", "Letzte Gen. Stimmen", "PDV Stimmen", "PdF Stimmen",	"V-Partei Stimmen", "Die PARTEI", "Tierschutz", "Piraten", "Familie", "Freie Wähler", "ÖDP", "BIG", "Mera25", "Tierschutz hier", "PdH", "Heimat", "Bündnis C", "Verjüngungsforschung", "Menschliche Welt", "MLPD", "DKP", "SGP", "ABG", "dieBasis", "Bündnis D", "BSW", "DAVA", "Klimaliste", "Letzte Gen.", "PDV", "PdF", "V-Partei", "Kontrollsumme", "Großparteien", "Kontrollsumme2"}
daten = daten.drop(Spaltenlöschen, axis=1)

# Daten mit den Stadtteilen indexieren
daten.index = np.arange(1, len(daten) + 1)
daten = daten.set_index('gebiet-name')

# Die Auswahl für die  Gebiete
gebiete = ["Altstadt/Nord", "Altstadt/Süd", "Bayenthal", "Bickendorf", "Bilderstöckchen", "Blumenberg", "Bocklemünd/Mengenich", "Braunsfeld", "Brück", "Buchforst", "Buchheim", "Chorweiler", "Dellbrück", "Deutz", "Dünnwald", "Ehrenfeld", "Eil", "Elsdorf", "Ensen", "Esch/Auweiler", "Finkenberg", "Flittard", "Fühlingen", "Godorf", "Gremberghoven", "Grengel", "Hahnwald", "Heimersdorf", "Höhenberg", "Höhenhaus", "Holweide", "Humboldt/Gremberg", "Immendorf", "Junkersdorf", "Kalk", "Klettenberg", "Langel", "Libur", "Lind", "Lindenthal", "Lindweiler", "Lövenich", "Longerich", "Marienburg", "Mauenheim", "Merheim", "Merkenich", "Meschenich", "Mülheim", "Müngersdorf", "Neubrück", "Neuehrenfeld", "Neustadt/Nord", "Neustadt/Süd", "Niehl", "Nippes", "Ossendorf", "Ostheim", "Pesch", "Poll", "Porz", "Raderberg", "Raderthal", "Rath/Heumar", "Riehl", "Rodenkirchen", "Roggendorf/Thenhoven", "Rondorf", "Seeberg", "Stammheim", "Sülz", "Sürth", "Urbach", "Vingst", "Vogelsang", "Volkhoven/Weiler", "Wahn", "Wahnheide", "Weiden", "Weidenpesch", "Weiß", "Westhoven", "Widdersdorf", "Worringen", "Zollstock", "Zündorf"]

# Ab hier Web-App-Erstellun via Streamlit

# """
# Wahlergebnisse in den Kölner Stadtteilen
#### Schaue dir an, wie Kölnerinnen und Kölner bei der Europawahl am 9. Juni 2024 in deinem Stadtteil gewählt haben
# """

auswahl = st.selectbox("", gebiete, index=0, placeholder="Wähle ein Gebiet aus")

# st.write("Du hast ", auswahl, " ausgewählt.")

# Erzeugen der Daten für das ausgewählte Veedel
getroffeneauswahl = daten.loc[auswahl]

# Basisinfos für das Diagramm
# font = {'fontname': "Segoe UI"}
farben = ['k', 'LimeGreen', 'r', 'MediumBlue', 'Gold', 'DeepPink', 'purple', 'grey']

st.set_option('deprecation.showPyplotGlobalUse', False)

# Erzeugen der Figure und Achsen
fig, ax = plt.subplots(figsize=(5, 5))
bars = ax.bar(getroffeneauswahl.index, getroffeneauswahl.values, color=farben)

# Beschriftungen und Titel setzen
ax.set_xlabel("Wahlergebnis der Parteien", **font)
ax.set_ylabel("Prozent", **font)
ax.set_title("Europawahl, 9. Juni 2024" + ", " + str(auswahl), **font)
ax.tick_params(axis="x", labelsize=9, bottom=False)
ax.tick_params(axis="y", width=1)

# Balkenbeschriftungen hinzufügen
ax.bar_label(ax.containers[0], fmt='{:#.3n}', padding=3, **font)

# Ränder und Hintergrundfarbe setzen
ax.margins(x=0.1, y=0.2)
ax.set_facecolor('whitesmoke')

st.pyplot()

st.html("<p align=right><span>Quelle: Stadt Köln</span></p>")