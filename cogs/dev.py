import datetime
import traceback
import discord
import requests
from  colorama import Fore , Style
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
from discord.ext import commands
from discord.ext.commands import check
import os
import textwrap
from contextlib import redirect_stdout
import asyncio
import sys
import assets.otp_assets
import assets.reactor
import subprocess
from subprocess import Popen, PIPE
import shlex
import json
def restart_bot(mode): 
  if mode ==1:
    os.execv(sys.executable, ['python'] + sys.argv)
  if mode==2:
    os.system('busybox reboot')
def devc(ctx):
  with open("storage/dev.json") as f:
      dev_users_list = json.load(f)
      if ctx.author.id not in dev_users_list:
          return False
  return True


class Dev(commands.Cog):
    def __init__(self, client):
        self.bot = client
        self._last_result = None
 
    @staticmethod
    def cleanup_code(content):
        """Automatically removes code blocks from the code."""
        # remove ```py\n```
        if content.startswith("```") and content.endswith("```"):
            return "\n".join(content.split("\n")[1:-1])

        # remove `foo`
        return content.strip("` \n") 
    @commands.command(help="The main command check that you are a dev soul")    
    async def devtest(self,ctx,user:discord.Member=None):
      if not user:
        user=ctx.author
      with open("storage/dev.json") as f:

        dev_users_list = json.load(f)
      if user.id not in dev_users_list:

          await ctx.send(
              embed=discord.Embed(
                  title="<:Warn:922468797108080660> Permission Denied",
                  description="Dude! that's not a dev",
                  color=discord.Color.red(),
              )
          )          
      else:
        owner='True <:owner:946288312220536863>' if user.id==900992402356043806 else False
        await ctx.send(
            embed=discord.Embed(
                title="<a:Tick:922450348730355712> Verified",
                description=f"Found entry in Database. {user} is a developer \n The lord? {owner}",
                color=discord.Color.green(),
            )
        )        

    @commands.command(help="Lists Some poor souls having dev access for me" ,aliases=['devlist'])
    @check(devc)
    async def listdev(self,ctx):
        x = discord.Embed(description="Users having Dev access for me",color=0x34363A)
        with open("storage/dev.json") as f:
            dev_users_list = json.load(f)
        pa =1
        for user in dev_users_list:
          
          e = self.bot.get_user(user)
          x.add_field(name="_ _",value=e,inline=False)
          pa +=1
        x.set_footer(text=f"Total users : {pa-1}")
        await ctx.send(embed=x)

    @commands.command(help="Lists Some idiots who cant even use me",aliases=['blist','blacklisted'])
    @check(devc)
    async def listblack(self,ctx):
        x = discord.Embed(description="<:dnd_status:946652840053600256> Blacklisted User",color=0x34363A)
        with open("storage/black.json") as f:
            dev_users_list = json.load(f)
        pa =1
        for user in dev_users_list:
          
          e = self.bot.get_user(user)
          x.add_field(name=e,value=e.id,inline=False)
          pa +=1
        x.set_footer(text=f"Total users : {pa-1}")
        await ctx.send(embed=x)        
    @commands.command(help="Dont have silly juicy ideas used for adding some more devs (imagine my owner is too poor)")
    @check(devc)
    async def adddev(self,ctx, user : discord.Member):
  

        with open("storage/dev.json") as f:
            dev_users_list = json.load(f)

        if user.id not in dev_users_list and not user.bot:
            dev_users_list.append(user.id)

            with open("storage/dev.json", "w+") as f:
                json.dump(dev_users_list, f)

            await ctx.send(f"{user.mention} has been added!")  
        else:
          await ctx.send('See Developer , either you are adding a dev again as dev or a bot (bots arent that much cool)') 
    @commands.command(help="Removes a silly soul having dev access ")
    @check(devc)
    async def removedev(self,ctx, user : discord.Member):
        with open("storage/dev.json") as f:
            dev_users_list = json.load(f)

        if user.id in dev_users_list:
            dev_users_list.remove(user.id)
        else:
            await ctx.send(f"{user.mention} is not in the list, so they cannot be removed!")
            return

        with open("storage/dev.json", "w+") as f:
            json.dump(dev_users_list, f)

        await ctx.send(f"{user.mention} has been removed!")                   
    @commands.command(aliases=["m","evaldev","deveval","eval"],help="Execuete some stuff")
    @check(devc)  
    async def python_shell(self, ctx, *, code):
      if ctx.guild.id !=912569937116147772:
        
        re = discord.Embed(
            title="Unverified Server",
            description=f"{ctx.author.mention} This command is now only for the main server which is Tessa Bot Developers",
            color=discord.Color.blue(),
        )
        await ctx.send(embed=re)  
        re.title=" Attempt of using deveval outside TBD"
        re.description=f"{ctx.author.mention} Tried to use dev eval outside TBD but failed \n Requested Code \n `{code}`"
        devchannel=self.bot.get_channel(979345665081610271)
        return await devchannel.send(embed=re)
      env = {
          "ctx": ctx,
          "discord": discord,
          "commands": commands,
          "client":ctx.bot,
          "__import__": __import__,
          "guild":ctx.guild,
          "last_result":self._last_result 
          
      }
      code = code.replace("```py", "")
      code = code.replace("```", "")
      if  "client.http.token" in code:
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
          ecolor = 0x00ff00

      except Exception as error:
          output = error.__class__.__name__+": "+str(error)
          ecolor = 0xe60000
      self._last_result = "Last Result\n"+str(output)
      embed = discord.Embed(title="Eval",description="```\n"+str(output)+"\n```",colour=ecolor,timestamp=ctx.message.created_at)
  
  
      embed.set_author(name=ctx.author.display_name,icon_url=ctx.author.avatar_url)
      await ctx.reply(embed=embed)

               
    @commands.command(name= 'restart',help='Hidden command, youre not supposed to access this.Now off you go. Nothing to see here.',aliases=['reboot'])
    @check(devc)
    async def restart(self,ctx,mode:int=1):
      listd=[1,2] 
      if mode not in listd:
        dd = discord.Embed(title='Invalid Input',description=f' Invalid Mode = {mode} \n Accepted mode {listd}',color=discord.Color.red())          
        await ctx.send(embed=dd)     
        return
      otp_success = await assets.reactor.reactor(ctx, self.bot, 'Do you want to continue the restart ', color=0x607d8b,usr=ctx.author)
      # random otp generator. if user enters correct otp, returns true. else, returns false
      if not otp_success:
          return 
      if len(self.bot.voice_clients)>0:
        await ctx.send(embed=discord.Embed(description=f"There are {len(self.bot.voice_clients)} servers listening to music through Tessarect, Do you wanna restart?"))
        otp_success = await assets.reactor.reactor(ctx, self.bot, 'Do you want to continue the restart process while people are listening to me ', color=0x607d8b,usr=ctx.author)
        if not otp_success:
            return 
      modedict={1:'Simple restart',2:'Advanced RESTART'}
      e = discord.Embed(title='Restarting Started',description=f'**Mode = {mode}**\n{modedict[mode]}',color=discord.Color.dark_grey())
      e.add_field(name="Progress",value='11%')
      x = await ctx.send(embed=e)
      await asyncio.sleep(1)  
      e.set_field_at(0,name="Progress",value='33%')
      await x.edit(embed=e)
      await asyncio.sleep(2)
      e.set_field_at(0,name="Progress",value='66%')
      e.add_field(name="Status",value='Unloading Cogs')
      await x.edit(embed=e)        


      for filename in os.listdir("./cogs"):   
        try:
          
          self.bot.unload_extension(f"cogs.{filename[:-3]}")
        except Exception as ex:
          print(f'{filename} - {ex}')         

      e.set_field_at(0,name="Progress",value='99%')
      
      e.set_field_at(1,name="Status",value='Changing Status')
      e.color=discord.Color.dark_blue()
      await asyncio.sleep(1)
      e.set_field_at(1,name="Status",value='Restarted')
      e.color=discord.Color.blue()
      await x.edit(embed=e)
      await self.bot.change_presence(
              status=discord.Status.idle,
              activity=discord.Activity(                 
                  type=discord.ActivityType.watching,
                  name= f"🚀 System Reboot "
              ))
      with open("./storage/reboot.json", "w") as rebootFile:
          json.dump(ctx.message.channel.id, rebootFile) 
      
           
      restart_bot(mode)  




    @commands.command(name='reload', description="Reload all/one of the bot's cogs.\n"
                                                 "This is Dev-only, so don't have any Devny ideas.", )
    @check(devc)
    async def reload(self, ctx, cog=None):
        async with ctx.typing():
            if not cog:
                embed = discord.Embed(title="Reloading cogs!",timestamp=ctx.message.created_at,color=discord.Color.blue())
                for ext in os.listdir("./cogs/"):
                    if ext.endswith(".py") and not ext.startswith("_"):
                        try:
                            self.bot.unload_extension(f"cogs.{ext[:-3]}")
                            self.bot.load_extension(f"cogs.{ext[:-3]}")
                            embed.add_field(
                                name=f"Reloaded: `{ext}`", value='\uFEFF', inline=False)

                        except Exception as e:
                            embed.add_field(
                                name=f"Failed to reload: `{ext}`", value=str(e), inline=False)

                        await asyncio.sleep(0.5)
                await ctx.send(embed=embed)
                return


            embed = discord.Embed(
                title=f"Reloading {cog}!", timestamp=ctx.message.created_at)
            #embed.color=discord.Color.green()
            ext = f"{cog.lower()}.py"
            if not os.path.exists(f"./cogs/{ext}"):
                embed.add_field(
                    name=f"Failed to reload: `{ext}`", value="This cog does not exist.", inline=False)
                embed.color=discord.Color.red()

            elif ext.endswith(".py") and not ext.startswith("_"):
                try:
                    self.bot.unload_extension(f"cogs.{ext[:-3]}")
                    self.bot.load_extension(f"cogs.{ext[:-3]}")
                    embed.description=f"Reloaded: `{ext}`"
                    embed.color=discord.Color.dark_theme()
                except Exception:
                    desired_trace = traceback.format_exc()
                    if len(desired_trace) > 2500 :
                      print(desired_trace)
                      embed.description=f"Failed to reload: `{ext}`Too Big error , printed instead"
                    else:
                      embed.description=f"Failed to reload: `{ext}`"                     
                    embed.color=discord.Color.red()
            await ctx.send(embed=embed)

    @commands.command(name='load', description='Loads a cog. Mention the python file\'s name as `cog_file_name`')
    @check(devc)
    async def load_cog(self, ctx, cog_file_name):
        embed = discord.Embed(title=f"Loading Cog {cog_file_name}.py!", 
                              timestamp=ctx.message.created_at)
        if os.path.exists(f"./cogs/{cog_file_name}.py"):
            try:
                self.bot.load_extension(f"cogs.{cog_file_name}")
                embed.add_field(
                    name=f"Loaded: `{cog_file_name}.py`", value='\uFEFF', inline=False)
                #embed.color=discord.Color.green()
            except Exception as e:
                embed.add_field(
                    name=f"Failed to load: `{cog_file_name}.py`", value=str(e), inline=False)
               # embed.color=discord.Color.red()
            await ctx.send(embed=embed)

    @commands.command(name='unload', description="Unloads a cog. Mention the python file\'s name as `cog_file_name`")
    @check(devc)
    async def unload_cog(self, ctx, cog_file_name):
        embed = discord.Embed(title=f"Unloading Cog {cog_file_name}.py!", color=discord.Color.random(),
                              timestamp=ctx.message.created_at)
        if os.path.exists(f"./cogs/{cog_file_name}.py"):
            try:
                self.bot.unload_extension(f"cogs.{cog_file_name}")
                embed.add_field(
                    name=f"Unloaded: `{cog_file_name}.py`", value='\uFEFF', inline=False)
                embed.color=discord.Color.green()
            except Exception as e:
                embed.add_field(
                    name=f"Failed to unload: `{cog_file_name}.py`", value=str(e), inline=False)
                embed.color=discord.Color.red()
            await ctx.send(embed=embed)

    @commands.command(name="gitpull",help="Pull stuff from my github repo")
    @commands.guild_only()
    @check(devc)
    async def update(self, ctx):
        async with ctx.typing():
            print(sys.argv)
            print(sys.path)
            with open("./storage/update.txt", "w") as output:
                subprocess.call(["git", "pull"], stdout=output)
            with open("./storage/update.txt", "r") as output:
                file = discord.File(output)
        await ctx.send(content="Done! Output in text file", file=file)
        await asyncio.sleep(1)
        try:
            os.remove("./storage/update.txt")
        except:
            pass

    @commands.command(name="loadjsk")
    @check(devc)
    async def loadjsk(self, ctx):
        async with ctx.typing():
            try:
                self.bot.load_extension("jishaku")
            except commands.ExtensionAlreadyLoaded:
                pass
            except commands.ExtensionNotFound:
                em =discord.Embed(description="Couldnt not Load jsk")
                return await ctx.send(embed=em)
            em =discord.Embed(description="Loaded")    
            await ctx.send(embed=em)

    @commands.command(name="unloadjsk")
    @check(devc)
    async def unloadjsk(self, ctx):
        async with ctx.typing():
            try:
                self.bot.unload_extension("jishaku")
            except commands.ExtensionNotLoaded:
                pass
            except commands.ExtensionNotFound:
                return await ctx.send("Could not unload!")
            await ctx.send("Unloaded!")
    @commands.command(help="Blacklist some idiot from using me")
    @check(devc)
    async def blacklist(self,ctx, user : discord.Member,*,reason:str):
        with open("storage/black.json") as f:
            users_list = json.load(f)
        if user.id==ctx.author.id:
          return await ctx.send('You cant blacklisted yourself')
        if user.id not in users_list  :
            users_list.append(user.id)
            e=discord.Embed(title="Blacklisted User!",description=f":white_medium_square: Member {user.mention}\n:white_medium_square:Reason: {reason}\n :white_medium_square: Developer {ctx.author.mention}",color=discord.Color.red())  
            e.set_author(name=user.name,icon_url=user.avatar_url)            
            logschannel=self.bot.get_channel(979345665081610271)
            await logschannel.send(embed=e)
            with open("storage/black.json", "w+") as f:
                json.dump(users_list, f)
            
            await ctx.send(f"{user.mention} has been added!")  
        else:
          await ctx.send('See Developer , either you are adding a blacklisted user again ') 
    @commands.command(help="Unblacklist some users if they are behaving nice")
    @check(devc)
    async def unblacklist(self,ctx, user : discord.Member):
        with open("storage/black.json") as f:
            users_list = json.load(f)

        if user.id in users_list:
            users_list.remove(user.id)
            e=discord.Embed(title="UnBlacklisted User!",description=f":white_medium_square: Member {user.mention}\n :white_medium_square: Developer {ctx.author.mention}",color=discord.Color.gold())  
            e.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
            logschannel=self.bot.get_channel(979345665081610271)
            await logschannel.send(embed=e)            
        else:
            await ctx.send(f"{user.mention} is not in the list, so they cannot be removed!")
            return

        with open("storage/black.json", "w+") as f:
            json.dump(users_list, f)

        await ctx.send(f"{user.mention} has been removed!")  

           

    @check(devc)
    @commands.command(hidden=True,help="get info on all my guilds , add False to get Compact Info")
    async def servers(self,ctx,compact=True):       
        activeservers = self.bot.guilds
        if not compact:
          for guild in activeservers:
              name=str(guild.name)
              description=str(guild.description)
              owner=str(guild.owner)
              _id = str(guild.id)
              region=str(guild.region)
              memcount=str(guild.member_count)
              icon = str(guild.icon_url)
              ver = str(ctx.guild.verification_level)
              embed=discord.Embed(
                      title=name +" Server Information",
                      description=description,
                      color=discord.Color.blue()
                      )
              embed.set_thumbnail(url=icon)
              embed.add_field(name="Owner",value=owner,inline=True)
              embed.add_field(name="Server Id",value=_id,inline=True)
              embed.add_field(name="Region",value=region,inline=True)
              embed.add_field(name="Member Count",value=memcount,inline=True)
              embed.add_field(name="Verification Level",value=ver,inline=True)
  
              await ctx.send(embed=embed)
        else:
          embed=discord.Embed(title="My Guilds",color=discord.Color.dark_theme())
          for guild in activeservers:
            embed.add_field(name=guild,value=f"({str(guild.id)}) -{str(guild.member_count)} **({str(guild.owner)})**",inline=False)
          await ctx.send(embed=embed) 
    @check(devc)
    @commands.command()
    async def reply(self,ctx,member:discord.User,*,content:str):
      
      embed = discord.Embed(timestamp=ctx.message.created_at,description=content, color=0x8df2db)
     
      embed.set_footer(text=f"Sent by  {ctx.author}")
  
      try:
        await member.send(embed=embed)      
      except:
        await ctx.send(embed=discord.Embed(title="User has DM's Disabled",color=discord.Color.red()))
        return
      await ctx.send(embed= discord.Embed(title=f"<:user:941986233574367253> DM SENT <:sucess:935052640449077248> ", description=f"Your Message was Successfully Sent.", timestamp=ctx.message.created_at, color=0x02e7e7))
    @check(devc)
    @commands.command(hidden=True)
    async def invservers(self,ctx):
        invites = []
        em=discord.Embed(color=discord.Color.dark_theme())
        for guild in self.bot.guilds:
            for c in guild.text_channels:
                if c.permissions_for(guild.me).create_instant_invite:  # make sure the bot can actually create an invite
                    invite = await c.create_invite()
                    em.add_field(name=guild , value=invite)
                    break 
        print(invites) # stop iterating over guild.text_channels, since you only need one invite per guild
        await ctx.send(embed=em)
    @commands.group()
    @commands.check(devc)
    async def change(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send_help(str(ctx.command))

 
    @change.command(name="nickname")
    @commands.check(devc)
    async def change_nickname(self, ctx, *, name: str = None):
        """ Change nickname. """
        try:
            await ctx.guild.me.edit(nick=name)
            if name:
                await ctx.send(f"Successfully changed nickname to **{name}**")
            else:
                await ctx.send("Successfully removed nickname")
        except Exception as err:
            await ctx.send(err)


      
    @change.command(name="username")
    @commands.check(devc)
    async def change_username(self, ctx, *, name: str):
        """ Change username. """
        try:
            await self.bot.user.edit(username=name)
            await ctx.send(f"Successfully changed username to **{name}**")
            devchannel=self.bot.get_channel(979345665081610271)
            await devchannel.send(f"{ctx.author} successfully changed my username to **{name}**")
        except discord.HTTPException as err:
            await ctx.send(err)


def setup(client):
    client.add_cog(Dev(client))