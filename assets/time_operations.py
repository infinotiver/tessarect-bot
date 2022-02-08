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
    with open("./storage/time_files/time_offset.json", 'r') as jsonFile:
        data_offset = json.load(jsonFile)

    with open("./storage/time_files/time_tz.json", 'r') as jsonFile:
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