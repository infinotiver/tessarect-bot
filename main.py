import os
with open("requirements.txt") as file:
    os.system(f"pip3 install {' '.join(file.read().split())}")
import time
from discord.ext import tasks
import  discord
import assets.reactor
import traceback
from dislash import SelectMenu,SelectOption
import web        
#dislash.py 
from discord.ext import commands
import subprocess
import requests, urllib, re
#import praw 
import pyjokes
import json
from dislash import InteractionClient, ActionRow, Button, ButtonStyle
from dislash import  ContextMenuInteraction
import asyncio 
import jishaku
import googletrans
import sys
#from discord_slash import SlashCommand, SlashContext
try:

  import DiscordUtils
except:
  os.system( 'pip install DiscordUtils')

import pkg_resources
import contextlib
import sys
import inspect
import os
import shutil
import glob
import math
import textwrap
from discord.ext import commands
from io import StringIO
from traceback import format_exc

from contextlib import redirect_stdout

# Common imports that can be used by the debugger.
import requests
import json
import gc
import datetime
import time
import traceback
import re
import io
import asyncio
import discord
import random
import subprocess
from bs4 import BeautifulSoup
import urllib
import psutil

#from replit import db
import motor.motor_asyncio
#import nest_asyncio
#import datetime
import socket  
import datetime
#from datetime import datetime, timedelta
# Create a translator object
#from discord_slash import SlashCommand, SlashContext
import logging

# create logger
logger = logging.getLogger('logger')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')
import urllib.request
from dislash import  Option, OptionType
import typing
import random
from PIL import Image
import io

#subprocess.check_call([sys.executable, '-m', 'pip', 'install','dislash.py', 'discord-pretty-help','randfacts','TenGiphPy','pymongo[srv]'])
def get_prefix(client, message):
    try:
        with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)
            return prefixes[str(message.guild.id)]
        
    except KeyError: 
        with open('prefixes.json', 'r') as k:
            prefixes = json.load(k)
        prefixes[str(message.guild.id)] = ['amt','a! ']

        with open('prefixes.json', 'w') as j:
            json.dump(prefixes, j, indent = 4)

        with open('prefixes.json', 'r') as t:
            prefixes = json.load(t)
            return prefixes[str(message.guild.id)]
        
    except: # I added this when I started getting dm error messages
        print("Not ok")
        return ['a!','amt ']
#-----------------------------------------------------------------------------------------------------------------------
import aiohttp
import warnings
from discord.ext.commands import AutoShardedBot
from pretty_help import DefaultMenu, PrettyHelp

r = requests.head(url="https://discord.com/api/v1")
try:
  print(f"Rate limit {int(r.headers['Retry-After']) / 60} minutes left")
except:
  print('No ratelimit')
restart_data = {
    'str': datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
    'obj': time.time()
}

#menu = DefaultMenu(page_left="<:arrow_left:940845517703889016>", page_right="<:arrow_right:940608259075764265>", remove="❌", active_time=15)
import nest_asyncio              
nest_asyncio.apply()
mongo_url = os.environ.get("tst")
cluster = motor.motor_asyncio.AsyncIOMotorClient(mongo_url)
db = cluster["tst"]["data"]
intents = discord.Intents.all()
client =AutoShardedBot(shard_count=5,
    command_prefix= (get_prefix),intents=intents,description="Support server https://discord.gg/avpet3NjTE \n Invite https://dsc.gg/tessarect",case_insensitive=True, help_command=PrettyHelp(index_title="Help <:book:939017828852449310>",no_category="Basic Commands",sort_commands=False,show_index=True))
#slash = SlashCommand(client)
m = '֍'

#____emojis______
blueokay = '<a:Tick:922450348730355712>'
bluetrusted=''
mongo_url = os.environ['enalevel']

cluster = motor.motor_asyncio.AsyncIOMotorClient(mongo_url)
ecomoney = cluster["discord"]["terrabux"]
prefix=(get_prefix)
from itertools import cycle
from discord.ext import  tasks

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        try:
          client.load_extension(f"cogs.{filename[:-3]}")
        except Exception as e:
          print(f"{filename} - {traceback.print_exc()}") 


import glob
@client.event
async def on_ready():  
    print(f'{client.user} - Tessarect  has connected to Discord! Enjoy ')  
    em = discord.Embed(title ="<:online_status:930347639172657164> Tessarect Up again !",color =discord.Color.dark_theme())
    em.set_author(name=client.user.name,icon_url=client.user.avatar_url)
    em.set_thumbnail(url=client.user.avatar_url)
    em.add_field(name="Server Count",value=len(client.guilds),inline=False)
    em.add_field(name="User Count",value=len(client.users),inline=False)
    
    channel=client.get_channel(953571969780023366)
    await channel.purge(limit=None, check=lambda msg: not msg.pinned)
    cog_list = ["cogs." + os.path.splitext(f)[0] for f in [os.path.basename(f) for f in glob.glob("cogs/*.py")]]
    loaded_cogs = [x.__module__.split(".")[1] for x in client.cogs.values()]
    unloaded_cogs = [c.split(".")[1] for c in cog_list if c.split(".")[1] not in loaded_cogs]
    await channel.send(embed=em)
    em2 = discord.Embed(title ="Successfuly `on_ready`",color =discord.Color.dark_blue())
    em2.add_field(name="Cogs Count",value=len(client.cogs),inline=False)
    em2.add_field(name='Loaded Cogs ({})'.format(len(loaded_cogs)), value='\n'.join(sorted(loaded_cogs)))
    value='All Loaded' if len(unloaded_cogs)<0 else '\n'.join(sorted(unloaded_cogs))
    if not len(unloaded_cogs)==0:
      em2.add_field(name='UnLoaded Cogs ({})'.format(len(unloaded_cogs)), value='value')

    await channel.send(embed=em2)
    for x in client.shards:
      if not x==3:#3 is the shard id of tbd
          
        await client.change_presence(
                status=discord.Status.dnd,
                shard_id=x, 
                activity=discord.Activity(
                    type=discord.ActivityType.watching,
                    name= f"Shard {x} | {len(client.guilds)}"
                ))
      else:
                  
        await client.change_presence(
                status=discord.Status.dnd,
                shard_id=x, 
                activity=discord.Activity(
  
                    type=discord.ActivityType.watching,
                    name= f"{len(client.users)} users on {len(client.guilds)} servers "
                ))

    if os.path.exists("./storage/reboot.json"):
        with open("./storage/reboot.json", "r") as readFile:
            channel_id = json.load(readFile)

        channel = client.get_channel(channel_id)
        ex=discord.Embed(title="Successfully Restarted",description="Heyo I am back after reboot ",color=discord.Color.dark_blue())
        await channel.send(embed=ex)

        os.remove("./storage/reboot.json")  
    #deletelogs.start()              
    #update_s.start()


from googletrans import Translator


@client.command()
async def translate(ctx, lang, *, thing=None):
    description = ""
    for lang in googletrans.LANGCODES:
        description += "**{}** - {}\n".format(string.capwords(lang), googletrans.LANGCODES[lang])
    if not thing:
      return await ctx.send(embed=discord.Embed(description=description,color=discord.Color.blue()))
    translator = Translator()
    
    translation = translator.translate(thing, dest=lang)
    e=discord.Embed(title="Google Translation",description=f"""```yml
Output: {translation.text}
Input: {thing}```""",color=discord.Color.blue())
    await ctx.reply(embed=e)


status= [" a!help in {n}  servers ",'Tessarect  BOT','Try my New Economy Bots'.format(n=len(client.guilds))]

warnings.filterwarnings("ignore", category=DeprecationWarning)
client.session = aiohttp.ClientSession()
client.load_extension('jishaku')
import datetime

@client.event
async def on_resumed():
    print("Bot user: {0.user} RESUMED".format(client))

    print("==========RESUMED==========")
    em = discord.Embed(title ="Tessarect Up Again",description=f"Tessarect  Service Resumed ",color =discord.Color.dark_theme())
    em.add_field(name="Server Count",value=len(client.guilds),inline=False)
    em.add_field(name="User Count",value=len(client.users),inline=False)
    channel = client.get_channel(953571969780023366)

    await channel.send(embed=em)    

import topgg

# This example uses tasks provided by discord.ext to create a task that posts guild count to Top.gg every 30 minutes.

dbl_token = os.environ['topgg']  # set this to your bot's Top.gg token
client.topggpy = topgg.DBLClient(client, dbl_token)

@tasks.loop(minutes=30)
async def update_stats():
    """This function runs every 30 minutes to automatically update your server count."""
    try:
        await client.topggpy.post_guild_count()
        print(f"Posted server count ({client.topggpy.guild_count})")
    except Exception as e:
        print(f"Failed to post server count\n{e.__class__.__name__}: {e}")
import topgg



#update_stats.start()
@client.event
async def on_guild_remove(guild): #when the bot is removed from the guild
    with open('prefixes.json', 'r') as f: #read the file
        prefixes = json.load(f)

    prefixes.pop(str(guild.id)) #find the guild.id that bot was removed from

    with open('prefixes.json', 'w') as f: #deletes the guild.id as well as its prefix
        json.dump(prefixes, f, indent=4)
    await client.change_presence(

            activity=discord.Activity(
                type=discord.ActivityType.watching,
                name= f"{str(len(client.guilds))} Servers"
            ))
        
@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def changeprefix(ctx, prefix): #command: a!changeprefix ...
    #test
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = [prefix,"amt "]

    with open('prefixes.json', 'w') as f: #writes the new prefix into the .json
        json.dump(prefixes, f, indent=4)

    await ctx.reply(f'Prefix changed to: {prefix}')
    #test #confirms the prefix it's been changed to

    await client.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.watching,
                name= f"{str(len(client.guilds))} Servers"
            ))

def dev():
    def predicate(ctx):
        return ctx.message.author.id == 904221795358478366 or 855327915301404674  or 892376302831677520 or 900992402356043806 or 900992402356043806
    return commands.check(predicate)
@client.event
async def on_guild_join(guild): #when the bot joins the guild
    with open('prefixes.json', 'r') as f: #read the prefix.json file
        prefixes = json.load(f) #load the json file

    prefixes[str(guild.id)] = ['a!','amt ']#default prefix

    with open('prefixes.json', 'w') as f: #write in the prefix.json "message.guild.id": "a!"
        json.dump(prefixes, f, indent=4) #the indent is to make everything look a bit neater





