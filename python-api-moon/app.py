from libs.openexchange import OpenExchangeClient

APP_ID = "f70b4ffc85ee4d3fb79be4528df07a3f"

client = OpenExchangeClient(APP_ID)

usd_amount = 1
jpy_amount = client.convert(usd_amount, "USD", "JPY")

print(f"USD {usd_amount} is JPY {jpy_amount:.2f}")