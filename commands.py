from repositories.we_flask import dodaj,szukaj
from klasa import Database

import click
@click.group()
def cli():
    pass
@click.command()
def setup():
    db = Database("dane1.db")
    db.setup("CREATE TABLE oferta (name TEXT, price REAL, city TEXT,brand TEXT)")
    quit()
@click.command()
def add():
    dodaj()
@click.command()
def search():
    szukaj()
@click.command()
def delete():
    x=Database("dane1.db")
    x.usuwanie("oferta")