# Дан список ненулевых целых чисел размера N. Проверить, чередуются ли в нем
# положительные и отрицательные числа. Если чередуются, то вывести 0, если нет
# то вывести порядковый номер 1 элемента, нарущающего закономерность


import random

# инициализация переменных
tf = False
l = []
b = 0
i = 0
r = int(input('введите размер масива : '))


try:
    # создание масива
    while i < r:
        a = random.randint(-3,3)
        i+=1
        if a == 0:
             i = i-1
             continue
        l.append(a)


    print(l)
    s=0

    #Проверка
    for i in l:
        if i*b > 0:
            tf = True
            print(s,'порядковый номер последнего элемента')
            break
        s += 1

        b = i
    if tf == False:
        print(0)
except:
    print('error')
