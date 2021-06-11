import viewUI, wx


class control_petunjuk():
    def __init__(self,username,stage):
        self.view = viewUI.v_petunjuk_permainan(None,username,stage)
        self.view.Show()
