import asyncio
import json
import traceback

import discord
from discord.ext import commands
import aiohttp


async def aiohttp_get(url: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            response = (await response.content.read()).decode('utf-8')
            return response


async def aiohttp_get_binary(url: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            response = (await response.content.read())
            return response


async def aiohttp_post(url: str, data: dict = None, params: dict = None):
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=data, params=params) as response:
            response = (await response.content.read()).decode('utf-8')
            return response


async def aiohttp_post_binary(url: str, data: dict = None, params: dict = None):
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=data, params=params) as response:
            response = (await response.content.read())
            return response

import discord


def get_color(user: discord.Member):
    color = user.color
    if str(color) == "#000000":
        color = discord.Color.random()
    return color


class MadLibs(commands.Cog, description="A category for Mad Libs.\n"
                                        "You can restrict Mad Libs games to a single channel "
                                        "using the `setmadlibschannel` command."):
    def __init__(self, bot):
        self.bot = bot
        with open("storage/madlibs_channels.json", "r") as madlibsChannels:
            self.madlibs_channels = json.load(madlibsChannels)
        self.madlibsApi = "http://madlibz.herokuapp.com/api/random?minlength=5&maxlength=15"
        self.vowels = ["a", "e", "i", "o", "u"]

    @commands.command(name="setmadlibschannel", aliases=["madlibschannel"],
                      description="Sets the channels for playing MadLibs.")
    @commands.has_permissions(manage_guild=True)
    @commands.guild_only()
    async def set_madlibs_channel(self, ctx, channel: discord.TextChannel = None):
        """You will not be able to play madlibs in any other channel, as it'll clog the chat with tons of messages
Do not enter the "channel" argument to clear the madlibs channel entry from my database."""
        if channel is None:
            try:
                self.madlibs_channels.pop(str(ctx.guild.id))  # removing the server's channel from the dictionary
                return await ctx.send(embed=discord.Embed(description="MadLibs channel removed from database succesfully.",color=discord.Color.dark_theme()))
            except Exception as e:
                return print(traceback.format_exc(e))

        self.madlibs_channels[str(ctx.guild.id)] = channel.id
        with open("storage/madlibs_channels.json", "w") as writeFile:
            json.dump(self.madlibs_channels, writeFile)
        await ctx.send(embed=discord.Embed(description=f"MadLibs channel set as {channel.mention} succesfully!",color=discord.Color.dark_theme()))

    @commands.command(name="madlibs", aliases=["ml"], description="Let's play MadLibs!")
    async def play_madlibs(self, ctx):
        channel_id = self.madlibs_channels.get(str(ctx.guild.id))
        if channel_id:
            channel = self.bot.get_channel(id=int(channel_id))
            if not channel == ctx.message.channel:
                return await ctx.send(embed=discord.Embed(description=f"You can only play MadLibs in {channel.mention}.",color=discord.Color.red()))

        madlibs_dict = await aiohttp_get(self.madlibsApi)
        madlibs_dict = json.loads(madlibs_dict)
        title = madlibs_dict.get("title")
        blanks = madlibs_dict.get("blanks")
        value = madlibs_dict.get("value")[:-1]
        user_results = []
        for x in range(len(blanks)):  # get the input from the user for each entry in the blanks list
            em = discord.Embed(description=f"**{x + 1}/{len(blanks)}** - "
                           f"{ctx.author.mention}, I need "
                           f"{'an' if blanks[x][0].lower() in self.vowels else 'a'} "  # vowels
                           f"{blanks[x]}",color=0x34363A)
            em.set_footer(text="Type cancel to end the game")
            await ctx.send(embed=em)
            user_input_message = await self.bot.wait_for(
                "message", check=lambda message: message.channel == ctx.message.channel and message.author == ctx.author
                , timeout=15)

            if user_input_message.content=='cancel':
              return await ctx.send('Oh Ok , Lets end this game')

            user_results.append(f"**{user_input_message.content}**")  # append results to another dict
        string = ""
        for x in range(len(user_results)):
            string += value[x]  # adding the values to the final string
            string += user_results[x]
        string += value[-1]  # adding the final value tha twas missed in the for loop
        embed=discord.Embed(title=title, description=string, colour=get_color(ctx.author))
        embed.set_footer(text=f"Excellent, {ctx.author.display_name}!", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @play_madlibs.error
    async def madlibs_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            error = error.original
        if isinstance(error, asyncio.TimeoutError):
            return await ctx.send("I'm done waiting. We'll play again later.")
        if isinstance(error, asyncio.CancelledError):
            pass


def setup(bot):
    bot.add_cog(MadLibs(bot))