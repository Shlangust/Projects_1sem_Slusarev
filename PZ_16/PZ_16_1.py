# Создать класс "круг", который имеет атрибут радиуса и методы
# для вычисления площади, длинны окружности и диаметра
class Circle:
    def __init__(self,r):
        self.r = r
    def area(self):
        return self.r**2*3.14
    def len(self):
        return self.r*2*3.14
    def diameter(self):
        return self.r*2
a = Circle(10)
print(a.diameter())
