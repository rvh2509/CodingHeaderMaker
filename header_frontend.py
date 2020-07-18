from database_manager import LangDB
import tkinter
from datetime import date

db = LangDB()
window = tkinter.Tk()
window.wm_title("Coding Header Maker")

name_text = tkinter.StringVar()
date_text = tkinter.StringVar()
lang_text = tkinter.StringVar()
lang_front = tkinter.StringVar()
lang_back = tkinter.StringVar()
lang_extension = tkinter.StringVar()
class_text = tkinter.StringVar()
extra_text = tkinter.StringVar()

def clear_screen(win):
    widgets = win.grid_slaves()
    for element in widgets:
        element.destroy()

def ask_lang():
    clear_screen(window)
    lang_label = tkinter.Label(window, text="What language are you working in today?")
    lang_label.grid(row=0, column=0)

    lang_entry = tkinter.Entry(window, textvariable=lang_text)
    lang_entry.grid(row=1, column=0)

    sub = tkinter.Button(window, text="Submit", command=lang_work)
    sub.grid(row=2, column=0)

def lang_work():
    lang = lang_text.get()

    try:
        db.search_by_name(lang)
    except IndexError:
        unknown_front(lang)
    else:
        ask_name()

def unknown_front(lang):
    clear_screen(window)
    front_label1 = tkinter.Label(window, text="I don't think I've heard of %s. Can you help me learn?" % lang)
    front_label1.grid(row=0, column=0)

    front_label2 = tkinter.Label(window, text="How do you begin a single-line comment in %s?" % lang)
    front_label2.grid(row=1, column=0)

    front_entry = tkinter.Entry(window, textvariable=lang_front)
    front_entry.grid(row=2, column=0)

    sub = tkinter.Button(window, text="Submit", command=lambda: unknown_back(lang))
    sub.grid(row=3, column=0)

def unknown_back(lang):
    clear_screen(window)
    back_label = tkinter.Label(window, text="Does %s need something to end a single-line comment?" % lang)
    back_label.grid(row=0, column=0)

    yes = tkinter.Button(window, text="Yes", command=lambda: unknown_back_yes(lang))
    yes.grid(row=1, column=0)

    no = tkinter.Button(window, text="No", command=lambda: unknown_extension(lang))
    no.grid(row=1, column=1)

def unknown_back_yes(lang):
    clear_screen(window)
    back_label = tkinter.Label(window, text="How do you end a single-line comment in %s?" % lang)
    back_label.grid(row=0, column=0)

    back_entry = tkinter.Entry(window, textvariable=lang_back)
    back_entry.grid(row=1, column=0)

    sub = tkinter.Button(window, text="Submit", command=lambda: unknown_extension(lang))
    sub.grid(row=2, column=0)

def unknown_extension(lang):
    clear_screen(window)
    extension_label = tkinter.Label(window, text="Finally, what is the file extension for %s? (include the '.', like '.py')" % lang)
    extension_label.grid(row=0, column=0)

    extension_entry = tkinter.Entry(window, textvariable=lang_extension)
    extension_entry.grid(row=1, column=0)

    sub = tkinter.Button(window, text="Submit", command=lambda: [db.insert(lang_text.get(), lang_front.get(), lang_back.get(), lang_extension.get()), ask_name()])
    sub.grid(row=2, column=0)

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

    no = tkinter.Button(window, text="No")#, command=ask_class)
    no.grid(row=1, column=1)

def date_yes():
    today = date.today()
    creation_date = "%d/%d/%d" % (today.month, today.day, today.year)
    date_text.set(creation_date)
    #ask_class()

#def ask_class():

#def ask_extra():
ask_lang()
window.mainloop()