names =['Spencer M. McKnight','Saul D. Burgess','Ghiyath Haddad Shadid','Ramzi Muta Hakimi','Callum Peel','Joao Barbosa Pinto','Bertram Hoving','Cian Reith','Mat Twofoot''Alexander Achen''Rohan ','Manish Nadela']   
   
    
@client.command(hidden=True)
@commands.is_owner()
async def shutdown(ctx):

    log_out = ['Man am I tired, I think I need to get some shuteye',
               'CAN\'T SEE, NEED TO CLOSE EYES',
               'I think I\'ll just lay down for a minute ',
               'Short of breath, vision fading..... leave me here to DIIIE'
               ]

    response3 = random.choice(log_out)
    await ctx.reply(response3)
    await client.logout()
@shutdown.error
async def error(ctx,error):

        annoyed = [
            'Your\'re not the boss of me!!',
            'You dare to defy ME????',
            'Yeah, you bugger off!!',
            'You\'r words mean nothing to me!!!'
        ]
        pain = random.choice(annoyed)
        await ctx.reply(pain)



@client.command()
async def convertmoney(ctx,value,curr1,curr2):
  res=await get_converted_currency(value,curr1,curr2)
  await ctx.send(embed=discord.Embed(description=res,color=discord.Color.gold()))
import urllib
@client.command(alises=['dict','define'])
async def dictionary(ctx, *, text):
  textf=urllib.parse.quote(text)
  page=requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/"+textf)
  data = json.loads(page.content)
  if type(data) == type([]):
      data = data[0]
      word = data["word"]
      description = "**Results : **\n\n"
      if "phonetics" in data.keys():
          if "text" in data["phonetics"][0]:
              phonetics = (
                  "**Phonetics:**\n" + data["phonetics"][0]["text"] + "\n\n"
              )
              description += phonetics
      if "origin" in list(data.keys()):
          origin = "**Origin: **" + data["origin"] + "\n\n"
          description += origin
      if "meanings" in data.keys() and "definitions" in data["meanings"][0]:
          meanings = data["meanings"][0]["definitions"][0]
          if "definition" in list(meanings.keys()):
              meaning = "**Definition: **" + meanings["definition"] + "\n\n"
              description += meaning
          if "example" in list(meanings.keys()):
              example = "**Example: **" + meanings["example"]
              description += example
  else:
      word = data["title"]
      description = data["message"]
  embed=discord.Embed(title=word,
    description=description,color=discord.Color.dark_theme())
  await ctx.send(embed=embed)
@client.command(name="eval",hidden=True)
@commands.is_owner()
async def _eval(ctx, *, code):
    env = {
        "ctx": ctx,
        "discord": discord,
        "commands": commands,
        "bot": ctx.bot,
        "client":ctx.bot,
        "__import__": __import__,
        "guild":ctx.guild
    }
    code = code.replace("```py", "")
    code = code.replace("```", "")
    if "bot.http.token" in code or "client.http.token" in code:
        return await ctx.reply(f"You can't take my token , huh {ctx.author.name}")

    splitcode = []
    
    for line in code.splitlines():
        splitcode.append(line)
    
    try:
        compile(splitcode[len(splitcode)-1],"<stdin>","eval")
        splitcode[len(splitcode)-1] = f"return {splitcode[len(splitcode)-1]}"
    except:
        pass
    
    parsedcode = []

    for line in splitcode:
        parsedcode.append("  "+line)

    parsedcode = "\n".join(parsedcode)

    fn = f"async def eval_fn():\n{parsedcode}"

    exec(fn,env)

    try:
        output = (await eval("eval_fn()",env))
        ecolor = discord.Color.green()
        outname = "Output"
    except Exception as error:
        output = error.__class__.__name__+": "+str(error)
        ecolor = discord.Color.red()
        outname = "Error"

    embed = discord.Embed(title="Eval",description="```\n"+str(output)+"\n```",colour=ecolor)
    try:
      
      embed.add_field(name="Input",value="```py\n"+code+"\n```",inline=False)
    except:
      embed.add_field(name="Input",value="Too large to fit here",inline=False)
    #embed.add_field(name=outname,value="```\n"+str(output)+"\n```",inline=False)
    embed.set_author(name=ctx.author.display_name,icon_url=ctx.author.avatar_url)
    await ctx.reply(embed=embed)

@client.command(aliases=['namaste','hi','bonjour'],hidden=True) 
async def hello(ctx):
  #test 
  em = discord.Embed(title="Hi", description=f" Namaste  ,Hi , Bonjour 🙏  {ctx.author.mention}", color=discord.Color.green())
  em.set_image(url="https://media2.giphy.com/media/SbKNFpFZEumGTkgPgA/giphy.gif?cid=ecf05e47bhxa7graukqo2r3o6o83x9a3wja60ym4y9rmud4o&rid=giphy.gif&ct=g")
#no errors ok to move on checked 2nd error nothing useful 
  await ctx.channel.send(embed = em)

@client.command(aliases=['supportserver','githubrepo','src','invite','website','vote'])
async def links(ctx):
    row = ActionRow(
        Button(
            style=ButtonStyle.link,
            label="Invite !",
            url='https://discord.com/api/oauth2/authorize?client_id=916630347746250782&permissions=8&scope=bot&applications.commands',
            emoji='<:Info:939018353396310036>'
        ),
        Button(
            style=ButtonStyle.link,
            label="Support!",
            url='https://discord.gg/avpet3NjTE',
            emoji="<a:devserver:930350030072729620>"
        ),        
        Button(
            style=ButtonStyle.link,
            label="Github Src!",
            url='https://github.com/prakarsh17/tessarect-bot',
            emoji="<:github:912608431230320660>"
        ),
        Button(
            style=ButtonStyle.link,
            label="Website!",
            url='https://bit.ly/tessarect-website',
            emoji="<:planet:930351400532201532>"
        ),       
        Button(
            style=ButtonStyle.link,
            label="Vote !",
            url='https://top.gg/bot/916630347746250782/vote',
            emoji="<:heart:939018192498593832>"
        ),

    )   
    links_dict={"invite":"https://discord.com/api/oauth2/authorize?client_id=916630347746250782&permissions=8&scope=bot&applications.commands",
               "githubrepo":"https://github.com/prakarsh17/tessarect-bot",
               "src":"https://github.com/prakarsh17/tessarect-bot",
               "website":"https://bit.ly/tessarect-website",
               "vote":"https://top.gg/bot/916630347746250782/vote",
               "support server":"https://discord.gg/avpet3NjTE"}
    embed=discord.Embed(title=ctx.message.content[len("a!"):].split()[0].upper(),description="Important Links ",color=0xFFC0CB,timestamp=ctx.message.created_at)
    embed.set_footer(text="Stay Safe and be happy and keep using Me !")
    for x in links_dict:
      if str(ctx.message.content[len("a!"):].split()[0])== x:
        embed.add_field(name="Link",value=f"{x.upper()} - {links_dict[x]}")
    embed.set_thumbnail(url=client.user.avatar_url)
    await ctx.reply(embed=embed,components=[row])


    
  #e = discord.Embed()
ser = []

from requests import PreparedRequest
@client.command(pass_context=True)
@commands.has_permissions(administrator=True) #ensure that only administrators can use this command
async def setwelcomechannel(ctx,channel:discord.TextChannel,*,txt=None): 
    with open('storage/welcome.json', 'r') as f:
        wel = json.load(f)
    wel[str(ctx.guild.id)] = [int(channel.id),txt]

      
   

    with open('storage/welcome.json', 'w') as f: #writes the new prefix into the .json
        json.dump(wel, f, indent=4)

    await ctx.reply(f'Changed welcome channel to {channel}') #confirms the prefix it's been changed to

# ...

@client.event
async def on_member_join(member):
    with open('storage/welcome.json', 'r') as f:
        wel = json.load(f)  
    if str(member.guild.id) not in wel:
        return
    channel = client.get_channel(wel[str(member.guild.id)][0])
    if channel==None:
      return print('not set')
    embed = discord.Embed(colour=discord.Colour.blue(),description=wel[str(member.guild.id)][1])
    name=member.display_name.split()
    finalname='+'.join(name)
    link=f"https://api.popcat.xyz/welcomecard?background=https://cdn.discordapp.com/attachments/850808002545319957/859359637106065408/bg.png&text1={finalname}&text2=Welcome&text3=#+{str(len(ctx.guild.members))}+Member&avatar={str(member.avatar_url_as(format='png'))}"
    embed.set_image(url=link)
    await channel.send(embed=embed)    

@client.event
async def on_member_remove(member):
    with open('storage/welcome.json', 'r') as f:
        wel = json.load(f)  
    if str(member.guild.id) not in wel:
        return
    channel = client.get_channel(wel[str(member.guild.id)][0])
    if channel==None:
      return print('not set')
    embed = discord.Embed(colour=discord.Colour.blue(),description=f"{member} left")
    name=member.display_name.split()
    finalname='+'.join(name)
    link=f"https://api.popcat.xyz/welcomecard?background=https://media.discordapp.net/attachments/929332390432735243/945522028985872424/9k.png&text1={finalname}&text2=Left&text3=Hope+They+had+a+Good+time+and+maybe+join+back&avatar={str(member.avatar_url_as(format='png'))}"
    embed.set_image(url=link)
    await channel.send(embed=embed)    


@client.command()
async def meme(ctx):
    page = requests.get(f'https://api.popcat.xyz/meme')
    d = json.loads(page.content)
    title=d['title']
    img=d['image']
    url=d['url']
    like = d['upvotes']
    comm=d['comments']
    embed = discord.Embed(title=title,url=url,color=0x34363A)
    embed.set_image(url=img)
    embed.set_footer(text=f"👍🏻{like} 💬 {comm} ")
    await ctx.reply(embed=embed)




def searchyt(song):
    music_name = song
    query_string = urllib.parse.urlencode({"search_query": music_name})
    formatUrl = urllib.request.urlopen("https://www.youtube.com/results?" + query_string)
    search_results = re.findall(r"watch\?v=(\S{11})", formatUrl.read().decode())
    clip2 = "https://www.youtube.com/watch?v=" + "{}".format(search_results[0])
    return clip2

@client.command()
async def yt(ctx, *, url):
    await ctx.reply(searchyt(url))

import platform





