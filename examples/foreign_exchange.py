from alpha_vantage.foreignexchange import ForeignExchange
from pprint import pprint
cc = ForeignExchange(key='ODNW5DM6YQ581D1A')
# There is no metadata in this call
data, _ = cc.get_currency_exchange_rate(from_currency='UAH',to_currency='USD')
pprint(data)
