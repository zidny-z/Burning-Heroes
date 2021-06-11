from model.database_connect import koneksi
import mysql.connector

class get_item(koneksi):
    def __init__(self):
        koneksi.__init__(self)

    #untuk user baru
    def get_data_item(self,username):
        self.cursor.execute("select NamaItem, value, storage, price from item where username = '{}'".format(username))
        self.res = self.cursor.fetchall()
        return self.res

    def set_item_user_baru(self,data_item,username):
        sql = "INSERT INTO item(NamaItem, storage, price, username) VALUES (%s, %s, %s, %s)"
        val = [(data_item[0], data_item[2], data_item[3], username)]
        self.cursor.executemany(sql, val)
        self.con.commit()

    #mengambil storage atau jumlah item yang dimiliki
    def get_storage(self,username):
        self.cursor.execute("select storage from item where username = '{}'".format(username))
        self.res = self.cursor.fetchall()
        return(self.res)

    def get_item(self,username,nama_item):
        self.cursor.execute("select price, storage from item where username = '{}' and NamaItem = '{}'".format(username, nama_item))
        self.res = self.cursor.fetchall()
        return(self.res[0][0], self.res[0][1])

    def set_item(self,username,nama_item,storage):
        sql = "UPDATE item SET storage='{}' WHERE username = '{}' and NamaItem ='{}'".format(storage, username, nama_item)
        self.cursor.execute(sql)
        self.con.commit()
