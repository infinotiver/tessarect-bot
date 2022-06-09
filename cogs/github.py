import json

import requests
from bs4 import BeautifulSoup
from discord.ext import commands

import discord

def createem(text,color=0x171515):
  
  return discord.Embed(description=text,color=color)

class GitHub(commands.Cog):
    """Get repository info"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['ghr'])
    async def github(self, ctx, arg):
        """Fetch repository info"""

        req = requests.get(f'https://api.github.com/repos/{arg}')
        apijson = json.loads(req.text)
        if req.status_code == 200:
            em = discord.Embed(color=0x4078c0)
            em.set_author(name=apijson['owner']['login'], icon_url=apijson['owner']['avatar_url'],
                          url=apijson['owner']['html_url'])
            em.set_thumbnail(url=apijson['owner']['avatar_url'])
            em.add_field(name="Repository:", value=f"[{apijson['name']}]({apijson['html_url']})", inline=True)
            em.add_field(name="Language:", value=apijson['language'], inline=True)

            try:
                license_url = f"[{apijson['license']['spdx_id']}]({json.loads(requests.get(apijson['license']['url']).text)['html_url']})"
            except:
                license_url = "None"
            em.add_field(name="License:", value=license_url, inline=True)
            if apijson['stargazers_count'] != 0:
                em.add_field(name="Star:", value=apijson['stargazers_count'], inline=True)
            if apijson['forks_count'] != 0:
                em.add_field(name="Fork:", value=apijson['forks_count'], inline=True)
            if apijson['open_issues'] != 0:
                em.add_field(name="Issues:", value=apijson['open_issues'], inline=True)
            em.add_field(name="Description:", value=apijson['description'], inline=False)

            for meta in BeautifulSoup(requests.get(apijson['html_url']).text, features="html.parser").find_all('meta'):
                try:
                    if meta.attrs['property'] == "og:image":
                        em.set_thumbnail(url=meta.attrs['content'])
                        break
                except:
                    pass

            await ctx.send(embed=em)
        elif req.status_code == 404:
            """if repository not found"""
            await ctx.send(embed=createem('NOT FOUND'))
        elif req.status_code == 503:
            """GithubAPI down"""
            await ctx.send(embed=createem("GithubAPI down"))
            
        else:
            """some error occurred while fetching repository info"""
            await ctx.send(embed=createem('UNKNOWN ERROR'))
    @commands.command(aliases=['ghu'])
    async def githubuser(self, ctx, arg):
        """Fetch user info"""

        req = requests.get(f'https://api.github.com/users/{arg}')
        apijson = json.loads(req.text)
        if req.status_code == 200:
            em = discord.Embed(color=0x4078c0,description=f"<:github:912608431230320660> {apijson['public_repos']} Public Repos \n {apijson['public_gists']} Public Gists & {apijson['followers']} Followers & {apijson['following']} Following")
            em.set_author(name=f"{apijson['name']}", icon_url=apijson['avatar_url'],
                          url=apijson['html_url'])
            em.set_thumbnail(url=apijson['avatar_url'])
            em.set_footer(text='Account created at '+apijson['created_at'])


            
            em.add_field(name="Bio", value=f"```\n{apijson['bio']}\n```", inline=False)
            
            em.add_field(name="Company", value=apijson['company'], inline=False)
            em.add_field(name="Blog", value=apijson['blog'], inline=False)
            em.add_field(name="Location", value=apijson['location'], inline=False)
            



            await ctx.send(embed=em)
        elif req.status_code == 404:
            """if user not found"""
            await ctx.send(embed=createem('NOT FOUND'))
        elif req.status_code == 503:
            """GithubAPI down"""
            await ctx.send(embed=createem("GithubAPI down"))
            
        else:
            """some error occurred while fetching repository info"""
            await ctx.send(embed=createem('UNKNOWN ERROR'))


def setup(bot):
    """ Setup GitHub Module"""
    bot.add_cog(GitHub(bot))