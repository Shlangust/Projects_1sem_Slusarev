# для задачи из блока 1 создать две функции, save_def и load_def, которые позволяют
# сохранить информацию из экземпляров класса (3 шт.) в файл и загружать ее обратно.
# Использовать модуль pickle для сериализации и десериализации объектов Python в
# бинарном формате

import pickle
from PZ_16_1 import Circle


def save_circle(circle, filename):
    with open(f'{filename}.bin', 'wb') as file:
        pickle.dump(circle, file)

def load_circle(filename):
    with open(f'{filename}.bin', 'rb') as file:
        return pickle.load(file)
c = Circle(5)
save_circle(c,'1')
c1 = Circle(10)
save_circle(c1,'2')
