import discord
import numpy as np
import random
import string
import Augmentor
import os
import requests
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
import requests
import motor
mongo_url = os.environ['warn']
cluster = motor.motor_asyncio.AsyncIOMotorClient(mongo_url)
import discord_pass

warndb = cluster["discord"]["warn"]
warns=1
reason="Used a bad word"
class Security(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.warns={}



    @commands.Cog.listener()
    async def on_message(self,message):
      if message.attachments:
        r = requests.post(
            "https://api.deepai.org/api/nsfw-detector",
            data={
                'image': message.attachments[0].url,
            },
            headers={'api-key': os.environ['deepai']}
        )
        print(r.json())  
        #{'id': 'c9d5bf5b-a9ea-4aa7-a854-3ff04c0da209', 'output': {'detections': [{'confidence': '0.95', 'bounding_box': [116, 118, 187, 94], 'name': 'blah'}], 'nsfw_score': 0.7178798913955688}}    
        # example response  
        d= r.json()
        nsfwscore=d['output']['nsfw_score']
        nsfwscorer=round(nsfwscore)
        if nsfwscorer == 1:
          if message.channel.is_nsfw():
            return # if it is nsfw then ok
          else:
            await message.delete()   
            await message.channel.send(f'{message.author.mention} Stop Sending nsfw pictures in non nsfw channels')     
      
      with open(f'./storage/scamlinks.json', 'r') as jsonFile:
          link = json.load(jsonFile)    
          scamlinks = link['scamlinks']
      
      
      member=message.author
      for links in scamlinks:
        reason = f"POSTING A SCAM LINK > {link} "
        if links in message.content and message.author !=self.client.user:
            if message.author.id in self.warns:
              self.warns[message.author.id] +=1
              print(self.warns)
            else:
              self.warns[message.author.id]=1
              print(self.warns)          
            stats = await warndb.find_one({"id": member.id})
            await message.delete() 
            if stats is None and warns <= 5:
                passwor = discord_pass.secure_password_gen(10)
                passwor = str(passwor)
                newuser = {
                    "id": member.id,
                    "Cases": [[passwor, reason, message.author.mention, warns]],
                    "warns": warns,
                }
                await warndb.insert_one(newuser)
                embed = discord.Embed(
                    title="Warn",
                    description=f"{member.name} has been warned with {warns} warn(s) for `{reason}` ",
                    color=0xFF0000,
                )
                await message.channel.send(embed=embed)   
            else:
                passwor = discord_pass.secure_password_gen(10)
                passwor = str(passwor)
                total_warn = stats["warns"] + warns
                await warndb.update_one(
                    {"id": member.id}, {"$set": {"warns": total_warn}}
                )
                await warndb.update_one(
                    {"id": member.id},
                    {
                        "$addToSet": {
                            "Cases": [
                                passwor,
                                reason,
                                message.author.mention,
                                warns,
                            ]
                        }
                    },
                )

                embed = discord.Embed(
                    title="Warn",
                    description=f"{member.name} has been warned with {warns} warn(s) for `{reason}` ",
                    color=0xFF0000,
                )
                await message.channel.send(embed=embed)

                if self.warns[message.author.id] >= 10:
                  try:

                    await member.kick(reason=reason)
                    embed = discord.Embed(
                        title="Warn",
                        description=f"{member.name} has been kicked since the y exceeded the warn limit",
                        color=0xFF0000,
                    )
                    await message.channel.send(embed=embed)

                    await warndb.delete_one({"id": member.id})
                  except Exception as e:
                    return await message.channel.send(f'WARN LIMIT EXCEEDED | UNSUCCESSFUL kick\n{e}')
      
      try:

        with open(f'./configs/{message.guild.id}.json', 'r') as jsonFile:
            data = json.load(jsonFile)


        if not data['antiswear'] =="enable":
          return
      except:
        return         
      msg = message.content.split()    

      bad_list=[]
      url = "https://raw.githubusercontent.com/turalus/encycloDB/master/Dirty%20Words/DirtyWords.json"
      response = requests.get(url).json()
      records=response["RECORDS"]
      msg = message.content.split()
      for i in records:
        if i["language"] == "en": bad_list.append(i["word"])
      member=message.author
      for word in bad_list:
          if word in msg:
              
              #await message.delete()
              stats = await warndb.find_one({"id": member.id})
              await message.delete() 
              if stats is None and warns <= 5:
                  passwor = discord_pass.secure_password_gen(10)
                  passwor = str(passwor)
                  newuser = {
                      "id": member.id,
                      "Cases": [[passwor, reason, message.author.mention, warns]],
                      "warns": warns,
                  }
                  await warndb.insert_one(newuser)
                  embed = discord.Embed(
                      title="Warn",
                      description=f"{member.name} has been warned with {warns} warn(s) for `{reason}` ",
                      color=0xFF0000,
                  )
                  await message.channel.send(embed=embed)   
              else:
                  passwor = discord_pass.secure_password_gen(10)
                  passwor = str(passwor)
                  total_warn = stats["warns"] + warns
                  await warndb.update_one(
                      {"id": member.id}, {"$set": {"warns": total_warn}}
                  )
                  await warndb.update_one(
                      {"id": member.id},
                      {
                          "$addToSet": {
                              "Cases": [
                                  passwor,
                                  reason,
                                  message.author.mention,
                                  warns,
                              ]
                          }
                      },
                  )

                  embed = discord.Embed(
                      title="Warn",
                      description=f"{member.name} has been warned with {warns} warn(s) for `{reason}` ",
                      color=0xFF0000,
                  )
                  await message.channel.send(embed=embed)

                  if self.warns[message.author.id] >= 10:
                    try:

                      await member.kick(reason=reason)
                      embed = discord.Embed(
                          title="Warn",
                          description=f"{member.name} has been kicked since the y exceeded the warn limit",
                          color=0xFF0000,
                      )
                      await message.channel.send(embed=embed)

                      await warndb.delete_one({"id": member.id})
                    except Exception as e:
                      return await message.channel.send(f'WARN LIMIT EXCEEDED | UNSUCCESSFUL kicj\n{e}')


      

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
            captcha_embed.set_footer(text=f"Want this bot in your server? → [p]invite")
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