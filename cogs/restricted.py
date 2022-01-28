import discord
from discord.ext import commands,tasks
import random
import requests
import json
import asyncio
import itertools
import io
from contextlib import redirect_stdout


mainaccid =900992402356043806

class Restricted(commands.Cog):
    def __init__(self,bot):
        self.bot=bot

    ##DANGEROUS-> "https://stackoverflow.com/questions/34385014/how-do-i-set-the-output-of-exec-to-variable-python"
    ##BUT RUNNING FROM SERVERS LIKE heroku TILL NOW HAVE NOT SHOWN ANY AFFECT ON THE CODING COMPUTER EVEN WITH OS MODULE CODES
    ##THE OUTPUT IS : "py"
    ##eval command->executes any python code and displays output(work in progress)

    @commands.is_owner()
    @commands.command(hidden=True)
    async def servers(self,ctx):
        activeservers = self.bot.guilds
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
            print(guild.name)
    @commands.is_owner()
    @commands.command(hidden=True)
    async def invservers(self,ctx):
        invites = []

        for guild in self.bot.guilds:
            for c in guild.text_channels:
                if c.permissions_for(guild.me).create_instant_invite:  # make sure the bot can actually create an invite
                    invite = await c.create_invite()
                    invites.append(invite)
                    break 
        print(invites) # stop iterating over guild.text_channels, since you only need one invite per guild

    @commands.is_owner()
    @commands.command(hidden=True)
    async def msgservers(self,ctx,*,text):
        activeservers = self.bot.guilds
        for guild in activeservers:
            allowed=[]
            for channel in guild.text_channels:
                if channel.permissions_for(guild.me).send_messages and channel.permissions_for(guild.me).embed_links:
                    allowed.append(channel)
            if len(allowed) >= 1:
                to_post = allowed[0]
                for channel in allowed:
                    if "general" in channel.name.lower():
                        to_post = channel
                        break
                try:
                    await to_post.send(text)
                    await ctx.send("Sent message to Guild: "+guild.name+" Channel: "+to_post.name)
                except Exception as e:
                    await ctx.send(e)


    @commands.is_owner()
    @commands.command(hidden=True)
    async def msgserver(self,ctx):
        def check(msg):
            return msg.author == ctx.author and str(ctx.author.id) == mainaccid and msg.channel == ctx.channel
        await ctx.send("Guild name:")
        try:
            guild = await self.bot.wait_for("message", check=check , timeout=60)
        except asyncio.TimeoutError:
            await ctx.send("Sorry you took too long to respond!(waited for 60sec)")
            return
        await ctx.send("Channel name:")
        try:
            channel = await self.bot.wait_for("message", check=check , timeout=60)
        except asyncio.TimeoutError:
            await ctx.send("Sorry you took too long to respond!(waited for 60sec)")
            return
        await ctx.send("Message:")
        try:
            msg = await self.bot.wait_for("message", check=check , timeout=60)
        except asyncio.TimeoutError:
            await ctx.send("Sorry you took too long to respond!(waited for 60sec)")
            return
        await ctx.send("Times:")
        try:
            times = await self.bot.wait_for("message", check=check , timeout=60)
        except asyncio.TimeoutError:
            await ctx.send("Sorry you took too long to respond!(waited for 60sec)")
            return
        activeservers = self.bot.guilds
        for g in activeservers:
            if g.name==guild.content:
                for ch in g.channels:
                    if(ch.name == channel.content):
                        for i in range(int(times.content)):
                            try:
                                await ch.send(msg.content)
                                await ctx.send("Sent message")
                            except Exception as e:
                                await ctx.send(e)

def setup(bot):
    bot.add_cog(Restricted(bot))