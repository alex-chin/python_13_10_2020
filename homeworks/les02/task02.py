"""
2. Для списка реализовать обмен значений соседних элементов,
 т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().

"""
str_elem = None
elements = []
sym_stop = {'', ' ', 'q'}  # стоп символы

while str_elem not in sym_stop:  # вводить элементы до стоп символов
    str_elem = input('Введите элемент :')
    if str_elem in sym_stop:  # запретить ввод стоп-символов
        break
    elements.append(str_elem)

part_odd = elements[0::2]  # нечетные элементы
part_even = elements[1::2]  # четные элементы
list_pair = []

for idx in range(len(part_even)):  # проход по количеству четных элементов
    # собираем массив [четный, нечетный]
    list_pair.append(part_even[idx])
    list_pair.append(part_odd[idx])

# список нечетный - добавить последний элемент из нечетного списка
if len(elements) % 2:
    list_pair.append(part_odd[-1])

print(list_pair)
