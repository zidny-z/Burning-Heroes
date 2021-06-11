import viewUI, wx
from model import get_data_item, get_data_user

class control_inventory():
    def __init__(self,username,stage):
        self.view = viewUI.v_inventory(None, username, stage)
        self.data_item = get_data_item.get_item().get_storage(username)
        self.koin = get_data_user.get_user().get_koin(username)
        self.view.set_view_item(self.data_item,self.koin)
        self.view.Show()
