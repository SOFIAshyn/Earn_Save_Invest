from modules.data_collecting.person import Person, Family


class BasicOutgoings:
    '''
    Class to check if money of person divided correctly
    '''
    COSTS = 100
    UTILITY = 20
    FOOD = 30
    TRANSPORT = 15
    CLOTHES = 15
    TRIPS = 10
    HOUSEHOLD = 5
    UNKNOWN = 5

    def __init__(self, days=30):
        '''
        Initialize attributes (in percentage)
        '''
        # for how many days can we count saving moneys
        self.days = days

        self._utility = self.UTILITY
        self._food = self.FOOD
        self._transport = self.TRANSPORT
        self._household = self.HOUSEHOLD
        self._clothes = self.CLOTHES
        self._unknown = self.UNKNOWN
        self._trips = self.TRIPS

    def outgoings_calculator(self):
        '''
        Call all functions
        Calculate for THE days and for family

        :return: dict (Family.family_money_box)
        '''
        # TODO: call _family_calculator
        pass

    def _family_calculator(self):
        '''
        Check if everybody in family still can save money
        Add all money_boxes together

        :return: dict (Family.family_money_box)
        '''
        # TODO: call _person_calculator
        pass

    def _person_calculator(self):
        '''
        Check if person still can save money

        :return: dict (Person.money_box)
        '''
        pass


class NewIncome:
    '''
    Class to calculate possible income
    '''
    def __init__(self, days=30):
        '''
        Initialize attributes that can be offered
        for person (in percentage)
        '''
        # for how many days can we calculate bigger profit
        self.days = days

        self.stock_income = 0
        self.currency_income = 0
        self.deposit_income = 0
        # money that we saved and how we did it
        self.saving = {}

    def new_family_income(self):
        '''
        Check how family can earrn additional money
        Call possible functions
        Edit self.saving - result of calculation

        :return: None
        '''
        pass

    def _calculate_stock_income(self):
        '''
        Analize stock markets and add new kay to self.savings

        :return: None
        '''
        pass

    def _calculate_currency_income(self):
        '''
        Analize stock markets and add new kay to self.savings

        :return: None
        '''
        pass

    def _calculate_deposit_income(self):
        '''
        Analize stock markets and add new kay to self.savings

        :return: None
        '''
        pass
