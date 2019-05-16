"""

To know all information about spending less money
We can use this cases to calculate how much money he / she can save

"""
import re

from modules.family_outcome_analysis.family_outcome_an import UtilityBills


# from modules.data_collecting.family import Family
#

class Cases:
    """
    Class to create cases for user to save money
    """
    SAVINGS = {}
    FAM_SAVINGS = {}
    PER_SAVINGS = {}

    def __init__(self, family_instance):
        """
        Initialize all the attributes
        :param family_instance: Family
        """
        self.name = ''
        self.file = ''
        self.cases = []
        self.family = family_instance

    def _read_file(self):
        """
        Get cases from the file

        :return: None
        """
        with open(self.file, 'r') as file:
            cases = file.read()
        self.cases = re.split(r'\n(?=[А-Я])', cases)

    def add_case(self):
        """
        Get case from cases and add it to sting
        to present information for user

        :return: str
        """
        self._read_file()
        res = '\n{}:\n'.format(self.name)
        for i, case in enumerate(self.cases):
            res += "{}.\t{}\n".format(i + 1, case)
        return res

    def get_all_cases(self):
        """
        Get all cases together
        :return: str
        """
        person = None
        lst_f = [CaseUtilityBills(self.family),
                 CaseFood(self.family),
                 CaseHousehold(self.family),
                 CaseUnknown(self.family),
                 CaseTrips(self.family)]
        lst_p = [CaseTransport(person),
                 CaseClothes(person),
                 CaseEducation(person),
                 CaseEntertainment(person)]
        res = ''
        for func in lst_f:
            res += func.add_case() + '\n'
        for person in self.family.members:
            for func in lst_p:
                res += func.add_case() + '\n'
        return res

    def get_all_possible_savings(self):
        """
        Based on pieces of advice recommend real numbers to user

        :return:dict
        """
        CaseUtilityBills(self.family).get_all_possible_savings()
        CaseFood(self.family).get_all_possible_savings()
        CaseHousehold(self.family).get_all_possible_savings()
        CaseUnknown(self.family).get_all_possible_savings()
        CaseTrips(self.family).get_all_possible_savings()
        print ('dfghjkljhjghfghjgfdfghj')
        print(self.FAM_SAVINGS)
        self.SAVINGS['Загальні заощадження сім\'ї'] = self.FAM_SAVINGS
        # here self.family
        for i in range(len(self.family.members)):
            person = self.family.members[i]
            # count all savings
            CaseTransport(person).get_all_possible_savings()
            CaseClothes(person).get_all_possible_savings()
            CaseEducation(person).get_all_possible_savings()
            CaseEntertainment(person).get_all_possible_savings()
            # count start savings
            person_gen_income = person.income + person.extra_income
            self.PER_SAVINGS['Початкові заощадження'] = \
                round(person_gen_income * person.saving / 100, 2)
            print('self.PER_SAVINGS')
            print(self.PER_SAVINGS, person.name)
            self.SAVINGS['Заощадження {}'.format(person.name)] = \
                self.PER_SAVINGS
            self.PER_SAVINGS = {}
        return self.SAVINGS


class CaseUtilityBills(Cases):
    """
    Subclass of different cases
    """

    def __init__(self, family_instance):
        """
        Initialize all the attributes
        """
        super(CaseUtilityBills, self).__init__(family_instance)
        self.name = "Комунальні витрати"
        self.file = 'modules/less_money_cases/case_utility_bills.txt'

    def get_all_possible_savings(self):
        """
        Count possible money-back with utility bills

        :return: None
        """
        ut_b = UtilityBills(len(self.family.members))
        # one LED save 215UAH per year
        # on 20m^2 you max need 6 LED
        area = ut_b.all_area
        LED_num = area / 20 * 6
        LED_saving = LED_num * 215 / 12
        # per month
        self.FAM_SAVINGS['Заощадження на LED лампочках'] = round(LED_saving, 2)

        # washing machine - less in 2 - 3 times water + 2 - 2,5 kVt
        # scullion - less in 4 - 5 times water, + 1kVt
        # 1/3 of water for people usage
        # rest - washing machine and scullion
        # 27 times per year both machines
        TIMES_MACHINE_RUNS_PER_MONTH = 27
        WASHING_MACHINE_kVt_1_LOOP = 2.5
        SCULLION_kVt_1_LOOP = 1
        WASHING_MACHINE_m3_1_LOOP = 2.5
        SCULLION_m3_1_LOOP = 4.5
        # how many kVt in month
        plus_kVt = TIMES_MACHINE_RUNS_PER_MONTH * (
                WASHING_MACHINE_kVt_1_LOOP + SCULLION_kVt_1_LOOP)
        # in how many times it is less
        minus_water_m3 = TIMES_MACHINE_RUNS_PER_MONTH * (
                WASHING_MACHINE_m3_1_LOOP + SCULLION_m3_1_LOOP)
        # how much money we save
        # more kVt , less m3
        machines_saving = (minus_water_m3 * ut_b.water_price - \
                           plus_kVt * ut_b.el_price) / 12
        # per month
        self.FAM_SAVINGS[
            'Заощадження на машинах хатньої роботи'] = round(
            machines_saving, 2)

        # refund of fee from community offer
        PDV = 19.9
        fam_utility_bills = ut_b.calculate_utility_bills()
        refund_utility_bills = round(fam_utility_bills * PDV / 100, 2)
        # per month
        self.FAM_SAVINGS[
            'Повернення податку на комунальні послуги'] = \
            round(refund_utility_bills, 2)


