import discord
from discord.ext import commands
import random

def get_embed(_title, _description, _color):
    return discord.Embed(title=_title, description=_description, color=_color)

class games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def findimposter(self, ctx):
        """
        Impostors can sabotage the reactor, 
        which gives Crewmates 30–45 seconds to resolve the sabotage. 
        If it is not resolved in the allotted time, The Impostor(s) will win.
        """

        embed1 = discord.Embed(title = "Who's the imposter?" , description = "Find out who the imposter is, before the reactor breaks down! (15 secs)" , color=0xff0000)
        
        embed1.add_field(name = 'Red' , value= 'RED' , inline=False)
        embed1.add_field(name = 'Blue' , value= 'BLUE' , inline=False)
        embed1.add_field(name = 'Lime' , value= 'GREEN' , inline=False)
        embed1.add_field(name = 'White' , value= 'WHITE' , inline=False)
        
        msg = await ctx.send(embed=embed1)
        
        # imposter : emoji
        emojis = {
            'red': '🔴',
            'blue': '🔵',
            'lime': '🟢',
            'white': '⬜'
        }
        
        # pick the imposter
        imposter = random.choice(list(emojis.items()))
        imposter = imposter[0]
        
        # add all possible reactions
        for emoji in emojis.values():
            await msg.add_reaction(emoji)
        
        # check whether the correct user responded.
        # also check its a valid reaction.
        def check(reaction, user):
            self.reacted = reaction.emoji
            return user == ctx.author and str(reaction.emoji) in emojis.values()

        # waiting for the reaction to proceed
        try: 
            reaction, user = await self.bot.wait_for('reaction_add', timeout=15, check=check)
        
        except TimeoutError:
            # defeat, reactor meltdown
            description = "Reactor Meltdown.{0} was the imposter...".format(imposter)
            embed = get_embed("Defeat", description, discord.Color.red())
            await ctx.send(embed=embed)
        else:
            # victory, correct answer
            if str(self.reacted) == emojis[imposter]:
                description = "**{0}** was the imposter...".format(imposter)
                embed = get_embed("Victory", description, discord.Color.blue())
                await ctx.send(embed=embed)

            # defeat, wrong answer
            else:
                for key, value in emojis.items(): 
                    if value == str(self.reacted):
                        description = "**{0}** was not the imposter... ,".format(key)
                        embed = get_embed("Defeat", description, discord.Color.red())
                        await ctx.send(embed=embed)
                        break
 

def setup(bot):
    bot.add_cog(games(bot))