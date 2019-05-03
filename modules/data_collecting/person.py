from modules.exceptions.exceptions import IntInvalidInput, FloatInvalidInput


class Person:
    '''
    Class to collect all the information about user
    '''

    def __init__(self, i,
                 age=0,
                 worked=None,
                 workplace=None,
                 income=0.0,
                 extra_income=0.0,
                 hours_on_work=0,
                 saving=0):
        '''
        Initialize all the attributes
        :param i: int
        :param age: int
        :param worked: None
        :param workplace: None
        :param income: float
        :param extra_income: float
        :param hours_on_work: int
        :param saving: int
        '''
        self.number = i + 1
        self.__age = age
        self.__worked = worked
        # TODO: create list of positions and on data analisys offer
        #  additional income
        self.__workplace = workplace
        self.__income = income
        self.__extra_income = extra_income
        self.__hours_on_work = hours_on_work
        self.__saving = saving
        self.money_box = {
            'Previous savings': saving,
        }
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

    def _get_person_data(self):
        '''
        Get and set data sbout user in correct type

        :return: None
        '''
        print('Введіть інформацію про члена сім\'ї № {}'.format(self.number))
        while not self.age:
            self.age = input('Вік: ')
        while self.worked is None:
            employed = input('Чи працевлаштований член сім\'ї (Так \ '
                             'Ні): ')
            if employed == 'так':
                self.worked = True
            elif employed == 'ні':
                self.worked = False
            else:
                self.worked = None
        if self.worked is True:
            while not self.income:
                self.income = input(
                    'Введіть суму, яку стабільно заробляє член '
                    'сім\'ї: ')
            self.extra_income = input('Введіть додатковий '
                                      'прибуток, яку отримує '
                                      'член сім\'ї: ')
            while not self.hours_on_work:
                self.hours_on_work = input(
                    'Скільки годин на день працює член сім\'ї: ')
            self.saving = input('Скільки відсотків від доходу / додаткового '
                                'доходу заощаджує член сім\'ї: ')

    def __str__(self):
        '''
        Return information about person

        :return: str
        '''
        res = '{}{}: вік = {}; працевлаштування = {}'.format(
            self.__class__.__name__, self.number, self.age, self.worked)
        if self.worked:
            res += '; прибуток = {}; додатковий прибуток = {}; ' \
                   'робочі години на день = {}; заощадження = {}%'.format(
                self.income, self.extra_income, self.hours_on_work,
                self.saving)
        return res


class Family:
    '''
    Class to collect all family data
    '''

    def __init__(self,
                 members=[],
                 fam_income=0.0,
                 benefits=0.0,
                 out_food=None,
                 out_utility_bills=None,
                 out_household=None,
                 out_transport=None,
                 out_education=0.0,
                 out_clothes=None,
                 out_trips=None,
                 out_unknown=None,
                 saving=0):
        '''
        Initialize all the attributes
        :param members: list
        :param fam_income: float
        :param benefits: float
        :param out_food: none
        :param out_utility_bills: None
        :param out_household: None
        :param out_transport: None
        :param out_education: float
        :param out_clothes: None
        :param out_trips: None
        :param out_unknown: None
        :param saving: int
        '''
        self.members = members
        self.__fam_income = fam_income
        self.__benefits = benefits
        self.__out_food = out_food
        self.__out_utility_bills = out_utility_bills  # комунальні витрати
        self.__out_household = out_household  # побутові витрати
        self.__out_transport = out_transport
        self.__out_education = out_education
        self.__out_clothes = out_clothes
        self.__out_trips = out_trips
        self.__out_unknown = out_unknown
        self.__saving = saving
        # from what family have money
        self.family_money_box = {}

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
    def out_trips(self):
        return self.__out_trips

    @out_trips.setter
    def out_trips(self, val):
        try:
            self.__out_trips = float(val)
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

    # TODO: questions as in person
    def _get_family_data(self):
        '''
        Get data from user in correct type

        :return: None
        '''
        self._set_default_family_data()
        # Questions
        while not self.out_food:
            self.out_food = input('Введіть суму місячних витрат на '
                                  'харчування: ')
        while not self.out_utility_bills:
            self.out_utility_bills = input(
                'Введіть суму місячних комунальних витрат: ')
        while not self.out_household:
            self.out_household = input(
                'Введіть суму місячних побутових витрат\n(засоби гігієни, '
                'засоби для прибирання дому і т.д.): ')
        while not self.out_transport:
            self.out_transport = input(
                'Введіть суму місячних транспортних витрат: ')
        while not self.out_education:
            self.out_education = input(
                'Введіть суму місячних витрат на освіту: ')
        while not self.out_clothes:
            self.out_clothes = input(
                'Введіть суму місячних витрат на одяг та взуття: ')
        while not self.out_trips:
            self.out_trips = input(
                'Введіть суму річних витрат на подорожі: ')
        while not self.out_unknown:
            self.out_unknown = input(
                'Введіть суму річних несподіваних витрат: ')
        # TODO: get to understand if we need these variables
        general_outcome = self.out_utility_bills + self.out_food + \
                          self.out_household + self.out_clothes + \
                          self.out_transport
        gen_per_year = self.out_trips + self.out_unknown + self.out_education
        if self.fam_income + self.benefits < general_outcome:
            print('Ви маєте серйозні проблеми з бюджнтом. Слідкуйте за '
                  'порадами платформи Earn Save Invest')

    def _set_default_family_data(self):
        '''
        Check each person in family and add all info to family info

        :return: None
        '''
        for person in self.members:
            if person.income:
                self.fam_income += person.income
            if person.extra_income:
                self.benefits += person.extra_income
            if person.saving:
                self.saving += person.saving

    def __str__(self):
        '''
        Return all info about family

        :return: str
        '''
        res = '{}:\n'.format(self.__class__.__name__)
        for person in self.members:
            res += str(person) + '\n'
        res += 'місячні витрати на харчування = {};\nмісячні комунальні ' \
               'витрати = {};\nмісячні побутові витрати = {};\nмісячні ' \
               'транспортні витрати = {};\nмісячні витрат на освіту = {' \
               '};\nмісячні витрати на одяг та взуття = {};\nрічні витрати ' \
               'на подорожі = {};\nрічні несподівані витрати = {}'.format(
            self.out_food, self.out_utility_bills, self.out_household,
            self.out_transport, self.out_education, self.out_clothes,
            self.out_trips, self.out_unknown)
        return res
