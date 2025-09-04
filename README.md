# Projektna naloga - UVP

## Analiza igralcev lige NBA glede na posamično igro

Avtorica: Neža Zupančič

avgust 2025


### Uvod

Glavno področje moje analize je bilo deset najboljših igralcev lige NBA. Zajela sem podatke iz spletne strani Basketball reference, avgusta 2025. Podatki zajemajo 25 sezon in so sezonska povprečja igralcev.

Osredotočila sem se na:
- Ali se je povprečje doseženih točk vseh igralcev v zadnjih 25-ih letih povečalo?
- Kateri so najboljši strelci? Katere pozicije prevladujejo med top deset strelci v vseh sezonah in iz katerih ekip prihajajo?

Analizirala sem tudi povprečno starost med najboljšimi desetimi igralci in igralci vseh sezon. Zanimalo me je tudi kako so igralci učinkoviti glede na minuto svoje igre in kateri so pri tem najboljši.

### Navodila za uporabo

Za uspešen zagon analize so potrebne naslednje knjižnice: beautifulsoup, pandas, requests, csv in matplotlib.pyplot.
Celotna analiza se nahaja v datoteki z imenom 'analiza_podatkov.ipynb'.

### Datoteke
- 'podatki.py' prenese podatke o igralcih lige NBA, ki zajemajo povprečne sezonske podatke zadnjih 25 let, s spletne strani v obliki HTML. Podatke nato obdela, pretvori in shrani in jih pretvori ter shrani v datoteko 'podatki.csv'.
- 'analiza_podatkov.ipynb' vsebuje zaključno analizo pridobljenih podatkov dopolnjeno z grafi in histogrami.
