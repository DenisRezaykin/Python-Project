# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# *Пример:*
#
# - 6 -> да
# - 7 -> да
# - 1 -> нет

# a = int(input('Введите число обозначающее день недели: '))
# if a > 7:
#     print('Такого дня недели не существует')
# elif a > 5:
#     print('Выходной')
# else:
#     print('День недели не является выходным')

print('Выходной') if int(input()) > 5 else print('День недели не является выходным')

# int()
# float()
# bool()
# str()
# a = []

