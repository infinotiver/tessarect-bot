
import discord
import datetime
from discord.ext import commands



class ServerLogs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.description = "Shows when the bot joins or leaves a guild"
        self.theme_color = discord.Color.green()
        self.logs_channel = 929333502577606656

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        embed = discord.Embed(
            title="I Have Joined A New Guild!",
            description=guild.name,
            timestamp=datetime.datetime.now(),
            color=self.theme_color,
        )
        embed.add_field(name="Server ID",value=guild.id)
        embed.add_field(
            name=f"This Guild Has {guild.member_count} Members!",
            value=f"Yay Another Server! We Are Now At {len(self.bot.guilds)} Guilds!",
        )
        await self.bot.get_channel(self.logs_channel).send(embed=embed)


    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        embed = discord.Embed(
            title="I Have Left A Guild!",
            description=f"{guild.name}",
            timestamp=datetime.datetime.now(),
            color=self.theme_color,
        )
        embed.add_field(name="Server ID",value=guild.id)                        
        embed.add_field(
            name=f"We Are Now At {len(self.bot.guilds)} Guilds!", value="_ _"
        )
        await self.bot.get_channel(self.logs_channel).send(embed=embed)


def setup(bot):
    bot.add_cog(ServerLogs(bot))