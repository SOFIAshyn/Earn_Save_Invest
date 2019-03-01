from alpha_vantage.timeseries import TimeSeries
from stocker import Stocker
import matplotlib.pyplot as plt
import pandas as pd
import json



def main():
    microsoft = Stocker(ticker='MSFT')
    Stocker.predict_future(microsoft, days=60)


if __name__ == "__main__":
    main()
