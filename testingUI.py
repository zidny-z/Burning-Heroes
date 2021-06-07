import wx
import noname

class subClass(noname.f_shop):
	def __init__(self,parent):
		noname.f_shop.__init__(self,parent)	
	
	def img_daftarOnButtonClick( self, event ):
		print('a')


app = wx.App()
frame = subClass(parent=None)
frame.Show()

app.MainLoop()
