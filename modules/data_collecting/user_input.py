'''

Module to get information from user about family and each person.
Collect all the data and return it.

'''
from modules.data_collecting import Person, Family
from modules.exceptions.exceptions import IntInvalidInput


def family_questions_answers():
    '''
    Unite all the people to family
    Return family

    :return: Family
    '''
    num_fam_members = None
    while not num_fam_members:
        try:
            num_fam_members = fam_members()
        except ValueError:
            continue

    family_members = []
    for i in range(num_fam_members):
        person = Person(i)
        family_members.append(person)

    family = Family(family_members)

    return family


def fam_members():
    '''
    Return number of family members

    :return: int
    '''
    try:
        num_fam_members = int(input("Скільки людей разом з вами веде "
                                    "бюджет:\n"
                                    "(введіть число)\n1 - сам розпоряджаюсь "
                                    "витратами, 2 - з однією людиною і "
                                    "т.д.)"))
        return int(num_fam_members)
    except ValueError:
        print(IntInvalidInput().message())


if __name__ == '__main__':
    family = family_questions_answers()
    print(family)

