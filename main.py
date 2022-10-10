import os
import time
from discord.ext import tasks
import  discord
import assets.reactor
import traceback
from dislash import SelectMenu,SelectOption
import web    
import platform
from discord.ext import commands
import subprocess
import requests, urllib, re
import pyjokes
import json
from dislash import InteractionClient, ActionRow, Button, ButtonStyle
from dislash import  ContextMenuInteraction
import asyncio 
import jishaku
import googletrans
import string    
import google , bs4
import sys
import DiscordUtils
import pkg_resources
import contextlib
import sys
import inspect
import shutil
import glob
import math
import textwrap
from discord.ext import commands
from io import StringIO
from traceback import format_exc
from contextlib import redirect_stdout
import json
import gc
import datetime
import traceback
import re
import io
import asyncio
import discord
import subprocess
from bs4 import BeautifulSoup
import urllib
import psutil
import motor.motor_asyncio
from lyrics_extractor import SongLyrics
import socket  
import termcolor 
from pyfiglet import Figlet
import urllib.request
from dislash import  Option, OptionType
import typing
import random
import io
import aiohttp
import warnings
from discord.ext.commands import AutoShardedBot
from pretty_help import DefaultMenu, PrettyHelp
from requests import PreparedRequest
from itertools import cycle
from discord.ext import  tasks
import topgg
import nest_asyncio 
import glob
from googletrans import Translator
import assets.funcs as funcs
# --------------------------------------------------
funcs.ratelimit()
nest_asyncio.apply()
mongo_url = os.environ.get("tst")
cluster = motor.motor_asyncio.AsyncIOMotorClient(mongo_url)
db = cluster["tst"]["data"]
predb = cluster["tst"]["prefix"]
# --------------------------------------------------
async def get_prefix(client, message):

  stats = await predb.find_one({"guild": message.guild.id})
# server_prefix = stats["prefix"]
  if stats is None:
    updated = {"guild": message.guild.id, "prefix": "a!"}
    await predb.insert_one(updated)
    extras = "a!"
    return commands.when_mentioned_or(extras)(client, message)
  else:
    extras = stats["prefix"]
  return commands.when_mentioned_or(extras)(client, message)
# --------------------------------------------------
intents = discord.Intents.all()
client =AutoShardedBot(shard_count=5,
command_prefix= (get_prefix),intents=intents,description="Support server https://discord.gg/avpet3NjTE \n Invite https://dsc.gg/tessarect",case_insensitive=True, help_command=PrettyHelp(index_title="Help <:book:939017828852449310>",))
# --------------------------------------------------
#Loading all cogs
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        try:          
          client.load_extension(f"cogs.{filename[:-3]}")
        except Exception as e:
          termcolor.cprint(e, color="red")
client.load_extension('jishaku')  
# --------------------------------------------------
@client.event
async def on_ready(): 
  os.system("clear")
  font = Figlet(font="standard")
  print(termcolor.colored(font.renderText(client.user.name), "blue"))
  termcolor.cprint(f"[+] Logged in as {client.user} ( ID : {client.user.id} )", color="blue")
  #reports=f"<:sucess:935052640449077248> Logged in as {client.user} ( ID : {client.user.id} )\n"
  system_latency = round(client.latency * 1000)
  em = discord.Embed(title =f"{client.user.name} Online!",color =discord.Color.green()).set_thumbnail(url=client.user.avatar_url).add_field(name="Ping (ms)",value=system_latency,inline=False).add_field(name="Servers",value=len(client.guilds),inline=True).add_field(name="Users",value=len(client.users),inline=True)     
  #reports +="<:sucess:935052640449077248> Initialised Embed\n"
  channel=client.get_channel(953571969780023366)

  cog_list = ["cogs." + os.path.splitext(f)[0] for f in [os.path.basename(f) for f in glob.glob("cogs/*.py")]]
  loaded_cogs = [x.__module__.split(".")[1] for x in client.cogs.values()]
  unloaded_cogs = [c.split(".")[1] for c in cog_list if c.split(".")[1] not in loaded_cogs]
  #reports +="<:sucess:935052640449077248> Initialised Cogs count\n"

  #reports +=f"<:sucess:935052640449077248> {loaded_cogs}\n"
  #reports +=f"<:Red_Cross:988360177017311263> {unloaded_cogs}\n"
  #reports +="<:sucess:935052640449077248> Ready for flight\n"
  #em.description=reports
  await channel.send(embed=em)
  for x in client.shards:
    if not x==3: #3 is the shard id of tbd
      emojis = ['😀', '😁', '🤣', '😃', '😄', '😅', '😆', '😉', '😊', '😋', '😎', '😍', '😘', '😗']
      await client.change_presence(
          status=discord.Status.dnd,
          shard_id=x, 
          activity=discord.Activity(
              type=discord.ActivityType.listening,
              name= f"{random.choice(emojis)} Shard {x}"
          )
      )
    else:
                
      await client.change_presence(
              status=discord.Status.dnd,
              shard_id=x, 
              activity=discord.Activity(
                  type=discord.ActivityType.listening,
                  name= f"{len(client.users):,} 👤 @ {len(client.guilds)} 🛸"
              ))  
  
  if os.path.exists("./storage/reboot.json"):
      with open("./storage/reboot.json", "r") as readFile:
          channel_id = json.load(readFile)
  
      channel = client.get_channel(channel_id)
      ex=discord.Embed(title="Successfully Restarted",description="100% \nBeep Beep Boop Beep !, Reboot done  ",color=funcs.theme_color)
      await channel.send(embed=ex)
  
      os.remove("./storage/reboot.json") 

    
# Running Bot
web.keep_alive()
try:
  client.run(os.environ['btoken'],reconnect=True)
except:
  embed=discord.Embed(
      title="Downtime",
      description="There was an issue when connecting to the bot, please be patient, conducting auto-restart",
      color=discord.Color.red()
  )
  requests.post(
      os.environ.get("healthwebhook"),
      json={'embeds':[embed.to_dict()]}
  )
  time.sleep(20)
  os.system("busybox reboot")