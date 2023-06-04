# Importing the moudles 
import json
import os 
import platform 
import random 
import sys 
import discord 
from discord.ext import commands, tasks 
from discord.ext.commands import Bot, Context 
  
intents = discord.Intents.default() 
  
""" 
Uncomment this if you want to use prefix (normal) commands. 
It is recommended to use slash commands and therefore not use prefix commands. 
 
If you want to use prefix commands, make sure to also enable the intent below in the Discord developer portal. 
""" 
intents.message_content = True 
 
bot = Bot( 
    command_prefix=commands.when_mentioned_or(config["prefix"]), 
    intents=intents, 
    help_command=None, 
 
bot.config = config 
  
  
@bot.event 
async def on_ready() -> None: 
    """ 
    The code in this event is executed when the bot is ready. 
    """ 
    bot.logger.info(f"Logged in as {bot.user.name}") 
    bot.logger.info(f"discord.py API version: {discord.__version__}") 
    bot.logger.info(f"Python version: {platform.python_version()}") 
    bot.logger.info(f"Running on: {platform.system()} {platform.release()} ({os.name})") 
    bot.logger.info("-------------------") 

# Starting the bot with the token    
bot.run(config["token"])
