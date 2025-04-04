from abc import ABC, abstractmethod
class Unit(ABC):
    def __init__(self, name: str, health: int, damage: int):
        self.name = name
        self.health = health
    @abstractmethod
    def attack(self, target):
        pass
    @abstractmethod
    def defend(self, damage: int):
        pass
    @abstractmethod
    def is_alive(self) -> bool:
        return self.health > 0
class player_character(Unit):
    def __init__(self, name: str, health: int, damage: int):
        super().__init__(name, health, damage)

    def attack(self, target):
        target.defend(self.damage)

    def defend(self, damage: int):
        self.health -= damage

    def is_alive(self) -> bool:
        return self.health > 0