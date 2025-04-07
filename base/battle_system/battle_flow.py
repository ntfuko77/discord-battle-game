from stack_and_queue import stack,queue
import sys
sys.path.append("..")
from base.character import Character

class base_battle_flow:
    def __init__(self):
        self.round=0
        self.battle_stack = stack()
        self.battle_log = queue()
        team = (None,None)
        self.battle_result = None
        self.battle_end = False
        self.battle_start = False
    def battle_start(self,start_function:function=None):
        """Start the battle."""
        self.battle_stack.push(self.round_start_phase)
    def round_start_phase(self,round_start_function:function=None):
        """Start the round."""
        self.round+=1
        self.battle_stack.push(self.battle_phase)
    def battle_phase(self,battle_phase_function:function=None):
        """Start the battle phase."""
        self.battle_stack.push(self.battle_end_phase)
    def round_end_phase(self,round_end_function:function=None):
        """End the battle."""
        if self.round>=10:
            self.battle_stack.push(self.battle_end_phase)
        else:
            self.battle_stack.push(self.round_start_phase)
    def battle_end_phase(self,battle_end_function:function=None):
        """End the battle."""
        self.battle_end = True
        self.battle_stack.push(self.battle_result_phase)
    def battle_result_phase(self,battle_result_function:function=None):
        """End the battle."""
        self.battle_result = battle_result_function()
class battle_flow(base_battle_flow):
    def __init__(self,red:Character,blue:Character):
        super().__init__()
        self.team = (red,blue)
    
        
class base_battle_scene:
    def __init__(self):
        self.battle_flow = battle_flow()
        self.battle_flow.battle_start(None)
        while self.battle_stack.is_empty() == False:
            current_function = self.battle_stack.pop()
            current_function()
        