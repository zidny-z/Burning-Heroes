from model.get_data_item import get_item
from model.get_data_hero import get_hero
from mysql.connector import fabric
from control import c_daftar, c_login, c_main, c_home, c_fight, c_petunjuk_permainan, c_shop,c_inventory, c_pilih_hero, c_menu_hero
import webbrowser
import wx
import noname

class v_halaman_awal(noname.f_halaman_awal):
	def __init__(self,parent):
		noname.f_halaman_awal.__init__(self,parent)

	def img_daftarOnButtonClick( self, event ):
		self.Destroy()
		self.controler = c_daftar.control_daftar()

	def img_loginOnButtonClick( self, event ):
		self.Destroy()
		self.controler = c_login.control_login()

class v_login(noname.f_login):
	def __init__(self,parent):
		noname.f_login.__init__(self,parent)

	def btn_lupa_pswdOnButtonClick( self, event ):
		self.username = self.login_username.GetValue()
		c_login.control_login.lupa_password(self,self.username)

	def btn_loginOnButtonClick( self, event ):
		self.Destroy()
		self.username = self.login_username.GetValue()
		self.password = self.login_Password.GetValue()
		controler, stage = c_login.control_login.cek_login(False,self.password,self.username)
		if controler:
			self.controler = c_home.control_menu(self.username, stage)


class v_daftar(noname.f_daftar):
	def __init__(self,parent):
		noname.f_daftar.__init__(self,parent)	

	def btn_daftarOnButtonClick( self, event ):
		self.Destroy()
		self.username = self.daftar_username.GetValue()
		self.password = self.daftar_password.GetValue()
		self.hint = self.daftar_hint.GetValue()
		self.password2 = self.daftar_password2.GetValue()
		self.controler = c_daftar.control_daftar.user_signup(self,self.password,self.username,self.hint,self.password2)
		if self.controler:
			self.controler = c_home.control_menu(self.username,0)


class v_menu(noname.f_menu):
	def __init__(self,parent):
		noname.f_menu.__init__(self,parent)

	def set_value(self,username, stage):
		self.username = username
		self.stage = stage
		self.menu_username.SetLabel(self.username)
		self.menu_stage.SetLabel(str(self.stage))

	def fightOnButtonClick( self, event ):
		self.Destroy()
		self.controller = c_pilih_hero.control_pilih_hero(self.username,self.stage)
		event.Skip()

	def hero_menuOnButtonClick( self, event ):
		self.Destroy()
		self.controller = c_menu_hero.control_hero(self.username,self.stage)

	def inventoryOnButtonClick( self, event ):
		self.Destroy()
		self.controller = c_inventory.control_inventory(self.username,self.stage)

	def shopOnButtonClick( self, event ):
		self.Destroy()
		self.controller = c_shop.control_shop(self.username,self.stage,True)

	def petunjukOnButtonClick( self, event ):
		self.Destroy()
		self.controller = c_petunjuk_permainan.control_petunjuk(self.username,self.stage)

	def tentangOnButtonClick( self, event ):
		webbrowser.open_new_tab('https://github.com/zidny-z/Burning-Heroes')


	def exitOnButtonClick( self, event ):
		exit()


class v_petunjuk_permainan(noname.f_petunjuk_permainan):
	def __init__(self,parent,username,stage):
		noname.f_petunjuk_permainan.__init__(self,parent)	
		self.username = username
		self.stage = stage

	def back_homeOnButtonClick( self, event ):
		self.Destroy()
		self.controler = c_home.control_menu(self.username, self.stage)
		event.Skip()

class v_hero_menu(noname.f_hero_menu):
	def __init__(self,parent,username,stage):
		noname.f_hero_menu.__init__(self,parent)
		self.username = username
		self.stage = stage

	def set_view_hero(self,data_hero):
		self.attack_batman.SetLabel(str(data_hero[0][0]))
		self.attack_superman.SetLabel(str(data_hero[1][0]))
		self.attack_joker.SetLabel(str(data_hero[2][0]))
		self.attack_wonder_women.SetLabel(str(data_hero[3][0]))

		self.hp_batman.SetLabel(str(data_hero[0][1]))
		self.hp_superman.SetLabel(str(data_hero[1][1]))
		self.hp_joker.SetLabel(str(data_hero[2][1]))
		self.hp_wonder_women.SetLabel(str(data_hero[3][1]))

		self.max_hp_batman.SetLabel(str(data_hero[0][2]))
		self.max_hp_superman.SetLabel(str(data_hero[1][2]))
		self.max_hp_joker.SetLabel(str(data_hero[2][2]))
		self.max_hp_wonder_women.SetLabel(str(data_hero[3][2]))

	def m_bpButton65OnButtonClick( self, event ):
		self.Destroy()
		self.controler = c_home.control_menu(self.username, self.stage)
		event.Skip()

