import aiohttp
import discord
import requests
from discord.ext import commands


class Calculator(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.description="<:sucess:935052640449077248> Calculator "

    @commands.Cog.listener()
    async def on_ready(self):
        print("Calc cog loaded successfully")

    @commands.command(description="Calculates the given expression")
    async def calc(self, ctx, *, expression):
        if len(expression) > 10000:
            await ctx.send("**I dont think I can bear that much**")
        else:
            st = expression.replace("+", "%2B")
            async with aiohttp.ClientSession() as session:
                async with session.get(
                    f"https://api.mathjs.org/v4/?expr={st}"
                ) as response:
                    ex = await response.text()
                    if len(ex) > 20000:
                        await ctx.send("I dont think I can bear that much")
                    else:

                        embed = discord.Embed(
                            timestamp=ctx.message.created_at,
                            description="Here is the result ",
                            color=discord.Color.gold()
                        )
                        embed.add_field(
                            name=f"Expression", value=f"```css\n{expression}```", inline=False
                        )                      
                        embed.add_field(
                            name=f"Result", value=f"```css\n{ex}```", inline=False
                        )
                        
                        embed.set_author(
                            name="Calculator"
                            
                        )
                        embed.set_thumbnail(url="https://www.involve.me/assets/images/blog/how-to-create-a-simple-price-calculator-and-capture-more-leads/calculator-L.png",)
                        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Calculator(client))