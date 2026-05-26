import sqlite3

DATABASE_NAME = "corebanking.db"

def get_db_connection():
    """SQLite Create and return a database connection."""
    conn  = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row
    return conn
def create_tables():
    """Create the tables in the database."""
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('''
        Create TABLE IF NOT EXISTS accounts (
             account_id INTEGER PRIMARY KEY AUTOINCREMENT,
             owner_id TEXT NOT NULL,
             balance REAL NOT NULL DEFAULT 0.0
        )     
    ''')
    conn.commit()
    conn.close()
    print("Tables created successfully.")

if __name__ == '__main__':
    create_tables()