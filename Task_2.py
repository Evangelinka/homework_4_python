# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

number = int(input('Введите число: '))
start = 2
simple_multiplier_spisok = []
if number == 1:
    simple_multiplier_spisok.append(number)
while number >= start:
    if number % start == 0:
        number /= start
        simple_multiplier_spisok.append(start)
    else:
        start += 1
print(simple_multiplier_spisok)
