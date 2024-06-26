# 3.	Дано множество A из N точек (N > 2, точки заданы своими координатами x, у).
# Найти такую точку из данного множества, сумма расстояний от которой до остальных его точек минимальна,
# и саму эту сумму.
# Расстояние R между точками с координатами (x1, y1) и (x2, у2) вычисляется по формуле:
# R = √(x2 – x1)2 + (у2 – y1)2.
# Для хранения данных о каждом наборе точек следует использовать по два списка:
# первый список для хранения абсцисс, второй — для хранения ординат.


import math

points = [(1, 2), (3, 4), (5, 6)]# точки


min_sum = float(100000000) # изначальное min sum
min_point = ()


try:
    # Нахождение точки с минимальной суммой расстояний
    for point in points:
        x, y = point
        total = 0
        for i in range(len(points)):
            total += math.sqrt((points[i][0] - x) ** 2 + (points[i][1] - y) ** 2)

        if total < min_sum:
            min_sum = total
            min_point = (x, y)

    #Вывод
    print("Точка с минимальной суммой расстояний :", min_point)
    print("Минимальная сумма расстояний :", min_sum)
except:
    print('Error')