from tkinter import *
root = Tk()

text1=Text(root,							        #слово, которое нужно шифровать
		   height=2,
		   width=15,
		   font='Arial 14',
		   wrap=WORD)
text1.pack()

text2=Text(root,							        #ключ, необходимый для шифрования
		   height=2,
		   width=15,
		   font='Arial 14',
		   wrap=WORD)
text2.pack()

text3=Text(root,							        #вывод зашифрованного слова
		   height=2,
		   width=15,
		   font='Arial 14',
		   wrap=WORD)
text3.pack()

def box_input(new = str):							#функция для шифрования
	new = ''
	sample=text1.get("1.0",'end-1c')
	key=(text2.get("1.0", 'end-1c'))
	for i in sample:
		new += chr(ord(i) + int(key))
	text3.insert(1.0, new)

button1 = Button(root,						    #кнопка
             	 text="зашифровать",
             	 width=30,height=5,
             	 bg="white",fg="black")
button1.bind("<Button-1>", box_input)
button1.pack()


root.mainloop()
