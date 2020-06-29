#%%
from datetime import date, timedelta
from pprint import pprint

import requests


def get_ratings(currencies, days=30): # list of currencies
    end_date = date.today()
    start_date = end_date - timedelta(days=days)

    symboles = ','.join(currencies)
    requete = f"https://api.exchangeratesapi.io/history?start_at={start_date}&end_at={end_date}&symbols={symboles}"
    r = requests.get(requete)

    if not r and not r.json(): # order is important as the 2nd condition is not evaluated if 1st one is False
        return False, False

    api_rates = r.json().get("rates")
    all_rates = {currency: [] for currency in currencies} # dict init
    all_days = sorted(api_rates.keys()) # dict keys not sorted in previous versions python

    for each_day in all_days:
        [all_rates[currency].append(rate) for currency, rate in api_rates[each_day].items()]

    return all_days, all_rates

if __name__ == "__main__":
    days, rates = get_ratings(['USD', 'CHF'])
    pprint(days)
    pprint(rates)


# %%
