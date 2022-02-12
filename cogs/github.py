import json

import requests
from bs4 import BeautifulSoup
from discord.ext import commands

import discord


class GitHub(commands.Cog):
    """Get repository info"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['gh'])
    async def github(self, ctx, arg):
        """Fetch repository info"""

        req = requests.get(f'https://api.github.com/repos/{arg}')
        apijson = json.loads(req.text)
        if req.status_code == 200:
            em = discord.Embed()
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
                        em.set_image(url=meta.attrs['content'])
                        break
                except:
                    pass

            await ctx.send(embed=em)
        elif req.status_code == 404:
            """if repository not found"""
            await ctx.send('NOT FOUND')
        elif req.status_code == 503:
            """GithubAPI down"""
            await ctx.send("GithubAPI down")
            
        else:
            """some error occurred while fetching repository info"""
            await ctx.send('UNKNOWN ERROR')


def setup(bot):
    """ Setup GitHub Module"""
    bot.add_cog(GitHub(bot))