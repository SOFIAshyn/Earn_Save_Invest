class Person:
    def __init__(self,
                 age: int,
                 worked: bool,
                 workplace=None,
                 incomes=None,
                 extra_incomes=None,
                 hours_on_work=None,
                 saving=None):
        self.worked = worked
        self.age = age
        self.workplace = workplace
        self.incomes = incomes
        self.extra_incomes = extra_incomes
        self.hours_on_work = hours_on_work
        self.saving = saving

    def __repr__(self):
        return 'age: {}; workplace: {}'.format(self.age, self.workplace)


class Family:
    def __init__(self,
                 members: list,
                 benefits: int,
                 out_food: int,
                 out_utility_bills: int,
                 out_household: int,
                 out_transport: int,
                 out_clothes: int,
                 out_unknown=None,
                 saving=None):
        self.members = members
        self.benefits = benefits
        self.out_food = out_food
        self.out_utility_bills = out_utility_bills
        self.out_household = out_household
        self.out_transport = out_transport
        self.out_clothes = out_clothes
        self.out_unknown = out_unknown
        self.saving = saving

    def __repr__(self):
        return ''.join(self.members)
