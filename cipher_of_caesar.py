def Shifr_Chezar(text,tab1):
  return ''.join([chr(ord(elem)+tab1)for elem in text])

text = input("Input your text: ")
tab1 = int (input("Enter tab: "))
print("Tab text: ",Shifr_Chezar(text,tab1))
