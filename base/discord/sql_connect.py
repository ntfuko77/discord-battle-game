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
    def find_character(self, user_id:int) -> dict:
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
        print(user_id, character)
        self.con.execute("INSERT INTO user_character (user_id,character_name,max_hp,current_hp,attack,defense,speed,agility) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                        (user_id, character["name"],character["attributes"]["mhp"],character["attributes"]["mhp"],
                         character["attributes"]["attack"],character["attributes"]["defense"],character["attributes"]["speed"],
                         character["attributes"]["agility"]))
        self.save
    def delete_character(self, user_id:int) -> None:
        """Delete the character from the database."""
        self.con.execute("DELETE FROM user_character WHERE user_id = ?", (user_id,))
        self.save
    def match_opponent(self, user_id:int):
        """Find an opponent for the user."""
        target=self.find_character(user_id)['level']
        interval=(target-1,target+2,user_id)
        result=self.con.execute("SELECT * FROM user_character WHERE level BETWEEN ? AND ? AND user_id != ? LIMIT 10", interval)
        result=result.fetchall()
        if len(result)==0:
            return None
        else:
            return result
    def play_battle_start(self, user_id:int, opponent_id:int):
        """Start a battle between two users."""
        red=self.con.find_character(user_id)
        blue=self.con.find_character(opponent_id)
        return (red, blue)
        
        
        


test=1
if __name__=="__main__":
    module=Discord_Sql()
    if test==1:
        id=695714007339892766
        character={"name":"test","attributes":{"mhp":100,"attack":10,"defense":5,"speed":3,"agility":2}}
        module.save_character(id, character)
    id=695714007339892766

    print(module.serch_user(id))



