import os
import discord
import traceback
from discord.ext.commands import has_permissions
from dislash import SelectMenu, SelectOption
import web        
#dislash.py 
from discord.ext import commands
import subprocess
import requests, urllib, re
import praw 
import pyjokes
import json
from dislash import InteractionClient, ActionRow, Button, ButtonStyle
from dislash import ContextMenuInteraction
import time
import asyncio 
import jishaku
#from load import  printProgressBar, printProgressBar2
import googletrans
import sys
import sys
try:

  import DiscordUtils
except:
  subprocess.check_call([sys.executable, '-m', 'pip', 'install','DiscordUtils' ])
#from replit import db
import motor.motor_asyncio
#import nest_asyncio
#import datetime
import socket   
from datetime import datetime, timedelta
# Create a translator object
#from discord_slash import SlashCommand, SlashContext
import logging
 
# Create and configure logger
logging.basicConfig(
                    format='%(asctime)s %(message)s',
                    )
 
# Creating an object
logger = logging.getLogger()
 
# Setting the threshold of logger to DEBUG
logger.setLevel(logging.INFO)
 
import urllib.request
from dislash import InteractionClient, Option, OptionType
import typing
import random
from PIL import Image
import io

# Test messages
logger.debug("TESTING LOGGER DEBUG")
logger.info("Just an information")
logger.warning("Its a Warning")
logger.error("Error Logger Test")
logger.critical("Testing Critical Logging")
#subprocess.check_call([sys.executable, '-m', 'pip', 'install','dislash.py', 'discord-pretty-help','randfacts','TenGiphPy','pymongo[srv]'])
def get_prefix(client, message):
    try:
        with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)
            return prefixes[str(message.guild.id)]
        
    except KeyError: # if the guild's prefix cannot be found in 'prefixes.json'
        with open('prefixes.json', 'r') as k:
            prefixes = json.load(k)
        prefixes[str(message.guild.id)] = ['a!','amt ']

        with open('prefixes.json', 'w') as j:
            json.dump(prefixes, j, indent = 4)

        with open('prefixes.json', 'r') as t:
            prefixes = json.load(t)
            return prefixes[str(message.guild.id)]
        
    except: # I added this when I started getting dm error messages
        print("Not ok")
        return 'a!' 
#-----------------------------------------------------------------------------------------------------------------------

from discord.ext.commands import AutoShardedBot
#from pretty_help import DefaultMenu, PrettyHelp

r = requests.head(url="https://discord.com/api/v1")
try:
    print(f"Rate limit {int(r.headers['Retry-After']) / 60} minutes left")
except:
    print('No rate limit Sire Lets do it!')
try:
  from pretty_help import PrettyHelp
except:
  subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'discord_pretty_help'])

intents = discord.Intents.all()
client =AutoShardedBot(shard_count=2,
    command_prefix= (get_prefix),intents=intents,description="A POWERFUL DISCORD client YOU WILL EVER NEED",case_insensitive=True, help_command=PrettyHelp(index_title="Plugins",color=0x34363A,no_category="Base Commands",sort_commands=False,show_index=False))
#inter_client = InteractionClient(client)
m = '֍'
#slashx = SlashCommand(client)

#____emojis______
blueokay = '<a:Tick:922450348730355712>'
bluetrusted=''
mongo_url = os.environ['enalevel']

cluster = motor.motor_asyncio.AsyncIOMotorClient(mongo_url)
ecomoney = cluster["discord"]["terrabux"]


# Initial Prefix
# with open("guilds.json") as f:
#     guild = message.channel.guild
#     x = json.load(f)
#     prefix = x[guild.id]
prefix=(get_prefix)
from itertools import cycle
from discord.ext import  tasks

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")



# ":discord:743511195197374563" is a custom discord emoji format. Adjust to match your own custom emoji.
#menu = DefaultMenu(page_left="◀", page_right="▶", remove="⛔", active_time=20)

# Custom ending note
#ending_note = "Hello "
#client.help_command = PrettyHelp(menu=menu, ending_note=ending_note)
@client.event
async def on_ready():
    #DiscordComponents(client) 
    print(f'{client.user} - Tessarect (Formerly Amteor) has connected to Discord! Enjoy ')  

    await client.change_presence(

            activity=discord.Activity(
                type=discord.ActivityType.listening,
                name= f"8.0"
            ))


from googletrans import Translator

@client.command()
async def translate(ctx, lang, *, thing):
    translator = Translator()
    translation = translator.translate(thing, dest=lang)
    await ctx.send(translation.text)


status= cycle([" a!help in {n}  servers ",'Tessarect (Formely Tessarect (Formely Amteor)) BOT','Try my New Economy Bots','Try me new leveling sys by using<prefix>level','Wanna advertise your server go to my repo(<prefix>src) and go to the discussions and make a topic in Website category details are there'.format(n=len(client.guilds))])
er = 0xFF0000
'''
@client.event
async def on_command_error(ctx, error): 
    if hasattr(ctx.command, "on_error"):
      return
    #test
    if isinstance(error, commands.MissingRequiredArgument):
      embed=discord.Embed(title="ERROR", description=f"""```diff
-You are missing an argument
Correct Usage - 
{ctx.prefix}{ctx.command.name} {ctx.command.signature}
```""", color=er)
      embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/922468797108080660.png")
      await ctx.send(embed= embed)
    elif isinstance(error, commands.CommandNotFound):
      x = ctx.message.content
      print(f"""
    
███╗░░██╗░█████╗░████████╗  ███████╗░█████╗░██╗░░░██╗███╗░░██╗██████╗░
████╗░██║██╔══██╗╚══██╔══╝  ██╔════╝██╔══██╗██║░░░██║████╗░██║██╔══██╗
██╔██╗██║██║░░██║░░░██║░░░  █████╗░░██║░░██║██║░░░██║██╔██╗██║██║░░██║
██║╚████║██║░░██║░░░██║░░░  ██╔══╝░░██║░░██║██║░░░██║██║╚████║██║░░██║
██║░╚███║╚█████╔╝░░░██║░░░  ██║░░░░░╚█████╔╝╚██████╔╝██║░╚███║██████╔╝
╚═╝░░╚══╝░╚════╝░░░░╚═╝░░░  ╚═╝░░░░░░╚════╝░░╚═════╝░╚═╝░░╚══╝╚═════╝░\nCommand Name {x}  ```""")

    elif isinstance(error, MissingPermissions):
      embed=discord.Embed(title="ERROR", description=f"""```diff
- {error}
```""", color=er)
      embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/922468797108080660.png")
      await ctx.send(embed= embed)
    elif isinstance(error , commands.CommandOnCooldown):
      embed=discord.Embed(title="Whoa Slow It Down", description=f"Command On Cooldown. Hold your horses . Wait  **{display_time(error.retry_after)}** Seconds", color=0x303236)

      await ctx.send(embed= embed)  
    elif isinstance(error, discord.errors.Forbidden):
        try:
            embed = discord.Embed(
                title="Forbidden",
                description=f"Error - 403 - Forbidden | Missing perms",
                color=0xFF0000,
            )
            await ctx.send(embed=embed)
        except:
            print("Failed forbidden")
        return      
    elif isinstance(error, commands.BotMissingPermissions):
        missing = [
            perm.replace("_", " ").replace("guild", "server").title()
            for perm in error.missing_perms
        ]
        if len(missing) > 2:
            fmt = "{}, and {}".format("**, **".join(missing[:-1]), missing[-1])
        else:
            fmt = " and ".join(missing)

        embed = discord.Embed(
            title="Missing Permissions",
            description=f"I am missing **{fmt}** permissions to run this command :(",
            color=0xFF0000,
        )
        return   
    elif isinstance(error, commands.CheckFailure):
        embed = discord.Embed(
            title="Permissions Not Satisfied",
            description=f"You do not have permissions to use this command",
            color=0xFF0000,
        )          
    elif isinstance(error,commands.BadArgument):

      embed=discord.Embed(title="Incorrect Argument ", description=f"You have entered a incorrect/Bad Argument\n{error}", color=er)
      embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/922468797108080660.png")
      await ctx.send(embed= embed)   
    elif isinstance(error, commands.MaxConcurrencyReached):
        await ctx.send('{} Bot is busy! Please retry after some time'.format(ctx.author.mention))
        return
    elif isinstance(error, commands.errors.NSFWChannelRequired):
      embed=discord.Embed(title="Whoa , No nsfw here", description=f"NSFW CHANNELS ONLY \n{error}", color=er)
      embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/922468797108080660.png")     
    elif isinstance(error, commands.CheckFailure):
        embed = discord.Embed(
            title="Permissions Not Satisfied",
            description=f"You do not have permissions to use this command",
            color=0xFF0000,
        )
        await ctx.send(embed=embed)
        return



    else:
        erx = discord.Embed(title="An Error Occured",description=f"""```diff
-{error}
```""")
        await ctx.send(embed=erx)
        print(error)
    print("Ignoring exception in command {}:".format(ctx.command), file=sys.stderr)

    traceback.print_exception(
        type(error), error, error.__traceback__, file=sys.stderr
    )
'''
import aiohttp
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
client.session = aiohttp.ClientSession()
client.load_extension('jishaku')






import datetime

@client.event
async def on_resumed():
    print("Bot user: {0.user} RESUMED".format(client))

    print("==========RESUMED==========")
    em = discord.Embed(title ="Monitor RESUMED",description=f"Tessarect (Formely Tessarect (Formely Amteor)) Monitor Resumed ",color =0x00b300)

    channel = client.get_channel(918800361278550037)

    await channel.send(embed=em)    

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
@has_permissions(administrator=True)
async def changeprefix(ctx, prefix): #command: a!changeprefix ...
    #test
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = [prefix,"amt "]

    with open('prefixes.json', 'w') as f: #writes the new prefix into the .json
        json.dump(prefixes, f, indent=4)

    await ctx.send(f'Prefix changed to: {prefix}')
    #test #confirms the prefix it's been changed to
#next step completely optional: changes bot nickname to also have prefix in the nickname
    name=f'{prefix}Tessarect (Formely Tessarect (Formely Amteor))'
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
tips=['Have you used our leveling system? Try <prefix>level<user(optional> to check out','Want your server on our website? use command <prefix>web for details','We have added daily command which gives you some money per day once or if you are so lucky then even twice or thrice . Depends','Have you ever robbed someone?']     
    
