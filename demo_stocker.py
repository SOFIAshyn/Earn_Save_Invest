from modules.stocker.stocker import Stocker


def get_stock_info():
    file = open('docs/companies.csv', 'r')
    for line in file.readlines():
        line = line.strip()
        s = Stocker(line)
        s.predict_future(365)
    file.close()


def main():
    '''
    Run all the process with all companies
    :return: None
    '''
    get_stock_info()


if __name__ == '__main__':
    main()
