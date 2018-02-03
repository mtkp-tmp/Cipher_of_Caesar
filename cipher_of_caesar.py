# you're code here
import random

n = random.randint(1, 25)


def cipher_lat(s, d):  # s только латиница
    return [chr(ord(i) + d - 26) if ((ord(i) + d > 90) & (ord(i) + d < 117) & (ord(i) < 91)) | (ord(i) + d > 122) else chr(ord(i) + d) for i in s]


def cipher_kir(s, d):  # s только кириллица без букв ё, Ё
    return [chr(ord(i) + d - 32) if ((ord(i) + d > 1071) & (ord(i) + d < 1104) & (ord(i) < 1072)) | (ord(i) + d > 1103) else chr(ord(i) + d) for i in s]


ss1 = cipher_lat('Hello, World!', n)
print('Сдвиг:', n, ss1)
ss2 = cipher_kir('Привет, Мир!', n)
print('Сдвиг:', n, ss2)
