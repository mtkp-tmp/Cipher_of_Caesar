n, s, res = int(input("Введите сдвиг шифра")), input("Введите текст").strip(), ""
for c in s:
    if c in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя': res += 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'[('абвгдеёжзийклмнопрстуфхцчшщъыьэюя'.index(c) + n) % len('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')]
    elif c in 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ': res += 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'[('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'.index(c) + n) % len('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')]
    elif c in 'abcdefghijklmnopqrstuvwxyz': res += 'abcdefghijklmnopqrstuvwxyz'[('abcdefghijklmnopqrstuvwxyz'.index(c) + n)% len('abcdefghijklmnopqrstuvwxyz')]
    elif c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ': res += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[('ABCDEFGHIJKLMNOPQRSTUVWXYZ'.index(c) + n)% len('ABCDEFGHIJKLMNOPQRSTUVWXYZ')]
print('Защифрованный текст: "' + res + '"')
