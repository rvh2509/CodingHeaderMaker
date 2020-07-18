from writing import CodeWriter
import tkinter
from datetime import date

#cw = CodeWriter()

window = tkinter.Tk()
window.wm_title("Coding Header Maker")

name_text = tkinter.StringVar()
date_text = tkinter.StringVar()
lang_text = tkinter.StringVar()
class_text = tkinter.StringVar()
extra_text = tkinter.StringVar()

def clear_screen(win):
    widgets = win.grid_slaves()
    for element in widgets:
        element.destroy()

def ask_name():
    clear_screen(window)
    name_label = tkinter.Label(window, text="What's your name?")
    name_label.grid(row=0, column=0)

    name_entry = tkinter.Entry(window, textvariable=name_text)
    name_entry.grid(row=1, column=0)

    sub = tkinter.Button(window, text="Submit", command=ask_date)
    sub.grid(row=2, column=0)

def ask_date():
    clear_screen(window)
    date_label = tkinter.Label(window, text="Would you like today's date in your comment?")
    date_label.grid(row=0, column=0)

    yes = tkinter.Button(window, text="Yes", command=date_yes)
    yes.grid(row=1, column=0)

    no = tkinter.Button(window, text="No", command=ask_lang)
    no.grid(row=1, column=1)

def date_yes(yn):
    today = date.today()
    creation_date = "%d/%d/%d" % (today.month, today.day, today.year)
    date_text.set(creation_date)
    ask_lang()

#def ask_lang():

#def ask_class():

#def ask_extra():

window.mainloop()