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