# you're code here
# Латиница
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

    return st

str = "Hello World"
print(Cezar(str,key))
