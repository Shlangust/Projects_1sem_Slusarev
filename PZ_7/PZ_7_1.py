# даны положительные числа N1 и N2 и строки S1 и S2
# получить из этих строк, строку содержащую первые N1 символов
# первой строки и последние N2 символов 2

N1 = 4
N2 = 4
S1 = 'Do glatem live'
S2 = 'Now your soul return to paradise (fall down)'
try:
    S = S1[0:N1] + S2[-N2:]
    print(S)
except:
    print('Error')