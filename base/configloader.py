import json

class Configloader:
    def __init__(self):...
    def load_botkey(self)->dict:
        with open('discord-battle-game/profile/botkey.json',encoding='utf-8') as file:
            botkey_data=json.load(file)
            return botkey_data
