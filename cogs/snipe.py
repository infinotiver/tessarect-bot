import discord
from discord.ext import commands
import DiscordUtils
from discord.ext.commands import has_permissions, MissingPermissions
import datetime 

class Snipe(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.description = (
            " <:sucess:935052640449077248> Commands to snipe out messages that people try to hide"
        )
        self.theme_color = discord.Color.blue()

        self.deleted_msgs = {}
        self.edited_msgs = {}
        self.snipe_limit = 20
       
    @commands.Cog.listener()
    async def on_message_delete(self, message: discord.Message):
        ch_id = message.channel.id

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
    async def snipe(self, ctx: commands.Context):
        limit = self.snipe_limit

     
        try:
            msgs: list[discord.Message] = self.deleted_msgs[ctx.channel.id][
                ::-1
            ][:limit]
            print(msgs)
            





            
            embeds=[]
            for msg in msgs:
                snipe_embed = discord.Embed(
                title="Snipe",description=f"Most recent deleted messages\n Channel {ctx.channel.mention}", color=self.theme_color
            )
                a=str(msg.created_at)
                b = datetime.datetime.strptime(a, '%Y-%m-%d %H:%M:%S.%f')
                c = b.timestamp()
                snipe_embed.add_field(
                    name=f"{msg.author} @<t:{round(c)}>", value=f"{msg.content}", inline=False
                )
                embeds.append(snipe_embed)
              
                

            paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, remove_reactions=True)
            paginator.add_reaction('<:arrow_left:940845517703889016>', "first")
            paginator.add_reaction('<:leftarrow:941994549935472670>', "back")
            
            paginator.add_reaction('<:rightarrow:941994550124245013>', "next")
            paginator.add_reaction('<:arrow_right:940608259075764265>', "last")
            paginator.add_reaction('<:DiscordCross:940914829781270568>', "lock")
            await paginator.run(embeds)      

        except KeyError:
            await ctx.send(embed=discord.Embed(description="**There's nothing to snipe here...**\n Wait for a deleted message",color=discord.Color.dark_grey()))

    @commands.command(
        name="editsnipe",
        aliases=["esn"],
        help="See recently edited messages in the current channel",
    )
    @has_permissions(manage_messages=True)
    async def editsnipe(self, ctx: commands.Context):
        limit = self.snipe_limit

        try:
            msgs = self.edited_msgs[ctx.channel.id][::-1][:limit]
            

            


            embeds=[]
            for msg in msgs:
                editsnipe_embed = discord.Embed(title=f"Edit Snipe ({len(self.edited_msgs[ctx.channel.id][::-1][:limit])} Entries)",
                description=f"Author  •  {msg[1].author}  |  Edited", color=self.theme_color
            )
                editsnipe_embed.add_field(
                    name='Before',
                    value=f"{msg[0].content}",
                    inline=True,
                )
                editsnipe_embed.add_field(
                    name='After',
                    value=f" {msg[1].content}",
                    inline=True,
                )
                editsnipe_embed.set_footer(text=f"Edited at {msg[1].created_at}")
                embeds.append(editsnipe_embed)
            paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, remove_reactions=True)
            paginator.add_reaction('<:arrow_left:940845517703889016>', "first")
            paginator.add_reaction('<:leftarrow:941994549935472670>', "back")
            
            paginator.add_reaction('<:rightarrow:941994550124245013>', "next")
            paginator.add_reaction('<:arrow_right:940608259075764265>', "last")
            paginator.add_reaction('<:DiscordCross:940914829781270568>', "lock")
            await paginator.run(embeds)            

        except KeyError:
            await ctx.send(embed=discord.Embed(description="**There's nothing to snipe here...**\n Wait for a edited message",color=discord.Color.dark_grey()))


def setup(bot):
    bot.add_cog(Snipe(bot))