os.system('pip install google bs4')
@client.command()
async def google(ctx, *, query):
    import google , bs4
    e=discord.Embed(description="Here are some results",color=discord.Color.random())
    from googlesearch import search # pip install google, bs4
    for j in search(query, tld="co.in", num=1, stop=5, pause=2):
        e.add_field(name="_ _",value=j) 
    await ctx.reply(embed=e)




    
    #
 
# ---------------------------------------------------------------------------------------

 

@client.command()
async def lyrics(ctx, *, song):
    from lyrics_extractor import SongLyrics

    sc = SongLyrics('AIzaSyCBc9vGiM-q0dIOpt0mSIdhraUGiF1pU_U', '2c0e4a26e5d598f41')
    js = sc.get_lyrics(
        song
    )
    em = discord.Embed(title=js["title"], description=js["lyrics"], color=discord.Color.dark_grey())
    await ctx.reply(embed=em)












 
























mainshop = [{"name":"Watch","price":100,"description":"Watch Time","emoji":'<a:watchx:920617389618503730>','com':'Very Common'},
            {"name":"Laptop","price":1000,"description":"Do work and gain money(under progress)","emoji":"💻",'com':'Very Common'},
            {"name":"PC","price":10000,"description":"PLay some games and get money(under progress)","emoji":"🖥️",'com':'Very Common'},
            {"name":"Ferrari","price":99999,"description":"Race with others(under progress)","emoji":"🚗",'com':'Very Common'},
            {"name":"Kingpass","price":1000000000,"description":"Only for kings , Are you one?","emoji":'<:crownx:920620263584960533>','com':'Very Common'},
            {"name":"Shovel","price":1650,"description":"Dig and have some luck of gaining something","emoji":"<:shovel:920616784648888320>",'com':'Very Common'},
            {"name":"Fishingrope","price":12340,"description":"Fish fish(under progress)","emoji":"<a:fishing:920625284435292171>",'com':'Very Common'},
            {"name":"Juice","price":1013,"description":"Drink some Juice and enjoy some free coins","emoji":"<:juice:920625284854726686>",'com':'Very Common'},
            {"name":"Rope","price":500,"description":"Rope","emoji":"",'com':'Very Common'},
            {"name":"Ink","price":220,"description":"Scrible ","emoji":"",'com':' Common'}]

weapons=[{"name":"Phasing_Bow","price":100000000000000,"short":"his flexible bow is made from the chitinous legs of a phase spider and retains some of its ethereal properties. ","description":"This flexible bow is made from the chitinous legs of a phase spider and retains some of its ethereal properties. The bow has 5 charges and regains all expended charges daily at dawn. When you make a ranged attack roll with this magic bow, you can expend 1 of its charges to cause the arrow to slip partially into the Ethereal Plane. When you do, the target of the attack gains no benefit from cover, including total cover, as long as the cover isn't made of lead or more than 1 foot thick. If you hit, the target takes an extra 2d6 force damage. Any effect that blocks travel through the Ethereal Plane also blocks the arrow. Alternatively, you can speak the bow's command word as a bonus action to expend 3 of its charges and fire an arrow at a point you can see within the weapon's normal range. When the arrow hits a solid surface, you vanish from your location and reappear in an unoccupied space nearest to that point.**Oh, you're not getting away that easily.**","emoji":"",'com':'Epic Rare'},
{"name":"Pride_Armor","price":100000000000000,"short":"This well-crafted leather armor comes with a sturdy, enveloping longcoat, bearing on its back the insignia of a well-known pirate captain","description":"This well-crafted leather armor comes with a sturdy, enveloping longcoat, bearing on its back the insignia of a well-known pirate captain. When you attune to it, the insignia changes to one that represents you instead. While wearing this armor, climbing and swimming don't cost you extra movement, and you can breathe underwater.Use this for protecting yourself from Robs etc","emoji":"",'com':'Epic Rare'}]

bundles=[{"name":"DiplomatPack","items":"Includes a chest, 2 cases for maps and scrolls, a set of fine clothes, a bottle of ink, an ink pen, a lamp, 2 flasks of oil, 5 sheets of paper, a vial of perfume, sealing wax, and soap.**","emoji":"",'com':' lEGENDARY ePic',"price":12000}]
with open("mainbank.json") as file:
    bank = json.load(file)
async def open_ter( id : int):
        newuser = {"id": id, "terrabux": 0}
        # wallet = current money, bank = money in bank
        await ecomoney.insert_one(newuser) 

#@slashx.slash(name="balance")
@client.command(aliases=['bal'])
async def balance(ctx ,user: discord.Member = None):

  if user is None:

    user = ctx.author
  bal = await ecomoney.find_one({"id": user.id})
  if bal is None:
      await open_ter(user.id)
      bal = await ecomoney.find_one({"id": user.id})
  #test
  await open_account(user)


  users = await get_bank_data()

  wallet_amt = users[str(user.id)]["wallet"]

  bank_amt = users[str(user.id)]["bank"]
  em = discord.Embed(title=f'{user.name} Balance',color = 0x0437F2,timestamp=ctx.message.created_at)
  em.add_field(name="Wallet Balance", value=f'֍{wallet_amt:,}')
  em.add_field(name='Bank Balance',value=f'֍{bank_amt:,}')
  em.set_thumbnail(url=user.avatar_url)
  em.add_field(name='Terrabux',value=f"<a:Diamond:930350459020017694>{bal['terrabux']}",inline=False)

  tot = bank_amt+wallet_amt+(bal['terrabux']*10)
  em.set_footer(text=f"🤨 {tot}")        
  msg=await ctx.reply(embed= em)


import string    
hacking_status = ['breaching mainframe', 'accessing CPU pins', 'a couple gigabytes of RAM','Accessing Ip adress ','Getting Os info']
osd = ['unkown windows','windows 11','unknown linux','mac','arch','calinix','windows xp','andriod 2','andriod 12','A poor os ']
 
 
@client.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def beg(ctx):
    await open_account(ctx.author)
    user = ctx.author

    users = await get_bank_data()

    earnings = random.randrange(400)
    em = discord.Embed(title =random.choice(names),description =f'Gave {ctx.author.mention} ֍ {earnings} ',color = discord.Color.green())
    await ctx.reply(embed=em)

    users[str(user.id)]["wallet"] += earnings

    with open("mainbank.json",'w') as f:
        json.dump(users,f)
@client.command(hidden=True)
@commands.is_owner()
async def max_bal(ctx):

    await open_account(ctx.author)
    user = ctx.author

    users = await get_bank_data()

    earnings = 100000000

    em = discord.Embed(title =' Max Command',description =f'Maxed Money {earnings}',color = discord.Color.green())
    await ctx.reply(embed=em)

    users[str(user.id)]["bank"] += earnings

    with open("mainbank.json",'w') as f:
        json.dump(users,f)




# JOB COMMANDS  ## 
### CURRENCY COMMANDS  ###

cashier_employers = ['Lidl', 'Aldi', 'Sainsbury\'s', 'Morrison\'s', 'Tesco', 'Premier', 'Londis']
fastfood_employers = ['KFC', 'McDonalds', 'Subway', 'Taco Bell']
stocker_employers = ['Halford\'s', 'B&Q', 'Ikea', 'The Range', 'Home Bargain\'s']
dev_epy=['MiS','lINux','OMac','Discord']
victims = ['a blind woman', 'a blind man', 'a dog', 'a business person', 'a furry', 'Jeff Bezos', 'Patrick Gaming']
sucess_phrases = ['got away with the cash', 'ran away with the cash', 'ran away with the money', 'got away with the money']
fail_phrases = ['was beaten up', 'got sucker punched', 'was knocked out', 'was stabbed', 'was caught']




@client.group(aliases=['job'],invoke_without_command=True)
async def findjob(ctx):
    await open_account(ctx.author)

    job_menu = discord.Embed(title='The Job Centre :money_with_wings:', color=0xd400ff)
    job_menu.add_field(name='Cashier', value=f'Wage - {m}1 Per Work\nEmployer - {random.choice(cashier_employers)}', inline=True)
    job_menu.add_field(name='Fastfood Cook', value=f'Wage - {m}3 Per Work\nEmployer - {random.choice(fastfood_employers)}', inline=True)
    job_menu.add_field(name='Shelf Stocker', value=f'Wage - {m}2 Per Work\nEmployer - {random.choice(stocker_employers)}', inline=True)
    job_menu.add_field(name='Python Developer', value=f'Wage - {m}6 Per Work\nEmployer - {random.choice(dev_epy)}', inline=True)
    job_menu.set_footer(text=f'Use {" or ".join(prefix_check(ctx.message.guild))}apply <job> title to get started.')

    await ctx.reply(embed=job_menu)
@findjob.command()
@commands.cooldown(1, 2000, commands.BucketType.user)
async def resign(ctx):
    await open_account(ctx.author)

    with open(r'mainbank.json', 'r') as f:
            user_info = json.load(f)
    
    await ctx.reply(f'YOU RESIGNED now u have no work to do')
    user_info[str(ctx.author.id)]['career']='None'

    with open(r'mainbank.json', 'w') as f:
        json.dump(user_info, f)   
@client.command()
async def apply(ctx, *, title: str):
    await open_account(ctx.author)

    with open(r'mainbank.json', 'r') as f:
            user_info = json.load(f)

    if title.lower() == 'cashier':
        title = 'Cashier'
    elif title.lower() == 'fastfood cook' or title.lower() == 'cook':
        title = 'Fastfood Cook'
    elif title.lower() == 'stocker' or title.lower() == 'shelf stocker':
        title = 'Shelf Stocker'
    elif title.lower() == 'python' or title.lower() == 'python developer':
        title = 'Python Developer'
    else: # job not found
        title = ''
    
    if title != '':
        user_info[str(ctx.author.id)]['career'] = title
        await ctx.reply(embed=discord.Embed(title='Interview Passed :money_with_wings:', description=f'{ctx.author.name} started a job as a {title}. Type {" or ".join(prefix_check(ctx.message.guild))}work to begin.', color=0xd400ff))

        with open(r'mainbank.json', 'w') as f:
            json.dump(user_info, f)
async def add_money(author, amount):
        with open(r'mainbank.json', 'r') as f:
            user_info = json.load(f)

        user_info[str(author.id)]['wallet'] += amount

        with open(r'mainbank.json', 'w') as f:
            json.dump(user_info, f)

