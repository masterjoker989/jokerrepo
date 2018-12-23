import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import asyncio
import colorsys
import random
import platform
from discord import Game, Embed, Color, Status, ChannelType
import os
import functools
import time
import datetime
import requests
import json
import aiohttp


client = Bot(description="Here is some commands for you", command_prefix="mw!", pm_help = True) #add_your_bot_description_with_prefix_here
client.remove_command('help')


@client.event
async def on_ready():
	print('Logged in as '+client.user.name+'')
	print('--------')
	print('--------')
	print('Started pubg') #add_your_bot_name_here
	return await client.change_presence(game=discord.Game(name='Master play bots | 9679 users')) #add_your_bot_status_here










client.run(os.getenv('Token'))
