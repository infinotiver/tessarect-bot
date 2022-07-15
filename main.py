import os
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
import string    
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
import random
import subprocess
from bs4 import BeautifulSoup
import urllib
import psutil
import motor.motor_asyncio
#import nest_asyncio
#import datetime
import socket  
import datetime
from termcolor import colored
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
from itertools import cycle
from discord.ext import  tasks
import topgg
import nest_asyncio 
import glob
def get_prefix(client, message):
    try:
        with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)
            return prefixes[str(message.guild.id)]
        
    except KeyError: 
        with open('prefixes.json', 'r') as k:
            prefixes = json.load(k)
        prefixes[str(message.guild.id)] = ['a! ']

        with open('prefixes.json', 'w') as j:
            json.dump(prefixes, j, indent = 4)

        with open('prefixes.json', 'r') as t:
            prefixes = json.load(t)
            return prefixes[str(message.guild.id)]
        
    except: # I added this when I started getting dm error messages
        print("Not ok")
        return ['a!']
#-----------------------------------------------------------------------------------------------------------------------

r = requests.head(url="https://discord.com/api/v1")
try:
  print(f"[🔴] Rate limit {int(r.headers['Retry-After']) / 60} minutes left")
except:
  print('[🟢] No ratelimit')

             
nest_asyncio.apply()
mongo_url = os.environ.get("tst")
cluster = motor.motor_asyncio.AsyncIOMotorClient(mongo_url)
db = cluster["tst"]["data"]
intents = discord.Intents.all()
client =AutoShardedBot(shard_count=5,
    command_prefix= (get_prefix),intents=intents,description="Support server https://discord.gg/avpet3NjTE \n Invite https://dsc.gg/tessarect",case_insensitive=True, help_command=PrettyHelp(index_title="Help <:book:939017828852449310>",no_category="Basic Commands",sort_commands=False,show_index=True))
#slash = SlashCommand(client)
m = '**⌾** '

blueokay = '<a:Tick:922450348730355712>'
bluetrusted=''
mongo_url = os.environ['enalevel']
cluster = motor.motor_asyncio.AsyncIOMotorClient(mongo_url)
ecomoney = cluster["discord"]["terrabux"]
prefix=(get_prefix)
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        try:
          client.load_extension(f"cogs.{filename[:-3]}")
        except Exception as e:
          print(f"[🔴] {filename} - {traceback.print_exc()}") 


@client.event
async def on_ready(): 
    os.system("clear")
    font = Figlet(font="standard")
    print(colored(font.renderText(client.user.name), "blue"))
    print(f"[🟢] Logged in as {client.user} ( ID : {client.user.id} )")
    em = discord.Embed(title =f"{client.user.name} Online!",color =discord.Color.green())
    system_latency = round(client.latency * 1000)
    em.set_thumbnail(url=client.user.avatar_url)
    em.add_field(name="Ping",value=system_latency,inline=False)
    em.add_field(name="Server Count",value=len(client.guilds),inline=True)
    em.add_field(name="User Count",value=len(client.users),inline=True)    
    channel=client.get_channel(953571969780023366)

    cog_list = ["cogs." + os.path.splitext(f)[0] for f in [os.path.basename(f) for f in glob.glob("cogs/*.py")]]
    loaded_cogs = [x.__module__.split(".")[1] for x in client.cogs.values()]
    unloaded_cogs = [c.split(".")[1] for c in cog_list if c.split(".")[1] not in loaded_cogs]
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
        ex=discord.Embed(title="Successfully Restarted",description="100% \nBeep Beep Boop Beep !, Reboot done  ",color=discord.Color.dark_blue())
        await channel.send(embed=ex)

        os.remove("./storage/reboot.json")  



dbl_token = os.environ['topggt']  
client.topggpy = topgg.DBLClient(client, dbl_token)
@tasks.loop(minutes=30)
async def update_stats():
    """This function runs every 30 minutes to automatically update your server count."""
    try:
        await client.topggpy.post_guild_count()
        print(f"[🟢] Posted server count ({client.topggpy.guild_count})")
    except Exception as e:
        print(f"[🔴] Failed to post server count\n{e.__class__.__name__}: {e}")


