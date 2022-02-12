import asyncio
import discord_pass
import random
import string
import requests
import discord
import pyfiglet
from discord.ext import commands
import aiohttp
import json
import aiohttp

import os

from discord.ext import commands, tasks
async def get_tinyurl(link: str):
    url = f"http://tinyurl.com/api-create.php?url={link}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            response = (await response.content.read()).decode('utf-8')
    return response      

class FunUtility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.description = (
            "Commands to have some fun and relieve stress (or induce it)"
        )
        self.theme_color = discord.Color.purple()
        self.eight_ball_responses = [
            [
                "No.",
                "Nope.",
                "Highly Doubtful.",
                "Not a chance.",
                "Not possible.",
                "Don't count on it.",
            ],
            [
                "Yes.",
                "Yup",
                "Extremely Likely",
                "It is possible",
                "Very possibly.",
            ],
            ["I'm not sure", "Maybe get a second opinion", "Maybe"],
        ]
  

        self.emojify_symbols = {
            "0": ":zero:",
            "1": ":one:",
            "2": ":two:",
            "3": ":three:",
            "4": ":four:",
            "5": ":five:",
            "6": ":six:",
            "7": ":seven:",
            "8": ":eight:",
            "9": ":nine:",
            "!": ":exclamation:",
            "#": ":hash:",
            "?": ":question:",
            "*": ":asterisk:",
        }
  

    
    @commands.command(
        name="coinflip", aliases=["coin", "flip"], help="Flip a coin!"
    )
    async def coin_flip(self, ctx):
        result = random.choice(["heads", "tails"])
        await ctx.send(
            f"The coin has been flipped and resulted in **{result}**"
        )

    @commands.command(name="tinyurl", aliases=["tiny"], description="URL shortening command.")
    async def tinyurl_command(self, ctx, *, url):
        if not url.startswith("http"):
            url = f"https://{url}"
        message = await ctx.send(f"Shortening **{url}**...\n")
        try:
            tinyurl_link = await get_tinyurl(url)
        except Exception as e:
            return await message.edit(content=f"Could not shorten URL.\n{e if len(str(e)) < 1024 else str(e)[:1024]}")
        await message.edit(content=f"Here is the shortened URL for **{url}**.\n{tinyurl_link}")

    @commands.command(name="roll", aliases=["dice"], help="Roll a dice!")
    async def dice_roll(self, ctx: commands.Context, dice_count: int = 1):
        number = random.randint(dice_count, dice_count * 6)

        if dice_count > 1:
            await ctx.send(
                f"You rolled **{dice_count} dice** and got a **{number}**"
            )
        else:
            await ctx.send(f"You rolled a **{number}**")
    @commands.command(
          help="Shows how much a user is gay.",
          description="`user` (Optional): The user to calculate gay rate of.",
          brief='/fun/rates',
          usage='gayrate'
          )
    async def gayrate(self, ctx, user:discord.Member = None):
        if user is None:
            user = ctx.author

        msg = await ctx.send(":thinking_face:")
        embed = discord.Embed(title=":rainbow: Gay Rate")
        embed.set_author(name=str(user), icon_url=ctx.author.avatar_url)

        rate = random.randint(0, 100)
        if random.randint(0, 100) == random.randint(0, 100):
            embed.description = "{}\n\n**INFINITY!** The gay rate of {} is so high that I can't even calculate it!".format(str(user))
            embed.set_image(url=f'https://api.toxy.ga/api/gay?avatar={user.avatar_url}')
        else: 
            embed.description = r"**{}** is **{}% gay!**".format(str(user), str(rate))

        embed.color = int(random.choice([
                    '0xff0018', 
                    '0xffa52c',
                    '0xffff41',
                    '0x008018',
                    '0x000DF9',
                    '0x86007D']), 16) # These are Pride flag colors

        await msg.edit(embed=embed)
    @commands.command(
        name="avatar",
        aliases=["av", "pfp"],
        help="Get somebody's Discord avatar",
    )
    async def avatar(
        self, ctx: commands.Context, member: discord.Member = None
    ):
        if member:
            m = member
        else:
            m = ctx.author

        av_embed = discord.Embed(title=f"{m}'s Avatar", color=self.theme_color)
        av_embed.set_image(url=m.avatar_url)
        await ctx.send(embed=av_embed)

    @commands.command(
        name="choose",
        aliases=["choice"],
        help="Let Amteor choose the best option for you. Separate the choices with a comma (,)",
    )
    async def choose(self, ctx: commands.Context, *, options: str):
        items = [
            option.strip().replace("*", "") for option in options.split(",")
        ]
        choice = random.choice(items)
        await ctx.send(
            f"I choose **{choice}**",
            allowed_mentions=discord.AllowedMentions.none(),
        )

    @commands.command(
        name="8ball",
        aliases=["8"],
        help="Call upon the powers of the all knowing magic 8Ball",
    )
    async def eight_ball(self, ctx: commands.Context, question: str):
        group = random.choice(self.eight_ball_responses)
        response = random.choice(group)

        await ctx.send(response)

    @commands.command(
        name="emojify", aliases=["emoji"], help="Turn a sentence into emojis"
    )
    async def emojify(self, ctx: commands.Context, *, sentence: str):
        emojified_sentence = ""
        sentence = sentence.lower()

        for char in sentence:
            char_lower = char.lower()

            if char_lower in string.ascii_lowercase:
                emojified_sentence += f":regional_indicator_{char}:"
            elif char_lower in self.emojify_symbols:
                emojified_sentence += self.emojify_symbols[char_lower]
            else:
                emojified_sentence += char

        await ctx.send(emojified_sentence)

    @commands.command(name="ascii", help="Turn a sentence into cool ASCII art")
    async def ascii(self, ctx: commands.Context, *, sentence: str):
        ascii_text = pyfiglet.figlet_format(sentence)
        await ctx.send(f"```{ascii_text}```")

    @commands.command(name="trivia", aliases=["quiz"], description="The bot asks a question, you answer. Simple.")
    async def trivia(self, ctx):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://opentdb.com/api.php?amount=1") as x:
                response = (await x.content.read()).decode("utf-8")
                response = json.loads(response)

        if not response.get("response_code") == 0:
            return

        results = response.get("results")[0]
        category = results.get("category").replace(
            "&quot;", "\"").replace("&#039;", "'")
        difficulty = results.get("difficulty").replace(
            "&quot;", "\"").replace("&#039;", "'")
        question = results.get("question").replace(
            "&quot;", "\"").replace("&#039;", "'")
        correctans = results.get("correct_answer").replace(
            "&quot;", "\"").replace("&#039;", "'")
        wrong_ans_list = results.get("incorrect_answers")
        answers = wrong_ans_list
        answers.append(correctans)

        random.shuffle(answers)
        correctans_index = list(answers).index(correctans) + 1
        rules=discord.Embed(title="Trivia Rules",description="The rules are simple. I will ask you a question, you choose the answer.\n"
                                         "If there are 4 options in the answer, "
                                         "you can enter \"1\", \"2\", \"3\", or \"4\".\n"
                                         "The game starts in 5 seconds.")
        message_to_edit = await ctx.send(embed=rules)
        await asyncio.sleep(5)
        await message_to_edit.edit(content=f"_{ctx.author.display_name}_, go!")
        embed = discord.Embed(title=f"Category: {category}\nDifficulty: {difficulty}",
                              color=ctx.author.color)
        embed.add_field(name=question, value="\ufeff", inline=False)

        option_string = ""
        for x in answers:
            option_str = x.replace("&quot;", "\"").replace("&#039;", "'")
            option_string += f"`{answers.index(x) + 1}.` {option_str}\n"

        embed.add_field(name="Options", value=option_string, inline=True)
        embed.set_footer(
            text=f"{ctx.author.display_name}, pick the answer! You have 20 seconds.")
        await ctx.send(embed=embed)
        try:
            message_from_user = await self.bot.wait_for("message", check=lambda message: message.author == ctx.author,
                                                        timeout=20)
        except asyncio.TimeoutError:
            return await ctx.send(f"_{ctx.author.display_name}_, Dumbass you didnt replied , We will play again later btw \n"
                                  f"The answer was **{correctans}**")

        try:
            content = int(message_from_user.content)
        except ValueError:
            content = ""
            return await ctx.send(f"_{ctx.author.display_name}_ , wrong format!\n"
                                  "You can only answer with the Index of the option you think is correct.\n"
                                  "We'll play later.")
        if content == correctans_index:
            await message_from_user.add_reaction("🎉")
            await message_from_user.reply("You won!")
        else:
            await message_from_user.add_reaction("❌")
            await message_from_user.reply(f"_{ctx.author.display_name}_, good try, "
                                          f"but that was not the correct answer.\n"
                                          f"The correct answer is **{correctans}**.")
        await ctx.send(f"Thanks for playing **Trivia**, _{ctx.author.display_name}_!")

    @commands.command()
    @commands.cooldown(rate=1, per=2.0, type=commands.BucketType.user)
    async def nitro(self, ctx, *, emoji: commands.clean_content):
        """ Allows you to use nitro emojis """
        nitromote = discord.utils.find(
            lambda e: e.name.lower() == emoji.lower(), self.bot.emojis
        )
        if nitromote is None:
            return await ctx.send(
                f":warning: | **Sorry, no matches found for `{emoji.lower()}`**"
            )
        await ctx.send(f"{nitromote}")

    @commands.command()
    @commands.guild_only()
    @commands.cooldown(rate=1, per=5.0, type=commands.BucketType.user)
    async def osu(self, ctx, osuplayer, usrhex: str = 170_041):
        """ Shows an osu! profile. """
        embed = discord.Embed(color=random.randint(0x000000, 0xFFFFFF))
        embed.set_image(
            url="http://lemmmy.pw/osusig/sig.php?colour=hex{0}&uname={1}&pp=1&countryrank&removeavmargin&flagshadow&flagstroke&darktriangles&onlineindicator=undefined&xpbar&xpbarhex".format(
                usrhex, osuplayer
            )
        )
        embed.set_footer(
            text="Powered by lemmmy.pw",
            icon_url="https://raw.githubusercontent.com/F4stZ4p/resources-for-discord-bot/master/osusmall.ico",
        )
        await ctx.send(embed=embed)





    @commands.command(description="Guess age of given name")
    async def ga(self, ctx, name):
        if name == None:
            await ctx.send("You forgot name")
        else:
            name = str(name)
            URL = f"https://api.agify.io/?name={name}"

            def check_valid_status_code(request):
                if request.status_code == 200:
                    return request.json()

                return False

            def get_age():
                request = requests.get(URL)
                data = check_valid_status_code(request)

                return data

            age = get_age()
            if not age:
                await ctx.channel.send("Couldn't get age from API. Try again later.")

            else:
                agee = str(age["age"])
                embed = discord.Embed(
                    title="Age Guess",
                    description="Guesses the age of given name!",
                    color=0xFF0000,
                )
                embed.add_field(name=name, value=f"I guess he/she is {agee} years old")
                embed.set_footer(
                    text=f"Requested By: {ctx.author.name}",
                    icon_url=f"{ctx.author.avatar_url}",
                )
                await ctx.send(embed=embed)
    
    @commands.command(name='perms', aliases=['perms_for', 'permissions'])
    @commands.guild_only()
    async def check_permissions(self, ctx, *, member: discord.Member=None):
        """A simple command which checks a members Guild Permissions.
        If member is not provided, the author will be checked."""

        if not member:
            member = ctx.author

        # Here we check if the value of each permission is True.
        perms = '\n'.join(perm for perm, value in member.guild_permissions if value)

        # And to make it look nice, we wrap it in an Embed.
        embed = discord.Embed(title='Permissions for:', description=ctx.guild.name, colour=member.colour)
        embed.set_author(icon_url=member.avatar_url, name=str(member))

        # \uFEFF is a Zero-Width Space, which basically allows us to have an empty field name.
        embed.add_field(name='\uFEFF', value=perms)

        await ctx.send(content=None, embed=embed)


def setup(bot):
    bot.add_cog(FunUtility(bot))