async def work_embed(ctx, action, value):
    embed = discord.Embed(
        colour=0xd400ff,
        title=f"{action} :money_with_wings:",
    )

    embed.add_field(name="Pay", value=f"``{m}{value}``")
    embed.add_field(name="Recognition", value=f"``{random.randint(1,100)}%``")

    await add_money(ctx.author, value)
    await ctx.channel.send(embed=embed)

@client.command()
@commands.cooldown(1, 200, commands.BucketType.user)
async def work(ctx):
    await open_account(ctx.author)

    with open(r'mainbank.json', 'r') as f:
            user_info = json.load(f)

    if user_info[str(ctx.author.id)]['career'] == 'Fastfood Cook':
        await work_embed(ctx, 'Burger Flipped', 3)
    elif user_info[str(ctx.author.id)]['career'] == 'Cashier':
        await work_embed(ctx, 'Shopping Scanned', 1)
    elif user_info[str(ctx.author.id)]['career'] == 'Shelf Stocker':
        await work_embed(ctx, 'Shelf Stacked', 2)
    elif user_info[str(ctx.author.id)]['career'] == 'Python Developer':
        await work_embed(ctx, 'Module Made', 6)
    else:
        x = discord.Embed(title="No work fool",description='DUMBASS u dont have a work to do , use job command to find one')
        await ctx.reply(embed=x)
intervals = (
    ('weeks', 604800),  # 60 * 60 * 24 * 7
    ('days', 86400),    # 60 * 60 * 24
    ('hours', 3600),    # 60 * 60
    ('minutes', 60),
    ('seconds', 1),
)

def display_time(seconds, granularity=2):
    result = []

    for name, count in intervals:
        value = seconds // count
        if value:
            seconds -= value * count
            if value == 1:
                name = name.rstrip('s')
            result.append("{} {}".format(value, name))
    return ', '.join(result[:granularity]) 

import requests
api_key = "c525a3540cb35084c1283ca6252387bd"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
@client.command()
async def weather(ctx, *, city: str):
    city_name = city
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    channel = ctx.message.channel
    if x["cod"] != "404":
        async with channel.typing():
            y = x["main"]
            current_temperature = y["temp"]
            current_temperature_celsiuis = str(round(current_temperature - 273.15))
            current_pressure = y["pressure"]
            current_humidity = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            weather_description = z[0]["description"]
            embed = discord.Embed(title=f"Weather in {city_name}",
                              color=ctx.guild.me.top_role.color,
                              timestamp=ctx.message.created_at,)
            embed.add_field(name="Descripition", value=f"**{weather_description}**", inline=False)
            embed.add_field(name="Temperature(C)", value=f"**{current_temperature_celsiuis}°C**", inline=False)
            embed.add_field(name="Humidity(%)", value=f"**{current_humidity}%**", inline=False)
            embed.add_field(name="Atmospheric Pressure(hPa)", value=f"**{current_pressure}hPa**", inline=False)
            embed.set_thumbnail(url="https://i.ibb.co/CMrsxdX/weather.png")
            embed.set_footer(text=f"Requested by {ctx.author.name}")
        await channel.send(embed=embed)
    else:
        await channel.send("City not found.") 
 


async def open_streak(user):

    await open_account(user)
    users = await get_bank_data()

    with open('streak.json','r') as f:

      strx = json.load(f)

    if str(user.id) in strx:
        return False
    else:
        now = datetime.now()
        last_claim_stamp = str(now.timestamp())
        last_claim=datetime.fromtimestamp(float(last_claim_stamp))
        earnings = 50500
        strx[str(user.id)] = {}
        strx[str(user.id)]["streak"] = 1
        strx[str(user.id)]["last_claim"] = last_claim_stamp     
        users[str(user.id)]["wallet"] += earnings

        with open("mainbank.json",'w') as f:
            json.dump(users,f)
        #with open("mainbank.json",'w') as f:
            #json.dump(users,f)  
    
    with open('streak.json','w') as f:
        json.dump(strx,f)
    await user.send('yOU HAVE GOt your daily + monthly, dont go on the message which says you already claimed your daily , your amount has been credited too , this issue is know and is under development')
    return True    
import datetime
from datetime import datetime, timedelta                                              
@client.command()
async def daily(ctx):

  await open_streak(ctx.author)
  user = ctx.author
  users = await get_bank_data()
  '''UNDER WORK DONT USE THIS COMMAND'''
  with open ("streak.json","r") as f:
    data = json.load(f)
  streak=data[f"{ctx.author.id}"]["streak"]
  last_claim_stamp=data[f"{ctx.author.id}"]["last_claim"]
  last_claim=datetime.fromtimestamp(float(last_claim_stamp))
  now  =datetime.now() 
  delta = now-last_claim 
  print(f"{streak}\n{last_claim_stamp}\n{last_claim}\n{now}\n{delta}") 
  if delta< timedelta(hours=24):
    await ctx.reply(f'YOU ALREADY CLAIMED YOUR DAILY in 24 hours , your last claim was on <t:{round(int(float(last_claim_stamp)))}>')
    return
  if delta > timedelta(hours=48):
    print('streak reset')
    streak = 1
  else:
    streak+=1   
  daily = 500+(streak*5) 
  data[f'{ctx.author.id}']["streak"]=streak
  data[f'{ctx.author.id}']["last_claim"]= str(now.timestamp())
  with open("streak.json","w") as f:
    json.dump(data,f,indent=2)
  embed = discord.Embed(title="Daily", colour=random.randint(0, 0xffffff), description=f"You've claimed your daily of **{daily}** \n ")
  embed.set_footer(text=f"Your daily streak : {streak}")
  users[str(user.id)]["wallet"] += daily

  with open("mainbank.json",'w') as f:
      json.dump(users,f)
  await ctx.reply(embed=embed)

@client.command(aliases=['wd','with'])
async def withdraw(ctx,amount = None):
    #test
    await open_account(ctx.author)
    if amount is None:
        await ctx.reply("Please enter the amount")
        return

    bal = await update_bank(ctx.author)
    if amount in ("all", "max"):

      amount = int(bal[1])
        
    amount = int(amount)

    if amount > bal[1]:
      
        ex= discord.Embed(description='You do not have sufficient balance')
        await ctx.reply(embed=ex)
        return
    if amount < 0:
        ex= discord.Embed(description='Amount must be positive!')
        await ctx.reply(embed=ex)      

        return

    await update_bank(ctx.author,amount)
    await update_bank(ctx.author,-1*amount,'bank')
    await ctx.reply(f'{ctx.author.mention} You withdrew {amount} coins')


@client.command(aliases=['dp','dep'])
async def deposit(ctx,amount = None):
    #test
    await open_account(ctx.author)
    if amount is None:
        await ctx.reply("Please enter the amount")
        return

    bal = await update_bank(ctx.author)
    if amount in ("all", "max"):

      amount = int(bal[0])
   
    amount = int(amount)

    if amount > bal[0]:
        await ctx.reply('You do not have sufficient balance')
        return
    if amount < 0:
        await ctx.reply('Amount must be positive!')
        return



    await update_bank(ctx.author,-1*amount)
    await update_bank(ctx.author,amount,'bank')
    await ctx.reply(f'{ctx.author.mention} You deposited {amount} coins')





@client.command(aliases=['sm'])
async def send(ctx,member : discord.Member,amount = None):
    await open_account(ctx.author)
    await open_account(member)
    if amount == None:
        await ctx.reply("Please enter the amount")
        return

    bal = await update_bank(ctx.author)
    if amount == 'all':
        amount = bal[0]

    amount = int(amount)

    if amount > bal[0]:
        await ctx.reply('You do not have sufficient balance')
        return
    if amount < 0:
        await ctx.reply('Amount must be positive!')
        return

    await update_bank(ctx.author,-1*amount,'wallet')
    await update_bank(member,amount,'bank')
    await ctx.reply(f'{ctx.author.mention} You gave {member} {amount} coins')

def convert(time):
    pos = ["s", "m", "h", "d"]

    time_dict = {"s": 1, "m": 60, "h": 3600, "d": 3600 * 24}

    unit = time[-1]

    if unit not in pos:
        return -1
    try:
        val = int(time[:-1])
    except:
        return -2

    return val * time_dict[unit]


# ---------------------------------------------------------------------------

from random import randint
@client.command(aliases=['rb'])
@commands.cooldown(1, 60, commands.BucketType.user)
async def rob(ctx,member : discord.Member):
  aut = ctx.author
  if  member == ctx.author  or member.bot or member.status == discord.Status.offline:
    #await ctx.reply('hey stupid, why r u either robbing urself or a bot or a offline person now u might have to payback')
    if member.status == discord.Status.offline:

      await open_account(ctx.author)
      await open_account(member)
      bal = await update_bank(aut)
      earningd = random.randrange(0,bal[0])
  

      await update_bank(member,earningd)
      await update_bank(ctx.author,-1*earningd) 
      await update_bank(member,+1*earningd) 
      await ctx.reply(f"You got caught while robbing {member} , and u payed them {earningd}.BE more pro next time :/")      

    return


  users = await get_bank_data()
  bag = users[str(member.id)].get("bag")


  if bag:
      if any(element['item'] == 'pride_armor' and element['amount'] > 0
            for element in bag): 
              return await ctx.reply(f'You tried to rob **{member}**, but they had a **Pride_Armor**🛡. Try again next time.')
  await open_account(ctx.author)
  await open_account(member)
  bal = await update_bank(member)

  if bal[0]<100:
    await ctx.reply('It is useless to rob them :(')
    return

  earning = random.randrange(0,bal[0])
  

  await update_bank(ctx.author,earning)
  await update_bank(member,-1*earning)
  em = discord.Embed(title =f'{ctx.author} robbed {member}',description =f'{ctx.author.mention}  robbed {member} and got {m}{earning} ')
  emd = discord.Embed(title =f'{ctx.author} tried to robb You',description =f'{ctx.author}  tried to rob {member} and got {m}{earning} ')
  await ctx.reply(embed=em)
  await member.send(embed=emd)

