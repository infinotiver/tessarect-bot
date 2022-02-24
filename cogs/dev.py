import datetime
import traceback
import discord
import requests
from  colorama import Fore , Style

from discord.ext import commands
from discord.ext.commands import check
import os
import asyncio
import sys
import assets.otp_assets
import assets.button_check
import subprocess
from subprocess import Popen, PIPE
import shlex
import json

#from main import check_Mod
def restart_bot(mode): 
  if mode ==1:
    os.execv(sys.executable, ['python'] + sys.argv)
  if mode==2:
    os.system('busybox reboot')
  
def check_Mod(ctx):
  with open("storage/dev.json") as f:
      dev_users_list = json.load(f)
      if ctx.author.id not in dev_users_list:
          return False

  return True


class Dev(commands.Cog):
    def __init__(self, client):
        self.bot = client

    @staticmethod
    def cleanup_code(content):
        """Automatically removes code blocks from the code."""
        # remove ```py\n```
        if content.startswith("```") and content.endswith("```"):
            return "\n".join(content.split("\n")[1:-1])

        # remove `foo`
        return content.strip("` \n") 
    @commands.command()    
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
        await ctx.send(
            embed=discord.Embed(
                title="Verified",
                description="Found entry in Database",
                color=discord.Color.green(),
            )
        )        

    @commands.command()
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
    @commands.command()
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
    @commands.command()
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
    @commands.command(aliases=["m","evaldev","deveval"])
    @check(check_Mod)  
    async def python_shell(self, ctx, *, text):
        env = {
            "ctx": ctx,
            "discord": discord,
            "commands": commands,
            "client":self.bot,
            "__import__": __import__,
            "guild":ctx.guild
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
                a = eval(text,env)

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
    @commands.command(name= 'restart',hidden=True,help='Hidden command, youre not supposed to access this.Now off you go. Nothing to see here.')
    @check(check_Mod)
    async def restart(self,ctx,mode:int=1):
      
      otp_success = await assets.otp_assets.send_waitfor_otp(ctx, self.bot)
      # random otp generator. if user enters correct otp, returns true. else, returns false
      if not otp_success:
          return 
      async with ctx.typing():  
    
        e = discord.Embed(title='<:reset:942782303552282624>Restarting..',description=f' Scheduled , in approx 5 seconds(unless errors) Mode = {mode} \n 1 = Simple restart 2 = Full restart',color=discord.Color.red())
        e3= discord.Embed(title='<:Protectedshield:922468797246488596> **RESTARTING BOT **',description="Unloaded cogs,Final Works , ",color=discord.Color.green())
        e2= discord.Embed(title='<a:Loading:941646457562365962>',description="Unloading cogs",color=discord.Color.blue())  
        x = await ctx.send(embed=e)
        await asyncio.sleep(2)
        await x.edit(embed=e2)
        await asyncio.sleep(2)
        for filename in os.listdir("./cogs"):
          if filename.endswith(".py"):
              try:

                self.bot.unload_extension(f"cogs.{filename[:-3]}")
              except Exception as e:
                e2.set_footer(text=f"{filename} - {e}") 
                await x.edit(embed=e2)
                await asyncio.sleep(2)


        await x.edit(embed=e3)
        e3.set_footer(text="Changing Status")
        await x.edit(embed=e3)
  
        await self.bot.change_presence(

                activity=discord.Activity(
                    type=discord.ActivityType.watching,
                    name= f"🌠 System Reboot [DONT USE]"
                ))
        with open("./storage/reboot.json", "w") as rebootFile:
            json.dump(ctx.message.channel.id, rebootFile)                
        restart_bot(mode)  



    @commands.command(name='reload', description="Reload all/one of the bot's cogs.\n"
                                                 "This is Dev-only, so don't have any funny ideas.", )
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

            """ Now the code for reloading One cog comes into play"""

            embed = discord.Embed(
                title="Reloading cogs!", timestamp=ctx.message.created_at)
            ext = f"{cog.lower()}.py"
            if not os.path.exists(f"./cogs/{ext}"):
                embed.add_field(
                    name=f"Failed to reload: `{ext}`", value="This cog does not exist.", inline=False)
                embed.color=discord.Color.red()

            elif ext.endswith(".py") and not ext.startswith("_"):
                try:
                    self.bot.unload_extension(f"cogs.{ext[:-3]}")
                    self.bot.load_extension(f"cogs.{ext[:-3]}")
                    embed.add_field(
                        name=f"Reloaded: `{ext}`", value='\uFEFF', inline=False)
                    embed.color=discord.Color.green()
                except Exception:
                    desired_trace = traceback.format_exc()
                    embed.add_field(
                        name=f"Failed to reload: `{ext}`", value=desired_trace, inline=False)
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
                embed.color=discord.Color.green()
            except Exception as e:
                embed.add_field(
                    name=f"Failed to load: `{cog_file_name}.py`", value=str(e), inline=False)
                embed.color=discord.Color.red()
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

    @commands.command(name="gitpull")
    @commands.guild_only()
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
    @commands.command()
    @check(check_Mod)
    async def blacklist(self,ctx, user : discord.Member):
  

        with open("storage/black.json") as f:
            users_list = json.load(f)

        if user.id not in users_list  :
            users_list.append(user.id)

            with open("storage/black.json", "w+") as f:
                json.dump(users_list, f)

            await ctx.send(f"{user.mention} has been added!")  
        else:
          await ctx.send('See Developer , either you are adding a dev again as dev or a bot (bots arent that much cool)') 
    @commands.command()
    @check(check_Mod)
    async def unblacklist(self,ctx, user : discord.Member):
     

        with open("storage/black.json") as f:
            users_list = json.load(f)

        if user.id in users_list:
            users_list.remove(user.id)
        else:
            await ctx.send(f"{user.mention} is not in the list, so they cannot be removed!")
            return

        with open("storage/black.json", "w+") as f:
            json.dump(users_list, f)

        await ctx.send(f"{user.mention} has been removed!")  


def setup(client):
    client.add_cog(Dev(client))