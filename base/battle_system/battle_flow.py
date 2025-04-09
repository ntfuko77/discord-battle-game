from stack_and_queue import stack,queue
import sys
sys.path.append("discord-battle-game/base")
from character import Character
from typing import Optional, Callable

#for testing
from discord.sql_connect import Discord_Sql

class base_battle_flow:
    def __init__(self):
        self.round=0
        self.battle_stack = stack()
        self.battle_log = queue()
        team = (None,None)
        self.battle_result = None
        self.battle_end = False
    def battle_start(self,start_function: Optional[Callable]=None):
        """Start the battle."""
        self.battle_stack.push(self.round_start_phase)
        self.battle_stack.push(start_function)
    def round_start_phase(self,round_start_function:Optional[Callable]=None):
        """Start the round."""
        self.round+=1
        self.battle_stack.push(self.battle_phase)
        self.battle_stack.push(round_start_function)
    def battle_phase(self,battle_phase_function:Optional[Callable]=None):
        """Start the battle phase."""
        self.battle_stack.push(self.round_end_phase)
        self.battle_stack.push(battle_phase_function)
    def round_end_phase(self,round_end_function:Optional[Callable]=None):
        """End the battle."""
        if self.round>=10:
            self.battle_stack.push(self.battle_end_phase)
        else:
            self.battle_stack.push(self.round_start_phase)
            self.battle_stack.push(round_end_function)
    def battle_end_phase(self,battle_end_function:Optional[Callable]=None):
        """End the battle."""
        self.battle_stack.push(self.battle_result_phase)
        self.battle_stack.push(battle_end_function)
    def battle_result_phase(self,battle_result_function:Optional[Callable]=None):
        """End the battle."""
        self.battle_stack.push(battle_result_function)
        self.battle_end = True
    def log(self,message:str):
        """Log the message."""
        self.battle_log.enqueue(message)
    def result_battle_log(self) -> str:
        """Return the battle log."""
        buffer=''
        if self.battle_end == True:
            while self.battle_log.is_empty() == False:
                buffer+=self.battle_log.dequeue()+'\n'
        return buffer

class battle_flow(base_battle_flow):
    def __init__(self,red:Character,blue:Character):
        super().__init__()
        self.team = (red,blue)
    def start_function(self):
        self.log("Battle Start!")
        self.log(f"{self.team[0]['character_name']} vs {self.team[1]['character_name']}")
    def battle_start(self):
        super().battle_start(self.start_function)
    def round_start_function(self):
        self.log(f"Round {self.round} Start!")
    def round_start_phase(self):
        super().round_start_phase(self.round_start_function)
    def round_end_function(self):
        self.log(f"Round {self.round} End!")
    def round_end_phase(self):
        super().round_end_phase(self.round_end_function)
    def battle_end_function(self):
        self.log("Battle End!")
    def battle_end_phase(self):
        super().battle_end_phase(self.battle_end_function)


    
        
class base_battle_scene:
    def __init__(self,red:Character,blue:Character):
        self.battle_flow = battle_flow(red,blue)
        self.battle_flow.battle_start()
        while self.battle_flow.battle_stack.is_empty() == False:
            current_function = self.battle_flow.battle_stack.pop()
            current_function()
        print(self.battle_flow.result_battle_log())
        print(self.battle_flow.battle_log.dequeue())

if __name__ == "__main__":
    con=Discord_Sql()
    buffer=con.con.execute("SELECT * FROM user_character").fetchall()
    red=Character(buffer[0])
    
    blue=Character(buffer[1])
    battle = base_battle_scene(red,blue)
        