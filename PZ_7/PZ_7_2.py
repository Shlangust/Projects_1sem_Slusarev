'''
даны строки S S0. Удалить из строки N1 все подстроки, совподающие с S0.
Если таких нет вывести строку без изменений
'''

S = 'Мое имя "Никто"'
S0 = 'о'
try:
 print(S.replace(S0,''))
except:
    print('Error')