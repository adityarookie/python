from tkinter import*
from PIL import Image,ImageTk

x = Tk()
x.title("cute dog")
x.geometry("500x500")

upload = Image.open("dog.jpg")

image = ImageTk.PhotoImage(upload)

label = Label(x,image = image, height = 400, width = 320)
label.pack()

x.mainloop()
