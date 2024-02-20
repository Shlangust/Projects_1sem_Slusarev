# в матрице  элементы 1 столбца возвести в куб
import numpy as np
matr = np.random.randint(-3, 3, size=(np.random.randint(2, 4), np.random.randint(2, 4)))
print(matr)
matr = matr.transpose()
matr[0] = matr[0] ** 3
matr = matr.transpose()
print('измененная матрица : \n',matr)
