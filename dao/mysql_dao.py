import mysql.connector
from models.produit import Produit
from models.client import Client

class MySQLDAO:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="boutique"
        )
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS produit(id INT PRIMARY KEY, nom VARCHAR(255), prix DOUBLE)")
        self.cur.execute("CREATE TABLE IF NOT EXISTS client(id INT PRIMARY KEY, nom VARCHAR(255), email VARCHAR(255))")
        self.conn.commit()

    def ajouter_produit(self, produit):
        self.cur.execute("INSERT INTO produit VALUES (%s, %s, %s)", (produit.id, produit.nom, produit.prix))
        self.conn.commit()

    def ajouter_client(self, client):
        self.cur.execute("INSERT INTO client VALUES (%s, %s, %s)", (client.id, client.nom, client.email))
        self.conn.commit()

    def lister_produits(self):
        self.cur.execute("SELECT * FROM produit")
        return [Produit(*row) for row in self.cur.fetchall()]

    def lister_clients(self):
        self.cur.execute("SELECT * FROM client")
        return [Client(*row) for row in self.cur.fetchall()]

    def rechercher_client_email(self, email):
        self.cur.execute("SELECT * FROM client WHERE email=%s", (email,))
        row = self.cur.fetchone()
        return Client(*row) if row else None

    def modifier_prix(self, id, prix):
        self.cur.execute("UPDATE produit SET prix=%s WHERE id=%s", (prix, id))
        self.conn.commit()
