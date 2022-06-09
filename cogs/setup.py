import json
import os
import DiscordUtils
import discord
from discord.ext import commands
import motor.motor_asyncio
import nest_asyncio
from assets.reactor import reactor
from pymongo import MongoClient
from assets.reactor import reactor
nest_asyncio.apply()
mongo_url =  os.environ['enalevel']

cluster = motor.motor_asyncio.AsyncIOMotorClient(mongo_url)

ledb = cluster["discord"]["enalevel"]

def createem(text,color=0x71C562):
  
  return discord.Embed(description=text,color=color)

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
                              color=0x34363A)



        embed.add_field(name='<:rightarrow:941994550124245013>Set default reason when kicking/banning members',
                        value=f'`[p]setkickreason [reason]`\nExample: `[p]setkickreason Being a jerk :rofl:`\n'
                              f'__**What the kicked member would see**__:\n'
                              f'You have been kicked from **{ctx.guild.name}** for **Being a jerk :rofl:**.',
                        inline=False)

        embed.add_field(name='<:rightarrow:941994550124245013>Set the mute role for this server',
                        value=f'`[p]setmuterole [role]`\nExample: `[p]setmuterole muted` '
                              f'(muted must be an actual role).\n'
                              f'You can create a mute role by `[p]createmuterole [role name]`',
                        inline=False)

        embed.add_field(name='<:rightarrow:941994550124245013>Set the default Member role for this server',
                        value=f'`[p]setmemberrole [role]`\nExample: `[p]setmemberrole Member`'
                              f' (Member must be an actual role).\n'
                              f'If you want to turn off MemberRole, make a role, assign the member role to that role, and delete the role. It is for verify command',
                        inline=False)
        embed2=discord.Embed(timestamp=ctx.message.created_at,
                              color=0x34363A)
        embed2.add_field(name="<:rightarrow:941994550124245013>Switch antiswear filter for this server",value=f"Tessarect offers a very advanced antiswear filter to keep your server safe , to enable by disable it do `[p]antiswear [enable/disable]`")           
        embed2.add_field(name="<:rightarrow:941994550124245013>Switch antiscam filter for this server",value=f"Tessarect offers a very advanced antiscam filter to keep your server safe , to enable by disable it do `[p]antiscam [enable/disable]`")                                    
        embed.add_field(name='Set the Security Logs channel [important]',
                        value=f'Set the security logs channel use `[p]securitylogschannel <channel>`',
                        inline=False)                        
        embed2.add_field(name="<:rightarrow:941994550124245013>Switch Levelling System for this server",value=f"Tessarect offers a very advanced and good levelling system , if you want to switch it (disabled by default) you can do \n `[p]levelconfig [enable/disable]`. \n Get more info on its commands by using `[p]help Level`")
       
        embed2.set_footer(text=f' Note there are other setups too for each cog you are requested to go through it while using them | Requested by {ctx.author.name}')
        paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx,remove_reactions=True)
        embeds = [embed, embed2]
        paginator.add_reaction('<:arrow_left:940845517703889016>', "first")
        paginator.add_reaction('<:leftarrow:941994549935472670>', "back")
        
        paginator.add_reaction('<:rightarrow:941994550124245013>', "next")
        paginator.add_reaction('<:arrow_right:940608259075764265>', "last")
        paginator.add_reaction('<:DiscordCross:940914829781270568>', "lock")
        await paginator.run(embeds)




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

        await ctx.send(embed=createem(f'Default kick/ban reason set to **{reason}** successfully.'))
    @commands.command(name='securitylogschannel', description='Set logs channel for security related messages')
    @commands.has_permissions(manage_guild=True)
    @commands.guild_only()
    async def securitylogs(self, ctx, role: discord.TextChannel):
        if os.path.exists(f'./configs/{ctx.guild.id}.json'):
            with open(f'./configs/{ctx.guild.id}.json', 'r') as jsonFile:
                data = json.load(jsonFile)
        else:
            data = {}

        data['securitylogs'] = role.id

        with open(f'./configs/{ctx.guild.id}.json', 'w') as jsonFile:
            json.dump(data, jsonFile, indent=3)

        await ctx.send(embed=createem(f'Security Logs Channel set to **{role.mention}** successfully.'))

    @commands.command(name='setmemberrole', description='Set role which user gets on using verify command')
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

        await ctx.send(embed=createem(f'Member role set to **{role.name}** successfully.'))

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

        await ctx.send(embed=createem(f'Mute role set to **{role.name}** successfully.'))

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
        await ctx.send(embed=createem(f'Created role **{mutedRole}** and set permissions accordingly.'))
        await Setup.set_mute_role(self, ctx, mutedRole)


    @commands.command(name='antiswear', description='Toggle Antiswear filter (enable or disable only)')
    @commands.has_permissions(manage_guild=True)
    @commands.guild_only()
    async def antiswear(self, ctx, *, choice):
        lst = ["enable", "disable"]
        if choice in lst:      

          if os.path.exists(f'./configs/{ctx.guild.id}.json'):
              with open(f'./configs/{ctx.guild.id}.json', 'r') as jsonFile:
                  data = json.load(jsonFile)
          else:
              data = {}

          data['antiswear'] = str(choice)

          with open(f'./configs/{ctx.guild.id}.json', 'w') as jsonFile:
              json.dump(data, jsonFile, indent=4)

          await ctx.send(embed=createem(f'**Changes Saved | Choice : {choice}**'))
        else:
          await ctx.send(embed=createem('Invalid Choice'))
    @commands.command(name='antiscam', description='Toggle Antiscam filter (enable or disable only)')
    @commands.has_permissions(manage_guild=True)
    @commands.guild_only()
    async def antiscam(self, ctx, *, choice):
        lst = ["enable", "disable"]
        if choice in lst:      

          if os.path.exists(f'./configs/{ctx.guild.id}.json'):
              with open(f'./configs/{ctx.guild.id}.json', 'r') as jsonFile:
                  data = json.load(jsonFile)
          else:
              data = {}

          data['antiscam'] = str(choice)

          with open(f'./configs/{ctx.guild.id}.json', 'w') as jsonFile:
              json.dump(data, jsonFile, indent=4)

          await ctx.send(embed=createem(f'**Changes Saved | Choice : {choice}**'))
        else:
          await ctx.send(embed=createem('Invalid Choice')   )
            
    @commands.command(name='antispam', description='Toggle Antispam filter (enable or disable only)')
    @commands.has_permissions(manage_guild=True)
    @commands.guild_only()
    async def antispamr(self, ctx, *, choice):
        lst = ["enable", "disable"]
        if choice in lst:      

          if os.path.exists(f'./configs/{ctx.guild.id}.json'):
              with open(f'./configs/{ctx.guild.id}.json', 'r') as jsonFile:
                  data = json.load(jsonFile)
          else:
              data = {}

          data['antispam'] = str(choice)

          with open(f'./configs/{ctx.guild.id}.json', 'w') as jsonFile:
              json.dump(data, jsonFile, indent=4)

          await ctx.send(embed=createem(f'**Changes Saved | Choice : {choice}**'))
        else:
          await ctx.send(embed=createem('Invalid Choice')  )        
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
                    await ctx.send(embed=createem("**Changes are saved**"))

                elif stats["type"] == 0:
                    await ctx.send(embed=createem("**Command is already enabled**"))

                else:
                    await ledb.update_one(
                        {"id": ctx.guild.id}, {"$set": {"type": choice}}
                    )

                    await ctx.send(embed=createem("**Changes are saved | Command enabled**"))
            else:
                choice = 1

                stats = await ledb.find_one({"id": ctx.guild.id})
                if stats is None:
                    newuser = {"id": ctx.guild.id, "type": choice}
                    await ledb.insert_one(newuser)
                    await ctx.send(embed=createem("**Changes are saved**"))

                elif stats["type"] == 1:
                    await ctx.send(embed=createem("**Command is already disabled**"))

                else:
                    await ledb.update_one(
                        {"id": ctx.guild.id}, {"$set": {"type": choice}}
                    )

                    await ctx.send(embed=createem("**Changes are saved | Command disabled**"))

        else:
            await ctx.send(embed=createem("**It can be enable/disable only**"))


def setup(bot):
    bot.add_cog(Setup(bot))