import wx

class Page1(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        sizer_all = wx.BoxSizer(wx.HORIZONTAL)





app = wx.App(False)
frame = wx.Frame(None)
panel =Page1(frame)
frame.Show()
app.MainLoop()


