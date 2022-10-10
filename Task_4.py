# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k.
# Пример:
# k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

k = int(input('Введите натуральную степень: '))


def write_file(cp):
    with open('Task_4.txt', 'w') as data:
        data.write(cp)


def create_list(k):
    random_list = []
    for i in range(0, k+1):
        random_list.append(random.randint(0, 100))
    return random_list


def create_polynominal(random_list):
    random_list = random_list[::-1]
    polynominal = ''
    if len(random_list) < 1:
        polynominal = 'x = 0'
    else:
        for i in range(len(random_list)):
            if i != len(random_list) - 1 and random_list[i] != 0 and i != len(random_list) - 2:
                polynominal += f'{random_list[i]}x^{len(random_list) - i - 1}'
                if random_list[i + 1] != 0:
                    polynominal += ' + '
            elif i == len(random_list) - 2 and random_list[i] != 0:
                polynominal += f'{random_list[i]}x'
                if random_list[i + 1] != 0:
                    polynominal += ' + '
            elif i == len(random_list) - 1 and random_list[i] != 0:
                polynominal += f'{random_list[i]} = 0'
            elif i == len(random_list) - 1 and random_list[i] == 0:
                polynominal += ' = 0'
    return polynominal


koef_k = create_list(k)
write_file(create_polynominal(koef_k))
