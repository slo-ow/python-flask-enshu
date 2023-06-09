import requests

APP_ID = "f70b4ffc85ee4d3fb79be4528df07a3f"
ENDPOINT = "https://openexchangerates.org/api/latest.json"

response = requests.get(f"{ENDPOINT}?app_id={APP_ID}")
exchange_rates = response.json()["rates"]

usd_amount = 1
jpy_amout = usd_amount * exchange_rates["JPY"]

print(f"USD {usd_amount} is JPY {jpy_amout}")