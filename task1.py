# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
    # - 0,56 -> 11

    # Было:
# import math

# number = str(math.fabs(float(input("Введите число => "))))
# number = number.replace('.', '')
# sum = 0
# for n in number:
#     sum += int(n)
# print(f"Сумма цифр числа равна {sum}")

    # Стало:

number_digits = [digit for digit in (input('Введите число => ')) if digit != '.']
print(sum(tuple(map(int, number_digits))))