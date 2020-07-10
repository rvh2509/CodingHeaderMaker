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
        new_file = open(file_name + lang_extension)

        name = input("What is your name? (Enter n/a if not applicable)\n")

        date_yn = input("Do you want today's date in your comment? (y/n)\n")
        today = date.today()
        creation_date = "%d/%d/%d" % (today.month, today.day, today.year)

        your_class = input("What class is this for? (Enter n/a if not applicable)\n")

        done = input("Do you want to write anything else in your comment? (y/n)\n")
        while done.lower() != "n":
            next_input = input("What would you like your next line to say?\n")
            done = input("Do you want to write anything else in your comment? (y/n)\n")

    def unknown_lang(self, lang):
        print("I don't think I've heard of %s. Can you help me learn?\n" % lang)
        front = input("How do you begin a single-line comment in %s?\n" % lang)

        back_yn = input("Does %s need something to end a single-line comment? (y/n)\n" % lang)
        if back_yn.lower()[0] == "y":
            back = input("How do you end a single-line comment in %s?\n" % lang)
        else:
            back = ""

        extension = input("Finally, what is the file extension for %s? (include the '.', like '.py')\n" % lang)
        print("Thanks for the info!\n")

        self.db.insert(lang, front, back, extension)