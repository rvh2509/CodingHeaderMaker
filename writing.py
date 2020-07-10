from datetime import date

class CodeWriter:
    def __init__(self):
        lang = input("What language are you working in today?\n")
        self.front = input("How do you begin a single-line comment in %s?\n" % lang)

        back_yn = input("Does %s need something to end a single-line comment? (y/n)\n" % lang)
        if back_yn.lower()[0] == "y":
            self.back = input("How do you end a single-line comment in %s?\n" % lang)
        else:
            self.back = ""

    def ask_questions(self, lang):
        name = input("What is your name? (Enter n/a if not applicable)\n")

        date_yn = input("Do you want today's date in your comment? (y/n)\n")
        today = date.today()
        creation_date = "%d/%d/%d" % (today.month, today.day, today.year)

        your_class = input("What class is this for? (Enter n/a if not applicable)\n")

        done = input("Do you want to write anything else in your comment? (y/n)\n")
        while done.lower() != "n":
            next_input = input("What would you like your next line to say?\n")
            done = input("Do you want to write anything else in your comment? (y/n)\n")