

import asyncio
import aiohttp
import json
from discord import Game
from discord.ext.commands import Bot

BOT_PREFIX = ("?","!")
client = BOT(command_prefix=BOT_PREFIX)


descrip = "This is all the bots commands that it has learned over the years\nKnowing these will help you operate Greg to Greg's full capacity!"
@client.command(name='command', description=descrip, brief="its the commands you doof", aliases=['commands','floofles','tittlywinks'], pass_context=True)
async def command(context, member: discord.Member):
    await bot.send_message()
    #figure this out later
