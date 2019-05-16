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
        update the Banks: their indexes, titles, programs, etc.
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
        """
        method for parsing programs of banks
        :param program: current program
        :return: list of Program instances
        """
        res = []
        for each in program:
            res.append(Program(each["id_condition"], each['title'],
                               each['link'], each['currency_diapasons_rates']))
        return res

    def banks_processing(self):
        self.update_information()
        res = sorted(self.update_instance(),
                     key=lambda x: float(x.index))[::-1]
        # for b in res:
        #     print(b)
        return res


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
        self.index += float(self.rating) * self.coeffs['rating']
        self.programs = [each for each in self.programs if each.find_best() is not None]
        
        print(self, '\n', sorted(self.programs, key=lambda x: x.find_best()[3])[-1])
        # for each in self.programs:
        #     print(each.find_best())


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
        # self.find_best(self.UAH_rates)

    def __repr__(self):
        return '{}'.format(self.title)

    def find_best(self):
        currency = self.UAH_rates
        year = 12
        res = []
        for each in currency:
            # min_invest = float(each[0])
            min_invest = float(10000000)
            num_of_years = 1
            for months in each[1]:
                num_of_adds = year / float(months)
                year_rate = float(each[1][months])
                n = num_of_years * num_of_adds
                result = round(min_invest * (1 + year_rate / 100 / num_of_adds)
                               ** n, 2)
                res.append([float(each[0]), months, min_invest, result])
        if not res:
            return None
        return (sorted(res, key=lambda x: x[2]))[-1]

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
