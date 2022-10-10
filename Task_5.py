# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

with open('Task_5_1.txt', 'r') as data:
    pol_1 = data.read()

with open('Task_5_2.txt', 'r') as data:
    pol_2 = data.read()


def makeDict(pol):
    pol = pol.replace('= 0', '')
    pol = pol.replace('*x^', '|')
    pol = pol.split('+')
    for i in range(len(pol)):
        if str(pol[i]).isdigit():
            pol[i] = [pol[i], 0]
        elif pol[i].find('*x') > 0:
            pol[i] = [pol[i].replace('*x', ''), 1]
        else:
            pol[i] = pol[i].split('|')
    for i in pol:
        pol[i] = [int(pol[i][1]), int(pol[i][0])]
    return dict(pol)

def sumDict(d1, d2):
    for key, value in d1.items():
        d1[key] = value + d2.get(key, 0)
    return d1


pol_1 = makeDict(pol_1)
pol_2 = makeDict(pol_2)
if len(pol_1) > len(pol_2):
    res = sumDict(pol_1, pol_2)
else:
    res = sumDict(pol_2, pol_1)


with open('Task_5_Sum.txt', 'w') as data:
    for key, value in res.items():
        if key > 1:
            data.write(f'{value}*x^{key} + ')
        elif key == 1:
            data.write(f'{value}*x + ')
        else:
            data.write(f'{value} = 0')