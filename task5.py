# 5) Реализуйте алгоритм перемешивания списка.

from random import randint


def fill_list_random(n, a, b):
    list = []
    for i in range(n):
        list.append((randint(a, b)))
    return list


len = int(input("Сколько будет элементов в списке? "))
a = int(input("Нижняя граница диапазона: "))
b = int(input("Верхняя граница диапазона: "))
user_list = fill_list_random(len, a, b)
print(user_list)
user_list_asc = user_list[::-1]
print(user_list_asc)
