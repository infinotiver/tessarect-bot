def convert(time):
    pos = ["s", "m", "h", "d", "w"]
    time_dict = {"s": 1, "m": 60, "h": 3600, "d": 3600 * 24, "w": 3600 * 24 * 7}
    unit = time[-1]

    if unit not in pos:
        return -1
    try:
        val = int(time[:-1])
    except:
        return -2

    return val * time_dict[unit]

import discord
from discord.ext import commands
import asyncio
import random
import motor.motor_asyncio
import nest_asyncio
import requests
from discord.ext import commands, tasks, timers
import os
from pymongo import MongoClient
import datetime

#import time
nest_asyncio.apply()
mongo_url = os.environ.get("tst")
cluster = motor.motor_asyncio.AsyncIOMotorClient(mongo_url)
give = cluster["tst"]["give"]
class Giveaway(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.checker.start()

    @commands.command()
    #@commands.has_role(config['giveaway_role'])
    async def giveaway(self, ctx):
        timeout = 30
        embedq1 = discord.Embed(title="<a:tada_animated:985058030305566780> | Giveaway Setup Wizard",
                                description=f"Welcome to the Setup Wizard. Answer the following questions within ``{timeout}`` Seconds!",color=0xffd700)
        embedq1.add_field(name="<:arrow_right:940608259075764265> | Question 1",
                          value="Where should we host the Giveaway?\n\n **Example**: ``#General``")
        embedq2 = discord.Embed(title="<a:tada_animated:985058030305566780> | SETUP WIZARD",
                                description="Great! Let's move onto the next question.",color=0xffd700)
        embedq2.add_field(name="<:arrow_right:940608259075764265> | Question 2",
                          value="How long should it last? ``<s|m|h|d|w>``\n\n **Example**:\n ``1d``")
        embedq3 = discord.Embed(title="<a:tada_animated:985058030305566780> | SETUP WIZARD",
                                description="Awesome. You've made it to the last question!",color=0xffd700)
        embedq3.add_field(name="<:arrow_right:940608259075764265> | Question 2",
                          value="What is the prize the winner will receive?\n\n **Example**:\n ``10000 TESSARECT COINS``",)

        questions = [embedq1,
                     embedq2,
                     embedq3]

        answers = []

        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        for i in questions:
            await ctx.send(embed=i)

            try:
                msg = await self.client.wait_for('message', timeout=30, check=check)
            except asyncio.TimeoutError:
                embed = discord.Embed(title="<a:tada_animated:985058030305566780> **Giveaway Wizard**",
                                      description=":x: You didn't answer in time!",color=0xffd700)
                await ctx.send(embed=embed)
                return
            else:
                answers.append(msg.content)

        try:
            c_id = int(answers[0][2: -1])
        except:
            embed = discord.Embed(title="<a:tada_animated:985058030305566780> **Giveaway Wizard**",
                                  description=":x: You didn't specify a channel correctly!",color=0xffd700)
            await ctx.send(embed=embed)
            return

        channel = self.client.get_channel(c_id)

        time = datetime.datetime.now()
        time = time + datetime.timedelta(seconds=convert(answers[1]))
        if time == -1:
            embed = discord.Embed(title="<a:tada_animated:985058030305566780> **Giveaway Wizard**",
                                  description=":x: You didn't set a proper time unit!",color=0xffd700)
            await ctx.send(embed=embed)
            return
        elif time == -2:
            embed = discord.Embed(title="<a:tada_animated:985058030305566780> **Giveaway Wizard**",
                                  description=":x: Time unit **MUST** be an integer",color=0xffd700)
            await ctx.send(embed=embed)
            return
        prize = answers[2]

        embed = discord.Embed(title="<a:tada_animated:985058030305566780> **Giveaway Wizard**",
                              description="Okay, all set. The Giveaway will now begin!",color=0xffd700)
        embed.add_field(name="Hosted Channel:", value=f"{channel.mention}")
        embed.add_field(name="Time:", value=f"{answers[1]}")
        embed.add_field(name="Prize:", value=prize)
        await ctx.send(embed=embed)
        print(
            f"New Giveaway Started! Hosted By: {ctx.author.mention} | Hosted Channel: {channel.mention} | Time: {answers[1]} | Prize: {prize}")
        print("------")
        embed = discord.Embed(title=f"<a:tada_animated:985058030305566780> **GIVEAWAY FOR: {prize}**",
                              description=f"React With 🎉 To Participate!",color=0xffd700)
        embed.add_field(name="Lasts:", value=answers[1])
        embed.add_field(name=f"Hosted By:", value=ctx.author.mention)
        msg = await channel.send(embed=embed)
        newuser = {
            "Time": time,
            "Prize":prize,
            "msg":msg.id,
            "Channel": channel.id,
            "set":0
        }
        await give.insert_one(newuser)
        await msg.add_reaction('🎉')

    @tasks.loop(minutes=1)
    async def checker(self):
        try:
            all = give.find({})
            current = datetime.datetime.now()
            async for x in all:
                if current >= x["Time"] and x['set']==0:
                    #set=x['set']=1
                    #await give.update_one(set)
                    channel = self.client.get_channel(x["Channel"])
                    prize=x['Prize']
                  
                    msg = await channel.fetch_message(x["msg"])
                    new_msg = await channel.fetch_message(x["msg"])
                    
                    users = await new_msg.reactions[0].users().flatten()
                    print(users)
                    users.pop(users.index(self.client.user))

                    winner = random.choice(users)

                    await channel.send(f":tada: Congratulations! {winner.mention} won: **{x['Prize']}**!")
                    print(f"New Winner! User: {winner.mention} | Prize: {prize}")
                    print("------")
                    
                    embed2 = discord.Embed(title=f"<a:tada_animated:985058030305566780> **GIVEAWAY FOR: {x['Prize']}**",
                                          description=f":trophy: **Winner:** {winner.mention}",color=0xffd700)
                    embed2.set_footer(text="Giveaway Has Ended")
                    await msg.edit(embed=embed2)
                    await give.delete_one(x)
                    
                else:
                    pass
        except Exception:
            pass

def setup(client):
    client.add_cog(Giveaway(client))