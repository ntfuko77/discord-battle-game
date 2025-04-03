import configloader
import discord
from discord.ext import commands

class bot_base_order():
    def setup_bot(self) -> None:
        self.bot_log()
        self.bot=discord.Client(intents=self.set_Intents())
        print(type(self.bot))
    async def send_message(self, channel_id=909488097266389097, message='Hello'):
        channel = self.bot.get_channel(channel_id)
        if channel:
            self.bot.loop.create_task(channel.send(message))
        else:
            print(f"Channel with ID {channel_id} not found.")

def set_events(bot:discord.client.Client,cursor) -> None:
    @bot.event
    async def on_ready():
        print('ready')
        await cursor.send_message()
        

class BotBase(bot_base_order):
    def __init__(self):
        self.config = configloader.Configloader().load_botkey()
        self.setup_bot()
    def set_Intents(self) -> discord.Intents:
        intents = discord.Intents.default()
        intents.message_content = True
        return intents
    def login(self) -> None:
        print(f'{self.config["bot_name"]} has connected to Discord!')
        self.bot.run(self.config['key'])
        return
    def bot_log(self) -> None:
        self.log=open('discord-battle-game/profile/botlog.txt', 'a+')

test=1
if __name__ == "__main__":
    bot = BotBase()
    if test==0:
        @bot.bot.event
        async def on_ready():
            print(f'{bot.config["bot_name"]} has connected to Discord!')
            await bot.send_message()
    if test==1:
        set_events(bot.bot,bot)
    bot.login()
