# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class f_halaman_awal
###########################################################################

class f_halaman_awal ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Burning Heroes", pos = wx.DefaultPosition, size = wx.Size( 637,425 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_CAPTIONTEXT ) )

		bSizer1 = wx.BoxSizer( wx.HORIZONTAL )

		self.img_sider = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"properties/img/sider.bmp", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 200,400 ), 0 )
		bSizer1.Add( self.img_sider, 0, wx.ALL, 5 )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.img_banner = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"properties/img/BANNER.bmp", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 400,200 ), 0 )
		bSizer2.Add( self.img_banner, 0, wx.ALL, 5 )

		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

		self.img_daftar = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 200,200 ), wx.BU_AUTODRAW|0 )

		self.img_daftar.SetBitmap( wx.Bitmap( u"properties/img/daftar.bmp", wx.BITMAP_TYPE_ANY ) )
		self.img_daftar.SetBitmapDisabled( wx.Bitmap( u"properties/img/daftar.bmp", wx.BITMAP_TYPE_ANY ) )
		self.img_daftar.SetBitmapPressed( wx.Bitmap( u"properties/img/daftar.bmp", wx.BITMAP_TYPE_ANY ) )
		self.img_daftar.SetBitmapFocus( wx.Bitmap( u"properties/img/daftar.bmp", wx.BITMAP_TYPE_ANY ) )
		self.img_daftar.SetBitmapCurrent( wx.Bitmap( u"properties/img/daftar.bmp", wx.BITMAP_TYPE_ANY ) )
		self.img_daftar.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )
		self.img_daftar.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer3.Add( self.img_daftar, 0, wx.ALL, 5 )

		self.img_login = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 200,200 ), wx.BU_AUTODRAW|0 )

		self.img_login.SetBitmap( wx.Bitmap( u"properties/img/login.bmp", wx.BITMAP_TYPE_ANY ) )
		bSizer3.Add( self.img_login, 0, wx.ALL, 5 )


		bSizer2.Add( bSizer3, 1, wx.EXPAND, 5 )


		bSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.img_daftar.Bind( wx.EVT_BUTTON, self.img_daftarOnButtonClick )
		self.img_login.Bind( wx.EVT_BUTTON, self.img_loginOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def img_daftarOnButtonClick( self, event ):
		event.Skip()

	def img_loginOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class f_login
###########################################################################

class f_login ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Login - Burning Heores", pos = wx.DefaultPosition, size = wx.Size( 632,425 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )

		bSizer1 = wx.BoxSizer( wx.HORIZONTAL )

		self.img_sider = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"properties/img/sider.bmp", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 200,400 ), 0 )
		bSizer1.Add( self.img_sider, 0, wx.ALL, 5 )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.img_banner = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"properties/img/BANNER.bmp", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 400,200 ), 0 )
		bSizer2.Add( self.img_banner, 0, wx.ALL, 5 )

		bSizer11 = wx.BoxSizer( wx.VERTICAL )

		self.login_username = wx.TextCtrl( self, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.Size( 400,30 ), 0 )
		self.login_username.SetToolTip( u"Username" )

		bSizer11.Add( self.login_username, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.login_Password = wx.TextCtrl( self, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.Size( 400,30 ), 0 )
		bSizer11.Add( self.login_Password, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.cb_ingat_saya = wx.CheckBox( self, wx.ID_ANY, u"Ingat saya!", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cb_ingat_saya.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		bSizer11.Add( self.cb_ingat_saya, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.btn_lupa_pswd = wx.Button( self, wx.ID_ANY, u"Lupa Password", wx.DefaultPosition, wx.Size( 400,30 ), 0 )
		self.btn_lupa_pswd.SetToolTip( u"Lupa Password" )

		bSizer11.Add( self.btn_lupa_pswd, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.btn_login = wx.Button( self, wx.ID_ANY, u"Login", wx.DefaultPosition, wx.Size( 400,30 ), 0 )
		bSizer11.Add( self.btn_login, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer2.Add( bSizer11, 1, wx.EXPAND, 5 )


		bSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.cb_ingat_saya.Bind( wx.EVT_CHECKBOX, self.cb_ingat_sayaOnCheckBox )
		self.btn_lupa_pswd.Bind( wx.EVT_BUTTON, self.btn_lupa_pswdOnButtonClick )
		self.btn_login.Bind( wx.EVT_BUTTON, self.btn_loginOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def cb_ingat_sayaOnCheckBox( self, event ):
		event.Skip()

	def btn_lupa_pswdOnButtonClick( self, event ):
		event.Skip()

	def btn_loginOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class f_daftar
###########################################################################

class f_daftar ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Daftar - Burning Heroes", pos = wx.DefaultPosition, size = wx.Size( 629,450 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_CAPTIONTEXT ) )

		bSizer1 = wx.BoxSizer( wx.HORIZONTAL )

		self.img_sider = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"properties/img/sider.bmp", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 200,400 ), 0 )
		bSizer1.Add( self.img_sider, 0, wx.ALL, 5 )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.img_banner = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"properties/img/BANNER.bmp", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 400,200 ), 0 )
		bSizer2.Add( self.img_banner, 0, wx.ALL, 5 )

		bSizer11 = wx.BoxSizer( wx.VERTICAL )

		self.daftar_username = wx.TextCtrl( self, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.Size( 400,30 ), 0 )
		self.daftar_username.SetToolTip( u"Username" )

		bSizer11.Add( self.daftar_username, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.daftar_password = wx.TextCtrl( self, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.Size( 400,30 ), 0 )
		bSizer11.Add( self.daftar_password, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.daftar_password2 = wx.TextCtrl( self, wx.ID_ANY, u"Ulangi Password", wx.DefaultPosition, wx.Size( 400,30 ), 0 )
		bSizer11.Add( self.daftar_password2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.daftar_hint = wx.TextCtrl( self, wx.ID_ANY, u"Hint", wx.DefaultPosition, wx.Size( 400,30 ), 0 )
		self.daftar_hint.SetToolTip( u"Hint" )

		bSizer11.Add( self.daftar_hint, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.btn_daftar = wx.Button( self, wx.ID_ANY, u"Daftar", wx.DefaultPosition, wx.Size( 400,30 ), 0 )
		bSizer11.Add( self.btn_daftar, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer2.Add( bSizer11, 1, wx.EXPAND, 5 )


		bSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btn_daftar.Bind( wx.EVT_BUTTON, self.btn_daftarOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btn_daftarOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class f_menu
###########################################################################

class f_menu ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Menu - Burning Heroes", pos = wx.DefaultPosition, size = wx.Size( 777,575 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )

		bSizer1 = wx.BoxSizer( wx.HORIZONTAL )

		self.img_sider = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"properties/img/sidermenu.bmp", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 200,530 ), 0 )
		self.img_sider.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWFRAME ) )

		bSizer1.Add( self.img_sider, 0, wx.ALL, 5 )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		bSizer26 = wx.BoxSizer( wx.HORIZONTAL )

		self.txt_menu_username = wx.StaticText( self, wx.ID_ANY, u"Username : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_menu_username.Wrap( -1 )

		self.txt_menu_username.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.txt_menu_username.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.txt_menu_username.SetToolTip( u"Jumlah Koin Anda" )

		bSizer26.Add( self.txt_menu_username, 1, wx.ALL, 5 )

		self.menu_username = wx.StaticText( self, wx.ID_ANY, u"Aku", wx.Point( -1,-1 ), wx.Size( -1,-1 ), 0 )
		self.menu_username.Wrap( -1 )

		self.menu_username.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.menu_username.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )

		bSizer26.Add( self.menu_username, 0, wx.ALL, 5 )


		bSizer3.Add( bSizer26, 1, wx.EXPAND, 5 )

		bSizer261 = wx.BoxSizer( wx.HORIZONTAL )

		self.tx_user_stage = wx.StaticText( self, wx.ID_ANY, u"Stage : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tx_user_stage.Wrap( -1 )

		self.tx_user_stage.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.tx_user_stage.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.tx_user_stage.SetToolTip( u"Jumlah Koin Anda" )

		bSizer261.Add( self.tx_user_stage, 1, wx.ALL, 5 )

		self.menu_stage = wx.StaticText( self, wx.ID_ANY, u"1", wx.Point( -1,-1 ), wx.Size( -1,-1 ), 0 )
		self.menu_stage.Wrap( -1 )

		self.menu_stage.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.menu_stage.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )

		bSizer261.Add( self.menu_stage, 0, wx.ALL, 5 )


		bSizer3.Add( bSizer261, 1, wx.EXPAND, 5 )

		self.fight = wx.Button( self, wx.ID_ANY, u"Fight", wx.DefaultPosition, wx.Size( -1,50 ), 0 )
		self.fight.SetToolTip( u"Fight" )

		bSizer3.Add( self.fight, 0, wx.ALL|wx.EXPAND, 5 )

		self.hero_menu = wx.Button( self, wx.ID_ANY, u"Hero Anda", wx.DefaultPosition, wx.Size( -1,50 ), 0 )
		self.hero_menu.SetToolTip( u"Hero Anda" )

		bSizer3.Add( self.hero_menu, 0, wx.ALL|wx.EXPAND, 5 )

		self.inventory = wx.Button( self, wx.ID_ANY, u"Inventory", wx.DefaultPosition, wx.Size( -1,50 ), 0 )
		self.inventory.SetToolTip( u"Inventory" )

		bSizer3.Add( self.inventory, 0, wx.ALL|wx.EXPAND, 5 )

		self.shop = wx.Button( self, wx.ID_ANY, u"Shop", wx.DefaultPosition, wx.Size( -1,50 ), 0 )
		self.shop.SetToolTip( u"Shop" )

		bSizer3.Add( self.shop, 0, wx.ALL|wx.EXPAND, 5 )

		self.petunjuk = wx.Button( self, wx.ID_ANY, u"Petunjuk Permainan", wx.DefaultPosition, wx.Size( -1,50 ), 0 )
		self.petunjuk.SetToolTip( u"Petunjuk Permainan" )

		bSizer3.Add( self.petunjuk, 0, wx.ALL|wx.EXPAND, 5 )

		self.tentang = wx.Button( self, wx.ID_ANY, u"Tentang Game", wx.DefaultPosition, wx.Size( -1,50 ), 0 )
		self.tentang.SetToolTip( u"Tentang Game" )

		bSizer3.Add( self.tentang, 0, wx.ALL|wx.EXPAND, 5 )

		self.logout = wx.Button( self, wx.ID_ANY, u"Logout", wx.DefaultPosition, wx.Size( -1,50 ), 0 )
		self.logout.SetToolTip( u"Logout" )

		bSizer3.Add( self.logout, 0, wx.ALL|wx.EXPAND, 5 )

		self.exit = wx.Button( self, wx.ID_ANY, u"Exit", wx.DefaultPosition, wx.Size( -1,50 ), 0 )
		self.exit.SetToolTip( u"Exit" )

		bSizer3.Add( self.exit, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer2.Add( bSizer3, 1, wx.EXPAND, 5 )


		bSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )

		self.img_sider1 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"properties/img/sidermenu.bmp", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 200,530 ), 0 )
		bSizer1.Add( self.img_sider1, 0, wx.ALL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.hero_menu.Bind( wx.EVT_BUTTON, self.hero_menuOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def hero_menuOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class f_petunjuk_permainan
###########################################################################

class f_petunjuk_permainan ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Petunjuk Permainan - Burning Heroes", pos = wx.DefaultPosition, size = wx.Size( 630,438 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWFRAME ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		self.SetToolTip( u"Petunjuk Permainan" )

		bSizer1 = wx.BoxSizer( wx.HORIZONTAL )

		self.img_sider = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"properties/img/sider.bmp", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 200,400 ), 0 )
		bSizer1.Add( self.img_sider, 0, wx.ALL, 5 )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.m_bpButton14 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 400,200 ), wx.BU_AUTODRAW|0 )

		self.m_bpButton14.SetBitmap( wx.Bitmap( u"properties/img/BANNER.bmp", wx.BITMAP_TYPE_ANY ) )
		bSizer3.Add( self.m_bpButton14, 0, wx.ALL|wx.EXPAND, 5 )

		self.deskripsi = wx.StaticText( self, wx.ID_ANY, u"Silahkan daftarkan diri anda jika belum mempunyai akun. \nJangan lupa ingat username, hint dan password anda.\nSilahkan Menakan button sesuai kebutuhan Anda. \nBelilah item yang sesuai dengan koin Anda. \n\n\nSelamat Berperang di game!", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.deskripsi.Wrap( -1 )

		self.deskripsi.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.deskripsi.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )

		bSizer3.Add( self.deskripsi, 1, wx.ALL|wx.EXPAND, 5 )

		self.back_home = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.back_home.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_GO_BACK, wx.ART_BUTTON ) )
		bSizer3.Add( self.back_home, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		bSizer2.Add( bSizer3, 1, wx.EXPAND, 5 )


		bSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.back_home.Bind( wx.EVT_BUTTON, self.back_homeOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def back_homeOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class f_hero_menu
###########################################################################

class f_hero_menu ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Hero - Burning Heroes", pos = wx.DefaultPosition, size = wx.Size( 644,533 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 12, 12, 12 ) )

		bSizer24 = wx.BoxSizer( wx.VERTICAL )

		self.m_bpButton65 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton65.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_GO_BACK, wx.ART_BUTTON ) )
		bSizer24.Add( self.m_bpButton65, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )

		bSizer28 = wx.BoxSizer( wx.VERTICAL )

		self.img_superman = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"properties/img/250125/superman_fight.bmp", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 200,100 ), 0 )
		self.img_superman.SetToolTip( u"Meat" )

		bSizer28.Add( self.img_superman, 0, wx.ALL, 5 )

		self.txt_superman = wx.StaticText( self, wx.ID_ANY, u"Superman", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_superman.Wrap( -1 )

		self.txt_superman.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.txt_superman.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		bSizer28.Add( self.txt_superman, 0, wx.ALL, 5 )

		bSizer2611 = wx.BoxSizer( wx.HORIZONTAL )

		self.txt_attack_superman = wx.StaticText( self, wx.ID_ANY, u"Attack : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_attack_superman.Wrap( -1 )

		self.txt_attack_superman.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.txt_attack_superman.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.txt_attack_superman.SetToolTip( u"Jumlah Koin Anda" )

		bSizer2611.Add( self.txt_attack_superman, 1, wx.ALL, 5 )

		self.attack_superman = wx.StaticText( self, wx.ID_ANY, u"20", wx.Point( -1,-1 ), wx.Size( -1,-1 ), 0 )
		self.attack_superman.Wrap( -1 )

		self.attack_superman.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.attack_superman.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		bSizer2611.Add( self.attack_superman, 0, wx.ALL, 5 )


		bSizer28.Add( bSizer2611, 1, wx.EXPAND, 5 )

		bSizer26 = wx.BoxSizer( wx.HORIZONTAL )

		self.txt_hp_superman = wx.StaticText( self, wx.ID_ANY, u"HP : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_hp_superman.Wrap( -1 )

		self.txt_hp_superman.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.txt_hp_superman.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.txt_hp_superman.SetToolTip( u"Jumlah Koin Anda" )

		bSizer26.Add( self.txt_hp_superman, 1, wx.ALL, 5 )

		self.hp_superman = wx.StaticText( self, wx.ID_ANY, u"100", wx.Point( -1,-1 ), wx.Size( -1,-1 ), 0 )
		self.hp_superman.Wrap( -1 )

		self.hp_superman.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.hp_superman.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		bSizer26.Add( self.hp_superman, 0, wx.ALL, 5 )


		bSizer28.Add( bSizer26, 1, wx.EXPAND, 5 )

		bSizer261 = wx.BoxSizer( wx.HORIZONTAL )

		self.txt_max_hp_superman = wx.StaticText( self, wx.ID_ANY, u"Max HP : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_max_hp_superman.Wrap( -1 )

		self.txt_max_hp_superman.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.txt_max_hp_superman.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.txt_max_hp_superman.SetToolTip( u"Jumlah Koin Anda" )

		bSizer261.Add( self.txt_max_hp_superman, 1, wx.ALL, 5 )

		self.max_hp_superman = wx.StaticText( self, wx.ID_ANY, u"100", wx.Point( -1,-1 ), wx.Size( -1,-1 ), 0 )
		self.max_hp_superman.Wrap( -1 )

		self.max_hp_superman.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.max_hp_superman.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		bSizer261.Add( self.max_hp_superman, 0, wx.ALL, 5 )


		bSizer28.Add( bSizer261, 1, wx.EXPAND, 5 )


		gSizer1.Add( bSizer28, 1, wx.EXPAND, 5 )

		bSizer282 = wx.BoxSizer( wx.VERTICAL )

		self.img_batman = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"properties/img/250125/batman_fight.bmp", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 200,100 ), 0 )
		self.img_batman.SetToolTip( u"Meat" )

		bSizer282.Add( self.img_batman, 0, wx.ALL, 5 )

		self.txt_batman = wx.StaticText( self, wx.ID_ANY, u"Batman", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_batman.Wrap( -1 )

		self.txt_batman.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.txt_batman.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )

		bSizer282.Add( self.txt_batman, 0, wx.ALL, 5 )

		bSizer26111 = wx.BoxSizer( wx.HORIZONTAL )

		self.txt_attack_batman = wx.StaticText( self, wx.ID_ANY, u"Attack : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_attack_batman.Wrap( -1 )

		self.txt_attack_batman.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.txt_attack_batman.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.txt_attack_batman.SetToolTip( u"Jumlah Koin Anda" )

		bSizer26111.Add( self.txt_attack_batman, 1, wx.ALL, 5 )

		self.attack_batman = wx.StaticText( self, wx.ID_ANY, u"21", wx.Point( -1,-1 ), wx.Size( -1,-1 ), 0 )
		self.attack_batman.Wrap( -1 )

		self.attack_batman.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.attack_batman.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		bSizer26111.Add( self.attack_batman, 0, wx.ALL, 5 )


		bSizer282.Add( bSizer26111, 1, wx.EXPAND, 5 )

		bSizer262 = wx.BoxSizer( wx.HORIZONTAL )

		self.txt_hp_batman = wx.StaticText( self, wx.ID_ANY, u"HP : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_hp_batman.Wrap( -1 )

		self.txt_hp_batman.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.txt_hp_batman.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.txt_hp_batman.SetToolTip( u"Jumlah Koin Anda" )

		bSizer262.Add( self.txt_hp_batman, 1, wx.ALL, 5 )

		self.hp_batman = wx.StaticText( self, wx.ID_ANY, u"100", wx.Point( -1,-1 ), wx.Size( -1,-1 ), 0 )
		self.hp_batman.Wrap( -1 )

		self.hp_batman.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.hp_batman.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		bSizer262.Add( self.hp_batman, 0, wx.ALL, 5 )


		bSizer282.Add( bSizer262, 1, wx.EXPAND, 5 )

		bSizer2612 = wx.BoxSizer( wx.HORIZONTAL )

		self.txt_max_hp_batman = wx.StaticText( self, wx.ID_ANY, u"Max HP : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_max_hp_batman.Wrap( -1 )

		self.txt_max_hp_batman.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.txt_max_hp_batman.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.txt_max_hp_batman.SetToolTip( u"Jumlah Koin Anda" )

		bSizer2612.Add( self.txt_max_hp_batman, 1, wx.ALL, 5 )

		self.max_hp_batman = wx.StaticText( self, wx.ID_ANY, u"100", wx.Point( -1,-1 ), wx.Size( -1,-1 ), 0 )
		self.max_hp_batman.Wrap( -1 )

		self.max_hp_batman.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.max_hp_batman.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		bSizer2612.Add( self.max_hp_batman, 0, wx.ALL, 5 )


		bSizer282.Add( bSizer2612, 1, wx.EXPAND, 5 )


		gSizer1.Add( bSizer282, 1, wx.EXPAND, 5 )

		bSizer281 = wx.BoxSizer( wx.VERTICAL )

		self.img_wonder_women = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"properties/img/250125/wonderwomen_fight.bmp", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 200,100 ), 0 )
		self.img_wonder_women.SetToolTip( u"Meat" )

		bSizer281.Add( self.img_wonder_women, 0, wx.ALL, 5 )

		self.txt_wonder_women = wx.StaticText( self, wx.ID_ANY, u"Wonder Women", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_wonder_women.Wrap( -1 )

		self.txt_wonder_women.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.txt_wonder_women.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		bSizer281.Add( self.txt_wonder_women, 0, wx.ALL, 5 )

		bSizer26112 = wx.BoxSizer( wx.HORIZONTAL )

		self.txt_attack_wonder_women = wx.StaticText( self, wx.ID_ANY, u"Attack : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_attack_wonder_women.Wrap( -1 )

		self.txt_attack_wonder_women.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.txt_attack_wonder_women.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.txt_attack_wonder_women.SetToolTip( u"Jumlah Koin Anda" )

		bSizer26112.Add( self.txt_attack_wonder_women, 1, wx.ALL, 5 )

		self.attack_wonder_women = wx.StaticText( self, wx.ID_ANY, u"20", wx.Point( -1,-1 ), wx.Size( -1,-1 ), 0 )
		self.attack_wonder_women.Wrap( -1 )

		self.attack_wonder_women.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.attack_wonder_women.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		bSizer26112.Add( self.attack_wonder_women, 0, wx.ALL, 5 )


		bSizer281.Add( bSizer26112, 1, wx.EXPAND, 5 )

		bSizer263 = wx.BoxSizer( wx.HORIZONTAL )

		self.txt_hp_wonder_women = wx.StaticText( self, wx.ID_ANY, u"HP : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_hp_wonder_women.Wrap( -1 )

		self.txt_hp_wonder_women.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.txt_hp_wonder_women.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.txt_hp_wonder_women.SetToolTip( u"Jumlah Koin Anda" )

		bSizer263.Add( self.txt_hp_wonder_women, 1, wx.ALL, 5 )

		self.hp_wonder_women = wx.StaticText( self, wx.ID_ANY, u"100", wx.Point( -1,-1 ), wx.Size( -1,-1 ), 0 )
		self.hp_wonder_women.Wrap( -1 )

		self.hp_wonder_women.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.hp_wonder_women.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		bSizer263.Add( self.hp_wonder_women, 0, wx.ALL, 5 )


		bSizer281.Add( bSizer263, 1, wx.EXPAND, 5 )

		bSizer2613 = wx.BoxSizer( wx.HORIZONTAL )

		self.txt_max_hp_wonder_women = wx.StaticText( self, wx.ID_ANY, u"Max HP : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_max_hp_wonder_women.Wrap( -1 )

		self.txt_max_hp_wonder_women.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.txt_max_hp_wonder_women.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.txt_max_hp_wonder_women.SetToolTip( u"Jumlah Koin Anda" )

		bSizer2613.Add( self.txt_max_hp_wonder_women, 1, wx.ALL, 5 )

		self.max_hp_wonder_women = wx.StaticText( self, wx.ID_ANY, u"100", wx.Point( -1,-1 ), wx.Size( -1,-1 ), 0 )
		self.max_hp_wonder_women.Wrap( -1 )

		self.max_hp_wonder_women.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.max_hp_wonder_women.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		bSizer2613.Add( self.max_hp_wonder_women, 0, wx.ALL, 5 )


		bSizer281.Add( bSizer2613, 1, wx.EXPAND, 5 )


		gSizer1.Add( bSizer281, 1, wx.EXPAND, 5 )

		bSizer283 = wx.BoxSizer( wx.VERTICAL )

		self.img_joker = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"properties/img/250125/joker_fight.bmp", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 200,100 ), 0 )
		self.img_joker.SetToolTip( u"Meat" )

		bSizer283.Add( self.img_joker, 0, wx.ALL, 5 )

		self.txt_joker = wx.StaticText( self, wx.ID_ANY, u"Joker", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_joker.Wrap( -1 )

		self.txt_joker.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.txt_joker.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		bSizer283.Add( self.txt_joker, 0, wx.ALL, 5 )

		bSizer26113 = wx.BoxSizer( wx.HORIZONTAL )

		self.txt_attack_joker = wx.StaticText( self, wx.ID_ANY, u"Attack : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_attack_joker.Wrap( -1 )

		self.txt_attack_joker.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.txt_attack_joker.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.txt_attack_joker.SetToolTip( u"Jumlah Koin Anda" )

		bSizer26113.Add( self.txt_attack_joker, 1, wx.ALL, 5 )

		self.attack_joker = wx.StaticText( self, wx.ID_ANY, u"20", wx.Point( -1,-1 ), wx.Size( -1,-1 ), 0 )
		self.attack_joker.Wrap( -1 )

		self.attack_joker.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.attack_joker.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		bSizer26113.Add( self.attack_joker, 0, wx.ALL, 5 )


		bSizer283.Add( bSizer26113, 1, wx.EXPAND, 5 )

		bSizer264 = wx.BoxSizer( wx.HORIZONTAL )

		self.txt_hp_joker = wx.StaticText( self, wx.ID_ANY, u"HP : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_hp_joker.Wrap( -1 )

		self.txt_hp_joker.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.txt_hp_joker.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.txt_hp_joker.SetToolTip( u"Jumlah Koin Anda" )

		bSizer264.Add( self.txt_hp_joker, 1, wx.ALL, 5 )

		self.hp_joker = wx.StaticText( self, wx.ID_ANY, u"100", wx.Point( -1,-1 ), wx.Size( -1,-1 ), 0 )
		self.hp_joker.Wrap( -1 )

		self.hp_joker.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.hp_joker.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		bSizer264.Add( self.hp_joker, 0, wx.ALL, 5 )


		bSizer283.Add( bSizer264, 1, wx.EXPAND, 5 )

		bSizer2614 = wx.BoxSizer( wx.HORIZONTAL )

		self.txt_max_hp_joker = wx.StaticText( self, wx.ID_ANY, u"Max HP : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_max_hp_joker.Wrap( -1 )

		self.txt_max_hp_joker.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.txt_max_hp_joker.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.txt_max_hp_joker.SetToolTip( u"Jumlah Koin Anda" )

		bSizer2614.Add( self.txt_max_hp_joker, 1, wx.ALL, 5 )

		self.max_hp_joker = wx.StaticText( self, wx.ID_ANY, u"100", wx.Point( -1,-1 ), wx.Size( -1,-1 ), 0 )
		self.max_hp_joker.Wrap( -1 )

		self.max_hp_joker.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.max_hp_joker.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		bSizer2614.Add( self.max_hp_joker, 0, wx.ALL, 5 )


		bSizer283.Add( bSizer2614, 1, wx.EXPAND, 5 )


		gSizer1.Add( bSizer283, 1, wx.EXPAND, 5 )


		bSizer24.Add( gSizer1, 1, wx.EXPAND, 10 )


		self.SetSizer( bSizer24 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class f_inventory
###########################################################################

class f_inventory ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Inventory - Burning Heroes", pos = wx.DefaultPosition, size = wx.Size( 645,529 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		bSizer24 = wx.BoxSizer( wx.VERTICAL )

		bSizer26 = wx.BoxSizer( wx.HORIZONTAL )

		self.back_home = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.back_home.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_GO_BACK, wx.ART_BUTTON ) )
		bSizer26.Add( self.back_home, 0, wx.ALL, 5 )

		self.txt_jumlah_koin = wx.StaticText( self, wx.ID_ANY, u"Koin Anda : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_jumlah_koin.Wrap( -1 )

		self.txt_jumlah_koin.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.txt_jumlah_koin.SetToolTip( u"Jumlah Koin Anda" )

		bSizer26.Add( self.txt_jumlah_koin, 1, wx.ALIGN_CENTER_VERTICAL, 5 )

		self.jumlah_koin = wx.StaticText( self, wx.ID_ANY, u"9999", wx.Point( -1,-1 ), wx.Size( -1,-1 ), 0 )
		self.jumlah_koin.Wrap( -1 )

		self.jumlah_koin.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer26.Add( self.jumlah_koin, 0, wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer24.Add( bSizer26, 0, 0, 5 )

		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )

		bSizer28 = wx.BoxSizer( wx.VERTICAL )

		self.img_meat = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"properties/img/item/meat.bmp", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 200,100 ), 0 )
		self.img_meat.SetToolTip( u"Meat" )

		bSizer28.Add( self.img_meat, 0, wx.ALL, 5 )

		self.meat_name = wx.StaticText( self, wx.ID_ANY, u"Meat", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.meat_name.Wrap( -1 )

		self.meat_name.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer28.Add( self.meat_name, 0, wx.ALL, 5 )

		self.desc_meat = wx.StaticText( self, wx.ID_ANY, u"Meat menambahkan HP hero terpilih sebanyak 50 HP", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.desc_meat.Wrap( -1 )

		bSizer28.Add( self.desc_meat, 0, wx.ALL, 5 )

		bSizerJumlah = wx.BoxSizer( wx.HORIZONTAL )

		self.txt_jumlah_meat = wx.StaticText( self, wx.ID_ANY, u"Jumlah : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_jumlah_meat.Wrap( -1 )

		self.txt_jumlah_meat.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.txt_jumlah_meat.SetToolTip( u"Jumlah Koin Anda" )

		bSizerJumlah.Add( self.txt_jumlah_meat, 1, wx.ALL, 5 )

		self.jumlah_meat = wx.StaticText( self, wx.ID_ANY, u"1", wx.Point( -1,-1 ), wx.Size( -1,-1 ), 0 )
		self.jumlah_meat.Wrap( -1 )

		self.jumlah_meat.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizerJumlah.Add( self.jumlah_meat, 0, wx.ALL, 5 )


		bSizer28.Add( bSizerJumlah, 1, 0, 5 )


		gSizer1.Add( bSizer28, 1, 0, 5 )

		bSizer281 = wx.BoxSizer( wx.VERTICAL )

		self.img_potion = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"properties/img/item/potion.bmp", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 200,100 ), 0 )
		self.img_potion.SetToolTip( u"Potion" )

		bSizer281.Add( self.img_potion, 0, wx.ALL, 5 )

		self.potion_name = wx.StaticText( self, wx.ID_ANY, u"Potion", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.potion_name.Wrap( -1 )

		self.potion_name.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.potion_name.SetToolTip( u"Potion" )

		bSizer281.Add( self.potion_name, 0, wx.ALL, 5 )

		self.desc_potion = wx.StaticText( self, wx.ID_ANY, u"Potion memberikan efek damage tambahan 20% - 30%", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.desc_potion.Wrap( -1 )

		bSizer281.Add( self.desc_potion, 0, wx.ALL, 5 )

		bSizerJumlah1 = wx.BoxSizer( wx.HORIZONTAL )

		self.txt_jumlah_potion = wx.StaticText( self, wx.ID_ANY, u"Jumlah : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_jumlah_potion.Wrap( -1 )

		self.txt_jumlah_potion.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.txt_jumlah_potion.SetToolTip( u"Jumlah Koin Anda" )

		bSizerJumlah1.Add( self.txt_jumlah_potion, 1, wx.ALL, 5 )

		self.jumlah_potion = wx.StaticText( self, wx.ID_ANY, u"1", wx.Point( -1,-1 ), wx.Size( -1,-1 ), 0 )
		self.jumlah_potion.Wrap( -1 )

		self.jumlah_potion.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizerJumlah1.Add( self.jumlah_potion, 0, wx.ALL, 5 )


		bSizer281.Add( bSizerJumlah1, 1, 0, 5 )


		gSizer1.Add( bSizer281, 1, 0, 5 )

		bSizer2811 = wx.BoxSizer( wx.VERTICAL )

		self.img_potion1 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"properties/img/item/sharpener.bmp", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 200,100 ), 0 )
		self.img_potion1.SetToolTip( u"Potion" )

		bSizer2811.Add( self.img_potion1, 0, 0, 5 )

		self.sharpener_name = wx.StaticText( self, wx.ID_ANY, u"Sharpener", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.sharpener_name.Wrap( -1 )

		self.sharpener_name.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.sharpener_name.SetToolTip( u"Sharpener" )

		bSizer2811.Add( self.sharpener_name, 0, wx.ALL, 5 )

		self.desc_sharpener = wx.StaticText( self, wx.ID_ANY, u"Sharpener menambahkan 20 attack tambahan ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.desc_sharpener.Wrap( -1 )

		bSizer2811.Add( self.desc_sharpener, 0, wx.ALL, 5 )

		bSizerJumlah11 = wx.BoxSizer( wx.HORIZONTAL )

		self.txt_jumlah_sharpener = wx.StaticText( self, wx.ID_ANY, u"Jumlah : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_jumlah_sharpener.Wrap( -1 )

		self.txt_jumlah_sharpener.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.txt_jumlah_sharpener.SetToolTip( u"Jumlah Koin Anda" )

		bSizerJumlah11.Add( self.txt_jumlah_sharpener, 1, wx.ALL, 5 )

		self.jumlah_sharpener = wx.StaticText( self, wx.ID_ANY, u"1", wx.Point( -1,-1 ), wx.Size( -1,-1 ), 0 )
		self.jumlah_sharpener.Wrap( -1 )

		self.jumlah_sharpener.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizerJumlah11.Add( self.jumlah_sharpener, 0, wx.ALL, 5 )


		bSizer2811.Add( bSizerJumlah11, 1, 0, 5 )


		gSizer1.Add( bSizer2811, 1, 0, 5 )

		bSizer2812 = wx.BoxSizer( wx.VERTICAL )

		self.img_giant_potion = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"properties/img/item/giant_potion.bmp", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 200,100 ), 0 )
		self.img_giant_potion.SetToolTip( u"Giant Potion" )

		bSizer2812.Add( self.img_giant_potion, 0, wx.ALL, 5 )

		self.giant_potion_name = wx.StaticText( self, wx.ID_ANY, u"Giant Potion", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.giant_potion_name.Wrap( -1 )

		self.giant_potion_name.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer2812.Add( self.giant_potion_name, 0, wx.ALL, 5 )

		self.desc_giant_potion = wx.StaticText( self, wx.ID_ANY, u"Giant Potion menambahkan Hp sebanyak 30% - 40%", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.desc_giant_potion.Wrap( -1 )

		bSizer2812.Add( self.desc_giant_potion, 0, wx.ALL, 5 )

		bSizerJumlah111 = wx.BoxSizer( wx.HORIZONTAL )

		self.txt_jumlah_giant_potion = wx.StaticText( self, wx.ID_ANY, u"Jumlah : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_jumlah_giant_potion.Wrap( -1 )

		self.txt_jumlah_giant_potion.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.txt_jumlah_giant_potion.SetToolTip( u"Jumlah Koin Anda" )

		bSizerJumlah111.Add( self.txt_jumlah_giant_potion, 1, wx.ALL, 5 )

		self.jumlah_giant_potion = wx.StaticText( self, wx.ID_ANY, u"1", wx.Point( -1,-1 ), wx.Size( -1,-1 ), 0 )
		self.jumlah_giant_potion.Wrap( -1 )

		self.jumlah_giant_potion.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizerJumlah111.Add( self.jumlah_giant_potion, 0, wx.ALL, 5 )


		bSizer2812.Add( bSizerJumlah111, 1, 0, 5 )


		gSizer1.Add( bSizer2812, 1, 0, 5 )


		bSizer24.Add( gSizer1, 1, 0, 5 )


		self.SetSizer( bSizer24 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.back_home.Bind( wx.EVT_BUTTON, self.back_homeOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def back_homeOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class f_fight
###########################################################################

class f_fight ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Fight - Burning Heroes", pos = wx.DefaultPosition, size = wx.Size( 803,562 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )

		bSizer126 = wx.BoxSizer( wx.HORIZONTAL )

		bSizerUserSide = wx.BoxSizer( wx.VERTICAL )

		bSizerHero1 = wx.BoxSizer( wx.VERTICAL )

		self.m_bpButton38 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 250,125 ), wx.BU_AUTODRAW|0 )

		self.m_bpButton38.SetBitmap( wx.Bitmap( u"properties/img/250125/batman_fight.bmp", wx.BITMAP_TYPE_ANY ) )
		bSizerHero1.Add( self.m_bpButton38, 0, wx.ALL, 5 )

		bSizer2611 = wx.BoxSizer( wx.HORIZONTAL )

		self.txt_attack_hero_user1 = wx.StaticText( self, wx.ID_ANY, u"Attack : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_attack_hero_user1.Wrap( -1 )

		self.txt_attack_hero_user1.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.txt_attack_hero_user1.SetToolTip( u"Jumlah Koin Anda" )

		bSizer2611.Add( self.txt_attack_hero_user1, 1, wx.ALL, 5 )

		self.attack_hero_user1 = wx.StaticText( self, wx.ID_ANY, u"20", wx.Point( -1,-1 ), wx.Size( -1,-1 ), 0 )
		self.attack_hero_user1.Wrap( -1 )

		self.attack_hero_user1.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer2611.Add( self.attack_hero_user1, 0, wx.ALL, 5 )


		bSizerHero1.Add( bSizer2611, 1, wx.EXPAND, 5 )

		bSizer26111 = wx.BoxSizer( wx.HORIZONTAL )

		self.txt_hp_hero_user1 = wx.StaticText( self, wx.ID_ANY, u"HP : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_hp_hero_user1.Wrap( -1 )

		self.txt_hp_hero_user1.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.txt_hp_hero_user1.SetToolTip( u"Jumlah Koin Anda" )

		bSizer26111.Add( self.txt_hp_hero_user1, 1, wx.ALL, 5 )

		self.hp_hero_user1 = wx.StaticText( self, wx.ID_ANY, u"20", wx.Point( -1,-1 ), wx.Size( -1,-1 ), 0 )
		self.hp_hero_user1.Wrap( -1 )

		self.hp_hero_user1.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer26111.Add( self.hp_hero_user1, 0, wx.ALL, 5 )


		bSizerHero1.Add( bSizer26111, 1, wx.EXPAND, 5 )

		bSizer26112 = wx.BoxSizer( wx.HORIZONTAL )

		self.txt_max_hp_hero_user1 = wx.StaticText( self, wx.ID_ANY, u"Max HP :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_max_hp_hero_user1.Wrap( -1 )

		self.txt_max_hp_hero_user1.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.txt_max_hp_hero_user1.SetToolTip( u"Jumlah Koin Anda" )

		bSizer26112.Add( self.txt_max_hp_hero_user1, 1, wx.ALL, 5 )

		self.max_hp_hero_user1 = wx.StaticText( self, wx.ID_ANY, u"20", wx.Point( -1,-1 ), wx.Size( -1,-1 ), 0 )
		self.max_hp_hero_user1.Wrap( -1 )

		self.max_hp_hero_user1.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer26112.Add( self.max_hp_hero_user1, 0, wx.ALL, 5 )


		bSizerHero1.Add( bSizer26112, 1, wx.EXPAND, 5 )

		bSizer26115 = wx.BoxSizer( wx.HORIZONTAL )

		self.txt_dipakai_hero1 = wx.StaticText( self, wx.ID_ANY, u"Dipakai : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_dipakai_hero1.Wrap( -1 )

		self.txt_dipakai_hero1.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.txt_dipakai_hero1.SetToolTip( u"Jumlah Koin Anda" )

		bSizer26115.Add( self.txt_dipakai_hero1, 1, wx.ALL, 5 )

		self.dipakai_hero1 = wx.StaticText( self, wx.ID_ANY, u"Ya", wx.Point( -1,-1 ), wx.Size( -1,-1 ), 0 )
		self.dipakai_hero1.Wrap( -1 )

		self.dipakai_hero1.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer26115.Add( self.dipakai_hero1, 0, wx.ALL, 5 )


		bSizerHero1.Add( bSizer26115, 1, wx.EXPAND, 5 )


		bSizerUserSide.Add( bSizerHero1, 1, wx.EXPAND, 5 )

		bSizerHero2 = wx.BoxSizer( wx.VERTICAL )

		self.m_bpButton383 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 250,125 ), wx.BU_AUTODRAW|0 )

		self.m_bpButton383.SetBitmap( wx.Bitmap( u"properties/img/250125/wonderwomen_fight.bmp", wx.BITMAP_TYPE_ANY ) )
		bSizerHero2.Add( self.m_bpButton383, 0, wx.ALL, 5 )

		bSizer26113 = wx.BoxSizer( wx.HORIZONTAL )

		self.txt_attack_hero_user2 = wx.StaticText( self, wx.ID_ANY, u"Attack : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_attack_hero_user2.Wrap( -1 )

		self.txt_attack_hero_user2.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.txt_attack_hero_user2.SetToolTip( u"Jumlah Koin Anda" )

		bSizer26113.Add( self.txt_attack_hero_user2, 1, wx.ALL, 5 )

		self.attack_hero_user2 = wx.StaticText( self, wx.ID_ANY, u"20", wx.Point( -1,-1 ), wx.Size( -1,-1 ), 0 )
		self.attack_hero_user2.Wrap( -1 )

		self.attack_hero_user2.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer26113.Add( self.attack_hero_user2, 0, wx.ALL, 5 )


		bSizerHero2.Add( bSizer26113, 1, wx.EXPAND, 5 )

		bSizer261111 = wx.BoxSizer( wx.HORIZONTAL )

		self.txt_hp_hero_user2 = wx.StaticText( self, wx.ID_ANY, u"HP : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_hp_hero_user2.Wrap( -1 )

		self.txt_hp_hero_user2.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.txt_hp_hero_user2.SetToolTip( u"Jumlah Koin Anda" )

		bSizer261111.Add( self.txt_hp_hero_user2, 1, wx.ALL, 5 )

		self.hp_hero_user2 = wx.StaticText( self, wx.ID_ANY, u"20", wx.Point( -1,-1 ), wx.Size( -1,-1 ), 0 )
		self.hp_hero_user2.Wrap( -1 )

		self.hp_hero_user2.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer261111.Add( self.hp_hero_user2, 0, wx.ALL, 5 )


		bSizerHero2.Add( bSizer261111, 1, wx.EXPAND, 5 )

		bSizer261121 = wx.BoxSizer( wx.HORIZONTAL )

		self.txt_max_hp_hero_user2 = wx.StaticText( self, wx.ID_ANY, u"Max HP :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_max_hp_hero_user2.Wrap( -1 )

		self.txt_max_hp_hero_user2.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.txt_max_hp_hero_user2.SetToolTip( u"Jumlah Koin Anda" )

		bSizer261121.Add( self.txt_max_hp_hero_user2, 1, wx.ALL, 5 )

		self.max_hp_hero_user2 = wx.StaticText( self, wx.ID_ANY, u"20", wx.Point( -1,-1 ), wx.Size( -1,-1 ), 0 )
		self.max_hp_hero_user2.Wrap( -1 )

		self.max_hp_hero_user2.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer261121.Add( self.max_hp_hero_user2, 0, wx.ALL, 5 )


		bSizerHero2.Add( bSizer261121, 1, wx.EXPAND, 5 )

		bSizer261151 = wx.BoxSizer( wx.HORIZONTAL )

		self.txt_dipakai_hero2 = wx.StaticText( self, wx.ID_ANY, u"Dipakai : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_dipakai_hero2.Wrap( -1 )

		self.txt_dipakai_hero2.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.txt_dipakai_hero2.SetToolTip( u"Jumlah Koin Anda" )

		bSizer261151.Add( self.txt_dipakai_hero2, 1, wx.ALL, 5 )

		self.dipakai_hero2 = wx.StaticText( self, wx.ID_ANY, u"Tidak", wx.Point( -1,-1 ), wx.Size( -1,-1 ), 0 )
		self.dipakai_hero2.Wrap( -1 )

		self.dipakai_hero2.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer261151.Add( self.dipakai_hero2, 0, wx.ALL, 5 )


		bSizerHero2.Add( bSizer261151, 1, wx.EXPAND, 5 )


		bSizerUserSide.Add( bSizerHero2, 1, wx.EXPAND, 5 )


		bSizer126.Add( bSizerUserSide, 1, wx.EXPAND, 5 )

		bSizerTengah = wx.BoxSizer( wx.VERTICAL )

		bSizer234 = wx.BoxSizer( wx.VERTICAL )

		self.keterangan_perang = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer234.Add( self.keterangan_perang, 1, wx.ALL|wx.EXPAND, 5 )


		bSizerTengah.Add( bSizer234, 1, wx.EXPAND, 5 )

		bSizer247 = wx.BoxSizer( wx.VERTICAL )

		bSizer261163 = wx.BoxSizer( wx.HORIZONTAL )

		self.txt_potion = wx.StaticText( self, wx.ID_ANY, u"Potion :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_potion.Wrap( -1 )

		self.txt_potion.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.txt_potion.SetToolTip( u"Jumlah Koin Anda" )

		bSizer261163.Add( self.txt_potion, 1, wx.ALL, 5 )

		self.jumlah_meat3 = wx.StaticText( self, wx.ID_ANY, u"1", wx.Point( -1,-1 ), wx.Size( -1,-1 ), 0 )
		self.jumlah_meat3.Wrap( -1 )

		self.jumlah_meat3.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer261163.Add( self.jumlah_meat3, 0, wx.ALL, 5 )

		self.btn_pakai_potion = wx.Button( self, wx.ID_ANY, u"Pakai", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer261163.Add( self.btn_pakai_potion, 0, wx.ALL, 5 )


		bSizer247.Add( bSizer261163, 1, wx.EXPAND, 5 )

		bSizer261162 = wx.BoxSizer( wx.HORIZONTAL )

		self.txt_sharpener = wx.StaticText( self, wx.ID_ANY, u"Sharpener :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_sharpener.Wrap( -1 )

		self.txt_sharpener.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.txt_sharpener.SetToolTip( u"Jumlah Koin Anda" )

		bSizer261162.Add( self.txt_sharpener, 1, wx.ALL, 5 )

		self.jumlah_sharpener = wx.StaticText( self, wx.ID_ANY, u"1", wx.Point( -1,-1 ), wx.Size( -1,-1 ), 0 )
		self.jumlah_sharpener.Wrap( -1 )

		self.jumlah_sharpener.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer261162.Add( self.jumlah_sharpener, 0, wx.ALL, 5 )

		self.btn_pakai_sharpener = wx.Button( self, wx.ID_ANY, u"Pakai", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer261162.Add( self.btn_pakai_sharpener, 0, wx.ALL, 5 )


		bSizer247.Add( bSizer261162, 1, wx.EXPAND, 5 )

		bSizer261161 = wx.BoxSizer( wx.HORIZONTAL )

		self.txt_giant_potion = wx.StaticText( self, wx.ID_ANY, u"Giant Potion :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_giant_potion.Wrap( -1 )

		self.txt_giant_potion.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.txt_giant_potion.SetToolTip( u"Jumlah Koin Anda" )

		bSizer261161.Add( self.txt_giant_potion, 1, wx.ALL, 5 )

		self.jumlah_giant_potion = wx.StaticText( self, wx.ID_ANY, u"1", wx.Point( -1,-1 ), wx.Size( -1,-1 ), 0 )
		self.jumlah_giant_potion.Wrap( -1 )

		self.jumlah_giant_potion.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer261161.Add( self.jumlah_giant_potion, 0, wx.ALL, 5 )

		self.btn_pakai_giant_potion = wx.Button( self, wx.ID_ANY, u"Pakai", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer261161.Add( self.btn_pakai_giant_potion, 0, wx.ALL, 5 )


		bSizer247.Add( bSizer261161, 1, wx.EXPAND, 5 )

		bSizer26116 = wx.BoxSizer( wx.HORIZONTAL )

		self.txt_meat = wx.StaticText( self, wx.ID_ANY, u"Meat :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_meat.Wrap( -1 )

		self.txt_meat.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.txt_meat.SetToolTip( u"Jumlah Koin Anda" )

		bSizer26116.Add( self.txt_meat, 1, wx.ALL, 5 )

		self.jumlah_meat = wx.StaticText( self, wx.ID_ANY, u"1", wx.Point( -1,-1 ), wx.Size( -1,-1 ), 0 )
		self.jumlah_meat.Wrap( -1 )

		self.jumlah_meat.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer26116.Add( self.jumlah_meat, 0, wx.ALL, 5 )

		self.btn_pakai_meat = wx.Button( self, wx.ID_ANY, u"Pakai", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer26116.Add( self.btn_pakai_meat, 0, wx.ALL, 5 )


		bSizer247.Add( bSizer26116, 1, wx.EXPAND, 5 )

		self.btn_ganti_hero = wx.Button( self, wx.ID_ANY, u"Ganti Hero", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer247.Add( self.btn_ganti_hero, 0, wx.ALL|wx.EXPAND, 5 )

		self.btn_serang = wx.Button( self, wx.ID_ANY, u"Serang", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer247.Add( self.btn_serang, 0, wx.ALL|wx.EXPAND, 5 )


		bSizerTengah.Add( bSizer247, 1, wx.EXPAND, 5 )


		bSizer126.Add( bSizerTengah, 1, wx.EXPAND, 5 )

		bSizerEnemySide = wx.BoxSizer( wx.VERTICAL )

		bSizerHeroMusuh1 = wx.BoxSizer( wx.VERTICAL )

		self.m_bpButton384 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 250,125 ), wx.BU_AUTODRAW|0 )

		self.m_bpButton384.SetBitmap( wx.Bitmap( u"properties/img/250125/joker_fight.bmp", wx.BITMAP_TYPE_ANY ) )
		bSizerHeroMusuh1.Add( self.m_bpButton384, 0, wx.ALL, 5 )

		bSizer26117 = wx.BoxSizer( wx.HORIZONTAL )

		self.txt_attack_hero_musuh1 = wx.StaticText( self, wx.ID_ANY, u"Attack : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_attack_hero_musuh1.Wrap( -1 )

		self.txt_attack_hero_musuh1.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.txt_attack_hero_musuh1.SetToolTip( u"Jumlah Koin Anda" )

		bSizer26117.Add( self.txt_attack_hero_musuh1, 1, wx.ALL, 5 )

		self.attack_hero_musuh1 = wx.StaticText( self, wx.ID_ANY, u"20", wx.Point( -1,-1 ), wx.Size( -1,-1 ), 0 )
		self.attack_hero_musuh1.Wrap( -1 )

		self.attack_hero_musuh1.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer26117.Add( self.attack_hero_musuh1, 0, wx.ALL, 5 )


		bSizerHeroMusuh1.Add( bSizer26117, 1, wx.EXPAND, 5 )

		bSizer261114 = wx.BoxSizer( wx.HORIZONTAL )

		self.txt_hp_hero_musuh1 = wx.StaticText( self, wx.ID_ANY, u"HP : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_hp_hero_musuh1.Wrap( -1 )

		self.txt_hp_hero_musuh1.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.txt_hp_hero_musuh1.SetToolTip( u"Jumlah Koin Anda" )

		bSizer261114.Add( self.txt_hp_hero_musuh1, 1, wx.ALL, 5 )

		self.hp_hero_musuh1 = wx.StaticText( self, wx.ID_ANY, u"20", wx.Point( -1,-1 ), wx.Size( -1,-1 ), 0 )
		self.hp_hero_musuh1.Wrap( -1 )

		self.hp_hero_musuh1.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer261114.Add( self.hp_hero_musuh1, 0, wx.ALL, 5 )


		bSizerHeroMusuh1.Add( bSizer261114, 1, wx.EXPAND, 5 )

		bSizer261124 = wx.BoxSizer( wx.HORIZONTAL )

		self.txt_max_hp_hero_musuh1 = wx.StaticText( self, wx.ID_ANY, u"Max HP :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_max_hp_hero_musuh1.Wrap( -1 )

		self.txt_max_hp_hero_musuh1.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.txt_max_hp_hero_musuh1.SetToolTip( u"Jumlah Koin Anda" )

		bSizer261124.Add( self.txt_max_hp_hero_musuh1, 1, wx.ALL, 5 )

		self.max_hp_hero_musuh1 = wx.StaticText( self, wx.ID_ANY, u"20", wx.Point( -1,-1 ), wx.Size( -1,-1 ), 0 )
		self.max_hp_hero_musuh1.Wrap( -1 )

		self.max_hp_hero_musuh1.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer261124.Add( self.max_hp_hero_musuh1, 0, wx.ALL, 5 )


		bSizerHeroMusuh1.Add( bSizer261124, 1, wx.EXPAND, 5 )

		bSizer261152 = wx.BoxSizer( wx.HORIZONTAL )

		self.txt_dipakai_hero_musuh1 = wx.StaticText( self, wx.ID_ANY, u"Dipakai : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_dipakai_hero_musuh1.Wrap( -1 )

		self.txt_dipakai_hero_musuh1.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.txt_dipakai_hero_musuh1.SetToolTip( u"Jumlah Koin Anda" )

		bSizer261152.Add( self.txt_dipakai_hero_musuh1, 1, wx.ALL, 5 )

		self.dipakai_hero_musuh1 = wx.StaticText( self, wx.ID_ANY, u"Ya", wx.Point( -1,-1 ), wx.Size( -1,-1 ), 0 )
		self.dipakai_hero_musuh1.Wrap( -1 )

		self.dipakai_hero_musuh1.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer261152.Add( self.dipakai_hero_musuh1, 0, wx.ALL, 5 )


		bSizerHeroMusuh1.Add( bSizer261152, 1, wx.EXPAND, 5 )


		bSizerEnemySide.Add( bSizerHeroMusuh1, 1, wx.EXPAND, 5 )

		bSizerHeroMusuh2 = wx.BoxSizer( wx.VERTICAL )

		self.m_bpButton381 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 250,125 ), wx.BU_AUTODRAW|0 )

		self.m_bpButton381.SetBitmap( wx.Bitmap( u"properties/img/250125/superman_fight.bmp", wx.BITMAP_TYPE_ANY ) )
		bSizerHeroMusuh2.Add( self.m_bpButton381, 0, wx.ALL, 5 )

		bSizer26114 = wx.BoxSizer( wx.HORIZONTAL )

		self.txt_attack_hero_musuh2 = wx.StaticText( self, wx.ID_ANY, u"Attack : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_attack_hero_musuh2.Wrap( -1 )

		self.txt_attack_hero_musuh2.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.txt_attack_hero_musuh2.SetToolTip( u"Jumlah Koin Anda" )

		bSizer26114.Add( self.txt_attack_hero_musuh2, 1, wx.ALL, 5 )

		self.attack_hero_musuh2 = wx.StaticText( self, wx.ID_ANY, u"20", wx.Point( -1,-1 ), wx.Size( -1,-1 ), 0 )
		self.attack_hero_musuh2.Wrap( -1 )

		self.attack_hero_musuh2.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer26114.Add( self.attack_hero_musuh2, 0, wx.ALL, 5 )


		bSizerHeroMusuh2.Add( bSizer26114, 1, wx.EXPAND, 5 )

		bSizer261112 = wx.BoxSizer( wx.HORIZONTAL )

		self.txt_hp_hero_musuh2 = wx.StaticText( self, wx.ID_ANY, u"HP : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_hp_hero_musuh2.Wrap( -1 )

		self.txt_hp_hero_musuh2.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.txt_hp_hero_musuh2.SetToolTip( u"Jumlah Koin Anda" )

		bSizer261112.Add( self.txt_hp_hero_musuh2, 1, wx.ALL, 5 )

		self.hp_hero_musuh2 = wx.StaticText( self, wx.ID_ANY, u"20", wx.Point( -1,-1 ), wx.Size( -1,-1 ), 0 )
		self.hp_hero_musuh2.Wrap( -1 )

		self.hp_hero_musuh2.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer261112.Add( self.hp_hero_musuh2, 0, wx.ALL, 5 )


		bSizerHeroMusuh2.Add( bSizer261112, 1, wx.EXPAND, 5 )

		bSizer261122 = wx.BoxSizer( wx.HORIZONTAL )

		self.txt_max_hp_hero_musuh2 = wx.StaticText( self, wx.ID_ANY, u"Max HP :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_max_hp_hero_musuh2.Wrap( -1 )

		self.txt_max_hp_hero_musuh2.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.txt_max_hp_hero_musuh2.SetToolTip( u"Jumlah Koin Anda" )

		bSizer261122.Add( self.txt_max_hp_hero_musuh2, 1, wx.ALL, 5 )

		self.max_hp_hero_musuh2 = wx.StaticText( self, wx.ID_ANY, u"20", wx.Point( -1,-1 ), wx.Size( -1,-1 ), 0 )
		self.max_hp_hero_musuh2.Wrap( -1 )

		self.max_hp_hero_musuh2.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer261122.Add( self.max_hp_hero_musuh2, 0, wx.ALL, 5 )


		bSizerHeroMusuh2.Add( bSizer261122, 1, wx.EXPAND, 5 )

		bSizer2611521 = wx.BoxSizer( wx.HORIZONTAL )

		self.txt_dipakai_hero_musuh2 = wx.StaticText( self, wx.ID_ANY, u"Dipakai : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_dipakai_hero_musuh2.Wrap( -1 )

		self.txt_dipakai_hero_musuh2.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.txt_dipakai_hero_musuh2.SetToolTip( u"Jumlah Koin Anda" )

		bSizer2611521.Add( self.txt_dipakai_hero_musuh2, 1, wx.ALL, 5 )

		self.dipakai_hero_musuh2 = wx.StaticText( self, wx.ID_ANY, u"Tidak", wx.Point( -1,-1 ), wx.Size( -1,-1 ), 0 )
		self.dipakai_hero_musuh2.Wrap( -1 )

		self.dipakai_hero_musuh2.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer2611521.Add( self.dipakai_hero_musuh2, 0, wx.ALL, 5 )


		bSizerHeroMusuh2.Add( bSizer2611521, 1, wx.EXPAND, 5 )


		bSizerEnemySide.Add( bSizerHeroMusuh2, 1, wx.EXPAND, 5 )


		bSizer126.Add( bSizerEnemySide, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer126 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class f_pilih_hero_fight
###########################################################################

class f_pilih_hero_fight ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Pilih Hero - Fight", pos = wx.DefaultPosition, size = wx.Size( 854,535 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 19, 19, 19 ) )

		bSizer164 = wx.BoxSizer( wx.VERTICAL )

		self.m_bpButton66 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton66.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_GO_BACK, wx.ART_BUTTON ) )
		bSizer164.Add( self.m_bpButton66, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		bSizer202 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer1653 = wx.BoxSizer( wx.VERTICAL )

		self.m_bpButton463 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 200,300 ), wx.BU_AUTODRAW|0 )

		self.m_bpButton463.SetBitmap( wx.Bitmap( u"properties/img/23/batman23.bmp", wx.BITMAP_TYPE_ANY ) )
		bSizer1653.Add( self.m_bpButton463, 0, wx.ALL, 5 )

		bSizer26115 = wx.BoxSizer( wx.HORIZONTAL )

		self.txt_attack_superman3 = wx.StaticText( self, wx.ID_ANY, u"Attack : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_attack_superman3.Wrap( -1 )

		self.txt_attack_superman3.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.txt_attack_superman3.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )
		self.txt_attack_superman3.SetToolTip( u"Jumlah Koin Anda" )

		bSizer26115.Add( self.txt_attack_superman3, 1, wx.ALL, 5 )

		self.attack_superman4 = wx.StaticText( self, wx.ID_ANY, u"20", wx.Point( -1,-1 ), wx.Size( -1,-1 ), 0 )
		self.attack_superman4.Wrap( -1 )

		self.attack_superman4.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.attack_superman4.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		bSizer26115.Add( self.attack_superman4, 0, wx.ALL, 5 )


		bSizer1653.Add( bSizer26115, 1, wx.EXPAND, 5 )

		bSizer261113 = wx.BoxSizer( wx.HORIZONTAL )

		self.txt_hp_superman3 = wx.StaticText( self, wx.ID_ANY, u"HP : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_hp_superman3.Wrap( -1 )

		self.txt_hp_superman3.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.txt_hp_superman3.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.txt_hp_superman3.SetToolTip( u"Jumlah Koin Anda" )

		bSizer261113.Add( self.txt_hp_superman3, 1, wx.ALL, 5 )

		self.HP_superman3 = wx.StaticText( self, wx.ID_ANY, u"20", wx.Point( -1,-1 ), wx.Size( -1,-1 ), 0 )
		self.HP_superman3.Wrap( -1 )

		self.HP_superman3.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.HP_superman3.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		bSizer261113.Add( self.HP_superman3, 0, wx.ALL, 5 )


		bSizer1653.Add( bSizer261113, 1, wx.EXPAND, 5 )

		bSizer261123 = wx.BoxSizer( wx.HORIZONTAL )

		self.txt_max_hp_superman3 = wx.StaticText( self, wx.ID_ANY, u"Max HP : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_max_hp_superman3.Wrap( -1 )

		self.txt_max_hp_superman3.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.txt_max_hp_superman3.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )
		self.txt_max_hp_superman3.SetToolTip( u"Jumlah Koin Anda" )

		bSizer261123.Add( self.txt_max_hp_superman3, 1, wx.ALL, 5 )

		self.attack_superman23 = wx.StaticText( self, wx.ID_ANY, u"20", wx.Point( -1,-1 ), wx.Size( -1,-1 ), 0 )
		self.attack_superman23.Wrap( -1 )

		self.attack_superman23.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.attack_superman23.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )

		bSizer261123.Add( self.attack_superman23, 0, wx.ALL, 5 )


		bSizer1653.Add( bSizer261123, 1, wx.EXPAND, 5 )

		self.cb_hero_batman = wx.CheckBox( self, wx.ID_ANY, u"Pilih", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cb_hero_batman.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		bSizer1653.Add( self.cb_hero_batman, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer202.Add( bSizer1653, 1, wx.EXPAND, 5 )

		bSizer1652 = wx.BoxSizer( wx.VERTICAL )

		self.m_bpButton462 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 200,300 ), wx.BU_AUTODRAW|0 )

		self.m_bpButton462.SetBitmap( wx.Bitmap( u"properties/img/23/joker23.bmp", wx.BITMAP_TYPE_ANY ) )
		bSizer1652.Add( self.m_bpButton462, 0, wx.ALL, 5 )

		bSizer26114 = wx.BoxSizer( wx.HORIZONTAL )

		self.txt_attack_superman2 = wx.StaticText( self, wx.ID_ANY, u"Attack : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_attack_superman2.Wrap( -1 )

		self.txt_attack_superman2.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.txt_attack_superman2.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.txt_attack_superman2.SetToolTip( u"Jumlah Koin Anda" )

		bSizer26114.Add( self.txt_attack_superman2, 1, wx.ALL, 5 )

		self.attack_superman3 = wx.StaticText( self, wx.ID_ANY, u"20", wx.Point( -1,-1 ), wx.Size( -1,-1 ), 0 )
		self.attack_superman3.Wrap( -1 )

		self.attack_superman3.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.attack_superman3.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		bSizer26114.Add( self.attack_superman3, 0, wx.ALL, 5 )


		bSizer1652.Add( bSizer26114, 1, wx.EXPAND, 5 )

		bSizer261112 = wx.BoxSizer( wx.HORIZONTAL )

		self.txt_hp_superman2 = wx.StaticText( self, wx.ID_ANY, u"HP : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_hp_superman2.Wrap( -1 )

		self.txt_hp_superman2.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.txt_hp_superman2.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.txt_hp_superman2.SetToolTip( u"Jumlah Koin Anda" )

		bSizer261112.Add( self.txt_hp_superman2, 1, wx.ALL, 5 )

		self.HP_superman2 = wx.StaticText( self, wx.ID_ANY, u"20", wx.Point( -1,-1 ), wx.Size( -1,-1 ), 0 )
		self.HP_superman2.Wrap( -1 )

		self.HP_superman2.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.HP_superman2.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		bSizer261112.Add( self.HP_superman2, 0, wx.ALL, 5 )


		bSizer1652.Add( bSizer261112, 1, wx.EXPAND, 5 )

		bSizer261122 = wx.BoxSizer( wx.HORIZONTAL )

		self.txt_max_hp_superman2 = wx.StaticText( self, wx.ID_ANY, u"Max HP : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_max_hp_superman2.Wrap( -1 )

		self.txt_max_hp_superman2.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.txt_max_hp_superman2.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.txt_max_hp_superman2.SetToolTip( u"Jumlah Koin Anda" )

		bSizer261122.Add( self.txt_max_hp_superman2, 1, wx.ALL, 5 )

		self.attack_superman22 = wx.StaticText( self, wx.ID_ANY, u"20", wx.Point( -1,-1 ), wx.Size( -1,-1 ), 0 )
		self.attack_superman22.Wrap( -1 )

		self.attack_superman22.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.attack_superman22.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		bSizer261122.Add( self.attack_superman22, 0, wx.ALL, 5 )


		bSizer1652.Add( bSizer261122, 1, wx.EXPAND, 5 )

		self.cb_hero_joker = wx.CheckBox( self, wx.ID_ANY, u"Pilih", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cb_hero_joker.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		bSizer1652.Add( self.cb_hero_joker, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer202.Add( bSizer1652, 1, wx.EXPAND, 5 )

		bSizer1651 = wx.BoxSizer( wx.VERTICAL )

		self.m_bpButton461 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 200,300 ), wx.BU_AUTODRAW|0 )

		self.m_bpButton461.SetBitmap( wx.Bitmap( u"properties/img/23/superman23.bmp", wx.BITMAP_TYPE_ANY ) )
		bSizer1651.Add( self.m_bpButton461, 0, wx.ALL, 5 )

		bSizer26113 = wx.BoxSizer( wx.HORIZONTAL )

		self.txt_attack_superman1 = wx.StaticText( self, wx.ID_ANY, u"Attack : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_attack_superman1.Wrap( -1 )

		self.txt_attack_superman1.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.txt_attack_superman1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.txt_attack_superman1.SetToolTip( u"Jumlah Koin Anda" )

		bSizer26113.Add( self.txt_attack_superman1, 1, wx.ALL, 5 )

		self.attack_superman1 = wx.StaticText( self, wx.ID_ANY, u"20", wx.Point( -1,-1 ), wx.Size( -1,-1 ), 0 )
		self.attack_superman1.Wrap( -1 )

		self.attack_superman1.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.attack_superman1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		bSizer26113.Add( self.attack_superman1, 0, wx.ALL, 5 )


		bSizer1651.Add( bSizer26113, 1, wx.EXPAND, 5 )

		bSizer261111 = wx.BoxSizer( wx.HORIZONTAL )

		self.txt_hp_superman1 = wx.StaticText( self, wx.ID_ANY, u"HP : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_hp_superman1.Wrap( -1 )

		self.txt_hp_superman1.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.txt_hp_superman1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.txt_hp_superman1.SetToolTip( u"Jumlah Koin Anda" )

		bSizer261111.Add( self.txt_hp_superman1, 1, wx.ALL, 5 )

		self.HP_superman1 = wx.StaticText( self, wx.ID_ANY, u"20", wx.Point( -1,-1 ), wx.Size( -1,-1 ), 0 )
		self.HP_superman1.Wrap( -1 )

		self.HP_superman1.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.HP_superman1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		bSizer261111.Add( self.HP_superman1, 0, wx.ALL, 5 )


		bSizer1651.Add( bSizer261111, 1, wx.EXPAND, 5 )

		bSizer261121 = wx.BoxSizer( wx.HORIZONTAL )

		self.txt_max_hp_superman1 = wx.StaticText( self, wx.ID_ANY, u"Max HP : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_max_hp_superman1.Wrap( -1 )

		self.txt_max_hp_superman1.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.txt_max_hp_superman1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.txt_max_hp_superman1.SetToolTip( u"Jumlah Koin Anda" )

		bSizer261121.Add( self.txt_max_hp_superman1, 1, wx.ALL, 5 )

		self.attack_superman21 = wx.StaticText( self, wx.ID_ANY, u"20", wx.Point( -1,-1 ), wx.Size( -1,-1 ), 0 )
		self.attack_superman21.Wrap( -1 )

		self.attack_superman21.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.attack_superman21.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		bSizer261121.Add( self.attack_superman21, 0, wx.ALL, 5 )


		bSizer1651.Add( bSizer261121, 1, wx.EXPAND, 5 )

		self.cb_hero_superman = wx.CheckBox( self, wx.ID_ANY, u"Pilih", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cb_hero_superman.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		bSizer1651.Add( self.cb_hero_superman, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer202.Add( bSizer1651, 1, wx.EXPAND, 5 )

		bSizer165 = wx.BoxSizer( wx.VERTICAL )

		self.m_bpButton46 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 200,300 ), wx.BU_AUTODRAW|0 )

		self.m_bpButton46.SetBitmap( wx.Bitmap( u"properties/img/23/wonderwomen23.bmp", wx.BITMAP_TYPE_ANY ) )
		bSizer165.Add( self.m_bpButton46, 0, wx.ALL, 5 )

		bSizer2611 = wx.BoxSizer( wx.HORIZONTAL )

		self.txt_attack_superman = wx.StaticText( self, wx.ID_ANY, u"Attack : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_attack_superman.Wrap( -1 )

		self.txt_attack_superman.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.txt_attack_superman.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.txt_attack_superman.SetToolTip( u"Jumlah Koin Anda" )

		bSizer2611.Add( self.txt_attack_superman, 1, wx.ALL, 5 )

		self.attack_superman = wx.StaticText( self, wx.ID_ANY, u"20", wx.Point( -1,-1 ), wx.Size( -1,-1 ), 0 )
		self.attack_superman.Wrap( -1 )

		self.attack_superman.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.attack_superman.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		bSizer2611.Add( self.attack_superman, 0, wx.ALL, 5 )


		bSizer165.Add( bSizer2611, 1, wx.EXPAND, 5 )

		bSizer26111 = wx.BoxSizer( wx.HORIZONTAL )

		self.txt_hp_superman = wx.StaticText( self, wx.ID_ANY, u"HP : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_hp_superman.Wrap( -1 )

		self.txt_hp_superman.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.txt_hp_superman.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.txt_hp_superman.SetToolTip( u"Jumlah Koin Anda" )

		bSizer26111.Add( self.txt_hp_superman, 1, wx.ALL, 5 )

		self.HP_superman = wx.StaticText( self, wx.ID_ANY, u"20", wx.Point( -1,-1 ), wx.Size( -1,-1 ), 0 )
		self.HP_superman.Wrap( -1 )

		self.HP_superman.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.HP_superman.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		bSizer26111.Add( self.HP_superman, 0, wx.ALL, 5 )


		bSizer165.Add( bSizer26111, 1, wx.EXPAND, 5 )

		bSizer26112 = wx.BoxSizer( wx.HORIZONTAL )

		self.txt_max_hp_superman = wx.StaticText( self, wx.ID_ANY, u"Max HP : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_max_hp_superman.Wrap( -1 )

		self.txt_max_hp_superman.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.txt_max_hp_superman.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.txt_max_hp_superman.SetToolTip( u"Jumlah Koin Anda" )

		bSizer26112.Add( self.txt_max_hp_superman, 1, wx.ALL, 5 )

		self.attack_superman2 = wx.StaticText( self, wx.ID_ANY, u"20", wx.Point( -1,-1 ), wx.Size( -1,-1 ), 0 )
		self.attack_superman2.Wrap( -1 )

		self.attack_superman2.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.attack_superman2.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		bSizer26112.Add( self.attack_superman2, 0, wx.ALL, 5 )


		bSizer165.Add( bSizer26112, 1, wx.EXPAND, 5 )

		self.cb_hero_wonderwomen = wx.CheckBox( self, wx.ID_ANY, u"Pilih", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cb_hero_wonderwomen.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		bSizer165.Add( self.cb_hero_wonderwomen, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer202.Add( bSizer165, 1, wx.EXPAND, 5 )


		bSizer164.Add( bSizer202, 1, wx.EXPAND, 5 )

		self.btn_pilih_hero = wx.Button( self, wx.ID_ANY, u"Start", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_pilih_hero.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer164.Add( self.btn_pilih_hero, 0, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer164 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


