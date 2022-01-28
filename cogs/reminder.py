import os
import json
import datetime
import time

import discord
from discord.ext import commands
from discord.ext.commands import BucketType, cooldown
import motor.motor_asyncio
import nest_asyncio
import subprocess
import sys
try:

  from apscheduler.schedulers.asyncio import AsyncIOScheduler
except:
  subprocess.check_call([sys.executable, '-m', 'pip', 'install','apscheduler'])

nest_asyncio.apply()



mongo_url = 'mongodb+srv://prakarsh17:Prakarsh_262@remindercog.yjf1z.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
cluster = motor.motor_asyncio.AsyncIOMotorClient(mongo_url)
rem = cluster["bot"]["reminder"]

class Reminder(commands.Cog):
    """ Reminder cog """
    def __init__(self, bot):
        self.bot = bot
        """Start check for reminders"""
        self.bot.loop.create_task(self.reminder_check())

    @commands.Cog.listener()
    async def on_ready(self):
        print("Reminder Cog Loaded Succesfully")

    @commands.command(name='reminder', aliases=['remind'])
    @cooldown(1, 1, BucketType.user)
    async def reminder(self, ctx, time, *, message):
        """Reminds you of something in the future"""
        t_key = {'s':1, 'm':60, 'h':3600, 'd':86400, 'w':604800}
        if len(message) not in range(1,150):
            return await ctx.send("Message length must be between 1 and 150 characters")
        if time[-1] not in t_key:
            return await ctx.send("Time must be in seconds, minutes, hours, days or weeks")
        if time[:-1].isdigit() == False:
            return await ctx.send("Time must be in seconds, minutes, hours, days or weeks")

        cT = datetime.datetime.now()
        t = int(time[:-1]) * t_key[time[-1]]
        if t > 1209600:
            return await ctx.send("Time must be less than 14 days")
        fT = cT + datetime.timedelta(seconds=t)

        stats = await rem.find_one({"id": ctx.author.id})
        embed = discord.Embed(title="Reminder", description=f"\u200b", color=0x1a1aff)
        if stats is None:
            await rem.insert_one({'id' : ctx.author.id, 'reminders' : [{'time' : fT, 'message' : message}]})
            embed = discord.Embed(title="Reminder", description=f"{ctx.author.mention} will be reminded at {fT.strftime('%d/%m/%Y %H:%M:%S')}", color=0xff0000)
            return await ctx.send(embed=embed)
        
        if len(stats['reminders']) >= 5:
            return await ctx.send("You have reached the maximum amount of reminders")
        
        await rem.update_one({"id": ctx.author.id}, {"$push": {"reminders": {'time' : fT, 'message' : message}}})
        embed = discord.Embed(title="Reminder", description=f"{ctx.author.mention} will be reminded at {fT.strftime('%d/%m/%Y %H:%M:%S')}", color=0x007f)
        await ctx.send(embed=embed)

    @commands.command(name='reminders', aliases=['reminds'])
    @cooldown(1, 1, BucketType.user)
    async def reminders(self, ctx):
        """Shows all your reminders"""
        stats = await rem.find_one({"id": ctx.author.id})
        if stats is None:
            return await ctx.send("You have no reminders")
        embed = discord.Embed(title="Reminders", description=f"\u200b", color=0xc8ffff)
        if len(stats['reminders']) == 0:
            return await ctx.send("You have no reminders")
        for i in stats['reminders']:
            embed.add_field(name=f"{i['time'].strftime('%d/%m/%Y %H:%M:%S')}", value=f"{i['message']}", inline=False)
        await ctx.send(embed=embed)

    @commands.command(name='removereminder', aliases=['removeremind','rr'])
    @cooldown(1, 1, BucketType.user)
    async def removereminder(self, ctx, index):
        """Removes a reminder"""
        il = [1,2,3,4,5,'all']
        if index not in il:
            return await ctx.send("Index must be 1, 2, 3, 4, 5 or all")

        stats = await rem.find_one({"id": ctx.author.id})
        if stats is None:
            return await ctx.send("You have no reminders")

        if index == 'all':
            await rem.update_one({"id": ctx.author.id}, {"$set": {"reminders": []}})
            return await ctx.send("Reminder removed")

        if index > len(stats['reminders']):
            return await ctx.send("Index must be less than the amount of reminders")

        reminder = stats['reminders'][int(index) - 1]

        await rem.update_one({"id": ctx.author.id}, {"$pull": {"reminders": {'time' : reminder['time'], 'message' : reminder['message']}}})
        return await ctx.send("Reminder removed")
    
    async def reminder_check(self):
        """
        Setup Scheduler
        Creates a scheduler using AsyncIOScheduler
        """
        scheduler = AsyncIOScheduler(timezone="Asia/Kolkata")
        scheduler.add_job(self.check_reminders, 'interval', seconds=5)
        scheduler.start()
    
    async def check_reminders(self):
        """ 
        Check for Reminders
        Gets the current time and then loop through the whole database.
        If the current time is greater than the time of the reminder, then send the message.
        """
        cT = datetime.datetime.now()
        stats = rem.find()
        async for i in stats:
            for j in i['reminders']:
                if j['time'] <= cT:
                    try:
                        await self.bot.get_user(i['id']).send(f"Reminder: {j['message']}")
                        await rem.update_one({"id": i['id']}, {"$pull": {"reminders": {'time' : j['time'], 'message' : j['message']}}})
                    except Exception as e:
                        print(e)
                        pass

def setup(bot):
    bot.add_cog(Reminder(bot))