import sqlite3

class SqlBase:
    def __init__(self, db_path: str):
        self.db_path = db_path
        self.connection = None

    def connect(self):
        """Connect to the SQLite database."""
        self.connection = sqlite3.connect(self.db_path)
        self.connection.row_factory = sqlite3.Row
        print(f"Connected to database at {self.db_path}")

    def close(self):
        """Close the SQLite database connection."""
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

if __name__ == "__main__":
    sql_base = SqlBase("discord-battle-game/profile/simple_world.sqlite3")
    sql_base.connect()
    # Perform database operations here
    con = sql_base.connection.cursor()
    # Example: Create a table
    # reset table
    reset=True
    if reset==True:
        con.execute('''DROP TABLE IF EXISTS user_character''')
        con.execute('''DROP TABLE IF EXISTS users''')
        con.execute('''DROP TABLE IF EXISTS status''')
    con.execute('''CREATE TABLE IF NOT EXISTS users(
                    user_id INTEGER PRIMARY KEY,
                    inventory_id INTEGER,
                    character_id INTEGER NOT NULL,
                    status_id INTEGER,
                    registered_at TIMESTAMP DEFAULT SELECT(DATETIME("now","+8 hours"))
                )''')
    con.execute('''CREATE TABLE IF NOT EXISTS status(
                    status_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    status_name TEXT NOT NULL,
                    description TEXT NOT NULL,
                    effect TEXT NOT NULL,
                    
                )''')

    con.execute('''CREATE TABLE IF NOT EXISTS user_character (
                    user_id INTEGER PRIMARY KEY,
                    character_name TEXT NOT NULL,
                    max_hp INTEGER NOT NULL CHECK (max_hp > 0),
                    current_hp INTEGER NOT NULL,
                    attack INTEGER NOT NULL CHECK (attack > 0),
                    defense INTEGER NOT NULL CHECK (defense > 0),
                    speed INTEGER NOT NULL CHECK (speed > 0),
                    agility INTEGER NOT NULL CHECK (agility > 0),
                    level INTEGER DEFAULT 1 CHECK (level > 0),
                    experience INTEGER DEFAULT 0 CHECK (experience >= 0)
                )''')
    

    sql_base.close()
