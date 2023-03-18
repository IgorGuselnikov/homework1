"""
Задание 4.

Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки).
Выведите соответствующее сообщение. Если фирма отработала с прибылью,
вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите
прибыль фирмы в расчете на одного сотрудника.

Пример:
Введите выручку фирмы: 1000
Введите издержки фирмы: 500
Финансовый результат - прибыль. Ее величина: 500
Значит вычисляем рентабельность выручки (соотношение прибыли к выручке)
Рентабельность выручки = 0.5
Введите численность сотрудников фирмы: 10
Прибыль фирмы в расчете на одного сотрудника = 50.0s
"""

print("Введите выручку компании в рублях: ")
earnings_company = int(input())
print("Введите издержки компании в рублях: ")
cost_company = int(input())
if earnings_company > cost_company:
    profit = earnings_company - cost_company
    profitability = round(profit/earnings_company, 2)
    print(f"Финансовый результат - прибыль. Ее величина: {profit} руб.")
    print(f"Рентабельность выручки составляет: {profitability * 100}%")
    print("Введите численность сотрудников фирмы: ")
    people_value = int(input())
    profit_on_one_person = round(profit/people_value, 2)
    print(f"Прибыль фирмы в расчете на одного сотрудника = {profit_on_one_person} руб.")
elif earnings_company == cost_company:
    print("Финансовый результат - сработали в 'ноль'. Нужно что то делать,чтобы не раззорился бизнес")
else:
    print("Финансовый результат - убыток. Нужно что то делать,чтобы не раззорился бизнес")