while True:
    try: n, s, res = int(input("Введите сдвиг шифра")), input("Введите текст строчными буквами").strip(), ""
    except ValueError: print("Ошибка типа данных")
    else: break
for c in s:
    if c.islower():
        if c in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя': res += 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'[('абвгдеёжзийклмнопрстуфхцчшщъыьэюя'.index(c) + n) % len('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')]
        elif c in 'abcdefghijklmnopqrstuvwxyz': res += 'abcdefghijklmnopqrstuvwxyz'[('abcdefghijklmnopqrstuvwxyz'.index(c) + n) % len('abcdefghijklmnopqrstuvwxyz')]
    elif c.isupper():
        if c in 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ': res += 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'[('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'.index(c) + n) % len('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')]
        elif c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ': res += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[('ABCDEFGHIJKLMNOPQRSTUVWXYZ'.index(c) + n) % len('ABCDEFGHIJKLMNOPQRSTUVWXYZ')]
    else: res += c
print('Защифрованный текст: "' + res + '"')
