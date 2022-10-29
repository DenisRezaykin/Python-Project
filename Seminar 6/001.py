# 1. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Use comprehension.
# in
# 9
#
# out
# [15, 16, 2, 3, 1, 7, 5, 4, 10]
# [16, 3, 7, 10]

from random import sample

def nums(count):
    ls = sample(range(count * 3), count)
    print(ls)
    return [ls[count] for count in range(1, len(ls)) if ls[count] > ls[count - 1]]

print(nums(int(input('Введите число: '))))

