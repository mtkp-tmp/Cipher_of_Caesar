# you're code here
print('test for trevis')

import random

n = random.randint(1, 25)


def cipher(s, d):  # s только латиница
    return [chr(ord(i) + d - 26) if ((ord(i) + d > 90) & (ord(i) + d < 117) &(ord(i) < 91)) ^ (ord(i) + d > 122) else chr(ord(i) + d) for i in s]


ss1 = cipher('Hello, World!', n)
print('Сдвиг:', n, ss1)
