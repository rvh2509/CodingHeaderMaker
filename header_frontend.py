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
db_text = tkinter.StringVar()
db_front = tkinter.StringVar()
db_back = tkinter.StringVar()
db_extension = tkinter.StringVar()

lang = ""
front = ""
back = ""
extension = ""
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

def set_extension(str_var):
    global extension
    extension = str_var.get()

def set_file(str_var):
    global file_name
    file_name = str_var.get()

def set_name(str_var):
    global name
    name = str_var.get()

def set_class(str_var):
    global your_class
    your_class = str_var.get()

def main_menu():
    clear_screen(window)

    mm_label = tkinter.Label(window, text="Welcome to the Coding Header Maker!")
    mm_label.grid(row=0, column=0)
    
    new_file = tkinter.Button(window, text="New File", command=ask_lang)
    new_file.grid(row=1, column=0)

    db_mode_button = tkinter.Button(window, text="Update Database", command=database_mode)
    db_mode_button.grid(row=2, column=0)

    db_view_button = tkinter.Button(window, text="View Database", command=view_database)
    db_view_button.grid(row=3, column=0)

def ask_lang():
    clear_screen(window)
    lang_text.set("")

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
    lang_front.set("")

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
    lang_back.set("")

    back_label = tkinter.Label(window, text="How do you end a single-line comment in %s?" % lang)
    back_label.grid(row=0, column=0)

    back_entry = tkinter.Entry(window, textvariable=lang_back)
    back_entry.grid(row=1, column=0)

    sub = tkinter.Button(window, text="Submit", command=lambda: [set_back(lang_back), unknown_extension()])
    sub.grid(row=2, column=0)

def unknown_extension():
    clear_screen(window)
    lang_extension.set("")

    extension_label = tkinter.Label(window, text="Finally, what is the file extension for %s? (include the '.', like '.py')" % lang)
    extension_label.grid(row=0, column=0)

    extension_entry = tkinter.Entry(window, textvariable=lang_extension)
    extension_entry.grid(row=1, column=0)

    sub = tkinter.Button(window, text="Submit", command=lambda: test_extension(lang_extension.get()))
    sub.grid(row=2, column=0)

def test_extension(ext):
    if ext[0] == ".":
        set_extension(ext)
        db.insert(lang, front, back, extension)
        ask_file()
    else:
        invalid_extension()

def invalid_extension():
    clear_screen(window)
    lang_extension.set("")

    inv_extension_label = tkinter.Label(window, text="Please give a valid extension (such as .py, .java, etc).")
    inv_extension_label.grid(row=0, column=0)

    inv_extension_entry = tkinter.Entry(window, textvariable=lang_extension)
    inv_extension_entry.grid(row=1, column=0)

    sub = tkinter.Button(window, text="Submit", command=lambda: test_extension(lang_extension.get()))
    sub.grid(row=2, column=0)

def ask_file():
    clear_screen(window)
    file_text.set("")

    file_label = tkinter.Label(window, text="What's the name of your file (don't include the extension)?")
    file_label.grid(row=0, column=0)

    file_entry = tkinter.Entry(window, textvariable=file_text)
    file_entry.grid(row=1, column=0)

    sub = tkinter.Button(window, text="Submit", command=lambda: [set_file(file_text), ask_name()])
    sub.grid(row=2, column=0)

def ask_name():
    clear_screen(window)
    name_text.set("")

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
    class_text.set("")

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
    extra_text.set("")

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

# use this to update the database without needing to make a file
def database_mode():
    clear_screen(window)
    db_text.set("")
    db_front.set("")
    db_back.set("")
    db_extension.set("")

    db_label = tkinter.Label(window, text="Please enter all of the relevant information about your language.")
    db_label.grid(row=0, column=0)
    
    db_name_label = tkinter.Label(window, text="Language Name:")
    db_name_label.grid(row=1, column=0)

    db_name_entry = tkinter.Entry(window, textvariable=db_text)
    db_name_entry.grid(row=2, column=0)
    set_lang(db_text)

    db_front_label = tkinter.Label(window, text="Start of a single-line comment:")
    db_front_label.grid(row=3, column=0)

    db_front_entry = tkinter.Entry(window, textvariable=db_front)
    db_front_entry.grid(row=4, column=0)
    set_front(db_front)

    db_end_label = tkinter.Label(window, text="End of a single-line comment:")
    db_end_label.grid(row=5, column=0)

    db_end_entry = tkinter.Entry(window, textvariable=db_back)
    db_end_entry.grid(row=6, column=0)
    set_back(db_back)

    db_extension_label = tkinter.Label(window, text="Language extension:")
    db_extension_label.grid(row=7, column=0)

    db_extension_entry = tkinter.Entry(window, textvariable=db_extension)
    db_extension_entry.grid(row=8, column=0)
    set_extension(db_extension)

    sub = tkinter.Button(window, text="Submit", command=database_mode_check)
    sub.grid(row=9, column=0)

    mm_button = tkinter.Button(window, text="Main Menu", command=main_menu)
    mm_button.grid(row=10, column=0)

def database_mode_check():
    try:
        db.search_by_name(lang)
    except IndexError:
        db.insert(lang, front, back, extension)
        database_mode_new_lang()
    else:
        database_mode_known_lang()

def database_mode_known_lang():
    clear_screen(window)
    db_known_label = tkinter.Label(window, text="Your language is already in the database.")
    db_known_label.grid(row=0, column=0)

    mm_button = tkinter.Button(window, text="Main Menu", command=main_menu)
    mm_button.grid(row=1, column=0)

def database_mode_new_lang():
    clear_screen(window)
    db_known_label = tkinter.Label(window, text="Your language has been added to the database!")
    db_known_label.grid(row=0, column=0)

    main_menu = tkinter.Button(window, text="Main Menu", command=ask_lang)
    main_menu.grid(row=1, column=0)

def view_database():
    clear_screen(window)
    db.delete_by_name("")
    db_list = tkinter.Listbox(window, height=6, width=35)
    db_list.grid(row=0, column=0, rowspan=6, columnspan=2)

    db_scrollbar = tkinter.Scrollbar(window)
    db_scrollbar.grid(row=0, column=2, rowspan=6)

    db_list.configure(yscrollcommand=db_scrollbar.set)
    db_scrollbar.configure(command=db_list.yview)

    db_list.delete(0, tkinter.END)
    for row in db.view_all() :
        str = row[0] + " " + row[1] + " " 
        if row[2] != "":
            str = str + row[2] + " "
        str = str + row[3]

        db_list.insert(tkinter.END, str)

    mm_button = tkinter.Button(window, text="Main Menu", command=main_menu)
    mm_button.grid(row=7, column=0)

main_menu()
window.mainloop()