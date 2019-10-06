#Tkinter - Tkinter Textbox Example
#Written by: Jeff Brusoe
#Last Updated: October 5, 2019

import tkinter

#Configure main form
MainForm = tkinter.Tk()
MainForm.geometry("300x300")
MainForm.title("Tkinter Textbox Example")

txtName = tkinter.Entry(MainForm,width=25)
lblName = tkinter.Label(MainForm,text="", font=("Comic Sans",40))

txtName.pack()
lblName.pack()

MainForm.mainloop()
