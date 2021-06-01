import database_connect
import mysql.connector

class get_hero(database_connect.koneksi):
    def __init__(self):
        database_connect.koneksi.__init__(self)

    #mengambil data hero
    def get_hero_batman(self,username):
        self.cursor.execute("select heroname, heroattack, herohp, maxhp from hero where username = '{}' and HeroName = 'batman'".format(username))
        self.res = self.cursor.fetchall()
    def get_hero_superman(self,username):
        self.cursor.execute("select heroname, heroattack, herohp, maxhp from hero where username = '{}' and HeroName = 'superman'".format(username))
        self.res = self.cursor.fetchall()
    def get_hero_joker(self,username):
        self.cursor.execute("select heroname, heroattack, herohp, maxhp from hero where username = '{}' and HeroName = 'joker'".format(username))
        self.res = self.cursor.fetchall()
    def get_hero_wonderwoman(self,username):
        self.cursor.execute("select heroname, heroattack, herohp, maxhp from hero where username = '{}' and HeroName = 'wonderwoman'".format(username))
        self.res = self.cursor.fetchall()
    


    #set hero untuk user baru
    def set_hero_user_baru(self):
        sql = "INSERT INTO hero(heroname, herorole, heroattack, herohp, maxhp, username) VALUES (%s, %s, %s, %s,%s, %s)"
        val = self.res
        mycursor.executemany(sql, val)
        mydb.commit()
