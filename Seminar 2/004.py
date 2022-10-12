# Напишите программу, которая принимает на вход 2 числа.
# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях(не индексах).
# Position one: 1
# Position two: 3
# Number of elements: 5
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# -> 15

Pos_1 = int(input('Введите число: '))
Pos_2 = int(input('Введите число: '))
Num_elem = int(input('Введите число: '))
ls = list()
for i in range(-Num_elem, Num_elem + 1):
    ls.append(i)
print(ls)
A = ls[Pos_1 - 1] * ls[Pos_2 - 1]
print(A)
