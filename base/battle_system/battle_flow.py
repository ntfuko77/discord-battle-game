from stack_and_queue import stack

class base_battle_flow:
    def __init__(self):

        self.battle_stack = stack()
        self.battle_log = 
        self.battle_result = None
        self.battle_end = False
        self.battle_start = False

    def battle_start(self, red, blue):
        """Start the battle."""
        self.red = red
        self.blue = blue
        self.battle_start = True