update_stats.start()

from googletrans import Translator
@client.command()
async def translate(ctx, lang=None, *, thing=None):
    description = ""
    for langx in googletrans.LANGCODES:
        description += "**{}** - {}\n".format(string.capwords(langx), googletrans.LANGCODES[langx])
    if not thing or not lang:
      return await ctx.send(embed=discord.Embed(description=description,color=discord.Color.blue()))
    translator = Translator()
    
    translation = translator.translate(thing, dest=lang)
    e=discord.Embed(title="Google Translation",color=discord.Color.blue())
    e.add_field(name="Output",value=translation.text)
    e.add_field(name="Input",value=thing,inline=False)
    await ctx.reply(embed=e)
warnings.filterwarnings("ignore", category=DeprecationWarning)
client.session = aiohttp.ClientSession()
client.load_extension('jishaku')
import datetime

@client.event
async def on_resumed():
    print("[🟢] {0.user} Resumed ".format(client))

@client.event
async def on_guild_remove(guild): 
    with open('prefixes.json', 'r') as f: #read the file
        prefixes = json.load(f)

    prefixes.pop(str(guild.id)) #find the guild.id that bot was removed from

    with open('prefixes.json', 'w') as f: #deletes the guild.id as well as its prefix
        json.dump(prefixes, f, indent=4)
    await client.change_presence(

            activity=discord.Activity(
                type=discord.ActivityType.watching,
                name= f"😢 {str(len(client.guilds))} Servers"
            ))
        
@client.command(pass_context=True,aliases=['prefix'])
@commands.has_permissions(administrator=True)
async def changeprefix(ctx, prefix): #command: a!changeprefix ...
    #test
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = [prefix]

    with open('prefixes.json', 'w') as f: #writes the new prefix into the .json
        json.dump(prefixes, f, indent=4)

    await ctx.reply(f'[🟢] Prefix changed to: {prefix}')
    #test #confirms the prefix it's been changed to




@client.event
async def on_guild_join(guild): #when the bot joins the guild
    with open('prefixes.json', 'r') as f: #read the prefix.json file
        prefixes = json.load(f) #load the json file

    prefixes[str(guild.id)] = ['a!']#default prefix

    with open('prefixes.json', 'w') as f: #write in the prefix.json "message.guild.id": "a!"
        json.dump(prefixes, f, indent=4) #the indent is to make everything look a bit neater





names =['Spencer M.',' McKnight','Saul D. Burgess','Ghiyath Haddad Shadid','Ramzi Muta Hakimi','Callum Peel','Joao Barbosa Pinto','Bertram Hoving','Cian Reith','Mat Twofoot''Alexander Achen''Rohan ','Manish Nadela']   
   

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
                  "**<:arrow_right:940608259075764265> Phonetics:**\n" + data["phonetics"][0]["text"] + "\n\n"
              )
              description += phonetics
      if "origin" in list(data.keys()):
          origin = "**<:arrow_right:940608259075764265> Origin: **" + data["origin"] + "\n\n"
          description += origin
      if "meanings" in data.keys() and "definitions" in data["meanings"][0]:
          meanings = data["meanings"][0]["definitions"][0]
          if "definition" in list(meanings.keys()):
              meaning = "**<:arrow_right:940608259075764265> Definition: **" + meanings["definition"] + "\n\n"
              description += meaning
          if "example" in list(meanings.keys()):
              example = "**<:arrow_right:940608259075764265> Example: **" + meanings["example"]
              description += example
  else:
      word = data["title"]
      description = data["message"]
  embed=discord.Embed(title=f"Word-{word}",
    description=description,color=discord.Color.dark_theme())
  await ctx.send(embed=embed)

