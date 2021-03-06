from modules.exceptions.exceptions import IntInvalidInput, FloatInvalidInput


class Person:
    """
    Class to collect all the information about user
    """

    def __init__(self, i,
                 age=0,
                 name=None,
                 worked=None,
                 workplace=None,
                 income=0.0,
                 extra_income=1.0,
                 hours_on_work=0,
                 saving=1,
                 out_transport=0.0,
                 out_clothes=0.0,
                 out_education=0.0,
                 out_entertainment=0.0):
        """
        Initialize all the attributes
        :param i: int
        :param name: None
        :param age: int
        :param worked: None
        :param workplace: None
        :param income: float
        :param extra_income: float
        :param hours_on_work: int
        :param saving: int
        :param out_entertainment: float
        """
        self.number = i + 1
        self.name = name
        self.__age = age
        self.__worked = worked
        # TODO: create list of positions and on data analisys offer
        #  additional income for future
        self.__workplace = workplace  # current
        self.__income = income  # per month
        self.__extra_income = extra_income  # per month
        self.__hours_on_work = hours_on_work  # per day
        self.__saving = saving  # per month
        self.__out_transport = out_transport  # per month
        self.__out_clothes = out_clothes  # per month
        self.__out_education = out_education  # per month
        self.__out_entertainment = out_entertainment  # per month
        self.money_box = {
            'Стабільні заощадження': saving,
        }
        # get data from user
        self._get_person_data()

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, val=0):
        try:
            self.__age = int(val)
        except ValueError:
            print(IntInvalidInput().message())

    @property
    def workplace(self):
        return self.__workplace

    @workplace.setter
    def workplace(self, val=False):
        self.__workplace = val

    @property
    def worked(self):
        return self.__worked

    @worked.setter
    def worked(self, val):
        self.__worked = val

    @property
    def income(self):
        return self.__income

    @income.setter
    def income(self, val=0):
        try:
            self.__income = float(val)
        except ValueError:
            print(FloatInvalidInput().message())

    @property
    def extra_income(self):
        return self.__extra_income

    @extra_income.setter
    def extra_income(self, val=0):
        try:
            self.__extra_income = float(val)
        except ValueError:
            self.__extra_income = None

    @property
    def hours_on_work(self):
        return self.__hours_on_work

    @hours_on_work.setter
    def hours_on_work(self, val=0):
        try:
            self.__hours_on_work = int(val)
        except ValueError:
            print(IntInvalidInput().message())

    @property
    def saving(self):
        return self.__saving

    @saving.setter
    def saving(self, val=0):
        try:
            self.__saving = float(val)
        except ValueError:
            self.__saving = None

    @property
    def out_transport(self):
        return self.__out_transport

    @out_transport.setter
    def out_transport(self, val=0):
        try:
            self.__out_transport = float(val)
        except ValueError:
            self.__out_transport = None

    @property
    def out_clothes(self):
        return self.__out_clothes

    @out_clothes.setter
    def out_clothes(self, val):
        try:
            self.__out_clothes = float(val)
        except ValueError:
            self.__out_clothes = None

    @property
    def out_education(self):
        return self.__out_education

    @out_education.setter
    def out_education(self, val):
        try:
            self.__out_education = float(val)
        except ValueError:
            self.__out_education = None

    @property
    def out_entertainment(self):
        return self.__out_entertainment

    @out_entertainment.setter
    def out_entertainment(self, val):
        try:
            self.__out_entertainment = float(val)
        except ValueError:
            self.__out_entertainment = None

    def _get_person_data(self):
        """
        Get and set data sbout user in correct type

        :return: None
        """
        print('Введіть інформацію про члена сім\'ї № {}'.format(self.number))
        while not self.name:
            try:
                self.name = input('Iм\'я: ')
            except UnicodeDecodeError:
                self.name = 'NoName'
        while not self.age:
            try:
                self.age = input('Вік: ')
            except UnicodeDecodeError:
                self.worked = None
        while self.worked is None:
            try:
                employed = input('Чи працевлаштований член сім\'ї (Так \ '
                                 'Ні): ')
                if employed == 'так':
                    self.worked = True
                elif employed == 'ні':
                    self.worked = False
                else:
                    self.worked = None
            except UnicodeDecodeError:
                self.worked = None
        # TODO: check income and extra income for a time for future
        if self.worked is True:
            while not self.workplace:
                try:
                    self.workplace = input(
                        'Введіть посаду / навчальний статус члена сім\'ї: ')
                except UnicodeDecodeError:
                    self.workplace = 'NoData'

            while not self.income:
                self.income = input(
                    'Введіть суму, яку стабільно заробляє член '
                    'сім\'ї за місяць: ')
            while not self.hours_on_work:
                self.hours_on_work = input(
                    'Скільки годин на день працює член сім\'ї: ')
        self.extra_income = input('Введіть додатковий '
                                  'прибуток, який отримує '
                                  'член сім\'ї на місяць: ')
        self.saving = input('Скільки відсотків від загального '
                            'прибутку щомісячно заощаджує '
                            'член сім\'ї: ')
        while not self.out_transport:
            self.out_transport = input(
                'Введіть суму місячних витрат особи на транспорт: ')
        while not self.out_education:
            self.out_education = input(
                'Введіть суму місячних витрат на освіту: ')
        while not self.out_clothes:
            self.out_clothes = input(
                'Введіть суму місячних витрат на одяг та взуття: ')
        while not self.out_entertainment:
            self.out_entertainment = input(
                'Введіть суму місячних витрат особи на розваги та спорт: ')

    def __str__(self):
        """
        Return information about person

        :return: str
        """
        res = '{}{}: вік = {}; працевлаштування = {}; витрати на траспорт = ' \
              '{}; витрати на одяг та взуття = {}; витрати на освіту = {}; ' \
              'витрати на розваги та спорт = {}'.format(
            self.__class__.__name__, self.number, self.age, self.worked,
            self.out_transport, self.out_clothes, self.out_education,
            self.out_entertainment)
        if self.worked:
            res += '; прибуток = {}; додатковий прибуток = {}; ' \
                   'посада = {}; робочі години на день = {}; заощадження = {' \
                   '}%'.format(
                self.income, self.extra_income, self.workplace,
                self.hours_on_work, self.saving)
        return res


