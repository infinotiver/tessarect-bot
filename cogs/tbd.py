import discord
import os
import sys
import requests
import asyncio
import json
import psutil
from discord.ext import tasks
import datetime
import logging
import copy
from functools import cached_property
from discord.ext import commands
from dislash import InteractionClient, ActionRow, Button, ButtonStyle
from discord.utils import get
class TBD(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.description="Commands for my Official support server Tessa Bot developers https://discord.gg/avpet3NjTE "
        self.dailyjoke.start()
        self.dailymeme.start()
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
          return await ctx.send('Heyo this command is only for my support server . Join it and use this command to add your bot  \n https://discord.gg/avpet3NjTE ')
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
                                description="Please provide its prefix and a brief description.",color=discord.Color.blurple()))

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
        d= discord.Embed(description=f" \n**Botname** > `{bot}`\n**Id ** > `{bot.id}` \n **Your reason +prefix** > `{reason}`",color=discord.Color.green(),timestamp=ctx.message.created_at)
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
        embedx.add_field(name='Prefix + Reason', value=reason,inline=False)
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

    
    @tasks.loop(hours = 24) 
    async def dailyjoke(self):
      try:
        c=self.bot.get_channel(967774377334702132)
        page = requests.get('https://joke.deno.dev/')
        jokesource = json.loads(page.content)
        joke = jokesource['setup']
        answer = jokesource['punchline']
        je=discord.Embed(title='Joke for today',color=discord.Color.gold(),description=f"**{joke}**\n{answer}")        .set_footer(text=f"Type: {jokesource['type']} joke")
        await c.send(embed=je)
      except Exception as e:
        print(e)
    @tasks.loop(hours = 10) 
    async def dailymeme(self):
      try:
        c=self.bot.get_channel(967774377334702132)
        page = requests.get(f'https://api.popcat.xyz/meme')
        d = json.loads(page.content)
        title=d['title']
        img=d['image']
        url=d['url']
        like = d['upvotes']
        comm=d['comments']
        embed = discord.Embed(title="10 Hourly Meme Time",description=title,url=url,color=0x34363A)
        embed.set_image(url=img)
        embed.set_footer(text=f"👍🏻{like} 💬 {comm} ")
        await c.send(embed=embed)
      except Exception as e:
        print(e)        
def setup(bot):
    bot.add_cog(TBD(bot))