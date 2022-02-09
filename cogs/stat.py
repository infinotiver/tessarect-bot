import os
# Recommended cog for uploading stats to Void Bots' api.
from discord.ext import commands
import aiohttp # Use `pip install aiohttp` to install
from discord.ext import  tasks
from discord.ext import tasks

import topgg
dbl_token = os.environ['topgg']
class StatsUpload(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.VoidUpload.start()
    self.DiscordBotsUpload.start()
    self.update_stats.start()
    self.bot.topggpy = topgg.DBLClient(self.bot, dbl_token)    

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
  @tasks.loop(minutes = 30)
  async def DiscordBotsUpload(self):
    await self.bot.wait_until_ready()
    async with aiohttp.ClientSession() as session:
      async with session.post(url = f"https://discordbots.gg/api/servers",
      headers = {
        "Authorization": f"bearer {os.environ['discordbots']}"
        },
      json = {
        "client_id": self.bot.user.id,
        "count": len(self.bot.guilds) 
        }) as r:
        json = await r.json()
        print(json)
  @commands.Cog.listener()
  async def on_dbl_vote(self, data):
      user = data['user']
      embed = discord.Embed(description="New Vote! Voter: {}".format(user))
      channel = self.bot.get_channel(int(929332390432735243))
      await channel.send(embed=embed) 


  # This example uses tasks provided by discord.ext to create a task that posts guild count to Top.gg every 30 minutes.

    # set this to your bot's Top.gg token
  


  @tasks.loop(minutes=30)
  async def update_stats():
      """This function runs every 30 minutes to automatically update your server count."""
      try:
          await self.bot.topggpy.post_guild_count()
          print(f"Posted server count ({self.bot.topggpy.guild_count})")
      except Exception as e:
          print(f"Failed to post server count\n{e.__class__.__name__}: {e}")


    
def setup(bot):
 bot.add_cog(StatsUpload(bot))   