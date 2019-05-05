class UtilityBills:
    '''
    Class to calculate min outgoings on utility bills for one person
    '''

    def __init__(self, members_num):
        '''
        Initialize all the attributes for one person
        '''
        self.members_num = members_num

        self.gaz_price = 8.55  # UAH
        self.month_gaz = 25  # m^3

        self.el_price = 0.9  # UAH
        self.month_el = 50  # kVt

        self.water_price = 14.50  # UAH
        self.month_water = 4  # m^3

        self.jek_area_price = 4.8  # UAH
        self.fam_area = 20  # m^2
        self.person_area = 21  # m^2

        self.all_area = self.person_area * self.members_num + self.fam_area

    def calculate_utility_bills(self):
        '''
        Calculate min sum of utility_bills for family

        :return: float
        '''
        # jek offers
        fam_jek_price = self.all_area * self.jek_area_price

        # family water price
        fam_water_price = self.month_water * self.members_num * self.water_price

        # family electricity price
        fam_el_price = self.month_el * self.members_num * self.el_price

        # family gaz price
        fam_gaz_price = self.month_gaz * self.members_num * self.gaz_price

        general_utility_price = fam_jek_price + fam_water_price + \
                                fam_el_price + fam_gaz_price
        return general_utility_price


class BasicOutgoings:
    '''
    Class to analise user data/outgoings with optimal values
    '''

    def __init__(self, members):
        '''
        inintialize all the attributes according to standarts
        More than 100% because family can have some fields absolutely empty
        '''
        self.members = members
        self.members_num = len(members)

        self.min_utility_bills = UtilityBills(
            self.members_num).calculate_utility_bills()

        self.max_utility_bills = 20
        self.food = 30
        self.household = 3
        self.transport = 15
        self.unknown = 5
        self.clothes = 5
        self.trips = 10
        self.education = 47
        self.entertainment = 5

        self.price_utility_bills = UtilityBills(
            self.members_num).calculate_utility_bills()

    def __str__(self):
        '''
        Return all info about family

        :return: str
        '''
        res = '{}:\nВідсоткова база витрат сім\'ї\n'.format(
            self.__class__.__name__)
        for person in self.members:
            res += str(person) + '\n'
        res += 'місячні витрати на харчування = {};\nмісячні комунальні ' \
               'витрати = від {}UAH до {};\nмісячні побутові витрати = {' \
               '};\nмісячні транспортні витрати = {};\nмісячні витрат ' \
               'на освіту = {};\nмісячні витрати на одяг та взуття = {};' \
               '\nрічні витрати на подорожі = {};\nмісячні несподівані ' \
               'витрати = {};\nмісячні витрати на розваги = {};\n'.format(
            self.food,
            self.min_utility_bills,
            self.max_utility_bills,
            self.household,
            self.transport,
            self.education,
            self.clothes,
            self.trips,
            self.unknown,
            self.entertainment)
        return res
