'''

Main file to run all the process

'''
from modules.data_collecting.user_input import family_questions_answers
from modules.family_outcome_analysis.family_outcome_an import BasicOutgoings



def main():
    # Get and print data frm user
    family = family_questions_answers()
    print(family)

    # data analysis - real and basic percentage
    basic_family_outgoings = BasicOutgoings(len(family.members))
    real_family_outgoings = FamilyPercent(
        family.get_fam_outdoings_in_percents())

    real_basic_difference = (basic_family_outgoings,
                                                       real_family_outgoings)


if __name__ == '__main__':
    main()
