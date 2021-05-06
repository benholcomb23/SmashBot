# bot.py
import os
import random
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected, sheeeeeeeeeshh!')

DISCORD_TOKEN = 'ODM3MTg1MTI3NTY5Njg2NTg5.YIo3aA.0B-NX4fjcGiCGnRq_kK_1tTh_t8'


work_words = ['work', 'working', 'slack', 'qualcomm', 'twerrrk']

stop_working_responses = [
    "Stop working.",
    "You should be smashing, not working",
    "Do not lust after productivity, my friend!"
]

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content


    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if any(word in msg.lower() for word in work_words):
        await message.channel.send(random.choice(stop_working_responses))

client.run(DISCORD_TOKEN)