@client.command()
@commands.guild_only()
@commands.cooldown(rate=1, per=3.0, type=commands.BucketType.user)
async def slots( ctx, bet: int):
    await open_account(ctx.author)
    bal = await update_bank(ctx.author)
    amount = int(bet)

    if amount > bal[0]:
        await ctx.reply('You do not have sufficient balance')
        return
    if amount < 0:
        await ctx.reply('Amount must be positive!')
        return    
    if 1 > bet:
        return await ctx.reply("Give some money! ;w;")

    losshearts = [ "💔"]
    doublehearts = ["❤️", "💚", "💛", "🧡", "💜", "💙","🖤",]
    triplehearts = ["💗", "💖","💟","🤎"]
    jackpothearts = ["💘"]
    hearts = {}
    heartlist = ["❤️", "🖤", "💗", "💚", "💖", "💛", "💔", "🧡", "💜", "💙", "💘","💟","🤎"]
    for x in range(1, 10):
        hearts[f"heart{x}"] = random.choice(heartlist)
    msg = await ctx.reply(
        f"```\n{hearts['heart1']}{hearts['heart2']}{hearts['heart3']}\n{hearts['heart4']}{hearts['heart5']}{hearts['heart6']}\n{hearts['heart7']}{hearts['heart8']}{hearts['heart9']}\n```"
    )
    if hearts["heart4"] == hearts["heart5"] == hearts["heart6"]:
        if hearts["heart4"] in losshearts:
            multiplier = 0
        if hearts["heart4"] in doublehearts:
            multiplier = 2
        if hearts["heart4"] in triplehearts:
            multiplier = 3
        if hearts["heart4"] in jackpothearts:
            multiplier = 10
    else:
        multiplier = 0
    msg = await ctx.channel.fetch_message(msg.id)
    await msg.edit(
        content=f"{msg.content}\nAnd you got a multiplier of {multiplier}!"
    )
    betresult = int(bet * multiplier)
    if multiplier == 0:
        await update_bank(ctx.author,-1*amount)
    else:
        await update_bank(ctx.author,1*betresult)
    
import DiscordUtils 
@client.group(invoke_without_command=True)
async def shop(ctx):
    #test
    em1 = discord.Embed(title = "Shop")

    for item in mainshop:
        name = item["name"]
        price = item["price"]
        desc = item["description"]
        emoji=item["emoji"]
     
        em1.add_field(name = f'{emoji} {name} - {m}{price:,} ', value = f"  \n {desc}",inline=False)
    em2=discord.Embed(title="Weapons",description="Some weapons")


    for item in weapons:
        name = item["name"]
        price = item["price"]
        desc = item["short"]
        emoji=item["emoji"]
        com=item["com"]           
        em2.add_field(name = f'{emoji} {name} - {price:,}', value = f" \n {desc}\nRarity : {com}",inline=False)
    em3=discord.Embed(title="Bundles",description="Some bundles you cant buy")


    for item in bundles:
        name = item["name"]
        desc = item["items"]
        emoji=item["emoji"]
        com=item["com"]           
        em3.add_field(name = f'{emoji} {name}', value = f" \n {desc}\nRarity : {com}",inline=False)        
    paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx,remove_reactions=True)
    embeds = [em1, em2, em3]
    paginator.add_reaction('⏮️', "first")
    paginator.add_reaction('⏪', "back")
    paginator.add_reaction('🗑', "lock")
    paginator.add_reaction('⏩', "next")
    paginator.add_reaction('⏭️', "last")
    await paginator.run(embeds)

@client.command()
async def buy(ctx,item,amount = 1):
    #test
    await open_account(ctx.author)

    res = await buy_this(ctx.author,item,amount)

    if not res[0]:
        if res[1]==1:
            await ctx.reply("That Object isn't there!")
            return
        if res[1]==2:
            await ctx.reply(f"You don't have enough money in your wallet to buy {amount} {item}")
            return

    buy = discord.Embed(title=item,description=f"You bought {amount} {item}",color=discord.Color.green())
    await ctx.reply(embed=buy)

@client.command(aliases =['inventory','inv'])
async def bag(ctx,user:discord.Member = None):
  #test
  if user ==None:

    await open_account(ctx.author)
    user = ctx.author
    users = await get_bank_data()

    try:
        bag = users[str(user.id)]["bag"]
    except:
        bag = []


    em = discord.Embed(title = "Bag")
    for item in bag:
        name = item["item"]
        amount = item["amount"]

        em.add_field(name = f'{name}', value = amount)    

    await ctx.reply(embed = em)
  else:

    await open_account(ctx.author)

    users = await get_bank_data()

    try:
        bag = users[str(user.id)]["bag"]
    except:
        bag = []


    em = discord.Embed(title = "Bag")
    for item in bag:
        name = item["item"]
        amount = item["amount"]

        em.add_field(name = name, value = amount)    

    await ctx.reply(embed = em)    


