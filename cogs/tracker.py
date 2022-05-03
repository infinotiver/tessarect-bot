
import discord
import asyncio
import json
import time
import typing
import datetime
from discord.ext import commands
# from discord.ext.commands import has_permissions
from discord import Embed
import DiscordUtils

class invite_tracker(commands.Cog):
    """
    Keep track of your invites
    """
    def __init__(self, bot):
        self.bot = bot


        self.invites = {}
        bot.loop.create_task(self.load())
        with open("storage/invite_channels.json", "r") as modlogsFile:
            self.modlogsFile = json.load(modlogsFile)

    @commands.command(name="invitelogschannel",

                      description="Sets the channel in which edited/deleted message logs are sent.")
    @commands.has_permissions(administrator=True)
    async def set_modlogs_channel(self, ctx, channel: discord.TextChannel):
        channel_id = channel.id
        self.modlogsFile[str(ctx.guild.id)] = int(channel_id)
        with open("storage/invite_channels.json", "w") as modlogsFile:
            json.dump(self.modlogsFile, modlogsFile, indent=4)
        await ctx.send(embed=discord.Embed(description=f"Invited Logs channel set as {channel.mention} succesfully. "
                       f"Invites , Server Joins will be shown here"))
    async def load(self):
        await self.bot.wait_until_ready()
        for guild in self.bot.guilds:
            try:
                self.invites[guild.id] = await guild.invites()
            except:
                pass

    def find_invite_by_code(self, inv_list, code):
        for inv in inv_list:
            if inv.code == code:
                return inv

    @commands.Cog.listener()
    async def on_member_join(self, member):
        message_channel_id = self.modlogsFile.get(str(member.guild.id))
        if message_channel_id is None:
            return
        message_channel = self.bot.get_channel(id=int(message_channel_id))
        if message_channel is None:
            return

        eme = Embed(description=f"Just joined  {member.guild}", color=0x03d692)
        eme.set_author(name=str(member), icon_url=member.avatar_url)
        eme.set_footer(text="ID: " + str(member.id))
        eme.timestamp = member.joined_at
        try:
            invs_before = self.invites[member.guild.id]
            invs_after = await member.guild.invites()
            self.invites[member.guild.id] = invs_after
            for invite in invs_before:
                if invite.uses < self.find_invite_by_code(invs_after, invite.code).uses:
                    eme.add_field(name="Used invite",
                                  value=f"Inviter: {invite.inviter.mention} (`{invite.inviter}` | `{str(invite.inviter.id)}`)\nCode: `{invite.code}`\nTotal Uses Uses: ` {str(invite.uses)} `", inline=False)
        except:
            pass
        await message_channel.send(embed=eme)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        message_channel_id = self.modlogsFile.get(str(member.guild.id))
        if message_channel_id is None:
            return
        message_channel = self.bot.get_channel(id=int(message_channel_id))
        if message_channel is None:
            return
        eme = Embed(description="Just left the server", color=0xff0000, title=member.guild)
        eme.set_author(name=str(member), icon_url=member.avatar_url)
        eme.set_footer(text="ID: " + str(member.id))
        eme.timestamp = member.joined_at
        try:
            invs_before = self.invites[member.guild.id]
            invs_after = await member.guild.invites()
            self.invites[member.guild.id] = invs_after
            for invite in invs_before:
                if invite.uses > self.find_invite_by_code(invs_after, invite.code).uses:
                    eme.add_field(name="Used invite",
                                  value=f"Inviter: {invite.inviter.mention} (`{invite.inviter}` | `{str(invite.inviter.id)}`)\nCode: `{invite.code}`\nUses: ` {str(invite.uses)} `", inline=False)
        except:
            pass
        await message_channel.send(embed=eme)

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        try:
            self.invites[guild.id] = await guild.invites()
        except:
            pass
 
    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        try:
            self.invites.pop(guild.id)
        except:
            pass


def setup(bot):
    bot.add_cog(invite_tracker(bot))