import pandas as pd
import numpy as np
import fbprophet

import matplotlib.pyplot as plt
import matplotlib
import datetime as dt
import pandas_datareader.data as web
from modules.plots.main_plot import company_middle_plot


class Stocker:
    """
    Class for analyzing and (attempting) to predict future prices
    Contains a number of visualizations methods
    """

    def __init__(self, ticker):
        """
        Initialization requires a ticker symbol

        :param ticker: str
        """

        # Enforce capitalization
        ticker = ticker.upper()

        # Symbol is used for labeling plots
        self.symbol = ticker
        self.df = None

        # Retrieval the financial data
        try:
            start = dt.datetime(1989, 1, 29)
            end = dt.datetime.today()

            self.df = web.DataReader(self.symbol, 'yahoo', start, end)


        except Exception as e:
            print('Error Retrieving Data.')
            print(e)
            return

        # Set the index to a column called Date
        self.df = self.df.reset_index(level=0)

        # Columns required for prophet
        self.df['ds'] = self.df['Date']

        self.df['y'] = self.df['Close']
        self.df['Daily Change'] = self.df['Close'] - self.df['Open']

        # Data assigned as class attribute
        self.stock = self.df.copy()

        # Minimum and maximum date in range
        self.min_date = min(self.df['Date'])
        self.max_date = max(self.df['Date'])

        # Find max and min prices and dates on which they occurred
        self.max_price = np.max(self.stock['y'])
        self.min_price = np.min(self.stock['y'])

        self.min_price_date = self.stock[self.stock['y'] == self.min_price][
            'Date']
        self.min_price_date = self.min_price_date[self.min_price_date.index[0]]
        self.max_price_date = self.stock[self.stock['y'] == self.max_price][
            'Date']
        self.max_price_date = self.max_price_date[self.max_price_date.index[0]]

        # The starting price (starting with the opening price)
        self.starting_price = float(self.stock.ix[0, 'Open'])

        # The most recent price
        self.most_recent_price = float(self.stock.ix[len(self.stock) - 1, 'y'])

        # Whether or not to round dates
        self.round_dates = True

        # Number of years of data to train on
        self.training_years = 3

        # Prophet parameters
        # Default prior from library
        self.changepoint_prior_scale = 0.05
        self.weekly_seasonality = False
        self.daily_seasonality = False
        self.monthly_seasonality = True
        self.yearly_seasonality = True
        self.changepoints = None

        print(
            '{} Stocker Initialized. Data covers {} to {}.'.format(self.symbol,
                                                                   self.min_date.date(),
                                                                   self.max_date.date()))

    def handle_dates(self, start_date, end_date):
        """
        Make sure start and end dates are in the range and can be
        converted to pandas datetimes. Returns dates in the correct format
        """

        # Default start and end date are the beginning and end of data
        if start_date is None:
            start_date = self.min_date
        if end_date is None:
            end_date = self.max_date

        try:
            # Convert to pandas datetime for indexing dataframe
            start_date = pd.to_datetime(start_date)
            end_date = pd.to_datetime(end_date)

        except Exception as e:
            print('Enter valid pandas date format.')
            print(e)
            return

        valid_start = False
        valid_end = False

        # User will continue to enter dates until valid dates are met
        while (not valid_start) & (not valid_end):
            valid_end = True
            valid_start = True

            if end_date.date() < start_date.date():
                print('End Date must be later than start date.')
                start_date = pd.to_datetime(input('Enter a new start date: '))
                end_date = pd.to_datetime(input('Enter a new end date: '))
                valid_end = False
                valid_start = False

            else:
                if end_date.date() > self.max_date.date():
                    print('End Date exceeds data range')
                    end_date = pd.to_datetime(input('Enter a new end date: '))
                    valid_end = False

                if start_date.date() < self.min_date.date():
                    print('Start Date is before date range')
                    start_date = pd.to_datetime(
                        input('Enter a new start date: '))
                    valid_start = False

        return start_date, end_date

    # Reset the plotting parameters to clear style formatting
    # Not sure if this should be a static method
    @staticmethod
    def reset_plot():
        """
        Reset the plotting parameters to clear style formatting
        Not sure if this should be a static method
        :return: None
        """

        # Restore default parameters
        matplotlib.rcParams.update(matplotlib.rcParamsDefault)

        # Adjust a few parameters to liking
        matplotlib.rcParams['figure.figsize'] = (8, 5)
        matplotlib.rcParams['axes.labelsize'] = 10
        matplotlib.rcParams['xtick.labelsize'] = 8
        matplotlib.rcParams['ytick.labelsize'] = 8
        matplotlib.rcParams['axes.titlesize'] = 14
        matplotlib.rcParams['text.color'] = 'k'

    def remove_weekends(self, dataframe):
        """
        Remove weekends from a dataframe
        :param dataframe: pandas DataFrame
        :return: pandas DataFrame
        """

        # Reset index to use ix
        dataframe = dataframe.reset_index(drop=True)

        weekends = []

        # Find all of the weekends
        for i, date in enumerate(dataframe['ds']):
            if (date.weekday()) == 5 | (date.weekday() == 6):
                weekends.append(i)

        # Drop the weekends
        dataframe = dataframe.drop(weekends, axis=0)

        return dataframe

    def create_model(self):
        """
        Create a prophet model without training
        :return: Prophet
        """
        # Make the model
        model = fbprophet.Prophet(daily_seasonality=self.daily_seasonality,
                                  weekly_seasonality=self.weekly_seasonality,
                                  yearly_seasonality=self.yearly_seasonality,
                                  changepoint_prior_scale=self.changepoint_prior_scale,
                                  changepoints=self.changepoints)

        if self.monthly_seasonality:
            # Add monthly seasonality
            model.add_seasonality(name='monthly', period=30.5, fourier_order=5)

        return model

    def predict_future(self, days=70):
        """
        Predict the future price for a given range of days
        :param days: int
        :return: pandas DataFrame
        """
        # Use past self.training_years years for training
        train = self.stock[self.stock['Date'] > (
                max(self.stock['Date']) - pd.DateOffset(
            years=self.training_years)).date()]

        print(type(self.stock['Date']), self.stock['Date'])

        model = self.create_model()

        model.fit(train)

        # Future dataframe with specified number of days to predict
        future = model.make_future_dataframe(periods=days, freq='D')
        future = model.predict(future)

        # Only concerned with future dates
        future = future[future['ds'] >= max(self.stock['Date']).date()]

        # Remove the weekends
        future = self.remove_weekends(future)

        # Calculate whether increase or not
        future['diff'] = future['yhat'].diff()

        future = future.dropna()

        # Find the prediction direction and create separate dataframes
        future['direction'] = (future['diff'] > 0) * 1

        # Rename the columns for presentation
        future = future.rename(
            columns={'ds': 'Date', 'yhat': 'estimate', 'diff': 'change',
                     'yhat_upper': 'upper', 'yhat_lower': 'lower'})

        future_increase = future[future['direction'] == 1]
        future_decrease = future[future['direction'] == 0]

        future_increase = future_increase[
            ['Date', 'estimate', 'change', 'upper', 'lower']]

        # Print out the dates
        # print('\nPredicted Increase: \n')
        # print(
        #     type(future_increase[['Date', 'estimate', 'change', 'upper',
        #                           'lower']]))
        # print(future_increase)
        # file = open(r'modules\tmp\future_increase.csv', 'w+')
        # file.write('s')
        # future_increase.to_csv(r'tmp\future_increase.csv', index=False,
        #                        header=False)

        # print('\nPredicted Decrease: \n')
        # print(
        #     future_decrease[['Date', 'estimate', 'change', 'upper', 'lower']])

        return future_increase

        # Plot in matplot lib with errorbar
        # self.reset_plot()
        #
        # # Set up plot
        # plt.style.use('fivethirtyeight')
        # matplotlib.rcParams['axes.labelsize'] = 10
        # matplotlib.rcParams['xtick.labelsize'] = 8
        # matplotlib.rcParams['ytick.labelsize'] = 8
        # matplotlib.rcParams['axes.titlesize'] = 12
        #
        # # Plot the predictions and indicate if increase or decrease
        # fig, ax = plt.subplots(1, 1, figsize=(8, 6))
        #
        # # Plot the estimates
        # ax.plot(future_increase['Date'], future_increase['estimate'], 'g^',
        #         ms=12, label='Pred. Increase')
        # ax.plot(future_decrease['Date'], future_decrease['estimate'], 'rv',
        #         ms=12, label='Pred. Decrease')
        #
        # # Plot errorbars
        # ax.errorbar(future['Date'].dt.to_pydatetime(), future['estimate'],
        #             yerr=future['upper'] - future['lower'],
        #             capthick=1.4, color='k', linewidth=2,
        #             ecolor='darkblue', capsize=4, elinewidth=1,
        #             label='Pred with Range')
        #
        # # Plot formatting
        # plt.legend(loc=2, prop={'size': 10})
        # plt.xticks(rotation='45')
        # plt.ylabel('Predicted Stock Price (US $)')
        # plt.xlabel('Date')
        # plt.title('Predictions for %s' % self.symbol)
        # plt.show()

    def check_month_interval(self, future_increase):
        """
        Check future increase or decrease
        how many percents will be added in next month
        :param future_increase: pandas DataFrame
        :return: float
        """
        # price of company on stock at the begining of month
        start = future_increase['estimate'].iloc[0]
        # price of company on stock at the end of month
        end_month = future_increase['estimate'].iloc[29]

        # percentage of last of month option
        per_end_month = end_month * 100 / start

        # how many percents will be added in next month
        increase_per = per_end_month - 100

        return increase_per

    def show_plots(self, future_increase):
        """
        Calculate company and how many may it earn / get
        :return: float
        """
        company_middle_plot(future_increase['Date'],
                            future_increase['estimate'], self.symbol)
