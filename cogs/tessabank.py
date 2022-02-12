from discord.ext import commands
import perms
import json

with open("loan.json") as file:
    bank = json.load(file)

class TessaBank(commands.Cog):
    '''You See Nothing'''
    def __init__(self, bot):
        self.bot = bot

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

def setup(bot):
    bot.add_cog(TessaBank(bot))    