@client.command(aliases=['namaste','hi','sup'],hidden=True) 
async def hello(ctx):

  em = discord.Embed(title="Hi <a:panda:930348733844033576>", description=f"Thats Me ! Doing great as ever<a:happyblob:946284960271175710> \nAll right pal   {ctx.author.mention} ? ", color=discord.Color.blue())
  
  page = requests.get(f'https://api.popcat.xyz/fact')
  source = json.loads(page.content)
  f=source['fact']
  em.add_field(name="Quick Knowledge",value=f)
  await ctx.channel.send(embed = em)

@client.command(aliases=['supportserver','githubrepo','src','invite','website'])
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
               "supportserver":"https://discord.gg/avpet3NjTE"}
    embed=discord.Embed(title=ctx.message.content[len("a!"):].split()[0].upper(),description="Important Links ",color=0xFFC0CB,timestamp=ctx.message.created_at)
    embed.set_footer(text="Stay Safe and be happy and keep using Me !")
    for x in links_dict:
      if str(ctx.message.content[len("a!"):].split()[0])== x:
        embed.add_field(name="Link",value=f"{x.upper()} - {links_dict[x]}")
    embed.set_thumbnail(url=client.user.avatar_url)
    await ctx.reply(embed=embed,components=[row])
@client.command(aliases=["vote",'v','support'])
async def vote_tessarect( ctx):
    ef=discord.Embed(
            title=f"Vote for {client.user.name}",
            description=f"Top.gg > https://top.gg/bot/916630347746250782/vote \n VoidBots > https://voidbots.net/bot/916630347746250782/vote \n DiscordBots.gg > https://discordbots.gg/bot/916630347746250782/vote \n" ,     color=discord.Color.gold())
    ef.set_thumnail(url='https://image.shutterstock.com/image-vector/funny-vote-characters-stand-near-600w-1562866837.jpg')
    ef.set_footer(text=f"{client.user.name} Developers !")
    await ctx.send(embed=ef)
    
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
    try:
      channel = client.get_channel(wel[str(member.guild.id)][0])
    except:
      return
    embed = discord.Embed(title=f"{member.name} joined the Party",colour=discord.Colour.dark_orange(),description=wel[str(member.guild.id)][1])
    finalname='+'.join(member.display_name.split())
    finalguild='+'.join(member.guild.name.split())
    
    link=f"https://api.popcat.xyz/welcomecard?background=https://media.discordapp.net/attachments/929334504236122123/997496526903447592/unknown.png&text1={finalname}&text2=Left+{finalguild}&text3=We+have+now+{str(len(member.guild.members))}+people&avatar={str(member.avatar_url_as(format='png'))}"
    embed.set_image(url=link)
    await channel.send(content=f"🌹 Roses are red, 🌸 violets are blue, {member.mention} joined this server with you",embed=embed)    

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
    finalname='+'.join(member.display_name.split())
    finalguild='+'.join(member.guild.name.split())
    link=f"https://api.popcat.xyz/welcomecard?background=https://media.discordapp.net/attachments/929334504236122123/997496526903447592/unknown.png&text1={finalname}&text2=Left+{finalguild}&text3=We+have+now+{str(len(member.guild.members))}+people&avatar={str(member.avatar_url_as(format='png'))}"
    
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
@commands.is_nsfw()
async def yt(ctx, *, url):
    await ctx.reply(searchyt(url))

import platform





os.system('pip install google bs4')
@client.command()
@commands.is_nsfw()
async def google(ctx, *, query):
    import google , bs4
    e=discord.Embed(description="Here are some results",color=discord.Color.random())
    from googlesearch import search # pip install google, bs4
    for j in search(query, tld="co.in", num=1, stop=5, pause=2):
        e.add_field(name="_ _",value=j) 
    await ctx.reply(embed=e)




    
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
  em = discord.Embed(title=f'{user.name} Balance',color = user.color,timestamp=ctx.message.created_at)
  em.add_field(name="Wallet Balance", value=f'**⌾** {wallet_amt:,}',inline=False)
  em.add_field(name='Bank Balance',value=f'**⌾** {bank_amt:,}',inline=False)
  em.set_thumbnail(url=user.avatar_url)
  em.add_field(name='Terrabux',value=f"<a:Diamond:930350459020017694> {bal['terrabux']}",inline=False)
  em.set_footer(text=f"You can be rich")        
  msg=await ctx.reply(embed= em)

 
