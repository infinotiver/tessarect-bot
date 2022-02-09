import json
import os

import discord
from discord.ext import commands
import motor.motor_asyncio
import nest_asyncio

from pymongo import MongoClient

nest_asyncio.apply()
mongo_url =  os.environ['enalevel']

cluster = motor.motor_asyncio.AsyncIOMotorClient(mongo_url)

ledb = cluster["discord"]["enalevel"]



class Setup(commands.Cog, description='Used to set up the bot for mute/unmute etc.'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='setup', description='Used to set the bot up, for welcome messages, mute roles, etc.\n'
                                                'Recommended to set the bot up as early as possible when it joins a '
                                                'server.')
    @commands.guild_only()
    async def setup_welcome(self, ctx):
        embed = discord.Embed(title='Setup Tessarect.',
                              timestamp=ctx.message.created_at,
                              color=discord.Color.random())



        embed.add_field(name='Set default reason when kicking/banning members',
                        value=f'`[p]setkickreason [reason]`\nExample: `[p]setkickreason Being a jerk :rofl:`\n'
                              f'__**What the kicked member would see**__:\n'
                              f'You have been kicked from **{ctx.guild.name}** for **Being a jerk :rofl:**.',
                        inline=False)

        embed.add_field(name='Set the mute role for this server',
                        value=f'`[p]setmuterole [role]`\nExample: `[p]setmuterole muted` '
                              f'(muted must be an actual role).\n'
                              f'You can create a mute role by `[p]createmuterole [role name]`',
                        inline=False)

        embed.add_field(name='Set the default Member role for this server',
                        value=f'`[p]setmemberrole [role]`\nExample: `[p]setmemberrole Member`'
                              f' (Member must be an actual role).\n'
                              f'If you want to turn off AutoRole, make a role, assign the member role to that role, and delete the role',
                        inline=False)
        embed.add_field(name="Switch Levelling System for this server",value=f"Tessarect offers a very advanced and good levelling system , if you want to switch it (disabled by default) you can do \n `[p]levelconfig [enable/disable]`. \n Get more info on its commands by using `[p]help Level`")
        embed.set_footer(text=f' Note there are other setups too for each cog you are requested to go through it while using them | Requested by {ctx.author.name}')
        embed.set_thumbnail(url=self.bot.user.avatar_url)
        await ctx.send(embed=embed)



    @commands.command(name='setkickreason', description='Used to set the default kick/ban reason '
                                                        'in a case where no reason is given.\n'
                                                        'Check the description of the `setup` command '
                                                        'for more information.')
    @commands.has_permissions(manage_guild=True)
    @commands.guild_only()
    async def set_kick_reason(self, ctx, *, reason):
        if os.path.exists(f'./configs/{ctx.guild.id}.json'):
            with open(f'./configs/{ctx.guild.id}.json', 'r') as jsonFile:
                data = json.load(jsonFile)
        else:
            data = {}

        data['default_kick_ban_reason'] = str(reason)

        with open(f'./configs/{ctx.guild.id}.json', 'w') as jsonFile:
            json.dump(data, jsonFile, indent=4)

        await ctx.send(f'Default kick/ban reason set to **{reason}** successfully.')

    @commands.command(name='setmemberrole', description='Used to set the role which is given to every member upon '
                                                        'joining. '
                                                        'Check description of `setup` command for more info.')
    @commands.has_permissions(manage_guild=True)
    @commands.guild_only()
    async def set_member_role(self, ctx, role: discord.Role):
        if os.path.exists(f'./configs/{ctx.guild.id}.json'):
            with open(f'./configs/{ctx.guild.id}.json', 'r') as jsonFile:
                data = json.load(jsonFile)
        else:
            data = {}

        data['member_role'] = role.id

        with open(f'./configs/{ctx.guild.id}.json', 'w') as jsonFile:
            json.dump(data, jsonFile, indent=3)

        await ctx.send(f'Member role set to **{role.name}** successfully.')

    @commands.command(name='setmuterole', description='Sets the role assigned to muted people. '
                                                      'Use `createmuterole` for creating a muted role and '
                                                      'automatically setting permissions to every channel.')
    @commands.has_permissions(manage_guild=True)
    @commands.guild_only()
    async def set_mute_role(self, ctx, role: discord.Role):
        if os.path.exists(f'./configs/{ctx.guild.id}.json'):
            with open(f'./configs/{ctx.guild.id}.json', 'r') as jsonFile:
                data = json.load(jsonFile)
        else:
            data = {}
        data['mute_role'] = role.id

        with open(f'./configs/{ctx.guild.id}.json', 'w') as jsonFile:
            json.dump(data, jsonFile, indent=4)

        await ctx.send(f'Mute role set to **{role.name}** successfully.')

    @commands.command(name='createmuterole', description='Creates a mute role, and sets messaging permissions to '
                                                         'every channel.\n '
                                                         'the `rolename` argument is optional. (Defaults to "Muted")')
    @commands.has_permissions(manage_roles=True)
    @commands.guild_only()
    async def create_mute_role(self, ctx, rolename=None):
        if rolename is None:
            rolename = 'Muted'
        guild = ctx.guild
        mutedRole = await guild.create_role(name=rolename)  # creating the role
        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_messages=False, use_slash_commands=False)
            # setting permissions for each channel
        await ctx.send(f'Created role **{mutedRole}** and set permissions accordingly.')
        await Setup.set_mute_role(self, ctx, mutedRole)




    @commands.command(aliases=["levelling"], description="Enable or disable levelling")
    @commands.has_permissions(administrator=True)
    async def levelconfig(self, ctx, choice):
        lst = ["enable", "disable"]
        stats = await ledb.find_one({"id": ctx.guild.id})
        if choice in lst:
            if choice == "enable" :
                choice = 0
                stats = await ledb.find_one({"id": ctx.guild.id})
                if stats is None:
                    newuser = {"id": ctx.guild.id, "type": choice}
                    await ledb.insert_one(newuser)
                    await ctx.send("**Changes are saved**")

                elif stats["type"] == 0:
                    await ctx.send("**Command is already enabled**")

                else:
                    await ledb.update_one(
                        {"id": ctx.guild.id}, {"$set": {"type": choice}}
                    )

                    await ctx.send("**Changes are saved | Command enabled**")
            else:
                choice = 1

                stats = await ledb.find_one({"id": ctx.guild.id})
                if stats is None:
                    newuser = {"id": ctx.guild.id, "type": choice}
                    await ledb.insert_one(newuser)
                    await ctx.send("**Changes are saved**")

                elif stats["type"] == 1:
                    await ctx.send("**Command is already disabled**")

                else:
                    await ledb.update_one(
                        {"id": ctx.guild.id}, {"$set": {"type": choice}}
                    )

                    await ctx.send("**Changes are saved | Command disabled**")

        else:
            await ctx.send("**It can be enable/disable only**")


def setup(bot):
    bot.add_cog(Setup(bot))