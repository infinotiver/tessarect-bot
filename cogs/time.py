'''concept by Code-Cecilia/BotMan.py
'''
import ast
import asyncio
import json
import os
import re

import aiohttp
import discord
from discord.ext import commands
import json
import re

import discord


def format_time(time: str):
    am_pm = "AM"
    time_hours = int(time[:2])
    time_minutes = int(time[3:])
    if time_hours >= 12:
        time_hours -= 12
        am_pm = "PM"
    if len(str(time_hours)) == 1:
        time_hours = f"0{time_hours}"
    if len(str(time_minutes)) == 1:
        time_minutes = f"0{time_minutes}"
    return f"{time_hours}:{time_minutes} {am_pm}"


def check_if_offset_or_api(string: str):
    pattern = r'^[+\-]+\d+:\d+$'
    if re.match(pattern, string):
        return True
    else:
        return False


async def check_time(user: discord.Member):
    with open("storage/time_files/time_offset.json", 'r') as jsonFile:
        data_offset = json.load(jsonFile)

    with open("storage/time_files/time_tz.json", 'r') as jsonFile:
        data_tz = json.load(jsonFile)

    pattern = r'^[+\-]+\d+:\d+$'

    offset_user = data_offset.get(str(user.id))
    tz_user = data_tz.get(str(user.id))

    if re.match(pattern, str(offset_user)):
        offset_bool = True
    else:
        offset_bool = False

    if tz_user is not None:
        timezone_bool = True
    else:
        timezone_bool = False

    return offset_bool, timezone_bool
import datetime


def time_bm(timezone):
    now = datetime.datetime.utcnow()

    if timezone is None:
        return now
    else:
        time_offsets = [int(value) for value in timezone.split(':')]
        if len(time_offsets) == 2:
            now += datetime.timedelta(hours=time_offsets[0],
                                      minutes=time_offsets[1] * (-1 if (time_offsets[0] < 0) else 1))
        else:
            now += datetime.timedelta(hours=time_offsets[0])
        final_time = str(now)[11:16]
        return final_time
def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]           

time_link = 'https://worldtimeapi.org/api/timezone/'