@client.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def beg(ctx):
    await open_account(ctx.author)
    user = ctx.author

    users = await get_bank_data()

    earnings = random.randrange(400)
    em = discord.Embed(title =random.choice(names),description =f'Gave {ctx.author.mention} **⌾**  {earnings} ',color = discord.Color.green())
    await ctx.reply(embed=em)

    users[str(user.id)]["wallet"] += earnings

    with open("mainbank.json",'w') as f:
        json.dump(users,f)


api_key = os.environ['weather']
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
            feellike = y["feels_like"]
            feellike_celsiuis = str(round(current_temperature - 273.15))
            current_pressure = y["pressure"]
            current_humidity = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            weather_description = z[0]["description"]
            embed = discord.Embed(title=f"Weather in {city_name}",
                              color=ctx.author.color,
                              timestamp=ctx.message.created_at,)
            embed.add_field(name="Descripition", value=f"**{weather_description}**", inline=False)
            embed.add_field(name="Temperature(C)", value=f"**{current_temperature_celsiuis}°C**", inline=False)
            embed.add_field(name="Feels Like(C)", value=f"**{feellike_celsiuis}°C**", inline=False)
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
    await user.send('YOU HAVE GOt your daily + monthly, dont go on the message which says you already claimed your daily , your amount has been credited too , this issue is know and is under development')
    return True    
import datetime
from datetime import datetime, timedelta                                              
@client.command()
async def daily(ctx):

  await open_streak(ctx.author)
  user = ctx.author
  users = await get_bank_data()
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



@client.command(aliases = ["glb"])
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






@client.command(aliases=['screenshot','websitecapture'])
async def ss(ctx, site):
    embed=discord.Embed(description="Here is the Website's ScreenShot you requested",colour = discord.Colour.orange(), timestamp=ctx.message.created_at)
    embed.set_footer(text="Please wait for the image to load")
    embed.set_image(url=(f"https://image.thum.io/get/width/1920/crop/675/maxAge/1/noanimate/{site}"))
    await ctx.reply(embed=embed)
    




def prefix_check(guild):
    # Check if this is a dm instead of a server
    # Will give an error if this is not added (if guild is None)
    if guild == None:
        return "a!"
    try:
        # Check if the guild id is in your 'prefixes.json'
        with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)
            p = prefixes[str(guild.id)]
    except:
        # Otherwise, default to a set prefix
        p = "a!"
    return p


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
@commands.max_concurrency(1,per=commands.BucketType.default,wait=False)
async def fact(ctx): 
  page = requests.get(f'https://api.popcat.xyz/fact')
  source = json.loads(page.content)
  ft = source["fact"] 
  em=discord.Embed(title="A Fact...",description=ft,color=discord.Color.random())
  await ctx.reply(embed=em)




import psutil

