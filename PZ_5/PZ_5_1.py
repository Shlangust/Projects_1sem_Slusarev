#Создать программу а в ней функцию, строящию изображение, в котором в 1
# строке 1 звездочка во второй 2 и тд размером m

m = int(input('введите кол-во строк ')) # ввод m
def stair(m): # объявление функции
 for i in range(m):
    print('*'*(i+1))
try:
    stair(m) # вызов функции
except:
    print('Ошибка')

