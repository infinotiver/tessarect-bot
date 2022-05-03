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
import assets.button_check
import subprocess
from subprocess import Popen, PIPE
import shlex
import json
def restart_bot(mode): 
  if mode ==1:
    os.execv(sys.executable, ['python'] + sys.argv)
  if mode==2:
    os.system('busybox reboot')
def progress_bar(progress):
    return '[{0}{1}] {2}%'.format('█'*(int(round(progress/2))), ' '*(50-(int(round(progress/2)))), progress)
def check_Mod(ctx):
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
    @commands.command(help="The main command check that you are a lost dev")    
    async def devtest(self,ctx,user:discord.Member=None):
      if not user:
        user=ctx.author
      with open("storage/dev.json") as f:

        dev_users_list = json.load(f)
      if user.id not in dev_users_list:

          await ctx.send(
              embed=discord.Embed(
                  title="Permission Denied",
                  description="Dude! that's  not a dev,go away",
                  color=discord.Color.red(),
              )
          )          
      else:
        owner=True if user.id==900992402356043806 else False
        await ctx.send(
            embed=discord.Embed(
                title="Verified",
                description=f"Found entry in Database \n Owner? {owner}",
                color=discord.Color.green(),
            )
        )        

    @commands.command(help="Lists Some poor souls having dev access for me")
    @check(check_Mod)
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

    @commands.command(help="Lists Some idiots who cant even use me")
    @check(check_Mod)
    async def listblack(self,ctx):
        x = discord.Embed(description="Blacklisted User",color=0x34363A)
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
    @check(check_Mod)
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
    @check(check_Mod)
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
    @commands.command(aliases=["m","evaldev","deveval"],help="Execuete some stuff")
    @check(check_Mod)  
    async def python_shell(self, ctx, *, text):
        env = {
            "ctx": ctx,
            "discord": discord,
            "commands": commands,
            "client":self.bot,
            "__import__": __import__,
            "guild":ctx.guild,
            "_":self._last_result
        }         
        if  "client.http.token" in text:
          return await ctx.send('not my token') 
        print(f"{Fore.GREEN}Python Shell Invoked: {Style.RESET_ALL}")
        print(Fore.CYAN,text, str(ctx.author))

        print(Style.RESET_ALL)
        if str(ctx.author.guild.id) == "912569937116147772":
            try:
                text = text.replace("```py", "")
                text = text.replace("```", "")
                a = eval(text)

                em = discord.Embed(
                    title="Successfully Execueted",
                    description=f"```py\n{str(a)}\n```",
                    color=discord.Color.green(),
                )
                await ctx.send(embed=em)
         
            except Exception as e:
                desired_trace = traceback.format_exc()
                await ctx.send(
                    embed=discord.Embed(
                        title="Oops ! there was a error",
                        description=f'```py\n{desired_trace}\n```',
                        color=0xff0000,
                    )
                )
        else:

      
          re = discord.Embed(
              title="Unverified Server",
              description=f"{ctx.author.mention} This command is now only for the main server which is Tessa Bot Developers",
              color=discord.Color.blue(),
          )
          await ctx.send(embed=re)      

               
    @commands.command(name= 'restart',help='Hidden command, youre not supposed to access this.Now off you go. Nothing to see here.',aliases=['reboot'])
    @check(check_Mod)
    async def restart(self,ctx,mode:int=1):
      listd=[1,2] 
      if mode not in listd:
        dd = discord.Embed(title='Invalid Input',description=f' Invalid Mode = {mode} \n Accepted mode {listd}',color=discord.Color.red())          
        await ctx.send(embed=dd)     
        return
      otp_success = await assets.otp_assets.send_waitfor_otp(ctx, self.bot)
      # random otp generator. if user enters correct otp, returns true. else, returns false
      if not otp_success:
          return await ctx.send('Restart Command Aborted')
      if len(self.bot.voice_clients)>0:
        await ctx.send(embed=discord.Embed(description=f"There are {len(self.bot.voice_clients)} servers listening to music through Tessarect, Do you wanna restart?"))
        otp_success = await assets.otp_assets.send_waitfor_otp(ctx, self.bot)
        if not otp_success:
            return await ctx.send('Restart Command Aborted')
      async with ctx.typing():  
        e = discord.Embed(title='Restart  Invoked',description=f'**Mode = {mode}** \n 1 = Simple restart 2 = Full restart',color=discord.Color.dark_gold())
        e.add_field(name="Progress",value=progress_bar(10))
        x = await ctx.send(embed=e)
        await asyncio.sleep(1)  
        e.set_field_at(0,name="Progress",value=progress_bar(30))
        await x.edit(embed=e)
        await asyncio.sleep(2)
        e.set_field_at(0,name="Progress",value=progress_bar(50))
        e.add_field(name="Status",value='Unloading Cogs')
        await x.edit(embed=e)        

        for filename in os.listdir("./cogs"):
          if filename.endswith(".py"):
              try:

                self.bot.unload_extension(f"cogs.{filename[:-3]}")
              except Exception as e:
                print(f'{filename} - {e}')           

        e.set_field_at(0,name="Progress",value=progress_bar(100))
        
        e.set_field_at(1,name="Status",value='Changing Status')
        await x.edit(embed=e)
        await self.bot.change_presence(
                status=discord.Status.idle,
                activity=discord.Activity(
                    
                    type=discord.ActivityType.watching,
                    name= f"🌠 System Reboot [DONT USE]"
                ))
        with open("./storage/reboot.json", "w") as rebootFile:
            json.dump(ctx.message.channel.id, rebootFile) 
        
             
        restart_bot(mode)  




    @commands.command(name='reload', description="Reload all/one of the bot's cogs.\n"
                                                 "This is Dev-only, so don't have any Devny ideas.", )
    @check(check_Mod)
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
    @check(check_Mod)
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
    @check(check_Mod)
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
    @check(check_Mod)
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
    @check(check_Mod)
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
    @check(check_Mod)
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
    @check(check_Mod)
    async def blacklist(self,ctx, user : discord.Member,*,reason:str):
        with open("storage/black.json") as f:
            users_list = json.load(f)
        if user.id==ctx.author.id:
          return await ctx.send('You cant blacklisted yourself')
        if user.id not in users_list  :
            users_list.append(user.id)
            e=discord.Embed(title="Blacklisted User!",description=f":white_medium_square: Member {user.mention}\n:white_medium_square:Reason: {reason}\n :white_medium_square: Developer {ctx.author.mention}",color=discord.Color.red())  
            e.set_author(name=user.name,icon_url=user.avatar_url)            
            logschannel=self.bot.get_channel(929333373913137224)
            await logschannel.send(embed=e)
            with open("storage/black.json", "w+") as f:
                json.dump(users_list, f)
            
            await ctx.send(f"{user.mention} has been added!")  
        else:
          await ctx.send('See Developer , either you are adding a blacklisted user again ') 
    @commands.command(help="Unblacklist some users if they are behaving nice")
    @check(check_Mod)
    async def unblacklist(self,ctx, user : discord.Member):
        with open("storage/black.json") as f:
            users_list = json.load(f)

        if user.id in users_list:
            users_list.remove(user.id)
            e=discord.Embed(title="UnBlacklisted User!",description=f":white_medium_square: Member {user.mention}\n :white_medium_square: Developer {ctx.author.mention}",color=discord.Color.gold())  
            e.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
            logschannel=self.bot.get_channel(929333373913137224)
            await logschannel.send(embed=e)            
        else:
            await ctx.send(f"{user.mention} is not in the list, so they cannot be removed!")
            return

        with open("storage/black.json", "w+") as f:
            json.dump(users_list, f)

        await ctx.send(f"{user.mention} has been removed!")  

           

    @check(check_Mod)
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
            embed.add_field(name=guild,value=f"({str(guild.id)}) {str(guild.member_count)} ({str(guild.owner)})")
          await ctx.send(embed=embed) 
    @check(check_Mod)
    @commands.command()
    async def reply(self,ctx,member:discord.User,*,content:str):
      
      embed = discord.Embed(title=f"**Tessarect Support **",description=f"Hello {member.mention} , here is a message from my developers",timestamp=ctx.message.created_at, color=0xac5ece)
    
  
      embed.add_field(name="<:arrow_right:940608259075764265> Message",value=content,inline=False)
  
      embed.set_footer(text=f"Sent by Tessarect Devs | {ctx.author}")
  
      try:
        await member.send(embed=embed)      
      except:
        await ctx.send(embed=discord.Embed(title="User has DM's Disabled",color=discord.Color.red()))
        return
      await ctx.send(embed= discord.Embed(title="<:user:941986233574367253> Reply", description=f"Your Message was Successfully Sent.", timestamp=ctx.message.created_at, color=0xff0000)        )
    @check(check_Mod)
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

def setup(client):
    client.add_cog(Dev(client))