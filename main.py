'''

Main file to run all the process

'''
# TODO: import from modules family and utility_bills to cases
from modules.data_collecting.user_input import family_questions_answers
from modules.family_outcome_analysis.family_outcome_an import BasicOutgoings
from modules.data_comparing.compare_data import CompareBasicReal
from modules.data_collecting.family import FamilyPercent
from modules.less_money_cases.less_money_cases import Cases


def use_cases_spend_less_money(too_much_money_spend, fam):
    '''
    Function to show user where and how he/she can save money

    :param too_much_money_spend: dictionary
    :param fam: Family
    :return: str,
    '''

    # TODO: sent family income as attribute

    savings = None
    case = Cases(fam)
    # dictionary
    savings = case.get_all_possible_savings()
    # text
    advise = 'Ви можете заощаджувати, користуючись такими правилами: \n' + \
             case.get_all_cases()
    return advise, savings


def main():
    '''
    Main function to run all the process
    :return: None
    '''
    # Get and print data frm user
    family = family_questions_answers()
    print(family)  # Family

    # data analysis - real and basic percentage
    basic_family_outgoings = BasicOutgoings(family.members)
    print(basic_family_outgoings)  # BasicOutgoings

    real_family_outgoings = FamilyPercent(
        family.get_fam_outdoings_in_percents(), family.members)
    print(real_family_outgoings)  # FamilyPercent

    real_basic_difference = CompareBasicReal(basic_family_outgoings,
                                             real_family_outgoings)
    too_much_money_spend, res = real_basic_difference.create_advise()
    print('fghjk', real_basic_difference)  # CompareBasicReal
    # print data about family outgoings - where too much
    print('RES =', res)  # okay

    # calculation and giving pieces of advise
    # cases to spend less money
    family.saved_percentage_to_UAH(real_basic_difference.all_outgoings,
                                   real_basic_difference.outgoing_names)

    advise_str, dict_savings = use_cases_spend_less_money(
        too_much_money_spend, family)
    print('advise_str', advise_str)  # okay
    print('dict_savings', dict_savings)  # okay

    # update money_box with savings from dict_saving
    family.family_money_box.update(dict_savings)
    print('family_money_box', family.family_money_box) # okay






if __name__ == '__main__':
    main()
