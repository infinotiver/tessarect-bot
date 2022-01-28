import discord, datetime
from discord.ext import commands
from discord.ext import commands
# Import third-party libraries.


from flask import Flask, jsonify
from tinydb import TinyDB, Query
from async_timeout import timeout
from better_profanity import profanity
from decouple import config, UndefinedValueError
import random
# I
accent_color = {
    'primary': 0, 
    'error': 14573921
}
lock_roles = {
    'moderator':'Founder' ,
    'admin': 'CO- DEVELOPERS'
}


import discord
import datetime


class mongoIO():

	def __init__(self, bot):
		self.config = bot.config
		self.db=bot.motorClient[self.config.mongo['database']]
	async def muteUser(self, member: discord.Member, guild: discord.Guild, ends):
		await self.db.mutes.update_one(
			{"memberID": member.id, "guildID": guild.id},
			{
				"$set": {
					"memberID": member.id,
					"guildID": guild.id,
					"ends":  ends
				}
			}, upsert=True
		)

	async def unmuteUser(self, member: discord.Member, guild: discord.Guild):
		await self.db.mutes.delete_many({"memberID": member.id, "guildID": guild.id})

def generate_random_footer() -> str:
    footers_list = [
        'Hey there pal :D',
        'Invite me?',
        'Thank my developer'

    ]
    return random.choice(footers_list)
# Implementation of the guild database.
#db = TinyDB('guild-db.json')
Guild = Query()
# Global variables.
global jail_members
jail_members = []
global frozen_guilds
frozen_guilds = []
global snipeables
snipeables = []
def check_permissions(ctx, perms):
    if is_owner_check(ctx):
        return True

    ch = ctx.message.channel
    author = ctx.author
    resolved = ch.permissions_for(author)
    return all(getattr(resolved, name, None) == value for name, value in perms.items())

def is_gowner(**perms):
    def predicate(ctx):
        if ctx.guild is None:
            return False
        guild = ctx.guild
        owner = guild.owner

        if ctx.author.id == owner.id:
            return True

        return check_permissions(ctx,perms)
    return commands.check(predicate)

def can_mute(**perms):
    def predicate(ctx):
        if ctx.author.guild_permissions.mute_members:
            return True
        else:
            return False
    return commands.check(predicate)

def can_kick(**perms):
    def predicate(ctx):
        if ctx.author.guild_permissions.kick_members:
            return True
        else:
            return False
    return commands.check(predicate)

def can_ban(**perms):
    def predicate(ctx):
        if ctx.author.guild_permissions.ban_members:
            return True
        else:
            return False
    return commands.check(predicate)

def can_managemsg(**perms):
    def predicate(ctx):
        if ctx.author.guild_permissions.manage_messages:
            return True
        else:
            return False
    return commands.check(predicate)

def can_manageguild(**perms):
    def predicate(ctx):
        if ctx.author.guild_permissions.manage_guild:
            return True
        else:
            return False
    return commands.check(predicate)

def is_admin(**perms):
    def predicate(ctx):
        if ctx.author.guild_permissions.administrator:
            return True
        else:
            return False
    return commands.check(predicate)
from pytimeparse.timeparse import timeparse

