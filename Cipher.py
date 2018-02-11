key = int(input("Enter key: "))
str = input("Enter text: ")

for i, x in enumerate(str): str = str[:i] + chr(ord(x) + key)

print(str)
