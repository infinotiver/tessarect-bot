import os
# Recommended cog for uploading stats to Void Bots' api.
from discord.ext import commands
import aiohttp # Use `pip install aiohttp` to install
from discord.ext import  tasks
class StatsUpload(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.VoidUpload.start()

  def cog_unload(self):
    self.VoidUpload.cancel()

  @tasks.loop(minutes = 30)
  async def VoidUpload(self):
    await self.bot.wait_until_ready()
    async with aiohttp.ClientSession() as session:
      async with session.post(url = f"https://api.voidbots.net/bot/stats/{self.bot.user.id}",
      headers = {
        "content-type":"application/json",
        "Authorization": os.environ['void']
        },
      json = {
        "server_count": len(self.bot.guilds),
        "shard_count": len(self.bot.shards) #Uncomment this line if shards are used.
        }) as r:
        json = await r.json()
        print(json)

def setup(bot):
 bot.add_cog(StatsUpload(bot))   