import wx


class MainPanel(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(200, 70))


        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        fgSizer1 = wx.FlexGridSizer(0, 3, 0, 0)
        fgSizer1.SetFlexibleDirection(wx.BOTH)
        fgSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText2 = wx.StaticText(self, wx.ID_ANY, u"Введите пароль", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText2.Wrap(-1)

        fgSizer1.Add(self.m_staticText2, 0, wx.ALL, 5)

        self.m_textCtrl2 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, style=wx.TE_PASSWORD)
        fgSizer1.Add(self.m_textCtrl2, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.btn_ok = wx.Button(self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.Size(60, -1), 0)
        fgSizer1.Add(self.btn_ok, 0, wx.ALL, 5)

        bSizer1.Add(fgSizer1, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer1)
        self.Layout()
        self._bindGuiEvents()

    def __del__(self):
        pass

    def _bindGuiEvents(self):
        self.btn_ok.Bind(wx.EVT_BUTTON, self.ok_pressed)


    def ok_pressed(self, event):
        paswd = self.m_textCtrl2.GetValue()
        if paswd == str('123456'):
            self.run_admin_interface()

    def run_admin_interface(self):
        pass



class MainFrame(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, None, -1, 'Title', style= wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX)

        self.SetSizeHints(70, 70)

        self.Centre(wx.BOTH)
        panel = MainPanel(self)

def run_page():
    app = wx.App(False)
    frame = MainFrame(None)
    frame.Show()
    app.MainLoop()

if __name__ == '__main__':
    run_page()

