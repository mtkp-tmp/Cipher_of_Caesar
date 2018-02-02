import random

n = random.randint(1, 26)


def cipher(s, d):  # s только латиница
    return [chr(ord(i) + d - 26) if (ord(i)+d > 122) & (ord(i)+d > 90) else chr(ord(i)+d) for i in s]


ss1 = cipher('Hello, World!', n)
print('Сдвиг:', n, ss1)

