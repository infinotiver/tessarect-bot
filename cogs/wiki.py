import asyncio
from random import randint

import discord
import requests
import wikipedia
from discord.ext import commands
from discord.ext.commands import BucketType, cooldown


class Wiki(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.description="<:sucess:935052640449077248> Search Wikipedia"

    @commands.Cog.listener()
    async def on_ready(self):
        print("Wiki cog loaded successfully")

    @commands.command(
        cooldown_after_parsing=True, description="Shows wikipedia summary"
    )
    @cooldown(1, 10, BucketType.user)
    async def wiki(self, ctx, *, msg):
        try:
            content = wikipedia.summary(msg, auto_suggest=False, redirect=True)

            embed = discord.Embed(title="Wikipedia", color=0xB2BEB5)
            chunks = [content[i : i + 1024] for i in range(0, len(content), 2000)]
            for chunk in chunks:
                embed.add_field(name="\u200b", value=chunk, inline=False)
            await ctx.send(embed=embed)
        except:
            await ctx.send(embed = discord.Embed(title="**Failed to get information**",description='No results for that topic, kindly search again and be sure to check case and spelling !',color=0xB2BEB5))

    @commands.command(
        cooldown_after_parsing=True,
        description="Search the wikipedia and see the results",
    )
    @cooldown(1, 5, BucketType.user)
    async def search_wiki(self, ctx, *, msg):
        try:

            content = wikipedia.search(msg, results=5, suggestion=True)
            content = content[0]
            embed = discord.Embed(title="Search Results", color=0xB2BEB5)
            z = 1
            for i in content:
                embed.add_field(name="\u200b", value=f"{z}-{i}", inline=False)
                z += 1

            await ctx.send(embed=embed)
        except:
            await ctx.send("**Failed to get information**")


def setup(client):
    client.add_cog(Wiki(client))