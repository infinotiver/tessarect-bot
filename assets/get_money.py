import aiohttp
import json

import os

api_key = os.environ['currency_api_key']

link = f"http://api.exchangeratesapi.io/v1/latest?access_key={api_key}"


async def get_converted_currency(value, from_currency, to_currency):
    async with aiohttp.ClientSession() as session:
        async with session.get(link) as response:
            response = (await response.content.read()).decode('utf-8')
    response_dict = json.loads(response)
    rates_dict = response_dict.get('rates')
    base = response_dict.get('base')
    base_value = rates_dict.get(base)

    if rates_dict.get(from_currency) is None or rates_dict.get(to_currency) is None:
        return "One or more currency codes are invalid. Please check the help command for more info."

    from_currency_ratio = float(rates_dict.get(
        from_currency)) / float(base_value)
    to_currency_ratio = float(rates_dict.get(to_currency)) / float(base_value)
    value_to_multiply = from_currency_ratio / to_currency_ratio

    final_value = round(value / value_to_multiply, 2)
    final_string = f"`{value}` {from_currency} --> `{final_value}` {to_currency}"

    return final_string