"""

3. Узнайте у пользователя число n.
Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3.
Считаем 3 + 33 + 333 = 369.

"""

num1 = input('Введите число: ')  # воод ввод числа
num_digits = len(num1)
num1 = int(num1)
summa = 0  # общая сумма
digits = 0

for rank in range(0, 3 * num_digits, num_digits):
    digits += num1 * 10 ** rank  #
    summa += digits

print('Сумма чисел :', summa)
