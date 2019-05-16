import urllib.request
import json


class BankType:
    """
    Class for representation bank instance
    """

    def __init__(self, cur_incomes):
        self.info = None
        self.conditions = None
        self.cur_incomes = cur_incomes

    def update_information(self):
        """
        update information from the Internet
        """
        url = 'https://resources.finance.ua/ua/deposit/program?type=nat'
        #########################################################################
        # data = urllib.request.urlopen(url).read().decode()
        # with open('modules/bank/data.json', 'w', encoding='utf-8') as ff:
        #     print(data, file=ff)
        #########################################################################
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
                            b['index'],
                            self.cur_incomes))
        return res

    @staticmethod
    def parse_programs(program):
        """
        method for parsing each program from the banks
        :param program:
        :return:
        """
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
        """
        method for processing the info about the bank
        """
        self.update_information()
        res = sorted(self.update_instance(),
                     key=lambda x: float(x.index))[::-1]
        return res


class Bank:
    """
    class for representing Bank instance
    """

    def __init__(self, title, link, programs, index, cur_incomes):
        self.title = title
        self.link = link
        self.programs = programs
        self.rating = index
        self.current_incomes = cur_incomes
        self.coeffs = {
            'rating': .5,
            'programs': .2,
            'rates': .2
            }
        self.index = 0
        self.update()
        self.best_prog = self.find_best_program()
        self.index = round(self.index, 2)

    def __str__(self):
        if self.best_prog:
            return '{}, найкраща для вас програма - {}, посилання: \n{}'.format(
                    self.title,
                    self.best_prog,
                    self.best_prog)

    def __repr__(self):
        return '\nBank: <{}, rating: {},  Program: {}>{}'.format(self.title,
                                                                 self.rating,
                                                                 self.best_prog,
                                                                 self.index)

    def find_best_program(self):
        maxx = 0
        res = None
        for each in self.programs:
            if maxx < each.find_best()[4]:
                res = each
                maxx = each.find_best()[4]
        return res

    def update(self):
        """
        method for updating the info about current bank
        :return:
        """
        self.programs = [each for each in self.programs if
                         each.find_best(self.current_incomes)]
        for each in self.programs:
            tmp = each.find_best()
            sub = (tmp[3] - tmp[2]) / tmp[2] * 100 - tmp[4]
            # print(each, tmp, (tmp[3]-tmp[2])/tmp[2]*100)
            self.index += sub + self.coeffs['rates']
        self.index += float(self.rating) * self.coeffs['rating']
        self.index += len(self.programs) * self.coeffs['programs']


class Program:
    """
    class for representation Bank programs
    """

    def __init__(self, condition, title, link, rates):
        self.condition = condition
        self.title = title
        self.link = link
        self.EUR_rates = []
        self.UAH_rates = []
        self.USD_rates = []
        self.rates = self.transform_rates(rates)

    def __repr__(self):
        return '{}'.format(self.title)

    def find_best(self, current_incomes=0, currency=None):
        """
        method for finding best rate for current program
        :param current_incomes: current incomes of the family
        :param currency: current currency
        :return: the best program for the family
        """
        currency = self.UAH_rates if currency is None else currency
        current_incomes = 10000000 if current_incomes == 0 else current_incomes
        year = 12
        res = []
        for each in currency:
            if float(each[0]) > current_incomes:
                continue
            # min_invest = float(each[0])
            min_invest = float(200)
            num_of_years = 1
            for months in each[1]:
                num_of_adds = year / float(months)
                year_rate = float(each[1][months])
                n = num_of_years * num_of_adds
                result = round(min_invest * (1 + year_rate / 100 / num_of_adds)
                               ** n, 2)
                res.append([float(each[0]), months, min_invest, result,
                            year_rate])
        if not res:
            return None
        return (sorted(res, key=lambda x: x[2]))[-1]

    def transform_rates(self, rates):
        """
        method for transforming rates in needed format
        :param rates: list of rates
        :return: sorted list
        """
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
