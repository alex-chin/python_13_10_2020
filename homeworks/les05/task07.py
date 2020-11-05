"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""
import json

with open('task07in.txt', 'r', encoding='utf-8') as file:
    num_company = 0
    sum_company = 0
    dict_company = dict()
    for line in file:
        words = line.split()
        name_company, type_company, income_company, costs_company = words[0], words[1], int(words[2]), int(words[3])
        profit_company = income_company - costs_company
        if profit_company > 0:
            num_company += 1
            sum_company += profit_company
        dict_company[name_company] = profit_company
ledger_companies = [dict_company, {'average_profit': sum_company / num_company}]
# print(json.dumps(ledger_companies,indent=4))

with open('task07out.json', 'w', encoding='utf-8') as file:
    json.dump(ledger_companies, file, indent=4)