class Family:
    """
    Class to collect all family data
    """

    def __init__(self,
                 members=[],
                 fam_income=0.0,
                 benefits=0.0,
                 out_food=None,
                 out_utility_bills=None,
                 out_household=None,
                 out_transport=0.0,
                 out_education=0.0,
                 out_clothes=0.0,
                 out_entertainment=0.0,
                 out_trips=None,
                 out_unknown=None,
                 saving=0):
        """
        Initialize all the attributes
        :param members: list
        :param fam_income: float
        :param benefits: float
        :param out_food: none
        :param out_utility_bills: None
        :param out_household: None
        :param out_transport: float
        :param out_education: float
        :param out_clothes: None
        :param entertainment: float
        :param out_trips: None
        :param out_unknown: None
        :param saving: int
        """
        self.members = members
        self.__fam_income = fam_income  # per month
        self.__benefits = benefits  # per_month
        self.__out_food = out_food  # per month
        self.__out_utility_bills = out_utility_bills  # комунальні витрати per month
        self.__out_household = out_household  # побутові витрати per month
        self.__out_transport = out_transport  # per month
        self.__out_education = out_education  # per month
        self.__out_clothes = out_clothes  # per month
        self.__out_entertainment = out_entertainment  # per month
        self.__out_trips = out_trips  # per month
        self.__out_unknown = out_unknown  # per month
        self.__saving = saving  # per month
        # from what family have money
        self.family_money_box = {
            'Початкові заощадження': self.__saving,
        }

        self._get_family_data()

    @property
    def fam_income(self):
        return self.__fam_income

    @fam_income.setter
    def fam_income(self, val):
        self.__fam_income = val

    @property
    def benefits(self):
        return self.__benefits

    @benefits.setter
    def benefits(self, val):
        self.__benefits = val

    @property
    def out_food(self):
        return self.__out_food

    @out_food.setter
    def out_food(self, val):
        try:
            self.__out_food = float(val)
        except ValueError:
            self.__out_food = None

    @property
    def out_utility_bills(self):
        return self.__out_utility_bills

    @out_utility_bills.setter
    def out_utility_bills(self, val):
        try:
            # PER YEAR - more correct
            # self.__out_utility_bills = round(float(val) / 12, 2)
            # PER MONTH - user usaully don't notice
            self.__out_utility_bills = float(val)
        except ValueError:
            self.__out_utility_bills = None

    @property
    def out_household(self):
        return self.__out_household

    @out_household.setter
    def out_household(self, val):
        try:
            self.__out_household = float(val)
        except ValueError:
            self.__out_household = None

    @property
    def out_transport(self):
        return self.__out_transport

    @out_transport.setter
    def out_transport(self, val):
        try:
            self.__out_transport = float(val)
        except ValueError:
            self.__out_transport = None

    @property
    def out_education(self):
        return self.__out_education

    @out_education.setter
    def out_education(self, val):
        try:
            self.__out_education = float(val)
        except ValueError:
            self.__out_education = None

    @property
    def out_clothes(self):
        return self.__out_clothes

    @out_clothes.setter
    def out_clothes(self, val):
        try:
            self.__out_clothes = float(val)
        except ValueError:
            self.__out_clothes = None

    @property
    def out_entertainment(self):
        return self.__out_entertainment

    @out_entertainment.setter
    def out_entertainment(self, val):
        self.__out_entertainment = val

    @property
    def out_trips(self):
        return self.__out_trips

    @out_trips.setter
    def out_trips(self, val):
        try:
            self.__out_trips = round(float(val) / 12, 2)
        except ValueError:
            self.__out_trips = None

    @property
    def out_unknown(self):
        return self.__out_unknown

    @out_unknown.setter
    def out_unknown(self, val):
        try:
            self.__out_unknown = float(val)
        except ValueError:
            self.__out_unknown = None

    @property
    def saving(self):
        return self.__saving

    @saving.setter
    def saving(self, val):
        self.__saving = val

    def _get_family_data(self):
        """
        Get data from user in correct type

        :return: None
        """
        self._set_default_family_data()
        # Questions
        while not self.out_food:
            self.out_food = input('Введіть суму місячних витрат на '
                                  'харчування: ')
        while not self.out_utility_bills:
            self.out_utility_bills = input(
                'Введіть середню суму місячних комунальних витрат та, '
                'за наявності, оплату за оренду житла: ')
        while not self.out_household:
            self.out_household = input(
                'Введіть суму місячних побутових витрат\n(засоби гігієни, '
                'засоби для прибирання дому і т.д.): ')
        while not self.out_transport:
            self.out_transport = input(
                'Введіть суму місячних транспортних витрат: ')
        while not self.out_trips:
            self.out_trips = input(
                'Введіть суму річних витрат на подорожі: ')
        while not self.out_unknown:
            self.out_unknown = input(
                'Введіть суму місячних несподіваних витрат: ')

        general_outcome = self.out_utility_bills + self.out_food + \
                          self.out_household + self.out_clothes + \
                          self.out_transport
        if self.fam_income + self.benefits < general_outcome:
            print('Ви маєте проблеми з бюджнтом. Слідкуйте за '
                  'порадами платформи Earn Save Invest')

    def _set_default_family_data(self):
        """
        Check each person in family and add all info to family info

        :return: None
        """
        for person in self.members:
            if person.income:
                self.fam_income += person.income
            if person.extra_income:
                self.benefits += person.extra_income
            if person.saving:
                self.saving += person.saving
            if person.out_transport:
                self.out_transport += person.out_transport
            if person.out_entertainment:
                self.out_entertainment += person.out_entertainment
            if person.out_education:
                self.out_education += person.out_education
            if person.out_clothes:
                self.out_clothes += person.out_clothes

    def get_fam_outdoings_in_percents(self):
        """
        Calculate how many money in percentage family spend and for what
        :return: list
        """
        # to deny ZeroDivisionError
        if not self.fam_income:
            self.fam_income = 1
        if self.benefits:
            all_income = self.fam_income + self.benefits
        else:
            all_income = self.fam_income

        utility_bills_per = round((self.out_utility_bills * 100) / \
                                  all_income, 2)
        food_per = round((self.out_food * 100) / self.fam_income, 2)
        household_per = round((self.out_household * 100) / \
                              all_income, 2)
        transport_per = round((self.out_transport * 100) / \
                              all_income, 2)
        unknown_per = round((self.out_unknown * 100) / \
                            all_income, 2)
        education_per = round((self.out_education * 100) / \
                              all_income, 2)
        clothes_per = round((self.out_clothes * 100) / \
                            all_income, 2)
        trips_per = round((self.out_trips * 100) / \
                          all_income, 2)
        entertainment_per = round((self.out_entertainment * 100) / \
                                  all_income, 2)

        return [utility_bills_per, food_per, household_per,
                transport_per, unknown_per, education_per,
                clothes_per, trips_per, entertainment_per]

    def saved_percentage_to_UAH(self, list_with_difference_in_percentage,
                                list_with_names):
        """
        Calculate how much money we can save in one month
        Change money box

        :return: None
        """
        if self.benefits:
            all_income = self.fam_income + self.benefits
        else:
            all_income = self.fam_income

        lst = list_with_difference_in_percentage

        for i in range(len(lst)):
            persent = lst[i]
            self.family_money_box[list_with_names[i] + ' - збереження'] = \
                round(persent * all_income / 100, 2)

    def check_gen_income(self):
        """
        Check in general income > than min in Ukraine
        :return: bool
        """
        # 2019 - update every year
        MIN_INCOME = 4173

        gen_income = 0
        for person in self.members:
            if person.income:
                gen_income += person.income
            if person.extra_income:
                gen_income += person.extra_income
        if gen_income > MIN_INCOME:
            return False
        return True

    def __str__(self):
        """
        Return all info about family

        :return: str
        """
        res = '{}:\n'.format(self.__class__.__name__)
        for person in self.members:
            res += str(person) + '\n'
        res += 'місячні витрати на харчування = {};\nмісячні комунальні ' \
               'витрати = {};\nмісячні побутові витрати = {};\nмісячні ' \
               'транспортні витрати = {};\nмісячні витрат на освіту = {' \
               '};\nмісячні витрати на одяг та взуття = {};\nрічні витрати ' \
               'на подорожі = {};\nмісячні несподівані витрати = {};\n' \
               'місячні витрати на розваги = {}\n'.format(
            self.out_food, self.out_utility_bills, self.out_household,
            self.out_transport, self.out_education, self.out_clothes,
            self.out_trips, self.out_unknown, self.out_entertainment)
        return res


