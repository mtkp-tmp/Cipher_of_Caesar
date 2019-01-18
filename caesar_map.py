''.join((lambda sh, text : [''.join((lambda sh, text : [''.join((lambda sh, text :
['abcdefghijklmnopqrstuvwxyz'[(i + sh % 26)] for i in map('abcdefghijklmnopqrstuvwxyz'.index, text)])(sh, l)) if ord(l) in range(97,123) else
''.join((lambda sh, text : ['ABCDEFGHIJKLMNOPQRSTUVWXYZ'[(i + sh) % 26] for i in map('ABCDEFGHIJKLMNOPQRSTUVWXYZ'.index, text)])(sh, l)) if l.isalpha() else l for l in text])(sh, l))
if ord(l) in range(65,123) else
''.join((lambda sh, text : [''.join((lambda sh, text : 
['абвгдеёжзийклмнопрстуфхцчшщъыьэюя'[(i + sh) % 33] for i in map('абвгдеёжзийклмнопрстуфхцчшщъыьэюя'.index, text)])(sh, l)) if ord(l) in range(1072,1106) else
''.join((lambda sh, text : ['АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'[(i + sh) % 33] for i in map('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'.index, text)])(sh, l)) if l.isalpha() else l for l in text])(sh,l))
for l in text])(int(input('Введите сдвиг для шифрования шифром Цезаря : ')), input('Введите строку для шифрования шифром Цезаря : ')))
