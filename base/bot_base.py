from abc import ABC, abstractmethod
import configloader
import discord
from discord.ext import commands

class BotBase(commands.Bot, ABC):
    def __init__(self, command_prefix: str, intents: discord.Intents) -> None:
        super().__init__(command_prefix=command_prefix, intents=intents)
        self.config = configloader.Configloader()
        self.botkey_data = self.config.load_botkey()
        self.botkey = self.botkey_data['botkey']
        self.guild_id = self.botkey_data['guild_id']
        self.channel_id = self.botkey_data['channel_id']

    @abstractmethod
    async def on_ready(self) -> None:
        pass