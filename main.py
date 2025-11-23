from dao.mysql_dao import MySQLDAO
from models.produit import Produit
from models.client import Client

dao = MySQLDAO()

while True:
    print("\n1. Ajouter produit")
    print("2. Ajouter client")
    print("3. Lister produits")
    print("4. Lister clients")
    print("5. Rechercher client par email")
    print("6. Modifier prix produit")
    print("7. Quitter")

    choix = input("Choix : ")

    if choix == "1":
        p = Produit(int(input("ID : ")), input("Nom : "), float(input("Prix : ")))
        dao.ajouter_produit(p)

    elif choix == "2":
        c = Client(int(input("ID : ")), input("Nom : "), input("Email : "))
        dao.ajouter_client(c)

    elif choix == "3":
        for p in dao.lister_produits():
            print(p)

    elif choix == "4":
        for c in dao.lister_clients():
            print(c)

    elif choix == "5":
        email = input("Email : ")
        client = dao.rechercher_client_email(email)
        print(client if client else "Aucun client trouvé")

    elif choix == "6":
        dao.modifier_prix(int(input("ID : ")), float(input("Nouveau prix : ")))

    elif choix == "7":
        break
