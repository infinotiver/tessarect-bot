import json
import os

import discord
from discord.ext import commands



def prefix_check(guild):
    # Check if this is a dm instead of a server
    # Will give an error if this is not added (if guild is None)
    if guild == None:
        return "!"
    try:
        # Check if the guild id is in your 'prefixes.json'
        with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)
            p = prefixes[str(guild.id)]
    except:
        # Otherwise, default to a set prefix
        p = "a!"
    # If you're confident that the guild id will always be in your json,
    # feel free to remove this try-except block

    return p
prefix=""
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
                        value=f'`{prefix}setkickreason [reason]`\nExample: `{prefix}setkickreason Being a jerk :rofl:`\n'
                              f'__**What the kicked member would see**__:\n'
                              f'You have been kicked from **{ctx.guild.name}** for **Being a jerk :rofl:**.',
                        inline=False)

        embed.add_field(name='Set the mute role for this server',
                        value=f'`{prefix}setmuterole [role]`\nExample: `{prefix}setmuterole muted` '
                              f'(muted must be an actual role).\n'
                              f'You can create a mute role by `{prefix}createmuterole [role name]`',
                        inline=False)

        embed.add_field(name='Set the default Member role for this server',
                        value=f'`{prefix}setmemberrole [role]`\nExample: `{prefix}setmemberrole Member`'
                              f' (Member must be an actual role).\n'
                              f'If you want to turn off AutoRole, make a role, assign the member role to that role, and delete the role',
                        inline=False)




        embed.set_footer(text=f' Note there are other setups too for each cog you are requested to go through it while using them | Requested by {ctx.author.name}')
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




def setup(bot):
    bot.add_cog(Setup(bot))