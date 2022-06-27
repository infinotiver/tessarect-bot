import os

import discord
import motor.motor_asyncio
import nest_asyncio
from discord.ext import commands
from discord.ext.commands import BucketType, cooldown
from pymongo import MongoClient

nest_asyncio.apply()
mongo_url = os.environ['enalevel']

cluster = motor.motor_asyncio.AsyncIOMotorClient(mongo_url)


notedb = cluster["discord"]["note"]


class Note(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Note cog loaded successfully")

    @commands.command(cooldown_after_parsing=True, description="Notes down  a note for you")
    @cooldown(1, 10, BucketType.user)
    async def note(self, ctx, *, message):
        message = str(message)

        stats = await notedb.find_one({"id": ctx.author.id})
        if len(message) <= 1000:
            #
            if stats is None:
                newuser = {"id": ctx.author.id, "note": message}
                await notedb.insert_one(newuser)
                embed=discord.Embed(title="New Note",description="**<:note:942777255376068659>Your note has been stored**",color=discord.Color.blue())
                await ctx.send(embed=embed)
                await ctx.message.delete()

            else:
                x = notedb.find({"id": ctx.author.id})
                z = 0
                async for i in x:
                    z += 1
                if z > 10 and ctx.author.id !=900992402356043806:
                    await ctx.send("**You cannot add more than 10 notes**")
                else:
                    newuser = {"id": ctx.author.id, "note": message}
                    await notedb.insert_one(newuser)
                    embed=discord.Embed(title="New Note",description="**<:note:942777255376068659>Your note has been stored**",color=discord.Color.blue())
                    await ctx.send(embed=embed)
                    await ctx.message.delete()

        else:
            await ctx.send("**Message cannot be greater then 1000 characters as yo**")

    @commands.command(description="Shows your note")
    async def notes(self, ctx):
        await ctx.send()
        stats = await notedb.find_one({"id": ctx.author.id})
        if stats is None:
            embed = discord.Embed(
                timestamp=ctx.message.created_at,
                title="Notes",
                description=f"{ctx.author.mention} has no notes",
                color=0xFF0000,
            )
            await ctx.send(embed=embed)

        else:
            embed = discord.Embed(
                title="<:notepad:942777255506108438> Your Notepad", description=f"Here are your notes", color=0x34363A
            )
            x = notedb.find({"id": ctx.author.id})
            z = 1
            async for i in x:
                msg = i["note"]
                embed.add_field(name=f"Note {z}", value=f"{msg}", inline=False)
                z += 1
            await ctx.author.send(embed=embed)
            xc = discord.Embed(title="<:checkboxcheck:942779132117409863> Notes sent",description="**Please check your private messages to see your notes**", color=0x34363A)
            await ctx.send(embed=xc)

    @commands.command(description="Delete  the note , it's a good practice")
    async def trash(self, ctx,*,message):
      
        try:
            await notedb.delete_many({"note": message})
            embed=discord.Embed(title="Note Deleted",description=f"<:messagealert:942777256160428063> Your notes having content *{message}* has been deleted  , thank you",color=discord.Color.red())
            await ctx.send(embed=embed)          

        except:
            await ctx.send("**You have no record or some other error occured**")


def setup(client):
    client.add_cog(Note(client))