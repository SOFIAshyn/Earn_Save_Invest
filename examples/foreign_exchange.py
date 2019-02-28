from alpha_vantage.foreignexchange import ForeignExchange
from pprint import pprint
cc = ForeignExchange(key='ODNW5DM6YQ581D1A')
# There is no metadata in this call
data, _ = cc.get_currency_exchange_rate(from_currency='UAH',to_currency='USD')
pprint(data)


# {'1. From_Currency Code': 'UAH',
#  '2. From_Currency Name': 'Ukrainian Hryvnia',
#  '3. To_Currency Code': 'USD',
#  '4. To_Currency Name': 'United States Dollar',
#  '5. Exchange Rate': '0.03700962',
#  '6. Last Refreshed': '2019-02-28 17:00:15',
#  '7. Time Zone': 'UTC'}