class Admin(commands.Cog):
    """Commands for managing Discord servers."""
    def __init__(self,bot):
        self.bot = bot

    @can_kick()
    @commands.command()
    async def kick(self, ctx, user : discord.Member):
        """Kicks a user from the server."""
        if ctx.author == user:
            return await ctx.send("You cannot kick yourself.")
        await user.kick()
        embed = discord.Embed(title=f'User {user.name} has been kicked.', color=0x00ff00)
        embed.add_field(name="Goodbye!", value=":boot:")
        embed.set_thumbnail(url=user.avatar_url)
        await ctx.send(embed=embed)

    @can_ban()
    @commands.command()
    async def ban(self, ctx, user : discord.Member):
        """Bans a user from the server."""
        if ctx.author == user:
            return await ctx.send("You cannot ban yourself.")
        await user.ban()
        embed = discord.Embed(title=f'User {user.name} has been banned.', color=0x00ff00)
        embed.add_field(name="Goodbye!", value=":hammer:")
        embed.set_thumbnail(url=user.avatar_url)
        await ctx.send(embed=embed)

    @can_mute()
    @commands.command()
    async def mute(self, ctx, user : discord.Member, time: str):
        """Prevents a user from speaking for a specified amount of time."""
        if ctx.author == user:
            return await ctx.send("You cannot mute yourself.")
        if (rolem := discord.utils.get(ctx.guild.roles, name='Muted')) is None:
            return ctx.send("You have not set up the 'Muted' role!")
        if rolem in user.roles:
            return await ctx.send(f'User {user.mention} is already muted.')
        await user.add_roles(rolem)
        if time.isnumeric():
            time += "s"
        duration = datetime.timedelta(seconds=timeparse(time))
        ends = datetime.datetime.utcnow() + duration
        await self.bot.mongoIO.muteUser(user, ctx.guild, ends)
        embed = discord.Embed(title=f'User {user.name} has been successfully muted for {duration}', color=0x00ff00)
        embed.add_field(name="Shhh!", value=":zipper_mouth:")
        embed.set_thumbnail(url=user.avatar_url)
        await ctx.send(embed=embed)

    @can_mute()
    @commands.command()
    async def unmute(self, ctx, user: discord.Member):
        """Unmutes a user."""
        rolem = discord.utils.get(ctx.guild.roles, name='Muted')
        if rolem not in user.roles:
            return await ctx.send("User is not muted.")
        embed = discord.Embed(title=f'User {user.name} has been unmuted.', color=0x00ff00)
        embed.add_field(name="Welcome back!", value=":open_mouth:")
        embed.set_thumbnail(url=user.avatar_url)
        await ctx.send(embed=embed)
        await user.remove_roles(rolem)
        await self.bot.mongoIO.unmuteUser(user, ctx.guild)

    @commands.command(
        name='jail',
        help='Temporarily prevents a member from chatting in server.'
    )
    @commands.guild_only()
    @commands.has_permissions(manage_roles=True)
    async def jail(self, ctx: commands.Context, member: discord.Member, *, reason: str='No reason provided.'):
        do_jail = False

        if member == self.bot.user:
            await ctx.reply('Why are you even trying to jail me?')

        elif member == ctx.author:
            await ctx.reply('You can\'t jail yourself!')

        elif (
            member.guild_permissions.administrator
            and ctx.author.guild_permissions.administrator
            or not member.guild_permissions.administrator
        ):
            do_jail = True

        else:
            await ctx.reply('You can\'t jail an admin!')

        if do_jail:
            jail_members.append([member.id, ctx.guild.id, reason, ctx.author.id])
            await ctx.send(f'You\'ve been captured! {member.mention} | Reason: {reason}')
            await ctx.message.delete()

    @commands.command(
        name='jailed', 
        help='Views jailed members.'
    )
    @commands.guild_only()
    @commands.has_permissions(manage_roles=True)
    async def jailed(self, ctx: commands.Context):
        jail_has_member = False

        embed = (
            discord.Embed(
                title='Now viewing the prison!', 
                color=accent_color['primary']
            ).set_footer(
                icon_url=ctx.author.avatar, 
                text=generate_random_footer()
            )
        )

        for jail_member in jail_members:
            if jail_member[1] == ctx.guild.id:
                embed.add_field(
                    name=self.bot.get_user(jail_member[0]).name, 
                    value=('Jailed by ' + self.bot.get_user(jail_member[3]).mention + ' | Reason: `' + jail_member[2] + '`'), 
                    inline=False
                )
                jail_has_member = True

        if not jail_has_member:
            await ctx.reply('No members are inside the jail.')

        else:
            await ctx.reply(embed=embed)

    @commands.command(
        name='unjail', 
        help='Removes a member from jail.'
    )
    @commands.guild_only()
    @commands.has_permissions(manage_roles=True)
    async def unjail(self, ctx: commands.Context, member: discord.Member):
        for jail_member in jail_members:
            if jail_member[1] == ctx.guild.id and jail_member[0] == member.id:
                if member != ctx.author:
                    jail_members.remove(jail_member)
                    await ctx.message.add_reaction('☑️')

                else:
                    await ctx.reply('You can\'t free yourself!')

    @commands.command(
        name='block', 
        help='Blocks a user from chatting in a specific channel.'
    )
    @commands.guild_only()
    @commands.has_any_role(lock_roles['moderator'], lock_roles['admin'])
    async def block(self, ctx: commands.Context, member: discord.Member, *, reason: str='No reason provided.'):
        if member == self.bot.user:
            await ctx.reply('Why are you even trying to block me?')

        elif member != ctx.author:
            await ctx.channel.set_permissions(member, send_messages=False)
            await ctx.send(f'You\'re now blocked from chatting, {member.mention} | Reason: {reason}')
            await ctx.message.delete()

        else:
            await ctx.reply("You can't block yourself!")

    @commands.command(
        name='unblock', 
        help='Unblocks a user.'
    )
    @commands.guild_only()
    @commands.has_any_role(lock_roles['moderator'], lock_roles['admin'])
    async def unblock(self, ctx: commands.Context, member: discord.Member):
        await ctx.channel.set_permissions(member, overwrite=None)
        await ctx.message.add_reaction('☑️')

def setup(bot):
    bot.add_cog(Admin(bot))