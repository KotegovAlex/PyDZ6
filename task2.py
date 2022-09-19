# 1. Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на чётной позиции.
    # Пример:
    # [2, 3, 5, 9, 3] -> на чётных позициях элементы 3 и 9, ответ: 12

    #  Было:
import random as r

# n = int(input("Задайте длину списка чисел -> "))

# def create_list(length: int, min_value: int, max_value: int):
#     result = []
#     for i in range(0, length):
#         result.append(r.randint(min_value, max_value))
#     return result

# def find_odd_position_sum(input_list: list):
#     result_list = []
#     sum = 0
#     for i in range(1, len(input_list), 2):
#         result_list.append(input_list[i])
#         sum += input_list[i]
#     print(f'На нечетных позициях элементы: {result_list}, сумма равна: {sum}')

# number_list = create_list(n, 0, 10)
# print(number_list)
# find_odd_position_sum(number_list)

    # Стало:
number_list = [r.randint(0, 10) for i in range(int(input('Задайте длину списка чисел -> ')))]
print(number_list)
number_list = [number_list[i] for i in range(1, len(number_list), 2)]
print(f'Элементы на четных позициях: {number_list}, их сумма: {sum(number_list)} ')
