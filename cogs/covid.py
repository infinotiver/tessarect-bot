import ast
import datetime

import discord
from discord.ext import commands
def get_time(time):
    if time is not None:
        if time[-1] == 'd':
            time_final = int(time[-1]) * 3600*24
        elif time[-1] == 'h':
            time_final = int(time[:-1]) * 3600
        elif time[-1] == 'm':
            time_final = int(time[:-1]) * 60
        elif time[-1] == 's':
            time_final = int(time[:-1])
        else:
            time_final = int(time)
        return time_final


def parse_utc(utc_str: str):
    date = utc_str[:10]
    time = utc_str[11:19]
    return date, time


def time_suffix(time):
    if time is not None:
        if time[-1] == 'd':
            final_thing = str(time)[:-1] + ' days'
        elif time[-1] == 'h':
            if not time[:-1] == '1':
                final_thing = str(time)[:-1] + ' hours'
            else:
                final_thing = str(time)[:-1] + ' hour'
        elif time[-1] == 'm':
            if not time[:-1] == '1':
                final_thing = str(time)[:-1] + ' minutes'
            else:
                final_thing = str(time)[:-1] + ' minute'
        elif time[-1] == 's':
            if time[:-1] == '1':
                final_thing = str(time)[:-1] + ' second'
            else:
                final_thing = str(time)[:-1] + ' seconds'
        else:
            if time == '1':
                final_thing = str(time) + ' second'
            else:
                final_thing = str(time) + ' seconds'
        return final_thing
import aiohttp


async def aiohttp_get(url: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            response = (await response.content.read()).decode('utf-8')
            return response


async def aiohttp_get_binary(url: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            response = (await response.content.read())
            return response


async def aiohttp_post(url: str, data: dict = None, params: dict = None):
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=data, params=params) as response:
            response = (await response.content.read()).decode('utf-8')
            return response


async def aiohttp_post_binary(url: str, data: dict = None, params: dict = None):
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=data, params=params) as response:
            response = (await response.content.read())
            return response


class Covid(commands.Cog, description="<:sucess:935052640449077248> Get Covid-19 stats worldwide, or for a specific country"):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="covidstats", aliases=["coronastats", "corona", "covid"],
                      description="Returns status of Covid-19 worldwide")
    async def corona_stats(self, ctx, country: str = None):
        if country is None:
            track_url = "https://disease.sh/v3/covid-19/all"
        else:
            track_url = f"https://disease.sh/v3/covid-19/countries/{country}?strict=true"
        response_dict = await aiohttp_get(track_url)
        response_dict = ast.literal_eval(response_dict)

        if response_dict.get("message") == "Country not found or doesn't have any cases":
            return await ctx.send("Country not found or doesn't have any cases.")

        time_unix = response_dict.get("updated") / 1000
        time_utcformat = datetime.datetime.utcfromtimestamp(time_unix)

        updated_date, updated_time = parse_utc(str(time_utcformat))
        total_cases = response_dict.get("cases")
        today_cases = response_dict.get("todayCases")
        total_deaths = response_dict.get("deaths")
        affectedCountries = response_dict.get("affectedCountries")
        today_deaths = response_dict.get("todayDeaths")
        total_recovered = response_dict.get("recovered")
        today_recovered = response_dict.get("todayRecovered")
        active_cases = response_dict.get("active")
        critical_cases = response_dict.get("critical")
        cases_per_million = response_dict.get("casesPerOneMillion")
        deaths_per_million = response_dict.get("deathsPerOneMillion")
        total_tests = response_dict.get("tests")
        population = response_dict.get("population")
        active_per_million = response_dict.get("activePerOneMillion")
        recovered_per_million = response_dict.get("recoveredPerOneMillion")
        critical_per_million = response_dict.get("criticalPerOneMillion")

        virus_image_url = "https://cdn.who.int/media/images/default-source/mca/mca-covid-19/coronavirus-2.tmb-1920v.jpg?sfvrsn=4dba955c_6%201920w"
        country_name = response_dict.get(
            "country")  # not used in worldwide stats
        try:
            country_flag_url = response_dict.get("countryInfo").get("flag")
        except AttributeError:
            country_flag_url = virus_image_url
            pass

        if country is None:
            embed = discord.Embed(title="Covid-19 Stats Worldwide",
                                  description=f"Lasted Updated **{updated_date}** at **{updated_time} UTC+0**",
                                  color=discord.Color.blue())
            embed.set_thumbnail(url=virus_image_url)
        else:
            embed = discord.Embed(title=f"Covid-19 Stats in {country_name}",
                                  description=f"Updated **{updated_date}** at **{updated_time} UTC+0**",
                                  color=discord.Color.dark_red())
            embed.set_thumbnail(url=country_flag_url)
        embed.add_field(name="Total cases", value='{:,}'.format(total_cases), inline=True)
        embed.add_field(name="New Cases Today", value='{:,}'.format(today_cases), inline=True)
        embed.add_field(name="Cases per Million",
                        value='{:,}'.format(cases_per_million), inline=True)

        embed.add_field(name="Total Deaths", value='{:,}'.format(total_deaths), inline=True)
        embed.add_field(name="Deaths Today", value='{:,}'.format(today_deaths), inline=True)
        embed.add_field(name="Deaths per Million",
                        value=deaths_per_million, inline=True)

        embed.add_field(name="Active cases", value=active_cases, inline=True)
        embed.add_field(name="Active per Million",
                        value=active_per_million, inline=True)

        embed.add_field(name="Critical Cases",
                        value=critical_cases, inline=True)
        embed.add_field(name="Critical per Million",
                        value=critical_per_million, inline=True)

        embed.add_field(name="Recovered", value=total_recovered, inline=True)
        embed.add_field(name="Recovered Today",
                        value=today_recovered, inline=True)
        embed.add_field(name="Recovered per Million",
                        value=recovered_per_million, inline=True)

        embed.add_field(name="Total Tests", value=total_tests, inline=False)

        if country is None:
            embed.add_field(name="World Population",
                            value=population, inline=True)
            embed.add_field(name="Affected countries",value=affectedCountries,inline=True)
        else:
            embed.add_field(
                name=f"Population of {country_name}", value=population, inline=True)

        embed.set_footer(text=f"Powered by disease.sh")

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Covid(bot))