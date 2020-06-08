from tkinter import *
from tkinter import messagebox
from tkinter.font import Font
from PIL import ImageTk,Image
from tkinter import filedialog

main = Tk()

main.title("Poster")
main.geometry("640x480")
C = Canvas(main, bg="white", height=480, width=640)
fnt = Font(family="Helvetica",size=12,weight="bold")
file = ""

twitter = IntVar()
instagram = IntVar()
hive = IntVar()

def file():
    file = filedialog.askopenfilename(filetypes = ( ("Attachments", "*.png"), ("All files", "*.*")))

def cntUpdate():
    print("W")

def post():
    print("W")

cnt = StringVar()
cnt.set("0 Chars")

txt = StringVar()


B1 = Checkbutton(main, text = "Twitter", variable = twitter, onvalue = True, offvalue = False)
B2 = Checkbutton(main, text = "Instagram", variable = instagram, onvalue = True, offvalue = False)
B3 = Checkbutton(main, text = "Hive", variable = hive, onvalue = True, offvalue = False)


B1.place(x = 10, y = 20)
B2.place(x = 90, y = 20)
B3.place(x = 185, y = 20)

text = Entry(main, textvariable = txt)
text.place(x = 10, y = 100, width = 200, height = 100)

char = Label(main, textvariable = cnt)
char.place(x= 10, y = 230)

p = Button(main, text = "Attachments", command = file, compound = CENTER, font = fnt, fg = 'Black')
p.place(x = 10, y = 250)

p = Button(main, text = "Post", command = post, compound = CENTER, font = fnt, fg = 'Black')
p.place(x = 10, y = 290)

main.mainloop()
