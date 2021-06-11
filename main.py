from control import c_main
import wx

class main:
    def __init__(self):
        self.app = wx.App()
        self.controller = c_main.control_main()
        self.app.MainLoop()



user = main()