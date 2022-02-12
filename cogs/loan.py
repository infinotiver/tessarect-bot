from discord.ext import commands

import perms
import discord, json, asyncio

with open("loan.json") as file:
    bank = json.load(file)


class Loan(commands.Cog):
    '''Loan Commands'''
    def __init__(self, bot):
        self.bot = bot

    @commands.group(invoke_without_command=True)
    async def loan(self,ctx):
        '''Loan help command'''
        e= discord.Embed(title="Loan Command",description="Do you have less money in your wallet ? you can take a loan\n\n"
                   "**Everyone**\n"
                   "**loan request** (id) (Amount Loaned) (Amount Owed) \n",color=discord.Color.blue())
        e.add_field(name="**Owners + Tessarect Special Officers**",value="**loan accept** (Discord) (Amount Loaned) (Amount Owed)\n"
                   "**loan deny** (Discord) (Amount Loaned) (Reason)\n")     
        e.add_field(name="**Developers and above**",value= "**loan payback** (Discord) (Amount Paidback)\n"
                   "**loan update**\n")    
                             
        #e.add_field(name="CURRENT BALANCE OF BANK",value=f"")
        await ctx.send(embed=e)

    @commands.has_any_role(perms.captain_role, perms.owner_role)
    @loan.command()
    async def accept(self,ctx, user: discord.User, loaned: int, payback: int):
        '''Accept a loan'''
        if (loaned) >= ((bank["totals"]["balance"]-bank["totals"]["deposits"])// 25):
            await ctx.send(f"The loan of {loaned:,} ֍ is too big and will take us under our 25% reserve. Please decline this loan")
        else:
            todo_channel = self.bot.get_channel(929333807893598238)
            bank_channel = self.bot.get_channel(929332268688887908)
            await todo_channel.send(f"{ctx.author.mention} **, collect {payback:,} ֍ from {user.mention}.** They borrowed {loaned:,} ֍ from the Amteor International Bank.")
            await bank_channel.send(f"**-{loaned:,} ֍** Loaned to {user.mention}. Will pay back {payback:,} ֍.")
            bank["totals"]["balance"] -= loaned
            bank["totals"]["loans"] += payback
            with open("loan.json", "w") as file:
                json.dump(bank, file)
            await ctx.user.send(f"You have given {user.mention} a loan of {loaned:,} ֍. They will pay back with {payback:,} ֍.IT IS NOT CREDITED BTW AS THIS COMMAND IS UNDER DEVELOPMENT")

    @commands.has_any_role(perms.captain_role, perms.owner_role)
    @loan.command()
    async def deny(self, ctx, user: discord.User, amount: int, *, reason):
        '''Decline a loan'''
        await ctx.send(f"{user} has been denied of their {amount:,} ֍ loan.")
        await user.send(f"Your loan of {amount:,} ֍ has been denied. Reason: {reason}")


    @commands.has_role(perms.staff_role)
    @loan.command()
    async def payback(self, ctx, user: discord.User, paidback: int):
        '''Confirm a users loan repayment'''
        bank_channel = self.bot.get_channel(929332268688887908)
        bank["totals"]["balance"] += paidback
        await bank_channel.send(f"**+{paidback:,} ֍** Loan payment from {user.mention}")
        with open("loan.json", "w") as file:
            json.dump(bank, file)
        await ctx.send(f"Loan payment from {user.mention} of {paidback:,} ֍. Processed")

    @loan.command()
    async def request(self, ctx, id: str, amount: int, payback: int):
        '''Request a loan from the clan'''
        loan_channel = self.bot.get_channel(929332268688887908)
        await loan_channel.send(f"@everyone, discord user {ctx.author.mention} has requested a {amount:,} gem loan. They have offered to pay back {payback:,} ֍, and their id is `{id}`. Do a!loan {ctx.author.mention} {amount} {payback} to accept their loan, or if their loan is denied, do a!loan deny {ctx.author.mention} {amount} reason")
        await ctx.send(f"Your loan request for {amount:,} ֍ has been sent. You have offered to pay back the loan with {payback:,} ֍. ")

    @commands.has_role(perms.staff_role)
    @loan.command()
    async def update(self, ctx):
        '''Gets an update on number of ֍ loaned to users'''
        loan_amount = bank["totals"]["loans"]
        await ctx.send(f"Total amount of ֍ waiting to be paid back from loans is {loan_amount:,} ֍")

def setup(bot):
    bot.add_cog(Loan(bot))