#Sample Tkinter GUI

import tkinter

def clickOK():
    print("Ok button has been clicked.")

window = tkinter.Tk()
label = tkinter.Label(window, text = "Tkinter Test")

button = tkinter.Button(window, text = "Click Me!", command = clickOK)

label.pack()
button.pack()

window.mainloop()
