def CoC (text, offset):
    s,offset="",offset%26
    if offset==0:
        return text
    for c in text:
        oc=ord(c)                       #Код символа без отступа
        oc_of=oc+offset                 #Код символа с отступом
        if 65<=oc<=90:
            if oc_of>90:
                s+=chr(65+oc_of-91)
            else:
                s+=chr(oc_of)
        elif 97<=oc<=122:
            if oc_of>122:
                s+=chr(97+oc_of-123)
            else:
                s+=chr(oc_of)
        else:
            s+=c
    return s

print(CoC(".ABCDEFGHIJKLMNOPQRSTUVWXYZ___abcdefghijklmnopqrstuvwxyz.",-25))
print(CoC(".ABCDEFGHIJKLMNOPQRSTUVWXYZ___abcdefghijklmnopqrstuvwxyz.",1))
