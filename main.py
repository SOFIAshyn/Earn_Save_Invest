'''

Main file to run all the process

'''
# TODO: import from modules family and utility_bills to cases
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
    last = None
    res = 'Ви можете заощаджувати, користуючись такими правилами: \n'
    cases = (CaseUtilityBills(), CaseFood(), CaseHousehold(), CaseTransport(),
             CaseUnknown(), CaseClothes(), CaseTrips(), CaseEducation(),
             CaseEntertainment())
    for key in too_much_money_spend.keys():
        for case in cases:
            if key == case.name:
                # add info about saving money and spending them less
                res += case.add_case()
                case.get_all_possible_savings()
            last = case
    print(last.SAVINGS)
    return res, last.SAVINGS


def main():
    '''
    Main function to run all the process
    :return: None
    '''
    # Get and print data frm user
    family = family_questions_answers()
    print(family)

    # data analysis - real and basic percentage
    basic_family_outgoings = BasicOutgoings(family.members)
    print(basic_family_outgoings)
    real_family_outgoings = FamilyPercent(
        family.get_fam_outdoings_in_percents(), family.members)
    print(real_family_outgoings)

    real_basic_difference = CompareBasicReal(basic_family_outgoings,
                                             real_family_outgoings)
    too_much_money_spend, res = real_basic_difference.create_advise()
    print(real_basic_difference)
    # print data about family outgoings - where too much
    print(res)

    # calculation and giving pieces of advise
    # cases to spend less money
    family.saved_percentage_to_UAH(real_basic_difference.all_outgoings,
                                   real_basic_difference.outgoing_names)

    advise_str, dict_savings = use_cases_spend_less_money(too_much_money_spend)
    print(advise_str)
    family.family_money_box.update(dict_savings)
    print(family.family_money_box)


if __name__ == '__main__':
    main()
