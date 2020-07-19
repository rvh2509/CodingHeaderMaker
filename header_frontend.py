from database_manager import LangDB
import tkinter
from datetime import date

db = LangDB()
window = tkinter.Tk()
window.wm_title("Coding Header Maker")

lang_text = tkinter.StringVar()
lang_front = tkinter.StringVar()
lang_back = tkinter.StringVar()
lang_extension = tkinter.StringVar()
file_text = tkinter.StringVar()
name_text = tkinter.StringVar()
class_text = tkinter.StringVar()
extra_text = tkinter.StringVar()

lang = ""
front = ""
back = ""
file_name = ""
name = ""
creation_date = ""
your_class = ""

def clear_screen(win):
    widgets = win.grid_slaves()
    for element in widgets:
        element.destroy()

def set_lang(str_var):
    global lang
    lang = str_var.get()

def set_front(str_var):
    global front
    front = str_var.get()

def set_back(str_var):
    global back
    back = str_var.get()

def set_file(str_var):
    global file_name
    file_name = str_var.get()

def set_name(str_var):
    global name
    name = str_var.get()

def set_class(str_var):
    global your_class
    your_class = str_var.get()

def ask_lang():
    clear_screen(window)
    lang_label = tkinter.Label(window, text="What language are you working in today?")
    lang_label.grid(row=0, column=0)

    lang_entry = tkinter.Entry(window, textvariable=lang_text)
    lang_entry.grid(row=1, column=0)

    sub = tkinter.Button(window, text="Submit", command=lambda: [set_lang(lang_text), lang_work()])
    sub.grid(row=2, column=0)

def lang_work():
    try:
        db.search_by_name(lang)
    except IndexError:
        unknown_front()
    else:
        ask_file()

def unknown_front():
    clear_screen(window)
    text = "I don't think I've heard of %s. Can you help me learn?" % lang
    front_label1 = tkinter.Label(window, text=text)
    front_label1.grid(row=0, column=0)
    
    front_label2 = tkinter.Label(window, text="How do you begin a single-line comment in %s?" % lang)
    front_label2.grid(row=1, column=0)

    front_entry = tkinter.Entry(window, textvariable=lang_front)
    front_entry.grid(row=2, column=0)

    sub = tkinter.Button(window, text="Submit", command=lambda: [set_front(lang_front), unknown_back()])
    sub.grid(row=3, column=0)

def unknown_back():
    clear_screen(window)
    back_label = tkinter.Label(window, text="Does %s need something to end a single-line comment?" % lang)
    back_label.grid(row=0, column=0)

    yes = tkinter.Button(window, text="Yes", command=lambda: unknown_back_yes())
    yes.grid(row=1, column=0)

    no = tkinter.Button(window, text="No", command=lambda: unknown_extension())
    no.grid(row=1, column=1)

def unknown_back_yes():
    clear_screen(window)
    back_label = tkinter.Label(window, text="How do you end a single-line comment in %s?" % lang)
    back_label.grid(row=0, column=0)

    back_entry = tkinter.Entry(window, textvariable=lang_back)
    back_entry.grid(row=1, column=0)

    sub = tkinter.Button(window, text="Submit", command=lambda: [set_back(lang_back), unknown_extension()])
    sub.grid(row=2, column=0)

def unknown_extension():
    clear_screen(window)
    extension_label = tkinter.Label(window, text="Finally, what is the file extension for %s? (include the '.', like '.py')" % lang)
    extension_label.grid(row=0, column=0)

    extension_entry = tkinter.Entry(window, textvariable=lang_extension)
    extension_entry.grid(row=1, column=0)

    sub = tkinter.Button(window, text="Submit", command=lambda: [db.insert(lang, front, back, lang_extension.get()), ask_file()])
    sub.grid(row=2, column=0)

def ask_file():
    clear_screen(window)
    file_label = tkinter.Label(window, text="What's the name of your file (don't include the extension)?")
    file_label.grid(row=0, column=0)

    file_entry = tkinter.Entry(window, textvariable=file_text)
    file_entry.grid(row=1, column=0)

    sub = tkinter.Button(window, text="Submit", command=lambda: [set_file(file_text), ask_name()])
    sub.grid(row=2, column=0)

def ask_name():
    clear_screen(window)
    name_label = tkinter.Label(window, text="What's your name?")
    name_label.grid(row=0, column=0)

    name_entry = tkinter.Entry(window, textvariable=name_text)
    name_entry.grid(row=1, column=0)

    sub = tkinter.Button(window, text="Submit", command=lambda: [set_name(name_text), ask_date()])
    sub.grid(row=2, column=0)

def ask_date():
    clear_screen(window)
    date_label = tkinter.Label(window, text="Would you like today's date in your comment?")
    date_label.grid(row=0, column=0)

    yes = tkinter.Button(window, text="Yes", command=date_yes)
    yes.grid(row=1, column=0)

    no = tkinter.Button(window, text="No", command=ask_class)
    no.grid(row=1, column=1)

def date_yes():
    global creation_date
    today = date.today()
    creation_date = "%d/%d/%d" % (today.month, today.day, today.year)
    ask_class()

def ask_class():
    clear_screen(window)
    class_label = tkinter.Label(window, text="What class is this for?")
    class_label.grid(row=0, column=0)

    class_entry = tkinter.Entry(window, textvariable=class_text)
    class_entry.grid(row=1, column=0)

    sub = tkinter.Button(window, text="Submit", command=lambda: [set_class(class_text), ask_extra([])])
    sub.grid(row=2, column=0)

    na = tkinter.Button(window, text="Not Applicable", command=lambda: ask_extra([]))
    na.grid(row=2, column=1)

def ask_extra(lines):
    clear_screen(window)
    aextra_label = tkinter.Label(window, text="Would you like to add another line to your comment?")
    aextra_label.grid(row=0, column=0)

    yes = tkinter.Button(window, text="Yes", command=lambda: get_extra(lines))
    yes.grid(row=1, column=0)

    no = tkinter.Button(window, text="No", command=lambda: another_file(lines))
    no.grid(row=1, column=1)

def get_extra(lines):
    clear_screen(window)
    gextra_label = tkinter.Label(window, text="What line would you like to add?")
    gextra_label.grid(row=0, column=0)

    gextra_entry = tkinter.Entry(window, textvariable=extra_text)
    gextra_entry.grid(row=1, column=0)

    sub = tkinter.Button(window, text="Submit", command=lambda: [lines.append(extra_text.get()), extra_text.set(""), ask_extra(lines)])
    sub.grid(row=2, column=0)

def another_file(extras):
    db.write_to_file(lang, file_name, name, creation_date, your_class, extras)

    clear_screen(window)
    gextra_label = tkinter.Label(window, text="Would you like to make another file?")
    gextra_label.grid(row=0, column=0)

    yes = tkinter.Button(window, text="Yes", command=ask_lang)
    yes.grid(row=1, column=0)

    no = tkinter.Button(window, text="No", command=lambda: window.destroy())
    no.grid(row=1, column=1)

ask_lang()
window.mainloop()