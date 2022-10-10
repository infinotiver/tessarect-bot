import emoji , discord 
import assets.funcs as funcs

async def reactor(ctx, client, message, color=funcs.theme_color,usr=None):
    suc = '✅'
    det='❎'
    text = await ctx.channel.send(
        embed=discord.Embed(
            title="Confirm Action", description=message, color=discord.Color(color)
        )
    )
    await text.add_reaction(suc)
    await text.add_reaction(det)

    person=usr

    def check(reaction, user):
        a = user == ctx.author if person is None else person == user
        return (
            reaction.message.id == text.id
            and reaction.emoji
            in [suc, det]
            and a
        )

    reaction, user = await client.wait_for("reaction_add", check=check)
    if reaction.emoji == suc:
        await text.delete()
      
        return True
    if reaction.emoji == det:
        await text.delete()
        await ctx.channel.send(
            embed=discord.Embed(
                title="Oh Okay !", description="Aborted , never mind . You can use that command again if you change your mind", color=color
            )
        )
        return False