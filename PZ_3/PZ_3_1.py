# Даны числа x,y. Првести истинность высказывания: "Точка с координатами (x,y)
# лежит в четвертой координатной чертверти".

try:
    x = int(input('введите координаты x  : '))  #ввод данных
    y = int(input('введите координаты y  : '))
    if x > 0 and y < 0:   # проверка  в какой четверти находится координата
        print(True)     # вывод в случае если соответствует
    else:
        print(False)    # вывод в случае если несоответствует
except:
    print('Ошибка!') # вывод при ошибке