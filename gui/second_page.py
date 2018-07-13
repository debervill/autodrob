import wx

class SecondPagePanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(500, 500),
                          style=wx.FULLSCREEN_NOBORDER)
        self.frame = parent

        fgSizer3 = wx.FlexGridSizer(0, 1, 0, 0)
        fgSizer3.SetFlexibleDirection(wx.BOTH)
        fgSizer3.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText5 = wx.StaticText(self, wx.ID_ANY, u"Выберите лабораторную работу", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText5.Wrap(-1)
        fgSizer3.Add(self.m_staticText5, 0, wx.ALL, 5)

        self.m_radioBtn9 = wx.RadioButton(self, wx.ID_ANY, u"Лабораторная работа  № 1.", wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer3.Add(self.m_radioBtn9, 0, wx.ALL, 5)

        self.m_radioBtn10 = wx.RadioButton(self, wx.ID_ANY, u"Лабораторная работа  № 2.", wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer3.Add(self.m_radioBtn10, 0, wx.ALL, 5)

        self.m_radioBtn11 = wx.RadioButton(self, wx.ID_ANY, u"Лабораторная работа  № 3.", wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer3.Add(self.m_radioBtn11, 0, wx.ALL, 5)

        self.m_radioBtn12 = wx.RadioButton(self, wx.ID_ANY, u"Лабораторная работа  № 4.", wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer3.Add(self.m_radioBtn12, 0, wx.ALL, 5)

        self.SetSizer(fgSizer3)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_radioBtn9.Bind(wx.EVT_LEFT_DCLICK, self.lab1)




    # Virtual event handlers, overide them in your derived class
    def lab1(self, event):
        from labs.lab1 import lab1
        nex_page = lab1.MainFrame()
        nex_page.Show()

class SecondPage(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"SecondPage", pos=wx.DefaultPosition,
                          size=wx.Size(500, 300), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        self.Centre(wx.BOTH)
        self.Maximize(True)
        panel = SecondPagePanel(self)

def run_page(self):
    app = wx.App(False)
    frame = SecondPage(None)
    frame.Show()
    app.MainLoop()


