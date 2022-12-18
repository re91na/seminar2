# 1) Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

num = (input("Введите число: "))
sum = 0
num_list = list(num.split("."))
len = len(num_list)
i = 0
while i < len:
    num_int = int(num_list[i])
    while num_int > 0:
        sum = sum + num_int % 10
        num_int = num_int//10
    i = i +1
print(sum)