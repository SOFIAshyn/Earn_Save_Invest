import urllib.request
import json


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
        with open('modules/bank/data.json', 'w', encoding='utf-8') as ff:
            print(data, file=ff)
        with open('modules/bank/data.json', 'r') as ff:
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
            if not b['index']:
                continue
            res.append(Bank(b["title"],
                            b["link"],
                            self.parse_programs(each["programs"]),
                            b['index']))
        return res

    @staticmethod
    def parse_programs(program):
        res = []
        for each in program:
            res.append(Program(each["id_condition"], each['title'],
                               each['link'], each['currency_diapasons_rates']))
        return res

    def banks_processing(self):
        self.update_information()
        res = sorted(self.update_instance(),
                     key=lambda x: float(x.rating))[-1:-14:-1]
        return res


class Bank:
    def __init__(self, title, link, programs, index):
        self.title = title
        self.link = link
        self.programs = programs
        self.rating = index

    def __repr__(self):
        return 'Bank < {}, {} >'.format(self.title, self.rating)


class Program:
    def __init__(self, id_condition, title, link, rates):
        self.id_condition = id_condition
        self.title = title
        self.link = link
        self.EUR_rates = []
        self.UAH_rates = []
        self.USD_rates = []
        self.transform_rates(rates)

    def __repr__(self):
        pass

    def transform_rates(self, rates):
        for each in rates:
            if each == 'EUR':
                current = self.EUR_rates
            elif each == 'UAH':
                current = self.UAH_rates
            else:
                current = self.USD_rates

            for el in rates[each]['diapasons']:
                current.append([el['diapason'], el['rates']])
