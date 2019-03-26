<<<<<<< HEAD
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
=======
import sqlite3

# con_bd = sqlite3.connect('contacts.db')
# con_bd.close()
# cursor_agenda = con_bd.cursor()
# cursor_agenda.close()
# reg = (1, "A", "a@a.a", 1)
# cursor_agenda.execute("INSERT INTO agenda VALUES(?,?,?,?)", reg)
# con_bd.commit()
# cursor_agenda.execute("SELECT * FROM agenda")
# for registro in cursor_agenda:
#     print(registro)
# par = (1,)
# cursor_agenda.execute("SELECT * FROM agenda WHERE ident=?", par)
# for registro in cursor_agenda:
#     print(registro)
>>>>>>> ba8f63a01ed9be559828963a63b337d22694f3c8
