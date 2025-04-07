import random
import sql_connect
import sys
sys.path.append("discord-battle-game/base")
import character
import battlelog

def seed():
    random.seed()
    return
con=sql_connect.Discord_Sql()
def generate_character(name:str,id):
    """Generate a character with random attributes and skills."""

    attributes = {
        "mhp": random.randint(1,5)*2+10,
        "agility": random.randint(1, 10),
        "attack": random.randint(1, 10),
        "defense": random.randint(1, 10),
        "speed": random.randint(1, 10),
    }
    character = {
        "name": name,
        "attributes": attributes,
    }

    con.save_character(id, character)
    return character
def delete_character(id:int) -> None:
    """Delete the character from the database."""
    con.delete_character(id)
def reset_character(id:int) -> None:
    """Reset the character in the database."""
    buffer=con.find_character(id)['character_name']
    con.delete_character(id)
    return generate_character(buffer, id)

def generate_battlelog(red,blue)->str:
    log=battlelog.Fild(red, blue)
    buffer=''
    for i in log.base_scene():
        buffer+=i+'\n'
    return buffer