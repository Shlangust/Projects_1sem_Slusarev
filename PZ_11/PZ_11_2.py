# Из предложенного текстового файла (text18-26.txt)
# вывести на экран его содержимое, количество знаков препинания.
# Сформировать новый файл, в который поместить текст в стихотворной
# форме предварительно заменив все знаки пунктуации на знак «/».

f = open('text18-26.txt','r',encoding='utf-8')
fn = open('new_file.txt','w',encoding='utf-8')
marks = '''!()-[]{};?@#$%:'"\,./^&amp;*_—'''
s = 0
for i in f:
    for j in i:
        if j in marks:
            fn.write('/')
            s+=1
        else:
            fn.write(j)
