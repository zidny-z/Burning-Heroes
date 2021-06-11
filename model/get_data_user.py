import model.database_connect
import mysql.connector

class get_user(model.database_connect.koneksi):
    def __init__(self):
        model.database_connect.koneksi.__init__(self)

    #set data untuk user baru
    def set_user_baru(self,username,password,hint):
        sql = "INSERT INTO user(username,password,stage,koins,hint) VALUES (%s, %s, %s, %s, %s)"
        val = [(username,password,0,200,hint)]
        self.cursor.executemany(sql, val)
        self.con.commit()

    #mengambil data stage user
    def get_stage(self,username):
        self.cursor.execute("select stage from user where username = '{}'".format(username))
        res = self.cursor.fetchone()
        return(res[0])

    def set_stage(self,username,stage):
        sql= "UPDATE user SET stage = '{}' WHERE username = '{}'".format(stage,username)
        self.cursor.execute(sql)
        self.con.commit()

    def set_login(self,username):
        sql= "UPDATE user SET login_status = '1' WHERE username = '{}'".format(username)
        self.cursor.execute(sql)
        self.con.commit()

    def set_koin(self,username,koin):
        sql = "UPDATE user SET koins='{}' WHERE username = '{}'".format(koin,username)
        self.cursor.execute(sql)
        self.con.commit()

    def restart_login(self):
        sql= "UPDATE user SET login_status = '0'"
        self.cursor.execute(sql)
        self.con.commit()

    def get_hint(self,username):
        self.cursor.execute("select hint from user where username = '{}'".format(username))
        res = self.cursor.fetchone()
        return res[0]

    def get_username(self):
        self.cursor.execute("select username from user")
        res = self.cursor.fetchall()
        return res

    def get_password(self, username):
        self.cursor.execute("select password from user where username = '{}'".format(username))
        res = self.cursor.fetchone()
        return res[0]

    def get_koin(self, username):
        self.cursor.execute("select koins from user where username = '{}'".format(username))
        res = self.cursor.fetchone()
        return res[0]

    def get_user(self):
        self.cursor.execute("select username from user where login_status = '1'")
        res = self.cursor.fetchone()
        return res[0]

    def set_aktif_user(self):
        sql = "INSERT INTO user(username,password,stage,koins,hint) VALUES (%s, %s, %s, %s, %s)"
        val = [(username,password,0,200,hint)]
        self.cursor.executemany(sql, val)
        self.con.commit()