# bot.py
import os
import random
import discord

# env
token = os.environ.get('DISCORD_TOKEN')

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected, sheeeeeeeeeshh!')



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

client.run(token)