async def buy_this(user,item_name,amount):
    item_name = item_name.lower()
    name_ = None
    for item in mainshop:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            price = item["price"]

            break
    for item in weapons:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            price = item["price"]

            break
    if name_ == None:
        return [False,1]

    cost = price*amount

    users = await get_bank_data()

    bal = await update_bank(user)

    if bal[0]<cost:
        return [False,2]


    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["bag"]:
            n = thing["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt + amount
                users[str(user.id)]["bag"][index]["amount"] = new_amt
                t = 1
                break
            index+=1 
        if t == None:
            obj = {"item":item_name , "amount" : amount}
            users[str(user.id)]["bag"].append(obj)
    except:
        obj = {"item":item_name , "amount" : amount}
        users[str(user.id)]["bag"] = [obj]        

    with open("mainbank.json","w") as f:
        json.dump(users,f)

    await update_bank(user,cost*-1,"wallet")

    return [True,"Worked"]
    

@client.command()
async def sell(ctx,item,amount = 1):
    await open_account(ctx.author)

    res = await sell_this(ctx.author,item,amount)

    if not res[0]:
        if res[1]==1:
            await ctx.reply("That Object isn't there!")
            return
        if res[1]==2:
            await ctx.reply(f"You don't have {amount} {item} in your bag.")
            return
        if res[1]==3:
            await ctx.reply(f"You don't have {item} in your bag.")
            return
    s = discord.Embed(title = "Sold",description =f"You just sold {amount} {item}",color=discord.Color.green())
    await ctx.reply(embed=s)

async def sell_this(user,item_name,amount,price = None):
    item_name = item_name.lower()
    name_ = None
    for item in mainshop:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            if price==None:
                price = 0.7* item["price"]
            break
    for item in weapons or bundles:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            if price==None:
                price = 0.7* item["price"]
            break
    if name_ == None:
        return [False,1]

    cost = price*amount

    users = await get_bank_data()

    bal = await update_bank(user)


    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["bag"]:
            n = thing["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt - amount
                if new_amt < 0:
                    return [False,2]
                users[str(user.id)]["bag"][index]["amount"] = new_amt
                t = 1
                break
            index+=1 
        if t == None:
            return [False,3]
    except:
        return [False,3]    

    with open("mainbank.json","w") as f:
        json.dump(users,f)

    await update_bank(user,cost,"wallet")
    print(price)
    return [True,"Worked"]


  

async def open_account(user):

    users = await get_bank_data()

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["wallet"] = 250
        users[str(user.id)]["bank"] = 0
        users[str(user.id)]['career'] = 'None'
        users[str(user.id)]['rank'] = 'None'
        users[str(user.id)]['loan'] = 'None'
        users[str(user.id)]['loan_amount'] = 'None'                    
    with open('mainbank.json','w') as f:
        json.dump(users,f)

    return True


async def get_bank_data():
    with open('mainbank.json','r') as f:
        users = json.load(f)

    return users


async def update_bank(user,change=0,mode = 'wallet'):
    users = await get_bank_data()
    
    users[str(user.id)][mode] += change
    #if users[str(user.id)][mode] <0:
      #users[str(user.id)][mode] =0
    with open('mainbank.json','w') as f:
        json.dump(users,f)
    bal = users[str(user.id)]['wallet'],users[str(user.id)]['bank']
    return bal
players = {}



@client.command(aliases = ["lb"])
async def globallb(ctx,x = 10):
    users = await get_bank_data()
    leader_board = {}
    total = []
    for user in users:
        name = int(user)
        total_amount = users[user]["wallet"] + users[user]["bank"]
        leader_board[total_amount] = name
        total.append(total_amount)

    total = sorted(total,reverse=True)    

    em = discord.Embed(title = f"Top {x} Richest People" , description = "This is decided on the basis of raw money in the bank and wallet",color = discord.Color(0xfa43ee))
    index = 1
    for amt in total:
        id_ = leader_board[amt]
        member = client.get_user(id_)
        name = member
        em.add_field(name = f"{index}. {name}" , value = f"{amt}",  inline = False)
        if index == x:
            break
        else:
            index += 1

    await ctx.reply(embed = em)






@client.command()
async def ss(ctx, site):
    embed=discord.Embed(description="Here is the website'ss you requested",colour = discord.Colour.orange(), timestamp=ctx.message.created_at)
    embed.set_footer(text="WE got some reports that images dont load in embed so they will be sent seperately so please wait for few seconds so image can load")
    embed.set_image(url=(f"https://image.thum.io/get/width/1920/crop/675/maxAge/1/noanimate/{site}"))
    await ctx.reply(embed=embed)
    



player1 = ""
player2 = ""
turn = ""
gameOver = True

board = []

winningConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

def prefix_check(guild):
    # Check if this is a dm instead of a server
    # Will give an error if this is not added (if guild is None)
    if guild == None:
        return "!"
    try:
        # Check if the guild id is in your 'prefixes.json'
        with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)
            p = prefixes[str(guild.id)]
    except:
        # Otherwise, default to a set prefix
        p = "a!"
    # If you're confident that the guild id will always be in your json,
    # feel free to remove this try-except block

    return p
'''
# on_message event
@client.event
async def on_message(message):
  

  if f"<@!{client.user.id}>" or "<@&944855412979666984>" in message.content:
    
    if message.author.bot:
      return
    pr=", ".join(prefix_check(message.guild))
    emx = discord.Embed(title='Heyo',color=0xffffff)
      # This is how you call the prefix_check function. It takes a guild object
    emx.description = f'Tessarect\n<:arrow_right:940608259075764265> Another general purpose discord bot but with Economy commands and much more Well Attractive , Economy and Leveling Bot with tons of features. Utitlity Bot , Music Bot , Economy Bot , Moderation Bot and much more .\n<:blurple_slashcommands:930349698999537746> Prefix: {pr}'
    emx.add_field(name="**Seting Up**",value="<:arrow_right:940608259075764265> Type `[p]help` or mention bot to know prefix , do `[p]stats` for getting stats .`[p]setup` for basic configuration")
    #emx.add_field(name="Website",value="<:arrow_right:940608259075764265> [<:planet:930351400532201532> View](https://bit.ly/tessarect-website) Visit website and see our privacy policy and terms of service et ceter")
    #em.add_field()
    #em.add_field(name="Servers", value=len(client.guilds))
    emx.set_thumbnail(url=client.user.avatar_url)
    emx.set_author(name=client.user.display_name,icon_url=client.user.avatar_url,url="https://bit.ly/tessarect-website")
   
    await message.channel.send(embed=emx)
  await client.process_commands(message)
'''

@client.group()
async def tictactoe(ctx, p1: discord.Member, p2: discord.Member):
    #test
    global count
    global player1
    global player2
    global turn
    global gameOver
    if gameOver:
        global board
        board = [":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:"]
        turn = ""
        gameOver = False
        count = 0

        player1 = p1
        player2 = p2

        # print the board
        line = ""
        for x in range(len(board)):
            if x == 2 or x == 5 or x == 8:
                line += " " + board[x]
                await ctx.reply(line)
                line = ""
            else:
                line += " " + board[x]

        # determine who goes first
        num = random.randint(1, 2)
        if num == 1:
            turn = player1
            myEmbed = discord.Embed(title= "GAME IN PROGRESS",description="IT IS <@" + str(player1.id) + ">'s TURN.",color=0xe74c3c)
            await ctx.reply(embed=myEmbed)
        elif num == 2:
            turn = player2
            myEmbed = discord.Embed(title= "GAME IN PROGRESS",description="IT IS <@" + str(player2.id) + ">'s TURN.",color=0xe74c3c)
            await ctx.reply(embed=myEmbed)
    else:
        myEmbed = discord.Embed(title= "GAME IN PROGRESS",description="A GAME IS STILL IN PROGRESS. FINISH IT BEFORE STARTING A NEW ONE",color=0xe74c3c)
        await ctx.reply(embed=myEmbed)

@client.command()
async def place(ctx, pos: int):
    #test
    global turn
    global player1
    global player2
    global board
    global count
    global gameOver
    if not gameOver:
        mark = ""
        if turn == ctx.author:
            if turn == player1:
                mark = ":regional_indicator_x:"
            elif turn == player2:
                mark = ":o2:"
            if 0 < pos < 10 and board[pos - 1] == ":white_large_square:" :
                board[pos - 1] = mark
                count += 1

                # print the board
                line = ""
                for x in range(len(board)):
                    if x == 2 or x == 5 or x == 8:
                        line += " " + board[x]
                        await ctx.reply(line)
                        line = ""
                    else:
                        line += " " + board[x]

                checkWinner(winningConditions, mark)
                print(count)
                if gameOver == True:
                    myEmbed = discord.Embed(title= "WINNER!",description=mark + " :crown: ",color=0xf1c40f)
                    await ctx.reply(embed=myEmbed)
                elif count >= 9:
                    gameOver = True
                    myEmbed = discord.Embed(title= "TIE",description="IT'S A TIE :handshake:",color=0xf1c40f)
                    await ctx.reply(embed=myEmbed)

                # switch turns
                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1
            else:
                myEmbed = discord.Embed(title= "PLACE ERROR!",description="BE SURE TO CHOOSE AN INTEGER BETWEEN 1 AND 9 (INCLUSIVE) AND AN UNMARKED TILE. ",color=0xe74c3c)
                await ctx.reply(embed=myEmbed)
        else:
            myEmbed = discord.Embed(title= "TURN ERROR!",description="IT'S NOT YOUR TURN",color=0xe74c3c)
            await ctx.reply(embed=myEmbed)
    else:
        myEmbed = discord.Embed(title= "START GAME",description="TO START A NEW GAME, USE tictactoe COMMAND",color=0x2ecc71)
        await ctx.reply(embed=myEmbed)


def checkWinner(winningConditions, mark):
    global gameOver
    for condition in winningConditions:
        if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
            gameOver = True

@tictactoe.error
async def tictactoe_error(ctx, error):
    print(error)
    if isinstance(error, commands.MissingRequiredArgument):
        myEmbed = discord.Embed(title= "MENTION ERROR!",description="PLEASE MENTION 2 USERS",color=0xe74c3c)
        await ctx.reply(embed=myEmbed)
    elif isinstance(error, commands.BadArgument):
        myEmbed = discord.Embed(title= "ERROR!",description="PLEASE MAKE SURE TO MENTION/PING PLAYERS (ie. <@688534433879556134>)",color=0xe74c3c)
        await ctx.reply(embed=myEmbed)

@place.error
async def place_error(ctx, error):
    #test
    if isinstance(error, commands.MissingRequiredArgument):
        myEmbed = discord.Embed(title= "NO POSITION",description="PLEASE ENTER A POSITION TO MARK",color=0xe74c3c)
        await ctx.reply(embed=myEmbed)
    elif isinstance(error, commands.BadArgument):
        myEmbed = discord.Embed(title= "INTEGER ERROR!",description="PLEASE MAKE SURE IT'S AN INTEGER",color=0xe74c3c)
        await ctx.reply(embed=myEmbed)
@tictactoe.command()
async def end(ctx):
        #test
        # We need to declare them as global first
        global count
        global player1
        global player2
        global turn
        global gameOver
        
        # Assign their initial value
        count = 0
        player1 = ""
        player2 = ""
        turn = ""
        gameOver = True

        # Now print your message or whatever you want
        myEmbed = discord.Embed(title= "RESET GAME",description="TO START A NEW GAME, USE tictactoe COMMAND",color=0x2ecc71)
        await ctx.reply(embed=myEmbed)        


from asyncio import TimeoutError

@client.command()
async def joke(ctx): 

  page = requests.get('https://joke.deno.dev/')
  jokesource = json.loads(page.content)
  joke = jokesource['setup']
  print(joke)
  answer = jokesource['punchline']
  jembed=discord.Embed(description=f"**{joke}**\n{answer}",color=discord.Color.random()).set_footer(text=jokesource['type'])
  
  await ctx.channel.send(embed=jembed)

@client.command()
@commands.max_concurrency(1,per=commands.BucketType.default,wait=False)
async def fakename(ctx): 

  page = requests.get(f'https://api.namefake.com/')
  source = json.loads(page.content)
  name = source["name"]  
  address = source["address"]
  latitude = source["latitude"]  
  longitude = source["longitude"]  
  maiden_name = source["maiden_name"]  
  birth_data = source["birth_data"]  
  phone_h = source["phone_h"]  
  phone_w = source["phone_w"]  
  email_u = source["email_u"]  
  email_d = source["email_d"]  
  username = source["username"]
  password = source["password"]  
  domain = source["domain"]  
  useragent = source["useragent"]  
  ipv4 = source["ipv4"]  
  macaddress = source["macaddress"]  
  plasticcard = source["plasticcard"]  
  cardexpir = source["cardexpir"]  
  company = source["company"] 

  color = source["color"]
  uuid = source["uuid"]  
  height = source["height"]  
  weight = source["weight"]  
  blood = source["blood"]  
  eye = source["eye"]  
  hair = source["hair"]  
  pict = source["pict"]  
  url = source["url"]  
  sport = source["sport"]
  ipv4_url = source["ipv4_url"]  
  email_url = source["email_url"]  
  domain_url = source["domain_url"]  
  e = discord.Embed(title="Fake Name Generator",description=f"Here are some  generated info about a fake person . \n **Name : {name}**")   
  e.add_field(name="address",value=address,inline=False)
  e.add_field(name="latitude",value=latitude,inline=False)  
  e.add_field(name="longitude",value=longitude,inline=False) 
  e.add_field(name="maiden_name",value=maiden_name,inline=False)
  e.add_field(name="birth_data",value=birth_data,inline=False) 
  e.add_field(name="phone_h",value=phone_h,inline=False)
  e.add_field(name="phone_w",value=phone_w,inline=False) 
  e.add_field(name="email_u",value=email_u,inline=False)
  e.add_field(name="email_d",value=email_d,inline=False)   

  e.add_field(name="username",value=username,inline=False)
  e.add_field(name="password",value=password,inline=False)  
  e.add_field(name="password",value=password,inline=False)
  e.add_field(name="domain",value=domain,inline=False) 
  e.add_field(name="useragent",value=useragent,inline=False)
  e.add_field(name="ipv4",value=ipv4,inline=False) 
  e.add_field(name="macaddress",value=macaddress,inline=False)
  e.add_field(name="plasticcard",value=plasticcard,inline=False) 
  e.add_field(name="cardexpir",value=cardexpir,inline=False)
  e.add_field(name="company",value=company,inline=False)   
  e.add_field(name="color",value=color,inline=False)
  e.add_field(name="uuid",value=uuid,inline=False)  
  e.add_field(name="height",value=height,inline=False)
  e.add_field(name="weight",value=weight,inline=False) 
  e.add_field(name="blood",value=blood,inline=False)
  e.add_field(name="eye",value=eye,inline=False) 
  e.add_field(name="hair",value=hair,inline=False)
  e.add_field(name="pict",value=pict,inline=False) 
  e.add_field(name="url",value=url,inline=False)
  e.add_field(name="ipv4_url",value=company,inline=False)  
  e.add_field(name="email_url",value=email_url,inline=False)
  e.add_field(name="domain_url",value=domain_url,inline=False)      
  await ctx.channel.send(embed=e)  
@client.command()
async def getadvice(ctx):
    res = requests.get("https://api.senarc.org/misc/advice")
    source = json.loads(res.content)
    acti = source["text"]  

    em = discord.Embed(title=f"Advice", description=f"{acti}", color=discord.Color.blue())
    em.set_footer(text="Powered by Senarc API")
    await ctx.reply(embed=em)  
@client.command()
async def getidea(ctx):
    res = requests.get("https://www.boredapi.com/api/activity")
    source = json.loads(res.content)
    acti = source["activity"]  
    typ = source["type"]
    em = discord.Embed(title=f"Idea Generator", description=f"{acti}\n Type : {typ}", color=discord.Color.blue())
    await ctx.reply(embed=em)  
@client.command()
@commands.max_concurrency(1,per=commands.BucketType.default,wait=False)
async def fact(ctx): 
  page = requests.get(f'https://api.eriner.repl.co/fun/uselessfact')
  source = json.loads(page.content)
  ft = source["fact"] 
  em=discord.Embed(title="A Fact...",description=ft,color=discord.Color.random())
  await ctx.reply(embed=em)
@client.command(help="Shows info about a color by its hex")
@commands.max_concurrency(1,per=commands.BucketType.default,wait=False)
async def color(ctx,hex): 

  page = requests.get(f'https://api.eriner.repl.co/search/color?hex={hex}')
  source = json.loads(page.content)
  rgb = source["rgb"]
  hexx = source["hex"]
  name = source["name"]
  clean =source["clean"]
  img = source["image"]
  c = f"0x{clean}"
  print(c)
  emb = discord.Embed(title=name,description=f"Hex: {hexx}")
  emb.add_field(name="rgb",value=rgb,inline=False)
  emb.add_field(name="Clean Hex",value=clean)
  emb.set_thumbnail(url=img)
  await ctx.reply(embed=emb)  


  
'''
@client.command()
@commands.max_concurrency(1,per=commands.BucketType.default,wait=False)
async def kill(ctx,victim:discord.Member=None): 
  if not victim:
    victim=ctx.author
  if victim.id == 900992402356043806 or victim==client.user:
    return await ctx.reply('Just shut up , go to heck , u cant kill me or my owner stupid twit')
  page = requests.get(f'https://api.waifu.pics/sfw/kill')
  source = json.loads(page.content)
  url=source["url"]
  em=discord.Embed(description=f"{victim} is being ....",color=discord.Color.red())
  em.set_image(url=url)
  await ctx.reply(embed=em)  
'''
import psutil

startTime = time.monotonic()
@client.command(aliases=["bi", "about"])
async def bot( ctx):
    row = ActionRow(
        Button(
            style=ButtonStyle.link,
            label="Invite Me!",
            url='https://discord.com/api/oauth2/authorize?client_id=916630347746250782&permissions=8&scope=bot&applications.commands',
            emoji='<:invite:658538493949116428>'
        ),
        Button(
            style=ButtonStyle.link,
            label="Github!",
            url='https://github.com/prakarsh17/tessarect-bot',
            emoji="<:github:912608431230320660>"
        ),
        Button(
            style=ButtonStyle.link,
            label="Support !",
            url='https://discord.gg/avpet3NjTE',
            emoji="<:Servers:946289809289281566>"
        ),
        Button(
            style=ButtonStyle.link,
            label="Website!",
            url='https://tessarect-website.prakarsh17-coder.repl.co/',
            emoji="<:planet:930351400532201532>"
        ),      
        Button(
            style=ButtonStyle.primary,
            label="Developers!",
            custom_id="cred"
        )

  
    )   
    ser = len(client.guilds)
    mem = len(client.users)

    pre = ", ".join(prefix_check(ctx.message.guild))
    embed = discord.Embed(
        timestamp=ctx.message.created_at, description="<:tessarect:956440587177975878> Making experience better",title="Tessarect", color=0x050A30
    )
    embed.set_thumbnail(url=client.user.avatar_url)
    embed.add_field(
        name="<:Servers:946289809289281566> With", value=f"{ser} servers"
    )
    embed.add_field(
        name="<a:panda:930348733844033576> Enjoying With", value=f"{mem} members"
    )
    embed.add_field(name="<:blurple_slashcommands:930349698999537746> Prefix", value=f"{pre}")
    embed.add_field(
        name="<:crownx:920620263584960533> Owner", value="SniperXi199#2209"
    )
    embed.set_footer(
        text=f"Requested By: {ctx.author.name}", icon_url=f"{ctx.author.avatar_url}"
    )
    em = discord.Embed(title="Updates",description="Fetched from my server",color=discord.Color.gold())
    #em.set_author(name=client.user,icon_url=client.user.avatar_url)
    channel=client.get_channel(937559150936879144)
    async for message in channel.history(limit=9):
        content = message.content # get content
        try:
          if message.content is not None:
            try:
              
              em.add_field(name=f"By {message.author} on {message.created_at}",value=content ,inline=False)
            except:
              pass
          else:
            em.add_field(name="_ _",value='Couldnt Fetch Message',inline=False)
        except Exception as e:
          em.add_field(name="_ _",value='Nothin found')       
    msg =await ctx.reply(embed=embed,components=[row])
    await ctx.send(embed=em)
    on_click = msg.create_click_listener(timeout=60)
    @on_click.matching_id("cred")
    async def on_test_button(inter):
      try:
        
        em = discord.Embed(title="Contributors",description=f"{client.get_user(900992402356043806).mention} \n Owner and Lead Developer \n\n {client.get_user(432801163126243328).mention}\n Co Developer and a great supporter\n",color=discord.Color.blue())
        
        #em.set_image(url="https://contrib.rocks/image?repo=prakarsh17/tessarect-bot")
        em.set_footer(text="See our Github for details")
        await inter.reply(embed=em)
      except  Exception as e:
        await inter.reply(e)

    @on_click.timeout
    async def on_timeout():
        await msg.edit(components=[])    

@client.command(aliases=['bug','suggest'])
@commands.cooldown(1,40,commands.BucketType.guild)
@commands.max_concurrency(1,per=commands.BucketType.default,wait=False)
async def feedback(ctx,*,message):
    row = ActionRow(
   
        Button(
            style=ButtonStyle.success,
            label="Confirm!",
            custom_id="gr",
            emoji="<:sucess:935052640449077248>"
        ),
        Button(
            style=ButtonStyle.danger,
            label="Cancel!",
            custom_id="red",
            emoji="<:DiscordCross:940914829781270568>"
        )        
    )   
  
    embed = discord.Embed(
        timestamp=ctx.message.created_at, title="Confirm",description="Do you really wanna send that to developers note it may take time to process your request", color=0x06c8f9
    )

    msg =await ctx.reply(embed=embed,components=[row])
    on_click = msg.create_click_listener(timeout=10)
    @on_click.matching_id("red")
    async def on_test_button(inter):
      em = discord.Embed(title="Cancelled",description="Alright",color=discord.Color.red())   
      await msg.edit(content=None,embed=em)
      await msg.edit(components=[])
    @on_click.matching_id("gr")
    async def on_test_button(inter):
      bugs_channel = client.get_channel(929333373913137224)



      embed = discord.Embed(
            title='Feedback',
            colour = 0x000133
        )
      embed.add_field(name='Username', value=inter.author)
      embed.add_field(name='User id', value=inter.author.id,inline=True)
      embed.add_field(name='Report: ', value=message,inline=False)
      await bugs_channel.send(f"<@&912569937116147777>",embed=embed)



      em = discord.Embed(title="Done",description="Thank you for your feedback kindly keep your dms open they may contact anyway enjoy",color=discord.Color.green())   
      await inter.reply(content=None,embed=em)
      await msg.edit(components=[])

    @on_click.timeout
    async def on_timeout():
        await msg.edit("Ok so dude cancelling",components=[])    


@client.command(aliases=['debuginfo'])
async def stats(ctx):
    stats = await db.find_one({"id": client.user.id})
    now = time.monotonic()
    uptime_seconds = int(now - startTime)
    m, s = divmod(uptime_seconds, 60)  # getting the uptime mins, secs, hrs, days
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)
    values = psutil.virtual_memory()
    val2 = values.available * 0.001
    val3 = val2 * 0.001
    val4 = val3 * 0.001

    values2 = psutil.virtual_memory()
    value21 = values2.total
    values22 = value21 * 0.001
    values23 = values22 * 0.001
    values24 = values23 * 0.001
    dpyVersion = discord.__version__
    em=discord.Embed(title="Stats",description=f"Tessarect Stats \n <:crownx:920620263584960533> **Creator** \n__**SniperXi199#2209**__\n **Channels and Users** \n <:replycont:920287873591296000> {sum(1 for g in client.guilds for _ in g.channels)}\n <:Reply:941181074015412225>{len(client.users)}",color=discord.Color.gold())
    em.add_field(name="Total Commands used",value=stats['tot'],inline=False)
    em.add_field(name='<:CPU:937722162897375282> Hosting Stats', value=f'''```yml
Cpu_usage: {psutil.cpu_percent(1)}%
(Actual Cpu Usage May Differ)
                          
Cores: {psutil.cpu_count()} 
Physical_Cores: {psutil.cpu_count(logical=False)}
BotPlatform: {str(platform.platform())}
```''',inline=True)
    em.add_field(name='<:blurple_settings:937722489004515418> Storage', value=
                          f''' ```yml
Total_ram: {round(values24, 2)} GB                          
Available_Ram : {round(val4, 2)} GB```''',inline=False)   

    em.set_footer(text="Vote here : https://top.gg/bot/916630347746250782/vote ")
    #em.set_image(url="https://i.pinimg.com/originals/49/e7/6e/49e76e0596857673c5c80c85b84394c1.gif") 
    em.set_thumbnail(url=client.user.avatar_url) 
    try:
        foo = subprocess.run("pip show discord.py", stdout=subprocess.PIPE)
        _ver = re.search(r'Version: (\d+.\d+.\w+)', str(foo.stdout)).group(1)
    except: _ver = discord.__version__
    em.add_field(name='Discord.py Version', value='%s'%_ver)
    em.add_field(name='PIP Version', value='%s'%pkg_resources.get_distribution('pip').version)
    if os.path.exists('.git'):
        try: em.add_field(name='Bot version', value='%s' % os.popen('git rev-parse --verify HEAD').read()[:7])
        except: pass
    em.add_field(name='Python Version', value='%s (%s)'%(sys.version,sys.api_version), inline=False)
    dependencies = ''
    dep_file = sorted(open('%s/requirements.txt' % os.getcwd()).read().split("\n"), key=str.lower)
    for dep in dep_file:
        if not '==' in dep: continue
        dep = dep.split('==')
        cur = pkg_resources.get_distribution(dep[0]).version
        if cur == dep[1]: dependencies += '\✔  %s: %s\n'%(dep[0], cur)
        else: dependencies += '\❌ %s: %s / %s\n'%(dep[0], cur, dep[1])
    

   
    await ctx.reply(embed=em)
  
    want_depends=await assets.reactor.reactor(ctx, client, 'Do you want to check current dependencies', 0x34363A,ctx.author)
    if want_depends:
      emx=discord.Embed(title="Dependencies",color=discord.Color.dark_gray())
      emx.add_field(name='Dependencies', value='%s' % dependencies)
      await ctx.send(embed=emx)
