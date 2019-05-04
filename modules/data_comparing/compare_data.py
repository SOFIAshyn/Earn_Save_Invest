from modules.family_outcome_analysis.family_outcome_an import BasicOutgoings
from modules.data_collecting.family import FamilyPercent


class CompareBasicReal(BasicOutgoings, FamilyPercent):
    '''
    Class to compare real and basic values
    '''

    def __init__(self):
        '''
        initialize all the attributes due to this difference
        '''
        self.dif_utility_bills_per = None
        self.dif_food_per = None
        self.dif_household_per = None
        self.dif_transport_per = None
        self.dif_unknown_per = None
        self.dif_education_per = None
        self.dif_clothes_per = None
        self.dif_trips_per = None
        self.dif_entertainment_per = None

        self._comparing()

    def _comparing(self):
        '''
        Find difference between real and basic
        Change self values - if negative that means that family spend too
        much money on this field

        :return: None
        '''
        self.dif_utility_bills_per = self.utility_bills_per - \
                                     self.max_utility_bills
        self.dif_food_per = self.food_per - self.food
        self.dif_household_per = self.household_per - self.household
        self.dif_transport_per = self.transport_per - self.transport
        self.dif_unknown_per = self.unknown_per - self.unknown
        self.dif_education_per = self.education_per - self.education
        self.dif_clothes_per = self.clothes_per - self.clothes
        self.dif_trips_per = self.trips_per - self.trips
        self.dif_entertainment_per = self.entertainment_per - self.entertainment

    def __str__(self):
        '''
        Return all info about family

        :return: str
        '''
        res = '{}:\nВідсоткові, порівняні витрати сім\'ї\n'.format(
            self.__class__.__name__)
        for person in self.members:
            res += str(person) + '\n'
        res += 'місячні витрати на харчування = {};\nмісячні комунальні ' \
               'витрати = {};\nмісячні побутові витрати = {};\nмісячні ' \
               'транспортні витрати = {};\nмісячні витрат на освіту = {' \
               '};\nмісячні витрати на одяг та взуття = {};\nрічні витрати ' \
               'на подорожі = {};\nмісячні несподівані витрати = {};ґт' \
               'місячні витрати на розваги = {}' \
            .format(self.dif_food_per,
                    self.dif_utility_bills_per,
                    self.dif_household_per,
                    self.dif_transport_per,
                    self.dif_education_per,
                    self.dif_clothes_per,
                    self.dif_trips_per,
                    self.dif_unknown_per,
                    self.dif_entertainment_per)
        return res


if __name__ == '__main__':
    a = CompareBasicReal()
