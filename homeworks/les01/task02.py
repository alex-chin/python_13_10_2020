"""
 2. Пользователь вводит время в секундах.
 Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
 Используйте форматирование строк.
"""

from datetime import time, tzinfo, timedelta

seconds = int(input('Введите время в секундах: '))

num_hours = seconds // 3600
num_minutes = (seconds % 3600) // 60
num_seconds = seconds % 60

print(f'Введено время: {num_hours}:{num_minutes}:{num_seconds}')
print(f'В секундах: {num_hours * 3600 + num_minutes * 60 + num_seconds}')
