# bot.py
import os
import random
import discord
import responses
from string import Template
from datetime import datetime

# env
token = os.environ.get('DISCORD_TOKEN')

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected, sheeeeeeeeeshh!')


# messages user to stop working if they send message about work
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    if any(word in msg.lower() for word in work_words):
        await message.channel.send(random.choice(responses.stop_working_responses))


# pings a user if they enter the "Twerrrk" channel
@client.event
async def on_voice_state_update(user, before, after):
    if before.channel is None and after.channel is not None:
        now = datetime.now()
        if '9' > now.strftime('%H') > '19':
            if after.channel.id == 692913282457141399:
                worker = user.mention
                ctx_for_voice_chat = client.get_channel(773948529902223380)
                await ctx_for_voice_chat.send(Template(random.choice(responses.entered_twerrrk_responses)).substitute(
                    worker=worker))


client.run(token)
