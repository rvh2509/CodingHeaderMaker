from writing import CodeWriter
import tkinter

#cw = CodeWriter()
window = tkinter.Tk()
window.wm_title("Coding Header Maker")

l1 = tkinter.Label(window, text="Name")
l1.grid(row=0, column=0)

l2 = tkinter.Label(window, text="Date")
l2.grid(row=0, column=2)

l3 = tkinter.Label(window, text="Class")
l3.grid(row=1, column=0)

l4 = tkinter.Label(window, text="File Name")
l4.grid(row=1, column=2)

name_text = tkinter.StringVar()
e1 = tkinter.Entry(window, textvariable=name_text)
e1.grid(row=0, column=1)

date_text = tkinter.StringVar()
e2 = tkinter.Entry(window, textvariable=date_text)
e2.grid(row=0, column=3)

class_text = tkinter.StringVar()
e3 = tkinter.Entry(window, textvariable=class_text)
e3.grid(row=1, column=1)

filename_text = tkinter.StringVar()
e4 = tkinter.Entry(window, textvariable=filename_text)
e4.grid(row=1, column=3)

window.mainloop()