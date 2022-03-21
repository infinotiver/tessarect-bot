import subprocess 
import sys

try:
  import vacefron
except:
  subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'vacefron.py'])
import os
import random
import discord
import motor.motor_asyncio
import nest_asyncio
from discord.ext import commands

nest_asyncio.apply()

mongo_url = "mongodb+srv://prakarsh17:Prakarsh_262@enalevel.v4asb.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

cluster = motor.motor_asyncio.AsyncIOMotorClient(mongo_url)
levelling = cluster["discord"]["levelling"]

isitenabled = cluster["discord"]["enalevel"]


class Level(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.vac_api = vacefron.Client()
    @commands.Cog.listener()
    async def on_ready(self):
        print("Levelsys cog loaded successfully")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.guild is not None:
            try:
                stats2 = await isitenabled.find_one({"id": message.guild.id})

            except:
                newuser = {"id": message.guild.id, "type": 1}
                await isitenabled.insert_one(newuser)
            if stats2 is None:
                newuser = {"id": message.guild.id, "type": 1}
                await isitenabled.insert_one(newuser)
                a = 1
            else:
                a = stats2["type"]

            #
            if a == 0:
                #
                stats = await levelling.find_one({"id": message.author.id})
                if not message.author.bot:
                    #
                    if stats is None:
                        newuser = {"id": message.author.id, "xp": 100}
                        levelling.insert_one(newuser)

                    else:
                        xp = stats["xp"] + random.randrange(1,10)
                        levelling.update_one(
                            {"id": message.author.id}, {"$set": {"xp": xp}}
                        )

                        lvl = 0

                        while True:
                            if xp < ((50 * (lvl ** 2)) + (50 * (lvl))):
                                break
                            lvl += 1
                        xp -= (50 * ((lvl - 1) ** 2)) + (50 * (lvl - 1))

                        if xp == 0:

                            await message.channel.send(embed=discord.Embed(description=f"Well done  {message.author.mention} You levelled up to **level: {lvl}**",color=discord.Color.dark_theme()))
                                

        else:
            pass

    @commands.command(aliases=["xp", "r","level"], description="Shows your xp and global rank")
    async def rank(self, ctx,user:discord.Member=None,):
        if user ==None:
          user = ctx.author
        stats2 = await isitenabled.find_one({"id": ctx.guild.id})
        if stats2 is None:
            newuser = {"id": ctx.guild.id, "type": 1}
            await isitenabled.insert_one(newuser)
            a = 1
        else:
            a = stats2["type"]

        if a == 0:
            #

            stats = await levelling.find_one({"id": user.id})
            if stats is None:
                embed = discord.Embed(
                    description=f"No messages, no rank(or you are mentioning a bot are you a stupid person? ) !!!"
                )

                await ctx.channel.send(embed=embed)

            else:
                xp = stats["xp"]
                lvl = 0
                rank = 0

                while True:
                    if xp < ((50 * (lvl ** 2)) + (50 * (lvl))):
                        break
                    lvl += 1
                xp -= (50 * ((lvl - 1) ** 2)) + (50 * (lvl - 1))
                
                boxes = int((xp / (200 * ((1 / 2) * lvl))) * 20)
                rankings = levelling.find().sort("xp", -1)

                async for x in rankings:
                    rank += 1
                    if stats["id"] == x["id"]:
                        break
                if rank > 3:
                  emoji =""
                elif rank ==3:
                  emoji ="🥉"
                elif rank ==2:
                  emoji ="<:2rd:939020302426460220>"
                elif rank ==1:
                  emoji ="<:1st:939020133702201344>"            
                gen_card = await self.vac_api.rank_card(
                            username = str(user),  # wrapper will handle the #
                            avatar = user.avatar_url_as(format = "png"),  # converting avatar to .png, including .gif
                            level = lvl, # optional level int on the xp bar.
                            rank = rank, # optional #int on the card.
                            current_xp = xp,
                            next_level_xp = int(200* ((1/2)*lvl)),  # you will need calculate this according the current_xp.
                            previous_level_xp = 0,  # you will need calculate this according the current_xp.
                            custom_background = 'https://cdn.discordapp.com/attachments/850808002545319957/859359637106065408/bg.png',  # optional custom background.
                            xp_color = '7FFFD4',  # optional progress bar color. Defaults to #fcba41. 
                            #is_boosting = ,  # optional server boost icon next to username.
                            circle_avatar = True  # optional circle avatar instead of a square.
                            )
                rank_image = discord.File(fp = await gen_card.read(), filename = f"{user.name}_rank.png")
                await ctx.channel.send(file = rank_image) 
                #if embed:
                  #await ctx.channel.send(embed=embed)              
        else:
            await ctx.send("**Levelling is disabled here**")

    @commands.command(
        aliases=["db", "lbrank"], description="Shows server leaderboard"
    )
    async def dashboard(self, ctx):
        stats2 = await isitenabled.find_one({"id": ctx.guild.id})
        if stats2 is None:
            newuser = {"id": ctx.guild.id, "type": 1}
            await isitenabled.insert_one(newuser)
            a = 1
        else:
            a = stats2["type"]

        if a == 0:
            #
            rankings = levelling.find().sort("xp", -1)
            i = 1
            embed = discord.Embed(
                timestamp=ctx.message.created_at, title="Rankings", color=0xFF0000
            )
            async for x in rankings:
                try:
                    temp = ctx.guild.get_member(x["id"])
                    tempxp = x["xp"]
                    embed.add_field(
                        name=f"{i} : {temp.name}", value=f"XP: {tempxp}", inline=False
                    )
                    i += 1
                except:
                    pass
                if i == 11:
                    break

            embed.set_footer(
                text=f"Requested By: {ctx.author.name}",
                icon_url=f"{ctx.author.avatar_url}",
            )

            await ctx.channel.send(embed=embed)

        else:
            await ctx.send("**Levelling is disabled here**")


def setup(client):
    client.add_cog(Level(client))