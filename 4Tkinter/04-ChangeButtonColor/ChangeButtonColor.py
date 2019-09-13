#Tkinter - Change Button Color

import tkinter

def clickOK():
    print("Ok button has been clicked.")

#Configure main form
MainForm = tkinter.Tk()
MainForm.geometry("300x50")
MainForm.title("Tkinter Change Button Color")

button = tkinter.Button(MainForm, text = "Click Me!", command = clickOK, fg="red",bg="yellow")
button.pack()

MainForm.mainloop()
