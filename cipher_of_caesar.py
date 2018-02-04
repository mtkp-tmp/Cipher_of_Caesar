# алгоритм поддерживает гибридный режим, то есть можно шифровать и лат, и кир буквы в одном предложении
# знаки пунктуации и цифры не изменяются

rulit = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
enlit = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
rulitL = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
rulitU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
enlitL = 'abcdefghijklmnopqrstuvwxyz'
enlitU = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


# s только латиница
def cipher_lat(s, d):
    return [(el, enlitL[(enlitL.index(i) + d) % len(enlitL)]) if i in enlitL else (el, enlitU[(enlitU.index(i) + d) % len(enlitU)]) for el, i in s if i in enlit]


# s только кириллица без букв ё, Ё
def cipher_kir(s, d):
    return [(el, rulitL[(rulitL.index(i) + d) % len(rulitL)]) if i in rulitL else (el, rulitU[(rulitU.index(i) + d) % len(rulitU)]) for el, i in s if i in rulit]


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
n = 5
cipher(cipher(lit, n), -n)
