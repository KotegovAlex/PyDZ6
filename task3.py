# 3. Задайте список из k чисел последовательности (1 + 1\k)^k и выведите на экран их сумму.

    # Было:
# k = int(input("Введите число k => "))
# i = 0
# sequence = []

# while i < k:
#     sequence.append((1 + 1 / (i + 1))**(i + 1))
#     i += 1

# print(round(sum(sequence), 3))

    # Стало:
print(round(sum([(1 + 1 / (i + 1))**(i + 1) for i in range(int(input("Введите число k => ")))]), 3))