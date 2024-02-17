# Средствами языка Python сформировать два текстовых файла (.txt), содержащих по одной
# последовательности из целых положительных и отрицательных чисел.
# Сформировать новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую обработку элементов:
# Элементы первого и второго файлов:
# Элементы первого файла, отсутствующие во втором:
# Элементы второго файла, отсутствующие в первом:
# Количество элементов:
# Индекс первого минимального элемента:
# Индекс последнего максимального элемента:


import random
f1 = open('F1.txt','w',encoding='Utf-8')
f2 = open('F2.txt','w',encoding='Utf-8')
l1 = []
l2 = []
for i in range(random.randint(1,6)):
    x = random.randint(-5, 6)
    l1.append(x)
    f1.write(str(x))
    f1.write(' ')
for i in range(random.randint(1,6)):
    x = random.randint(-5, 6)
    l2.append(x)
    f2.write(str(x))
    f2.write(' ')

f_main = open('F_main.txt','w',encoding='utf-8')
f_main.write('Элементы 1 и 2 файлов : ')
f_main.write(' '.join(map(str,l1)))
f_main.write(' ')
f_main.write(' '.join((map(str,l2))))
f_main.write('\n')

f_main.write('Элеметы 1 файла, отцувствующие в 2 : ')
for i in l1:
    if i not in l2:
        f_main.write(str(i))
        f_main.write(' ')
f_main.write('\n')


f_main.write('Элеметы 2 файла, отцувствующие в 1 : ')
for i in l2:
    if i not in l1:
        f_main.write(str(i))
        f_main.write(' ')
f_main.write('\n')


f_main.write('Кол-во элементов : ')
f_main.write(str(len(l1)+len(l2)))
f_main.write('\n')

f_main.write('Индекс 1 мин элемента : ')
f_main.write(str(l1.index((min(l1)))))
f_main.write('\n')

f_main.write('Индекс 2 мин элемента : ')
f_main.write(str(l2.index((min(l2)))))