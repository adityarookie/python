from tkinter import *

window = Tk()
window.title("tkinter browser")
window.geometry("500x500")

greeting = Label(text="Hello user",fg="black",bg="white")
button = Button(text="Click me!",bg ="green",fg="yellow")
text = Text(bg ="yellow",fg="red")

greeting.pack()
button.pack()
text.pack()

frame= Frame(master=window,relief=SUNKEN,borderwidth=10)
frame.pack()
label2= Label(master=frame,text="sample text")
label2.pack()



window.mainloop()