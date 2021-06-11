import viewUI, wx
from model import get_data_user, get_data_hero, get_data_item

class control_daftar():
    def __init__(self):
        self.view =viewUI.v_daftar(parent=None)
        self.view.Show()

    def user_signup(self, password, username, hint, password2):
        if password2 != "" and username != "" and hint != "" and password2 != "":
            if password == password2:
                self.model = get_data_user.get_user()
                self.model.set_user_baru(username,password,hint)
                self.model = get_data_hero.get_hero()
                data_hero = self.model.get_data("bot")
                nama_hero = ["Batman", "Superman", "Joker", "Wonder Women"]
                nama_item = ["potion","meat","sharpener","giant potion"]
                self.model = get_data_hero.get_hero()
                for i in range(len(nama_hero)):
                    self.model.set_hero_user_baru(nama_hero[i],data_hero[i],username)
                self.model = get_data_item.get_item()
                data_item = self.model.get_data_item("bot")
                for i in range(len(nama_item)):
                    self.model.set_item_user_baru(data_item[i],username)
                return True
            else:
                wx.MessageBox("Password yang anda masukkan tidak sama")
        else:
            wx.MessageBox("Silahkan masukkan seluruh data yang diminta!")
