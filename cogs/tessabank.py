from discord.ext import commands
import perms
import json
import discord
with open("loan.json") as file:
    bank = json.load(file)

class TessaBank(commands.Cog):
    '''Official Tessarect Bank for Economy system - Under Maintainence'''
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def tessabank(self,ctx):
      '''Official Tessarect Bank for Economy system'''
      await ctx.send(embed=discord.Embed(title="Cog under maintainence", description="\n Sorry for it but you can't use this cog for now",color=discord.Color.dark_red(),timestamp=ctx.message.created_at))
'''
    @perms.owner()
    @commands.command(hidden=True)
    async def addm(self, ctx, add: int):
        bank["totals"]["balance"] += add
        with open("bank.json", "w") as file:
            json.dump(bank, file)
        await ctx.send(f'{bank["totals"]["balance"]:,} ')

    @perms.owner()
    @commands.command(hidden=True)
    async def removem(self, ctx, remove: int):
        bank["totals"]["balance"] -= remove
        with open("bank.json", "w") as file:
            json.dump(bank, file)
        await ctx.send(f'{bank["totals"]["balance"]:,} ')

    @perms.owner()
    @commands.command(hidden=True)
    async def count(self, ctx):
        await ctx.send(f'{bank["totals"]["balance"]:,} ')
'''
def setup(bot):
    bot.add_cog(TessaBank(bot))    