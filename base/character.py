from sqlite3 import Row
class Character(dict):
    def __sub__(self, number:int):
        """Subtracts the number from the character's HP.
        Returns True if the character is alive, False otherwise."""
        self.hp -= number
        if self.hp <= 0:
            self.alive=False





    