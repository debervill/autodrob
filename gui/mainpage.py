import wx

class MainWindow(wx.Frame):
    def __init__(self, *args, **kwds):
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((300, 200))
        self.doLayout()

    def doLayout(self):
        sizer_hor = wx.BoxSizer(wx.HORIZONTAL)
        sizer_vert_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_vert_2 = wx.BoxSizer(wx.VERTICAL)

        sizer_hor.Add(sizer_vert_1)
        sizer_hor.Add(sizer_vert_2)

        lgn_label = wx.StaticText(self, wx.NewId(), "Login")
        pswd_label = wx.StaticText(self, wx.NewId(), "Password")
        lgn_text = wx.TextCtrl(self, wx.NewId())
        pswd_text = wx.TextCtrl(self, wx.NewId())

        sizer_vert_1.Add(lgn_label, flag=wx.ALL)
        sizer_vert_1.AddSpacer(10)
        sizer_vert_1.Add(pswd_label, flag=wx.ALL)

        sizer_vert_2.Add(lgn_text)
        sizer_vert_2.Add(pswd_text)

        self.SetSizer(sizer_hor)
        self.Layout()


if __name__ == "__main__":
    app = wx.App(0)
    wx.InitAllImageHandlers()
    mainWnd = MainWindow(None, -1, "")
    app.SetTopWindow(mainWnd)
    mainWnd.Show()
    app.MainLoop()
