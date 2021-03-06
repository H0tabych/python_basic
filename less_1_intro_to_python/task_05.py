"""
5. Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма.
Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки. Выведите соответствующее сообщение.
Если фирма отработала с прибылью, вычислите рентабельность выручки.
Это отношение прибыли к выручке. Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчёте
на одного сотрудника.
"""

# Запрос у пользователя наименования фирмы, размеров выручки и издержек
company = input('Введите наименование вашей фирмы: ')
proceed = float(input('Введите сумму выручки вашей фирмы: '))
cost = float(input('Введите сумму издержек вашей фирмы: '))

# Расчёт финансового результата, выручка - издержки
fin_result = proceed - cost

# Определение и вывод показателей: прибыль, безубыточность, убыток
if proceed < cost:
    print(f'Фирма "ООО {company}" работает в убыток, равный {fin_result} у.е.')
elif proceed == cost:
    print(f'Фирма "ООО {company}" безубыточна, но и прибыли не приносит. '
          f'Её финансовый результат равен {fin_result} у.е.')
else:
    print(f'Фирма "ООО {company}" работает с прибылью, равной {fin_result} у.е.')
    #  Расчёт рентабельности выручки
    profit_cost = proceed / cost
    print(f'Рентабельность выручки равна {profit_cost:.2f} у.е.')
    headcount = float(input('Для определения прибыли в расчёте на одного сотрудника, '
                      'необходимо ввести численность сотрудников фирмы: '))
    #  Расчёт и вывод прибыли в расчёте на одного сотрудника
    fin_result_per_employee = fin_result / headcount
    print(f'Прибыль фирмы в расчёте на одного сотрудника равна {fin_result_per_employee:.2f} у.е.')
