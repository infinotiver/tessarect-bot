
import asyncio
import json
import os
import re
import datetime
import discord
from discord.ext import commands
from discord.utils import get

from assets import time_calc, misc_checks, otp_assets,button_check


class Moderation(commands.Cog, description="Moderation commands.A number of commands to moderate your server"):
    def __init__(self, bot):
        self.bot = bot
    '''
    @commands.command(name='timeout', description='Timeouts the person mentioned. Time period is required and should be in munutes| NEW |')
    @commands.has_permissions(manage_roles=True)
    async def timeout_func(self, ctx, user: discord.Member, time_period:int,*,reason:str=None):
      time_period=int(time_period)
      await user.edit(timeout = datetime.timedelta(minutes = time_period))
      muteem=discord.Embed(description=f"<:command:941986813013274625> Action: Timeout\n<:user:941986233574367253> Moderator:  {ctx.author.mention}\n<:target:941990853625389126> Target: {user.mention}\n<:timer:941993935507689492> Time:  {time_period} minute",color=0x99aab5)
      muteem.add_field(name="<:rightarrow:941994550124245013> Reason", value=reason, inline=False)
      await ctx.send(embed=muteem)
      '''



    @commands.command(name="clear",aliases=['purge'],pass_context=True)
    @commands.has_permissions(manage_channels=True)
    async def clear(self,ctx, limit: int):
            messages = await ctx.channel.history(limit=limit).flatten()
            await ctx.channel.purge(limit=limit)
            em=discord.Embed(description=f"<:Channel:946288872583725076> Channel:  {ctx.channel.mention}\n<:command:941986813013274625> Action: Clear\n<:chat:979769986484678656> Request:  {limit}\n<:Hacker:922468796852224061> Fetched: {str(len(messages))}\n<:user:941986233574367253> Moderator:  {ctx.author.mention}",color=0x99aab5)
            await ctx.send(embed=em)

    @commands.command(name='mute', description='Mutes the person mentioned. Time period is optional.')
    @commands.has_permissions(manage_roles=True)
    @commands.guild_only()
    async def mute_func(self, ctx, user: discord.Member, time_period=None,*,reason:str=None):
        if time_period is not None:
            pattern = r"^[\d]+[s|m|h|d]{1}$"
            if not re.match(pattern, time_period):
                return await ctx.send("Time period is of the wrong format.\n"
                                      "Example usage: `5s`, `10m`, `15h`, `2d`")

        if misc_checks.is_author(ctx, user):
            return await ctx.send('You cannot mute yourself.  lol')

        if misc_checks.is_client(self.bot, user):
            return await ctx.send('I can\'t mute myself, sorry but not sorry.')

        if os.path.exists(f'./configs/{ctx.guild.id}.json'):
            with open(f'./configs/{ctx.guild.id}.json', 'r') as jsonFile:
                data = json.load(jsonFile)
        else:
            data = {}
        mute_role_id = data.get('mute_role')

        if mute_role_id is None:
            return await ctx.send('It seems you have not set the mute role. '
                                  'Please ask a person with the `Manage Server` permission '
                                  'to set a role as the mute role, '
                                  'or make one by using the `setmuterole` or `createmuterole` commands.')

        # get the actual mute role from the role's ID
        mute_role = get(ctx.guild.roles, id=int(mute_role_id))
        await user.add_roles(mute_role)  # add the mute role

        if time_period is not None:
            final_time_text = time_calc.time_suffix(time_period)
            muteem=discord.Embed(description=f"<:command:941986813013274625> Action: Mute\n<:user:941986233574367253> Moderator:  {ctx.author.mention}\n<:target:941990853625389126> Target: {user.mention}\n<:timer:941993935507689492> Time:  {time_period}",color=0x99aab5)
            muteem.add_field(name="<:rightarrow:941994550124245013> Reason", value=reason, inline=False)

            await ctx.send(embed=muteem)
            await user.send(embed=muteem)
            # sleep for specified time, then remove the muted role
            await asyncio.sleep(time_calc.get_time(time_period))
            if mute_role in user.roles:
                await user.remove_roles(mute_role)
                await ctx.send(f'{user.display_name} has been unmuted.')
        else:
            muteem=discord.Embed(description=f"<:command:941986813013274625> Action: Mute\n<:user:941986233574367253> Moderator:  {ctx.author.mention}\n<:target:941990853625389126> Target: {user.mention}",color=0x99aab5)
            muteem.add_field(name="<:rightarrow:941994550124245013> Reason", value=reason, inline=False)

            await ctx.send(embed=muteem)

    @commands.command(name='hardmute', description='Hard-mutes the person mentioned. '
                                                   'This means all roles are removed until the mute period is over. '
                                                   'Time period is optional.')
    @commands.has_permissions(manage_roles=True)
    @commands.guild_only()
    async def hardmute_func(self, ctx, user: discord.Member, time_period=None,*,reason="No reason Provided"):
        if time_period is not None:
            pattern = r"^[\d]+[s|m|h|d]{1}$"
            if not re.match(pattern, time_period):
                return await ctx.send("Time period is of the wrong format.\n"
                                      "Example usage: `5s`, `10m`, `15h`, `2d`")

        if misc_checks.is_author(ctx, user):
            return await ctx.send('You cannot mute yourself. Sorry lol')
        if misc_checks.is_client(self.bot, user):
            return await ctx.send('I can\'t mute myself, sorry.')
        if os.path.exists(f'./configs/{ctx.guild.id}.json'):
            with open(f'./configs/{ctx.guild.id}.json', 'r') as jsonFile:
                data = json.load(jsonFile)
        else:
            data = {}
        mute_role_id = (data.get('mute_role'))
        if mute_role_id is None:
            return await ctx.send('It seems you have not set the mute role. '
                                  'Please ask a person with the `Manage Server` permission '
                                  'to set a role as the mute role, '
                                  'or make one by using the `setmuterole` or `createmuterole` commands.')

        otp_success = await otp_assets.send_waitfor_otp(ctx, self.bot)
        # random otp generator. if user enters correct otp, returns true. else, returns false
        if not otp_success:
            return
        mute_role = get(ctx.guild.roles, id=int(mute_role_id))

        await ctx.send("Adding the mute role now...")
        try:
            await user.add_roles(mute_role)
        except:
            return await ctx.send(embed=discord.Embed(description=
                        f'Could not add role **{str(actual_role.name).replace("@", "")}** to '
                        f'**{user.display_name}**. Aborting...',color=0x99aab5))

        roles_embed = discord.Embed(
            title=f"{user.display_name} has these roles", color=discord.Color.random())
        roles_embed.description = "\n".join([role.mention for role in user.roles])
        roles_embed.set_footer(text="Trying to remove these roles now...")
        await ctx.send(embed=roles_embed)

        if not os.path.exists(f'./storage/mute_files/guild{ctx.guild.id}.json'):
            with open(f'./storage/mute_files/guild{ctx.guild.id}.json', "w") as createFile:
                json.dump({}, createFile)
        with open(f'./storage/mute_files/guild{ctx.guild.id}.json', "r") as mute_file:
            mute_data = json.load(mute_file)

        role_list = []
        for role in user.roles:
            if role != mute_role:
                role_id = str(role.id)
                role_list.append(role_id)

        mute_data[str(user.id)] = role_list

        with open(f'./storage/mute_files/guild{ctx.guild.id}.json', "w") as muteFile:
            json.dump(mute_data, muteFile)

        for role in user.roles:
            try:
                if not role == mute_role:
                    await user.remove_roles(role)
            except:
                await ctx.send(f"Could not remove role **{str(role.name).replace('@', '')}**. Continuing... ")
        if time_period is not None:
            final_time_text = time_calc.time_suffix(time_period)
            muteem=discord.Embed(description=f"<:command:941986813013274625> Action: HardMute\n<:user:941986233574367253> Moderator:  {ctx.author.mention}\n<:target:941990853625389126> Target: {user.mention}\n<:timer:941993935507689492> Time:  {final_time_text}",color=0x99aab5)
            muteem.add_field(name="<:rightarrow:941994550124245013> Reason", value=reason, inline=False)            
            await ctx.send(embed=muteem)
            await asyncio.sleep(time_calc.get_time(time_period))
            if mute_role in user.roles:
                # if they are unmuted, we dont want to unmute again
                await Moderation.unhardmute_func(self, ctx, user)
        else:
            muteem=discord.Embed(description=f"<:command:941986813013274625> Action: HardMute\n<:user:941986233574367253> Moderator:  {ctx.author.mention}\n<:target:941990853625389126> Target: {user.mention}\n",color=0x99aab5)
            muteem.add_field(name="<:rightarrow:941994550124245013> Reason", value=reason, inline=False)            
            await ctx.send(embed=muteem)

    @commands.command(name='unmute', description='Unmutes the user mentioned if muted previously.\n')
    @commands.guild_only()
    @commands.has_permissions(manage_roles=True)
    async def unmute_func(self, ctx, user: discord.Member,*,reason="No reason Provided"):
        if os.path.exists(f'./configs/{ctx.guild.id}.json'):
            with open(f'./configs/{ctx.guild.id}.json', 'r') as jsonFile:
                data = json.load(jsonFile)
        else:
            data = {}
        if data.get('mute_role') is None:
            return await ctx.send('It seems you have not set the mute role. '
                                  'Please ask a person with the `Manage Server` permission '
                                  'to set a role as the mute role, '
                                  'or make one by using the `setmuterole` or `createmuterole` commands.')

        mute_role_id = int(data.get('mute_role'))
        mute_role = get(ctx.guild.roles, id=mute_role_id)
        if mute_role in user.roles:
            await user.remove_roles(mute_role)
        muteem=discord.Embed(description=f"<:command:941986813013274625> Action: Un-HardMute\n<:user:941986233574367253> Moderator:  {ctx.author.mention}\n<:target:941990853625389126> Target: {user.mention}",color=0x99aab5)
        muteem.add_field(name="<:rightarrow:941994550124245013> Reason", value=reason, inline=False)            
        await ctx.send(embed=muteem)
        await ctx.send(f'{user.display_name} has been unmuted.')


    @commands.command(name="unhardmute", description="Unmutes a user if hard-muted previously.\n"
                                                     "Adds the roles that the bot took away, and removes the mute role.")
    @commands.guild_only()
    @commands.has_permissions(manage_roles=True)
    async def unhardmute_func(self, ctx, user: discord.Member):
        if not os.path.exists(f'./configs/{ctx.guild.id}.json'):
            with open(f'./configs/{ctx.guild.id}.json', 'w') as createFile:
                json.dump({}, createFile, indent=4)
                # create file if not present
                print(f'Created file guild{ctx.guild.id}.json in configs...')

        with open(f'./configs/{ctx.guild.id}.json', 'r') as jsonFile:
            data = json.load(jsonFile)

        if data.get('mute_role') is None:
            return await ctx.send('It seems you have not set the mute role. '
                                  'Please ask a person with the `Manage Server` permission '
                                  'to set a role as the mute role, '
                                  'or make one by using the `setmuterole` or `createmuterole` commands.')

        mute_role_id = int(data.get('mute_role'))

        mute_role = get(ctx.guild.roles, id=mute_role_id)

        await ctx.send(f"Unmuting {user.display_name} and re-adding roles...")

        with open(f'./storage/mute_files/guild{ctx.guild.id}.json', 'r') as mute_file:
            data = json.load(mute_file)
        role_ids = data.get(f'{user.id}')
        if role_ids is not None:
            for x in role_ids:
                actual_role = get(ctx.guild.roles, id=int(x))
                try:
                    await user.add_roles(actual_role)
                except:
                    await ctx.send(embed=discord.Embed(description=
                        f'Could not add role **{str(actual_role.name).replace("@", "")}** to '
                        f'**{user.display_name}**. Continuing...',color=0x99aab5))
                    continue
        await user.remove_roles(mute_role)
        mod=self.bot.user or ctx.author
  
        muteem=discord.Embed(description=f"<:command:941986813013274625> Action: Unhard  Mute\n<:user:941986233574367253> Moderator:  {ctx.author}\n<:target:941990853625389126> Target: {user.mention}",color=0x99aab5)
        await ctx.send(embed=muteem)

        # since they're unmuted, we don't need the role list
        data.pop(str(user.id))

        with open(f'./storage/mute_files/guild{ctx.guild.id}.json', 'w') as mute_file:
            json.dump(data, mute_file, indent=4)

    # ban user
    @commands.command(name='ban', description='Does this really need a description?\n'
                                              'Bans the user who is mentioned as argument. '
                                              'Reason is optional. Defaults to the server\'s default Kick/Ban reason '
                                              'if no reason if given.')
    @commands.has_permissions(ban_members=True)
    @commands.guild_only()
    async def ban(self, ctx, member: discord.User, *, reason=None):

        if misc_checks.is_author(ctx, member):
            return await ctx.send('You cannot ban yourself. Sorry lol')

        if misc_checks.is_client(self.bot, member):
            return await ctx.send('I can\'t ban myself, sorry.')

        otp_success = await otp_assets.send_waitfor_otp(ctx, self.bot)
        if not otp_success:
            return

        if reason is not None:
            try:
                with open(f'./configs/{ctx.guild.id}.json', 'r') as jsonFile:
                    data = json.load(jsonFile)
            except:
                data = {}
            default_kickBan_reason = data.get(
                'default_kick_ban_reason')  # get the default reason
            reason = default_kickBan_reason if default_kickBan_reason else "Being a jerk"

        message_to_user = f'You have been banned from **{ctx.guild.name}** for **{reason}**'

        try:
            await member.send(message_to_user)
        except:
            await ctx.send(f'Count not send DM to {member}. Banning anyway...')
        try:
            await ctx.guild.ban(member, reason=reason)
        except Exception as e:
            return await ctx.send(f"Failed to ban. reason: `{type(e).__name__}`")
        await ctx.send(f'**{member}** has been banned for **{reason}**.')

    # kick user
    @commands.command(name='kick', description='Kicks the user who is mentioned as argument.\n'
                                               'Reason is optional, '
                                               'and it defaults to the server\'s default Kick/Ban reason '
                                               'when no reason is given.')
    @commands.has_permissions(kick_members=True)
    @commands.guild_only()
    async def kick(self, ctx, member: discord.Member, *, reason=None):

        if misc_checks.is_author(ctx, member):
            return await ctx.send('You cannot kick yourself. Sorry lol')

        if misc_checks.is_client(self.bot, member):
            return await ctx.send('I can\'t kick myself using this command.')

        otp_success = await otp_assets.send_waitfor_otp(ctx, self.bot)
        # random otp generator. if user enters correct otp, returns true. else, returns false
        if not otp_success:
            return

        if reason is None:
            try:
                with open(f'./configs/{ctx.guild.id}.json', 'r') as jsonFile:
                    data = json.load(jsonFile)
            except:
                data = {}
            default_kickBan_reason = data.get(
                'default_kick_ban_reason')  # get the default reason
            reason = default_kickBan_reason if default_kickBan_reason else "Being a jerk"
        message_to_user = f'You have been kicked from **{ctx.guild.name}** for **{reason}**'

        try:
            await member.send(message_to_user)
        except:
            await ctx.send(f'Count not send DM to {member}. Kicking anyway...')

        await member.kick(reason=reason)
        await ctx.send(f'**{member}** has been kicked for **{reason}**.')

    # unban user.
    @commands.command(name='unban', descriptiob='Unbans a member who is mentioned as argument.\n'
                                                'Correct format of mentioning the member is '
                                                '`User#1234` or the user\'s ID.\n'
                                                'You need the `Ban Members` permission to access this command.')
    @commands.has_permissions(ban_members=True)
    @commands.guild_only()
    async def unban(self, ctx, *, member):

        otp_success = await otp_assets.send_waitfor_otp(ctx, self.bot)
        # random otp generator. if user enters correct otp, returns true. else, returns false
        if not otp_success:
            return

        banned_users = await ctx.guild.bans()
        regex_user_disc = r"^.+#\d{4}$"  # matching by User#1234
        if re.match(regex_user_disc, member):
            member_name, member_discriminator = member.split("#")
            for ban_entry in banned_users:
                user = ban_entry.user
                if (user.name, user.discriminator) == (member_name, member_discriminator):
                    await ctx.guild.unban(user)
                    await ctx.send(f'Unbanned {user}!')

        elif len(member) == 18 or len(member) == 17:  # matching by user ID
            found_user = False
            for ban_entry in banned_users:
                user = ban_entry.user
                if user.id == int(member):
                    await ctx.guild.unban(user)
                    await ctx.send(f"Unbanned {user}.")
                    found_user = True
                    break
            if not found_user:
                await ctx.send(f"Could not find member with ID **{member}**.")

        else:
            return await ctx.send("Wrong format. use `User#1234` or the user's ID (17/18 digits long).")


 


def setup(bot):
    bot.add_cog(Moderation(bot))