@client.command(hidden=True)
@commands.is_owner()
async def bye(ctx):

    log_out = ['Man am I tired, I think I need to get some shuteye',
               'CAN\'T SEE, NEED TO CLOSE EYES',
               'I think I\'ll just lay down for a minute ',
               'Short of breath, vision fading..... leave me here to DIIIE'
               ]

    response3 = random.choice(log_out)
    await ctx.send(response3)
    await client.logout()
@bye.error
async def error(ctx,error):

        annoyed = [
            'Your\'re not the boss of me!!',
            'You dare to defy ME????',
            'Yeah, you bugger off!!',
            'You\'r words mean nothing to me!!!'
        ]
        pain = random.choice(annoyed)
        await ctx.send(pain)






from discord.http import Route
import uuid
client.poll_data = {}


def make_buttons(tag, data):
    splited_data = [data[i * 5:(i + 1) * 5] for i in range((len(data) + 5 - 1) // 5 )]
    components = []
    for i in splited_data:
        buttons = []

        for j in i:
            buttons.append({
                'type': 2,
                'style': 2,
                'custom_id': f'{tag}.{j["id"]}',
                'label': j['name']
            })

        components.append({
            'type': 1,
            'components': buttons
        })
    return components


@client.command('poll')
async def poll(ctx, title, *names):
    #test
    poll_id = uuid.uuid4().hex

    data = []
    client.poll_data[poll_id] = {
        'title': title,
        'items': {}
    }

    for i in names:
        item_id = uuid.uuid4().hex
        client.poll_data[poll_id]['items'][f'{poll_id}.{item_id}'] = {
            'name': i,
            'users': []
        }
        data.append({ 'name': i, 'id': item_id })

    embed = discord.Embed(
        title=title,
        description="\n".join(map(lambda x: f'`{x}` : 0 votes', names)),
        color=0x58D68D
    )
    embed.set_footer(text='Poll Services')

    route = Route('POST', '/channels/{channel_id}/messages', channel_id=ctx.channel.id)
    await client.http.request(route, json={
        'embed': embed.to_dict(),
        'components': make_buttons(poll_id, data)
    })


@client.event
async def on_socket_response(msg):

  if msg['t'] != 'INTERACTION_CREATE': return
  full_id = msg['d']['data']['custom_id']
  poll_id = full_id.split('.')[0]
  if not client.poll_data.get(poll_id): return
  data = client.poll_data[poll_id]
  user_id = msg['d']['member']['user']['id']
  if user_id in data['items'][full_id]['users']:
      client.poll_data[poll_id]['items'][full_id]['users'].remove(user_id)
  else:
      client.poll_data[poll_id]['items'][full_id]['users'].append(user_id)
    
  embed = msg['d']['message']['embeds'][0]
  content = "\n".join(map(lambda x: f'`{data["items"][x]["name"]}` : {len(data["items"][x]["users"])}', data['items']))
  embed['description'] = content

  route = Route('PATCH', '/channels/{channel_id}/messages/{message_id}', channel_id=msg['d']['channel_id'], message_id=msg['d']['message']['id'])
  await client.http.request(route, json={
      'embed': embed,
      'components': msg['d']['message']['components']
  })


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
        return await ctx.send(f"You can't take my token , huh {ctx.author.name}")

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
    embed.add_field(name="Input",value="```py\n"+code+"\n```",inline=False)
    #embed.add_field(name=outname,value="```\n"+str(output)+"\n```",inline=False)
    embed.set_author(name=ctx.author.display_name,icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

@client.command()
async def color(ctx, color: typing.Optional[discord.Color]):
    if color == None:
        color = discord.Color(random.randint(0,0xffffff))
    
    embed = discord.Embed(colour=color)
    embed.add_field(name="Hex",value=str(color),inline=False)
    embed.add_field(name="RGB",value=str(discord.Color.to_rgb(color)).replace("(","").replace(")",""),inline=False)
    embed.set_thumbnail(url="attachment://image.png")
    with io.BytesIO() as image_binary:
        Image.new("RGB",(256,256),discord.Color.to_rgb(color)).save(image_binary,"PNG")
        image_binary.seek(0)
        await ctx.send(embed=embed,file=discord.File(fp=image_binary, filename="image.png"))


@client.command(aliases =['delete'])
async def delete_channel(ctx, channel_name):
   #test
   # check if the channel exists
   existing_channel = discord.utils.get(ctx.guild.channels, name=channel_name)
   
   # if the channel exists
   if existing_channel is not None:
      await existing_channel.delete()
   # if the channel does not exist, inform the user
   else:
      await ctx.send(f'No channel named, "{channel_name}", was found')


    #embed = discord.Embed(title=f"{ctx.guild.name}", description="Tessarect (Formely Tessarect (Formely Amteor)) Information Services", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    #embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
    #embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
    #embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
    #embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    #embed.add_field(name="User ID", value=f"{ctx.author.id}")
    #embed.add_field(name="Display Name", value=f"{ctx.author.display_name}")
    #embed.add_field(name="Display Name", value=f'{r}')
    #embed.set_thumbnail(url=f"{ctx.guild.icon}")
    #await ctx.send(embed=embed)
@client.command(aliases=['namaste','hi','bonjour'],hidden=True) 
async def hello(ctx):
  #test 
  em = discord.Embed(title="Hi", description=f"Hi , Bonjour , Namaste 🙏  {ctx.author.mention}", color=discord.Color.green())
  em.set_image(url="https://media2.giphy.com/media/SbKNFpFZEumGTkgPgA/giphy.gif?cid=ecf05e47bhxa7graukqo2r3o6o83x9a3wja60ym4y9rmud4o&rid=giphy.gif&ct=g")

  await ctx.channel.send(embed = em)
#embed=discord.Embed(title="Here you go",description="Here are the important links you must have",color=discord.Color.random())
@client.command(aliases=['support server','githubrepo','src','invite'])
async def links(ctx):

    e = discord.Embed(title="LINKS",description="Keep it safe dude")
    e.add_field(name="Invite",value='[CLICK !](https://discord.com/api/oauth2/authorize?client_id=916630347746250782&permissions=8&scope=bot&applications.commands)')
    e.add_field(name="Get Support",value='[Support Server!](https://discord.gg/avpet3NjTE)')   
    e.add_field(name="Src",value='[See!](https://github.com/prakarsh17/tessarect-bot)')     
    await ctx.send(embed=e)
    
  #e = discord.Embed()
def getmeme(topic): # Topic/Subreddit name
    reddit = praw.Reddit(client_id=os.environ['client_id'],
                    client_secret=os.environ['client-secret'],
                    user_agent='meme') # Initializing details

    submission = reddit.subreddit(topic).random() #finding a random post in the given subreddit
    return submission.url
ser = []

from requests import PreparedRequest
@client.command(pass_context=True)
@has_permissions(administrator=True) #ensure that only administrators can use this command
async def setwelcomechannel(ctx,channel:discord.TextChannel): 
    with open('storage/welcome.json', 'r') as f:
        wel = json.load(f)

    wel[str(ctx.guild.id)] = int(channel.id)

    with open('storage/welcome.json', 'w') as f: #writes the new prefix into the .json
        json.dump(wel, f, indent=4)

    await ctx.send(f'Changed welcome channel to {channel}') #confirms the prefix it's been changed to

# ...

@client.event
async def on_member_join(member):
    with open('storage/welcome.json', 'r') as f:
        wel = json.load(f)  
    
    channel = client.get_channel(wel[str(member.guild.id)])
    if not channel:
      return print('not set ')
    embed = discord.Embed(colour=discord.Colour.green())
    req = PreparedRequest()
    req.prepare_url(
        url='https://api.xzusfin.repl.co/card?',
        params={
            'avatar': str(member.avatar_url_as(format='png')),
            'middle': 'Welcome ',
            'name': str(member.name),
            'bottom': str('to  ' + member.guild.name),
            'text': '#3333ff',
            'avatarborder': '#3333ff',
            'avatarbackground': 'https://replit.com/@AyushSehrawat/Prakash#bg.png',
            'background': 'https://images4.alphacoders.com/936/thumbbig-936378.webp' #or image url
        }
    )
    embed.set_image(url=req.url)
    await channel.send(embed=embed)    



@client.command()
async def meme(ctx):
    #test()
    embed = discord.Embed(color=0x34363A)
    embed.set_image(url=getmeme("ProgrammerHumor"))
    like = random.randrange(10,1000)
    dlike =random.randrange(0,1)
    comm=random.randrange(100,1200)
    trop = random.randrange(1,12)
    embed.set_footer(text=f"👍🏻{like} 👎🏻{dlike} 💬 {comm} 🏆{trop}")
    await ctx.send(embed=embed)



#The below code unbans player.
@client.command()
@commands.has_permissions(administrator = True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return


def searchyt(song):
    music_name = song
    query_string = urllib.parse.urlencode({"search_query": music_name})
    formatUrl = urllib.request.urlopen("https://www.youtube.com/results?" + query_string)
    search_results = re.findall(r"watch\?v=(\S{11})", formatUrl.read().decode())
    clip2 = "https://www.youtube.com/watch?v=" + "{}".format(search_results[0])
    return clip2

@client.command()
async def yt(ctx, *, url):
    await ctx.send(searchyt(url))



    


import platform
@client.command(hidden=True)
async def botplatform(ctx):
    """Shows what OS the bot is running on."""
    await ctx.send("The bot is currently running on: ```" + str(platform.platform()) + "```")



@client.command()
async def pyjoke(ctx):
    jk=pyjokes.get_joke(language='en', category= 'neutral')
    em = discord.Embed(title="Joke", description=jk,color=discord.Color.red())
    
    await ctx.send(embed = em)
@client.command(name='hp99', description="Sings Harry Potter in 99 Seconds ",hidden=True)
@commands.cooldown(1,99,commands.BucketType.guild)
async def hp99(ctx):
  await ctx.send("THERE ONCE WAS A BOY NAMED HARRY DESTINED TO BE A STAR HIS PARENTS WERE KILLED BY VOLDEMORT WHO GAVE HIM HIS LIGHTNING SCAR YO HARRY YER A WIZARD DOODOODOODOODOODOODOODOODOODOOODOODOODOODOODOODOO HARRY GOES TO HOGWARTS HE MEETS RON AND HERMIONE MCGONAGALL REQUIRES THAT HE PLAYS FOR GRYFFINDOR DRACO IS A DADDY'S BOY QUIRRELL BECOMES UNEMPLOYED AND THE SORCERER'S STONE IS DESTROYED BY DUMBLEDORE")
  await ctx.send("RON BREAKS HIS WAND NOW GINNY'S GONE AND HARRY'S IN MORTAL DANGER TOM RIDDLE HIDES HIS SNAKE INSIDE HIS GINORMOUS SECRET CHAMBER")
  await ctx.send("HARRY BLOWS UP AUNT MARGE THE DEMENTORS COME AND TAKE CHARGE LUPIN IS A WOLF THE RAT'S A MAN AND NOW THE PRISONER IS AT LARGE THEY USE TIME TRAVEL SO THEY CAN SAVE THE PRISONER OF AZKABAN WHO JUST SO HAPPENS TO BE HARRY'S GODFATHER I DON'T REALLY GET IT EITHER")
  await ctx.send("HARRY GETS PUT INTO THE TRIWIZARD TOURNAMENT DRAGONS AND MERMAIDS OH NO EDWARD CULLEN GETS SLAYED HE'S BACK")
  await ctx.send("HARRY HARRY ITS GETTING SCARY VOLDEMORT'S BACK YOU'REA REVOLUTIONARY HARRY DUMBLEDORE DUMBLEDORE WHY IS HE IGNORING YOUR CONSTANT ATTEMPTS TO CONTACT HIM HE IS FORCED TO LEAVE THE SCHOOL UMBRIDGE ARRIVES DRACO'S A TOOL KIDS BREAK INTO THE MINISTRY AND SIRIUS BLACK IS DEAD AS CAN BE OHHHHHH")
  await ctx.send("SPLIT YOUR SOUL SEVEN PARTS OF A WHOLE THEY'RE HORCRUXES IT'S DUMBELDORE'S END DOODOODOODOODOODOODOO")
  await ctx.send("THERE ONCE WAS A BOY NAMED HARRY WHO CONSTANTLY CONQUERED DEATH BUT IN ONE FINAL DUEL BETWEEN GOOD AND BAD HE MAY TAKE HIS FINAL BREATH...")


#+never
@client.command(name='never', description="Sings Never Gonna Give you Up by Rick Astley",hidden=True)
@commands.cooldown(1,212, commands.BucketType.guild)
async def never(ctx):
  await ctx.send(("We're no strangers to love You know the rules and so do I A full commitment's what I'm thinking of You wouldn't get this from any other guy").upper())
  await ctx.send(("I just wanna tell you how I'm feeling Gotta make you understand").upper())
  await ctx.send(("Never gonna give you up Never gonna let you down Never gonna run around and desert you Never gonna make you cry Never gonna say goodbye Never gonna tell a lie and hurt you").upper())
  await ctx.send(("We've known each other for so long Your heart's been aching, but you're too shy to say it Inside, we both know what's been going on We know the game, and we're gonna play it").upper())
  await ctx.send(("And if you ask me how I'm feeling Don't tell me you're too blind to see").upper())
  await ctx.send(("Never gonna give you up Never gonna let you down Never gonna run around and desert you Never gonna make you cry Never gonna say goodbye Never gonna tell a lie and hurt you Never gonna give you up Never gonna let you down Never gonna run around and desert you Never gonna make you cry Never gonna say goodbye Never gonna tell a lie and hurt you").upper())
  await ctx.send(("Ooh (Give you up) Ooh-ooh (Give you up) Ooh-ooh Never gonna give, never gonna give (Give you up) Ooh-ooh Never gonna give, never gonna give (Give you up)").upper())
  await ctx.send(("We've known each other for so long Your heart's been aching, but you're too shy to say it Inside, we both know what's been going on We know the game, and we're gonna play it").upper())
  await ctx.send(("I just wanna tell you how I'm feeling Gotta make you understand").upper())
  await ctx.send(("Never gonna give you up Never gonna let you down Never gonna run around and desert you Never gonna make you cry Never gonna say goodbye Never gonna tell a lie and hurt you Never gonna give you up Never gonna let you down Never gonna run around and desert you Never gonna make you cry Never gonna say goodbye Never gonna tell a lie and hurt you Never gonna give you up Never gonna let you down Never gonna run around and desert you Never gonna make you cry Never gonna say goodbye Never gonna tell a lie and hurt you").upper())





@client.command()
async def google(ctx, *, query):
    import google , bs4
    from googlesearch import search # pip install google, bs4
    for j in search(query, tld="co.in", num=1, stop=1, pause=2):
        await ctx.send(j) 





    
    #
 
# ---------------------------------------------------------------------------------------

 

@client.command()
@has_permissions(administrator=True)
async def dm(ctx,member: discord.User, *, text):
  try:
    em = discord.Embed(title=(f"Direct Message via Tessarect  DM Services . Sent by  {ctx.author.display_name} in  {ctx.message.guild.name}"), description=(text), color=discord.Color.blue())
    
    channel=await member.create_dm()
    await channel.send(embed = em) 
    await ctx.message.delete()
    
  except Exception as e:
    print(e)


@client.command()
async def lyrics(ctx, *, song):
    from lyrics_extractor import SongLyrics

    sc = SongLyrics('AIzaSyCBc9vGiM-q0dIOpt0mSIdhraUGiF1pU_U', '2c0e4a26e5d598f41')
    js = sc.get_lyrics(
        song
    )
    em = discord.Embed(title=js["title"], description=js["lyrics"], color=discord.Color.blue())
    await ctx.send(embed=em)












 








@client.command()
async def create(ctx, *, name=None):
  if (
        
         ctx.author.guild_permissions.manage_messages or
         ctx.author.id == 900992402356043806

    ):
    guild = ctx.message.guild
    if name == None:
     await ctx.send('Sorry, but you have to insert a name. Try again, but do it like this: `a!create [channel name]`')
     return
    else:
     await guild.create_text_channel(name)
    await ctx.send(f"Created a channel named {name}")
















@client.command()
@commands.cooldown(1, 2, commands.BucketType.guild)
async def flames(ctx, *, msg):
    msg = await ctx.send(f'{msg}? (15sec to vote)\n```{msg}?```')
    await msg.add_reaction('👍')
    await msg.add_reaction('👎')
    reaction = None
    try:
        while reaction == None or \
        (str(reaction.emoji) != '👍' and reaction.count <= 3):
            reaction, user = await client.wait_for('reaction_add', timeout=15.0)
    except asyncio.TimeoutError:
        await msg.delete()
        await sendTempMsg(ctx, 3, f'{ctx.message.author.mention} denied.')
        await ctx.message.add_reaction('👎')
    else:
        await msg.delete()
        await sendTempMsg(ctx, 3, f'{ctx.message.author.mention} approved!')
        await ctx.message.add_reaction('👍')

async def sendTempMsg(ctx, time, msg):
    tempMsg = await ctx.send(msg)
    await asyncio.sleep(time)
    await tempMsg.delete()




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
{"name":"Pride_Armor","price":100000000000000,"short":"This well-crafted leather armor comes with a sturdy, enveloping longcoat, bearing on its back the insignia of a well-known pirate captain","description":"This well-crafted leather armor comes with a sturdy, enveloping longcoat, bearing on its back the insignia of a well-known pirate captain. When you attune to it, the insignia changes to one that represents you instead. While wearing this armor, climbing and swimming don't cost you extra movement, and you can breathe underwater. In addition, you can use a bonus action to shift into a watery, elemental form, gaining the following benefits for the duration: Your speed increases by 10 feet. You have resistance to bludgeoning, piercing, and slashing damage from nonmagical attacks, as well as resistance to acid damage. You have advantage on ability checks to avoid or escape being grappled or restrained. If you’re already grappled or restrained when shift into this form, you automatically escape. While you’re underwater, Wisdom (Perception) checks made to see you have disadvantage. This form lasts as long as you concentrate (as if concentrating on a spell), to a maximum of 1 minute. Once this property of the armor has been used, it can’t be used again until the next dawn","emoji":"",'com':'Epic Rare'}]

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
  em.add_field(name='Terrabux',value=f"<a:Diamond:930350459020017694> {bal['terrabux']}",inline=False)
  em.set_thumbnail(url=user.avatar_url)
  tot = bank_amt+wallet_amt
  em.set_footer(text=f"🤨 {wallet_amt+bank_amt}")    
  msg=await ctx.send(embed= em)


import string    
hacking_status = ['breaching mainframe', 'accessing CPU pins', 'a couple gigabytes of RAM','Accessing Ip adress ','Getting Os info']
osd = ['unkown windows','windows 11','unknown linux','mac','arch','calinix','windows xp','andriod 2','andriod 12','A poor os ']
def random_char(y):
       return ''.join(random.choice(string.ascii_letters) for x in range(y))
@client.command()
@commands.cooldown(1, 1200, commands.BucketType.user)
async def hack(ctx,member:discord.Member):

    virus = "ZoinMot"
    first = random.choice(hacking_status)
    second = random.choice(hacking_status)
    third=random.choice(hacking_status)
   
    third2=random.choice(hacking_status)    
    end = 'Hack Completed'
    osf =random.choice(osd)
    email = member.name+random_char(4)+'cal.co'
    _pass= random_char(10)
    while first == second or first == third:
        first = random.choice(hacking_status)
    while  second== third:
        second = random.choice(hacking_status)


    embed = discord.Embed(colour=0x00ff55, title=f"{first}...",)
    message = await ctx.channel.send(embed=embed)
    await asyncio.sleep(1)
    embed = discord.Embed(colour=0x00ff55, title=f"{second}...",)
    await message.edit(embed=embed)
    await asyncio.sleep(6)
    embed = discord.Embed(colour=0x00ff55, title=f"Os :{osf}...",)
    await message.edit(embed=embed)   
    embed = discord.Embed(colour=0x00ff55, title=f"{third}...",)
    await message.edit(embed=embed)       
    await asyncio.sleep(2.5)

    await message.edit(f"``[▓                    ] / {virus}-virus.exe Packing files.``")
    list = (
        f"``[▓▓▓                    ] / {virus}-virus.exe Packing files.``",
        f"``[▓▓▓▓▓▓▓                ] - {virus}-virus.exe Packing files..``",
        f"``[▓▓▓▓▓▓▓▓▓▓▓▓           ] \ {virus}-virus.exe Packing files..``",
        f"``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓         ] | {virus}-virus.exe Packing files..``",
        f"``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓      ] / {virus}-virus.exe Packing files..``",
        f"``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   ] - {virus}-virus.exe Packing files..``",
        f"``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ] \ {virus}-virus.exe Packing files..``",
        f"``Successfully downloaded {virus}-virus.exe``",
        "``Injecting virus.   |``",
        "``Injecting virus..  /``",
        "``Injecting virus... -``",
        f"``Successfully Injected {virus}-virus.exe into {member.name}``",
        )
    for i in list:
        await asyncio.sleep(1.5)
        await message.edit(content=i)       
    await asyncio.sleep(6)    
    embed = discord.Embed(colour=0x00ff55, title=f"{third2}...",)
    await message.edit(embed=embed) 
    await asyncio.sleep(1)
    embed = discord.Embed(colour=0x00ff55, title=f"Email:{email}...",)
    await message.edit(embed=embed)   
    await asyncio.sleep(3)    
    embed = discord.Embed(colour=0x00ff55, title=f"Pass:{_pass}...",)
    await message.edit(embed=embed)   
    await asyncio.sleep(3)         
    embed = discord.Embed(colour=0x00ff55, title=f"{end}...",)
    await message.edit(embed=embed)   
 
@client.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def beg(ctx):
    await open_account(ctx.author)
    user = ctx.author

    users = await get_bank_data()

    earnings = random.randrange(400)
    em = discord.Embed(title =random.choice(names),description =f'Gave {ctx.author.mention} ֍ {earnings} ',color = discord.Color.green())
    await ctx.send(embed=em)

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
    await ctx.send(embed=em)

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

    await ctx.send(embed=job_menu)
@findjob.command()
@commands.cooldown(1, 2000, commands.BucketType.user)
async def resign(ctx):
    await open_account(ctx.author)

    with open(r'mainbank.json', 'r') as f:
            user_info = json.load(f)
    
    await ctx.send(f'YOU RESIGNED now u have no work to do')
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
        await ctx.send(embed=discord.Embed(title='Interview Passed :money_with_wings:', description=f'{ctx.author.name} started a job as a {title}. Type {" or ".join(prefix_check(ctx.message.guild))}work to begin.', color=0xd400ff))

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
        await ctx.send('DUMBASS u dont have a work to do , use job command to find one')
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
        strx[str(user.id)]["streakm"] = 1
        strx[str(user.id)]["last_claimm"] = last_claim_stamp        
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
    await ctx.send(f'YOU ALREADY CLAIMED YOUR DAILY in 24 hours , your last claim was on <t:{round(int(float(last_claim_stamp)))}>')
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
  await ctx.send(embed=embed)

@client.command()
async def monthly(ctx):

  await open_streak(ctx.author)
  user = ctx.author
  users = await get_bank_data()

  with open ("streak.json","r") as f:
    data = json.load(f)
  streak=data[f"{ctx.author.id}"]["streakm"]
  last_claim_stamp=data[f"{ctx.author.id}"]["last_claimm"]
  last_claim=datetime.fromtimestamp(float(last_claim_stamp))
  now  =datetime.now() 
  delta = now-last_claim 
  print(f"{streak}\n{last_claim_stamp}\n{last_claim}\n{now}\n{delta}") 
  if delta< timedelta(days=31):
    await ctx.send(f'YOU ALREADY CLAIMED YOUR MONTHLY in 31 days , your last claim was on <t:{round(int(float(last_claim_stamp)))}>')
    return
  if delta > timedelta(days=31):
    print('streak reset')
    streak = 1
  else:
    streak+=1   
  daily = 50000+(streak*5) 
  data[f'{ctx.author.id}']["streakm"]=streak
  data[f'{ctx.author.id}']["last_claimm"]= str(now.timestamp())
  with open("streak.json","w") as f:
    json.dump(data,f,indent=2)
  embed = discord.Embed(title="Monthly", colour=random.randint(0, 0xffffff), description=f"You've claimed your monthly of **{daily}** \n ")
  embed.set_footer(text=f"Your MONTHLY  streak : {streak}")
  users[str(user.id)]["wallet"] += daily

  with open("mainbank.json",'w') as f:
      json.dump(users,f)
  await ctx.send(embed=embed)

@client.command(aliases=['wd','with'])
async def withdraw(ctx,amount = None):
    #test
    await open_account(ctx.author)
    if amount is None:
        await ctx.send("Please enter the amount")
        return

    bal = await update_bank(ctx.author)
    if amount in ("all", "max"):

      amount = int(bal[1])
        
    amount = int(amount)

    if amount > bal[1]:
        await ctx.send('You do not have sufficient balance')
        return
    if amount < 0:
        await ctx.send('Amount must be positive!')
        return

    await update_bank(ctx.author,amount)
    await update_bank(ctx.author,-1*amount,'bank')
    await ctx.send(f'{ctx.author.mention} You withdrew {amount} coins')


@client.command(aliases=['dp','dep'])
async def deposit(ctx,amount = None):
    #test
    await open_account(ctx.author)
    if amount is None:
        await ctx.send("Please enter the amount")
        return

    bal = await update_bank(ctx.author)
    if amount in ("all", "max"):

      amount = int(bal[0])
   
    amount = int(amount)

    if amount > bal[0]:
        await ctx.send('You do not have sufficient balance')
        return
    if amount < 0:
        await ctx.send('Amount must be positive!')
        return



    await update_bank(ctx.author,-1*amount)
    await update_bank(ctx.author,amount,'bank')
    await ctx.send(f'{ctx.author.mention} You deposited {amount} coins')





@client.command(aliases=['sm'])
async def send(ctx,member : discord.Member,amount = None):
    await open_account(ctx.author)
    await open_account(member)
    if amount == None:
        await ctx.send("Please enter the amount")
        return

    bal = await update_bank(ctx.author)
    if amount == 'all':
        amount = bal[0]

    amount = int(amount)

    if amount > bal[0]:
        await ctx.send('You do not have sufficient balance')
        return
    if amount < 0:
        await ctx.send('Amount must be positive!')
        return

    await update_bank(ctx.author,-1*amount,'wallet')
    await update_bank(member,amount,'bank')
    await ctx.send(f'{ctx.author.mention} You gave {member} {amount} coins')
'''owner = 900992402356043806
@client.command()
@commands.cooldown(1, 60*60*24*7, commands.BucketType.user)
async def loan(ctx, amount : int):

    loan_available = int(client.open_account(owner)['wallet'])

    if int(amount) <= loan_available:

      time.sleep(1)

      await ctx.channel.send('You have been given ' + ''.join(str(amount) + ". You will have to pay " + str((int(amount)+int(amount)*0.1)) +" baguttes within 2 weeks."))

      await update_bank(ctx.author,+1*amount,'bank')


      must_pay.update({ctx.author.name:str(amount)})

    else:

        time.sleep(2)

        await ctx.channel.send("You Can only request a loan within "+str(loan_available))

    # New asyncio code
    
    await asyncio.sleep(60*60*24*7) # Wait for 60*60*24*7 seconds

    # Here, just add the code to take the money away after 60*60*24*7 seconds
'''
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
    #await ctx.send('hey stupid, why r u either robbing urself or a bot or a offline person now u might have to payback')
    if member.status == discord.Status.offline:

      await open_account(ctx.author)
      await open_account(member)
      bal = await update_bank(aut)
      earningd = random.randrange(0,bal[0])
  

      await update_bank(member,earningd)
      await update_bank(ctx.author,-1*earningd) 
      await update_bank(member,+1*earningd) 
      await ctx.send(f"You got caught while robbing {member} , and u payed them {earningd}.BE more pro next time :/")      

    return
  
  await open_account(ctx.author)
  await open_account(member)
  bal = await update_bank(member)

  if bal[0]<100:
    await ctx.send('It is useless to rob them :(')
    return

  earning = random.randrange(0,bal[0])
  

  await update_bank(ctx.author,earning)
  await update_bank(member,-1*earning)
  em = discord.Embed(title =f'{ctx.author} robbed {member}',description =f'{ctx.author.mention}  robbed {member} and got {m}{earning} ')
  emd = discord.Embed(title =f'{ctx.author} tried to robb You',description =f'{ctx.author}  tried to rob {member} and got {m}{earning} ')
  await ctx.send(embed=em)
  await member.send(embed=emd)

'''
@client.command()
async def slots(ctx,amount = None):
    #test
    await open_account(ctx.author)
    if amount == None:
        await ctx.send("Please enter the amount")
        return

    bal = await update_bank(ctx.author)

    amount = int(amount)

    if amount > bal[0]:
        await ctx.send('You do not have sufficient balance')
        return
    if amount < 0:
        await ctx.send('Amount must be positive!')
        return
    final = []
    for i in range(3):
        a = random.choice(['X','O','Q'])

        final.append(a)

    await ctx.send(str(final))

    if final[0] == final[1] or final[1] == final[2] or final[0] == final[2]:
        await update_bank(ctx.author,2*amount)
        await ctx.send(f'You won :) {ctx.author.mention}')
    else:
        await update_bank(ctx.author,-1*amount)
        await ctx.send(f'You lose :( {ctx.author.mention}')
'''
@client.command()
@commands.guild_only()
@commands.cooldown(rate=1, per=3.0, type=commands.BucketType.user)
async def slots( ctx, bet: int):
    await open_account(ctx.author)
    bal = await update_bank(ctx.author)
    amount = int(bet)

    if amount > bal[0]:
        await ctx.send('You do not have sufficient balance')
        return
    if amount < 0:
        await ctx.send('Amount must be positive!')
        return    
    if 1 > bet:
        return await ctx.send("Give some money! ;w;")

    losshearts = ["🖤", "💔"]
    doublehearts = ["❤️", "💚", "💛", "🧡", "💜", "💙"]
    triplehearts = ["💗", "💖","💟","🤎"]
    jackpothearts = ["💘"]
    hearts = {}
    heartlist = ["❤️", "🖤", "💗", "💚", "💖", "💛", "💔", "🧡", "💜", "💙", "💘","💟","🤎"]
    for x in range(1, 10):
        hearts[f"heart{x}"] = random.choice(heartlist)
    msg = await ctx.send(
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
        em2.add_field(name = f'{emoji} {name}', value = f" \n {desc}\nRarity : {com}",inline=False)
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
            await ctx.send("That Object isn't there!")
            return
        if res[1]==2:
            await ctx.send(f"You don't have enough money in your wallet to buy {amount} {item}")
            return

    buy = discord.Embed(title=item,description=f"You bought {amount} {item}",color=discord.Color.green())
    await ctx.send(embed=buy)

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

    await ctx.send(embed = em)
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

    await ctx.send(embed = em)    


@client.command()
@commands.max_concurrency(5,per=commands.BucketType.user,wait=False)
@commands.cooldown(1, 40, commands.BucketType.user)
async def dig(ctx):

    await open_account(ctx.author)
    user = ctx.author
    users = await get_bank_data()
    bag = users[str(user.id)].get("bag")


    if bag:
        if any(element['item'] == 'shovel' and element['amount'] > 0
              for element in bag):
            #items = ['junk','plastic']     
            earnings = random.randrange(700)
            em = discord.Embed(title ='Digged',description =f'{ctx.author.mention}digged and got  {earnings} ',color = discord.Color.green())
            await ctx.send(embed=em)

            users[str(user.id)]["wallet"] += earnings

            with open("mainbank.json",'w') as f:
                json.dump(users,f)
            
        else:

            await ctx.send('It seems like you dont have enough shovel are you fooling me')
    else:
        await ctx.send('I am not a mad go and buy a shovel first')
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
            await ctx.send("That Object isn't there!")
            return
        if res[1]==2:
            await ctx.send(f"You don't have {amount} {item} in your bag.")
            return
        if res[1]==3:
            await ctx.send(f"You don't have {item} in your bag.")
            return
    s = discord.Embed(title = "Sold",description =f"You just sold {amount} {item}",color=discord.Color.green())
    await ctx.send(embed=s)

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

    await ctx.send(embed = em)


# command to clear channel messages
@client.command(hidden=True)
@has_permissions(manage_messages=True)
async def clear(ctx, amount=5):
    #test
    await ctx.channel.purge(limit=amount)
    await ctx.send("Messages have been cleared")




@client.command()
async def ss(ctx, site):
    embed=discord.Embed(colour = discord.Colour.orange(), timestamp=ctx.message.created_at)
    embed.set_footer(text="Here is the website'ss you requested")
    embed.set_image(url=(f"https://image.thum.io/get/width/1920/crop/675/maxAge/1/noanimate/{site}"))
    await ctx.send(embed=embed)



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
 
# on_message event
@client.event
async def on_message(message):
    if f"<@!{client.user.id}>" in message.content:
      em = discord.Embed(title='I am tessarect',color=discord.Color.random())
        # This is how you call the prefix_check function. It takes a guild object
      em.description = 'Tessarect  (Formerly Amteor) Another general purpose discord bot but with Economy commands and much more Well Attractive , Economy and Leveling Bot with tons of features. Utitlity Bot , Music Bot , Economy Bot , Moderation Bot and much more .'
      #em.add_field(name="Servers", value=len(client.guilds))
      em.add_field(name="PREFIX",value=", ".join(prefix_check(message.guild)))
      await message.channel.send(embed=em)
    # Don't forget to process, otherwise your commands won't work!
		# if there is a discord nitro scam link in message content
      with urllib.request.urlopen('https://raw.githubusercontent.com/Jimmy-Blue/discord-scam-links/main/list.txt') as f:
        html = f.read().decode('utf-8')
      message.content = message.content.lower()
      for line in html.splitlines():
        if line in message.content:
          await message.delete()
          await message.channel.send(f"<@{message.author.id}>, sending a scam link is not allowed.")

    await client.process_commands(message)


@client.command()
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
                await ctx.send(line)
                line = ""
            else:
                line += " " + board[x]

        # determine who goes first
        num = random.randint(1, 2)
        if num == 1:
            turn = player1
            myEmbed = discord.Embed(title= "GAME IN PROGRESS",description="IT IS <@" + str(player1.id) + ">'s TURN.",color=0xe74c3c)
            await ctx.send(embed=myEmbed)
        elif num == 2:
            turn = player2
            myEmbed = discord.Embed(title= "GAME IN PROGRESS",description="IT IS <@" + str(player2.id) + ">'s TURN.",color=0xe74c3c)
            await ctx.send(embed=myEmbed)
    else:
        myEmbed = discord.Embed(title= "GAME IN PROGRESS",description="A GAME IS STILL IN PROGRESS. FINISH IT BEFORE STARTING A NEW ONE",color=0xe74c3c)
        await ctx.send(embed=myEmbed)

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
                        await ctx.send(line)
                        line = ""
                    else:
                        line += " " + board[x]

                checkWinner(winningConditions, mark)
                print(count)
                if gameOver == True:
                    myEmbed = discord.Embed(title= "WINNER!",description=mark + " :crown: ",color=0xf1c40f)
                    await ctx.send(embed=myEmbed)
                elif count >= 9:
                    gameOver = True
                    myEmbed = discord.Embed(title= "TIE",description="IT'S A TIE :handshake:",color=0xf1c40f)
                    await ctx.send(embed=myEmbed)

                # switch turns
                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1
            else:
                myEmbed = discord.Embed(title= "PLACE ERROR!",description="BE SURE TO CHOOSE AN INTEGER BETWEEN 1 AND 9 (INCLUSIVE) AND AN UNMARKED TILE. ",color=0xe74c3c)
                await ctx.send(embed=myEmbed)
        else:
            myEmbed = discord.Embed(title= "TURN ERROR!",description="IT'S NOT YOUR TURN",color=0xe74c3c)
            await ctx.send(embed=myEmbed)
    else:
        myEmbed = discord.Embed(title= "START GAME",description="TO START A NEW GAME, USE tictactoe COMMAND",color=0x2ecc71)
        await ctx.send(embed=myEmbed)


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
        await ctx.send(embed=myEmbed)
    elif isinstance(error, commands.BadArgument):
        myEmbed = discord.Embed(title= "ERROR!",description="PLEASE MAKE SURE TO MENTION/PING PLAYERS (ie. <@688534433879556134>)",color=0xe74c3c)
        await ctx.send(embed=myEmbed)

@place.error
async def place_error(ctx, error):
    #test
    if isinstance(error, commands.MissingRequiredArgument):
        myEmbed = discord.Embed(title= "NO POSITION",description="PLEASE ENTER A POSITION TO MARK",color=0xe74c3c)
        await ctx.send(embed=myEmbed)
    elif isinstance(error, commands.BadArgument):
        myEmbed = discord.Embed(title= "INTEGER ERROR!",description="PLEASE MAKE SURE IT'S AN INTEGER",color=0xe74c3c)
        await ctx.send(embed=myEmbed)
@client.command()
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
        await ctx.send(embed=myEmbed)        

'''
  if client.user.mentioned_in(message):



    em = discord.Embed(title ="Tessarect (Formely Tessarect (Formely Amteor))",color=discord.Color.green())
    em.add_field(name = "Default Prefix",value ="a!")      
    em.add_field(name="About ME",value ="Tessarect (Formely Tessarect (Formely Amteor)) Another general purpose discord bot but with Economy commands and much more Well Attractive , Economy and Leveling Bot with tons of features. Utitlity Bot , Music Bot , Economy Bot , Moderation Bot and much more . ",inline =False)
  
  
    await message.channel.send(embed=em)
  await client.process_commands(message) ''' 

from asyncio import TimeoutError

'''
@client.command()
async def bio(ctx,user:discord.Member=None):
    if user==None:
        user=ctx.author

    rlist = []
    for role in user.roles:
      if role.name != "@everyone":
        rlist.append(role.mention)

    b = ", ".join(rlist)


    embed = discord.Embed(colour=discord.Color.random(),timestamp=ctx.message.created_at)

    embed.set_author(name=user.name),
    embed.set_thumbnail(url=user.avatar_url),
    embed.set_footer(text=f'Requested by - {ctx.author}',
  icon_url=ctx.author.avatar_url)

    embed.add_field(name='ID:',value=user.id,inline=False)
    embed.add_field(name='Name:',value=user.display_name,inline=False)

    embed.add_field(name='Created at:',value=user.created_at,inline=False)
    embed.add_field(name='Joined at:',value=user.joined_at,inline=False)
    embed.add_field(name='Is Bot?',value=user.bot,inline=False)

    embed.add_field(name=f'Roles:({len(rlist)})',value=''.join([b]),inline=False)
    embed.add_field(name='Top Role:',value=user.top_role.mention,inline=False)

    await ctx.send(embed=embed)'''



@client.command()
@commands.cooldown(1,400,commands.BucketType.guild)
async def pickpocket(ctx):
  
    row = ActionRow(
        Button(
            style=ButtonStyle.green,
            label="Pickpocket!",
            custom_id="test_button"
        )
    )
    msg = await ctx.send("Pickpocket ", components=[row])

    # Here timeout=60 means that the listener will
    # finish working after 60 seconds of inactivity
    on_click = msg.create_click_listener(timeout=10)

    @on_click.not_from_user(ctx.author, cancel_others=True, reset_timeout=False)
    async def on_wrong_user(inter):
        # This function is called in case a button was clicked not by the author
        # cancel_others=True prevents all on_click-functions under this function from working
        # regardless of their checks
        # reset_timeout=False makes the timer keep going after this function is called
        await inter.reply("You're not the author", ephemeral=True)

    @on_click.matching_id("test_button")
    async def on_test_button(inter):
        # This function only works if the author presses the button
        # Becase otherwise the previous decorator cancels this one
        await msg.edit(components=[])
        await open_account(ctx.author)

        victim = random.choice(victims)
        value = random.randint(5,25)

        sucess = random.randint(1,100)
        if sucess >= 10:

          await add_money(ctx.author, value)
          sucs =discord.Embed(title =f'{ctx.author} attempted to pickpocket',description=f'``You attempted to pickpocket {victim} for {m}{value} and {random.choice(sucess_phrases)}.``')
          await ctx.channel.send(embed=sucs)
        else:

          await add_money(ctx.author, -value)
          await ctx.channel.send(f'``You attempted to pickpocket {victim} and {random.choice(fail_phrases)}. You lost {m}{value} in the process.``')
    @on_click.timeout
    async def on_timeout():
        await msg.edit(components=[])
inter_client = InteractionClient(client)
@inter_client.slash_command(description="Test command")
async def test(inter):
    await inter.reply("Test")


@inter_client.slash_command(
    description="Shows the avatar of the user",
    options=[
        Option("user", "Enter the user", OptionType.USER)
        # By default, Option is optional
        # Pass required=True to make it a required arg
    ]
)
async def avatar(inter, user=None):
    # If user is None, set it to inter.author
    user = user or inter.author
    # We are guaranteed to receive a discord.User object,
    # because we specified the option type as Type.USER

    emb = discord.Embed(
        title=f"{user}'s avatar",
        color=discord.Color.blue()
    )
    emb.set_image(url=user.avatar_url)
    await inter.reply(embed=emb)
@inter_client.message_command(name="Reverse")
async def reverse(inter: ContextMenuInteraction):
    # Message commands always have only this ^ argument
    if inter.message.content:
        # Here we will send a reversed message to the chat
        await inter.respond(inter.message.content[::-1])
    else:
        # Here we will explain that the message isn't valid
        await inter.respond("There's no content", ephemeral=True)

@client.group(invoke_without_command=True)
async def helpx(ctx):
    e = discord.Embed(title="Tessarect (Formely Tessarect (Formely Amteor)) Help",description="Here is a help for you ",color = 0x011D4F)
    e.add_field(name = "Utility",value ="Many useful commands s")
    e.add_field(name = "Moderation",value ="Many useful commands for managing your server like kick and warn")
    e.add_field(name = "Economy Commands",value ="Many interesting economy commands like rob ,bal or send")

    e.add_field(name = "Basic",value ="Some Basic Commands")
    e.add_field(name = "Fun Commands🎈",value ="Many interesting fun commands like 8ball ,ascii")
    e.add_field(name = "Music",value ="Listen to some music yay!")
    e.add_field(name = "Suggest",value ="Have an Idea on how we can imprve? use this command")  
    e.add_field(name = "Level",value ="Use Leveling Sys")
    e.add_field(name = "Others",value ="Other Commands that arent from any category")
    e.add_field(name = "Browsing",value ="Browse without leaving discord")
    e.add_field(name = "Information",value ="For Information by the Developers")
    e.set_footer(text="You can type help<category> for more help on a category")
    await ctx.send(embed =e)
@helpx.command()
async def utility(ctx):
  await ctx.send('this command is under progress kindly use help command till updates')
@helpx.command()
async def basic(ctx):
  await ctx.send('this command is under progress kindly use help command till updates')
'''
@client.command()
async def ping(ctx):
    if round(client.latency * 1000) <= 50:
        embed=discord.Embed(title="PING", description=f":ping_pong: Pingpingpingpingping! The ping is **{round(client.latency *1000)}** milliseconds!", color=0x44ff44)
    elif round(client.latency * 1000) <= 100:
        embed=discord.Embed(title="PING", description=f":ping_pong: Pingpingpingpingping! The ping is **{round(client.latency *1000)}** milliseconds!", color=0xffd000)
    elif round(client.latency * 1000) <= 200:
        embed=discord.Embed(title="PING", description=f":ping_pong: Pingpingpingpingping! The ping is **{round(client.latency *1000)}** milliseconds!", color=0xff6600)
    else:
        embed=discord.Embed(title="PING", description=f":ping_pong: Pingpingpingpingping! The ping is **{round(client.latency *1000)}** milliseconds!", color=0x990000)
    await ctx.send(embed=embed)
'''
@client.command()
async def joke(ctx): 

  page = requests.get('https://joke.deno.dev/')
  jokesource = json.loads(page.content)
  joke = jokesource['setup']
  print(joke)
  answer = jokesource['punchline']
  await ctx.channel.send(f"{joke} \n{answer}")

'''
@client.command()
@commands.max_concurrency(1,per=commands.BucketType.default,wait=False)
async def onewordtweet(ctx,member:discord.Member,msg): 
  if member==None:
    member=ctx.author
  page = f'https://some-random-api.ml/canvas/tweet?avatar={member.avatar_url_as(format="png", size=1024)}&username={member.name}&displayname={member.display_name}&comment={msg}'
  e=discord.Embed(title="Tweet",color=member.color)
  e.set_image(url=page)
  await ctx.send(embed=e)

@client.command()
@commands.max_concurrency(1,per=commands.BucketType.default,wait=False)
async def simpcard(ctx,member:discord.Member): 
  if member==None:
    member=ctx.author
  page = f'https://some-random-api.ml/canvas/simpcard?avatar{member.avatar_url_as(format="png", size=1024)}'
  e=discord.Embed(title="simpcard",color=member.color)
  e.set_image(url=page)
  await ctx.send(embed=e,page)
@client.command()
@commands.max_concurrency(1,per=commands.BucketType.default,wait=False)
async def stupid(ctx,member:discord.Member): 
  if member==None:
    member=ctx.author
  page = f'https://some-random-api.ml/canvas/its-so-stupid?avatar{member.avatar_url_as(format="png", size=1024)}&dog=im+stupid'
  e=discord.Embed(title="I am stupid",color=member.color)
  e.set_image(url=page)
  await ctx.send(embed=e,page)
@client.command()
@commands.max_concurrency(1,per=commands.BucketType.default,wait=False)
async def trash_img(ctx,member:discord.Member): 

  page = f'https://api.eriner.repl.co/image/trash?avatar={member.avatar_url_as(format="png", size=1024)}'
  e=discord.Embed(title="Trash ",color=member.color)
  e.set_image(url=page)
  await ctx.send(embed=e)
@client.command()
@commands.max_concurrency(1,per=commands.BucketType.default,wait=False)
async def gay(ctx,member:discord.Member): 

  page = f'https://api.eriner.repl.co/image/gay?avatar={member.avatar_url_as(format="png", size=1024)}'
  e=discord.Embed(title="GAY ",color=member.color)
  e.set_image(url=page)
  await ctx.send(embed=e)'''
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
@client.command(aliases=['c'])
#@commands.max_concurrency(1,per=commands.BucketType.default,wait=False)
async def chat(ctx,msg): 

  page = requests.get(f'https://api.spapi.ga/fun/chatbot?message={msg}&owner=SniperXi199&botname=Tessarect&user={ctx.author.id}')
  source = json.loads(page.content)
  res = source["response"]  
  await ctx.send(res)
@client.command()
@commands.max_concurrency(1,per=commands.BucketType.default,wait=False)
async def fact(ctx): 

  page = requests.get(f'https://api.eriner.repl.co/fun/uselessfact')
  source = json.loads(page.content)
  ft = source["fact"] 
  em=discord.Embed(title="A Fact...",description=ft,color=discord.Color.random())
  await ctx.send(embed=em)
@client.command(help="Shows info about a color by its hex")
@commands.max_concurrency(1,per=commands.BucketType.default,wait=False)
async def colorhex(ctx,hex): 

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
  await ctx.send(embed=emb)  


  

@client.command()
@commands.max_concurrency(1,per=commands.BucketType.default,wait=False)
async def kill(ctx,victim:discord.Member="Some One"): 
  if victim.id == 900992402356043806 or victim==client.user:
    return await ctx.send('Just shut up , go to heck u cant kill me or my owner stupid twit')
  page = requests.get(f'https://api.waifu.pics/sfw/kill')
  source = json.loads(page.content)
  url=source["url"]
  em=discord.Embed(description=f"{victim} is being ....",color=discord.Color.red())
  em.set_image(url=url)
  await ctx.send(embed=em)  
import psutil

startTime = time.monotonic()
@client.command(aliases=["bi", "about"])
async def bot( ctx):
    ser = len(client.guilds)
    mem = len(client.users)

    pre = ", ".join(prefix_check(ctx.message.guild))
    embed = discord.Embed(
        timestamp=ctx.message.created_at, title=":robot:  Bot Info", color=0x06c8f9
    )
    embed.set_thumbnail(url=client.user.avatar_url)
    embed.add_field(
        name="<:online_status:930347639172657164> Helping", value=f"{ser} servers"
    )
    embed.add_field(
        name="<a:panda:930348733844033576> Serving", value=f"{mem} members"
    )
    embed.add_field(name="<:blurple_slashcommands:930349698999537746> Prefix", value=f"`{pre}`")
    embed.add_field(
        name="<a:devserver:930350030072729620> Support Server",
        value="[Join My Server](https://discord.gg/avpet3NjTE)",
    )
    embed.add_field(
        name="<a:Diamond:930350459020017694> Add Me",
        value="[Click Here to Add Me](https://bit.ly/terrasectbot)",
    )
    embed.add_field(
        name="<:planet:930351400532201532>  Website",
        value="Under Development",
    )
    embed.add_field(
        name="🚀 Made By", value="SniperXi199#2209"
    )
    embed.set_footer(
        text=f"Requested By: {ctx.author.name}", icon_url=f"{ctx.author.avatar_url}"
    )
    await ctx.send(embed=embed)
@client.command()
async def stats(ctx):
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
    em=discord.Embed(title="Stats",description="Stats")
    em.add_field(name="Library", value=f"discord.py")
    em.add_field(name="Bot Latency", value=f"{client.ws.latency * 1000:.0f} ms")
    #em.add_field(name="Status Page", value=f"https://stats.uptimerobot.com/GA8lYTBq86")
    em.add_field(name="Version", value=f"·=»‡«=· 7.9.0·=»‡«=· ",inline=False)  
    em.add_field(name='Channels', value=f"{sum(1 for g in client.guilds for _ in g.channels)}")
    em.add_field(name='Total Members', value=client.users,inline=True)  
    em.add_field(name='Hosting Stats', value=f'Cpu usage- {psutil.cpu_percent(1)}%'
                          f'\n(Actual Cpu Usage May Differ)'
                          f'\n'

                          f'\nNumber OF Cores - {psutil.cpu_count()} '
                          f'\nNumber of Physical Cores- {psutil.cpu_count(logical=False)}'
                          f'\n'

                          f'\nTotal ram- {round(values24, 2)} GB'
                          f'\nAvailable Ram - {round(val4, 2)} GB',inline=False)
    em.set_footer(text="Support https://discord.gg/avpet3NjTE  ")  
    await ctx.send(embed=em)
@client.command()
async def goal(ctx):
  '''
  row = ActionRow(
        Button(
            style=ButtonStyle.link,
            label="Invite Me!",
            url='https://discord.com/api/oauth2/authorize?client_id=916630347746250782&permissions=8&scope=bot&applications.commands'
        )
    )    '''
  goal = 50
  currentg = len(client.guilds)
  em = discord.Embed(title="Bot Server Goal",description=f" Current Count {currentg}/{goal}",color=discord.Color.blue())
  em.set_footer(text="Kindly be kind enough to invite me in a server and contribute")
  
  if goal ==currentg:
    em.add_field(name='Congrats ',value=' I have achieved the current goal')
  else:
    em.add_field(name=":| Not yet" ,value=f"We still need {goal-currentg} servers more!")
  em.add_field(name="CONTRIBUTE by inviting me",value = "[INVITE](https://discord.com/api/oauth2/authorize?client_id=916630347746250782&permissions=8&scope=bot&applications.commands)")
  await ctx.send(embed=em)
# GIFs for Damn Son react
dms = ["https://giphy.com/gifs/batman-film-qVID3J8fLrlZK", "https://giphy.com/gifs/homer-simpson-barney-batman-and-robin-pSFEEQMaNcFAQ", "https://giphy.com/gifs/hug-5sos-5-seconds-of-summer-BcOvvS5t0sxnG", 'https://giphy.com/gifs/joker-the-joaquin-phoenix-A7ZbCuv0fJ0POGucwV']

# GIFs for LOL react
lolm = ['https://giphy.com/gifs/originals-lol-3o6ozvv0zsJskzOCbu', 'https://giphy.com/gifs/theoffice-episode-6-the-office-tv-bC9czlgCMtw4cj8RgH','https://giphy.com/gifs/moodman-lol-spit-take-Q7ozWVYCR0nyW2rvPW', 'https://giphy.com/gifs/moodman-funny-lol-laughing-fUYhyT9IjftxrxJXcE', 'https://giphy.com/gifs/laughing-despicable-me-minions-ZqlvCTNHpqrio', 
'https://giphy.com/gifs/laughing-applause-mike-tyson-wWue0rCDOphOE']

# GIFs for Yay reaction
yaym = [
    "https://giphy.com/gifs/F9hQLAVhWnL56",
    "https://giphy.com/gifs/thegifys-gifys-5xaOcLGvzHxDKjufnLW",
    "https://giphy.com/gifs/studiosoriginals-dog-josh-freydkis-bad-woof-l41Ym8O8dbIG0XvFK",
    "https://giphy.com/gifs/sherlockgnomes-sherlock-l4pTfx2qLszoacZRS",
    'https://giphy.com/gifs/foxinternational-reaction-simpsons-celebrate-26tPplGWjN0xLybiU',
    "https://giphy.com/gifs/excited-screaming-jonah-hill-5GoVLqeAOo6PK",
    "https://giphy.com/gifs/excited-yes-30-rock-I24hjk3H0R8Oc"
]



# GIFs for Yes Reaction
yesm = [
    "https://giphy.com/gifs/theoffice-MNmyTin5qt5LSXirxd",
    "https://giphy.com/gifs/DffShiJ47fPqM",
    "https://giphy.com/gifs/dYZuqJLDVsWMLWyIxJ"
]

susm = ["https://giphy.com/gifs/confused-futurama-suspicious-ANbD1CCdA3iI8","https://giphy.com/gifs/moodman-monkey-side-eye-sideeye-H5C8CevNMbpBqNqFjl","https://giphy.com/gifs/tiktok-cute-aww-jRHD367KLHU7NsPjmb",
"https://giphy.com/gifs/reaction-mood-3gNotAoIRZsb9UHPnj"]

# GIFs for No Reaction
nom = [
    "https://giphy.com/gifs/the-office-mrw-d10dMmzqCYqQ0",
    "https://giphy.com/gifs/NetflixisaJoke-netflix-iglesias-mr-h5cl6eHMvf0IQ3wJch",
    "https://giphy.com/gifs/memecandy-J46T6SB3yzwc4eBYeL"
]
from random import choice
@client.command()
async def yay(ctx):
    await ctx.send(choice(yaym))

@client.command()
async def lol(ctx):
    await ctx.send(choice(lolm))
@client.command()
async def yes(ctx):
    await ctx.send(choice(yesm))
@client.command()
async def no(ctx):
    await ctx.send(choice(nom))
@client.command()
async def sus(ctx):
    await ctx.send(choice(susm))
@client.command()
async def damnson(ctx):
    await ctx.send(choice(dms))
@client.command()
async def verify(ctx):
# Import the following modules
    from captcha.image import ImageCaptcha
    image = ImageCaptcha(width = 280, height = 90)
    captcha_text = str(random.randint(20000,300000))
    ## importing socket module
 
    host_name = socket.gethostname()    
    IPAddress = socket.gethostbyname(host_name)    
    print("Your Computer Name is:" + host_name)    
    print("Your Computer IP Address is:" + IPAddress) 
    #How to get the IP address of a client using socket module
    em = discord.Embed(title="VERIFY <:Protectedshield:922468797246488596>",description="Solve this Captcha to get access to the server",color=discord.Color.blue())
 
    print(captcha_text)
    data = image.generate(captcha_text)  
    image.write(captcha_text, 'CAPTCHA.png')   
    img = discord.File("CAPTCHA.png")
    #await ctx.send("Solve this Captcha:",file=img)
    file = discord.File("CAPTCHA.png", filename="CAPTCHA.png")
    em.set_image(url="attachment://CAPTCHA.png")
    await ctx.send(file=file, embed=em)
    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel

    msg = await client.wait_for("message", check=check)
    print(msg.content)
    if int(msg.content.lower()) == int(captcha_text):
        await ctx.send(f" {blueokay} Welcome to {ctx.guild.name} , YOU have been verified")
        role = discord.utils.get(ctx.guild.roles,name="Verified💠")

        print(str(role))
        await ctx.author.add_roles(role)
        
    else:
        await ctx.send(f"<:Warn:922468797108080660> Verification Failed, try again! , correct text was {captcha_text}")

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
    await ctx.send(embed=em)

@client.command(hidden=True)
@commands.cooldown(1,40,commands.BucketType.guild)
async def search(ctx):
    await open_account(ctx.author)
    user = ctx.author

    users = await get_bank_data()

    options = ['Socks',  'Toilet', 'Dog', 'Lawn','air','clothes','wine','Area 51','sink','gloves','car','shampoo']
    option1 = random.choice(options)
    options.remove(option1)
    option2 = random.choice(options)
    options.remove(option2)
    option3 = random.choice(options)
    li =[]
    li.append(option1)
    li.append(option2)
    li.append(option3)
    embed1 = discord.Embed(title='Choose your search place',description='What do you want to search', color=0xfcba03)
    embed1.add_field(name='search', value=f"``{option1}``,``{option2}``, ``{option3}`` ")
    await ctx.send(embed=embed1)

    def msg_check(m):
        return m.author == ctx.message.author and m.channel == ctx.channel

    try:
        response = await client.wait_for('message', check=msg_check, timeout=10.0)
        if str(response)in li:
            random_money = random.randint(0,2000)

            await ctx.send(f'``You searched {response.content} and found {m}{random_money} `` ')
            
            users[str(user.id)]["wallet"] += random_money

            with open("mainbank.json",'w') as f:
                json.dump(users,f)      
        else:
            await ctx.send('Bruh')    
    except asyncio.TimeoutError:
        await ctx.send('Dumbass you ran out of time')
 

# Responds to commands
@client.command(pass_context=True)
async def hypesquad(ctx, user: discord.Member):
    # Remove unnecessary characters
    hypesquad_class = str(user.public_flags.all()).replace('[<UserFlags.', '').replace('>]', '').replace('_',
                                                                                                         ' ').replace(
        ':', '').title()

    # Remove digits from string
    hypesquad_class = ''.join([i for i in hypesquad_class if not i.isdigit()])

    # Output
    test = discord.Embed(title=f"{user.name} User's Badges", description=f"{hypesquad_class}", color=0xff0000)
    await ctx.channel.send(embed=test)
with open('text files/badwords.txt', 'r') as f:
    global filter
    words = f.read()
    filter = words.split()



@client.command()
async def report( ctx, user : discord.Member, *reason):
    em = discord.Embed(title=f'Report {user}?',description="Are you sure you want to report that user , if yes choose report categories .")
    msg = await ctx.send(
        embed=em,
        components=[
            SelectMenu(
                custom_id="test",
                placeholder="Choose the needed choices",
                options=[
                    SelectOption("Used bad words via /for bot or anyone", "value 1"),
                    SelectOption("Used amteor currency for buying /trading anyother real existence item", "value 2"),
                    SelectOption("Made Tessarect (Formely Tessarect (Formely Amteor)) say foul/swearing words by any means ", "value 3"),
                    SelectOption("Breaking other rules","value 4"),
                    SelectOption("Something Else to be there in the reason","value 5"),
                    SelectOption("Reporting a staff","value 6"),
                    SelectOption("Appealing reconsideration in previously done ban or some other action","value 7"),
                    SelectOption("*Thuged* (Any kind of CHeating)","value 8")
                ]
            )
        ]
    )
    row = ActionRow(
        Button(
            style=ButtonStyle.green,
            label="Send as Solved",
            custom_id="y"
        ),
             Button(
            style=ButtonStyle.green,
            label="Mark as not important",
            custom_id="x"
        )
    )
    inter = await msg.wait_for_dropdown(timeout=60)
    # Send what you received
    if inter.author == ctx.author:

      labels = [option.label for option in inter.select_menu.selected_options]
      await inter.reply('YOUR REQUEST HAS BEEN SENT SUCCESSFULLY , YOU MAY BE CONTACTED SO KEEP YOUR DMS OPEN .')
     
    channel = client.get_channel(929333373913137224) #since it's a cog u need self.bot
    author = ctx.message.author
    rearray = ' '.join(reason[:]) #converts reason argument array to string

    if not rearray: #what to do if there is no reason specified
        await channel.send(f"{author} has reported {user}, reason: Not provided , Parameters {', '.join(labels)}", components=[row])
        on_click = msg.create_click_listener(timeout=60)        
        await ctx.message.delete() #I would get rid of the command input
    else:
        await channel.send(f"{author} has reported {user}, reason: {rearray}, Parameters {', '.join(labels)}", components=[row])
        on_click = msg.create_click_listener(timeout=60)   
        await ctx.message.delete() 
    @on_click.matching_id("x")
    async def on_test_button(inter):
        await inter.author.send("YOUR REQUEST HAS BEEN DENIED")


@client.command() 
async def features(ctx):

    contents = ["AMTEOR FEATURES",""""**Economy Bot**\n
Supports various economy commands like balance , send , rob to make the server more interactive""",
"""**Moderator Commands\n**
Moderation using bot , use Mute , kick ban etc""",
"""**Fully Open Source**
The code of the bot is open source so you dont have to worry about your privacy .""",
"""**Utility Commands**
Commands to make your work easier and faster like avatar{user} gets the avatar of the mentioned user""",
"""**Leveling System**
Enjoy and use Tessarect (Formely Tessarect (Formely Amteor))'s leveling system for your server . Make a rank system""",
"""**Fun Commands**
Enjoy various fun commands such as ascii font , emojify , avatar lookup , info or play tictactoe with someone""",
"""**Secured**
This bot is fully secured by 3 reasons .
Open sourced| It is open sourced so you can know what all things are collected or how the commands work
Permission Checks| There are permision checks for commands like mute , kick or ban. But still if any commands do not have , please report the error to us using the feedback command.""",
"""**Ticket System**
Is your Server messed up with feedback? Or do you not know where is a particular Suggestion? Or you are bored with one channel for suggestion which is filled with messages? If you answered any of these questions in yes , We are here to help you . Tessarect (Formely Tessarect (Formely Amteor)) Provides a ticketing system so people can use the command [prefix]new to make a ticket and support team roles can close them . You can even add valid i.e support team roles or pinging roles that get pinged everytime anyone makes a ticket.""","""**Watching Suggestions**
Your feedback is our priorty . We watch for your queries too . Do you have one ? Join our server -Click Here or use command query or suggest to send feedback from your server only""","""**Translation**
Have you ever faced problem in understanding some foriegn language in a server? No need to go out of discord to use a translater , use amteor translation command (syntax - {prefix}translate {language} {text})""","""**And Much More**"""]
    pages = len(contents)
    cur_page = 1
    message = await ctx.send(embed=discord.Embed(description=f"{contents[cur_page-1]}", color=discord.Color.blue()))


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
                if cur_page==8:
                    em=discord.Embed(description=f"{contents[cur_page-1]}", color=discord.Color.blue())

                else:
                    em=discord.Embed(description=f"{contents[cur_page-1]}", color=discord.Color.blue())
                
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

      #requestCopyright = request['copyright']
      requestDate = request['date']
      requestTitle = request['title']
      requestHDUrl = request['hdurl']
      requestUrl = request['url']
      embednasa = discord.Embed(title = "**Today's NASA Astronomogy Image of the Day**", description = f"{requestTitle} ({requestDate})", color=0x09ec23, url=requestHDUrl)

      embednasa.set_author(name = f"NASA API  ", icon_url = "https://api.nasa.gov/assets/img/favicons/favicon-192.png")
      embednasa.set_image(url=requestUrl)
      embednasa.set_footer(text="Press the blue text to see the full resolution image!")
      await ctx.send(embed=embednasa)
      #jsonOpen = open('./api/nasa_used.json')
      #jsonLoad = json.load(jsonOpen)
      #nasaUsed = int(jsonLoad['nasa']) + 1
     # nasanewUsed = {"nasa": nasaUsed}
      #jsonString = json.dumps(nasanewUsed)
      #jsonFile = open("./api/nasa_used.json", "w")
      #jsonFile.write(jsonString)
      #jsonFile.close()

def restart_bot(): 
  os.execv(sys.executable, ['python'] + sys.argv)
@client.command()
async def readfile(ctx,file):

  with open(file) as f:

    content = "\n".join(f.readlines())

  await ctx.send(f"```{content}```")
'''
@client.command(name= 'restart')
@commands.check(check_Mod)
async def restart(ctx):
  e = discord.Embed(title='🕐',description='Restarting.. Scheduled , in approx 7 seconds')
  e3= discord.Embed(title='<:Protectedshield:922468797246488596>',description="Unloaded Cogs,Final Works , **RESTARTING BOT IN 3 SECONDS FROM THIS EDIT**")
  e2= discord.Embed(title='<a:Loading:922468614009925692>',description="Unloading cogs")  
  x = await ctx.send(embed=e)

  await x.edit(embed=e2)
  for filename in os.listdir("./cogs"):
      if filename.endswith(".py"):
          client.unload_extension(f"cogs.{filename[:-3]}")

  await x.edit(embed=e3)  

  restart_bot()
'''



def replace_chars(stri):
    stri2 = ""
    for char in stri:
        if char not in "<@!>":
            stri2 += char
    # print (f'stri2 is {stri2}')
    return stri2

@client.command(name = 'uno', help="The classic Uno you know and love! (Only 2 players.) Use <prefix>uno @other-player to start. Play cards simply by typing their names into the chat.")
async def uno(ctx, *args):
    await ctx.send("Hi! Let's play some UNO!")
    unocards = [
        'r0','r1', 'r2', 'r3', 'r4', 'r5', 'r6', 'r7','r8','r9','r1', 'r2', 'r3', 'r4', 'r5', 'r6', 'r7','r8','r9',
        'b0','b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7','b8','b9','b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7','b8','b9',
        'y0','y1', 'y2', 'y3', 'y4', 'y5', 'y6', 'y7','y8','y9','y1', 'y2', 'y3', 'y4', 'y5', 'y6', 'y7','y8','y9', 
        'g0','g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7','g8','g9','g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7','g8','g9',
        'dr4', 'dr4', 'dr2', 'dr2'
    ]
    
    # for item in args:
    #    for ris in item:
    #        print(ris)
    if not args:
        await ctx.send("Who would you like to play with? (If you need help, do <PREFIX>.help uno)")
    
    else: 
        arg = args[0]
        if arg == 'com':
            await ctx.send("Sorry, we are still building this functionality!")
        elif arg == 'help':
           await ctx.send("Instructions \n") 
           await ctx.send("")
        elif arg[1] == '@': 
            # print(f'arg is {arg}')
            # print(f'replacecharsarg is {replace_chars(arg)}')
            player2 = client.get_user(int(replace_chars(arg)))
            player1 = ctx.author
            message = f"Let's play with <@{player1.id}> and <@{player2.id}>. ! Check your DMs to see your cards. Please note that UNO will time out after 5 minutes without a turn played."
            await ctx.send(message)        
            #currGame = Game(ctx.author)
            deck = [
               'r0','r1', 'r2', 'r3', 'r4', 'r5', 'r6', 'r7','r8','r9','r1', 'r2', 'r3', 'r4', 'r5', 'r6', 'r7','r8','r9',
               'b0','b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7','b8','b9','b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7','b8','b9',
               'y0','y1', 'y2', 'y3', 'y4', 'y5', 'y6', 'y7','y8','y9','y1', 'y2', 'y3', 'y4', 'y5', 'y6', 'y7','y8','y9', 
               'g0','g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7','g8','g9','g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7','g8','g9',
               'dr4', 'dr4', 'dr2', 'dr2'
            ]
            startcard = random.sample(deck, 1)[0]
            firstCard = f'Here is the starting card: {startcard}. Make sure to wait until it is your turn to play!'
            await ctx.send(firstCard)
            p1deck = random.sample(deck, 7)
            for element in p1deck:
                if element in deck:
                    deck.remove(element) 
            await player1.create_dm()
            
            await player1.dm_channel.send("You will be going first! Type the card name in the general chat. Make sure to not violate the rules of UNO! (or else the bot crashes! (totally intended)")
            p2deck = random.sample(deck, 7)
            for element in p2deck:
                if element in deck:
                    deck.remove(element) 
            await player2.create_dm()
            
            # await ctx.send(p2)
            waitp1 = "It is currently ", player2, "'s turn, please wait."
            waitp2 = "It is currently ", player1, "'s turn, please wait."
            #await player2.dm_channel.send(waitp2)
            # await ctx.send(waitp2)

            player1Turn = True
            stack = [startcard]
            
            while len(p1deck) != 0 and len(p2deck) != 0:
                #while they are not empty, play
                p1 = f'Your current deck: {p1deck}'
                await player1.dm_channel.send(p1)
                p2 = f'Your current deck: {p2deck}'
                await player2.dm_channel.send(p2)
                def check(x):
                    # print(f'x is {x}')
                    return x.author.id == player1.id or x.author.id == player2.id

                currentCard = stack[-1]
                # await ctx.send("Next person, go! (rm)")
                arg = await client.wait_for('message', check=check, timeout=300)
                rcard = arg.content
                # await ctx.send(rcard)

                # print(f'currentcard: {currentCard}')

                if rcard == 'draw':
                    rand = random.sample(deck, 1)
                    
                    if player1Turn:
                        p1deck.extend(rand)
                    
                    else:
                        p2deck.extend(rand)
                    player1Turn = not player1Turn
                    
                elif rcard[0] == currentCard[0] or rcard[1] == currentCard[1] or rcard[0] == 'd':
                    
                    if player1Turn:
                        p1deck.remove(rcard)
                    
                    else:
                        p2deck.remove(rcard)
                    
                    if rcard[0] != 'd':
                        currentCard = rcard
                        stack.append(currentCard)
                        curr = f"Current Card: {currentCard}"
                        await ctx.send(curr)
                    
                    if rcard == 'dr2': 
                        draw = random.sample(deck, 2) 
                        for element in draw:
                            if element in deck:
                                deck.remove(element)
                        if player1Turn: 
                            p2deck.extend(draw)
                        else:
                            p1deck.extend(draw)
                    
                    elif rcard == 'dr4':
                        draw = random.sample(deck, 4)
                        for element in draw:
                            if element in deck:
                                deck.remove(element)
                        if player1Turn:
                            p2deck.extend(draw)
                        else:
                            p1deck.extend(draw)
                    player1Turn = not player1Turn
                
                else:
                    await ctx.send("This card does not work, please try another one")
            
            if len(p1deck) == 0:
                await ctx.send("Game over! Player One has won!")
            elif len(p2deck) == 0:
                await ctx.send("Game over! Player Two has won!")
def check_Mod(ctx):
    with open('Dev.txt') as f: # do change the 'Mod.txt' to the name that suits you. Ensure that this file is in the same directory as your code!
        
        if str(ctx.author.id) in f.read(): # this is reading the text file and checking if there's a matching string
            return ctx.author.id 
        
          
@client.command()
@commands.check(check_Mod)
async def dev_test(ctx):
    await ctx.send("You are a dev!")
@client.command()
@commands.check(check_Mod)
async def add_dev(ctx, user:discord.Member=None):
    if user == None:
        await ctx.send("Please provide a user to add as a Mod!")
        return

    # First we'll make some functions for cleaner, more readable code #

    def is_Mod(user_id): 
    ## This function will check if the given id is already in the file. True if in file, False if not ##
        with open('Dev.txt', 'r') as f:
            if str(user_id) in f.read():
                return True
            else:
                return False

    def add_Mod(user_id):
    ## This function will add the given user id into the given text file, Mod.txt ##
        with open('Dev.txt', 'a') as f: # 'a' is used for appending, since we don't want to overwrite all the ids already in the file
            f.write(f"{str(user_id)}\n")
            f.close()

    # Now we put those functions to use #
    if is_Mod(user.id) == True:
        await ctx.send(f"The user {user} is already a Dev!")
    else:
        add_Mod(user.id)
        await ctx.send(f"{user} added as a Dev!")  
     
web.keep_alive()
client.run(os.environ['token'],reconnect=True)


