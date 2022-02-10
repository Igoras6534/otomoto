import sqlite3
from bs4 import BeautifulSoup
from requests import get
class Database:
    def __init__(self,data_name):
        self.conn=sqlite3.connect(data_name)
        self.cursor=self.conn.cursor()
    def __del__(self):
        self.conn.close()
    def setup(self,sql):
        self.cursor.execute(sql)
        self.conn.commit()
    def parse_page(self,table:str,url:str):
        page = get(url)
        bs = BeautifulSoup(page.content, "html.parser")
        for offer in bs.find_all("div", class_="offer-wrapper"):
            footer = offer.find("td", class_="bottom-cell")
            location = footer.find("small", class_="breadcrumb x-normal").get_text().strip().split(",")[0]
            ogloszenie = offer.find("strong").get_text().strip()
            marka = offer.find("small", class_="breadcrumb x-normal").get_text().strip().split(" ")[3].upper()
            price =(offer.find("p", class_="price").get_text().strip().replace(" ", "").replace("zł", "").replace(",", "."))
            self.cursor.execute(f"INSERT INTO {table} VALUES(?,?,?,?)", (ogloszenie, price, location, marka))
            self.conn.commit()

    def sortowanie(self,table):
        self.cursor.execute(f"SELECT DISTINCT name FROM {table}")
        a = input(f"How do you want to sort your results? 1-by city, 2-by price, 3-by brand or 4-by all: ")
        if a == "1":
            miasto = input("City: ")
            return self.cursor.execute(f"SELECT * FROM {table} WHERE city LIKE (?) ORDER BY price DESC", [miasto])
        elif a == "2":
            c = int(input("Max price: "))
            b = input("How do you want to sort your price? 1-High-Low, 2-Low-High: ")
            if b == "1":
                return self.cursor.execute(f"SELECT * FROM {table} WHERE price<=(?) ORDER BY price DESC ", [c])
            elif b == "2":
                return self.cursor.execute(f"SELECT * FROM {table} WHERE price<=(?) ORDER BY price ASC ", [c])
            else:
                print("Invalid Value")
        elif a == "3":
            marka = input("Brand: ")
            return self.cursor.execute(f"SELECT * FROM {table} WHERE brand LIKE (?) ORDER BY price DESC", [marka])
        elif a == "4":
            miasto = input("City: ")
            cena = int(input("Max price: "))
            marka = input("Brand: ")
            wsio = [miasto, cena, marka]
            return self.cursor.execute(
                f"SELECT * FROM {table} WHERE (city LIKE(?) AND price <= (?) AND brand LIKE(?)) ORDER BY price DESC",
                (wsio))
        else:
            print("Invalid Value")

    def usuwanie(self,table):
        self.cursor.execute(f"DELETE FROM {table}")
        self.conn.commit()
