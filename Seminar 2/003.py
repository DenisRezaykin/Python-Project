# Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.
# Для n = 6: [2, 2, 2, 2, 2, 3] -> 13

N = int(input('Введите число: '))
ls = list()
sum = 0
for i in range(1, N+1):
    c = round((1 + 1/i) ** i)
    ls.append(c)
    sum += c
print(ls)
print(sum)
