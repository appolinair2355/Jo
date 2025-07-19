import os
import psycopg2
from psycopg2.extras import RealDictCursor

DB_URL = os.getenv("DATABASE_URL")
conn = None

def setup_db():
    global conn
    conn = psycopg2.connect(DB_URL, cursor_factory=RealDictCursor)
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS compteur (
        symbole TEXT PRIMARY KEY,
        valeur INTEGER
    );
    CREATE TABLE IF NOT EXISTS messages (
        id BIGINT PRIMARY KEY
    );
    CREATE TABLE IF NOT EXISTS style (
        id INTEGER PRIMARY KEY DEFAULT 1,
        valeur INTEGER
    );
    INSERT INTO compteur (symbole, valeur) VALUES
        ('❤️', 0), ('♦️', 0), ('♣️', 0), ('♠️', 0)
    ON CONFLICT DO NOTHING;
    INSERT INTO style (id, valeur) VALUES (1, 1)
    ON CONFLICT DO NOTHING;
    """)
    conn.commit()

def get_counters():
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM compteur")
        rows = cur.fetchall()
        return {row['symbole']: row['valeur'] for row in rows}

def update_counters(symbols):
    with conn.cursor() as cur:
        for s in symbols:
            cur.execute("UPDATE compteur SET valeur = valeur + 1 WHERE symbole = %s", (s,))
        conn.commit()

def reset_counters():
    with conn.cursor() as cur:
        cur.execute("UPDATE compteur SET valeur = 0")
        cur.execute("DELETE FROM messages")
        conn.commit()

def get_processed_ids():
    with conn.cursor() as cur:
        cur.execute("SELECT id FROM messages")
        return {row['id'] for row in cur.fetchall()}

def save_processed_id(msg_id):
    with conn.cursor() as cur:
        cur.execute("INSERT INTO messages (id) VALUES (%s) ON CONFLICT DO NOTHING", (msg_id,))
        conn.commit()

def get_style():
    with conn.cursor() as cur:
        cur.execute("SELECT valeur FROM style WHERE id = 1")
        return cur.fetchone()['valeur']

def set_style(val):
    with conn.cursor() as cur:
        cur.execute("UPDATE style SET valeur = %s WHERE id = 1", (val,))
        conn.commit()