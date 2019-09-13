#Tkinter label demo

import tkinter

MainForm = tkinter.Tk()

#Configure main form
MainForm.title("Hello World in Tkinter")

lblHello = tkinter.Label(MainForm,text="Hello World!", font=("Comic Sans",50))
lblHello.grid(column=0,row=0)

MainForm.mainloop()
