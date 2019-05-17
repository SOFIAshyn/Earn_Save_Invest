from modules.stocker.stocker import Stocker
from datetime import datetime
from threading import Timer
import os
import pandas as pd
import re

COMPANIES_FILE = 'docs/nasdaq100list.csv'


def get_stock_info():
    """
    In percentage compare difference of stock market of the company
    Select top 10
    Save data in csv files
    :return: None
    """

    def check_top_10(dict_top_differance, item):
        """
        Check if company can be it top 10 stable companies for next one month
        :param dict_top_differance: dict
        :param item: float
        :return: tuple (bool, bool)
        """
        if len(dict_top_differance) < 10:
            return True, None

        smallest = min(dict_top_differance.values())
        if item > smallest:
            for key, val in dict_top_differance.items():
                if val == smallest:
                    return True, key
        return False, None

    def check_all_100():
        """
        Check all 100 companies and select top 10 for next one month
        :return:dict
        """
        dict_top_differance = {}
        # read top 100 companies from nasdaq
        # file = open('docs/nasdaq100list.csv', 'r')
        file = open(COMPANIES_FILE, 'r')
        for line in file.readlines():
            # get company token
            line = line.strip()
            s = Stocker(line)
            future_increase = s.predict_future(365)

            # get how many percents will be added in next month
            percent_increase = s.check_month_interval(future_increase)

            check_100_add, check_100_val = check_top_10(dict_top_differance,
                                                        percent_increase)
            # if we have to add this token
            if check_100_add:
                dict_top_differance[line] = percent_increase
            # if there is no place and we have to replace values
            if check_100_val:
                del dict_top_differance[check_100_val]

        file.close()
        return dict_top_differance

    # check 100 and choose top 10 for next month
    top_10_key_token = check_all_100()

    for token in top_10_key_token:
        s_general = Stocker(token)
        future_increase_general = s_general.predict_future(365)
        future_increase_general.to_csv(r'tmp/future_{}.csv'.format(
            token), header=True, index=False)


def draw_plots(token, future_increase_general):
    """
    Draw plots to show plots in PLotly
    :return: None
    """
    s = Stocker(token)
    s.show_plots(future_increase_general)


def each_file_plot():
    for future_file in os.listdir('tmp'):
        if 'future' in future_file:
            future_file = 'tmp/' + future_file

            future_increase_general = pd.read_csv(future_file)
            token = re.findall('_\w*.', future_file)[0][1:-1]
            draw_plots(token, future_increase_general)


def get_info_and_clean_old_files():
    """
    Delete yesterday information
    Get infomation from stock (up to date info)
    :return:None
    """
    for future_file in os.listdir('tmp'):
        if 'future' in future_file:
            future_file = 'tmp/' + future_file
            os.unlink(future_file)

    get_stock_info()


def stock_result_top_10():
    '''
    Run all the process with all companies
    :return: None
    '''

    # every day update data at 1 p.m.
    x = datetime.today()
    y = x.replace(day=x.day + 1, hour=1, minute=0, second=0, microsecond=0)
    delta_t = y - x
    secs = delta_t.seconds + 1

    t = Timer(secs, get_info_and_clean_old_files)
    t.start()

    # after upate save data to file
    # we don't need to do it because this process runs everyday at 1 p.m.
    # get_stock_info()

    # read data from csv and save in to DataFrame pd, show plot
    each_file_plot()