class v_inventory(noname.f_inventory):
	def __init__(self,parent,username,stage):
		noname.f_inventory.__init__(self,parent)	
		self.username = username
		self.stage = stage

	def set_view_item(self,data_item,koin):
		self.jumlah_giant_potion.SetLabel(str(data_item[3][0]))
		self.jumlah_koin.SetLabel(str(koin))
		self.jumlah_meat.SetLabel(str(data_item[1][0]))
		self.jumlah_potion.SetLabel(str(data_item[0][0]))
		self.jumlah_sharpener.SetLabel(str(data_item[2][0]))

	def back_homeOnButtonClick( self, event ):
		self.Destroy()
		self.controler = c_home.control_menu(self.username, self.stage)
		event.Skip()

class v_shop(noname.f_shop):
	def __init__(self,parent,username,stage,koin):
		noname.f_shop.__init__(self,parent)
		self.koin = koin
		self.jumlah_koin.SetLabel(str(self.koin))
		self.username = username
		self.stage = stage

	def back_homeOnButtonClick( self, event ):
		self.Destroy()
		self.controler = c_home.control_menu(self.username, self.stage)

	def beli_meatOnButtonClick( self, event ):
		self.Destroy()
		c_shop.control_shop(self.username,self.stage,False).set_item("meat")
		self.jumlah_koin.SetLabel(str(self.koin))

	def beli_potionOnButtonClick( self, event ):
		self.Destroy()
		c_shop.control_shop(self.username,self.stage,False).set_item("potion")
		self.jumlah_koin.SetLabel(str(self.koin))

	def beli_sharpenerOnButtonClick( self, event ):
		self.Destroy()
		c_shop.control_shop(self.username,self.stage,False).set_item("Sharpener")
		self.jumlah_koin.SetLabel(str(self.koin))

	def beli_giant_potionOnButtonClick( self, event ):
		self.Destroy()
		c_shop.control_shop(self.username,self.stage,False).set_item("Giant Potion")
		self.jumlah_koin.SetLabel(str(self.koin))


class v_fight(noname.f_fight):
	def __init__(self,parent, username, stage, hero_fight, data_item, musuh):
		noname.f_fight.__init__(self,parent)
		self.data_item = data_item
		self.username = username
		self.stage = stage
		self.hero_fight = hero_fight
		self.musuh = musuh

	def set_view_item(self,data_item):
		self.jumlah_giant_potion.SetLabel(str(data_item[3]))
		self.jumlah_meat.SetLabel(str(data_item[1]))
		self.jumlah_potion.SetLabel(str(data_item[0]))
		self.jumlah_sharpener.SetLabel(str(data_item[2]))

	def set_hero_satu(self,hero1):
		self.m_bpButton38.SetBitmap( wx.Bitmap( u"{}".format(hero1[3]), wx.BITMAP_TYPE_ANY ) )
		self.attack_hero_user1.SetLabel(str(hero1[0]))
		self.hp_hero_user1.SetLabel(str(hero1[1]))
		self.max_hp_hero_user1.SetLabel(str(hero1[2]))

	def set_hero_dua(self,hero2):
		self.m_bpButton383.SetBitmap( wx.Bitmap( u"{}".format(hero2[3]), wx.BITMAP_TYPE_ANY ) )
		self.attack_hero_user2.SetLabel(str(hero2[0]))
		self.hp_hero_user2.SetLabel(str(hero2[1]))
		self.max_hp_hero_user2.SetLabel(str(hero2[2]))

	def set_musuh_satu(self,musuh):
		self.m_bpButton384.SetBitmap( wx.Bitmap( u"{}".format(musuh[3]), wx.BITMAP_TYPE_ANY ) )
		self.attack_hero_musuh1.SetLabel(str(musuh[0]))
		self.hp_hero_musuh1.SetLabel(str(musuh[1]))
		self.max_hp_hero_musuh1.SetLabel(str(musuh[2]))

	def set_musuh_dua(self,musuh):
		self.m_bpButton381.SetBitmap( wx.Bitmap( u"{}".format(musuh[3]), wx.BITMAP_TYPE_ANY ) )
		self.attack_hero_musuh2.SetLabel(str(musuh[0]))
		self.hp_hero_musuh2.SetLabel(str(musuh[1]))
		self.max_hp_hero_musuh2.SetLabel(str(musuh[2]))

	def btn_pakai_potionOnButtonClick( self, event ):
		self.Destroy()
		c_fight.control_fight(self.username, self.stage, self.hero_fight, True, self.data_item, self.musuh).use_potion()

	def btn_pakai_sharpenerOnButtonClick( self, event ):
		self.Destroy()
		c_fight.control_fight(self.username, self.stage, self.hero_fight, True, self.data_item, self.musuh).use_sharpener()

	def btn_pakai_giant_potionOnButtonClick( self, event ):
		self.Destroy()
		c_fight.control_fight(self.username, self.stage, self.hero_fight, True, self.data_item, self.musuh).use_giant_potion()

	def btn_pakai_meatOnButtonClick( self, event ):
		self.Destroy()
		c_fight.control_fight(self.username, self.stage, self.hero_fight, True, self.data_item, self.musuh).use_meat()

	def btn_ganti_heroOnButtonClick( self, event ):
		self.Destroy()
		c_fight.control_fight(self.username, self.stage, self.hero_fight, True, self.data_item, self.musuh).swap_hero()


	def btn_serangOnButtonClick( self, event ):
		self.Destroy()
		c_fight.control_fight(self.username, self.stage, self.hero_fight, True, self.data_item, self.musuh).attack()


