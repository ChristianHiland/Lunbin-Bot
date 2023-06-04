# Importing the moudles 
import discord
import os
import time
import platform
import json
import discord.ext
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, CheckFailure, check

# Reading the Config file.
configJSON = "Config/Config.json"
config = open(configJSON, "r")
BOT_PREFIX = config['Prefix']
BOT_TOKEN = config['TOKEN']

client = discord.Client()
client = commands.Bot(command_prefix=BOT_PREFIX) # BOT_PREFIX is the prefix tha the user will type to active the bot.


# Printing this out on the terminal if the bot is online.
@client.event
async def on_ready():
	print("Lunbin Bot is online!")
	print("Bot is running on:\n")
	print("Platform System: {platform.system()}  Platform Release: {platform.release()}  OS Name: ({os.name})")
	print("-------------------")

@client.command()
async def ping(ctx):
	await ctx.send("pong!") # When a user types '$ping' the bot will send 'pong!'

client.run(BOT_TOKEN)