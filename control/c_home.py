import viewUI, wx

class control_menu():
    def __init__(self,username,stage):
        self.username = username
        self.stage = stage
        self.view = viewUI.v_menu(parent = None)
        self.view.Show()
        self.view.set_value(self.username,self.stage)
