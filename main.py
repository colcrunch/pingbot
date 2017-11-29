import sys
import asyncio
import config
import logging
import datetime
import re

import discord
from discord.ext.commands import Bot

logger = logging.getLogger('discord')
logger.setLevel(config.loggingLevel)
handler = logging.FileHandler(filename='logs/pingbot'+datetime.datetime.utcnow().strftime("%Y%m%d%H%M")+'.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s ::: %(levelname)s ::: %(name)s :::  %(message)s'))
logger.addHandler(handler)

pingbot = Bot(command_prefix=config.prefix)

@killbot.event
async def on_ready():
    print("Bot Online")
    print("------")
    print("Logged in as: {}".format(pingbot.user.name))
    print("ID: {}".format(pingbot.user.id))
    print("------")
    await pingbot.change_presence(game=discord.Game(type=0,name=config.msg+" | "+config.prefix+"help"),afk=false)

#Bot Commands go here
#---------------------------
# Ping
# Command returns PONG!
#---------------------------
@killbot.command()
async def ping():
    """ PONG! """
    await pingbot.say("PONG!")
