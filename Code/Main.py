# Importing the moudles 
import discord
import os
import time
import discord.ext
import platform
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, CheckFailure, check

client = discord.Client()
client = commands.Bot(command_prefix="$") # '$' is the prefix tha the user will type to active the bot.

# Printing this out on the terminal if the bot is online.
@client.event
async def on_ready():
	print("Lunbin Bot is online!")

@client.command()
async def ping(ctx):
	await ctx.send("pong!") # When a user types '$ping' the bot will send 'pong!'

client.run("BOT_TOKEN")