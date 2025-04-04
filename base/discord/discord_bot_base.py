import configloader
import discord
from discord.ext import commands
import parser
from discord_ui import send_menu
channel_id=909488097266389097

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
    @bot.event
    async def on_message(message:discord.message.Message) -> None:
        if message.author == bot.user:
            return
        par=parser.parser(message.content)
        if par=='menu':
            await send_menu(message.channel)
            


        if message.content.startswith('!hello'):
            await message.channel.send('Hello!')
        elif message.content.startswith('!ping'):
            await message.channel.send('Pong!')
        elif message.content.startswith('!help'):
            await message.channel.send('Available commands: !hello, !ping, !help')
        return
        

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
    if test==2:
        @bot.bot.event
        async def on_ready():
            x=discord.ui.View()
            y=discord.ui.Button(label="Click me!")
            @y.callback
            async def button_callback(interaction:discord.Interaction):
                await interaction.response.send("Button clicked!")
            x.add_item(y)
            print(f'{bot.config["bot_name"]} has connected to Discord!')
            await bot.send_message(909488097266389097, "Hello!")
            channel = bot.bot.get_channel(909488097266389097)
            if channel:
                await channel.send("Hello!", view=x)
            else:
                print(f"Channel with ID channel_id not found.")

    bot.login()
