import discord
from dislash import InteractionClient, ActionRow, Button, ButtonStyle

from discord.ext import commands
from discord.ext.commands import BucketType, cooldown
import datetime
from datetime import timedelta 
x = datetime.datetime.now()


class Suggestion(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Suggestion cog loaded successfully")
        em = discord.Embed(title ="Monitor Up",description=f"Tessarect Monitor Up At(GMT+ 5:30) ",color =discord.Color.blue())
        em.add_field(name="Time",value=datetime.datetime.now()+timedelta(hours=5,minutes=30))
        channel = self.client.get_channel(929333501101215794)

        await channel.send(embed=em)


      
    @commands.command(cooldown_after_parsing=True, description="Suggest Us :) ")
    @cooldown(1, 7200, BucketType.user)
    async def suggest(self, ctx, *, msg):

        channel_only = self.client.get_channel(929333373913137224)

        up = "\U0001f44d"
        down = "\U0001f44e"

        embed = discord.Embed(
            timestamp=ctx.message.created_at, title=f"Suggestion By {ctx.author}"
        )
        embed.add_field(name="Suggestion", value=msg)
        embed.add_field(name="Author Id", value = ctx.author.id)
        embed.set_footer(
            text=f"Wait until your suggestion is approved",
            icon_url=f"{ctx.author.avatar_url}",
        )
        message = await channel_only.send(embed=embed)
        await message.add_reaction(up)
        await message.add_reaction(down)
        await ctx.channel.send(embed=embed)
        await ctx.message.delete()
        await ctx.send("**Your Suggestion Has Been Recorded**")

      
      
    @commands.command(cooldown_after_parsing=True, description="Get help without joining our server ")
    @cooldown(1, 7200, BucketType.user)
    async def query(self, ctx, *, msg):

        channel_only = self.client.get_channel(929333373913137224)

        #up = "<:antimatterbig:912569937116147772>"


        embed = discord.Embed(
            timestamp=ctx.message.created_at, title=f"Asked By {ctx.author}"
        )
        embed.add_field(name="Question", value=msg)
        embed.add_field(name="Author Id", value = ctx.author.id)
        embed.set_footer(
            text=f"Wait until your question is answered",
            icon_url=f"{ctx.author.avatar_url}",
        )
        message = await channel_only.send(embed=embed)
        #await message.add_reaction(up)
        await ctx.channel.send(embed=embed)
        await ctx.message.delete()
        await ctx.send("**Your Question Has Been Recorded**")


    @commands.command(name='bugs', aliases=['bug'])
    async def bug_report(self, ctx, *, message):

      if len(message.split()) > 5:

        bugs_channel1 = self.bot.get_channel(929333373913137224)
        owner = self.bot.get_user(900992402356043806)


        embed = discord.Embed(
              title='BUG REPORTED',
              colour = 0x008000
          )
        embed.add_field(name='Username', value=ctx.message.author)
        embed.add_field(name='User id', value=ctx.message.author.id)
        embed.add_field(name='Bug: ', value=message)
        await bugs_channel1.send(embed=embed)
        await owner.send(embed=embed)


        await ctx.send("Your bug has been reported")
      else:
        await ctx.send("Please enter your bug in more than 5 words, try describing everything\nOr you might have forgotten to use the quotes")


def setup(client):
    client.add_cog(Suggestion(client))