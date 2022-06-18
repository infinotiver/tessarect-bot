import asyncio
import random
import requests
import discord
from discord.ext import commands
import aiohttp
import json
import aiohttp
import requests
import os
from discord.ext import commands, tasks
import re
def findurl(string):
  
    # findall() has been used 
    # with valid conditions for urls in string
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex,string)      
    return [x[0] for x in url]
class AI(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.description = (
            "<:sucess:935052640449077248> Ai related commands , feel smart by using it"
        )
    @commands.command(
        name="chat",aliases=['chit','c','talk'] ,help="Chat from bot"
    )
    async def chat(self, ctx,*,text):
      key=os.environ['chatbot']
      page = requests.get(f'https://api.popcat.xyz/chatbot?msg={text}&owner=SniperXi199+and+their+co+devs&botname=Tessarect')
      d = json.loads(page.content)

      out=d['response']
      urls=findurl(out)
      
      em=discord.Embed(description=out,color=0x34363A)

      if len(urls)==1:
        
        em.set_image(url=f"https://image.thum.io/get/width/1920/crop/675/maxAge/1/noanimate/{urls[0]}")
      elif len(urls)>1:
        em.add_field(name="Links",value=urls)
      await ctx.send(embed=em)          
    @commands.command(
        name="generate",aliases=['gen'] ,help="Generate some text"
    )
    async def gen(self, ctx,*,text):

      r = requests.post(
          "https://api.deepai.org/api/text-generator",
          data={
              'text': text,
          },
          headers={'api-key': os.environ['deepai']}
      )
      d=r.json()
      out=d['output']
      em=discord.Embed(description=out,color=0x34363A)
      await ctx.send(embed=em)    
    @commands.command(
        name="text2image",aliases=['createimage','text2img'] ,help="Creates image from your text , Recommended for Nature related images"
    )
    async def text2img(self, ctx,*,text):

      r = requests.post(
          "https://api.deepai.org/api/text2img",
          data={
              'text': text,
          },
          headers={'api-key': os.environ['deepai']}
      )
      d=r.json()
      img=d['output_url']
      em=discord.Embed(color=0x34363A)
      em.set_footer(text="The image may not be as you want , Recommended for Nature related images")
      em.set_image(url=img)
      await ctx.send(embed=em) 
    @commands.command(
        name="sentiment",help="This sentiment analysis API extracts sentiment in a given string of text. This  classifies each sentence in the input as very negative, negative, neutral, positive, or very positive."
    )
    async def check(self, ctx,*,text):

      r = requests.post(
          "https://api.deepai.org/api/sentiment-analysis",
          data={
              'text': text,
          },
          headers={'api-key': os.environ['deepai']}
      )
      d=r.json()
      out=d['output']
      em=discord.Embed(title="Text Sentitment",description=','.join(out),color=0x34363A)

      
      await ctx.send(embed=em)
    @commands.command(
        name="deepdream",help="Exaggerates feature attributes or textures using information that the bvlc_googlenet model learned during training. THE URL SHOULD BE A IMAGE URL OR ELSE ERROR WILL COME , IF NO URL PROVIDED YOUR PFP WILL BE TAKEN AS INPUT"
    )
    async def deepdream(self, ctx,*,url=None):
      if not url:
        url=str(ctx.author.avatar_url_as(format='png'))

      r = requests.post(
          "https://api.deepai.org/api/deepdream",
          data={
              'image': url,
          },
          headers={'api-key': os.environ['deepai']}
      )
      d=r.json()
      out=d['output_url']
      em=discord.Embed(color=0x34363A)
      em.set_image(url=out)     
      await ctx.send(embed=em)     
    @commands.command(
        name="enhance",help="Super Resolution API"
    )
    async def enhance(self, ctx,*,url=None):
      if not url:
        url=str(ctx.author.avatar_url_as(format='png'))

      r = requests.post(
          "https://api.deepai.org/api/torch-srgan",
          data={
              'image': url,
          },
          headers={'api-key': os.environ['deepai']}
      )
      d=r.json()
      out=d['output_url']
      em=discord.Embed(color=0x34363A)
      em.set_image(url=out)     
      await ctx.send(embed=em)    
       
def setup(bot):
    bot.add_cog(AI(bot))
