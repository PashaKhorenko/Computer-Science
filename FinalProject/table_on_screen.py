from prettytable import PrettyTable
from FinalProject.data import data_array
from FinalProject.data import enterprises_array

first_table = PrettyTable()

first_table.field_names = ['Код', 'Період', 'Товарообіг', 'Балансовий прибуток',
                           'Середньорічна вартість основних засобів']

for enterprise_activity in data_array:
    first_table.add_row([enterprise_activity.code, enterprise_activity.period,
                         enterprise_activity.commodity_circulation,
                         enterprise_activity.balance_income,
                         enterprise_activity.average_cost_main_components])

code_one_table = PrettyTable()

code_one_table.field_names = ['Код', 'Період', 'Товарообіг', 'Балансовий прибуток',
                              'Середньорічна вартість основних засобів']

for enterprise_activity in data_array:
    if enterprise_activity.code == 1:
        code_one_table.add_row([enterprise_activity.code, enterprise_activity.period,
                                enterprise_activity.commodity_circulation,
                                enterprise_activity.balance_income,
                                enterprise_activity.average_cost_main_components])

code_two_table = PrettyTable()

code_two_table.field_names = ['Код', 'Період', 'Товарообіг', 'Балансовий прибуток',
                              'Середньорічна вартість основних засобів']

for enterprise_activity in data_array:
    if enterprise_activity.code == 2:
        code_two_table.add_row([enterprise_activity.code, enterprise_activity.period,
                                enterprise_activity.commodity_circulation,
                                enterprise_activity.balance_income,
                                enterprise_activity.average_cost_main_components])

code_three_table = PrettyTable()

code_three_table.field_names = ['Код', 'Період', 'Товарообіг', 'Балансовий прибуток',
                                'Середньорічна вартість основних засобів']

for enterprise_activity in data_array:
    if enterprise_activity.code == 3:
        code_three_table.add_row([enterprise_activity.code, enterprise_activity.period,
                                  enterprise_activity.commodity_circulation,
                                  enterprise_activity.balance_income,
                                  enterprise_activity.average_cost_main_components])

second_table = PrettyTable()

second_table.field_names = ['Код', 'Назва підприємства']

for enterprise in enterprises_array:
    second_table.add_row([enterprise.code, enterprise.name])

while True:
    command = str(input(
        "Щоб вивести Табл.1 натисніть 1. Щоб вивести на екран Табл.2 натисніть 2. \n"
        "Щоб вивести підприємство за кодом напишіть Код і номер підприємстав, наприклад Код 1\n"
        "Щоб завершити роботу натисніть "
        "будь-яку іншу клавішу \n"))

    if command == "1":
        print(first_table)
    elif command == "2":
        print(second_table)
    elif command == "Код 1":
        print(code_one_table)
    elif command == "Код 2":
        print(code_two_table)
    elif command == "Код 3":
        print(code_three_table)
    else:
        print("До побачення")
        break
