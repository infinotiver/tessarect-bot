import discord
import os
import sys
import requests
import asyncio
import json
import aiohttp
import psutil
from discord.ext import tasks
import datetime
import logging
import copy
from functools import cached_property
from discord.ext import commands
from dislash import InteractionClient, ActionRow, Button, ButtonStyle
from discord.utils import get
from discord import Webhook, AsyncWebhookAdapter 

class Misc(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.description="Commands for my Official support server Tessa Bot Developers  https://discord.gg/avpet3NjTE"
        inter_client = InteractionClient(self.bot)
    class emoji:
        checkmark, cross, link = '<:sucess:935052640449077248>', '<:DiscordCross:940914829781270568>', '<:command:941986813013274625>'

    @property
    def pending_channel(self):
        return self.bot.get_channel(943726030911311922)

    @property
    def testing_guild(self):
        return self.bot.get_guild(942735208195711047)

    @property
    def testing_bot_role(self):
        return self.testing_guild.get_role(942735345206825002) if self.testing_guild else None
    
    @property
    def mainsrv(self):
        return self.bot.get_guild(912569937116147772)

    @property
    def user_bot_role(self):
        return self.mainsrv.get_role(920177952136757309) if self.mainsrv else None


    @commands.Cog.listener()
    async def on_member_join(self, member):
        if member.guild == self.testing_guild and member.bot:
            await member.add_roles(self.testing_bot_role)

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if payload.member.bot:
            return
        if payload.channel_id == self.pending_channel.id:
            message = await self.pending_channel.fetch_message(payload.message_id)
            if message.author != message.guild.me:
                return
            
            if str(payload.emoji) in (self.emoji.checkmark, self.emoji.cross, self.emoji.link):
                await message.remove_reaction(payload.emoji, payload.member)
                data = json.loads(message.content)
                if data['status'] == 0:
                    if not payload.member.guild_permissions.manage_roles:
                        return
                    bot = self.testing_guild.get_member(data['bot'])
                    #if not bot:
                        #return await payload.channel.send("You didn't invite the bot")
                    if str(payload.emoji) == self.emoji.checkmark:
                        embed = message.embeds[0]
                        data['staff'] = payload.member.id
                        embed.set_footer(text=f'Approved by {payload.member}')
                        data['status'] = 1
                        embed.set_field_at(0, name='Status', value='Pending admin approval and invite to server')
                        embed.add_field(name='Approved by',
                                        value=payload.member.mention + ' (' + str(payload.member.id) + ')',inline=False)
                        embed.description = 'React to get an invite link'
                        embed.color = discord.Color.blue()
                        embed.set_thumbnail(url=embed.author.avatar_url)
                        embed.set_author(name=embed.author.name, icon_url=embed.author.icon_url)
                        embed.timestamp = datetime.datetime.now(datetime.timezone.utc)
                        await message.edit(content=json.dumps(data), embed=embed)
                        await message.clear_reaction(self.emoji.checkmark)
                        await message.clear_reaction(self.emoji.cross)
                        await message.add_reaction(self.emoji.link)
                    elif str(payload.emoji) == self.emoji.cross:
              
                        embed = message.embeds[0]
                        data['staff'] = payload.member.id
                        embed.set_footer(text=f'Declined by {payload.member}')
                        data['status'] = -1
                        embed.set_field_at(0, name='Status', value='Declined',inline=False)
                        embed.add_field(name='Declined by',
                                        value=payload.member.mention + ' (' + str(payload.member.id) + ')',inline=False)
                        embed.description = 'Declined'
                        embed.color = discord.Color.red()
                        embed.set_author(name=embed.author.name, icon_url=embed.author.icon_url)
                        embed.timestamp = datetime.datetime.now(datetime.timezone.utc)
                        await message.edit(content=json.dumps(data), embed=embed,components=[])
                        print(data['user'])
                        print(type(data['user']))
                        user=self.bot.get_user(data['user'])
                        await user.send(embed=embed)
                        await message.clear_reaction(self.emoji.checkmark)
                        await message.clear_reaction(self.emoji.cross)
                elif data['status'] == 1:
                    if not payload.member.guild_permissions.manage_guild:
                        return
                    if str(payload.emoji) == self.emoji.link:
                        invite = discord.utils.oauth_url(data['bot'], guild=payload.member.guild)
                        embed = message.embeds[0]
                        temp_embed = copy.deepcopy(embed)
                        embed.set_author(name=embed.author.name, icon_url=embed.author.icon_url, url=invite)
                        embed.description = ('**IMPORTANT:** Please add the bot within 5 minutes, or else the bot will '
                                             'have elevated permissions.')
                        embed.set_field_at(0, name='Status', value='Admin adding bot...')
                        data['status'] = 2
                        await message.edit(content=json.dumps(data), embed=embed)
                        print(data['user'])
                        print(type(data['user']))
                        user=self.bot.get_user(data['user'])
                        await user.send(embed=embed)                        
                        await message.clear_reaction(self.emoji.link)
                        
                        def check(m):
                            return m.bot and m.id == data['bot']

                        try:
                            bot_joined = await self.bot.wait_for('member_join', check=check, timeout=300)
                        except asyncio.TimeoutError:
                            data['status'] = 1
                            await message.edit(content=json.dumps(data), embed=temp_embed)
                            await message.add_reaction(self.emoji.link)
                            return
                        await bot_joined.add_roles(self.user_bot_role)
                        data['admin'] = payload.member.id
                        embed.set_footer(text=f'Added by {payload.member}')
                        data['status'] = 3
                        embed.set_field_at(0, name='Status', value='Added',inline=False)
                        embed.add_field(name='Added by',
                                        value=payload.member.mention + ' (' + str(payload.member) + ')',inline=False)
                        embed.description = 'Added'
                        embed.color = discord.Color.green()
                        embed.set_author(name=embed.author.name, icon_url=embed.author.icon_url)
                        embed.timestamp = datetime.datetime.now(datetime.timezone.utc)
                        await message.edit(content=json.dumps(data), embed=embed)
                        await message.clear_reaction(self.emoji.checkmark)
                        await message.clear_reaction(self.emoji.cross)

    @commands.command(name='addbot',help="You can add your bot in TBD , use this command . Not in our server ? join now https://discord.gg/avpet3NjTE")
    #@commands.has_any_role(729927579645247562, 737517726737629214)
    @commands.cooldown(1, 10, commands.BucketType.user)
    @commands.max_concurrency(1, commands.BucketType.user)
    async def _addbot(self, ctx, bot: discord.User = None, *, reason: str = None):
        
        if ctx.guild.id !=912569937116147772:
          return await ctx.send(embed=discord.Embed(title="Not my house",description='Heyo this command is only for my support server . Join it and use this command to add your bot  \n https://discord.gg/avpet3NjTE ',color = ctx.author.color))
        if ctx.channel.id !=955745362306543616:
          return await ctx.send('This command works only in <#955745362306543616>')
        if not bot:
            await ctx.send(
                embed=discord.Embed(title="Add Bot", description="What is the user ID of your bot? (Right click->Copy ID)",color=discord.Color.blurple()))

            def check(m):
                return m.channel == ctx.channel and m.author == ctx.author and m.content.isdigit()

            try:
                bot = await commands.UserConverter().convert(ctx, (
                    await self.bot.wait_for('message', check=check, timeout=30)).content)
              
            except asyncio.TimeoutError:
                ctx.command.reset_cooldown(ctx)
                return await ctx.send('Timed out!')
            except commands.BadArgument:
                ctx.command.reset_cooldown(ctx)
                return await ctx.send('Invalid user!')
   
        if not bot.bot:
            return await ctx.send("That isn't a bot...")
        if bot in ctx.guild.members:
            return await ctx.send('Bot is already in server')
        if not reason:
            await ctx.send(
                embed=discord.Embed(title="Add Bot",
                                description="Please provide its prefix ",color=discord.Color.blurple()))

            def check(m):
                return m.channel == ctx.channel and m.author == ctx.author

            try:
                reason = (await self.bot.wait_for('message', check=check, timeout=30)).clean_content
                
                
            except asyncio.TimeoutError:
                ctx.command.reset_cooldown(ctx)
                return await ctx.send('Timed out!')
        bott=self.bot.get_user(int(bot.id))
        await ctx.message.delete()
        await ctx.channel.purge(limit=None, check=lambda msg: not msg.pinned)
        d= discord.Embed(description=f" \n**Botname** <:rightarrow:941994550124245013> `{bot}`\n**Id ** <:rightarrow:941994550124245013> `{bot.id}` \n **Prefix** <:rightarrow:941994550124245013> `{reason}`",color=discord.Color.green(),timestamp=ctx.message.created_at)
        #d.add_field(name="_ _ ",value="<:Info:939018353396310036> Kindly wait for a bot reviewer to review your bot  and dont send same bot entry again and again | Also you should be the owner of the bot | Keep your dms open")
        try:
            d.set_thumbnail(url=bott.avatar_url)
        except:
            return await ctx.send(embed=discord.Embed(title=ctx.author,description='Oh ho , seems like I never met this bot before , kindly add me in a common server with your bot and then apply again :wink:',color=discord.Color.dark_theme()))
        await ctx.channel.purge(limit=None, check=lambda msg: not msg.pinned)
        await ctx.send(embed=d) 
        data = {
            'user': ctx.author.id,
            'bot': bot.id,
            'reason': reason,
            'status': 0
            }
        invite = discord.utils.oauth_url(bot.id, guild=self.testing_guild)
        embedx = discord.Embed(title='User-Made Bot', description='Click bot name to invite. React here to confirm or deny the bot.',color=discord.Color.gold())
        embedx.add_field(name='Status', value='Pending approval',inline=False)
        embedx.add_field(name='Submitted By', value=ctx.author.mention + ' (' + str(ctx.author.id) + ')',inline=False)
        embedx.add_field(name='Prefix', value=reason,inline=False)
        embedx.add_field(name='Bot Account', value=bot.mention,inline=False)
        embedx.add_field(name='Bot Id', value=bot.id,inline=False)
        #bott=self.bot.get_user(int(bot.id))
        embedx.set_author(name=str(bot), icon_url=bott.avatar_url,url=invite)
 
        row = ActionRow(
      
            Button(
                style=ButtonStyle.link,
                label="Invite!",
                url=invite,
                emoji="<:rightarrow:941994550124245013>"
            ),
            Button(
                style=ButtonStyle.grey,
                label="Claim!",
                custom_id="cl",
                emoji="✋"
            )        
        )   
        row2 = ActionRow(
      
            Button(
                style=ButtonStyle.link,
                label="Invite!",
                url=invite,
                emoji="<:rightarrow:941994550124245013>"
            ),
            Button(
                style=ButtonStyle.grey,
                label="Claim!",
                custom_id="cl",
                emoji="✋",
                disabled = True
            )        
        )      

        msg = await self.pending_channel.send(json.dumps(data), embed=embedx, components=[row])
        
        embedx.set_thumbnail(url=bott.avatar_url)
        await msg.add_reaction(self.emoji.checkmark)
        await msg.add_reaction(self.emoji.cross)


        on_click = msg.create_click_listener(timeout=10)
        @on_click.matching_id("cl")
        async def on_test_button(inter):
          embedx.set_field_at(0, name='Status', value=f"This bot is claimed by {inter.author.mention},kindly let them review the bot")
          await msg.edit(embed=embedx,components=[row2])
    @commands.command(name='hire',help="For admins only")
    @commands.has_any_role(912569937153892361, 912569937116147778) 
    async def hire(self,ctx,member:discord.Member,role,*,reason):
      allowed=['br','mod']
      check=self.bot.get_channel(945682930846560326)
      tasks=self.bot.get_channel(945682067667181648)
      guide=self.bot.get_channel(945683048605814804)
      mod=ctx.guild.get_role(945679632424923189)
      if role not in allowed:
        return await ctx.send('Sire, that role isnt valid the valid roles are `br` and ``mod`')
      if role =='br':
        getrole="Trial Bot Reviewer"
      else:
        getrole="Trial Moderator"
      if role=="mod":
        e=discord.Embed(title=f"New hired staff",description=f"Hi, {member} your application for Moderator has been Accepted. *P.S: You are selected by CL/PL to be a Trial Moderator for a valid reasons. But they would like to see your skills.* New Hired {role}| Reason {reason} , Check out {tasks.mention} and {guide.mention}",color=discord.Color.green())
        e.set_author(name="Tessa Bot Developer Staff team",icon_url=ctx.guild.icon_url)
        e.set_footer(text="Please take a note, if you leak the staff information will get you fired.")
        e2=discord.Embed(title="New Hired Staff!",description=f":white_medium_square: Member {member.mention}\n:white_medium_square:Position {getrole}\n :white_medium_square: Role given {mod}",color=discord.Color.blue())
        e2.add_field(name="Who hired",value=ctx.author.mention)
        await member.add_roles(mod)
        await check.send(content=member.mention,embed=e2)
        await member.send(embed=e)
    @commands.command(name='tbd',help="Know about tbd")
    async def tessabotdevelopers(self,ctx):
      d="""**Tessɑ Bσt Deνelσpeɾs ( TBD)**

𝕱𝖔𝖚𝖓𝖉𝖊𝖉 𝖇𝖞 𝕾𝖓𝖎𝖕𝖊𝖗𝖃𝖎𝟏𝟗𝟗 

𝐴𝑏𝑜𝑢𝑡 𝑢𝑠 : 𝑊𝑒 𝑎𝑟𝑒 𝑎 𝑔𝑟𝑒𝑎𝑡 𝑛𝑒𝑡𝑤𝑜𝑟𝑘 .𝑇𝑒𝑠𝑠𝑎 𝐵𝑜𝑡 𝐷𝑒𝑣𝑒𝑙𝑜𝑝𝑒𝑟𝑠 . 𝑇𝐵𝐷 𝐼𝑆  𝑎 𝑐𝑜𝑚𝑚𝑢𝑛𝑖𝑡𝑦 𝑐𝑢𝑚 𝑏𝑜𝑡 𝑠𝑒𝑟𝑣𝑒𝑟 𝑎𝑛𝑑 𝑎𝑙𝑠𝑜 𝑠𝑢𝑝𝑝𝑜𝑟𝑡 𝑠𝑒𝑟𝑣𝑒𝑟 𝑓𝑜𝑟 𝑜𝑢𝑟 𝑏𝑜𝑡 𝑇𝑒𝑠𝑠𝑎𝑟𝑒𝑐𝑡 . 𝐶𝘩𝑎𝑡 𝘩𝑒𝑟𝑒 𝑤𝑖𝑡𝘩 𝑜𝑡𝘩𝑒𝑟 𝑚𝑒𝑚𝑏𝑒𝑟𝑠 , 𝑎𝑝𝑝𝑙𝑦 𝑓𝑜𝑟 𝑦𝑜𝑢𝑟 𝑏𝑜𝑡 𝑡𝑜 𝑏𝑒 𝘩𝑒𝑟𝑒 𝑎𝑛𝑑 𝑔𝑒𝑡 𝑒𝑎𝑟𝑙𝑦 𝑎𝑐𝑐𝑒𝑠𝑠 𝑡𝑜 𝑎𝑙𝑙 𝑜𝑢𝑟 𝑏𝑜𝑡𝑠 𝑎𝑛𝑑 𝑚𝑢𝑐𝘩 𝑚𝑜𝑟𝑒 . 𝑂𝑓𝑓𝑖𝑐𝑖𝑎𝑙 𝑠𝑢𝑝𝑝𝑜𝑟𝑡 𝑠𝑒𝑟𝑣𝑒𝑟 𝑓𝑜𝑟 𝑜𝑢𝑟 𝑏𝑜𝑡 𝑇𝑒𝑠𝑠𝑎𝑟𝑒𝑐𝑡(𝑐𝑢𝑟𝑟𝑒𝑛𝑡𝑙𝑦 𝑖𝑛 𝟹𝟶+ 𝑠𝑒𝑟𝑣𝑒𝑟𝑠) 𝑑𝑠𝑐.𝑔𝑔/𝑡𝑒𝑠𝑠𝑎𝑟𝑒𝑐𝑡. 𝐺𝑟𝑜𝑤 𝑦𝑜𝑢𝑟 𝑏𝑜𝑡 𝑎𝑛𝑑 𝑠𝑒𝑟𝑣𝑒𝑟 

───── ❝ **Why choose us** ❞ ─────

»»— Talkative and smart community
»»— Better Guidance
»»— Handpicked bots made by users 
»»— Top used bots for extra fun
»»— Get updates on our bots
»»— Apply  your bot and make it grow
»»— Get tips from our expert
»»— Have fun
»»— Much More
≿━━━━༺❀༻━━━━≾
8 + Popular Bots
38+ Members
30+ Channels
and much more
⊱ ────── {.⋅ ✯ ⋅.} ────── ⊰
Join Ʈᥱ⳽⳽ᥲ ᙖot ᙃᥱʋᥱꙆoρᥱɾ⳽ Now :
https://discord.gg/avpet3NjTE"""
      em=discord.Embed(title="Tessa Bot Developers",description=d,color=ctx.author.color)
      await ctx.send(embed=em)
    @commands.command(name='createficter')
    async def cf(self,ctx,avatar:str,spl:str,*,user:str):  
      
      with open("storage/tubble.json", "r") as modlogsFile:
          jsonfile = json.load(modlogsFile)   
        
      if spl in jsonfile:
        return await ctx.send('Sorry but you cant use that spl text it is taken already')
      if avatar=="None":
        avatar=None
      jsonfile[spl]={'name':user,'avatar':avatar,'invoke':spl,'owner':ctx.author.id}
      with open("storage/tubble.json", "w") as File:
          json.dump(jsonfile,File)      
      e=discord.Embed(title="Created a ficter",description=f"User- {user}\n Invoking Special Code - {spl}\n To use this fictere send `[p]sendfictermsg {spl} [your text you want to send]`",color=discord.Color.magenta())
      await ctx.send(embed=e)
    @commands.command(name='editficter')
    async def ctb(self,ctx,spl:str,avatar:str,*,user:str):  
      
      with open("storage/tubble.json", "r") as modlogsFile:
          jsonfile = json.load(modlogsFile)   
        

      if avatar=="None":
        avatar=None
      jsonfile[spl]={'name':user,'avatar':avatar,'invoke':spl,'owner':ctx.author.id}
      with open("storage/tubble.json", "w") as File:
          json.dump(jsonfile,File)      
      e=discord.Embed(title="Edited a ficter",description=f"User- {user}\n Invoking Special Code - {spl}\n To use this fictere send `[p]sendfictermsg {spl} [your text you want to send]`",color=discord.Color.magenta())
      await ctx.send(embed=e)      
    @commands.command(name='removeficter')
    async def rtb(self,ctx,spl:str):  
      
      with open("storage/tubble.json", "r") as modlogsFile:
          jsonfile = json.load(modlogsFile)   
      if spl in jsonfile:
        jsonfile.pop(spl)
      with open("storage/tubble.json", "w") as File:
          json.dump(jsonfile,File)    
      e=discord.Embed(title="Removed a ficter",description=f"Removed successfully",color=discord.Color.magenta())
      await ctx.send(embed=e)
    @commands.command(name='listficter')
    async def ltf(self,ctx):  
      
      with open("storage/tubble.json", "r") as modlogsFile:
          jsonfile = json.load(modlogsFile)   
      ed=discord.Embed(title="My Ficters",color=discord.Color.magenta())
      for x in jsonfile:
        if jsonfile[x]['owner']==ctx.author.id:
          ed.add_field(name=jsonfile[x]['name'],value=f"Invoke-{jsonfile[x]['invoke']}\n Avatar Url-{jsonfile[x]['avatar']}",inline=False)
      await ctx.send(embed=ed)
    @commands.command(name='sendfictermsg',aliases=['fictersend','fm','sfm','swm'])
    async def sendwebhookmsg(self,ctx,spl:str,*,text):  
      with open("storage/tubble.json", "r") as jsfile:
          jsonfile = json.load(jsfile)    
      #tubble=jsonfile[spl]
      if spl not in jsonfile:
        return await ctx.send('No Ficter found with that code ')
      else:
        tubble=jsonfile[spl]
      user=tubble['name']
      avatar=tubble['avatar']
      owner=tubble['owner']

      if ctx.author.id != owner:
        return await ctx.send('You are not the author of this Ficter')

      
      #if not 'https'or'http' in avatar:
        #return await ctx.send('Invalid url for avatar')
      web=await ctx.channel.create_webhook(name=f"Ficter {spl}")
     
      async with aiohttp.ClientSession() as session:  
        webhook = Webhook.from_url(web.url, adapter=AsyncWebhookAdapter(session)) # Initializing webhook with AsyncWebhookAdapter
        await webhook.send(username=user, avatar_url=avatar,content=text) 
        await web.delete()# Executing webhook.
        await ctx.message.delete()
def setup(bot):
    bot.add_cog(Misc(bot))