startTime = time.monotonic()
@client.command(aliases=["bi", "about","tessarect"])
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
        )

  
    )   
    ser = len(client.guilds)
    mem = len(client.users)
    system_latency = round(client.latency * 1000)
    pre = ", ".join(prefix_check(ctx.message.guild))
    embed = discord.Embed(
        timestamp=ctx.message.created_at, description=f"Making experience better\n<:timer:941993935507689492>**Ping** {system_latency} ms",title=f"{client.user.name}", color=discord.Color.dark_theme()
    )
    embed.set_thumbnail(url=client.user.avatar_url)
    embed.add_field(
        name="<:Servers:946289809289281566> Servers", value=f"┕ {ser} servers"
    )
    embed.add_field(
        name="<:Members:946289063810441248> Enjoying With", value=f"┕ {mem} members"
    )
    embed.add_field(name="<:blurple_slashcommands:930349698999537746> Prefix", value=f"┕ {pre}")
    embed.add_field(
        name="<:blurple_settings:937722489004515418> Developers", value="┕ SniperXi199#2209 - <:owner:946288312220536863> Founder\n┕ Dark-Knight#9193 - Co developer"
    )
    embed.add_field(
        name="<:command:941986813013274625> Commands", value=f"┕ {len(client.all_commands)}"
    )  
    embed.set_footer(
        text=f"Have a nice time :) | Requested By: {ctx.author.name}", icon_url=f"{ctx.author.avatar_url}"
    )
    #em.set_author(name=client.user,icon_url=client.user.avatar_url)  
    msg =await ctx.reply(embed=embed,components=[row])
    on_click = msg.create_click_listener(timeout=60)
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
            emoji="<:Red_Cross:988360177017311263>"
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
      bugs_channel = client.get_channel(979345665081610271)



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
    em=discord.Embed(title="Stats",description=f"{client.user.name} Stats \n <:owner:946288312220536863> **Creator** \n__**SniperXi199#2209**__",color=discord.Color.dark_theme())
    em.add_field(name="Servers",value=len(client.guilds),inline=True)
    em.add_field(name="Channels",value=sum(1 for g in client.guilds for _ in g.channels),inline=True)
    em.add_field(name="Users",value=len(client.users),inline=True)
    em.add_field(name="Total Commands used",value=stats['tot'],inline=True)
    em.add_field(name='<:CPU:937722162897375282> Hosting Stats', value=f'''```yml
Cpu_usage: {psutil.cpu_percent(1)}%
(Actual Cpu Usage May Differ)
                          
Cores: {psutil.cpu_count()} 
Physical_Cores: {psutil.cpu_count(logical=False)}
BotPlatform: {str(platform.platform())}
```''',inline=False)
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
  
    await ctx.reply(embed=em)
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
  em = discord.Embed(title=f"Invite {client.user.name}",description=f" Current Count {currentg}/{goal}",color=discord.Color.blue())
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
''' Need to get this command in dev   
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
     
    channel = client.get_channel(979345665081610271) 
    author = ctx.message.author
    rearray = ' '.join(reason[:]) #converts reason argument array to string

    if not rearray: #what to do if there is no reason specified
        await channel.send(f"{author.mention}({author.id}) has reported {user.mention} ({user.id}), reason: Not provided , Parameters {', '.join(labelsx)}")
     
        await ctx.message.delete() #I would get rid of the command input
    else:
        await channel.send(f"{author} has reported {user.mention} ({user.id}), reason: {rearray}, Parameters {', '.join(labelsx)}")
 
        await ctx.message.delete() 
'''

           
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

@client.after_invoke 
async def data(ctx):
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
    tips = ['Enjoy ','Check out other features','I have tickets too','Check out Security Cog','Any problem , join our support server','Join my support server-https://discord.gg/avpet3NjTE','Vote for me on top.gg','Check out my AI features by sending [p]help AI','Snipe out people hiding by using [p]snipe command','Do you know , I have two developers','Get info on covid by using Covid cog yeh !','Try me new leveling sys by using<prefix>level','Have you used our leveling system? Try <prefix>level<user(optional)> to check out','We have added daily command which gives you some money per day once ','Have you ever robbed someone? || in economy section, dont get bad ideas ||','Try the new Ticket System'] 
    em=discord.Embed(description=f"**Tip**-{random.choice(tips)}",color=discord.Color.dark_theme())
    if random.random()>0.9:
      await ctx.send(embed=em)
        
@client.before_invoke
async def checkblack(message):
  with open("storage/black.json") as f:
      users_list = json.load(f)
      if message.author.id  in users_list:
          raise discord.ext.commands.CommandError(f'You are blacklisted')
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
    