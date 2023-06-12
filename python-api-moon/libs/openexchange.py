import requests

class OpenExchangeClient:
    BASE_URL = "https://openexchangerates.org/api"
    
    def __init__(self, app_id):
        self.app_id = app_id
        
    @property
    def latest(self):
        return requests.get(f"{self.BASE_URL}/latest.json?app_id={self.app_id}").json()
    
    def convert(self, from_amount, from_currency, to_currency):
        retes = self.latest["rates"]
        to_rate = retes[to_currency]
        
        if from_currency == "USD":
            return from_amount * to_rate
        else:
            from_in_usd = from_amount / retes[from_currency]
            return from_in_usd * to_rate
        
        