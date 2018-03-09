# -*- coding: utf-8 -*-
import wx
import wx.xrc


class MainPage(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(500, 300), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        sizer_all = wx.FlexGridSizer(3, 2, 0, 0)
        sizer_all.SetFlexibleDirection(wx.BOTH)
        sizer_all.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.lgn_label = wx.StaticText(self, wx.ID_ANY, u"Логин", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lgn_label.Wrap(-1)
        sizer_all.Add(self.lgn_label, 0, wx.ALL, 5)

        self.lgn_txt = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        sizer_all.Add(self.lgn_txt, 0, wx.ALL, 5)

        self.pswd_label = wx.StaticText(self, wx.ID_ANY, u"Пароль", wx.DefaultPosition, wx.DefaultSize, 0)
        self.pswd_label.Wrap(-1)
        sizer_all.Add(self.pswd_label, 0, wx.ALL, 5)

        self.pswd_txt = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, style=wx.TE_PASSWORD)
        sizer_all.Add(self.pswd_txt, 0, wx.ALL, 5)


        self.lgn_button = wx.Button(self, wx.ID_ANY, u"Войти")
        sizer_all.Add(self.lgn_button,0, wx.ALL, 5)

        self.SetSizer(sizer_all)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.lgn_button.Bind(wx.EVT_BUTTON, self.login)


    def login(self, event):
        from gui import second_page
        nxt_page = second_page.SecondPage(None)
        nxt_page.Show()
        nxt_page.Destroy()




app = wx.App(False)
frame = MainPage(None)
frame.Show()
app.MainLoop()


