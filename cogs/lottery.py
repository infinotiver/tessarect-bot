from discord.ext import commands
import datetime, discord, json, random
import perms



with open("loan.json") as file:
    bank = json.load(file)
with open("lottery.json") as file:
    lottery = json.load(file)

class Lottery(commands.Cog):
    '''Lottery Commands'''
    def __init__(self, bot):
        self.bot = bot

    @commands.group(invoke_without_command=True)
    async def lottery(self, ctx):
        '''Lottery help command'''
        em = discord.Embed(title="__**Lottery Commands**__",description="\n"
                   "__*Developers+ Commands*__\n"
                   "**lottery end**\n"
                   "**lottery confirm** (Discord) (Tickets Purchased)\n"
                   "**lottery start** (cost per ticket) (end date) (end time)\n"
                    "__*Everyone*__\n"
                    "**lottery buy** (IGN(YOUR ID)) (# of tickets you want to buy)")
        em.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRxNZetVc2eE3g0PgekaiOF_4pRHzAnkhN5FQ&usqp=CAU")
        await ctx.send(embed=em)
        

    @commands.has_any_role(perms.captain_role, perms.owner_role)
    @lottery.command()
    async def start(self, ctx, price: int, *,end: str):
        '''Start a lottery'''
        lottery_channel = self.bot.get_channel(929332540131643464)
        lottery["price"] = price
        end = datetime.datetime.strptime(end,"%d/%m/%y")
        lottery["end"] = end.strftime("%d/%m/%y")
        with open("lottery.json", "w") as file:
            json.dump(lottery, file)
        message = (f'**Lottery Started**\n@everyone\nStarted on {datetime.datetime.utcnow().strftime("%d/%m/%y")}. Will be ending on {end.strftime("%d/%m/%y")}. The tickets can be bought for {price:,}  each.')
        await lottery_channel.send(message)

    @commands.has_any_role(perms.captain_role, perms.owner_role)
    @lottery.command()
    async def confirm(self, ctx, user: discord.User, tickets: int):
        '''Confirm a user has brough a ticket'''
        lottery_channel = self.bot.get_channel(929332540131643464)
        price = lottery["price"]
        if user.name in lottery["buyers"].keys():
            lottery["buyers"].update({user.name:(lottery["buyers"][user.name]+tickets)})
        else:
            lottery["buyers"].update({user.name:tickets})
        with open("lottery.json", "w") as file:
            json.dump(lottery, file)
        await lottery_channel.send(f"{tickets} lottery tickets brought by {user.mention}")
        await ctx.send(f"{tickets} lottery tickets brought by {user.mention} for {tickets*price:,} gems")

    @commands.is_owner()
    @lottery.command()
    async def end(self, ctx):
        '''End the lottery'''
        lottery_channel = self.bot.get_channel(929332540131643464)
        if datetime.datetime.now().strftime("%d/%m/%y") == lottery["end"]:
            pass
        elif datetime.datetime.now()>datetime.datetime.strptime(lottery["end"],"%d/%m/%y"):
            pass
        else:
            await ctx.send(f'The end date is {lottery["end"]}. Today is {datetime.datetime.now().strftime("%d/%m/%y")}')
            return
        list = []
        for name in dict.keys(lottery["buyers"]):
            for ticket in range(lottery["buyers"][name]):
                list.append(name)
        winner = random.choice(list)
        await ctx.send(f"{winner} has won the lottery. They won {len(list)*lottery['price']:,} gems")
        await lottery_channel.send(f"**Lotery ended**\n@eve ryone\nThere were {len(list)} tickets sold for {lottery['price']:,} gems.\n**The Winner was {winner} and the win {len(list)*lottery['price']:,} **")
        lottery["price"] = 0
        lottery["end"] = "None"
        lottery["buyers"] = {}
        with open("lottery.json", "w") as file:
            json.dump(lottery, file)

    @lottery.command()
    async def buy(self, ctx, ign: str, tickets: int):
        '''Request to buy a lottery ticket'''
        todo_channel = self.bot.get_channel(929333807893598238)
        await todo_channel.send(f"@everyone user {ctx.author.mention} wants to buy {tickets:,} tickets for the lottery. Their ign is `{ign}`. Please collect {tickets*lottery['price']:,} gems from them in game")
        await ctx.send(f"You have brough {tickets} tickets. This will cost you {tickets*lottery['price']:,} gems")

def setup(bot):
    bot.add_cog(Lottery(bot))