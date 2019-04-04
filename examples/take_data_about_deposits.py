import urllib.request
import json

url = 'https://resources.finance.ua/ua/deposit/program?type=nat'

data = urllib.request.urlopen(url).read().decode()
# print(data)
with open('data.json', 'w', encoding='utf-8') as ff:
    # json.dumps(data, ff, ensure_ascii=False)
    print(data, file=ff)