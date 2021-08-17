# bot.py
import os

import discord
from dotenv import load_dotenv
import random

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    bendiciones = [
        'Que tengas un increible dia Guerrero!',
        'Guerrero, no olvides que cualquier dia hay que truinfar, adelante!',
        'Jamas te rindas Guerrero! Toma mi mano y vamos hacia la victoria!',
        'Estoy contigo, adelante Guerrero!'
    ]

    print(message.channel.name)
    if message.channel.name != "los-caballero-de-corbulo-north":
         return
         
    if message.content == '!bendicion':
        response = random.choice(bendiciones)
        await message.channel.send(response)

client.run(TOKEN)