@client.command()
async def goal(ctx):

  row = ActionRow(
        Button(
            style=ButtonStyle.link,
            label="Invite Me!",
            url='https://discord.com/api/oauth2/authorize?client_id=916630347746250782&permissions=8&scope=bot&applications.commands'
        )
    )    
  goal = 50
  currentg = len(client.guilds)
  em = discord.Embed(title="Invite tessarect",description=f" Current Count {currentg}/{goal}",color=discord.Color.blue())
  em.set_footer(text="Kindly be kind enough to invite me in a server and contribute and make devs happy xD")
  #em.add_field(name="Goal 1(25 servers) " ,value=f"Achieved on 2nd Feb 2022",inline=False) 
  if goal ==currentg:
    em.add_field(name='Congrats ',value=' I have achieved the current goal')
  else:
    em.add_field(name=" Not yet" ,value=f"We still need {goal-currentg} servers more!")

  await ctx.reply(embed=em,components=[row])

def get_quote():
    res = requests.get("https://zenquotes.io/api/random")
    jsond= json.loads(res.text)
    quote = jsond[0]['q']
    auth = (jsond[0]['a'])
    return quote, auth
@client.command()
async def quote(ctx):
    q, a = get_quote()
    em = discord.Embed(title=a+" Once said.....", description=q, color=discord.Color.blue())
    await ctx.reply(embed=em)
