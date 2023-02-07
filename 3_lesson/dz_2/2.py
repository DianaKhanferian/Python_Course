# Задача 2: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai. Последняя строка
# содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5

import os
os.system('cls')

n = int(input("Введите количество элементов в массиве: "))
list = [int(input()) for _ in range(n)]
number = int(input("Число: "))
list.append(number)
list.sort()
if number != max(list):
    index_number = list.index(number)
    if list[index_number] - list[index_number - 1] > list[index_number + 1] - list[index_number]:
        print(f"Сосед числа {number} это {list[index_number + 1]}")
    elif list[index_number] - list[index_number - 1] == list[index_number + 1] - list[index_number]:
        print(f"Сосед числа {number} это {min(list[index_number + 1], list[index_number - 1])}")
    else:
         print(f"Сосед числа {number} это {list[index_number - 1]}")

else:
    print(f"Сосед числа {number} это {list[len(list)-2]}")