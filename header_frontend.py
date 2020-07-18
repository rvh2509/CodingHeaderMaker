from writing import CodeWriter
import tkinter

#cw = CodeWriter()

window = tkinter.Tk()
window.wm_title("Coding Header Maker")

def clear_screen(win):
    widgets = win.grid_slaves()
    for element in widgets:
        element.destroy()

def ask_name():
    clear_screen(window)
    name_label = tkinter.Label(window, text="What's your name?")
    name_label.grid(row=0, column=0)

    name_text = tkinter.StringVar()
    name_entry = tkinter.Entry(window, textvariable=name_text)
    name_entry.grid(row=1, column=0)

    sub = tkinter.Button(window, text="Submit", command=ask_date)
    sub.grid(row=2, column=0)

def ask_date():
    clear_screen(window)
#def ask_lang():

#def ask_class():

#def ask_extra():

window.mainloop()