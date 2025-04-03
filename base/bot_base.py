from abc import ABC, abstractmethod
import configloader
import discord
from discord.ext import commands

class BotBase():
    def load_token(self) -> str:
        bottoken = configloader.Configloader().load_botkey()['key']
        return bottoken
    def set_Intents(self) -> discord.Intents:
        intents = discord.Intents.default()
        intents.message_content = True
        return intents
    def login(self) -> None:
        token = self.load_token()
        self.bot=discord.Client(intents=self.set_Intents())
        print(' has connected to Discord!')
        self.bot.run(token)

if __name__ == "__main__":
    bot = BotBase()
    bot.login()
