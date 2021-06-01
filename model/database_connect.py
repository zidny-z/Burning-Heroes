import mysql.connector

class koneksi:
    def __init__(self):
        try:
            self.con=mysql.connector.connect(
                host="localhost",
                user="root",
                database="BurningHeroes"
            )
            self.cursor= self.con.cursor()
        except:
            a = input("Database belum terkoneksi, silahkan koneksikan database terlebih dahulu!\nTekan apa saja untuk melanjutkan ")