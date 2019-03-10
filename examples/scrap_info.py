import urllib.request
import json
import matplotlib.pyplot as plt

url_start = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange' \
            '?valcode=USD&date='

result = {}
for year in range(2006, 2019):
    for month in range(1, 13):
        print(year, month)
        for day in range(1, 29):
            date = str(year) + str(month).zfill(2) + str(day).zfill(2)
            url = url_start + date + '&json'
            data = urllib.request.urlopen(url).read()
            data = json.loads(data.decode('utf-8'))
            # result.append((data[0]['rate'],
            #                float(str(year) + str(int(month) * 8.3))))
            result[str(year) + str(int(month)) + str(int(day))] = str(data[0][
                                                                          'rate'])

with open('new_txt', 'w') as ff:
    json.dump(result, ff)
# plt.plot([i[1] for i in result], [i[0] for i in result], 'ro')
# plt.axis([201000, 201900, 2, 40])
# plt.show()
