from modules.data_collecting import Person, Family
from modules.exceptions.exceptions import IntInvalidInput


def questions_answers():
    num_fam_members = 0
    while not num_fam_members:
        try:
            num_fam_members = num_fam_members()
        except ValueError:
            continue

    family_members = []
    for i in range(num_fam_members):
        person = Person()
        family_members.append(person)

    family = Family(tuple(family_members))


def num_fam_members():
    try:
        num_fam_members = int(input("Скільки людей разом з вами веде "
                                    "бюджет:\n"
                                    "(введіть число)\n0 - сам розпоряджаюсь "
                                    "витратами, 1 - з однією людиною і т.д.)"))
        return num_fam_members
    except IntInvalidInput:
        print(IntInvalidInput.message())

# questions_answers()
