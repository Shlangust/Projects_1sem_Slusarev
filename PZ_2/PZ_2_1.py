# Условие: с начала суток прошло n секунд (n-целое).
# Найти кол-во секунд, прошедших с начала последней минуты
try:     # В конструкции try мы пытаемся создать переменную sec и обрабтать ее.
    sec = int(input('введите кол-во секунд : '))
    sec_after_minute = sec % 60 #  Операция нахождения остатка от делеиня.
    print('секунд с начала дня', sec,
          '\n',
          'секунд с начала минуты', sec_after_minute)
except:
    print('Вы ввели строку!')#  В случае если не получаетсяперевести input в int, выходим на это print