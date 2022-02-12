import discord
from discord.ext import commands
from algoliasearch.search_client import SearchClient
import os
class DiscordHelp(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        ## Fill out from trying a search on the ddevs portal
        app_id = os.environ['appid']
        api_key = os.environ['appkey']
        self.search_client = SearchClient.create(app_id, api_key)
        self.index = self.search_client.init_index('discord')
    @commands.command(help="discord api docs")
    async def ddoc(self, ctx, *, search_term):
        results = await self.index.search_async(search_term)
        description = ""
        hits = []
        for hit in results["hits"]:
            title = self.get_level_str(hit["hierarchy"])
            if title in hits:
                continue
            hits.append(title)
            url = hit["url"].replace("https://discord.com/developers/docs", "https://discord.dev")
            description += f"[{title}]({url})\n"
            if len(hits) == 10:
                break
        embed = discord.Embed(title="These might be Useful!", description=description, color=discord.Color.random())
        await ctx.send(embed=embed)

    def get_level_str(self, levels):
        last = ""
        for level in levels.values():
            if level is not None:
                last = level
        return last


def setup(bot):
    bot.add_cog(DiscordHelp(bot))