class FamilyPercent:
    """
    Class to contain family outgoings in percentage
    """

    def __init__(self, all_outgoings, members):
        """
        Initialize all attributes
        :param all_outgoings: list
        :param members: list of Person
        """
        self.members = members

        self.utility_bills_per = all_outgoings[0]
        self.food_per = all_outgoings[1]
        self.household_per = all_outgoings[2]
        self.transport_per = all_outgoings[3]
        self.unknown_per = all_outgoings[4]
        self.education_per = all_outgoings[5]
        self.clothes_per = all_outgoings[6]
        self.trips_per = all_outgoings[7]
        self.entertainment_per = all_outgoings[8]

    def __str__(self):
        """
        Return all info about family

        :return: str
        """
        res = '{}:\nВідсоткові витрати сім\'ї\n'.format(
            self.__class__.__name__)
        for person in self.members:
            res += str(person) + '\n'
        res += 'місячні витрати на харчування = {} %;\nмісячні комунальні ' \
               'витрати = {} %;\nмісячні побутові витрати = {} %;\nмісячні ' \
               'транспортні витрати = {} %;\nмісячні витрат на освіту = {' \
               '} %;\nмісячні витрати на одяг та взуття = {} %;\nрічні ' \
               'витрати на подорожі = {} %;\nмісячні несподівані витрати ' \
               '= {} %;\n місячні витрати на розваги = {} %;\n'.format(
            self.food_per, self.utility_bills_per, self.household_per,
            self.transport_per, self.education_per, self.clothes_per,
            self.trips_per, self.unknown_per, self.entertainment_per)
        return res
