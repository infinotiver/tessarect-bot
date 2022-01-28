import discord 
import datetime, time 

from discord.ext import commands
restart_data = {
    'str': str(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")),
    'obj': time.time()
}
#this is very important for creating a cog
class UPTIME(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self} has been loaded') 
        global startTime 
        startTime = time.time()

    #create a command in the cog
    @commands.command(name='uptime')
    async def _uptime(self,ctx):

        # what this is doing is creating a variable called 'uptime' and assigning it
        # a string value based off calling a time.time() snapshot now, and subtracting
        # the global from earlier
        uptime = str(datetime.timedelta(seconds=int(
            round(time.time() - restart_data['obj']))))
        embed=discord.Embed(title='Uptime ',description='Here is time I am online for you',color=discord.Color.blue())
        embed.add_field(name='UPTIME',value=uptime)
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
        message = await ctx.reply('Testing overall speed...')
        end_time = time.time()
        api_latency = round((end_time - start_time) * 1000)

        uptime = str(datetime.timedelta(seconds=int(
            round(time.time() - restart_data['obj']))))

        embed = (
            discord.Embed(
                color=xc
            ).add_field(
                name='System Latency', 
                value=f'{system_latency}ms [{self.bot.shard_count} shard(s)]', 
                inline=False
            ).add_field(
              name="SHARD STATS",value=f"Shard Id :{shard_id} \n Shard Ping :{shard_ping}").add_field(
                name='API Latency',
                value=f'{api_latency}ms'
            ).add_field(
                name='Startup Time', 
                value=restart_data['str'], 
                inline=False
            ).add_field(
                name='Uptime', 
                value=uptime, 
                inline=False
            ).set_footer(
                text='Ping'
               
            )
        )
        await message.edit(content=None, embed=embed)
    
def setup(bot):

    bot.add_cog(UPTIME(bot))    