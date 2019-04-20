from modules.exceptions.exceptions import IntInvalidInput, FloatInvalidInput


class Person:
    def __init__(self,
                 age=0,
                 worked=None,
                 workplace=None,
                 income=0.0,
                 extra_income=0.0,
                 hours_on_work=0,
                 saving=0):
        self.__age = age
        self.__worked = worked
        self.__workplace = workplace
        self.__income = income
        self.__extra_income = extra_income
        self.__hours_on_work = hours_on_work
        self.__saving = saving
        self.money_box = {
            'Previous savings': saving,
        }
        self._get_person_data()

    def _get_person_data(self):
        print('Введіть інформацію про члена сім\'ї № {}'.format(i + 1))
        self.__age = input('Вік: ')
        self.__worked = input('Чи працевлаштований член сім\'ї (Так \ Ні): ')
        self.__income = input('Введіть суму, яку стабільно заробляє член '
                              'сім\'ї: ')
        self.__extra_income = input('Введіть додатковий '
                                    'прибуток, яку отримує  '
                                    'член сім\'ї: ')
        self.__hours_on_work = input(
            'Скільки годин на день працює член сім\'ї: ')
        self.__saving = input('Скільки відсотків від доходу / додаткового '
                              'доходу заощаджує член сім\'ї: ')

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, val=0):
        try:
            self.__age = int(val)
        except IntInvalidInput:
            print(IntInvalidInput.message())

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
    def worked(self, val=False):
        if self.worked.lower() == 'так':
            self.__worked = True
        self.__worked = val

    @property
    def income(self):
        return self.__income

    @income.setter
    def income(self, val=0):
        try:
            self.__income = float(val)
        except FloatInvalidInput:
            print(FloatInvalidInput.message())

    @property
    def extra_income(self):
        return self.__extra_income

    @extra_income.setter
    def extra_income(self, val=0):
        try:
            self.__extra_income = float(val)
        except FloatInvalidInput:
            print(FloatInvalidInput.message())

    @property
    def hours_on_work(self):
        return self.__hours_on_work

    @hours_on_work.setter
    def hours_on_work(self, val=0):
        try:
            self.__age = int(val)
        except IntInvalidInput:
            print(IntInvalidInput.message())

    @property
    def saving(self):
        return self.__saving

    @saving.setter
    def saving(self, val=0):
        try:
            self.__saving = float(val)
        except FloatInvalidInput:
            print(FloatInvalidInput.message())

    def __repr__(self):
        return 'age: {}; workplace: {}'.format(self.age, self.workplace)


class Family:
    def __init__(self,
                 members=[],
                 benefits=0.0,
                 out_food=None,
                 out_utility_bills=None,
                 out_household=None,
                 out_transport=None,
                 out_clothes=None,
                 out_trips=None,
                 out_unknown=None,
                 saving=None):
        self.members = members
        self.__benefits = benefits
        self.__out_food = out_food
        self.__out_utility_bills = out_utility_bills
        self.__out_household = out_household
        self.__out_transport = out_transport
        self.__out_clothes = out_clothes
        self.__out_trips = out_trips
        self.__out_unknown = out_unknown
        self.__saving = saving
        self.family_money_box = {}

    # TODO: questions as in person

    # TODO: calculations according to data of each person in family
    def calculate_family_outcome(self):
        '''
        Check each person in family and add all info to family info

        :return: None
        '''
        pass

    def __repr__(self):
        return ''.join(self.members)
