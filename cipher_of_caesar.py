n = int(input('Введите сдвиг '))
print(*(chr(z + n) if 64 < z < 91 - n or 96 < z < 123 - n or
                      1039 < z < 1072 - n or 1071 < z < 1104 - n else
        chr(z - (26-n)) if 90 - n < z < 91 or 122 - n < z < 123 else
        chr(z - (32-n)) if 1071 - n < z < 1072 or 1103 - n < z < 1104 else

        chr(z) for z in map(ord, input('введите текст для шифрования '))), sep="")
