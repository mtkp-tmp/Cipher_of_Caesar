# you're code here
# алгоритм поддерживает гибридный режим, то есть можно шифровать и лат, и кир буквы в одном предложении
# знаки пунктуации, цифры и буквы ё и Ё не изменяются

rulit = 'абвгдежзийклмнопрстуфхцчшщъыьэюяАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
enlit = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


# s только латиница
def cipher_lat(s, d):
    d %= 26
    return [(el, chr(ord(i) + d - 26)) if ((ord(i) + d > 90) & (ord(i) + d < 117) & (ord(i) < 91)) | (
            ord(i) + d > 122) else (el, chr(ord(i) + d)) for el, i in s if i in enlit]


# s только кириллица без букв ё, Ё
def cipher_kir(s, d):
    d %= 32
    return [(el, chr(ord(i) + d - 32)) if ((ord(i) + d > 1071) & (ord(i) + d < 1104) & (ord(i) < 1072)) | (
            ord(i) + d > 1103) else (el, chr(ord(i) + d)) for el, i in s if i in rulit]


# функция для шифрования
def cipher(s, d):
    # 1. разбиваем предложение на латицицу, кириллицу и небуквы
    notlit = list()
    lCipher = list()  # lat
    ruLits = list()  # kir
    for i in range(0, len(s)):
        if s[i] in enlit:
            lCipher.append((i, s[i]))
        elif s[i] in rulit:
            ruLits.append((i, s[i]))
        else:
            notlit.append((i, s[i]))

    # 2. шифруем латиницу и кириллицу отдельно
    lCipher = cipher_lat(lCipher, d)
    ruLits = cipher_kir(ruLits, d)

    # 3. нормализуем для вывода
    lCipher.extend(ruLits)
    lCipher.extend(notlit)
    lCipher.sort()
    st = ''
    for i, l in lCipher:
        st += l

    # 4. вывод
    print('Сдвиг:', d, '\n', ''.join(s), ' => ', st)
    return st

#####################################################
# lit = list(input('Введите фразу: '))
# n = int(input('Введите сдвиг: '))
lit = list('Hello, World! Привет, Мир!')
n = -5
cipher(cipher(lit, n), -n)

# тестовый коммит