import viewUI, wx
from model.get_data_user import get_user
from control import c_home


class control_login():
    def __init__(self):
        self.view =viewUI.v_login(parent=None)
        self.view.Show()

    def cek_login(self, password, username):
        model = get_user()
        database_username = model.get_username()
        db_username = []
        for i in range(len(database_username)):
            db_username.append(database_username[i][0])
        if username in db_username:
            stage = model.get_stage(username)
            db_password = model.get_password(username)
            if password == db_password:
                db = get_user()
                db.set_login(username)
                return True, stage
            else:
                wx.MessageBox("Password yang anda masukkkan salah!")
        else:
            wx.MessageBox("username anda tidak terdaftar!")


    def lupa_password(self,username):
        if username == "":
            wx.MessageBox("Masukkan username terlebih dahulu!")
        else:
            self.model = get_user()
            self.hint_user = self.model.get_hint(username)
            print(self.hint_user)
            wx.MessageBox(str(self.hint_user))
