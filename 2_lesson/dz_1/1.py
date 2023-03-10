# Задача 1: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2

import os
os.system('cls')

n = int(input('Введите количество монет: '))
count_one = count_zero = 0

for i in range(n):
    coin = int(input())
    if coin:
        count_one += 1
    else:
        count_zero += 1

if count_one > count_zero:
    print(count_zero)
else:
    print(count_one)