#Python Tkinter Test
#Written by: Jeff Brusoe
#Last Updated: May 23, 2019
#
#https://wiki.python.org/moin/TkInter

import tkinter

top = tkinter.Tk()

def helloCallBack():
   tkinter.MessageBox.showinfo( "Hello Python", "Hello World")

B = tkinter.Button(top, text ="Hello", command = helloCallBack)

B.pack()
top.mainloop()