@client.command()
@commands.cooldown(1,100,commands.BucketType.guild)
async def report( ctx, user : discord.Member,*reason):
    em = discord.Embed(title=f'Report {user}?',description="Are you sure you want to report that user , if yes choose report categories else wait for 10 seconds it will automatically go",color=discord.Color.red())
    msg = await ctx.reply(
        embed=em,
        components=[

            SelectMenu(
                custom_id="choice",
                placeholder="Choose the needed choices",
                options=[
                    SelectOption("Used bad words or used bot for illegal stuff ", "value 1"),
                    SelectOption("Used Tessarect currency for buying /trading any other real existence item", "value 2"),
                    SelectOption("Made Tessarect  say foul/swearing words by any means ", "value 3"),
                    SelectOption("Breaking other rules","value 4"),
                    
                    SelectOption("Reporting a staff","value 6"),
                    SelectOption("Appealing reconsideration in previously done ban or some other action","value 7"),
                    SelectOption("*Thuged* (Any kind of CHeating)","value 8"),
                    SelectOption("Something Else to be there in the reason","value 5")               
                ]
            )
        ]
    )
 
    inter = await msg.wait_for_dropdown(timeout=20)

    # Send what you received
    if inter.author == ctx.author:

      labelsx = [option.label for option in inter.select_menu.selected_options]
      await inter.reply(embed=discord.Embed(description='Your report request is being sent to my developers , Kindly keep your dms open for further inquiry if necessary.'))
     
    channel = client.get_channel(929333373913137224) 
    author = ctx.message.author
    rearray = ' '.join(reason[:]) #converts reason argument array to string

    if not rearray: #what to do if there is no reason specified
        await channel.send(f"{author.mention}({author.id}) has reported {user.mention} ({user.id}), reason: Not provided , Parameters {', '.join(labelsx)}")
     
        await ctx.message.delete() #I would get rid of the command input
    else:
        await channel.send(f"{author} has reported {user.mention} ({user.id}), reason: {rearray}, Parameters {', '.join(labelsx)}")
 
        await ctx.message.delete() 


@client.command(name="features") 
async def features(ctx):

    contents = ["TESSARECT FEATURES",""""**Economy Bot**\n
Supports various economy commands like balance , send , rob to make the server more interactive""",
"""**Moderator Commands\n**
Moderation using bot , use Mute , kick ban etc""",
"""**Fully Open Source**
The code of the bot is open source so you dont have to worry about your privacy .""",
"""**Utility Commands**
Commands to make your work easier and faster like avatar{user} gets the avatar of the mentioned user""",
"""**Leveling System**
Enjoy and use Tessarect 's leveling system for your server . Make a rank system""",
"""**Fun Commands**
Enjoy various fun commands such as ascii font , emojify , avatar lookup , info or play tictactoe with someone""",
"""**Secured**
This bot is fully secured by 3 reasons .
Open sourced| It is open sourced so you can know what all things are collected or how the commands work
Permission Checks| There are permision checks for commands like mute , kick or ban. But still if any commands do not have , please report the error to us using the feedback command.""",
"""**Ticket System**
Is your Server messed up with feedback? Or do you not know where is a particular Suggestion? Or you are bored with one channel for suggestion which is filled with messages? If you answered any of these questions in yes , We are here to help you . Tessarect  Provides a ticketing system so people can use the command [prefix]new to make a ticket and support team roles can close them . You can even add valid i.e support team roles or pinging roles that get pinged everytime anyone makes a ticket.""","""**Watching Suggestions**
Your feedback is our priorty . We watch for your queries too . Do you have one ? Join our server -Click Here or use command query or suggest to send feedback from your server only""","""**Translation**
Have you ever faced problem in understanding some foriegn language in a server? No need to go out of discord to use a translater , use amteor translation command (syntax - {prefix}translate {language} {text})""","""**And Much More**"""]
    pages = len(contents)
    cur_page = 1
    message = await ctx.reply(embed=discord.Embed(description=f"{contents[cur_page-1]}", color=discord.Color.blue()))


    # getting the message object for editing and reacting

    await message.add_reaction("◀️")
    await message.add_reaction("▶️")

    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in ["◀️", "▶️"]
        # This makes sure nobody except the command sender can interact with the "menu"

    while True:
        try:
            reaction, user = await client.wait_for("reaction_add", timeout=10000, check=check)

            if str(reaction.emoji) == "▶️" and cur_page != pages:
                cur_page += 1

                em=discord.Embed(description=f"{contents[cur_page-1]}",color=discord.Color.dark_blue(),timestamp=ctx.message.created_at)



                
                await message.edit(embed=em)
                await message.remove_reaction(reaction, user)

            elif str(reaction.emoji) == "◀️" and cur_page > 1:
                cur_page -= 1
                if cur_page==8:
                    em=discord.Embed(description=f"{contents[cur_page-1]}", color=discord.Color.blue())
                    em.set_image(url="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.redd.it%2F9aj95rwqdex41.jpg&f=1&nofb=1")
                else:
                    em=discord.Embed(description=f"{contents[cur_page-1]}", color=discord.Color.blue())
                
                await message.edit(embed=em)
                await message.remove_reaction(reaction, user)

            else:
                await message.remove_reaction(reaction, user)
                # removes reactions if the user tries to go forward on the last page or
                # backwards on the first page
        except asyncio.TimeoutError:
            await message.delete()
            break
           
@client.command()
@commands.cooldown(1, 90, commands.BucketType.user)
async def nasa( ctx):
      api = os.environ['apinasa']
      request = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={api}").json()
      requestDate = request['date']
      requestText=request['explanation']
      requestTitle = request['title']
      requestHDUrl = request['hdurl']
      requestUrl = request['url']
      embednasa = discord.Embed(title = f"**Today's NASA Astronomogy Image of the Day**\n{requestTitle}", description = f"{requestText} ({requestDate})", color=0x09ec23, url=requestHDUrl)

      embednasa.set_author(name = f"NASA API  ", icon_url = "https://api.nasa.gov/assets/img/favicons/favicon-192.png")
      embednasa.set_image(url=requestUrl)
      embednasa.set_footer(text="Press the blue text to see the full resolution image!")
      await ctx.reply(embed=embednasa)
@client.command(aliases=['wolfram'],help="Get information from wolfram|alpha")
async def wolf(ctx, *, question):
    out = get_answer1(question)
    await ctx.reply(embed=out[0], file=out[1])

def get_answer1(question=""):
    if question == "_ _":
        embed = discord.Embed(
            title="Oops",
            description="You need to enter a question",

        )
        embed.set_thumbnail(url=client.user.avatar_url_as(format="png"))
        return (embed, None)
    else:
        question = urllib.parse.quote(question)
        a = requests.get(
            f"http://api.wolframalpha.com/v1/simple?appid={os.environ['wolf']}&i={question}&layout=labelbar&width=1500&fontsize=20"
        ).content
        file = open("output.png", "wb")
        file.write(a)
        file.close()
        embed = discord.Embed(
            title="Wolfram",
            description="This result is from Wolfram",
            color=discord.Color.dark_red()
        )
        embed.set_thumbnail(
            url="https://www.wolfram.com/homepage/img/carousel-wolfram-alpha.png"
        )
        file = discord.File("output.png")
        embed.set_image(url="attachment://output.png")
        return (embed, file)

def replace_chars(stri):
    stri2 = ""
    for char in stri:
        if char not in "<@!>":
            stri2 += char
    # print (f'stri2 is {stri2}')
    return stri2


@client.after_invoke 
async def data(ctx):
  print(ctx.command)
  stats = await db.find_one({"id": client.user.id})
  #print(stats)
  if stats is None:
    new = {"id": client.user.id, "tot": 1,"last_command":str(ctx.command),"last_author":ctx.author.id}
    db.insert_one(new)
  else:
    tot=stats['tot']+1
    last=str(ctx.command)
    lasta=ctx.author.id
    db.update_one({"id": client.user.id},{"$set": {"tot": tot,"last_command": last,"last_author": lasta}})

    
    #dumbest technique , ik
    tips = ['Enjoy ','Check out other features','I have tickets too','Check out Security Cog','Any problem , join our support server','Join my support server-https://discord.gg/avpet3NjTE','Vote for me on top.gg','Check out my AI features by sending [p]help AI','Snipe out people hiding by using [p]snipe command','Are you student ? Join a new server by SniperXi199 - https://discord.gg/3gCFrPXwbz','Do you know , I have two developers','Get info on covid by using Covid cog yeh !','Try me new leveling sys by using<prefix>level','Wanna advertise your server go to my repo(<prefix>src) and go to the discussions and make a topic in Website category details are there','Have you used our leveling system? Try <prefix>level<user(optional)> to check out','We have added daily command which gives you some money per day once ','Have you ever robbed someone?','Try new Ticket System'] 
    em=discord.Embed(description=f"**Tip**-{random.choice(tips)}",color=discord.Color.random())
    await ctx.send(embed=em)
@client.before_invoke
async def checkblack(message):
  with open("storage/black.json") as f:
      users_list = json.load(f)
      if message.author.id  in users_list:
          raise discord.ext.commands.CommandError(f'You are blacklisted')

web.keep_alive()
client.run(os.environ['btoken'],reconnect=True)