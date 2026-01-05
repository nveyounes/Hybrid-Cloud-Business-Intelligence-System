import json
import csv
import random
import os

# Create dummy data
os.makedirs("input_data", exist_ok=True)

# 1. Products (CSV)
products = [
    [3001, "Smartphone XYZ", "Electronique", 22.99],
    [3002, "Televiseur HD", "Electronique", 99.99],
    [3003, "Chaise ergonomique", "Meubles", 50.00],
    [3004, "Livre de programmation", "Education", 15.99],
    [3005, "Casque audio", "Electronique", 35.00]
]
with open('input_data/produits.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["ProduitID", "NomProduit", "Categorie", "Prix"])
    writer.writerows(products)

# 2. Orders (JSON)
orders = []
statuses = ["Validee", "Annulee", "En attente"]
for i in range(1001, 1021):
    orders.append({
        "CommandeID": i,
        "ClientID": random.choice([2001, 2002, 2003]),
        "ProduitID": random.choice([3001, 3002, 3003, 3004, 3005]),
        "Quantite": random.randint(1, 3),
        "DateCommande": "2024-09-30",
        "Statut": random.choice(statuses)
    })
with open('input_data/commandes.json', 'w') as f:
    json.dump(orders, f, indent=4)

# 3. SQL Script for Clients
sql_stmt = """
CREATE TABLE IF NOT EXISTS clients (
    ClientID INT PRIMARY KEY,
    NomClient VARCHAR(255),
    Pays VARCHAR(50),
    DateInscription DATE
);
TRUNCATE TABLE clients;
INSERT INTO clients (ClientID, NomClient, Pays, DateInscription) VALUES
(2001, 'John Doe', 'France', '2023-05-10'),
(2002, 'Jane Smith', 'USA', '2023-06-15'),
(2003, 'Carlos Garcia', 'Espagne', '2023-07-20');
"""
with open('input_data/init_clients.sql', 'w') as f:
    f.write(sql_stmt)

print("✅ Data generated in 'input_data' folder.")