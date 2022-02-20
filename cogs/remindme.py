import datetime
import os
import time

import discord
import motor.motor_asyncio
import nest_asyncio
import requests
from discord.ext import commands, tasks, timers
from discord.ext.commands import BucketType, cooldown
from pymongo import MongoClient

nest_asyncio.apply()
mongo_url = os.environ['remindmongo']
cluster = motor.motor_asyncio.AsyncIOMotorClient(mongo_url)
reminder = cluster["discord"]["reminder"]



class Remind(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.checker.start()

    @commands.Cog.listener()
    async def on_ready(self):
        print("Remind cog loaded successfully")

    @commands.command(cooldown_after_parsing=True, aliases=["remind", "reminder"])
    @cooldown(1, 5, BucketType.user)
    async def notify(self, ctx: commands.Context, ttime, *, desc: str):
        try:

            if len(desc) < 100:
                typ = ttime[-1]
                ttime = int(ttime[0:-1])
                choices = ["s", "m", "h", "d"]
                if typ not in choices:
                    em = discord.Embed(title="Invalid Format",description="**Only s(seconds), m(minutes),h(hours),d(days)**",color=0x34363A)
                    await ctx.send(embed=em)
                else:
                    if typ == "s":
                        conv = ttime
                    elif typ == "m":
                        conv = ttime * 60
                    elif typ == "h":
                        conv = ttime * 3600
                    elif typ == "d":
                        conv = ttime * 86400

                    if conv > 604800:
                        em = discord.Embed(title="Too Long",description="**Not more than 7 days**",color=0x34363A)                      
                        await ctx.send(embed=em)
                    else:
                        em = discord.Embed(title="<:timer:941993935507689492> Successfully Set Reminder",description=f"**Reminder has been set**\n Time set: {datetime.timedelta(seconds=conv)}",color=0x34363A)
                        await ctx.send(embed=em)
                        a = datetime.datetime.now()
                        a = a + datetime.timedelta(seconds=conv)
                        newuser = {
                            "id": ctx.author.id,
                            "Time": a,
                            "Desc": desc,
                        }
                        await reminder.insert_one(newuser)

            else:
                await ctx.send("**Too Long Reminder**")
        except ValueError:
            pass

    @tasks.loop(seconds=10)
    async def checker(self):
        try:
            all = reminder.find({})
            current = datetime.datetime.now()
            async for x in all:
                if current >= x["Time"]:

                    desc = x["Desc"]
                    person = self.client.get_user(int(x["id"]))
                    em = discord.Embed(title="<:timer:941993935507689492> Reminder",description=f"**Reminder > {desc}**\n",color=0x34363A)                    
                    await person.send(embed=em)
                    await reminder.delete_one(x)
                else:
                    pass
        except Exception as e:
            print(e)


def setup(client):
    client.add_cog(Remind(client))