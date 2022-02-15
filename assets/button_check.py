import asyncio
import random

import discord
from dislash import InteractionClient, ActionRow, Button, ButtonStyle



async def send_waitfor_otp(ctx, bot):
    inter_client = InteractionClient(bot)

    row = ActionRow(
   
        Button(
            style=ButtonStyle.success,
            label="Confirm!",
            custom_id="gr",
            emoji="<:like_blue_purple:939021441213562890>"
        ),
        Button(
            style=ButtonStyle.danger,
            label="Cancel!",
            custom_id="red",
            emoji="<:dislike_blue_purple:939021398284857364>"
        )        
    )   
  
    embed = discord.Embed(
        timestamp=ctx.message.created_at, title="Confirm",description="Confirm your request", color=0x06c8f9
    )

    msg =await ctx.send(embed=embed,components=[row])
    on_click = msg.create_click_listener(timeout=10)
    @on_click.matching_id("red")
    async def on_test_button(inter):
      em = discord.Embed(title="Cancelled",description="Alright",color=discord.Color.red())   
      await msg.edit(content=None,embed=em)
      await msg.edit(components=[])
      return False
    @on_click.matching_id("gr")
    async def on_test_button(inter):
      await msg.edit(components=[])
      return True
    @on_click.timeout
    async def on_timeout():
        await msg.edit(components=[])
        return False      
