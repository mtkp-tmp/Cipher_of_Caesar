# you're code here
key = int(input("Key: "))
if  (key < 1)or(key>54):
    print("Error!")
    exit()

def Cezar(str, k):
    st = ''
    for i in str:
        if (ord(i)>96)&(ord(i)<123):
            if ((ord(i)+k)>122):
                st += chr((ord(i)+k)-26)
            else:
                st += chr(ord(i)+k)

        if (ord(i)>64)&(ord(i)<91):
            if ((ord(i) + k) > 90):
                st += chr((ord(i) + k) - 26)
            else:
                st += chr(ord(i) + k)

        if (ord(i)>1039)&(ord(i)<1073):
            if ((ord(i)+k)>1072):
                st += chr((ord(i)+k)-26)
            else:
                st += chr(ord(i)+k)

        if (ord(i) > 1071) & (ord(i) < 1104):
            if ((ord(i) + k) > 1103):
                st += chr((ord(i) + k) - 26)
            else:
                st += chr(ord(i) + k)

    return st

str1 = "Привет мир!"
str = "Hello World!"
print(Cezar(str1,key))
print(Cezar(str,key))
