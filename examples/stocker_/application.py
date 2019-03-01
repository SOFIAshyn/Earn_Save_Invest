from stocker import Stocker
import matplotlib.pyplot as plt

# MSFT is in the WIKI database, which is default
microsoft = Stocker(ticker='AAPL')

# TECHM is in the NSE database
# aapl = Stocker(ticker='AAPL', exchange='NASDAQ')

# real plot
# Stocker.plot_stock(microsoft, start_date=microsoft.min_date,
#                    end_date=microsoft.max_date,
#                    stats=['Adj. ''Close'], plot_type='basic')

# prediction
# model, future = Stocker.create_prophet_model(microsoft, days=500,
#                                              resample=False)
# model.plot_components(future)
# plt.show()

# CHECKPOINTS PLOT
# Stocker.changepoint_date_analysis(microsoft, search=None)
# for i in range(3):
Stocker.predict_future(microsoft, days=60)
