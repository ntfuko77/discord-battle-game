from charactor import charactor
import battlecalculator
class fild_base:
    def __init__(self):
        self.round_number=0
    def begin(self)->str:
        """Generates a battle log message for the beginning of the battle."""
        self.round_number+=1
        return f"Round {self.round_number} begins!"
    def attack(self,nom:str,acc:str,number:int)->str:
        """Generates a battle log message for an attack."""
        return f"{nom} attacks with {acc} and deals {number} damage."

class fild(fild_base):
    def __init__(self,red:charactor,blue:charactor):
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
                break
            damage=battlecalculator.damage_calculator(order[1],order[0])
            yield self.attack(order[1].name,order[0].name,damage)
        if order[0].alive and not order[1].alive:
            yield f"{order[0].name} wins!"
        elif not order[0].alive and order[1].alive:
            yield f"{order[1].name} wins!"
        else:
            yield "It's a draw!"
        
    def scene(self,nom:charactor,acc:charactor):...
        
if __name__=='__main__':
    red=charactor("Red",100,50,30,20)
    blue=charactor("Blue",100,40,40,25)
    fild_instance=fild(red,blue)
    for log in fild_instance.base_scene():
        print(log)
