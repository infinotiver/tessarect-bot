import json
import discord_pass
import fnmatch
import datetime
import math
import asyncio
intervals = (
    ('weeks', 604800),  # 60 * 60 * 24 * 7
    ('days', 86400),    # 60 * 60 * 24
    ('hours', 3600),    # 60 * 60
    ('minutes', 60),
    ('seconds', 1),
)
def check_blacklist(ctx):
  with open("storage/black.json") as f:
      dev_users_list = json.load(f)
      if ctx.author.id not in dev_users_list:
          return False

  return True

import os
import sys
import traceback
from dislash import InteractionClient, ActionRow, Button, ButtonStyle

import discord
from discord.ext import commands


class Tessarect(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.inter_client = InteractionClient(bot)
        self.theme_color = 0xFF0800
        self._theme_color = 0x315399
        self.logs_channel = 929333502577606656
        self.description="Important cog for Tessarect Tessarect Another general purpose discord bot but with Economy commands and much more Well Attractive , Economy and Leveling Bot with tons of features. Utitlity Bot , Music Bot , Economy Bot , Moderation Bot and much more \n[p]help for more info"

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        embed = discord.Embed(
            title="I Have Joined A New Guild!",
            description=f"{guild.name} \nOwner {guild.owner}",
            timestamp=datetime.datetime.now(),
            color=self._theme_color,
        )
        embed.add_field(name="Server ID",value=guild.id)
        embed.add_field(
            name=f"This Guild Has {guild.member_count} Members!",
            value=f"Yay Another Server! We Are Now At {len(self.bot.guilds)} Guilds!",
        )
        await self.bot.get_channel(self.logs_channel).send(embed=embed)
        owner=guild.owner
        emx = discord.Embed(title='Hello',description=f"Hey {owner.mention} , thank you for adding me to {guild.name} , It is a informative embed for you to start up , you can join our support server [here](https://dsc.gg/tessarectsupport) for any kind of help ",color=discord.Color.gold())
          
        emx.add_field(name="Tessarect",value = f'<:arrow_right:940608259075764265> Another general purpose discord bot but with Economy commands and much more Well Attractive , Economy and Leveling Bot with tons of features. Utitlity Bot , Music Bot , Economy Bot , Moderation Bot and much more .')
        emx.add_field(name="**Seting Up**",value="<:arrow_right:940608259075764265> Type `[p]help`to know all commands ,(that's a lot !) , do `[p]stats` for getting stats .`[p]setup` for basic configuration")
        await owner.send(embed=emx)

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        embed = discord.Embed(
            title="<:downarrow:941994549822226452> ",
            description=f"Guild Elevator Down",
            timestamp=datetime.datetime.now(),
            color=discord.Color.red(),
        )
        embed.add_field(name="Guild",value=f"{guild.name} \n<:owner:946288312220536863> Owner: {guild.owner}")
        embed.set_thumbnail(url=guild.icon_url)
        
        embed.add_field(name="Server ID",value=guild.id,inline=False)                        
        embed.add_field(name="Current Guild count",value=len(self.bot.guilds),inline=False)  
        await self.bot.get_channel(self.logs_channel).send(embed=embed)

      
    @commands.Cog.listener()
    async def on_ready(self):
        print("Tessarect cog loaded successfully")
    @commands.command(pass_context=True)
    async def cloc(self, ctx):
      """Outputs the total count of lines of code in the currently installed repo."""
      # Script pulled and edited from https://github.com/kyco/python-count-lines-of-code/blob/python3/cloc.py
      
      message = await ctx.send(embed=discord.Embed(title="Scrolling Code",color=self._theme_color))


      # Get our current working directory <:checkboxsquare:942779132159356959>should be the bot's home
      path = os.getcwd()
      
      # Set up some lists
      extensions = []
      code_count = []
      ext_dict = {
        "py":"Python (.py)",
        "yml":"Yaml files (for some silly stuff ) (.yml)",
        "sh":"Shell Script (.sh)",
        "txt":"Text files (.txt)",
        "md":"Markdown Files (.md)",
        "css":"CSS Files (.css)",
        "html":"HTML Code (.html)"}
      
      # Get the extensions <:checkboxsquare:942779132159356959>include our include list
      extensions = self.get_extensions(path, list(ext_dict))
      
      for run in extensions:
        extension = "*."+run
        temp = 0
        for root, dir, files in os.walk(path):
          for items in fnmatch.filter(files, extension):
            value = root + "/" + items
            temp += sum(+1 for line in open(value, 'rb'))
        code_count.append(temp)
      
      # Set up our output
      fields = [{"name":ext_dict.get(extensions[x],extensions[x]),"value":"{:,} line{}".format(code_count[x],"" if code_count[x]==1 else "s")} for x in range(len(code_count))]
      dd=discord.Embed(
        title="Counted Lines of Code",
        description="My developers took so much time to sloppily write the following to bring me life...that it took me so many seconds to fetch that up ",
        color=discord.Color.blurple()
      )
      dd.set_footer(text="These counts are fetched from my github repo and may not be up to date")
      dd.set_thumbnail(url=self.bot.user.avatar_url)
      for x in fields:
        dd.add_field(name=x['name'],value=x['value'])
      return await message.edit(embed=dd)
      

    # Helper function to get extensions
    def get_extensions(self, path, excl):
      extensions = []
      for root, dir, files in os.walk(path):
        for items in fnmatch.filter(files, "*"):
          temp_extensions = items.rfind(".")
          ext = items[temp_extensions+1:]
          if ext not in extensions:
            if ext in excl:
              extensions.append(ext)
      return extensions

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if str(error) =="You are blacklisted":
          await ctx.send(embed=discord.Embed(description=f'Blacklisted User Attempted to use a command\n Status : Command blocked \n Note {ctx.author.mention}, you cant use me because you were blacklisted by a verified developer for some reason , for appealing go to my support server and ask the devs ',color=discord.Color.dark_red())  ) 
          return     
        if hasattr(ctx.command, "on_error"):
            return
        with open ('storage/errors.json', 'r') as f:
            data = json.load(f)
        error = getattr(error, "original", error)

        if isinstance(error, commands.BotMissingPermissions):
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
                color=self.theme_color,
            )
            
            embed.set_author(name=ctx.author,icon_url=ctx.author.avatar_url)
            return
        elif isinstance(error, commands.CommandNotFound):
          return
        elif isinstance(error, commands.DisabledCommand):
            embed = discord.Embed(
                title="Command disabled",
                description=f"Looks like This command is disabled for use !",
                color=self.theme_color,
            )   
            await ctx.send(embed=embed)       
            return

        elif isinstance(error, commands.CommandOnCooldown):
           
            embed = discord.Embed(
                title="Whoa Slow it down!!!!",
                description=f"Retry that command after {datetime.timedelta(seconds=error.retry_after)}.",
                color=self.theme_color,
            )
            embed.set_author(name=ctx.author,icon_url=ctx.author.avatar_url)
            #embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/922468797108080660.png")
            await ctx.send(embed=embed)
 
            return

        elif isinstance(error, commands.MissingPermissions):
            missing = [
                perm.replace("_", " ").replace("guild", "server").title()
                for perm in error.missing_perms
            ]
            if len(missing) > 2:
                fmt = "{}, and {}".format("**, **".join(missing[:-1]), missing[-1])
            else:
                fmt = " and ".join(missing)
            embed = discord.Embed(
                title="Insufficient Permission(s)",
                description=f"You need the **{fmt}** permission(s) to use this command.",
                color=self.theme_color,
            )
            embed.set_author(name=ctx.author,icon_url=ctx.author.avatar_url)
            #embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/922468797108080660.png")
            await ctx.send(embed=embed)
            return

        elif isinstance(error, commands.UserInputError):
          if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                title="<:blobno:941713015424839691> Required Argument Missing",
                description=f"You need to provide me some inputs for that command , check it's help page for more info\n <:rightarrow:941994550124245013> Correct Usage: `{ctx.prefix}{ctx.command.name} {ctx.command.signature}`",
                color=self.theme_color,
            )
            embed.set_author(name=ctx.author,icon_url=ctx.author.avatar_url)
           #embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/922468797108080660.png")
            await ctx.send(embed=embed)
          else: 
            embed = discord.Embed(
                title="Wrong Inputs",
                description=f"Maybe you forgot to specify inputs or gave an extra input or some invalid input \n<:rightarrow:941994550124245013>: `{error}`",
                color=self.theme_color)
            embed.set_author(name=ctx.author,icon_url=ctx.author.avatar_url)
            #embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/922468797108080660.png")
            await ctx.send(embed=embed)
          

        elif isinstance(error, commands.NoPrivateMessage):
            try:
                await ctx.author.send("This command cannot be used in direct messages.")
            except discord.Forbidden:
                raise error
            return
        elif isinstance(error, commands.MaxConcurrencyReached):
            embed = discord.Embed(
                title="<:dnd_status:946652840053600256> Bot Busy !",
                description=f"Please use that command few moments after ",
                color=self.theme_color,
            )
            embed.set_author(name=ctx.author,icon_url=ctx.author.avatar_url)
            #embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/922468797108080660.png")
            await ctx.send(embed=embed)
            return         
        elif isinstance(error, discord.errors.Forbidden):
            try:
                embed = discord.Embed(
                    title="Forbidden",
                    description=f"Error <:checkboxsquare:942779132159356959>403 <:checkboxsquare:942779132159356959>Forbidden | Missing perms\n Bot is missing permissions \n Recommended giving Permission `8` (admin)",
                    color=self.theme_color,
                )
                embed.set_author(name=ctx.author,icon_url=ctx.author.avatar_url)
                #embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/922468797108080660.png")
                await ctx.send(embed=embed)
            except:
                print("Failed forbidden")
            return

        elif isinstance(error, commands.CheckFailure):
            embed = discord.Embed(
                title="Permissions Denied",
                description=f"You do not have permissions to use this command",
                color=self.theme_color,
            )
            #embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/922468797108080660.png")
            await ctx.send(embed=embed)
            return
        else:
          devlogs=self.bot.get_channel(979345665081610271)
          err_code=discord_pass.secure_password_gen(10)             
          

          row2 = ActionRow(
              Button(
                  style=ButtonStyle.grey,
                  label="Error Code",
                  custom_id="test_button"),
              Button(
                  style=ButtonStyle.green,
                  label="Troubleshooting",
                  custom_id="tr")
              
          )
    
          msgcon=ctx.message.content
          known_error=False
          print(data)
          for x in data:
            if data[x]['error']==str(error) and data[x]['command used']==str(ctx.command) and data[x]['full text']==str(ctx.message.content):
              known_error=True
          if not known_error:
            data[str(err_code)] = {}
            data[str(err_code)]['error']=str(error)
            data[str(err_code)]['authorid']=str(ctx.author.id)
            data[str(err_code)]['author']=str(ctx.author)
            data[str(err_code)]['guild']=str(ctx.guild.id)
            data[str(err_code)]['full text']=str(ctx.message.content)
            data[str(err_code)]['command used']=str(ctx.command)
            data[str(err_code)]['time']=str(ctx.message.created_at)            
            with open ('storage/errors.json', 'w') as f:
                json.dump(data, f, indent=4)
          if not known_error:
            log=discord.Embed(description=f"**{err_code}**\n```\n{error}\n```\n{str(ctx.message.content)}",color=self.theme_color,timestamp=ctx.message.created_at)
            
            
            log.set_footer(text=f"{ctx.author} @ {ctx.guild}")
            await devlogs.send(embed=log)  
          uem=discord.Embed(title="Oops!",description=f'It seems like an unexpected error happened\n|| ** {error} ** ||',color=0xe74c3c).add_field(name="Known Error?",value=known_error)
          uem.set_author(name=ctx.author,icon_url=ctx.author.avatar_url)
          msg2=await ctx.send(embed=uem,components=[row2])
          on_click = msg2.create_click_listener(timeout=20)
          @on_click.not_from_user(ctx.author, cancel_others=False, reset_timeout=True)
          async def on_wrong_user(inter):
              
              await inter.reply("You're not the author dude , dont come in between enjoy your milk", ephemeral=True)         
          @on_click.matching_id("test_button")
          async def on_test_button(inter):
              await inter.reply(embed=discord.Embed(description='This error is known , kindly be patient , devs are working ' if known_error else f"Your error code is **{err_code} **",color=discord.Color.dark_theme()),ephemeral=True)
          @on_click.matching_id("tr")
          async def on_test(inter):
            await inter.reply("""**Basic Troubleshooting**
<:checkboxsquare:942779132159356959>Retry again
<:checkboxsquare:942779132159356959>Check bot's/your permissions 
<:checkboxsquare:942779132159356959>check command help 
<:checkboxsquare:942779132159356959>Ask developers 
<:checkboxsquare:942779132159356959>Try after sometime 
<:checkboxsquare:942779132159356959>Blacklisted cant use anything 
<:checkboxsquare:942779132159356959>Drink milk and enjoy other commands
**Cant solve it?**
<:checkboxcheck:942779132117409863> Join our support server
<:checkboxcheck:942779132117409863> Open issue on github""",ephemeral=True)
          @on_click.timeout
          async def on_timeout():
              #await ActionRow.disable_buttons(row2)
              try:
                await msg2.edit(components=[])
              except Exception as e:
                print(e)

          print("Ignoring exception in command {}:".format(ctx.command), file=sys.stderr)

          traceback.print_exception(
                type(error), error, error.__traceback__, file=sys.stderr
            )

def setup(bot):
    bot.add_cog(Tessarect(bot))