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
    @property
    def save(self):
        """Save the changes to the database."""
        self.connection.commit()
    def save_character(self, user_id:int, character:dict) -> None:
        """Save the character to the database."""
        self.con.execute("INSERT INTO user_character (user_id,character_name,max_hp,current_hp,attack,defense,speed,agility) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                        (user_id, character["name"],character["attributes"]["mhp"],character["attributes"]["mhp"],
                         character["attributes"]["attack"],character["attributes"]["defense"],character["attributes"]["speed"],
                         character["attributes"]["agility"]))
        self.save
    def delete_character(self, user_id:int) -> None:
        """Delete the character from the database."""
        self.con.execute("DELETE FROM user_character WHERE user_id = ?", (user_id,))
        self.save



