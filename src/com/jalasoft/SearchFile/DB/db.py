import os
import sqlite3


class ConnectionDB:
    dataBaseName = "search.db"

    def __init__(self):
        self.exist = os.path.exists(self.dataBaseName)

    def getConnection(self):
        con = sqlite3.connect(self.dataBaseName)

        if not self.exist:
            cu = con.cursor()
            cu.execute("Create if not exists Search(id integer, Path varchar (200), Primary Key (id));")
        return con
