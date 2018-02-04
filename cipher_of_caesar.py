#Использует алфавит без ё и Ё
def change (s,k):
    snew=''
    for i in range (len(s)):
        a=ord(s[i])
        print(a)
        if a>=1072 and a<=1103:
            if a+k>1103:
                a=1072+((a+k)-1104)
            else: a+=k
        elif a>=97 and a<=122:
            if a+k>122:
                a=97+((a+k)-123)
            else: a+=k
        elif a>=65 and a<=90:
            if a+k>90:
                a=65+((a+k)-91)
            else: a+=k
        elif a>=1040 and a<=1071:
            if a+k>1071:
                a=1040+((a+k)-1072)
            else: a+=k
        snew+=chr(a)
    return snew
k=int(input('Введите ключ = '))
str=input('Введите строку = ')
print(change(str,k))

#print('test for trevis')
