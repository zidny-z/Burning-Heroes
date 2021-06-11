import viewUI, wx
from model import get_data_hero,get_data_user


class control_pilih_hero():
    def __init__(self,username,stage):
        self.data_hero = get_data_hero.get_hero().get_data(username)
        self.view = viewUI.v_pilih_hero_fight(None, username,stage)
        self.view.set_view_hero(self.data_hero)
        self.view.Show()