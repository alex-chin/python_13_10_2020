"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

"""


def client_to_string(name, last_name, year_of_birth, email, phone):
    print(f'{name} {last_name}, {year_of_birth} года рождения, контакты: {email}, {phone}')


client_to_string(name='Николай', last_name='Иронов', year_of_birth=2019, email='ironov@artlebedev.ru',
                 phone='+7 495 926-18-00')
