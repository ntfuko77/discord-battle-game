import sys
sys.path.append("discord-battle-game/base/sql")
import sqlbase
class Discord_Sql(sqlbase.SqlBase):
    def __init__(self):
        super().__init__("discord-battle-game/profile/simple_world.sqlite3")
        self.connect()
        self.con=self.connection.cursor()
    def serch_user(self, user_id:int) -> bool:
        """Check if the user exists in the database."""
        self.con.execute("SELECT * FROM user_character WHERE user_id = ?", (user_id,))
        result = self.con.fetchone()
        return result is not None
    def find_user(self, user_id:int) -> dict:
        """Find the user in the database."""
        self.con.execute("SELECT * FROM user_character WHERE user_id = ?", (user_id,))
        result = self.con.fetchone()
        return dict(result) if result else None
    def save_character(self, user_id:int, character:dict) -> None:
        """Save the character to the database."""
        self.con.execute("INSERT INTO characters (user_id, name, attributes) VALUES (?, ?, ?)",
                        (user_id, character["name"], str(character["attributes"])))
        self.connection.commit()



