litters = ' ,./?!#@"№$;:&%^''*()-_=+[]{}<>\|~`абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
d = int(input('Сдвиг: '))
print('Зашифровано в', ''.join([litters[(litters.index(lit) + d) % len(litters)] for lit in input('Шифруемый текст: ')]))

