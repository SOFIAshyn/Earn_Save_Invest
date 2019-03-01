import pandas as pd


def read_companylist(company, path):
    pf = pd.read_csv(path)
    data = set(pf['Symbol'])
    if company in data:
        return company
    else:
        return False


def company_enter(path):
    while True:
        company = input('Company name: ')
        company = read_companylist(company, path)
        if company:
            return company


company_enter('../../docs/companies.csv')
