# Описать функцию InvertDigits(K) меняющие порядок следования цифр целого положительного
# числа K на обратный


def InvertDigits(K):
    K = str(K)
    K = K[::-1]
    return int(K)

try:
    print(InvertDigits(int(input())))
except:
    print('Error')


