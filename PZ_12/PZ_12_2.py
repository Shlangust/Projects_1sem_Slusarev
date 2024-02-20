# составить генератор (yield), который выводит из строки только буквы
from string import ascii_letters
s = ''
def let(b):
    yield from [i for i in b if i in ascii_letters]
b = let(input())

s += ''.join(b)

print('буквы в строке : ',s)
