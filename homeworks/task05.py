"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел,
то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

"""
sym_stop = 'q'
is_doing = True
summa = 0
while is_doing:
    buf = input("Введите числа через пробел: ")
    if buf[0] == sym_stop:
        break
    tokens = buf.split()
    for word in tokens:
        if word == sym_stop:
            is_doing = False
            break
        summa += float(word)
    print('Сумма : ', summa)
