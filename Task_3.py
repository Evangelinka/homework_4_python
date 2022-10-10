# Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.

import random
random_list = []
length = int(input('Введите длину списка: '))
for i in range(0, length):
    random_list.append(random.randint(1, 9))
print('Исходный список: ', random_list)
print('Список без повторяющихся элементов: ', list(set(random_list)))
