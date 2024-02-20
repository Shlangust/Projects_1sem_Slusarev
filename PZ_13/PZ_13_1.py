# В матрице найти средне-арефметическое  всех положительных элементов
import numpy as np
matr = np.random.randint(-3, 4, size=(np.random.randint(2, 4), np.random.randint(2, 4)))
l = []
[[l.append(j) for j in i if j > 0] for i in matr]
print(matr)
print('средне-арефметическое  всех положительных элементов : ',sum(l)/len(l))