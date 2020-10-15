"""
5. Запросите у пользователя значения выручки и издержек фирмы.
 Определите, с каким финансовым результатом работает фирма
 (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
 Выведите соответствующее сообщение.
 Если фирма отработала с прибылью, вычислите рентабельность выручки
 (соотношение прибыли к выручке).
 Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
"""
revenue = int(input('Введите значения выручки (тыс.): '))
costs = int(input('Введите значения издержек (тыс.): '))

if revenue > costs:
    print("Предприятие работает с прибылью!")
    income = revenue - costs;  # доход = операционная выручка - расходы
    print(f'Рентабельность выручки: {(income / revenue) * 100}%')  # todo проверить вычисление рентабельности
    num_member = int(input('Введите численность сотрудников: '))
    print('Прибыль фирмы в расчете на одного сотрудника (тыс.): ', income / num_member)
else:
    print("Предприятие работает в убыток...")
