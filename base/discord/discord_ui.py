# -*- coding: utf-8 -*-
# This is a sample code snippet for creating a Discord bot using discord.py.
import discord
# for testing purposes
import asyncio
from ui_trigger import generate_character, reset_character
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

class method:
    @staticmethod
    def menu_case_1()->discord.ui.view:
        view=discord.ui.View()
        buttons=[discord.ui.Button(label='fights', style=discord.ButtonStyle.primary)]
        buttons.append(discord.ui.Button(label='character', style=discord.ButtonStyle.primary))
        buttons.append(discord.ui.Button(label='rebirth', style=discord.ButtonStyle.primary))
        [view.add_item(i) for i in buttons]
        async def sub_fights(interaction:discord.Interaction)->None:
            await interaction.response.send_message("fights")
            # Add your fights logic here
        async def sub_character(interaction:discord.Interaction)->None:
            result=module.con.find_character(interaction.user.id)
            await interaction.response.send_message(result)
            # Add your character logic here
        buttons[0].callback = method.match_opponent
        buttons[1].callback = sub_character
        buttons[2].callback = method.rebirth
        return view
    @staticmethod
    async def rebirth(interaction:discord.Interaction)->None:
        result=reset_character(interaction.user.id)
        await interaction.response.send_message("rebirth:"+str(result))
    @staticmethod
    async def match_opponent(interaction:discord.Interaction)->None:
        target=module.con.match_opponent(interaction.user.id)
        if target is None:
            await interaction.response.send_message("You have no character.")
            return
        view=discord.ui.View()
        buttons=[discord.ui.Button(label=i['character_name'], custom_id=str(i['user_id']),style=discord.ButtonStyle.primary) for i in target]
        [view.add_item(i) for i in buttons]
        for i in buttons:
            i.callback = method.pvp_battle
        await interaction.response.send_message("match opponent", view=view)
        # Add your match logic here
    async def pvp_battle(interaction:discord.Interaction)->None:
        # Add your battle logic here
        await interaction.response.send_message(interaction.data)
        return
    



async def send_menu(message:discord.message.Message)->None:
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
        view=method.menu_case_1()
        await channel.send("menu here", view=view)
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
            charator=generate_character(textinput[0].value,interaction.user.id)
            await interaction.response.send_message(f"""submitted! get{textinput[0].value}
                    {charator['attributes']}""")
        modal.on_submit=on_submit
        await interaction.response.send_modal(modal)
    button[0].callback = create_charactor
    await channel.send("menu here", view=view)
    return






