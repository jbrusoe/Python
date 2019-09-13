#Tkinter - Change form size

import tkinter

MainForm = tkinter.Tk()

#Configure main form
MainForm.title("Tkinter Changing Form Size")
MainForm.geometry("500x500")

#Configure Label
lblSize = tkinter.Label(MainForm,text="Setting form size to 500X500", font=("Comic Sans",25))
lblSize.grid(column=0,row=0)

MainForm.mainloop()
