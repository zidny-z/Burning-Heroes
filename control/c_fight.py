import viewUI, wx, random, time
from model.get_data_hero import get_hero
from model.get_data_item import get_item
from model.get_data_user import get_user
from control.c_home import control_menu

class control_fight():
    def __init__(self, username, stage, hero_fight,show, data_item, musuh):
        self.view = viewUI.v_fight(None, username, stage, hero_fight, data_item, musuh)
        self.hero_fight = hero_fight
        self.username = username
        self.item = ["potion","meat","sharpener","giant potion"]
        self.musuh = musuh
        self.stage = stage
        self.ket = ""

        self.data_item = data_item
        self.view.set_view_item(self.data_item)

        self.view.set_hero_satu(hero_fight[0])
        self.view.set_hero_dua(hero_fight[1])

        self.view.set_musuh_satu(self.musuh[0])
        self.view.set_musuh_dua(self.musuh[1])

        self.view.Show(show)


        
    def use_potion(self):
        if self.check_item(self.data_item[0]):
            value = round(random.uniform(1.2, 1.3),2)
            self.hero_fight[0][0] = (self.hero_fight[0][0] * value)
            self.data_item[0] =  self.data_item[0] - 1
            self.refresh_hero()
            self.refresh_item()
        else:
            wx.MessageBox("Item tiidak cukup untuk digunakan!")
        

    def use_giant_potion(self):
        if self.check_item(self.data_item[3]):
            value = round(random.uniform(1.2, 1.3),2)
            self.hero_fight[0][1] = (self.hero_fight[0][1] * value)
            self.data_item[3] =  self.data_item[3] - 1
            self.refresh_hero()
            self.refresh_item()
        else:
            wx.MessageBox("Item tiidak cukup untuk digunakan!")

    def use_meat(self):
        if self.check_item(self.data_item[1]):
            self.hero_fight[0][1] = (self.hero_fight[0][1] + 50)
            self.data_item[1] =  self.data_item[1] - 1
            self.refresh_hero()
            self.refresh_item()
        else:
            wx.MessageBox("Item tiidak cukup untuk digunakan!")

    def use_sharpener(self):
        if self.check_item(self.data_item[2]):
            self.hero_fight[0][0] = (self.hero_fight[0][0] + 20)
            self.data_item[2] =  self.data_item[2] - 1
            self.refresh_hero()
            self.refresh_item()
        else:
            wx.MessageBox("Item tiidak cukup untuk digunakan!")

    def attack(self):
        self.musuh[0][1] = self.musuh[0][1] - self.hero_fight[0][0]
        self.refresh_musuh()
        self.check_winner()
        self.keterangan("Anda menyerang musuh!")
        # time.sleep(2)
        self.bot_turn()

    def swap_hero(self):
        self.hero_fight.reverse()
        self.refresh_hero()
        self.keterangan("Anda mengganti hero!")
        # time.sleep(2)
        self.bot_turn()

    def refresh_hero(self):
        self.view.set_hero_satu(self.hero_fight[0])
        self.view.set_hero_dua(self.hero_fight[1])

    def refresh_item(self):
        self.view.set_view_item(self.data_item)

    def refresh_musuh(self):
        self.view.set_musuh_satu(self.musuh[0])
        self.view.set_musuh_dua(self.musuh[1])

    def bot_attack(self):
        self.hero_fight[0][1] = self.hero_fight[0][1] - self.musuh[0][0]
        self.refresh_hero()
        self.check_winner()
        self.keterangan("Musuh menyerang anda!")

    def bot_swap_hero(self):
        self.musuh.reverse()
        self.refresh_musuh()
        self.keterangan("Musuh mengganti hero!")

    def bot_turn(self):
        turn = random.randint(0,1)
        if turn == 1:
            self.bot_attack()
        else:
            self.bot_swap_hero()

    def check_winner(self):
        if self.hero_fight[0][1] <= 0 or self.musuh[0][1] <= 0:
            koin = get_user().get_koin(self.username)
            if self.musuh[0][1] <= 0:
                wx.MessageBox("Selamat anda menang")
                self.stage = self.stage + 1
                get_user().set_stage(self.username,self.stage)
                get_user().set_koin(self.username,koin + 200)
            elif self.hero_fight[0][1] <= 0:
                wx.MessageBox("Anda Kalah!")
                get_user().set_koin(self.username,koin + 100)
            for i in range(len(self.item)):
                get_item().set_item(self.username,self.item[i],self.data_item[i])
            self.controller = control_menu(self.username,self.stage)


    def check_item(self,item):
        if item > 0:
            return True
        else:
            return False

    def keterangan(self,isi):
        self.ket = self.ket + isi + '\n'
        self.view.keterangan_perang.SetValue(self.ket)
