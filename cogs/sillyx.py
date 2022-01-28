import discord
from discord.ext import commands
import random
import aiohttp
import os
import ast
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
import asyncio
import random

import discord


def get_otp(digits=4):
    otp = ""
    for x in range(digits):
        otp += str(random.randint(0, 9))
    return otp


async def genpost(api, header, json):
    async with aiohttp.ClientSession() as session:
        async with session.post(api, headers=header, json=json) as resp:
            return await resp.json()
sadness = 'https://media0.giphy.com/media/OPU6wzx8JrHna/giphy.gif'

randomcolor = random.choice([discord.Color.red(), discord.Color.blue(), discord.Color.green(), discord.Color.purple(), discord.Color.magenta(), discord.Color.gold()])

class Attack(commands.Cog):
    """I like this category"""

    def __init__(self, bot):
        self.bot = bot
        self.spank_url = "https://api.devs-hub.xyz/spank?"
        self.hitler_url = "https://api.devs-hub.xyz/hitler?image="
        self.grab_url = "https://api.devs-hub.xyz/grab?image="
        self.trigger_url = "https://api.devs-hub.xyz/trigger?image="
        self.delete_url = "https://api.devs-hub.xyz/delete?image="
        self.wasted_url = "https://api.devs-hub.xyz/wasted?image="
        self.beautiful_url = "https://api.devs-hub.xyz/beautiful?image="
  
       
    @commands.command(usage='<member>')
    @commands.cooldown(1, 3, commands.BucketType.user)

    async def hug(self, ctx, member: discord.Member=None):
        """Hugs like a good boi :3"""
        if not member:
            return await ctx.send(f"**Use `{ctx.prefix}hug <member>`!**")
        if member == ctx.author:
            e = discord.Embed(title=f"Oh no! **{member.name}**, you're forever alone :(", color=randomcolor)
            e.set_image(url=sadness)
            return await ctx.send(embed=e)
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://some-random-api.ml/animu/hug') as r:
                res = await r.json()
                e = discord.Embed(title=f"**{member.name}**, you got a hug by **{ctx.author.name}**!", color=randomcolor)
                e.set_image(url=res['link'])
                return await ctx.send(embed=e)

        await ctx.send(embed=e)
    @commands.command(usage='<member>')
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def kiss(self, ctx, member: discord.Member=None):
        """\U0001f633"""
        kisses = [
            "https://media1.tenor.com/images/78095c007974aceb72b91aeb7ee54a71/tenor.gif?itemid=5095865", "https://media.giphy.com/media/ZRSGWtBJG4Tza/giphy.gif", "https://media.giphy.com/media/FqBTvSNjNzeZG/giphy.gif", "https://media.tenor.com/images/8cf98d92c54ee938e1c6617ad8c0e167/tenor.gif", "https://media.giphy.com/media/kU586ictpGb0Q/giphy.gif", "https://media.giphy.com/media/JYpVJEcNrDAWc/giphy.gif",
"https://24.media.tumblr.com/5d51b3bbd64ccf1627dc87157a38e59f/tumblr_n5rfnvvj7H1t62gxao1_500.gif", "https://media.giphy.com/media/KH1CTZtw1iP3W/giphy.gif", "https://uploads.disquscdn.com/images/964bd0189d1674220997816c271470bf5f2c32860ee5bcf63d50031fbc82a0cd.gif", "https://media.giphy.com/media/Gj8bn4pgTocog/giphy.gif", "https://i.imgur.com/eisk88U.gif", "https://media.tenor.com/images/12b26e30f1d526db62847bede9bbd414/tenor.gif",
"https://media.giphy.com/media/ONq87vZz4626k/giphy.gif", "https://media.giphy.com/media/BaEE3QOfm2rf2/giphy.gif", "https://media.tenor.com/images/de18124ebe36764446ee2dbf54a672bf/tenor.gif", "https://media.giphy.com/media/KmeIYo9IGBoGY/giphy.gif", "https://media.giphy.com/media/4gVv2ERASSYYo/giphy.gif", "https://media.giphy.com/media/vUrwEOLtBUnJe/giphy.gif", "https://i.pinimg.com/originals/f5/34/19/f53419e78c719c313b64378168fa94cc.gif",
"https://media.tenor.com/images/197df534507bd229ba790e8e1b5f63dc/tenor.gif", "https://thumbs.gfycat.com/NeatMinorAnglerfish-small.gif", "https://media.giphy.com/media/ll5leTSPh4ocE/giphy.gif", "https://media1.tenor.com/images/f5167c56b1cca2814f9eca99c4f4fab8/tenor.gif?itemid=6155657", "https://media.giphy.com/media/JFmIDQodMScJW/giphy.gif"
            ]
        if not member:
            return await ctx.send(f"**Use `{ctx.prefix}kiss <member>`!**")
        if member == ctx.author:
            e = discord.Embed(title=f"Oh no! **{member.name}**, you're forever alone :(", color=randomcolor)
            e.set_image(url=sadness)
            return await ctx.send(embed=e)
        e = discord.Embed(title=f"**{member.name}**, you got a kiss by **{ctx.author.name}**!", color=randomcolor)
        e.set_image(url=random.choice(kisses))
        return await ctx.send(embed=e)

    @commands.command(usage='<member>')
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def lick(self, ctx, member: discord.Member=None):
        """Lick? OwO"""
        licks = ["https://media1.giphy.com/media/12MEJ2ArZc23cY/source.gif", "https://media0.giphy.com/media/3t2KgMgBgMfwA/source.gif", "https://media1.tenor.com/images/6b701503b0e5ea725b0b3fdf6824d390/tenor.gif?itemid=12141727"]
        if not member:
            return await ctx.send(f"**Use `{ctx.prefix}lick <member>`!**")
        if member == ctx.author:
            e = discord.Embed(title=f"Oh no! **{member.name}**, you're forever alone :(", color=randomcolor)
            e.set_image(url=sadness)
            return await ctx.send(embed=e)
        e = discord.Embed(title=f"**{member.name}**, you got a lick by **{ctx.author.name}**!", color=randomcolor)
        e.set_image(url=random.choice(licks))
        return await ctx.send(embed=e)

    @commands.command(usage='<member>')
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def pat(self, ctx, member: discord.Member=None):
        """Pats a member :3"""
        pats = ["https://media1.tenor.com/images/68d981347bf6ee8c7d6b78f8a7fe3ccb/tenor.gif?itemid=5155410", "https://i.imgur.com/2lacG7l.gif", "https://media1.tenor.com/images/70960e87fb9454df6a1d15c96c9ad955/tenor.gif?itemid=10092582", "https://thumbs.gfycat.com/AgileHeavyGecko-max-1mb.gif", "https://i.imgur.com/4ssddEQ.gif", "https://media.giphy.com/media/ARSp9T7wwxNcs/giphy.gif"]
        if not member:
            return await ctx.send(f"**Use `{ctx.prefix}lick <member>`!**")
        if member == ctx.author:
            e = discord.Embed(title=f"Oh no! **{member.name}**, you're forever alone :(", color=randomcolor)
            e.set_image(url=sadness)
            return await ctx.send(embed=e)
        e = discord.Embed(title=f"**{member.name}**, you got a pat by **{ctx.author.name}**!", color=randomcolor)
        e.set_image(url=random.choice(pats))
        return await ctx.send(embed=e)
    
    @commands.command(usage='<member>')
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def slap(self, ctx, member: discord.Member=None):
        """Slaps a bad boi >:("""
        slaps = ["https://media.giphy.com/media/jLeyZWgtwgr2U/giphy.gif", "https://media1.tenor.com/images/1cf84bf514d2abd2810588caf7d9fd08/tenor.gif?itemid=7679403", "https://media1.tenor.com/images/b6d8a83eb652a30b95e87cf96a21e007/tenor.gif?itemid=10426943", "https://media.giphy.com/media/9U5J7JpaYBr68/giphy.gif"]
        if not member:
            return await ctx.send(f"**Use `{ctx.prefix}lick <member>`!**")
        if member == ctx.author:
            e = discord.Embed(title=f"Oh no! **{member.name}**, you're forever alone :(", color=randomcolor)
            e.set_image(url=sadness)
            return await ctx.send(embed=e)
        e = discord.Embed(title=f"**{member.name}**, you got a slap by **{ctx.author.name}**!", color=randomcolor)


        e.set_image(url=random.choice(slaps))
        return await ctx.send(embed=e)
    @commands.command(name="Poo")
    async def poo(self, ctx):
        embed = discord.Embed(
            title="POO",
            description="HAHAHA POO HAAHAHA STINKY POO HAHA TOILET POO AHAHAHAHAHAH",
            color=discord.Colour.red()
        )
        embed.set_thumbnail(url="https://www.emp.co.uk/dw/image/v2/BBQV_PRD/on/demandware.static/-/Sites-master-emp/default/dw8cf8d57b/images/3/5/8/7/358763a2-emp.jpg?sfrm=png")
        await ctx.channel.send(embed = embed)
        await ctx.channel.send("I'm suuuuuuu-ing you.")

    @commands.command(name="spank", description="Spank a user.")
    @commands.guild_only()
    async def spank(self, ctx, *, member: discord.Member):
        one_time_int =get_otp(digits=4)
        #  random 4 digit int so multiple requests dont overwrite the file
        if member is None:
            member = ctx.author
        async with ctx.typing():
            user1 = ctx.author.avatar_url
            user2 = member.avatar_url
            spank_url = f"{self.spank_url}face={user1}&face2={user2}"

            binary_data = await aiohttp_get_binary(spank_url)

            with open(f"./storage/spank{one_time_int}.png", "wb") as writeFile:
                writeFile.write(binary_data)
            file = discord.File(f"./storage/spank{one_time_int}.png", filename=f"spank{one_time_int}.png")

            embed = discord.Embed(title=f"Get spanked, {member.display_name}!", color=get_color(member))
            embed.set_image(url=f"attachment://spank{one_time_int}.png")
            await ctx.reply(file=file, embed=embed)
        await asyncio.sleep(1)
        os.remove(f"./storage/spank{one_time_int}.png")

    @commands.command(name="hitler", description="Breaking news! [user] is worse than Hitler!")
    @commands.guild_only()
    async def hitler(self, ctx, *, member: discord.Member = None):
        one_time_int = get_otp(digits=4)
        #  random 4 digit int so multiple requests dont overwrite the file
        if member is None:
            member = ctx.author
        async with ctx.typing():
            hitler_url = f"{self.hitler_url}{member.avatar_url}"

            binary_data = await aiohttp_get_binary(hitler_url)

            with open(f"./storage/hitler{one_time_int}.png", "wb") as writeFile:
                writeFile.write(binary_data)
            file = discord.File(f"./storage/hitler{one_time_int}.png", filename=f"hitler{one_time_int}.png")

            embed = discord.Embed(title=f"Oh no {member.name}, what have you done!",
                                  color=get_color(member))
            embed.set_image(url=f"attachment://hitler{one_time_int}.png")
            await ctx.reply(file=file, embed=embed)
        await asyncio.sleep(1)
        os.remove(f"./storage/hitler{one_time_int}.png")

    @commands.command(name="grab", description="Make a user's pfp grab you!")
    @commands.guild_only()
    async def grab(self, ctx, *, user: discord.Member = None):
        one_time_int = get_otp(digits=4)
        #  random 4 digit int so multiple requests dont overwrite the file
        if user is None:
            user = ctx.author
        grab_url = f"{self.grab_url}{user.avatar_url}"
        async with ctx.typing():
            binary_data = await aiohttp_get_binary(grab_url)
            try:
                dict_error = ast.literal_eval(binary_data.decode("utf-8"))
                if dict_error.get("error") is not None:
                    return await ctx.send(dict_error.get("error"))
            except:
                pass
            with open(f"./storage/grab{one_time_int}.png", "wb") as writeFile:
                writeFile.write(binary_data)
            file = discord.File(f"./storage/grab{one_time_int}.png", filename=f"grab{one_time_int}.png")

            embed = discord.Embed(color=get_color(ctx.author))
            embed.set_image(url=f"attachment://grab{one_time_int}.png")
            await ctx.reply(file=file, embed=embed)
        await asyncio.sleep(1)
        os.remove(f"./storage/grab{one_time_int}.png")

    @commands.command(name="trigger", description="Trigger a user! Get a \"Triggered!\" image!")
    @commands.guild_only()
    async def trigger(self, ctx, *, member: discord.Member = None):
        one_time_int = get_otp(digits=4)
        #  random 4 digit int so multiple requests dont overwrite the file
        if member is None:
            member = ctx.author
        grab_url = f"{self.trigger_url}{member.avatar_url}"
        async with ctx.typing():
            binary_data = await aiohttp_get_binary(grab_url)
            with open(f"./storage/trigger{one_time_int}.gif", "wb") as writeFile:
                writeFile.write(binary_data)
            file = discord.File(f"./storage/trigger{one_time_int}.gif", filename=f"trigger{one_time_int}.gif")

            embed = discord.Embed(color=get_color(ctx.author))
            embed.set_image(url=f"attachment://trigger{one_time_int}.gif")
            await ctx.reply(file=file, embed=embed)
        await asyncio.sleep(1)
        os.remove(f"./storage/trigger{one_time_int}.gif")

    @commands.command(name="delete_mem", description="Delete a member. Begone, filthy mortal!")
    @commands.guild_only()
    async def delete_user(self, ctx, user: discord.Member = None, dark=None):
        if user is None:
            user = ctx.author

        one_time_int = get_otp(digits=4)
        if dark == "dark":
            grab_url = f"{self.delete_url}{user.avatar_url}&darkmode={dark}"
        else:
            grab_url = f"{self.delete_url}{user.avatar_url}"
        async with ctx.typing():
            binary_data = await aiohttp_get_binary(grab_url)
            with open(f"./storage/delete{one_time_int}.png", "wb") as writeFile:
                writeFile.write(binary_data)
            file = discord.File(f"./storage/delete{one_time_int}.png", filename=f"delete{one_time_int}.png")
            embed = discord.Embed(color=get_color(user))
            embed.set_image(url=f"attachment://delete{one_time_int}.png")
            await ctx.reply(file=file, embed=embed)
        await asyncio.sleep(1)
        os.remove(f"./storage/delete{one_time_int}.png")

    @commands.command(name="wasted", aliases=["gta"], description="A user's pfp, but with the GTA \"Wasted\" overlay")
    @commands.guild_only()
    async def wasted(self, ctx, *, user: discord.Member = None):
        if user is None:
            user = ctx.author
        url = f"{self.wasted_url}{user.avatar_url}"
        one_time_int = get_otp(digits=4)
        async with ctx.typing():
            binary_data = await aiohttp_get_binary(url)
            with open(f"./storage/wasted{one_time_int}.png", "wb") as writeFile:
                writeFile.write(binary_data)
            file = discord.File(f"./storage/wasted{one_time_int}.png", filename=f"wasted{one_time_int}.png")
            embed = discord.Embed(color=get_color(user), title=f"{user.display_name}, you died.")
            embed.set_image(url=f"attachment://wasted{one_time_int}.png")
            await ctx.reply(file=file, embed=embed)
        await asyncio.sleep(1)
        os.remove(f"./storage/wasted{one_time_int}.png")

    @commands.command(name="beautiful", description="compliment a user for their beauty.")
    @commands.guild_only()
    async def beautiful(self, ctx, *, user: discord.Member = None):
        if user is None:
            user = ctx.author
        url = f"{self.beautiful_url}{user.avatar_url}"
        one_time_int =get_otp(digits=4)
        async with ctx.typing():
            binary_data = await aiohttp_get_binary(url)
            with open(f"./storage/beautiful{one_time_int}.png", "wb") as writeFile:
                writeFile.write(binary_data)
            file = discord.File(f"./storage/beautiful{one_time_int}.png", filename=f"beautiful{one_time_int}.png")
            embed = discord.Embed(color=get_color(user), title=f"{user.display_name}, you're beautiful.")
            embed.set_image(url=f"attachment://beautiful{one_time_int}.png")
            await ctx.reply(file=file, embed=embed)
        await asyncio.sleep(1)
        os.remove(f"./storage/beautiful{one_time_int}.png")


def setup(bot):
    bot.add_cog(Attack(bot))