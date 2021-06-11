import model.database_connect
import mysql.connector

class get_hero(model.database_connect.koneksi):
    def __init__(self):
        model.database_connect.koneksi.__init__(self)

    #mengambil data hero
    def get_data(self,username):
        self.cursor.execute("select heroattack, herohp, maxhp from hero where username = '{}'".format(username))
        res = self.cursor.fetchall()
        return res
    
    def get_musuh(self,nama_hero):
        self.cursor.execute("select heroattack, herohp, maxhp from hero where username = 'bot' and HeroName = '{}'".format(nama_hero))
        res = self.cursor.fetchall()
        return res[0]

    #set hero untuk user baru
    def set_hero_user_baru(self,heroname,data,username):
        sql = "INSERT INTO hero(HeroName, HeroAttack, HeroHP, MaxHP, username) VALUES (%s, %s, %s, %s, %s)"
        val = [(heroname,int(data[0]),int(data[1]),int(data[2]),username)]
        self.cursor.executemany(sql, val)
        self.con.commit()
