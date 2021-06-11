import viewUI, wx
from model import get_data_item,get_data_user

class control_shop():
    def __init__(self,username,stage,show):
        self.username = username
        self.stage = stage
        self.koin = get_data_user.get_user().get_koin(self.username)
        self.view = viewUI.v_shop(None, username, stage,self.koin)
        self.view.Show(show)

    def set_item(self,nama_item):
        self.price, self.storage = get_data_item.get_item().get_item(self.username,nama_item)
        if self.set_koin():
            self.storage = self.storage + 1
            get_data_item.get_item().set_item(self.username, nama_item, self.storage)
        else:
            wx.MessageBox("Mohon maaf koin anda tidak cukup untuk membeli item {}".format(nama_item))

    def set_koin(self):
        self.koin = self.koin - self.price
        get_data_user.get_user().set_koin(self.username,self.koin)
        control_shop(self.username,self.stage,True)
        return True
