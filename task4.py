# 4. Задайте список. Напишите программу, которая определит, 
# присутствует ли в заданном списке строк некое число.
    # ['efg23', '79234gefg', 'sdgs', 'g53']
    # '2'
    # ['efg23', '79234gefg']


    # Было:
# def find(input_list:list, find_str: str):
#     output_list = []
#     for i in input_list:
#         if find_str in i:
#             output_list.append(i)
#     return output_list

# list_1 = ['efg23', '79234gefg', 'sdgs', 'g53']
# str_1 = '2'

# print(find(list_1, str_1))


    # Стало:
list_2 = ['efg23', '79234gefg', 'sdgs', 'g53']
str_2 = '2'
print(tuple(filter(lambda x: str_2 in x, list_2)))