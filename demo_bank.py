from modules.bank import *

b = BankType()
b.update_information()
a = b.update_instance()
print(sorted(a, key=lambda x: float(x.rating)))
