# Книжные магазины предлагают следующие коллекции книг.
# Магистр - Лермонтов, Достоевский, Пушкин, Тютчев
# ДомКниг - Толстой, Грибоедов, Чехов, Пушкин
# БукМаркет - Пушкин, Достоевский, Маяковский
# Галлерея - Чехов, Тютчев, Пушкин,
# Определить : Список всех книг, Список книг во всех магазинах,
# Одну кнгу которая есть не во всех магазинах

mag = {'Лермонтов', 'Достоевский', 'Пушкин', 'Тютчев'}
Dom_k = {'Толстой', 'Грибоедов', 'Чехов', 'Пушкин'}
Bm = {'Пушкин', 'Достоевский', 'Маяковский'}
gall = {'Чехов', 'Тютчев', 'Пушкин'}
print('ассортимент всех книг :',*mag|Dom_k|Bm|gall)
print('книги во всех магазинах : ',*mag&Dom_k&Bm&gall)
print('одна книга которая не во всех множествах',list(mag.symmetric_difference(Dom_k).symmetric_difference(Bm).symmetric_difference(gall))[0])