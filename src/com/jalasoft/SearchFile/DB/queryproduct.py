from src.com.jalasoft.SearchFile.DB.db import ConnectionDB


class QueryProduct:
    def __init__(self):
        self.conn = ConnectionDB().getConnection()

    def insertProduct(self,path):#criteria
        cur  = self.conn.cursor()
        cur.execute("inset into search (path) values("+ path +")") #"+ criteria.getPath() +"
        cur.commit()

    def showProduct(self):
        cur = self.conn.cursor()
        cur.execute("select id, path, form search")
        productList = []
        for row in cur.fetchall():
            pro = Product()
            pro.setId(row[0])
            pro.setPath(row[1])
            productList.append(pro)