import urllib.request
import json
from modules.bank.one_bank import *


class BankType:
    """
    Class for representation bank instance
    """

    def __init__(self):
        self.info = None
        self.conditions = None

    def update_information(self):
        """
        update information from the Internet
        """
        url = 'https://resources.finance.ua/ua/deposit/program?type=nat'
        data = urllib.request.urlopen(url).read().decode()
        with open('data.json', 'w', encoding='utf-8') as ff:
            print(data, file=ff)
        with open('data.json', 'r') as ff:
            data = json.load(ff)
        self.info = data
        self.conditions = data['conditions']

    def update_instance(self):
        """
        update the Banks
        :return: list of Bank instances
        """
        res = []
        banks = self.info['banks']
        for each in banks:
            b = each["bank"]
            res.append(Bank(b["title"],
                            b["link"],
                            self.parse_programs(each["programs"])))
        return res

    def parse_programs(self, program):
        # print(program)
        return 0