from database_connect import koneksi
import mysql.connector

class get_item(koneksi):
    def __init__(self):
        koneksi.__init__(self)

    #untuk user baru
    def get_data_item(self,username):
        self.cursor.execute("select NamaItem, value, storage, price from item where username = '{}'".format(username))
        self.res = self.cursor.fetchall()

    def set_item_user_baru(self):
        sql = "INSERT INTO hero(NamaItem, value, storage, price) VALUES (%s, %s, %s, %s)"
        val = self.res
        mycursor.executemany(sql, val)
        mydb.commit()

    #mengambil storage atau jumlah item yang dimiliki
    def get_storage_meat(self,username):
        self.cursor.execute("select storage from item where username = '{}' and NamaItem = 'meat'".format(username))
        self.res = self.cursor.fetchone()
        return(self.res[0])

    def get_storage_potion(self,username):
        self.cursor.execute("select storage from item where username = '{}' and NamaItem = 'potion'".format(username))
        self.res = self.cursor.fetchone()
        return(self.res[0])

    def get_storage_giant_potion(self,username):
        self.cursor.execute("select storage from item where username = '{}' and NamaItem = 'giant_otion'".format(username))
        self.res = self.cursor.fetchone()
        return(self.res[0])

    def get_storage_sharpener(self,username):
        self.cursor.execute("select storage from item where username = '{}' and NamaItem = 'sharpener'".format(username))
        self.res = self.cursor.fetchone()
        return(self.res[0])

user = get_item()
print(user.get_storage_potion("poi"))
    