#  Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random.
# 10
# -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# -> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]

from random import randrange
num = int(input('Введите число: '))
nums_list = list(range(num))
len_list = len(nums_list)
print(nums_list)
for i in range(len_list):
    A = randrange(len_list)
    B = randrange(len_list)
    nums_list[A], nums_list[B] = nums_list[B], nums_list[A]
print(nums_list)
