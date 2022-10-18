# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
# in
# 5
#
# out
# [10, 2, 3, 8, 9]
# 22
#
# in
# 4
#
# out
# [4, 2, 4, 9]
# 8

import random


def sum_nums(count):
    if count < 0:
        return "Ошибка"
    ls = random.sample(range(count * 2), count)
    print(ls)
    print(sum(ls[0::2]))


num = int(input('Введите число: '))
print(sum_nums(num))
