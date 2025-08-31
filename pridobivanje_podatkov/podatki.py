import csv
import time

from bs4 import BeautifulSoup
import cloudscraper
# import requests

# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
# }
# seja = requests.Session()
# odziv = requests.get("https://www.basketball-reference.com/leagues/NBA_2000_per_game.html")
# print(odziv.status_code)
# print(odziv.text)

scraper = cloudscraper.create_scraper()
scraper.encoding = "utf-8"

podatki_vseh_let = []
for leto in range(2000, 2025):

    odziv = scraper.get(f"https://www.basketball-reference.com/leagues/NBA_{leto}_per_game.html")
    print(odziv.status_code, leto)
    # print(odziv.text)


    soup = BeautifulSoup(odziv.content.decode("utf-8"), 'html.parser')
    tabela = soup.find("table")
    glava = tabela.find("thead")
    glavna_vrstica = glava.find("tr")
    celice_v_glavi = glavna_vrstica.find_all("th")


    imena_stolpcev = []
    
    for celica in celice_v_glavi:
        imena_stolpcev.append(celica.text)
    imena_stolpcev.append("Year")  # v tabelo dodam stolpec leto


    # print(imena_stolpcev)

    telo = tabela.find("tbody")
    vrstice = telo.find_all("tr")

    podatki_vseh_vrstic = []

    for vrstica in vrstice:
        podatki_vrstice = []
        rank = vrstica.find("th")
        celice = vrstica.find_all("td")
        podatki_vrstice.append(rank.text)
        for celica in celice:
            podatek = celica.text
            podatki_vrstice.append(podatek)
        podatki_vrstice.append(leto)    # v vsako vrstico dodam leto
        podatki_vseh_vrstic.append(podatki_vrstice)
    podatki_vseh_vrstic = podatki_vseh_vrstic[:-1]   # odstranim zadnjo vrstico, potem ko končam z vsemi vrsticami
    podatki_vseh_let.extend(podatki_vseh_vrstic)
        

    # print(podatki_vseh_vrstic)

    time.sleep(2)   # program spi dve sekundi, da ne pošiljamo preveć zahtev na enkrat

with open("pridobivanje_podatkov/podatki.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(imena_stolpcev)
    writer.writerows(podatki_vseh_let)