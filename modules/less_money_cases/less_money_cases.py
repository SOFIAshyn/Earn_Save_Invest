'''

To know all information about spending less money
We can use this cases to calculate how much money he / she can save

'''
import re


# from modules.family_outcome_analysis.family_outcome_an import UtilityBills
# from modules.data_collecting.family import Family
#

class Cases:
    '''
    Class to create cases for user to save money
    '''
    SAVINGS = {}
    FAMILY = family
    UTILITY_BILLS = utility_bills

    def __init__(self):
        '''
        Initialize all the attributes
        '''
        self.name = ''
        self.file = ''
        self.cases = []

    def _read_file(self):
        '''
        Get cases from the file

        :return: None
        '''
        with open(self.file, 'r') as file:
            cases = file.read()
        self.cases = re.split(r'\n(?=[А-Я])', cases)

    def add_case(self):
        '''
        Get case from cases and add it to sting
        to present information for user

        :return: str
        '''
        self._read_file()
        res = f'\n{self.name}:\n'
        for i, case in enumerate(self.cases):
            res += f'{i + 1}.\t{case}\n'
        return res

    def get_all_possible_savings(self):
        '''
        Based on pieces of advise recommend real numbers to user

        :return:
        '''
        pass


class CaseUtilityBills(Cases):
    '''
    Subclass of different cases
    '''

    def __init__(self):
        '''
        Initialize all the attributes
        '''
        super(CaseUtilityBills, self).__init__()
        self.name = "Комунальні витрати"
        self.file = 'modules/less_money_cases/case_utility_bills.txt'

    def get_all_possible_savings(self):
        '''
        Count possible money-back with utility bills

        :return: None
        '''
        # one LED save 215UAH per year
        # on 20m^2 you max need 6 LED
        area = self.utility_bills.all_area
        LED_num = area / 20 * 6
        LED_saving = LED_num * 215
        SAVINGS['Заощадження на LED лампочках'] = LED_saving

        # washing machine - less in 2 - 3 times water + 2 - 2,5 kVt
        # scullion - less in 4 - 5 times water, + 1kVt
        # 1/3 of water for people usage
        # rest - washing machine and scullion
        # 15 times per month both machines
        TIMES_MACHINE_RUNS_PER_MONTH = 15
        WASHING_MACHINE_kVt_1_LOOP = 2.5
        SCULLION_kVt_1_LOOP = 1
        WASHING_MACHINE_m3_1_LOOP = 2.5
        SCULLION_m3_1_LOOP = 4.5
        plus_kVt = TIMES_MACHINE_RUNS_PER_MONTH * (
                WASHING_MACHINE_kVt_1_LOOP + SCULLION_kVt_1_LOOP)
        minus_water_m3 = TIMES_MACHINE_RUNS_PER_MONTH * (
                WASHING_MACHINE_m3_1_LOOP + SCULLION_m3_1_LOOP)
        machines_saving = plus_kVt * self.utility_bills.el_price - \
                          minus_water_m3 * self.utility_bills.water_price
        SAVINGS['Заощадження на машинах хатньої роботи'] = machines_saving

        # refund of fee from community offer
        PDV = 19.9
        fam_utility_bills = self.utility_bills.calculate_utility_bills()
        refund_utility_bills = round(fam_utility_bills * PDV / 100, 2)
        SAVINGS[
            'Повернення податку на комунальні послуги'] = refund_utility_bills


class CaseFood(Cases):
    '''
    Subclass of different cases
    '''

    def __init__(self):
        '''
        Initialize all the attributes
        '''
        super(CaseFood, self).__init__()
        self.name = "Витрати на харчування"
        self.file = 'modules/less_money_cases/case_food.txt'

    def get_all_possible_savings(self):
        pass


class CaseHousehold(Cases):
    '''
    Subclass of different cases
    '''

    def __init__(self):
        '''
        Initialize all the attributes
        '''
        super(CaseHousehold, self).__init__()
        self.name = "Засоби для домогосподарства"
        self.file = 'modules/less_money_cases/case_household.txt'

    def get_all_possible_savings(self):
        # buy with sale 10% and save some money
        HOUSEHOLDING_TYPICAL_SALE = 10
        household_out = Family().out_household
        household_saving = round(household_out * HOUSEHOLDING_TYPICAL_SALE /
                                 100, 2)
        SAVINGS[
            'Купівля миючих засобів оптом, по акції'] = household_saving


class CaseTransport(Cases):
    '''
    Subclass of different cases
    '''

    def __init__(self):
        '''
        Initialize all the attributes
        '''
        super(CaseTransport, self).__init__()
        self.name = "Транспортні витрати"
        self.file = 'modules/less_money_cases/case_transport.txt'

    def get_all_possible_savings(self):
        pass


class CaseUnknown(Cases):
    '''
    Subclass of different cases
    '''

    def __init__(self):
        '''
        Initialize all the attributes
        '''
        super(CaseUnknown, self).__init__()
        self.name = "Несподівані витрати"
        self.file = 'modules/less_money_cases/case_unknown.txt'

    def get_all_possible_savings(self):
        pass


class CaseClothes(Cases):
    '''
    Subclass of different cases
    '''

    def __init__(self):
        '''
        Initialize all the attributes
        '''
        super(CaseClothes, self).__init__()
        self.name = "Витрати на одяг та взуття"
        self.file = 'modules/less_money_cases/case_clothes.txt'

    def get_all_possible_savings(self):
        # if fam buy clothes from stock they save approximately 50%
        # we recommend to sell old clothes before new
        # so that you can save at least 15%
        # buy with sale 10% and save some money
        CLOTHES_TYPICAL_SALE = 15
        clothes_out = Family().out_clothes
        clothes_saving = round(clothes_out * CLOTHES_TYPICAL_SALE /
                               100, 2)
        SAVINGS['Перепродаж старого одягу'] = clothes_saving


class CaseTrips(Cases):
    '''
    Subclass of different cases
    '''

    def __init__(self):
        '''
        Initialize all the attributes
        '''
        super(CaseTrips, self).__init__()
        self.name = "Витрати на подорожі"
        self.file = 'modules/less_money_cases/case_trips.txt'

    def get_all_possible_savings(self):
        # you can easily save 5% from money from your trip
        # we recommend to do it
        TRIP_SAVING = 5
        trips_out = self.family.out_trips
        trip_saving = trips_out * TRIP_SAVING / 100
        SAVINGS['Збередення 5% від відпочинку'] = trip_saving


class CaseEducation(Cases):
    '''
    Subclass of different cases
    '''

    def __init__(self):
        '''
        Initialize all the attributes
        '''
        super(CaseEducation, self).__init__()
        self.name = "Витрати на освіту"
        self.file = 'modules/less_money_cases/case_education.txt'

    def get_all_possible_savings(self):
        if self.family.out_education > 10000:
            EDUCATION_AV_SAVING = 50
            edu_saving = self.family.out_education * EDUCATION_AV_SAVING / 100
            SAVINGS['Отримання грантів / пільг'] = edu_saving


class CaseEntertainment(Cases):
    '''
    Subclass of different cases
    '''

    def __init__(self):
        '''
        Initialize all the attributes
        '''
        super(CaseEntertainment, self).__init__()
        self.name = "Витрати на розваги"
        self.file = 'modules/less_money_cases/case_entertainment.txt'

    def get_all_possible_savings(self):
        pass

# CaseUtilityBills()
