'''

Main file to run all the process

'''
from modules.data_collecting.user_input import family_questions_answers


def main():
    # Get and print data frm user
    family = family_questions_answers()
    print(family)




if __name__ == '__main__':
    main()
