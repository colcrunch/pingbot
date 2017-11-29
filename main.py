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

@pingbot.event
async def on_ready():
    print("Bot Online")
    print("------")
    print("Logged in as: {}".format(pingbot.user.name))
    print("ID: {}".format(pingbot.user.id))
    print("------")
    await pingbot.change_presence(game=discord.Game(type=0,name=config.msg+" | "+config.prefix+"help"),afk=False)

#Bot Commands go here
#---------------------------
# Ping
# Command returns PONG!
#---------------------------
@pingbot.command()
async def ping():
    """ PONG! """
    await pingbot.say("PONG!")


#---------------------------
# Connections
# Displats information about bot connections.
#---------------------------
@pingbot.command()
async def conn():
    """ Displays information about bot connections."""
    servers = []
    for server in pingbot.servers:
        servers.append(server.name)
    await pingbot.say(len(servers))

@pingbot.event
async def on_message(message):
    print(message.channel.id)
    print(message.content)
    if message.channel.id in config.PingOrigins:
        if message.author.id != pingbot.user.id:
            for desti in config.PingDestis:
                dest = discord.Object(id=desti)
                await pingbot.send_message(dest, message.content)
        else:
            pass
    else:
        pass
    await pingbot.process_commands(message)

pingbot.run(config.BotToken)
