#Greg
import random
import asyncio
import aiohttp
import json
from discord import Game
from discord.ext.commands import Bot

TOKEN = 'NTcyNjU0ODM3MTQxOTk1NTMx.XMfdtg.ZuxaXPn0pCxzE_0OrkPJYRVarbE'
BOT_PREFIX = ("?","!")
client = Bot(command_prefix=BOT_PREFIX)

@client.command(name='8ball',
                description='Answers a yes/no question',
                brief='Answers from the beyond',
                aliases=['eigt-ball','eightball','8-ball'],
                pass_context=True)
async def eight_ball(context):
    possible_responses = [
    'I can happily say no',
    'Unfortunetaly yes',
    'I asked Steve, he said no',
    'I asked Larry, He said sure but only if its a wednesday',
    'I talked to some guy I found on Tinder, asked him that question, and he said, "Naw Bro."',
    'You are asking me a question, and boy howdy I have no idea.',
    'Clyde from South Park would have a better idea.',
    'Oof thats a yes, thanks Obama.'
    ]
    await client.say(random.choice(possible_responses)+", "+context.message.author.mention)

@client.command(name="hello",description="it says hello", brief="Hi", aliases=["hi"],pass_context=True)
async def hello(context):
    possible_responses = [
    "I am so dizzy, i was just doing the turn-around portion of the Hokey Pokey",
    "I love eating bread with pumpkin in it. Yes, I am that basic ;)."
    ]
    await client.say(context.message.author.mention+", "+random.choice(possible_responses))

@client.command(pass_context = True)
async def clear(ctx, number):
    mgs = [] #Empty list to put all the messages in the log
    number = int(number) #Converting the amount of messages to delete to an integer
    async for x in client.logs_from(ctx.message.channel, limit = number):
        mgs.append(x)
    await client.delete_messages(mgs)


@client.command()
async def square(number):
    squared_value = int(number)*int(number)
    await client.say(str(number) + " squared is " + str(squared_value))

@client.event
async def on_ready(message):
    if message.author == client.user:
        return
    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)



@client.event
async def on_ready():
    await client.change_presence(game=Game(name="Staring a bear down"))
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-------------')

async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        print("Current servers: ")
        for server in client.servers:
            print(server.name)
        await asyncio.sleep(600)

client.loop.create_task(list_servers())
client.run(TOKEN)
