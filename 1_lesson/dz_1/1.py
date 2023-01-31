# Задача 1: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

num = int(input())
num_sum = 0

while num:
    num_sum += num % 10
    num //=10

print(num_sum)