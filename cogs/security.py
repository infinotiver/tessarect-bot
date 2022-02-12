import discord
import numpy as np
import random
import string
import Augmentor
import os
import shutil
from shutil import rmtree
import asyncio
import time
import pytz
from discord.ext import commands
from discord.utils import get
from PIL import ImageFont, ImageDraw, Image
#from Tools.utils import   updateConfig
from datetime import datetime
from datetime import date
import json
import datetime
import discapty
import kwargs
import json

class Security(commands.Cog):
    def __init__(self, client):
        self.client = client

 

    @commands.command()
    async def verify(self, ctx):
        member = ctx.author
        with open(f'./configs/{member.guild.id}.json', 'r') as jsonFile:
          data = json.load(jsonFile)
        try:
            member_role_id = data.get('member_role')
            captchaLog = self.client.get_channel(int(data['securitylogs']))
        except:
          return await ctx.send('AN ERROR DEDUCTED | MOST PROBABLY YOU HAVENT SET MEMBER ROLE AND/OR SECURITY LOGS CHANNEL')
        
        xb=await ctx.send('<a:Loading:941646457562365962> Making Captcha .... Please wait')
        await asyncio.sleep(2)
        #captchaChannel = self.client.get_channel(data["captchaChannel"])
        
        await ctx.message.delete()


        # Create captcha
        image = np.zeros(shape=(100, 350, 3), dtype=np.uint8)

        # Create image
        image = Image.fromarray(image + 209)  # +255 : black to white

        # Add text
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype(font="assets/arial.ttf", size=60)

        text = ' '.join(
            random.choice(string.ascii_uppercase) for _ in range(6))  # + string.ascii_lowercase + string.digits

        # Center the text
        W, H = (350, 100)
        w, h = draw.textsize(text, font=font)
        draw.text(((W - w) / 2, (H - h) / 2), text, font=font, fill=(90, 90, 90))

        # Save
        ID = member.id
        folderPath = f"storage/{member.guild.id}/captcha_{ID}"
        try:
            os.mkdir(folderPath)
        except:
            if os.path.isdir(f"storage/{member.guild.id}") is False:
                os.mkdir(f"storage/{member.guild.id}")
            if os.path.isdir(folderPath) is True:
                shutil.rmtree(folderPath)
            os.mkdir(folderPath)
        image.save(f"{folderPath}/captcha{ID}.png")

        # Deform
        p = Augmentor.Pipeline(folderPath)
        p.random_distortion(probability=1, grid_width=4, grid_height=4, magnitude=14)
        p.process()

        # Search file in folder
        path = f"{folderPath}/output"
        files = os.listdir(path)
        captchaName = [i for i in files if i.endswith('.png')]
        captchaName = captchaName[0]

        image = Image.open(f"{folderPath}/output/{captchaName}")

        # Add line
        width = random.randrange(2, 6)
        co1 = random.randrange(0, 75)
        co3 = random.randrange(275, 350)
        co2 = random.randrange(40, 65)
        co4 = random.randrange(40, 65)
        draw = ImageDraw.Draw(image)
        draw.line([(co1, co2), (co3, co4)], width=width, fill=(90, 90, 90))

        # Add noise
        noisePercentage = 0.20  # 20%

        pixels = image.load()  # create the pixel map
        for i in range(image.size[0]):  # for every pixel:
            for j in range(image.size[1]):
                rdn = random.random()  # Give a random %
                if rdn < noisePercentage:
                    pixels[i, j] = (90, 90, 90)

        # Save
        image.save(f"{folderPath}/output/{captchaName}_2.png")
        #data = getConfig(member.guild.id)
        #captchaChannel = self.client.get_channel(data["captchaChannel"])
        #captchaLog = self.client.get_channel(data["captchaLog"])
        #gettemprole = get(member.guild.roles, id=data["temporaryRole"])
        channel =ctx.channel #await member.guild.create_text_channel('captcha-verify-here')
        await xb.delete()
        try:
            captchaFile = discord.File(f"{folderPath}/output/{captchaName}_2.png", filename="captcha.png")
            captcha_embed = discord.Embed(title=f"{member.guild.name} Captcha Verification",
                                          description=f"{member.mention} Please return me the code written on the Captcha.",
                                          colour=discord.Colour.blue())
            captcha_embed.set_image(url="attachment://captcha.png")
            captcha_embed.set_footer(text=f"Want this bot in your server? → s!invite")
            captchaEmbed = await channel.send(file=captchaFile, embed=captcha_embed)
        except:
            pass

            # Remove captcha folder
        try:
            shutil.rmtree(folderPath)
        except Exception as error:
            print(f"Delete captcha file failed {error}")

            # Check if it is the right user

        def check(message):
            if message.author == member and message.content != "":
                return message.content

        try:
            msg = await self.client.wait_for('message', timeout=120.0, check=check)
            # Check the captcha
            password = text.split(" ")
            password = "".join(password)
            if msg.content == password:
                
                try:
                    embed = discord.Embed(
                        title="Thank you!",
                        description="You have been verified in guild **{0}**".format(
                            member.guild),
                        color=discord.Colour.blue())
                    embed.set_footer(
                        text="Want this bot in your server? → [p]invite")
                    await channel.send(embed=embed)
                except:
                    pass

                try:

                    if member_role_id is not False:
                        await member.add_roles(get(member.guild.roles, id=int(member_role_id)))
                except Exception as error:
                    print(f"Give and remove roles failed : {error}")

                time.sleep(3)
                try:
                    await captchaEmbed.delete()
                except discord.errors.NotFound:
                    pass

                #try:
                    #await channel.delete()
                #except UnboundLocalError:
                    #pass

                # Logs
                timenow = datetime.datetime.now()
                now = round(timenow.timestamp())
                embed = discord.Embed(
                    title="Captcha Logging - Passed",
                    description="User {0} has successfully passed the captcha.".format(member.mention), color=discord.Colour.blue())
                embed.add_field(
                    name="User ID",
                    value=f'{member.id}', inline=False)
                embed.add_field(name="Date", value=f"<t:{now}:F>\n", inline=False)
                embed.set_thumbnail(url=member.avatar_url)
                try:
                  await captchaLog.send(embed=embed)
                except:
                  await ctx.send('SOME ERROR CAME WHILE SENDING LOGS CHECK YOUR SECURITY LOGS CHANNEL')

            else:
                

                time.sleep(3)
                try:
                    await captchaEmbed.delete()
                except discord.errors.NotFound:
                    pass
                try:
                    await msg.delete()
                except discord.errors.Forbidden:
                    pass
                #try:
                    #await channel.delete()
                #except UnboundLocalError:
                    #pass

                timenow = datetime.datetime.now()
                now = round(timenow.timestamp())
                embed = discord.Embed(
                    title="Captcha Logging - Failed",
                    description="User {0} has failed the captcha.".format(member.mention),
                    color=discord.Colour.red())
                embed.add_field(
                    name="User ID",
                    value=f'{member.id}')
                embed.add_field(name="Date", value=f"<t:{now}:F>\n", inline=False)
                embed.set_thumbnail(url=member.avatar_url)
                try:
                  await captchaLog.send(embed=embed)
                except:
                  await ctx.send('SOME ERROR CAME WHILE SENDING LOGS CHECK YOUR SECURITY LOGS CHANNEL')

        except(asyncio.TimeoutError):
            try:
                try:
                    await member.send("You have exceeded the response time (120s), please use the verify command again!")
                except discord.errors.Forbidden:
                    await channel.send("You have exceeded the response time (120s), please use the verify command again!")
            except Exception as error:
                print(f"Log failed (onJoin) : {error}")
            time.sleep(3)
            try:
                await captchaEmbed.delete()
            except discord.errors.Forbidden:
                pass
            try:
                await channel.delete()
            except UnboundLocalError:
                pass

            timenow = datetime.datetime.now()
            now = round(timenow.timestamp())
            embed = discord.Embed(
                title="Captcha Logging - Exceeded",
                description="User {0} has exceeded the captcha response time (120s)".format(member.mention),
                timestamp=datetime.now().astimezone(tz=de), color=discord.Colour.blue())
            embed.add_field(
                name="User ID",
                value=f'{member.id}', inline=False)
            embed.add_field(name="Date", value=f"<t:{now}:F>\n", inline=False)
            embed.set_thumbnail(url=member.avatar_url)
            try:
              await captchaLog.send(embed=embed)
            except:
              await ctx.send('SOME ERROR CAME WHILE SENDING LOGS CHECK YOUR SECURITY LOGS CHANNEL')


def setup(client):
    client.add_cog(Security(client))