'''

Main file to run all the process

'''
from modules.data_collecting.user_input import family_questions_answers
from modules.family_outcome_analysis.family_outcome_an import BasicOutgoings
from modules.data_comparing.compare_data import CompareBasicReal
from modules.data_collecting.family import FamilyPercent
from modules.less_money_cases.less_money_cases import CaseUtilityBills, \
    CaseFood, CaseHousehold, CaseTransport, CaseUnknown, CaseClothes, \
    CaseTrips, CaseEducation, CaseEntertainment


def use_cases_spend_less_money(too_much_money_spend):
    '''
    Function to show user where and how he/she can save money

    :param too_much_money_spend: dictionary
    :return: str
    '''
    res = 'Ви можете заощаджувати, користуючись такими правилами: \n'
    cases = (CaseUtilityBills(), CaseFood(), CaseHousehold(), CaseTransport(),
             CaseUnknown(), CaseClothes(), CaseTrips(), CaseEducation(),
             CaseEntertainment())
    for key in too_much_money_spend.keys():
        for case in cases:
            if key == case.name:
                # add info about saving money and spending them less
                res += case.add_case()
    return res


def main():
    '''
    Main function to run all the process
    :return: None
    '''
    # Get and print data frm user
    family = family_questions_answers()
    print(family)

    # data analysis - real and basic percentage
    basic_family_outgoings = BasicOutgoings(len(family.members))
    real_family_outgoings = FamilyPercent(
        family.get_fam_outdoings_in_percents())

    real_basic_difference = CompareBasicReal(basic_family_outgoings,
                                             real_family_outgoings)
    too_much_money_spend, res = real_basic_difference.create_advise()
    # print data about family outgoings - where too much
    print(res)

    # calculation and giving pieces of advise
    # cases to spend less money
    advise_str = use_cases_spend_less_money(too_much_money_spend)
    print(advise_str)


if __name__ == '__main__':
    main()
