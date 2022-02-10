from klasa import Database
from terminaltables import AsciiTable
def dodaj():
    dicto = {1: "https://www.olx.pl/motoryzacja/samochody/",
             2: "https://www.olx.pl/motoryzacja/samochody/?page=2",
             3: "https://www.olx.pl/motoryzacja/samochody/?page=3",
             4: "https://www.olx.pl/motoryzacja/samochody/?page=4",
             5: "https://www.olx.pl/motoryzacja/samochody/?page=5",
             6: "https://www.olx.pl/motoryzacja/samochody/?page=6",
             7: "https://www.olx.pl/motoryzacja/samochody/?page=7",
             8: "https://www.olx.pl/motoryzacja/samochody/?page=8",
             9: "https://www.olx.pl/motoryzacja/samochody/?page=9",
             10: "https://www.olx.pl/motoryzacja/samochody/?page=10",
             11: "https://www.olx.pl/motoryzacja/samochody/?page=11",
             12: "https://www.olx.pl/motoryzacja/samochody/?page=12",
             13: "https://www.olx.pl/motoryzacja/samochody/?page=13",
             14: "https://www.olx.pl/motoryzacja/samochody/?page=14",
             15: "https://www.olx.pl/motoryzacja/samochody/?page=15",
             16: "https://www.olx.pl/motoryzacja/samochody/?page=16",
             17: "https://www.olx.pl/motoryzacja/samochody/?page=17",
             18: "https://www.olx.pl/motoryzacja/samochody/?page=18",
             19: "https://www.olx.pl/motoryzacja/samochody/?page=19",
             20: "https://www.olx.pl/motoryzacja/samochody/?page=20",
             21: "https://www.olx.pl/motoryzacja/samochody/?page=21",
             22: "https://www.olx.pl/motoryzacja/samochody/?page=22",
             23: "https://www.olx.pl/motoryzacja/samochody/?page=23",
             24: "https://www.olx.pl/motoryzacja/samochody/?page=24",
             25: "https://www.olx.pl/motoryzacja/samochody/?page=25",
             26: "https://www.olx.pl/motoryzacja/samochody/?page=26",

             }
    x = Database("dane1.db")
    i = 1
    while True:
        x.parse_page("oferta", dicto[i])
        i = i + 1
        if i == 26:
            break

def szukaj():
    x= Database("dane1.db")
    lista = [["Ogłoszenie", "Cena", "Miasto", "Marka"]]
    for z in x.sortowanie("oferta"):
        lista.append(z)
    pokaz = AsciiTable(lista)
    print(pokaz.table)