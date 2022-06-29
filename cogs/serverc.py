import os
import aiohttp
import discord
from discord.ext import commands
import motor.motor_asyncio
from assets.reactor import reactor
import nest_asyncio              
nest_asyncio.apply()
mongo_url = os.environ.get("tst")
cluster = motor.motor_asyncio.AsyncIOMotorClient(mongo_url)
db = cluster["tst"]["data"]
telecluster=cluster["tst"]["tele"]
class ServerConnect(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("ServerConnect cog loaded successfully")

    @commands.command(aliases=["ServerConnect",'sc'])
    async def ServerHelp(self, ctx):
      em=discord.Embed(title="<:book:939017828852449310> Server Connection Help",description="This module helps in organising your server and creating your server channels and more from any of the other server tessarect is present . There are many more features coming . This help will be updated on their arrival*",color=discord.Color.dark_blue(),timestamp=ctx.message.created_at)
      em.add_field(name="<:dnd_status:946652840053600256> Important",value="Not all servers available , only servers which has used `allowservertemplate` command ( command available )")
      em.add_field(name="View Templates",value="Check which all server templates you can use using `viewtemplates` command")
      stats = await db.find_one({"n":"stemplates"})   
      list=stats['id']
      if ctx.guild.id in list:
        em.add_field(name="Server in database ",value=f"This server ({ctx.guild}) is in our database and is available to {len(self.client.users)} users to import channels and more",inline=False)
      await ctx.send(embed=em
                    )

    @commands.command(aliases=['ast','allowservertemplate'])
    @commands.has_permissions(administrator=True)
    async def Allowtemplate(self, ctx):   
      
      await ctx.send(embed=discord.Embed(description='''Allowing this will give access to all users of Tessarect to import the channels of your guild in their own server however you will still be notified about any activity , Allowing this will enter a entry in our database containing your guild id and if any one wants to copy your guild's channel , we will fetch the channels then and copy them however , we will not disclose the members of your server or your any of the messages''',color=discord.Color.red()))
      import assets.otp_assets
      success=await assets.otp_assets.send_waitfor_otp(ctx,self.client)
      if not success:
        return await ctx.send('Okay , no problem ')
      else:
        stats = await db.find_one({"n":"stemplates"})  
        if stats is None:
          new = {"n":"stemplates", "id": []}
          db.insert_one(new)      
          return await ctx.send('Initialized Database , Please try that command again ')        
        list=stats['id']
        list.append(ctx.guild.id)
        db.update_one({"n":'stemplates'},{"$set": {"id": list}})
        await ctx.send(embed=discord.Embed(title='Done',description="Added to database",color=discord.Color.dark_theme()))
        
    @commands.command(aliases=['rst','removeservertemplate'])
    @commands.has_permissions(administrator=True)
    async def Remtemplate(self, ctx):   
      await ctx.send(embed=discord.Embed(description='''Entrying the code will remove your server from our server and people will no longer be able to use your server template
            **To successfully remove your server , you might have to use this command twice **''',color=discord.Color.red()))
      import assets.otp_assets
      success=await reactor(ctx, self.client, 'Do you want to confirm this action', 0x34363A,ctx.author)
      if not success:
        return await ctx.send('Yey , no problem ')
      else:
        stats = await db.find_one({"n":"stemplates"})        
        list=stats['id']
        if ctx.guild.id in list:
          list.remove(ctx.guild.id)
          db.update_one({"n":'stemplates'},{"$set": {"id": list}})
          await ctx.send(embed=discord.Embed(title='Removed',description="Removed from database",color=discord.Color.red()))
        else:
          await ctx.send('You are not really in our database , you can do `[p]ast` to add your server')      

      
    @commands.command(aliases=['vt'])
    async def ViewTemplates(self, ctx):      
      stats = await db.find_one({"n":"stemplates"})
      if stats is None:
        new = {"n":"stemplates", "id": []}
        db.insert_one(new)      
        return await ctx.send('Initialized Database')
      list=stats['id']


      if list ==[]:    
        return await ctx.send(embed=discord.Embed(description='Oops ! No templates yet',color=discord.Color.dark_red()))
      else:
        for x in list:
          g=self.client.get_guild(x)
          e=discord.Embed(title=f"{g.name} - {g.id}",value=g.id,color=discord.Color.random())
          e.set_thumbnail(url=g.icon_url)
          e.add_field(name="Owner",value=g.owner)
          e.add_field(name="Total Chanels",value=len(g.channels))
          invites=await ctx.guild.invites() 
          e.add_field(name="Invite",value=invites[0])

          if len(g.channels)>20:
            e.add_field(name="<:Info:939018353396310036>",value="Showing top 20 channels(including categories)",inline=False)
            for x in g.channels:
              e.add_field(name=f"`{x.name}`",value=x.category,inline=False)
            
          else:
           for x in g.channels:
                e.add_field(name=f"`{x.name}`",value=x.category,inline=False)            
          await ctx.send(embed=e) 

    @commands.command(aliases=['importtemplate'])
    async def Import(self, ctx,g:int):      
      stats = await db.find_one({"n":"stemplates"}) 
      guild=self.client.get_guild(g)
      if guild.id in stats['id']:
        m=True
      else:
        m=False
      if m==False:
        return await ctx.send(embed=discord.Embed(description='Sorry , couldnt find that server in database and we are not hackers of discord '))
      else:
        await ctx.send(embed=discord.Embed(description=f'Guild: {guild.name}\nOwner: {guild.owner}\nIn Database: {m}\n\nProceeding..'))
        await ctx.send('Creating Roles')
        for role in guild.roles:
          name = role.name
          color = role.colour
          perms = role.permissions
          await ctx.guild.create_role(name=name, permissions=perms, colour=color)        
        await ctx.send('Adding channels and categories')
        for x in guild.channels:
          overwrites = x.overwrites  
          if str(x.type)=="text":
            category=x.category
            
            #if category.name not in ctx.guild.channels:
              #await ctx.guild.create_category(category.name)
            #category=self.client.get_channel(category.name)
            await ctx.guild.create_text_channel(x.name, overwrites=overwrites)#,category=category) 
            await ctx.send(f'Created Text channel- {x.name}')
          elif str(x.type)=="voice":
            await ctx.guild.create_voice_channel(x.name, overwrites=overwrites)
            
            
            await ctx.send(f'Created Voice Channel- {x.name}')
        await ctx.send('Done')
def setup(client):
    client.add_cog(ServerConnect(client))
