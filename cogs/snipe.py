import discord
from discord.ext import commands

from discord.ext.commands import has_permissions, MissingPermissions
import datetime 

class Snipe(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.description = (
            "Commands to snipe out messages that people try to hide"
        )
        self.theme_color = discord.Color.blue()

        self.deleted_msgs = {}
        self.edited_msgs = {}
        self.snipe_limit = 17
       
    @commands.Cog.listener()
    async def on_message_delete(self, message: discord.Message):
        ch_id = message.channel.id

        if not message.author.bot:
            if message.content:
                if ch_id not in self.deleted_msgs:
                    self.deleted_msgs[ch_id] = []

                self.deleted_msgs[ch_id].append(message)

            if len(self.deleted_msgs[ch_id]) > self.snipe_limit:
                self.deleted_msgs[ch_id].pop(0)

    @commands.Cog.listener()
    async def on_message_edit(
        self, before: discord.Message, after: discord.Message
    ):
        ch_id = before.channel.id

        if not before.author.bot:
            if before.content and after.content:
                if ch_id not in self.edited_msgs:
                    self.edited_msgs[ch_id] = []

                self.edited_msgs[ch_id].append((before, after))

            if len(self.edited_msgs[ch_id]) > self.snipe_limit:
                self.edited_msgs[ch_id].pop(0)

    @commands.command(
        name="snipe",
        aliases=["sn"],
        help="See recently deleted messages in the current channel",
    )
    @has_permissions(manage_messages=True)
    async def snipe(self, ctx: commands.Context, limit: int = 1):
        if limit > self.snipe_limit:
            await ctx.send(f"Maximum snipe limit is {self.snipe_limit}")
            return
     
        try:
            msgs: list[discord.Message] = self.deleted_msgs[ctx.channel.id][
                ::-1
            ][:limit]
            snipe_embed = discord.Embed(
                title="Message Snipe",description=f"Most recent deleted messages\n Channel {ctx.channel.mention}", color=self.theme_color
            )





            snipe_embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/941712157807100024.webp?size=96&quality=lossless')

            sc=1
            for msg in msgs:
                a=str(msg.created_at)
                b = datetime.datetime.strptime(a, '%Y-%m-%d %H:%M:%S.%f')
                c = b.timestamp()
                snipe_embed.add_field(
                    name=f"({sc}) {msg.author.display_name} @<t:{round(c)}>", value=f"{msg.content}", inline=False
                )
                sc+=1

            await ctx.send(embed=snipe_embed)

        except KeyError:
            await ctx.send(embed=discord.Embed(description="**There's nothing to snipe here...**\n Wait for a deleted message",color=discord.Color.dark_red()))

    @commands.command(
        name="editsnipe",
        aliases=["esn"],
        help="See recently edited messages in the current channel",
    )
    @has_permissions(manage_messages=True)
    async def editsnipe(self, ctx: commands.Context, limit: int = 1):
        if limit > self.snipe_limit:
            await ctx.send(f"Maximum snipe limit is {self.snipe_limit}")
            return

        try:
            msgs = self.edited_msgs[ctx.channel.id][::-1][:limit]
            editsnipe_embed = discord.Embed(
                title="Edit Snipe", color=self.theme_color
            )

            if msgs:
                top_author: discord.Member = await self.bot.fetch_user(
                    msgs[0][0].author.id
                )

                if top_author:
                    editsnipe_embed.set_thumbnail(
                        url=str(top_author.avatar_url)
                    )

            for msg in msgs:
                editsnipe_embed.add_field(
                    name=str(msg[0].author),
                    value=f"{msg[0].content} **-->** {msg[1].content}",
                    inline=False,
                )

            await ctx.send(embed=editsnipe_embed)

        except KeyError:
            await ctx.send(embed=discord.Embed(description="**There's nothing to snipe here...**\n Wait for a edited message",color=discord.Color.dark_red()))


def setup(bot):
    bot.add_cog(Snipe(bot))