# 5) Реализуйте алгоритм перемешивания списка.

from random import randint


def fill_list_random(n, a, b):
    list = []
    for i in range(n):
        list.append((randint(a, b)))
    return list


# def list_asc(list):
#     mid = len(list) // 2
#     j = 0
#     while j <= mid:
#         index_a = list[len(list)-1-j]
#         temp = list[j]
#         list[j] = list[index_a]
#         list[index_a] = temp
#         j += 1
#     return list


len = int(input("Сколько будет элементов в списке? "))
a = int(input("Нижняя граница диапазона: "))
b = int(input("Верхняя граница диапазона: "))
user_list = fill_list_random(len, a, b)
print(user_list)
user_list_asc = user_list[::-1]
print(user_list_asc)
