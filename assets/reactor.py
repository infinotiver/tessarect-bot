import emoji , discord

async def reactor(ctx, client, message, color=0x34363A,usr=None):
    suc = '✅'
    det='❎'
    mess = await ctx.channel.send(
        embed=discord.Embed(
            title="Confirm Action", description=message, color=discord.Color(color)
        )
    )
    await mess.add_reaction(suc)
    await mess.add_reaction(det)

    person=usr

    def check(reaction, user):
        a = user == ctx.author if person is None else person == user
        return (
            reaction.message.id == mess.id
            and reaction.emoji
            in [suc, det]
            and a
        )

    reaction, user = await client.wait_for("reaction_add", check=check)
    if reaction.emoji == suc:
        await mess.delete()
      
        return True
    if reaction.emoji == det:
        await mess.delete()
        await ctx.channel.send(
            embed=discord.Embed(
                title="Oh Okay !", description="Aborted , never mind . You can use that command again if you change your mind", color=color
            )
        )
        return False