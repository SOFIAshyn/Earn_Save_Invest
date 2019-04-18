import urllib.request
import json
import modules.tree


class Bank:
    """
    Class for representation bank instance
    """
    def __init__(self):
        self.id_org = None
        self.title = None
        self.programs = None
        self.info = None

    def __str__(self):
        pass

    def update_information(self):
        url = 'https://resources.finance.ua/ua/deposit/program?type=nat'
        data = urllib.request.urlopen(url).read().decode()
        with open('data.json', 'w', encoding='utf-8') as ff:
            print(data, file=ff)
        with open('data.json', 'r') as ff:
            data = json.load(ff)
        self.info = data

    def update_instance(self):
        banks = self.info['banks']
        print(banks)


b = Bank()
b.update_information()
b.update_instance()




