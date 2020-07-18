from writing import CodeWriter
import tkinter

#cw = CodeWriter()

window = tkinter.Tk()
window.wm_title("Coding Header Maker")

main_frame = tkinter.Frame(window)

def clear_screen(frame):
    widgets = frame.grid_slaves()
    for widget in widgets:
        widget.destroy()

def ask_name():

def ask_date():

def ask_lang():

def ask_class():

def ask_extra():
window.mainloop()