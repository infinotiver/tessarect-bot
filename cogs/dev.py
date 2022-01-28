import datetime

import discord
import requests
from discord.ext import commands
from discord.ext.commands import check
import os
import sys
from subprocess import Popen, PIPE
import shlex
import json
#from main import check_Mod
def restart_bot(): 
  os.execv(sys.executable, ['python'] + sys.argv)
def check_Mod(ctx):
    with open('Dev.txt') as f: # do change the 'Mod.txt' to the name that suits you. Ensure that this file is in the same directory as your code!
        if str(ctx.author.id) in f.read(): # this is reading the text file and checking if there's a matching string
            return ctx.author.id       
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
              
    @commands.command(name="evaldev")
    @check(check_Mod)
    async def _eval(self,ctx, *, code):
        env = {
            "ctx": ctx,
            "discord": discord,
            "commands": commands,
            "bot": ctx.bot,
            "client":ctx.bot,
            "__import__": __import__
        }
        if "bot.http.token" in code or "client.http.token" in code:
            return await ctx.send(f"You can't take my token , huh {ctx.author.name}")
        code = code.replace("```py", "")
        code = code.replace("```", "")
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

        embed = discord.Embed(title="Eval",colour=ecolor)
        embed.add_field(name="Input",value="```py\n"+code+"\n```",inline=False)
        embed.add_field(name=outname,value="```\n"+str(output)+"\n```",inline=False)
        embed.set_author(name=ctx.author.display_name,icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)  
    @commands.command(name= 'restart')
    @check(check_Mod)
    async def restart(self,ctx):
      e = discord.Embed(title='🕐',description='Restarting.. Scheduled , in approx 7 seconds')
      e3= discord.Embed(title='<:Protectedshield:922468797246488596>',description="Unloaded Cogs,Final Works , **RESTARTING BOT IN 3 SECONDS FROM THIS EDIT**")
      e2= discord.Embed(title='<a:Loading:922468614009925692>',description="Unloading cogs")  
      x = await ctx.send(embed=e)

      await x.edit(embed=e2)
      for filename in os.listdir("./cogs"):
          if filename.endswith(".py"):
              self.bot.unload_extension(f"cogs.{filename[:-3]}")

      await x.edit(embed=e3)  

      restart_bot()  
    @commands.command(hidden=True)
    @commands.check(check_Mod)
    async def shell(self, ctx: commands.Context, *, command: str) -> None:
        """ Run a shell command. """

        def run_shell(command):
            with Popen(command, stdout=PIPE, stderr=PIPE, shell=True) as proc:
                return [std.decode("utf-8") for std in proc.communicate()]

        command = self.cleanup_code(command)
        argv = shlex.split(command)
        stdout, stderr = await self.bot.loop.run_in_executor(None, run_shell, argv)
        if stdout:
            if len(stdout) >= 1500:
                print(stdout)
                return await ctx.send("Too big I'll print it instead")
            await ctx.send(f"```\n{stdout}\n```")
        if stderr:
            if len(stderr) >= 1500:
                print(stderr)
                return await ctx.send("Too big I'll print it instead")
            await ctx.send(f"```\n{stderr}\n```")

def setup(client):
    client.add_cog(Dev(client))