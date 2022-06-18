import asyncio
import strawpy
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
import requests
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
        heads='https://cdn.vectorstock.com/i/1000x1000/20/42/man-head-profile-gold-coin-vector-19272042.webp'
        tails='https://previews.123rf.com/images/spideyspike/spideyspike2007/spideyspike200700006/151874716-the-tail-side-of-the-coin-isolated-vector-illustration.jpg'
        e=discord.Embed(color=discord.Color.gold(),description=f"The coin has been flipped and resulted in **{result}**")
        if  result=='heads':
          e.set_thumbnail(url=heads)
        else:
          e.set_thumbnail(url=tails)
        await ctx.send(embed=e
            
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

        await msg.edit(content=None,embed=embed)
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

        av_embed = discord.Embed(title=f"{m}'s Avatar", color=m.color)
        av_embed.set_image(url=m.avatar_url)
        await ctx.send(embed=av_embed)

    @commands.command(
        name="choose",
        aliases=["choice"],
        help="Let Tessarect choose the best option for you. Separate the choices with a comma (,)",
    )
    async def choose(self, ctx: commands.Context, *, options: str):
        items = [
            option.strip().replace("*", "") for option in options.split(",")
        ]
        choice = random.choice(items)
        await ctx.send(
            f"I choose **{choice}**",
        )

    @commands.command(
        name="8ball",
        aliases=["8"],
        help="Call upon the powers of the all knowing magic 8Ball",
    )
    async def eight_ball(self, ctx,*, question: str):
        group = random.choice(self.eight_ball_responses)
        response = random.choice(group)
        em = discord.Embed(color=discord.Color.dark_theme())
        em.add_field(name='\u2753 Question', value=question)
        em.add_field(name='\ud83c\udfb1 8ball', value=response, inline=False)
        await ctx.send(content=None, embed=em)


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
                                         "The game starts in 5 seconds.",color=discord.Color.dark_theme())
        message_to_edit = await ctx.send(embed=rules)
        await asyncio.sleep(5)
        await message_to_edit.edit(content=f"{ctx.author.name}, go!")
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
        await ctx.send(embed=discord.Embed(description=f"Thanks for playing **Trivia**, _{ctx.author.display_name}_!",color=discord.Color.blue()))

    @commands.command()
    @commands.cooldown(rate=1, per=2.0, type=commands.BucketType.user)
    async def getemoji(self, ctx, *, emoji: commands.clean_content):
        """ Allows you to get emojis from all my servers """
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
                    color=discord.Color.dark_purple(),
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

    # Embeds the message
    @commands.command(pass_context=True)
    async def embed(self, ctx, *, msg: str = None):
        """
        ```
        ```md
        Embed given text. Ex: Do [p]embed for more help
        Example: [p]embed title=test this | description=some words | color=3AB35E | field=name=test value=test
        You do NOT need to specify every property, only the ones you want.
        **All properties and the syntax:**
        - title=<words>
        - description=<words>
        - color=<hex_value>
        - image=<url_to_image> (must be https)
        - thumbnail=<url_to_image>
        - author=<words> **OR** author=name=<words> icon=<url_to_image>**OR** author=self=yes 
        - footer=<words> **OR** footer=name=<words> icon=<url_to_image>
        - field=name=<words> value=<words> (you can add as many fields as you want)
        - ptext=<words>
        NOTE: After the command is sent, the bot will delete your message and replace it with the embed. Make sure you have it saved or else you'll have to type it all again if the embed isn't how you want it.
        
        PS: Hyperlink text like so:
        \[text](https://www.whateverlink.com)
        PPS: Force a field to go to the next line with the added parameter inline=False
        """
        
        if msg:
            if 1==1:
                ptext = title = description = image = thumbnail = color = footer = author = None
                timestamp = discord.Embed.Empty
                embed_values = msg.split('|')
            
                for i in embed_values:
                    color='27007A'
                    if i.strip().lower().startswith('ptext='):
                        ptext = i.strip()[6:].strip()
                    elif i.strip().lower().startswith('title='):
                        title = i.strip()[6:].strip()
                    elif i.strip().lower().startswith('description='):
                        description = i.strip()[12:].strip()
                    elif i.strip().lower().startswith('desc='):
                        description = i.strip()[5:].strip()
                    elif i.strip().lower().startswith('image='):
                        image = i.strip()[6:].strip()
                    elif i.strip().lower().startswith('thumbnail='):
                        thumbnail = i.strip()[10:].strip()
                    elif i.strip().lower().startswith('colour='):
                        color = i.strip()[7:].strip()
                    elif i.strip().lower().startswith('color='):
                        color = i.strip()[6:].strip()
                    elif i.strip().lower().startswith('footer='):
                        footer = i.strip()[7:].strip()
                    elif i.strip().lower().startswith('author='):
                        author = i.strip()[7:].strip()
                     
                    elif i.strip().lower().startswith('timestamp'):
                        timestamp = ctx.message.created_at
                    else:
                        if description is None and not i.strip().lower().startswith('field='):
                            description = i.strip()
                
                if color:
                    if color.startswith('#'):
                        color = color[1:]
                    if not color.startswith('0x'):
                        color = '0x' + color

                  

                if ptext is title is description is image is thumbnail is color is footer is author is None and 'field=' not in msg:
                    await ctx.message.delete()
                    return await ctx.send(content=None,
                                                       embed=discord.Embed(description=msg))

                if color:
                    em = discord.Embed(timestamp=timestamp, title=title, description=description, color=int(color, 16))
                else:
                    em = discord.Embed(timestamp=timestamp, title=title, description=description)
                for i in embed_values:
                    if i.strip().lower().startswith('field='):
                        field_inline = True
                        field = i.strip().lstrip('field=')
                        field_name, field_value = field.split('value=')
                        if 'inline=' in field_value:
                            field_value, field_inline = field_value.split('inline=')
                            if 'false' in field_inline.lower() or 'no' in field_inline.lower():
                                field_inline = False
                        field_name = field_name.strip().lstrip('name=')
                        em.add_field(name=field_name, value=field_value.strip(), inline=field_inline)
                if author:

                    if 'icon=' in author:
                        text, icon = author.split('icon=')
                        if 'url=' in icon:
                            em.set_author(name=text.strip()[5:], icon_url=icon.split('url=')[0].strip(), url=icon.split('url=')[1].strip())
                        else:
                            em.set_author(name=text.strip()[5:], icon_url=icon)
                    elif 'self=' in author:
                      ch=author.split('self=')

                      if ch[1]=='yes':
                        em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)                            
                    else:
                        if 'url=' in author:
                            em.set_author(name=author.split('url=')[0].strip()[5:], url=author.split('url=')[1].strip())
                        else:
                            em.set_author(name=author)

                if image:
                    em.set_image(url=image)
                if thumbnail:
                    em.set_thumbnail(url=thumbnail)
                if footer:
                    if 'icon=' in footer:
                        text, icon = footer.split('icon=')
                        em.set_footer(text=text.strip()[5:], icon_url=icon)
                    else:
                        em.set_footer(text=footer)
                await ctx.send(content=ptext, embed=em)
            else:
                await ctx.send('No embed permissions in this channel.')
        else:
            msg = '```How to use the [p]embed command:\nExample: [p]embed title=test this | description=some words | color=3AB35E | field=name=test value=test\n\nYou do NOT need to specify every property, only the ones you want.' \
                  '\nAll properties and the syntax (put your custom stuff in place of the <> stuff):\ntitle=<words>\ndescription=<words>\ncolor=<hex_value>\nimage=<url_to_image> (must be https)\nthumbnail=<url_to_image>\nauthor=<words> **OR** author=name=<words> icon=<url_to_image>\nfooter=<words> ' \
                  '**OR** footer=name=<words> icon=<url_to_image>\nfield=name=<words> value=<words> (you can add as many fields as you want)\nptext=<words>\n\nNOTE: After the command is sent, the bot will delete your message and replace it with ' \
                  'the embed. Make sure you have it saved or else you\'ll have to type it all again if the embed isn\'t how you want it.\nPS: Hyperlink text like so: [text](https://www.whateverlink.com)\nPPS: Force a field to go to the next line with the added parameter inline=False```'
            await ctx.send(embed=discord.Embed(description=msg))
        try:
          await ctx.message.delete()
        except:
          return
           
    @commands.has_permissions(add_reactions=True)
    @commands.command(pass_context=True,aliases=['rpoll'])
    async def poll(self, ctx, *, msg):
        """Create a poll using reactions. [p]help rpoll for more information.
        [p]rpoll <question> | <answer> | <answer> - Create a poll. You may use as many answers as you want, placing a pipe | symbol in between them.
        Example:
        [p]rpoll What feature is your favourite? | Economy | Ticket | Fun | AI | Other
        You can also add `time=<some integer (in seconds)>` to end the poll , default is Forever
        """
        
        options = msg.split(" | ")
        time = [x for x in options if x.startswith("time=")]
        if time:
            time = time[0]
        if time:
            options.remove(time)
        if len(options) <= 1:
            return await ctx.send( "You must have 2 options or more.")
        if len(options) >= 11:
            return await ctx.send( "You must have 9 options or less.")
        if time:
            time = int(time.strip("time="))
        else:
            time = 'Forever'
        emoji = ['1⃣', '2⃣', '3⃣', '4⃣', '5⃣', '6⃣', '7⃣', '8⃣', '9⃣']
        to_react = []
        confirmation_msg = "**{}?**:\n\n".format(options[0].rstrip("?"))
        for idx, option in enumerate(options[1:]):
            confirmation_msg += "{} - {}\n".format(emoji[idx], option)
            to_react.append(emoji[idx])
        confirmation_msg += "\n\nYou have {} seconds to vote!".format(time)
        poll_msg = await ctx.send(embed=discord.Embed(description=confirmation_msg,color=discord.Color.dark_theme()))
        for emote in to_react:
            await poll_msg.add_reaction(emote)
        print(time)
        if not time=="Forever":
          await asyncio.sleep(time)
          async for message in ctx.message.channel.history():
              if message.id == poll_msg.id:
                  poll_msg = message
          results = {}
          for reaction in poll_msg.reactions:
              if reaction.emoji in to_react:
                  results[reaction.emoji] = reaction.count - 1
          end_msg = "The poll is over. The results:\n\n"
          for result in results:
              end_msg += "{} {} - {} votes\n".format(result, options[emoji.index(result)+1], results[result])
          top_result = max(results, key=lambda key: results[key])
          if len([x for x in results if results[x] == results[top_result]]) > 1:
              top_results = []
              for key, value in results.items():
                  if value == results[top_result]:
                      top_results.append(options[emoji.index(key)+1])
              end_msg += "\nThe victory is tied between: {}".format(", ".join(top_results))
          else:
              top_result = options[emoji.index(top_result)+1]
              end_msg += "\n**{}** is the winner!".format(top_result)
          await ctx.send(embed=discord.Embed(description=end_msg,color=discord.Color.dark_theme()))          
          await ctx.message.delete()
def setup(bot):
    bot.add_cog(FunUtility(bot))
