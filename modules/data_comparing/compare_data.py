# from modules.family_outcome_analysis.family_outcome_an import BasicOutgoings
# from modules.data_collecting.family import FamilyPercent


class CompareBasicReal:
    """
    Class to compare real and basic values
    """

    def __init__(self, basic_family_outgoings, real_family_outgoings):
        """
        initialize all the attributes due to this difference
        """
        self.basic_outgoing = basic_family_outgoings
        self.family_percent = real_family_outgoings

        self.dif_utility_bills_per = None
        self.dif_food_per = None
        self.dif_household_per = None
        self.dif_transport_per = None
        self.dif_unknown_per = None
        self.dif_education_per = None
        self.dif_clothes_per = None
        self.dif_trips_per = None
        self.dif_entertainment_per = None

        self.all_outgoings = []
        self.outgoing_names = []

        self._comparing()

    def _comparing(self):
        """
        Find difference between real and basic
        Change self values - if negative that means that family spend too
        much money on this field

        :return: None
        """
        self.dif_utility_bills_per = self.family_percent.utility_bills_per - \
                                     self.basic_outgoing.max_utility_bills
        self.dif_food_per = self.family_percent.food_per - \
                            self.basic_outgoing.food
        self.dif_household_per = self.family_percent.household_per - \
                                 self.basic_outgoing.household
        self.dif_transport_per = self.family_percent.transport_per - \
                                 self.basic_outgoing.transport
        self.dif_unknown_per = self.family_percent.unknown_per - \
                               self.basic_outgoing.unknown
        self.dif_education_per = self.family_percent.education_per - \
                                 self.basic_outgoing.education
        self.dif_clothes_per = self.family_percent.clothes_per - \
                               self.basic_outgoing.clothes
        self.dif_trips_per = self.family_percent.trips_per - \
                             self.basic_outgoing.trips
        self.dif_entertainment_per = self.family_percent.entertainment_per - \
                                     self.basic_outgoing.entertainment

        self.all_outgoings = [self.dif_utility_bills_per,
                              self.dif_food_per,
                              self.dif_household_per,
                              self.dif_transport_per,
                              self.dif_unknown_per,
                              self.dif_education_per,
                              self.dif_clothes_per,
                              self.dif_trips_per,
                              self.dif_entertainment_per]

        self.outgoing_names = ["Комунальні витрати", "Витрати на харчування",
                               "Засоби для домогосподарства",
                               "Транспортні витрати",
                               "Несподівані витрати",
                               "Витрати на одяг та взуття",
                               "Витрати на подорожі", "Витрати на освіту",
                               "Витрати на розваги"]

    def _check_if_too_much_money_spend(self):
        """
        Check each attribute if it is according to standarts

        :return: list
        """
        over_outgoings = [self.dif_utility_bills_per,
                          self.dif_food_per,
                          self.dif_household_per,
                          self.dif_transport_per,
                          self.dif_unknown_per,
                          self.dif_education_per,
                          self.dif_clothes_per,
                          self.dif_trips_per,
                          self.dif_entertainment_per]
        for outgoing in over_outgoings:
            if outgoing >= 0:
                over_outgoings.remove(outgoing)

        return over_outgoings

    def create_advise(self):
        """
        Analise if all outgoings are less than 100%
        Decide where the user cam spend less

        :return:
        """
        over_outgoings = self._check_if_too_much_money_spend()
        fam_percentage = sum(self.all_outgoings)

        if fam_percentage <= -40:
            # it is okay if family spend money in the way they like it
            # check if all outgoings are reasonable
            return self.less_100_check()
        else:
            # give answer where family spend too much money
            return self.more_100_check()

    def less_100_check(self):
        """
        Give pieces of advise about outgoings
        if they are more than in basic rules

        :return: tuple(dict, str)
        """
        too_much_money_spend = {}
        res = 'Ваші витрати є оптимальними'
        for i in range(len(self.all_outgoings)):

            # check utility. if min profit > 20% can be not enough
            if self.outgoing_names[i] == 'Комунальні витрати':
                if self.all_outgoings[i] <= \
                        self.basic_outgoing.min_utility_bills:
                    self.all_outgoings[i] = 0
            if self.outgoing_names[i] == 'Витрати на харчування':
                MIN_FOR_FOOD = 2000
                if self.all_outgoings[i] <= MIN_FOR_FOOD:
                    self.all_outgoings[i] = 0

            # if number is negative it is mean that family spend less money
            # than expected, it is nice
            # otherwise we count how many % family could save:
            if self.all_outgoings[i] > 0:
                # on what how many % fam can save
                too_much_money_spend[self.outgoing_names[i]] = \
                    self.all_outgoings[i]

        if len(too_much_money_spend):
            res = 'Вам слід звернути увагу, на витрату завеликої кількості ' \
                  'коштів. Ви можете економити:\n\n'
            for outgo, per in too_much_money_spend.items():
                res += outgo + ",\tвитрачайте на {} відсотків, " \
                               "від прибутків сім\'ї, менше\n".format(str(
                    round(per, 2)))
        return too_much_money_spend, res

    def more_100_check(self):
        """
        Give pieces of advise about outgoings

        :return:
        """
        too_much_money_spend, res = self.less_100_check()
        res += "\nЗа дотримання вище зазначеної економії, ваші витрати " \
               "будуть унормовані, проте витрат є забагато.\n" \
               "Рекомендація від 'Earn Save Invest' - зменшення кількості " \
               "витрат на другорядні потреби.\n"
        return too_much_money_spend, res

    def __str__(self):
        """
        Return all info about family money percentage

        :return: str
        """
        res = '{}:\nВідсоткові, порівняні витрати сім\'ї\n'.format(
            self.__class__.__name__)
        for person in self.family_percent.members:
            res += str(person) + '\n'
        res += 'місячні витрати на харчування = {};\nмісячні комунальні ' \
               'витрати = {};\nмісячні побутові витрати = {};\nмісячні ' \
               'транспортні витрати = {};\nмісячні витрат на освіту = {' \
               '};\nмісячні витрати на одяг та взуття = {};\nрічні витрати ' \
               'на подорожі = {};\nмісячні несподівані витрати = {};\n' \
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