class Time(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='time', description='Gets the time from a location, or using the offset. '
                                               'Use the `settz` and `setoffset` commands for setting this up.')
    @commands.guild_only()
    async def time_user(self, ctx, user: discord.Member = None):
        if user is None:
            user = ctx.author

        is_offset, is_tz = await check_time(user)

        if not is_offset and not is_tz:
            return await ctx.send(f"{user.display_name} has not set their timezone. "
                                  f"They can do so with the `settz` or `setoffset` commands.")

        if is_tz:  # check if user has set their timezone, and get the data
            with open('storage/time_files/time_tz.json', 'r') as timeFile:
                data = json.load(timeFile)
                user_timezone = data.get(str(user.id))
            if user_timezone is None:
                return await ctx.send(f"{ctx.author.display_name} has not set their timezone. "
                                      f"They can do so with the `settz` command.")

            timezone_link = f"{time_link}{user_timezone}"
            async with aiohttp.ClientSession() as session:
                async with session.get(timezone_link) as response:
                    response_dict = (await response.content.read()).decode('utf-8')
                    response_dict = json.loads(response_dict)
            if response_dict.get('error') == "unknown location":
                return await ctx.send(
                    "Unknown timezone name. Check the `tzlist` command for a list of valid timezones.\n")

            if response_dict.get('datetime') is None:
                return await ctx.send(f'Couldn\'t get time data for **{user_timezone}**. '
                                      f"Check the `tzlist` command for a list of valid timezones.\n")

            time = response_dict.get('datetime')[11:16]
            actual_timezone = response_dict.get('timezone')

            time_formatted = format_time(time)

            final_string = f"`{actual_timezone}`, where **{user.display_name}** is, it's **{time_formatted}**. Note if you see 00:<something>pm it means it is 12 pm + some minutes"
            return await ctx.send(final_string)
            # since we have the "return" statement, none of the below code
            # in this command will get executed if is_tz is true.

        if is_offset:  # check for offset and get the data
            with open('storage/time_files/time_offset.json', 'r') as timeFile:
                time_data = json.load(timeFile)

            user_offset = time_data.get(str(ctx.author.id))
            time_unformatted = time_bm(user_offset)
            time_formatted = format_time(time_unformatted)
            await ctx.send(f"UTC{user_offset}, where **{user.display_name}** is, it's **{time_formatted}**.")

    @commands.command(name='settz',
                      description='Sets the timezone. Check the `tzlist` command for a list of timezones.')
    async def set_timezone_from_api(self, ctx, timezone: str.lower):
        timezone_link = f"{time_link}{timezone}"
        async with aiohttp.ClientSession() as session:
            async with session.get(timezone_link) as response:
                response_dict = (await response.content.read()).decode('utf-8')
                response_dict = json.loads(response_dict)
        # invalid timezones have this entry in the json response
        if response_dict.get('error') == "unknown location":
            return await ctx.send('Unknown timezone name. Check the `tzlist` command for a list of timezones.\n')

        if response_dict.get('datetime') is None:
            return await ctx.send(f'Couldn\'t get time data for **{timezone}**. '
                                  f'Check the `tzlist` command for a list of valid timezones.\n')

        if not os.path.exists('storage/time_tz.json'):  # create file if not exists
            with open('storage/time_files/time_tz.json', 'w') as jsonFile:
                json.dump({}, jsonFile)

        with open('storage/time_files/time_tz.json', 'r') as timeFile:
            time_data = json.load(timeFile)

        time_data[str(ctx.author.id)] = timezone

        with open('storage/time_files/time_tz.json', 'w') as timeFile:
            json.dump(time_data, timeFile)

        await ctx.send(f'Timezone set as {timezone.title()} successfully.')

        with open('storage/time_files/time_offset.json', 'r') as timeFile:
            offset_data = json.load(timeFile)

        offset_data.pop(str(ctx.author.id))
        # when user sets time location, the offset value is deleted

        with open('storage/time_files/time_offset.json', 'w') as timeFile:
            json.dump(offset_data, timeFile, indent=4)

        await ctx.send('Removed offset entry because you\'re using the location format now.')

    @commands.command(name='setoffset', description='Sets the user\'s time offset.\n'
                                                    'Format for offset: `-2:30` and `+2:30`\n'
                                                    '**Nerd note**: the regex for the offset is '
                                                    r'`^[+\-]+\d+:\d+$`')
    async def set_offset(self, ctx, offset):
        pattern = r'^[+\-]+\d+:\d+$'
        # matches the pattern, and if it fails, returns an error message
        if not re.match(pattern, offset):
            return await ctx.send('Improper offset format. Please read the help command for more info.')

        # create file if not exists
        if not os.path.exists('storage/time_files/time_offset.json'):
            with open('storage/time_files/time_offset.json', 'w') as jsonFile:
                json.dump({}, jsonFile)

        with open('storage/time_files/time_offset.json', 'r') as timeFile:
            time_data = json.load(timeFile)

        time_data[str(ctx.author.id)] = offset

        with open('storage/time_files/time_offset.json', 'w') as timeFile:
            json.dump(time_data, timeFile)

        await ctx.send(f'Time offset set as {offset} successfully.')

        with open('storage/time_files/time_tz.json', 'r') as timeFile:
            tz_data = json.load(timeFile)
        tz_data.pop(str(ctx.author.id))
        # delete the time location value because offset is set
        with open('storage/time_files/time_tz.json', 'w') as timeFile:
            json.dump(tz_data, timeFile, indent=4)

        await ctx.send("Removed the location entry because you\'re using the offset format now.")

    @commands.command(name='tzlist', aliases=['listtz', 'timezones'],
                      description='Gets the list of timezones available')
    async def get_tz_list(self, ctx):
        author = ctx.author

        async with aiohttp.ClientSession() as session:
            async with session.get(time_link) as response:
                response_list = (await response.content.read()).decode('utf-8')
                response_list = ast.literal_eval(response_list)

        chunk_list = list(chunks(response_list, 24))

        try:
            await author.send('**__Here\'s a list of timezones to choose from.__**')
            await ctx.message.add_reaction("📬")
        except:
            return await ctx.send('Could not send PM to you. '
                                  'Please check your settings to allow me to send messages to you.')
        for i in chunk_list:
            to_send = "\n".join(i)
            await author.send(f'```{to_send}```')
            await asyncio.sleep(1)

    @commands.command(name="timeinfo", description="Gets a list of time information for a specific location.\n"
                                                   "Argument passed in must one of the "
                                                   "locations in the `tzlist` command.")
    async def get_time_info(self, ctx, location: str.lower):
        timezone_link = f"{time_link}{location}"
        async with aiohttp.ClientSession() as session:
            async with session.get(timezone_link) as response:
                response_dict = (await response.content.read()).decode('utf-8')
                response_dict = json.loads(response_dict)
        if response_dict.get('error') == "unknown location":
            return await ctx.send(
                'Unknown timezone name. Check the `tzlist` command for a list of valid timezones.\n')

        if response_dict.get('datetime') is None:
            return await ctx.send(f'Couldn\'t get time data for **{location}**. '
                                  f'Check the `tzlist` command for a list of valid timezones.\n')

        time = response_dict.get('datetime')[11:19]
        date = response_dict.get('datetime')[:10]
        actual_timezone = response_dict.get('timezone')
        day_of_week = response_dict.get("day_of_week")
        day_of_year = response_dict.get("day_of_year")
        offset = response_dict.get("utc_offset")
        week = response_dict.get("week_number")
        abbreviation = response_dict.get("abbreviation")
        utc_datetime = response_dict.get("datetime")

        embed = discord.Embed(title=f"Time info for {actual_timezone}",
                              description=f"Abbreviation: **{abbreviation}** | UTC Offset: **{offset}**",
                              color=discord.Color.random())
        embed.add_field(name="Time", value=time, inline=True)
        embed.add_field(name="Date", value=date, inline=True)
        embed.add_field(name="Weeks since Jan 1", value=week, inline=True)
        embed.add_field(name="Day of the week", value=day_of_week, inline=True)
        embed.add_field(name="Day of the year", value=day_of_year, inline=True)
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/716649261449740329/884317624090116096/giphy-downsized-large.gif")
        embed.set_footer(text=f"UTC format: {utc_datetime}")

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Time(bot))