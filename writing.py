class CodeWriter:
    def __init__(self):
        self.lang = input("What language are you working in today?\n")
        self.front = input("How do you begin a single-line comment in %s?\n" % self.lang)

        back_yn = input("Does %s need something to end a single-line comment? (y/n)\n" % self.lang)
        if back_yn.lower()[0] == "y":
            self.back = input("How do you end a single-line comment in %s?\n" % self.lang)
        else:
            self.back = ""