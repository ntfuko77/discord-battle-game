import json

class configloader:
    def __init__(self):
        with open('discord-battle-game/profile/botkey.json') as file:
            self.botkey_data=json.load(file)
