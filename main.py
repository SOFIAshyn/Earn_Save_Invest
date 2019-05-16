"""

Main file to run all the process

"""
# TODO: import from modules family and utility_bills to cases
from modules.data_collecting.user_input import family_questions_answers
from modules.family_outcome_analysis.family_outcome_an import BasicOutgoings
from modules.data_comparing.compare_data import CompareBasicReal
from modules.data_collecting.family import FamilyPercent
from modules.less_money_cases.less_money_cases import Cases


def use_cases_spend_less_money(too_much_money_spend, fam):
    """
    Function to show user where and how he/she can save money

    :param too_much_money_spend: dictionary
    :param fam: Family
    :return: str,
    """

    # TODO: sent family income as attribute

    savings = None
    case = Cases(fam)
    # dictionary
    savings = case.get_all_possible_savings()
    # text
    advise = 'Ви можете заощаджувати, користуючись такими правилами: \n' + \
             case.get_all_cases()
    return advise, savings


def count_general_savings(family_money_box):
    """
    Return general sum of savings
    :return:float
    """
    general_summary = 0
    for key, val in family_money_box.items():
        if isinstance(val, dict):
            for v in val.values():
                general_summary += v
        else:
            # if < 0 -> family spend money on it correctly, even they have
            # some savings that are equal to val
            if val > 0:
                general_summary += val
    return round(general_summary, 2)


def print_family_general_savings(family_money_box):
    res = ''
    for key, val in family_money_box.items():
        if isinstance(val, dict):
            res += key + ':\n'
            for k, v in val.items():
                res += '\t' + k + ': ' + str(v) + '\n'
        elif val > 0:
            res += key + ': ' + str(val) + '\n'
    return res


def main():
    """
    Main function to run all the process
    :return: None
    """
    # TODO: uncomment
    # # Get and print data frm user
    # family = family_questions_answers()
    # print(family)  # Family
    #
    # # data analysis - real and basic percentage
    # basic_family_outgoings = BasicOutgoings(family.members)
    # print(basic_family_outgoings)  # BasicOutgoings
    #
    # real_family_outgoings = FamilyPercent(
    #     family.get_fam_outdoings_in_percents(), family.members)
    # print(real_family_outgoings)  # FamilyPercent
    #
    # real_basic_difference = CompareBasicReal(basic_family_outgoings,
    #                                          real_family_outgoings)
    # too_much_money_spend, res = real_basic_difference.create_advise()
    # print('fghjk', real_basic_difference)  # CompareBasicReal
    # # print data about family outgoings - where too much
    # print('RES =', res)  # okay
    #
    # # calculation and giving pieces of advise
    # # cases to spend less money
    # family.saved_percentage_to_UAH(real_basic_difference.all_outgoings,
    #                                real_basic_difference.outgoing_names)
    #
    # advise_str, dict_savings = use_cases_spend_less_money(
    #     too_much_money_spend, family)
    # # print('advise_str', advise_str)  # okay
    # # print('dict_savings', dict_savings)  # okay
    #
    # # update money_box with savings from dict_saving
    # family.family_money_box.update(dict_savings)
    # # print('family_money_box', family.family_money_box)  # okay
    #
    # # general sum that can be saved because of our program
    # general_sum = count_general_savings(family.family_money_box)
    # print(general_sum)

    # TODO: DELETE
    general_sum = 1000

    # DO MAGIC WITH SAVED SUM
    print('Вітаємо!\n{} - це гроші, які ви можете заощадити за місяць часу, '
          'якщо будете дотримуватись правил збереження коштів та будете '
          'вкладати прибуток у ресурси, які приносять додаткові '
          'кошти.\n\nРекомендуємо Вам переглянути ресурси для '
          'вкладів:'.format(general_sum))

    # give data about banks

    # give data of stock market

    # give data about hryvna


if __name__ == '__main__':
    main()
