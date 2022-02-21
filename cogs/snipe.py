import discord
from discord.ext import commands

from discord.ext.commands import has_permissions, MissingPermissions


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
                title="Message Snipe <:angry_scientist:941712157807100024>", color=self.theme_color
            )

            if msgs:
                top_author: discord.Member = await self.bot.fetch_user(
                    msgs[0].author.id
                )

                if top_author:
                    snipe_embed.set_thumbnail(url=str(top_author.avatar_url))

            for msg in msgs:
                snipe_embed.add_field(
                    name=str(msg.author), value=msg.content, inline=False
                )

            await ctx.send(embed=snipe_embed)

        except KeyError:
            await ctx.send("There's nothing to snipe here...")
     
    @commands.command(name ="clear_snipe",hidden=True)
    
    async def clearm(self,ctx):
      if ctx.author.id == 900992402356043806 or 855327915301404674:
        self.deleted_msgs.clear()
        self.edited_msgs.clear()
        await ctx.reply('Done')
      else:
        await ctx.reply('Hey you silly you cant use that command')
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
                title="Edit Snipe <:angry_scientist:941712157807100024>", color=self.theme_color
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
            await ctx.send("There's nothing to snipe here...")


def setup(bot):
    bot.add_cog(Snipe(bot))