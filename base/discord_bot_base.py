from abc import ABC, abstractmethod
import configloader
import discord
from discord.ext import commands

class BotBase():
    def __init__(self):
        self.config = configloader.Configloader().load_botkey()
        self.bot = None
    def set_Intents(self) -> discord.Intents:
        intents = discord.Intents.default()
        intents.message_content = True
        return intents
    def login(self) -> None:
        self.bot=discord.Client(intents=self.set_Intents())
        print(f'{self.config["bot_name"]} has connected to Discord!')
        self.bot.run(self.config['key'])

if __name__ == "__main__":
    bot = BotBase()
    bot.login()
