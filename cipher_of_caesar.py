# шифрует любое предложение

litters = ' ,./?!#@"№$;:&%^*()-_=+[]{}<>\|~`абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

# функция для шифрования
def cipher(s, d):
    st = [litters[(litters.index(lit) + d) % len(litters)] for lit in s]
    print('Сдвиг:', d, '\n', ''.join(s), ' => ', ''.join(st))
    return st

lit = list('Hello, W@rld! Привет,_Мир!')  # фраза
n = 25  # сдвиг
cipher(cipher(lit, n), -n)
