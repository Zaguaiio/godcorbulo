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

    uwu = [
        'No te preocupes guerrero, esa chatarra apenas y puede moverse adelante!',
        'Recuerdo que me daban 50 centavos en el kilo por esa bola de metal, no representara ningun problema para ti guerrero',
        'No te preocupes guerrero, sabes por que le dicen Ultima? Por la ultima leccion que le di'
    ]

    ucob = [
        'Esa lagartija que, no dejes que te intimide guerrero, adelante!',
        'Guerrero... Aun recuerdo el dia que me hice una carnita asada con el abuelo de esa lagartija! Me lo saludas a ver si no llora',
        'JA, que vas a necesitar bendicion para pelear esa cosa, no merece respeto guerrero'
    ]

    tea = [
        'Esa chatarra lo unico que sabe hacer es regresar el tiempo para que le ponga otra monda, no dejes que te intimide guerrero',
        'Recuerdo el dia que le pusieron Alexander de nombre, que nombre tan comun nada digno de un dios, tienes mi bendicion hijo',
        'Le preguntas por Corbulo y saldra corriendo como el payaso que es, buena suerte guerrero'
    ]

    montura = [
        'Adelante guerrero, la tendras muy pronto!',
        'No te desesperes guerrero, la fuerza recompensa!',
        'Tendras una digna del guerrero que eres!'
    ]

    savage = [
        'Lo unico salvage es el fuego en tu interior guerrero, tienes mi bendicion',
        'Salvage es el olimpo, eso es un dia de campo, tu puedes eso y mas guerrero'
    ]

    print(message.channel.name)
    if message.channel.name != "los-caballero-de-corbulo-north":
         return
         
    if message.content.startswith('!bendicion') or message.content.startswith('!bendiceme'):
        print('bendicion detected')
        response = random.choice(bendiciones)

        if 'uwu' in message.content:
            response = random.choice(uwu)

        if 'ucob' in message.content:
            response = random.choice(ucob)

        if 'tea' in message.content:
            response = random.choice(tea)

        if 'montura' in message.content:
            response = random.choice(montura)

        if 'savage' in message.content:
            response = random.choice(savage)
            
        await message.channel.send(response)

client.run(TOKEN)