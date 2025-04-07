from character import Character
from math import sin
import battlecalculator
import random
class Fild_base:
    def __init__(self):
        self.round_number=0
    def begin(self)->str:
        """Generates a battle log message for the beginning of the battle."""
        self.round_number+=1
        return f"Round {self.round_number} begins!"
    def attack(self,nom:str,acc:str,number:int)->str:
        """Generates a battle log message for an attack."""
        return f"{nom} attacks with {acc} and deals {number} damage."
    def round_end(self)->str:
        """Generates a battle log message for the end of the round."""
        return f"Round {self.round_number} ends!"
    def generate_random_seed(self,name_space:str):
        """Generates a random seed."""
        seed=sum([ord(char) for char in name_space])
        seed=abs(int(sin(seed)))
        random.seed(seed)
    def basic_attack(self,nom:Character,acc:Character):
        """Generates a random attack process"""
        ...
class Fild(Fild_base):
    def __init__(self,red:Character,blue:Character):
        super().__init__()
        self.red=red
        self.blue=blue
    def base_scene(self):
        """Generates a battle log message for the base scene."""
        order=[self.red,self.blue]if self.red.speed>self.blue.speed else [self.blue,self.red]
        yield str(order[0])
        yield str(order[1])
        yield self.begin()
        while order[0].alive and order[1].alive:
            damage=battlecalculator.damage_calculator(order[0],order[1])
            yield self.attack(order[0].name,order[1].name,damage)
            if not order[1].alive:
                yield f"{order[1].name} is defeated!"
                yield self.round_end()
                break
            damage=battlecalculator.damage_calculator(order[1],order[0])
            yield self.attack(order[1].name,order[0].name,damage)
            if not order[0].alive:
                yield f"{order[0].name} is defeated!"
                yield self.round_end()
                break
            yield self.round_end()
            if self.round_number>10:
                yield "The battle is too long!"
                return
            yield self.begin()
        if order[0].alive and not order[1].alive:
            yield f"{order[0].name} wins!"
        elif not order[0].alive and order[1].alive:
            yield f"{order[1].name} wins!"
        else:
            yield "It's a draw!"
        return
        
    def scene(self,nom:Character,acc:Character):...
        
if __name__=='__main__':
    red=Character("Red",100,50,30,20,10)
    blue=Character("Blue",100,40,40,25,15)
    fild_instance=Fild(red,blue)
    for log in fild_instance.base_scene():
        print(log)
