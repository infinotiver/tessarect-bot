import discord
import os
import sys
import asyncio
import json
import psutil
import datetime
import logging
import copy
from functools import cached_property
from discord.ext import commands


class AddBot(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    class emoji:
        checkmark, cross, link = '\U00002705', '\U0000274c', '\U0001f517'

    @property
    def pending_channel(self):
        return self.bot.get_channel(942735432796471326)

    @property
    def testing_guild(self):
        return self.bot.get_guild(942735208195711047)

    @property
    def testing_bot_role(self):
        return self.testing_guild.get_role(942735345206825002) if self.testing_guild else None
    
    @property
    def tca(self):
        return self.bot.get_guild(912569937116147772)

    @property
    def user_bot_role(self):
        return self.tca.get_role(920177952136757309) if self.tca else None
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.id == 929333807893598238:
            try:
                msg = await self.pending_channel.fetch_message(message.content.split()[0])
                reason = ' '.join(message.clean_content.split()[1:])
                data = json.loads(msg.content)
                user = message.guild.get_member(data['user'])
                bot = await self.bot.fetch_user(data['bot'])
                await user.send(f'Your bot, {bot}, has been rejected from joining {message.guild.name}. \n**Reason:** '
                                f'{reason}')
                await message.add_reaction(self.emoji.checkmark)
            except:
                await message.add_reaction(self.emoji.cross)
                raise

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
                    if not bot:
                        return await payload.member.send("You didn't invite the bot")
                    if str(payload.emoji) == self.emoji.checkmark:
                        embed = message.embeds[0]
                        data['staff'] = payload.member.id
                        embed.set_footer(text=f'Approved by {payload.member}')
                        data['status'] = 1
                        embed.set_field_at(0, name='Status', value='Pending admin approval')
                        embed.add_field(name='Approved by',
                                        value=payload.member.mention + ' (' + str(payload.member) + ')')
                        embed.description = 'React to get an invite link'
                        embed.color = discord.Color.blue()
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
                        embed.set_field_at(0, name='Status', value='Declined')
                        embed.add_field(name='Declined by',
                                        value=payload.member.mention + ' (' + str(payload.member) + ')')
                        embed.description = 'Declined'
                        embed.color = discord.Color.red()
                        embed.set_author(name=embed.author.name, icon_url=embed.author.icon_url)
                        embed.timestamp = datetime.datetime.now(datetime.timezone.utc)
                        await message.edit(content=json.dumps(data), embed=embed)
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
                        embed.set_field_at(0, name='Status', value='Added')
                        embed.add_field(name='Added by',
                                        value=payload.member.mention + ' (' + str(payload.member) + ')')
                        embed.description = 'Added'
                        embed.color = discord.Color.green()
                        embed.set_author(name=embed.author.name, icon_url=embed.author.icon_url)
                        embed.timestamp = datetime.datetime.now(datetime.timezone.utc)
                        await message.edit(content=json.dumps(data), embed=embed)
                        await message.clear_reaction(self.emoji.checkmark)
                        await message.clear_reaction(self.emoji.cross)

    @commands.command(name='addbot')
    #@commands.has_any_role(729927579645247562, 737517726737629214)
    @commands.cooldown(1, 86400, commands.BucketType.user)
    @commands.max_concurrency(1, commands.BucketType.user)
    async def _addbot(self, ctx, bot: discord.User = None, *, reason: str = None):
        if ctx.guild.id !=912569937116147772:
          return await ctx.send('Heyo this command is only for my support server . Join it and use this command to add your bot ')
        if not bot:
            await ctx.send(
                embed=discord.Embed(title="Add Bot", description="What is the user ID of your bot? (Right click->Copy ID)"))

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
                                description="Please provide a reason for why we should accept your bot."))

            def check(m):
                return m.channel == ctx.channel and m.author == ctx.author

            try:
                reason = (await self.bot.wait_for('message', check=check, timeout=30)).clean_content
            except asyncio.TimeoutError:
                ctx.command.reset_cooldown(ctx)
                return await ctx.send('Timed out!')

        if not 50 <= len(reason) <= 1000:
            ctx.command.reset_cooldown(ctx)
            return await ctx.send('Reason must be 50 to 1000 characters long.')

        await ctx.send('Please make sure your DMs are open so I can keep you updated on the status')
        data = {
            'user': ctx.author.id,
            'bot': bot.id,
            'reason': reason,
            'status': 0
            }
        invite = discord.utils.oauth_url(bot.id, guild=self.testing_guild)
        embedx = discord.Embed(title='User-Made Bot', description='Click bot name to invite. React here to confirm or deny '
                                                             'the bot.')
        embedx.add_field(name='Status', value='Pending approval')
        embedx.add_field(name='Submitted By', value=ctx.author.mention + ' (' + str(ctx.author) + ')')
        embedx.add_field(name='Reason', value=reason)
        embedx.add_field(name='Bot Account', value=bot.mention)
        embedx.set_author(name=str(bot), url=invite)
        msg = await self.pending_channel.send(json.dumps(data), embed=embedx)
        await msg.add_reaction(self.emoji.checkmark)
        await msg.add_reaction(self.emoji.cross)


def setup(bot):
    bot.add_cog(AddBot(bot))