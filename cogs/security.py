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
import datetime

import json
#import datetime
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
        self.time_window_milliseconds = 5000
        self.max_msg_per_window = 5
        self.author_msg_times = {}     
        self.links=requests.get("https://raw.githubusercontent.com/Dogino/Discord-Phishing-URLs/main/scam-urls.txt").content.decode().split("\n")
        



    @commands.Cog.listener()
    async def on_message(self,message):
      
      msg = message.content.split()  
      member=message.author
      try:
        with open(f'./configs/{message.guild.id}.json', 'r') as jsonFile:
            data = json.load(jsonFile)
        if data['antiswear']:

          antiswear =data['antiswear']   
        else:
          data['antiswear']='disable'
        if data['antiscam']:

          antiscam =data['antiscam']
        else:
          data['antiscam'] ='disable'
        if data['antispam']:

          antispam =data['antispam']   
        else:
          data['antispam']='disable'          
        with open(f"./configs/{message.guild.id}.json", "w") as file:
            json.dump(data, file)          
      except:
        return

      #nsfw detection
      if message.attachments:
        if message.author==self.client.user:
          return
        for attachment in message.attachments:
            if not attachment.content_type in ('image/jpeg', 'image/jpg', 'image/png','video/mp4'):
              return

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
        name=d['output']['detections'][0]['name']
        confidence=d['output']['detections'][0]['confidence']
        
        detections=d['output']['detections']
        nsfwscorer=round(nsfwscore)
        if 'Exposed' in name :
          if message.channel.is_nsfw():
            return # if it is nsfw then ok
          else:
            await message.delete()   
            em =discord.Embed(title=" <:messagealert:942777256160428063> Nsfw Image Detected in non nsfw channel",description=f"Channel: {message.channel.mention} \n <:target:941990853625389126>Sent by: {message.author.mention}\n<:arrow_right:940608259075764265> Nsfw score: {nsfwscore}\n <:arrow_right:940608259075764265> Confidence : {confidence} \n  <:arrow_right:940608259075764265> Details: || <:uparrow:941994550027759616> Name: {name}`|`\n {detections} ||",color=0xFF0000)
            await message.channel.send(f'{message.author.mention} Stop Sending nsfw pictures in non nsfw channels',embed=em)     
      

      if antiscam =="enable": 

        reason = f"POSTING A SCAM LINK >  "
                    
        for word in self.links:
            if word in msg:
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
                      description=f"{member.name} has been warned with {warns} warn(s) for {reason} ",
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
                      description=f"{member.name} has been warned with {warns} warn(s) for {reason} ",
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
      if antispam =="enable": 
        global author_msg_counts
    
        author_id = message.author.id 
        # Get current epoch time in milliseconds
        curr_time = datetime.datetime.now().timestamp() * 1000
    
        # Make empty list for author id, if it does not exist
        if not self.author_msg_times.get(author_id, False):
            self.author_msg_times[author_id] = []
    
        # Append the time of this message to the users list of message times
        self.author_msg_times[author_id].append(curr_time)
    
        # Find the beginning of our time window.
        expr_time = curr_time - self.time_window_milliseconds
    
        # Find message times which occurred before the start of our window
        expired_msgs = [
            msg_time for msg_time in self.author_msg_times[author_id]
            if msg_time < expr_time
        ]
    
        # Remove all the expired messages times from our list
        for msg_time in expired_msgs:
            self.author_msg_times[author_id].remove(msg_time)
        # ^ note: we probably need to use a mutex here. Multiple threads
        # might be trying to update this at the same time. Not sure though.
    
        if len(self.author_msg_times[author_id]) > self.max_msg_per_window:
            await message.channel.send(embed=discord.Embed(title="Stop Spamming",description="Stop spamming and post your messages in one message !",color=discord.Color.dark_red()))        
      if antiswear =="enable":

  

        bad_list=[]
        url = "https://raw.githubusercontent.com/turalus/encycloDB/master/Dirty%20Words/DirtyWords.json"
        response = requests.get(url).json()
        records=response["RECORDS"]
        msg = message.content.split()
        for i in records:
          if i["language"] == "en": 

            bad_list.append(i["word"])
        member=message.author
        reason="Used a swear and /or bad and/or blacklisted word"
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
                        description=f"{member.name} has been warned with {warns} warn(s) for {reason} ",
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
                        description=f"{member.name} has been warned with {warns} warn(s) for {reason} ",
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

      

    @commands.command()
    async def verify(self, ctx):
        member = ctx.author
        with open(f'./configs/{member.guild.id}.json', 'r') as jsonFile:
          data = json.load(jsonFile)
        try:
            member_role_id = data.get('member_role')
            captchaLog = self.client.get_channel(int(data['securitylogs']))
        except:
          error=discord.Embed(title="Setup Not found",description="AN ERROR DEDUCTED | MOST PROBABLY YOU HAVENT SET MEMBER ROLE AND/OR SECURITY LOGS CHANNEL",color=discord.Color.dark_red())
          return await ctx.send(embed=error)
        
        xb=await ctx.send('<a:Loading:941646457562365962> Making Captcha .... Please wait')
        await asyncio.sleep(2)
        #captchaChannel = self.client.get_channel(data["captchaChannel"])
        try:
          await ctx.message.delete()
        except:
          error=discord.Embed(title="Cant Delete Message",description="Never mind this error \n Priority: Low \n Severity: Low",color=discord.Color.dark_gold())
          await ctx.send(embed=error)

        # Create captcha
        image = np.zeros(shape=(100, 350, 3), dtype=np.uint8)

        # Create image
        image = Image.fromarray(image + 255)  # +255 : black to white

        # Add text
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype(font="assets/arial.ttf", size=60)

        text = ' '.join(
            random.choice(string.ascii_uppercase) for _ in range(6))  # + string.ascii_lowercase + string.digits

        # Center the text
        W, H = (350, 100)
        w, h = draw.textsize(text, font=font)
        draw.text(((W - w) / 2, (H - h) / 2), text, font=font, fill=(0, 139, 139))

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
        co3 = random.randrange(275, 650)
        co2 = random.randrange(40, 65)
        co4 = random.randrange(40, 80)
        draw = ImageDraw.Draw(image)
        draw.line([(co1, co2), (co3, co4)], width=width, fill=(0, 0, 0))

        # Add noise
        noisePercentage = 0.20  # 20%

        pixels = image.load()  # create the pixel map
        for i in range(image.size[0]):  # for every pixel:
            for j in range(image.size[1]):
                rdn = random.random()  # Give a random %
                if rdn < noisePercentage:
                    pixels[i, j] = 	(89,203,232)

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
            captcha_embed = discord.Embed(title=f"Captcha Verification for {member.guild.name}",
                                          description=f"{member.mention} Please return me the code written on the Captcha.",
                                          colour=discord.Colour.blue())
            captcha_embed.set_image(url="attachment://captcha.png")
            captcha_embed.set_footer(text=f"Want me in your server? → [p]invite")
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
                        description=f"You have been verified in {ctx.guild}",
                        color=discord.Colour.blue())
                    embed.set_footer(
                        text="Want me in your server? → [p]invite")
                    await channel.send(embed=embed)
                except:
                    pass

                try:

                    if member_role_id is not False:
                        await member.add_roles(get(member.guild.roles, id=int(member_role_id)))
                except Exception as error:
                        error=discord.Embed(title="Error",description=f"{error}\n Priority: Top \n Severity: High",color=discord.Color.dark_red())
                        await ctx.send(embed=error)      
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
                except Exception as e:
                  error=discord.Embed(title="Error",description=f"{e}\n Priority: Mild \n Severity: Medium",color=discord.Color.red())
                  await ctx.send(embed=error)

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
                except Exception as e:
                  error=discord.Embed(title="Error",description=f"{e}\n Priority: Mild \n Severity: Medium",color=discord.Color.red())
                  await ctx.send(embed=error)

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
                print('hi')
            except UnboundLocalError:
                pass

            timenow = datetime.datetime.now()
            now = round(timenow.timestamp())
            embed = discord.Embed(
                title="Captcha Logging - Exceeded",
                description="User {0} has exceeded the captcha response time (120s)".format(member.mention),
                timestamp=datetime.datetime.now().astimezone(tz=de), color=discord.Colour.blue())
            embed.add_field(
                name="User ID",
                value=f'{member.id}', inline=False)
            embed.add_field(name="Date", value=f"<t:{now}:F>\n", inline=False)
            embed.set_thumbnail(url=member.avatar_url)
            try:
              await captchaLog.send(embed=embed)
            except Exception as e:
                  error=discord.Embed(title="Error",description=f"{e}\n Priority: Mild \n Severity: Medium",color=discord.Color.red())
                  await ctx.send(embed=error)




def setup(client):
    client.add_cog(Security(client))