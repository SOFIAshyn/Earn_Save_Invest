#!./Earn_venv/bin/python

"""

Main file to run all the process

"""
from modules.data_collecting.user_input import family_questions_answers
from modules.family_outcome_analysis.family_outcome_an import BasicOutgoings
from modules.data_comparing.compare_data import CompareBasicReal
from modules.data_collecting.family import FamilyPercent
from modules.less_money_cases.less_money_cases import Cases
from modules.bank import *
from modules.stocker import stock_result_top_10


def use_cases_spend_less_money(too_much_money_spend, fam):
    """
    Function to show user where and how he/she can save money
    :param too_much_money_spend: dictionary
    :param fam: Family
    :return: str, dict
    """

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
    """
    Print data for user where and how you have to save money
    :param family_money_box: dict
    :return: None
    """
    res = ''
    check = 0

    for key, val in family_money_box.items():
        if isinstance(val, dict):
            res += key + ':\n'
            for k, v in val.items():
                res += '\t' + k + ': ' + str(v) + '\n'
        elif val > 0:
            if check == 0:
                res += 'Бажано на цю суму менше витрачати грошей на такі ' \
                       'категорії:\n'
            check = 1
            res += key + ': ' + str(val) + '\n'
    print(res)


def main():
    """
    Main function to run all the process
    :return: None
    """
    # Get and print data frm user
    family = family_questions_answers()
    # print(family)  # Family

    while family.check_gen_income():
        print(
            '\nУ вашої сім\'ї дохід не досягає прожиткового мінімуму. '
            'Будь ласка, введіть коректну інформацю:\n')
        family = family_questions_answers()

    # data analysis - real and basic percentage
    basic_family_outgoings = BasicOutgoings(family.members)
    # print(basic_family_outgoings)  # BasicOutgoings

    real_family_outgoings = FamilyPercent(
        family.get_fam_outdoings_in_percents(), family.members)
    print()
    print(real_family_outgoings)  # FamilyPercent

    real_basic_difference = CompareBasicReal(basic_family_outgoings,
                                             real_family_outgoings)
    too_much_money_spend, res = real_basic_difference.create_advise()
    # print(real_basic_difference)  # CompareBasicReal
    # print data about family outgoings - where too much
    print(res)  # okay

    # calculation and giving pieces of advise
    # cases to spend less money
    family.saved_percentage_to_UAH(real_basic_difference.all_outgoings,
                                   real_basic_difference.outgoing_names)

    advise_str, dict_savings = use_cases_spend_less_money(
        too_much_money_spend, family)
    print(advise_str)  # okay
    # print('dict_savings', dict_savings)  # okay

    # update money_box with savings from dict_saving
    family.family_money_box.update(dict_savings)
    # print('family_money_box', family.family_money_box)  # okay
    print_family_general_savings(family.family_money_box)

    # general sum that can be saved because of our program
    general_sum = count_general_savings(family.family_money_box)

    # DO MAGIC WITH SAVED SUM
    print('Вітаємо!\n{} - це гроші, які ви можете накопичити за місяць часу, '
          'якщо будете дотримуватись правил збереження та вкладання коштів '
          '- вкладання прибутку у ресурси, які приносять додаткові '
          'кошти. *(в суму враховано кошти, які ви заощаджуєте щомісяця, '
          'а також не витрачені кошти)'
          '\n\nРекомендуємо Вам переглянути ресурси для '
          'вкладів:\n'.format(general_sum))

    # give data about banks
    print("Рейтинг банківських компаній: ")
    # for future it will be in EUR, USD, now UAH
    b = BankType(general_sum)
    a = b.banks_processing()
    a = sorted(a, key=lambda x: x.index)[::-1][:5]

    for each in a:
        try:
            print(each)
        except TypeError:
            continue

    # give data of stock market
    print("\n\nУ вашому браузері, ви можете побачити 10 графіків, "
          "які показують "
          "поведінку акцій на Міжнародній Фондовій Біржі. Передбачення акцій "
          "'TOП 10' компаній складені на рік вперед.\nEarn Save Invest "
          "рекомендує вам компанії, у які вигідно вкладати кошти протягом "
          "місяця.\nДані про компанії оновлюються щодня о 13:00")
    stock_result_top_10()


if __name__ == '__main__':
    main()
