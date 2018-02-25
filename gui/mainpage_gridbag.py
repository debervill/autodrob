import wx

class MainPage(wx.Frame):
    def __init__(self, *args, **kwds):
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((300, 200))
        self.layout()

    def layout(self):
        sizer = wx.GridBagSizer()
        count = 4

        lgn_label = wx.StaticText(self, wx.NewId(), "Login")
        pswd_label = wx.StaticText(self, wx.NewId(), "Password")
        lgn_text = wx.TextCtrl(self, wx.NewId())
        pswd_text = wx.TextCtrl(self, wx.NewId())

        sizer.Add(lgn_label,  pos=(0, 0))
        sizer.Add(pswd_label, pos=(0, 1))
        sizer.Add(lgn_text,   pos=(1, 0))
        sizer.Add(pswd_text,  pos=(1, 1))

        self.SetSizer(sizer)
        self.layout()



if __name__ == "__main__":
    app = wx.App(0)
    wx.InitAllImageHandlers()
    mainWnd = MainPage(None, -1, "")
    app.SetTopWindow(mainWnd)
    mainWnd.Show()
    app.MainLoop()
