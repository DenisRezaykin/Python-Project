# Программа, которая принимает на вход число N и выдает последовательность из N членов
# in 5 out 1, -3, 9, -27, 81
# number = int(input('Введите число: '))
# num = 1
# for i in range(number):
#     print(num, end=" ")
#     num *= -3
#
# Создать список, длины n, значения формируются по формуле 3k+1, где k принимает значения от 1 до n включительно
# in 3 out [4, 7, 10]
#
# N = int(input('Введите число: '))
# ls = list()
# for k in range(1, N+1):
#     ls.append(3*k+1)
# print(ls)
#
# Напишите программу, в которой пользователь будет задавать две строки,
# программа - определять количество вхождений одной строки в другой.
# in
# gipopotampo
# po
# out 3
#
# Задайте список, состоящий из произвольных чисел, количество задает пользователь.
# Напишите программу, определяющую присутствует ли в заданном списке число, полученное от пользователя.
#
# import random
#
#
# def magic(count, find_num2):
#     if count < 0:
#         return "Ошибка"
#     ls = random.sample(range(count * 2), count)
#     print(ls)
#     if find_num2 in ls:
#         return "Yes"
#     return "No"
#
# num1 = int(input('Введите число: '))
# num2 = int(input('Введите число: '))
# print(magic(num1, num2))
#
#
# Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число.
# В качестве разделителя используйте пробел.
#
# num = input().split() # разбивка на список слов
#
# def my_func(string_val):
#     for index in string_val:  # перебор списка слов
#         if not index.replace("-", "").isdigit():  # метод isdigit проверяет, содержит ли строка только символы
#             return []
#     return string_val
#
#
# def min_sum(val):
#     art = my_func(val)
#     if art:
#         return min(art, key=int), max(art, key=int)
#     else:
#         return []
#
#
# print(min_sum(input().split()))
#
#
# Найдите корни квадратного уравнения Ax^2 + Bx + C = 0 с помощью корня модуля. Запросите значения A, B, C 3раза
# Уравнения и корни запишите в файл.

# from math import sqrt
#
# print("Введите коэффиценты квадратного уравнения")
# a = float(input("a = "))
# b = float(input("b = "))
# c = float(input("c = "))
#
# d = b ** 2 - 4 * a * c  # дискриминант
# sqrtd = sqrt(d)
#
# with open("temp.txt", "a", encoding="utf-8") as output:  # encoding="utf-8" - кодировка
#     output.write(f"Уравнение: {a} * x ^ 2 + {b} * x + {c}\n ")
#     if d > 0 and a:
#         x1 = (-b + sqrtd) / (2 * a)
#         x2 = (-b - sqrtd) / (2 * a)
#         output.write(f"Корни уравнения: {x1, x2}\n")
#     elif (int(d)) == 0:
#         x = -b / (2 * a)
#         output.write(f"Единственный корень: {x}\n")
#     else:
#         output.write("Rорней нет\n")

# Задайте два числа. Найти наименьшее общее кратное этих чисел

from math import gcd
print("Введите два числа: ")
a = int(input("a = "))
b = int(input("b = "))

def nok(first, second):
    return(first*second) // gcd(first, second) #Данная функция возвращает наибольший общий делитель аргументов a, b.
    # Если a и b отличны от нуля, то результат функции есть наибольшее число, на которое a и b делятся нацело.
print(nok(a, b))