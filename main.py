from tkinter import *
from tkinter import messagebox
from tkinter.font import Font
from PIL import ImageTk,Image

main = Tk()

main.title("Poster")
main.geometry("640x480")
C = Canvas(main, bg="white", height=480, width=640)

twitter = IntVar()
instagram = IntVar()
hive = IntVar()

B1 = Checkbutton(main, text = "Twitter", variable = twitter, onvalue = True, offvalue = False)
B2 = Checkbutton(main, text = "Instagram", variable = instagram, onvalue = True, offvalue = False)
B3 = Checkbutton(main, text = "Hive", variable = hive, onvalue = True, offvalue = False)


B1.place(x = 10, y = 20)
B2.place(x = 90, y = 20)
B3.place(x = 185, y = 20)

text = Entry(main)
text.place(x = 10, y = 100, width = 200, height = 100)

char = Label(main, text=str(len(str(text.get()))) + " Chars")
char.place(x= 10, y = 230)

main.mainloop()
