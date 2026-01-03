import os
import psycopg2
from typing import List
from models import Product

def load_products(products: List[Product]):

    db_url = os.getenv(
        "DATABASE_URL",
    )

    conn = psycopg2.connect(db_url)
    cur = conn.cursor()

    create_sql = """
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY,
        title TEXT,
        description TEXT,
        category TEXT,
        price REAL,
        rating REAL,
        stock INTEGER,
        brand TEXT,
        weight REAL
    );
    """
    cur.execute(create_sql)

    insert_sql = """
    INSERT INTO products
    (id, title, description, category, price, rating, stock, brand, weight)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (id) DO NOTHING;
    """

    for p in products:
        cur.execute(insert_sql, (
            p.id,
            p.title,
            p.description,
            p.category,
            p.price,
            p.rating,
            p.stock,
            p.brand,
            p.weight
        ))

    conn.commit()

    cur.close()
    conn.close()

    print("[LOAD] Datos guardados en Postgres correctamente.")