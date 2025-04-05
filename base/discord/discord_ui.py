# -*- coding: utf-8 -*-
# This is a sample code snippet for creating a Discord bot using discord.py.
import discord
# for testing purposes
import asyncio
from ui_trigger import generate_character
import sql_connect

class module:
    def __init__(self, name:str)->None:
        self.name=name
        self.con=sql_connect.Discord_Sql()
    def __str__(self)->str:
        return f'{self.name}'
    def __repr__(self)->str:
        return f'{self.name}'
module=module('discord_ui')
async def send_menu(message:discord.message.Message)->None:
    if hasattr(message.channel, 'send'):
        # Check if the channel object has a send method
        user=message.author if hasattr(message, 'author') else None
        if user is None:
            raise ValueError("User not found in the channel object.")
        channel=message.channel if hasattr(message, 'channel') else channel
        if channel is None:
            raise ValueError("Channel not found in the channel object.")
        # case 1: if user has character
        if module.con.serch_user(user.id)==True:
            # get user character
            await channel.send("charactor here")
            return


        # case 2: if user not has character
        # Create a button and a view
        view = discord.ui.View()
        button = [discord.ui.Button(label='Create charactor', style=discord.ButtonStyle.primary)]
        [view.add_item(i) for i in button]
        async def create_charactor(interaction:discord.Interaction)->None:
            modal=discord.ui.Modal(title='Create charactor')
            textinput=[discord.ui.TextInput(label='Create name')]
            [modal.add_item(i) for i in textinput]
            async def on_submit(interaction:discord.Interaction):
                charator=generate_character(textinput[0].value)
                id=interaction.user.id
                # Save the character to the database here
                module.con.save_character(id, charator)
                await interaction.response.send_message(f"""submitted! get{textinput[0].value}
                        {charator['attributes']}""")
            modal.on_submit=on_submit
            await interaction.response.send_modal(modal)
        button[0].callback = create_charactor
        await channel.send("menu here", view=view)
        return

    else:
        raise ValueError("Invalid channel object.not callable")




