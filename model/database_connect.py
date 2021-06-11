import mysql.connector
import wx

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
            wx.MessageBox("Database belum terkoneksi, silahkan koneksikan database terlebih dahulu!")