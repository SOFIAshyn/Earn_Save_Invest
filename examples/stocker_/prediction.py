from stocker import Stocker
import matplotlib.pyplot as plt

# MSFT is in the WIKI database, which is default
microsoft = Stocker(ticker='MSFT')
print(microsoft)