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
                     key=lambda x: float(x.rating))[::-1]
        # for b in res:
        #     print(b)
        # return res


class Bank:
    def __init__(self, title, link, programs, index):
        self.title = title
        self.link = link
        self.programs = programs
        self.rating = index
        self.coeffs = {
            'rating': .5,
            'programs': .1,
            'rates': .4
            }
        self.index = 0
        self.update()

    def __repr__(self):
        return 'Bank: < {}, rating: {},  Programs: {}>'.format(self.title,
                                                               self.rating,
                                                               self.programs)

    def update(self):
        self.index += len(self.programs) * self.coeffs['programs']


class Program:
    def __init__(self, condition, title, link, rates):
        self.condition = condition
        self.title = title
        self.link = link
        self.EUR_rates = []
        self.UAH_rates = []
        self.USD_rates = []
        self.rates = self.transform_rates(rates)
        # print(self.UAH_rates)
        self.find_minimum(self.UAH_rates)

    def __repr__(self):
        return '{}'.format(self.title)

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
                if current[-1] is []:
                    current.pop(-1)
        return current

    # @staticmethod
    # def percentage(summ, percent):
    #     return float(summ) * float(percent) / 100

    def find_minimum(self, currency):
        year = 12
        res = []
        for each in currency:
            min_invest = float(each[0])
            for months in each[1]:
                num_of_months = year / float(months)
                t = float(each[1][months])/100/float(num_of_months)
                a = round(min_invest * ((1 + t)**float(num_of_months)), 2)

                res.append([min_invest, months, a])

        return res
