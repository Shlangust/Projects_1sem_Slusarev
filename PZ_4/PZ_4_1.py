try:
    a = int(input('введите 2 числа. Первое должно быть меньше второго :\n')) #ввод данных
    b = int(input())
    if b>a: # проверка что а<b
     print('числа между 2 и 1 числом : ') # вывод перед циклом для того-чтобы не повторялся
     for i in range(b-a-1): #цикл
         print(b-i-1) # вывод от большего к меньшему
    else:
        print('b<a') # выод если условие в if не выполняется
except:  # вывод при ошибке
    print('вы ввели строку')