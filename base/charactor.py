class Charactor:
    def __init__(self, name, hp, attack, defense,speed,agility):
        self.name = name
        self.max_hp,self.hp=hp,hp
        self.attack = attack
        self.defense = defense
        self.speed=speed
        self.agility=agility
        self.alive=True

    def __str__(self):
        return f"{self.name} - HP: {self.hp}, Attack: {self.attack}, Defense: {self.defense}"
    def __sub__(self, number:int):
        """Subtracts the number from the character's HP.
        Returns True if the character is alive, False otherwise."""
        self.hp -= number
        if self.hp <= 0:
            self.alive=False

    