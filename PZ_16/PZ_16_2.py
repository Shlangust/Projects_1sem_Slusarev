# Создать класс "Человек", который содержит информацию о имени, возрасте, поле.
# Создать классы "Мужчина" и "Женьщина", которые наследуются от класса
# "Человек". Каждый класс должен иметь метод, который выводит информацию
# о поле объекта
class bald_monkey:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def display_gender(self):
        print("Gender: ",self.gender)

class man(bald_monkey):
    pass

class woman(bald_monkey):
    pass


person1 = bald_monkey("Олег", 30, "man")
person1.display_gender()

man1 = man("Илья", 25, "man")
man1.display_gender()

woman1 = woman("Анджелика", 28, "woman")
woman1.display_gender()