from bs4 import BeautifulSoup
import pandas as pd


def parser():
    # Формат: список транзакций, каждая транзакция - словарь
    # { 'shop': ... , 'date': ... , 'cost': ... , 'category': ... }
    result = []

    with open('index.html', 'r') as f:
        file_to_parse = f.read()

    soup = BeautifulSoup(file_to_parse, 'html.parser')
    soup.prettify()

    trs = soup.find_all('div', {'class': 'trs_it'})

    for tr in trs:
        tr_data = tr.contents[0]

        # 1. Магазин
        tr_shop = tr_data.contents[0].text.strip()

        # 2. Дата транзакции (строка)
        tr_date = str(tr_data.contents[1].contents[1]['data-date'])

        # 3. Стоимость
        tr_cost_parent = tr_data.contents[2].contents[2].contents[0]
        tr_cost_head = str(tr_cost_parent.contents[0])
        tr_cost_tail = str(tr_cost_parent.contents[1].contents[0])
        tr_cost = tr_cost_head + tr_cost_tail

        # Нормализуем стоимость
        tr_cost = tr_cost.replace(',', '.')
        tr_cost = tr_cost.replace('\u202f', '')
        tr_cost_number = float(tr_cost)
        tr_cost = '{:.2f}'.format(tr_cost_number)

        # 4. Категория
        tr_cat = tr_data.contents[3].contents[1].contents[0].contents[0]

        result.append({
            'date': tr_date,
            'category': tr_cat,
            'shop': tr_shop,
            'cost': tr_cost,
        })

    return result


def convert_to_dataframe(parsed_data):
    converted_data = {}
    keys = list(parsed_data[0].keys())
    for key in keys:
        values = []
        for tr in parsed_data:
            values.append(tr[key])
        converted_data[key] = values
    return converted_data


def export_to_excel(data):
    dframe = pd.DataFrame(data)
    dframe.to_excel('transactions.xlsx', index=False)


def export_to_csv(data):
    dframe = pd.DataFrame(data)
    dframe.to_csv('transactions.csv', index=False)
