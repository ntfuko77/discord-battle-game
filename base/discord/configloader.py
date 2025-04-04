import json

class Configloader:
    def __init__(self):
        with open('discord-battle-game/profile/botkey.json',encoding='utf-8') as file:
            self.botkey_data=json.load(file)
            self.bot_name=self.botkey_data['bot_name']
            self.key=self.botkey_data['key']
    def load_botkey(self)->dict:
        with open('discord-battle-game/profile/botkey.json',encoding='utf-8') as file:
            botkey_data=json.load(file)
            return botkey_data
