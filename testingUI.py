import wx
import noname

class subClass(noname.f_inventory):
	def __init__(self,parent):
		noname.f_inventory.__init__(self,parent)	


app = wx.App()
frame = subClass(parent=None)
frame.Show()

app.MainLoop()