class CaseFood(Cases):
    """
    Subclass of different cases
    """

    def __init__(self, family_instance):
        """
        Initialize all the attributes
        """
        super(CaseFood, self).__init__(family_instance)
        self.name = "Витрати на харчування"
        self.file = 'modules/less_money_cases/case_food.txt'

    def get_all_possible_savings(self):
        pass


class CaseHousehold(Cases):
    """
    Subclass of different cases
    """

    def __init__(self, family_instance):
        """
        Initialize all the attributes
        """
        super(CaseHousehold, self).__init__(family_instance)
        self.name = "Засоби для домогосподарства"
        self.file = 'modules/less_money_cases/case_household.txt'

    def get_all_possible_savings(self):
        # buy with sale 10% and save some money
        HOUSEHOLDING_TYPICAL_SALE = 10
        household_out = self.family.out_household
        household_saving = round(household_out * HOUSEHOLDING_TYPICAL_SALE /
                                 100, 2)
        # per month
        self.FAM_SAVINGS[
            'Купівля миючих засобів оптом, по акції'] = household_saving


class CaseUnknown(Cases):
    """
    Subclass of different cases
    """

    def __init__(self, family_instance):
        """
        Initialize all the attributes
        """
        super(CaseUnknown, self).__init__(family_instance)
        self.name = "Несподівані витрати"
        self.file = 'modules/less_money_cases/case_unknown.txt'

    def get_all_possible_savings(self):
        pass


class CaseTrips(Cases):
    """
    Subclass of different cases
    """

    def __init__(self, family_instance):
        """
        Initialize all the attributes
        """
        super(CaseTrips, self).__init__(family_instance)
        self.person_instance = self.family
        self.name = "Витрати на подорожі"
        self.file = 'modules/less_money_cases/case_trips.txt'

    def get_all_possible_savings(self):
        # you can easily save 5% from money from your trip
        # we recommend to do it
        TRIP_SAVING = 5
        trips_out = self.person_instance.out_trips
        trip_saving = trips_out * TRIP_SAVING / 100
        # per month
        self.FAM_SAVINGS['Збереження 5% від відпочинку'] = round(
            trip_saving, 2)


# savings for one person

class CaseTransport(Cases):
    """
    Subclass of different cases
    For 1 person
    """

    def __init__(self, family_instance):
        """
        Initialize all the attributes
        """
        super(CaseTransport, self).__init__(family_instance)
        self.name = "Транспортні витрати"
        self.file = 'modules/less_money_cases/case_transport.txt'

    def get_all_possible_savings(self):
        pass


class CaseClothes(Cases):
    """
    Subclass of different cases
    """

    def __init__(self, family_instance):
        """
        Initialize all the attributes
        """
        super(CaseClothes, self).__init__(family_instance)
        self.name = "Витрати на одяг та взуття"
        self.file = 'modules/less_money_cases/case_clothes.txt'

    def get_all_possible_savings(self):
        # if fam buy clothes from stock they save approximately 50%
        # we recommend to sell old clothes before new
        # so that you can save at least 15%
        # buy with sale 10% and save some money
        clothes_out = self.family.out_clothes
        CLOTHES_TYPICAL_SALE = 10
        clothes_saving = round(clothes_out * CLOTHES_TYPICAL_SALE /
                               100, 2)
        # per month
        self.PER_SAVINGS['Купівля одягу по знижках'] = clothes_saving

        # sell 1/2 of your clothes
        SEVED_SELL_CLOTHES_PRICE = 30
        old_clothes_saving = round(clothes_out * SEVED_SELL_CLOTHES_PRICE /
                                   100, 2)
        # per month
        self.PER_SAVINGS['Перепродаж старого одягу'] = old_clothes_saving


class CaseEducation(Cases):
    """
    Subclass of different cases
    """

    def __init__(self, family_instance):
        """
        Initialize all the attributes
        """
        super(CaseEducation, self).__init__(family_instance)
        self.name = "Витрати на освіту"
        self.file = 'modules/less_money_cases/case_education.txt'

    def get_all_possible_savings(self):
        if self.family.out_education > 10000:
            EDUCATION_AV_SAVING = 50
            edu_saving = round(self.family.out_education * \
                               EDUCATION_AV_SAVING / 100, 2)
            # per month
            self.PER_SAVINGS['Отримання грантів / пільг'] = edu_saving


class CaseEntertainment(Cases):
    """
    Subclass of different cases
    For person
    """

    def __init__(self, family_instance):
        """
        Initialize all the attributes
        """
        super(CaseEntertainment, self).__init__(family_instance)
        self.name = "Витрати на розваги"
        self.file = 'modules/less_money_cases/case_entertainment.txt'

    def get_all_possible_savings(self):
        pass

# CaseUtilityBills()
