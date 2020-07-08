import sqlite3

class LangDB:
    def __init__(self):
        self.conn = sqlite3.connect("languages.db")
        self.curr = self.conn.cursor()
        self.curr.execute("CREATE TABLE IF NOT EXISTS langs (name TEXT, front TEXT, back TEXT)")
        self.conn.commit()

    def insert(self, name, front, back):
        self.curr.execute("INSERT INTO langs VALUES (?, ?, ?)", (name, front, back))
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

    def __del__(self):
        self.conn.close()