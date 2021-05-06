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


# messages user to stop working if they send message about work
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    if any(word in msg.lower() for word in work_words):
        await message.channel.send(random.choice(stop_working_responses))


# messages a user if they enter the "Twerrrk" channel
@client.event
async def on_voice_state_update(user, before, after):

    entered_twerrrk_responses = [
        f'bro, @{user.nick}, why u on this channel... 😐😐😐',
        f'hey everyone, @{user.nick} is WORKING',
        f'@{user.nick}. pls quit your job',
        f'not even Tyler works as much as @{user.nick}'
    ]

    if before.channel is None and after.channel is not None:
        if after.channel.id == 692913282457141399:
            ctx_for_voice_chat = client.get_channel(773948529902223380)
            await ctx_for_voice_chat.send(random.choice(entered_twerrrk_responses))

client.run(token)
