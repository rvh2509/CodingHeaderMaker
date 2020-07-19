import sqlite3

class LangDB:
    def __init__(self):
        self.conn = sqlite3.connect("languages.db")
        self.curr = self.conn.cursor()
        self.curr.execute("CREATE TABLE IF NOT EXISTS langs (name TEXT, front TEXT, back TEXT, extension TEXT)")
        self.conn.commit()

    def insert(self, name, front, back, extension):
        self.curr.execute("INSERT INTO langs VALUES (?, ?, ?, ?)", (name, front, back, extension))
        self.conn.commit()

    def view_all(self):
        self.curr.execute("SELECT * FROM langs")
        rows = self.curr.fetchall()
        return rows

    def search_by_name(self, name):
        self.curr.execute("SELECT * FROM langs WHERE name=?", (name,))
        rows = self.curr.fetchall()
        return rows[0]

    def delete_by_name(self, name):
        self.curr.execute("DELETE FROM langs WHERE name=?", (name,))
        self.conn.commit()

    # TODO: Make sure to do something for when they say n/a
    def write_to_file(self, lang, file_name, name, creation_date, your_class, extras):
        lang_data = self.search_by_name(lang)
        lang_front = lang_data[1]
        lang_back = lang_data[2]
        lang_extension = lang_data[3]

        new_file = open(file_name + lang_extension, "w+")
        new_file.write(lang_front + " " + name + " " + lang_back + "\n")
        new_file.write(lang_front + " " + creation_date + " " + lang_back + "\n")
        new_file.write(lang_front + " " + your_class + " " + lang_back + "\n")

        for line in extras:
            new_file.write(lang_front + " " + line + " " + lang_back + "\n")

    def __del__(self):
        self.conn.close()