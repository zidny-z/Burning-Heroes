import database_connect
import mysql.connector

class get_user(database_connect.koneksi):
    def __init__(self):
        database_connect.koneksi.__init__(self)

    #set data untuk user baru
    def set_user_baru(self,username,password):
        sql = "INSERT INTO user(username,password,stage,koins) VALUES (%s, %s, %s, %s)"
        val = [(username,password,0,200)]
        self.cursor.executemany(sql, val)
        self.con.commit()

    #mengambil data stage user
    def get_stage(self,username):
        self.cursor.execute("select stage from user where username = '{}'".format(username))
        res = self.cursor.fetchone()
        print(res[0])


user = get_user()
user.get_stage("p")


