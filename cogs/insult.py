import aiohttp
import discord
from discord.ext import commands
from discord.ext.commands import BucketType, cooldown


class Fancy(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Insult cog loaded successfully")

    @commands.command(description="Roasts :)")
    async def roast(self, ctx, member: discord.Member = None):
        if member == None:
            member = ctx.author

        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"https://insult.mattbas.org/api/insult"
            ) as response:
                insult = await response.text()
                embed = discord.Embed(
                    timestamp=ctx.message.created_at,
                    title=f"{member.name} made roasted 🍳 toast 🍞",
                    description=f"{insult}",
                    color=0xFF0000,
                )
                embed.set_thumbnail(url="https://i.pinimg.com/originals/b4/b6/4a/b4b64a36369525c0f0574bdb0cb5239d.jpg")
                await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Fancy(client))