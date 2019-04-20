from modules.data_collecting.person import Person, Family


class BasicOutgoings:
    '''
    Class to check if money of person divided correctly
    '''
    COSTS = 100
    UTILITY = 20
    FOOD = 30
    TRANSPORT = 15
    OTHERS = COSTS - (UTILITY + FOOD + TRANSPORT)

    def __init__(self, days=30):
        '''
        Initialize attributes (in percentage)
        '''
        # for how many days can we count saving moneys
        self.days = days

        self.utility_costs = self.UTILITY
        self.food_costs = self.FOOD
        self.transport_costs = self.TRANSPORT



    def person_calculator(self):
        '''
        Check if person still can save money

        :return:dict
        '''
        pass


class NewIncome:
    def __init__(self, days=30):
        '''
        Initialize attributes that can be offered for person (in percentage)
        '''
        # for how many days can we calculate bigger profit
        self.days = days

        self.stock_income = 0
        self.course_income = 0
        self.deposit_income = 0
        self.savings = {}
