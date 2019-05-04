'''

To know all information about spending less money
We can use this cases to calculate how much money he / she can save

'''
import re


class Cases:
    '''
    Class to create cases for user to save money
    '''

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
        res = f'{self.name}:\n'
        for i, case in enumerate(self.cases):
            res += f'{i + 1}.\t{case}\n'
        return res

    def count_how_much_save(self):
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


CaseUtilityBills()
