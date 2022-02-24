import json
import discord_pass

import math
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
import os
import sys
import traceback
from dislash import InteractionClient, ActionRow, Button, ButtonStyle

import discord
from discord.ext import commands


class Errors(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.inter_client = InteractionClient(bot)
    @commands.Cog.listener()
    async def on_ready(self):
        print("Error cog loaded successfully")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if hasattr(ctx.command, "on_error"):
            return
        with open ('storage/errors.json', 'r') as f:
            data = json.load(f)

        # get the original exception
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
                color=0xFF0000,
            )
            embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/922468797108080660.png")
            return
        elif isinstance(error, commands.CommandNotFound):
          return
        elif isinstance(error, commands.DisabledCommand):
            await ctx.send("This command has been disabled.")
            return

        elif isinstance(error, commands.CommandOnCooldown):
           
            embed = discord.Embed(
                title="Whoa Slow it down!!!!",
                description=f"Retry that command after {display_time(error.retry_after,4)}.",
                color=0x1F242A,
            )
            embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/922468797108080660.png")
            msg=await ctx.send(embed=embed)
 
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
                title=" <:error:942777902125158473>Insufficient Permission(s)",
                description=f"You need the **{fmt}** permission(s) to use this command.",
                color=0xFF0000,
            )
            embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/922468797108080660.png")
            await ctx.send(embed=embed)
            return

        elif isinstance(error, commands.UserInputError):
            embed = discord.Embed(
                title="Invalid Input",
                description=f"Maybe you forgot to specify inputs or gave an extra input\nSPECIFIED ERROR\n ==> `{error}`",
                color=0xFF0000,
            )
            embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/922468797108080660.png")
            await ctx.send(embed=embed)


        elif isinstance(error, commands.NoPrivateMessage):
            try:
                await ctx.author.send("This command cannot be used in direct messages.")
            except discord.Forbidden:
                raise error
            return
        elif isinstance(error, discord.errors.Forbidden):
            try:
                embed = discord.Embed(
                    title="Forbidden",
                    description=f"Error - 403 - Forbidden | Missing perms\n Bot is missing permissions | Recommended giving Permission `8` (admin)",
                    color=0xFF0000,
                )
                embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/922468797108080660.png")
                await ctx.send(embed=embed)
            except:
                print("Failed forbidden")
            return

        elif isinstance(error, commands.CheckFailure):
            embed = discord.Embed(
                title="Permissions Denied",
                description=f"You do not have permissions to use this command",
                color=0xFF0000,
            )
            embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/922468797108080660.png")
            await ctx.send(embed=embed)
            return
        else:
          
          row2 = ActionRow(
              Button(
                  style=ButtonStyle.red,
                  label="Error Code",
                  custom_id="test_button"),
              Button(
                  style=ButtonStyle.blurple,
                  label="Troubleshooting",
                  custom_id="tr")
              
          )
          err_code=discord_pass.secure_password_gen(10)
          msgcon=ctx.message.content
          data[str(err_code)] = {}
          data[str(err_code)]['error']=str(error)
          data[str(err_code)]['authorid']=str(ctx.author.id)
          data[str(err_code)]['author']=str(ctx.author)
          data[str(err_code)]['guild']=str(ctx.guild.id)
          data[str(err_code)]['full text']=str(ctx.message.content)
          data[str(err_code)]['command used']=str(ctx.command)

          
          with open ('storage/errors.json', 'w') as f:
              json.dump(data, f, indent=4)
          uem=discord.Embed(title="Oops!",description=f'It seems like an unexpected error happened',color=0xff0800).add_field(name="Error",value=f"""```diff
- {error}
``` \n Click the button below to get your Error id for reference""")
          msg2=await ctx.send(embed=uem,components=[row2])
          on_click = msg2.create_click_listener(timeout=60)

          @on_click.matching_id("test_button")
          async def on_test_button(inter):
              await inter.reply(f"Your error code is **{err_code}** !",ephemeral=True)
          @on_click.matching_id("tr")
          async def on_test(inter):


            await inter.reply(embed=discord.Embed(title="TROUBLESHOOTING",description="""```yml
- Retry again
- Check bot's/your permissions 
- check command help 
- Ask developers 
- Try after sometime 
- Note if you are Blacklisted you cant use anything 
- Drink milk and enjoy other commands
          ```""",color=discord.Color.green()))
          @on_click.timeout
          async def on_timeout():
              await msg2.edit(components=[])
          print("Ignoring exception in command {}:".format(ctx.command), file=sys.stderr)

          traceback.print_exception(
              type(error), error, error.__traceback__, file=sys.stderr
          )

def setup(bot):
    bot.add_cog(Errors(bot))