# алгоритм поддерживает гибридный режим, то есть можно шифровать и лат, и кир буквы в одном предложении
# знаки пунктуации и цифры не изменяются

litters = ' ,./?!#@"№$;:%^*()-_=+[]{}<>\|~`абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

# функция для шифрования
def cipher(s, d):
    st = [litters[(litters.index(lit) + d) % len(litters)] for lit in s]
    print('Сдвиг:', d, '\n', ''.join(s), ' => ', ''.join(st))
    return st

lit = list('Hello, World! Привет, Мир!')  # фраза
n = 25  # сдвиг
cipher(cipher(lit, n), -n)
