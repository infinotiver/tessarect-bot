import datetime
import json
import os

import discord
from discord.errors import HTTPException
from discord.ext import commands


class Logging(commands.Cog, description="Keep a track of what members do in your server with this category."):
    def __init__(self, bot):
        self.bot = bot
        with open("storage/modlogs_channels.json", "r") as modlogsFile:
            self.modlogsFile = json.load(modlogsFile)

    @commands.command(name="messagelogschannel",
                      aliases=["seteditedlogschannel", "setdeletedlogschannel",
                               "setlogschannel", "setlogchannel"],
                      description="Sets the channel in which edited/deleted message logs are sent.")
    @commands.has_permissions(administrator=True)
    async def set_modlogs_channel(self, ctx, *channel: discord.TextChannel):
        if not channel:
          try:
            set=self.modlogsFile.get(str(ctx.guild.id))
            embed=discord.Embed(title="Current Message Log channel",description=f"<#{set}>",color=discord.Color.random())
            return await ctx.send(embed=embed)
          except:
            return await ctx.send('Not set')
        channel_id = channel.id
        self.modlogsFile[str(ctx.guild.id)] = int(channel_id)
        with open("storage/modlogs_channels.json", "w") as modlogsFile:
            json.dump(self.modlogsFile, modlogsFile, indent=4)
        await ctx.send(embed=discord.Embed(description=f"Logs channel set as {channel.name} succesfully. "
                       f"Edited/Deleted mesages, and profile changes will be shown in this channel.",color=discord.Color.green()))

    # message edit event
    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        message_channel_id = self.modlogsFile.get(str(before.guild.id))
        if message_channel_id is None:
            return
        message_channel = self.bot.get_channel(int(message_channel_id))
        if message_channel is None:
            return
        message_link = f"https://discord.com/channels/{before.guild.id}/{before.channel.id}/{before.id}"
        embed = discord.Embed(title=f"Message edited in {before.channel.name}",
                              color=before.author.color, timestamp=after.created_at)
        embed.add_field(name="Before", value=before.content)
        embed.add_field(name="After", value=after.content)
        embed.add_field(
            name="Link", value=f"__[Message]({message_link})__")
        embed.set_footer(text=f"Author  •  {before.author}  |  Edited")
        embed.set_thumbnail(url=before.author.avatar_url)
        # the edited timestamp would come in the right, so we dont need to specify it in the footer
        try:
            await message_channel.send(embed=embed)
        except:  # embeds dont have a message.content, so it gives us an error
            pass

    # message delete event
    @commands.Cog.listener()
    async def on_message_delete(self, message):
        message_channel_id = self.modlogsFile.get(str(message.guild.id))
        if message_channel_id is None:
            return
        message_channel = self.bot.get_channel(int(message_channel_id))
        if message_channel is None:
            return
        embed = discord.Embed(title=f"Message deleted in {message.channel.name}",
                              color=message.author.color, timestamp=message.created_at)
        embed.add_field(name="Content", value=message.content)
        embed.set_footer(text=f"Author  •  {message.author}  |  Created")
        embed.set_thumbnail(url=message.author.avatar_url)
        if message_channel is None:
            return
        try:
            await message_channel.send(embed=embed)
        except HTTPException:
            pass

    @commands.Cog.listener()
    async def on_bulk_message_delete(self, messages):
        message_channel_id = (self.modlogsFile.get(str(messages[0].guild.id)))
        if message_channel_id is None:
            return
        message_channel = self.bot.get_channel(int(message_channel_id))
        if message_channel is None:
            return
        with open(f"storage/tempText/{messages[0].guild.id}.txt", "w") as temp_textfile:
            for x in messages:
                line1 = f"{x.channel.name} | From: {x.author} | Sent At: {x.created_at}\n"
                temp_textfile.write(line1)
                temp_textfile.write(f"{x.content}\n\n")

        file = discord.File(f"./storage/tempText/{messages[0].guild.id}.txt")
        await message_channel.send(file=file, content=f"{len(messages)} messages deleted. "
                                                      f"Sending information as text file.")
        os.remove(f"./storage/tempText/{messages[0].guild.id}.txt")

    # ban event
    @commands.Cog.listener()
    async def on_member_ban(self, guild, member):
        message_channel_id = self.modlogsFile.get(str(guild.id))
        if message_channel_id is None:
            return
        message_channel = self.bot.get_channel(int(message_channel_id))
        if message_channel is None:
            return
        embed = discord.Embed(title=f"{member} has been banned from {guild.name}", description=f"ID: {member.id}",
                              timestamp=member.created_at)
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text="Account created at")
        await message_channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        message_channel_id = self.modlogsFile.get(str(before.guild.id))
        if message_channel_id is None:
            return
        message_channel = self.bot.get_channel(int(message_channel_id))
        if message_channel is None:
            return

        # nickname change
        if not before.nick == after.nick:
            embed = discord.Embed(title=f"{before}'s nickname has been updated", description=f"ID: {before.id}",
                                  color=after.color, timestamp=before.created_at)

            embed.add_field(
                name="Before", value=before.display_name)
            embed.add_field(
                name="After", value=after.display_name)

            embed.set_thumbnail(url=after.avatar_url)
            embed.set_footer(text="Account created at")
            await message_channel.send(embed=embed)

        # role change
        if not before.roles == after.roles:
            embed = discord.Embed(title=f"{before}'s roles have been updated", description=f"ID: {before.id}",
                                  color=after.color, timestamp=before.created_at)
            before_roles_str, after_roles_str = "", ""
            for x in before.roles[::-1]:
                before_roles_str += f"{x.mention} "
            for x in after.roles[::-1]:
                after_roles_str += f"{x.mention} "
            embed.add_field(
                name="Before", value=before_roles_str)
            embed.add_field(name="After", value=after_roles_str)
            embed.set_thumbnail(url=after.avatar_url)
            embed.set_footer(text="Account created at")
            await message_channel.send(embed=embed)

    # unban event
    @commands.Cog.listener()
    async def on_member_unban(self, guild, member):
        message_channel_id = self.modlogsFile.get(str(guild.id))
        if message_channel_id is None:
            return
        message_channel = self.bot.get_channel(int(message_channel_id))
        if message_channel is None:
            return
        embed = discord.Embed(title=f"{member} has been unbanned", description=f"ID: {member.id}",
                              color=discord.Color.green(),
                              timestamp=member.created_at)
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text="Account created at")
        await message_channel.send(embed=embed)

    # join event
    @commands.Cog.listener()
    async def on_member_join(self, member):
        message_channel_id = self.modlogsFile.get(str(member.guild.id))
        if message_channel_id is None:
            return
        message_channel = self.bot.get_channel(int(message_channel_id))
        if message_channel is None:
            return
        embed = discord.Embed(title=f"{member} joined the the server.", color=discord.Color.green(),
                              timestamp=datetime.datetime.utcnow(),
                              description=f"**Their account was created at:** {member.created_at}")
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text="Join time")
        await message_channel.send(embed=embed)

    # leave event
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        message_channel_id = self.modlogsFile.get(str(member.guild.id))
        if message_channel_id is None:
            return
        message_channel = self.bot.get_channel(int(message_channel_id))
        if message_channel is None:
            return
        roles = [role for role in member.roles]
        embed = discord.Embed(title=f"{member} has left the server.", color=discord.Color.dark_red(),
                              timestamp=datetime.datetime.utcnow(),
                              description=f"**Their account was created at:** {member.created_at}")
        embed.add_field(name="Their roles", value=" ".join(
            [role.mention for role in roles]))
        embed.set_footer(text=f"Left at")
        embed.set_thumbnail(url=member.avatar_url)
        await message_channel.send(embed=embed)


def setup(bot):
    bot.add_cog(Logging(bot))