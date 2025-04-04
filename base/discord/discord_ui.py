# -*- coding: utf-8 -*-
# This is a sample code snippet for creating a Discord bot using discord.py.
import discord
# for testing purposes
import asyncio
from ui_trigger import generate_character

async def send_menu(channel)->discord.ui.View:
    if hasattr(channel, 'send'):
        view = discord.ui.View()
        button = [discord.ui.Button(label='Create charactor', style=discord.ButtonStyle.primary)]
        [view.add_item(i) for i in button]
        async def create_charactor(interaction:discord.Interaction)->None:
            modal=discord.ui.Modal(title='Create charactor')
            textinput=[discord.ui.TextInput(label='Create name')]
            [modal.add_item(i) for i in textinput]
            async def on_submit(interaction:discord.Interaction):
                charator=generate_character(textinput[0].value)
                await interaction.response.send_message(f"""submitted! get{textinput[0].value}
                        {charator['attributes']}""")
            modal.on_submit=on_submit
            await interaction.response.send_modal(modal)
        button[0].callback = create_charactor
        await channel.send("menu here", view=view)

    else:
        raise ValueError("Invalid channel object.not callable")




