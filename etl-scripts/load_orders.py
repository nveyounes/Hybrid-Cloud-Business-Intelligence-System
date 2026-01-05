import json
import psycopg2

# 1. Database Connection (Your Neon Credentials)
DB_URL = "U CAN GET IT FROM NEON POSTGRES"

try:
    print("🔌 Connecting to Neon Cloud Database...")
    conn = psycopg2.connect(DB_URL)
    cur = conn.cursor()

    # 2. Create the Table (Fact_Orders)
    create_table_query = """
    CREATE TABLE IF NOT EXISTS "Fact_Orders" (
        "CommandeID" INT,
        "ClientID" INT,
        "ProduitID" INT,
        "Quantite" INT,
        "MontantTotal" FLOAT,
        "DateCommande" DATE,
        "Statut" VARCHAR(50)
    );
    """
    cur.execute(create_table_query)
    print("✅ Table 'Fact_Orders' ready.")

    # 3. Read the JSON File
    # Make sure this path matches where your json file actually is!
    with open('input_data/commandes.json', 'r') as f:
        orders = json.load(f)
    
    print(f"📂 Found {len(orders)} orders in JSON file.")

    # 4. Insert Data
    insert_query = """
    INSERT INTO "Fact_Orders" 
    ("CommandeID", "ClientID", "ProduitID", "Quantite", "MontantTotal", "DateCommande", "Statut") 
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    for order in orders:
        # Calculate a fake total if it's missing (just to be safe)
        total = order.get('MontantTotal', order.get('Quantite', 1) * 50.0)
        
        cur.execute(insert_query, (
            order['CommandeID'],
            order['ClientID'],
            order['ProduitID'],
            order['Quantite'],
            total,
            order['DateCommande'],
            order['Statut']
        ))

    conn.commit()
    cur.close()
    conn.close()
    print("🚀 SUCCESS! All orders loaded into the Cloud.")

except Exception as e:
    print(f"❌ Error: {e}")