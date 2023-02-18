# Задача 2: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1,
# 4, -2, 10, 2, 0, -9, 8, 10, -9,
# 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

import os
os.system('cls')

k = list(map(int, input('Введите массив: ').split()))

min = int(input('Min: '))
max = int(input('Max: '))
print(*[i for i in range(len(k)) if min <= k[i] <= max])


# ---Решение преподавателя---

# nums_list = [int(i) for i in input().split()]
# num_min = int(input())
# num_max = int(input())

# print([ind for ind, val in enumerate(nums_list) if num_min <= val <= num_max])