class v_pilih_hero_fight(noname.f_pilih_hero_fight):
	def __init__(self,parent,username,stage):
		noname.f_pilih_hero_fight.__init__(self,parent)	
		self.username = username
		self.stage = stage
		self.pilihan = []
		self.hero_fight = []
		self.musuh = []


	def set_view_hero(self,data_hero):
		self.data = data_hero

		self.attack_batman.SetLabel(str(data_hero[0][0]))
		self.attack_superman.SetLabel(str(data_hero[1][0]))
		self.attack_joker.SetLabel(str(data_hero[2][0]))
		self.attack_wonder_women.SetLabel(str(data_hero[3][0]))

		self.hp_batman.SetLabel(str(data_hero[0][1]))
		self.hp_superman.SetLabel(str(data_hero[1][1]))
		self.hp_joker.SetLabel(str(data_hero[2][1]))
		self.hp_wonder_women.SetLabel(str(data_hero[3][1]))

		self.max_hp_batman.SetLabel(str(data_hero[0][2]))
		self.max_hp_superman.SetLabel(str(data_hero[1][2]))
		self.max_hp_joker.SetLabel(str(data_hero[2][2]))
		self.max_hp_wonder_women.SetLabel(str(data_hero[3][2]))

	def cb_hero_batmanOnCheckBox( self, event ):
		if self.cb_hero_batman.IsChecked():
			self.pilihan.append("Batman")
		else:
			try:
				self.pilihan.remove("Batman")
			except:
				pass

	def cb_hero_jokerOnCheckBox( self, event ):
		if self.cb_hero_joker.IsChecked():
			self.pilihan.append("Joker")
		else:
			try:
				self.pilihan.remove("Joker")
			except:
				pass

	def cb_hero_supermanOnCheckBox( self, event ):
		if self.cb_hero_superman.IsChecked():
			self.pilihan.append("Superman")
		else:
			try:
				self.pilihan.remove("Superman")
			except:
				pass

	def cb_hero_wonderwomenOnCheckBox( self, event ):
		if self.cb_hero_wonderwomen.IsChecked():
			self.pilihan.append("Wonder Women")
		else:
			try:
				self.pilihan.remove("Wonder Women")
			except:
				pass

	def btn_pilih_heroOnButtonClick( self, event ):
		batman = "properties/img/250125/batman_fight.bmp"
		superman = "properties/img/250125/superman_fight.bmp"
		wonderwomen = "properties/img/250125/wonderwomen_fight.bmp"
		joker = "properties/img/250125/joker_fight.bmp"

		if len(self.pilihan) > 2:
			wx.MessageBox("Hanya diperbolehkan memilih 2 karakter!")
		elif len(self.pilihan) < 2:
			wx.MessageBox("Anda harus memilih 2 karakter!")
		else:
			self.Destroy()
			for i in self.pilihan:
				if i == "Batman":
					self.hero_fight.append([self.data[0][0],self.data[0][1],self.data[0][2],batman]) 
				elif i == "Superman":
					self.hero_fight.append([self.data[1][0],self.data[1][1],self.data[1][2],superman])
				elif i == "Joker":
					self.hero_fight.append([self.data[2][0],self.data[2][1],self.data[2][2],joker])
				else:
					self.hero_fight.append([self.data[3][0],self.data[3][1],self.data[3][2],wonderwomen])
			self.data_item = get_item().get_storage(self.username)
			data_item = []
			for i in self.data_item:
				data_item.append(i[0])
			self.set_musuh()
			self.controller = c_fight.control_fight(self.username,self.stage,self.hero_fight,True,data_item, self.musuh)

	def set_musuh(self):
		self.level = [
["joker","superman"],
["joker","batman"],
["joker","wonder women"],
["superman","joker"],
["superman","batman"],
["superman","wonder women"],
["batman","joker"],
["batman","superman"],
["batman","wonder women"],
["wonder women","joker"],
["wonder women","superman"],
["wonder women","batman"],
]
		model = get_hero()
		for i in self.level[self.stage]:
			isi = model.get_musuh(i)
			isi = list(isi)
			if i == "batman":
				gambar = "properties/img/250125/batman_fight.bmp"
			elif i == "superman":
				gambar = "properties/img/250125/superman_fight.bmp"
			elif i == "wonder women":
				gambar = "properties/img/250125/wonderwomen_fight.bmp"
			else:
				gambar = "properties/img/250125/joker_fight.bmp"
			isi.append(gambar)
			self.musuh.append(isi)
			isi = ""