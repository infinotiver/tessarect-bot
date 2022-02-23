import asyncio
import random
import pyfiglet
import discord


def get_otp(digits=4):
    otp = ""
    for x in range(digits):
        otp += str(random.randint(0, 9))
    return otp


async def send_waitfor_otp(ctx, bot):
    final_otp = get_otp(4)
    embed = discord.Embed(description=f"{ctx.author.mention}, Please enter the code given below to confirm this action.", color=0x34363A)
    ascii_text = pyfiglet.figlet_format(final_otp)
    embed.add_field(name="_ _",value=f"```{final_otp}```")
    embed.set_thumbnail(url=bot.user.avatar_url)

    embed.set_footer(text="Timeout: 15 seconds")
    msg=await ctx.send(embed=embed)
    try:
        message_otp = await bot.wait_for("message", check=lambda message: message.author == ctx.author,
                                         timeout=15)
        if str(message_otp.content) == final_otp:
            su=discord.Embed(description="Correct Otp" ,color=0x34363A)
            await msg.edit(content=None,embed=su)
            await message_otp.add_reaction("<:sucess:935052640449077248>")
            return True
        else:
            er=discord.Embed(description="Incorrect Code - Aborting..." ,color=0x34363A)
            await msg.edit(embed=er)
    except asyncio.TimeoutError:
        await msg.edit(embed=er)
        return False