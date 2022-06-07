import speedtest
import discord 
import datetime, time 
import asyncio
from discord.ext import commands
time_data = {
    'str': datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
    'obj': time.time()
}

class Stats(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Uptime cog Loaded  has been loaded') 
        global startTime 
        startTime = time.time()

    @commands.command(name='uptime',aliases=['upt'],help="Know for how long I am online")
    async def _uptime(self,ctx):
        uptime = str(datetime.timedelta(seconds=int(
            round(time.time() - time_data['obj']))))

        embed=discord.Embed(color=discord.Color.green())
        #embed.set_thumbnail(url="https://cdn.vectorstock.com/i/1000x1000/90/58/monitoring-bot-color-icon-monitor-websites-uptime-vector-29169058.webp")
        embed.set_footer(text='Hiya ! Have fun , checkout help')
        embed.set_image(url=f"https://falsiskremlin.sirv.com/resim_2020-11-28_113400.png?text.0.text={uptime}&text.0.position.x=-20%25&text.0.position.y=-30%25&text.0.size=50&text.0.color=ffffff&watermark.0.image=%2FImages%2Fresim_2020-11-29_103837.png&watermark.0.position.x=-35%25&watermark.0.scale.width=170&watermark.0.scale.height=170")
        await ctx.send(embed=embed)
    @commands.command(
        name='ping', 
        help='Shows my current response time.'
    )
    @commands.guild_only()
    async def ping(self, ctx: commands.Context):
        
        system_latency = round(self.bot.latency * 1000)

        shard_id = ctx.guild.shard_id
        shard = self.bot.get_shard(shard_id)
        shard_ping = shard.latency
        if shard_ping <= 4 :
          xc = discord.Color.green()
        elif shard_ping <=9:
          xc = 0xFFFF00
        else:
          xc = discord.Color.red()       
        start_time = time.time()
        message = await ctx.reply('<a:Loading:941646457562365962> Please wait...')
        end_time = time.time()
        api_latency = round((end_time - start_time) * 1000)

        uptime = str(datetime.timedelta(seconds=int(
            round(time.time() - time_data['obj']))))
        embed = (
            discord.Embed(
                color=xc
            ).add_field(
                name='<:CPU:937722162897375282> System Latency', 
                value=f'{system_latency}ms ({self.bot.shard_count} shards)', 
                inline=False
            ).add_field(
              name="<:Discord_Region:946289542330196028>  Shard Stats",value=f"Shard Id: {shard_id} "
            ).add_field(
                name='<:planet:930351400532201532> API Latency',
                value=f'{api_latency}ms', 
                inline=False
              
            ).add_field(
                name='<:Servers:946289809289281566> Startup Time', 
                value=time_data['str'], 
                inline=False
            ).add_field(
                name='<:online_status:930347639172657164> Uptime', 
                value=uptime, 
                inline=False
            )
        ).set_thumbnail(
          url=self.bot.user.avatar_url
        )
      
        em2=discord.Embed(color=discord.Color.random(),description="<a:Loading:941646457562365962> Sorting and Setting up things")
        await message.edit(content=None, embed=em2)
        await asyncio.sleep(0.2)
        await message.edit(content=None, embed=embed)
    @commands.command(pass_context=True)
    async def speedtest(self, ctx):
      message = await ctx.send(embed=discord.Embed(description='Speed Test Started...',color=discord.Color.blue()))
      try:
        st = speedtest.Speedtest()
        st.get_best_server()
        l = asyncio.get_event_loop()
        msg = '**Speed Test Results:**\n'
        msg += '```\n'
        await message.edit(embed=discord.Embed(color=discord.Color.gold(),description="Running speed test...\n- Downloading..."))
        d = await self.bot.loop.run_in_executor(None, st.download)
        msg += '    Ping: {} ms\nDownload: {} Mb/s\n'.format(round(st.results.ping, 2), round(d/1024/1024, 2))
        await message.edit(embed=discord.Embed(color=discord.Color.dark_gold(),description="Running speed test...\n- Downloading...\n- Uploading..."))
        u = await self.bot.loop.run_in_executor(None, st.upload)
        msg += '  Upload: {} Mb/s```'.format(round(u/1024/1024, 2))
        await message.edit(embed=discord.Embed(color=discord.Color.dark_blue(),description=msg))
      except Exception as e:
        await message.edit(content="Speedtest Error: {}".format(str(e)))   
def setup(bot):

    bot.add_cog(Stats(bot))    