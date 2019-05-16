from modules.stocker.stocker import Stocker


def get_stock_info():
    """
    In percentage compare difference of stock market of the company
    Select top 10
    Call functions to show plots in PLotly
    :return: None
    """
    lst_top_differance = {}
    file = open('docs/nasdaq100list.csv', 'r')
    for line in file.readlines():
        line = line.strip()
        s = Stocker(line)
        future_increase = s.predict_future(365)
        percent_increase = s.check_month_interval(future_increase)
        if check_top_10(lst_top_differance):
            pass
    file.close()


def main():
    '''
    Run all the process with all companies
    :return: None
    '''
    # get_stock_info()
    s = Stocker('MSFT')
    s.predict_future(365)


if __name__ == '__main__':
    main()
