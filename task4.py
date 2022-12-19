# 4) Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на 3 указанных позициях. 

from random import randint

num = int(input("Введите число: "))
list = []
for i in range(num):
    list.append(randint(-num,num))
mult = []
for j in range(1,4):
    mult.append(int(input(f"Введите номер {j} элемента для нахождения произведения в списке от 0 до {num}: ")))
num_mult = 1
for k in mult:
    num_mult *= list[k]
print(list)
print (f"Для данного списка произведение {mult[0]}, {mult[1]} и {mult[2]} элементов равно {num_mult}")