import emoji , discord
async def reactor(ctx, client, message, color=0x34363A,usr=None):
    mess = await ctx.channel.send(
        embed=discord.Embed(
            title="Confirm Action", description=message, color=discord.Color(color)
        )
    )
    await mess.add_reaction('<:sucess:935052640449077248>')
    await mess.add_reaction(emoji.emojize(":cross_mark_button:"))

    person=usr

    def check(reaction, user):
        a = user == ctx.author if person is None else person == user
        return (
            reaction.message.id == mess.id
            and reaction.emoji
            in ['<:sucess:935052640449077248>', emoji.emojize(":cross_mark_button:")]
            and a
        )

    reaction, user = await client.wait_for("reaction_add", check=check)
    if reaction.emoji == '<:sucess:935052640449077248>':
        await mess.edit(
            embed=discord.Embed(
                title="Yey", description=f"Action ({message}) Confirmed ", color=color
            )
        )
      
        return True
    if reaction.emoji == emoji.emojize(":cross_mark_button:"):
        await mess.delete()
        await ctx.channel.send(
            embed=discord.Embed(
                title="Oh Okay !", description="Aborted , never mind . You can use that command again if you change your mind", color=color
            )
        )
        return False