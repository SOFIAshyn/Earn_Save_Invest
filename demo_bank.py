from modules.bank import *

cur_incomes = 10000

b = BankType(cur_incomes)
a = b.banks_processing()
print(sorted(a, key=lambda x: x.index))

# print(b.conditions)
# for each in a:
#     print(each)
# for program in each.programs:
#     print(program)
