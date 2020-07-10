from database_manager import LangDB
from datetime import date

class CodeWriter:
    def __init__(self):
        self.db = LangDB()
        lang = input("What language are you working in today?\n")

        try:
            self.db.search_by_name(lang)
        except IndexError:
            self.unknown_lang(lang)

        self.ask_questions(lang)

    def ask_questions(self, lang):
        lang_data = self.db.search_by_name(lang)
        lang_front = lang_data[1]
        lang_back = lang_data[2]
        lang_extension = lang_data[3]

        file_name = input("What is the name of your file? (do not include the extension)\n")
        new_file = open(file_name + lang_extension, "w+")

        name = input("What is your name? (Enter n/a if not applicable)\n")
        if name.lower() != "n/a":
            new_file.write(lang_front + " " + name + " " + lang_back + "\n")

        date_yn = input("Do you want today's date in your comment? (y/n)\n")
        if date_yn.lower() == "y":
            today = date.today()
            creation_date = "%d/%d/%d" % (today.month, today.day, today.year)
            new_file.write(lang_front + " " + creation_date + " " + lang_back + "\n")

        your_class = input("What class is this for? (Enter n/a if not applicable)\n")
        if name.lower() != "n/a":
            new_file.write(lang_front + " " + your_class + " " + lang_back + "\n")

        done = input("Do you want to write anything else in your comment? (y/n)\n")
        while done.lower() != "n":
            next_input = input("What would you like your next line to say?\n")
            new_file.write(lang_front + " " + next_input + " " + lang_back + "\n")
            
            done = input("Do you want to write anything else in your comment? (y/n)\n")

    def unknown_lang(self, lang):
        print("I don't think I've heard of %s. Can you help me learn?" % lang)
        front = input("How do you begin a single-line comment in %s?\n" % lang)

        back_yn = input("Does %s need something to end a single-line comment? (y/n)\n" % lang)
        if back_yn.lower()[0] == "y":
            back = input("How do you end a single-line comment in %s?\n" % lang)
        else:
            back = ""

        extension = input("Finally, what is the file extension for %s? (include the '.', like '.py')\n" % lang)
        print("Thanks for the info!")

        self.db.insert(lang, front, back, extension)