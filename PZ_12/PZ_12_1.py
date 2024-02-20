# В последовательности из N чисел(n-четное) во второй половине найти сумму элементов больших 10


import random
r = random.randint(1,4)
l = []
[l.append((random.randint(0,20)))for i in range(r*2)]
print(l)

nl =[]
[nl.append(i) for i in l[r:] if i >9]
print(f'сумму элементов больших 10 во второй половине : {sum(nl)}')