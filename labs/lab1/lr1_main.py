# -*- coding: utf-8 -*-

import wx


class MyPanel1(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(500, 300),
                          style=wx.TAB_TRAVERSAL)

        bSizer3 = wx.BoxSizer(wx.VERTICAL)

        bSizer4 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText2 = wx.StaticText(self, wx.ID_ANY, u"Лабораторная работа 1", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText2.Wrap(-1)

        bSizer4.Add(self.m_staticText2, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_button4 = wx.Button(self, wx.ID_ANY, u"Прочти теорию", wx.DefaultPosition, wx.Size(200, -1), 0)
        bSizer4.Add(self.m_button4, 0, wx.LEFT, 5)

        self.m_button5 = wx.Button(self, wx.ID_ANY, u"Ответь на вопросы", wx.DefaultPosition, wx.Size(200, -1), 0)
        bSizer4.Add(self.m_button5, 0, wx.ALL, 5)

        self.m_button6 = wx.Button(self, wx.ID_ANY, u"Выполни лабораторную работу", wx.DefaultPosition,
                                   wx.Size(200, -1), 0)
        bSizer4.Add(self.m_button6, 0, wx.ALL, 5)

        bSizer3.Add(bSizer4, 1, wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL, 5)

        wSizer1 = wx.WrapSizer(wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS)

        self.m_button10 = wx.Button(self, wx.ID_ANY, u"Выйти", wx.DefaultPosition, wx.DefaultSize, 0)
        wSizer1.Add(self.m_button10, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        bSizer3.Add(wSizer1, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer3)
        self.Layout()
        self.m_button4.Bind(wx.EVT_BUTTON, self.read_theory)

    def read_theory(self):
        pass



class MyFrame1(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(500, 300), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        self.Centre(wx.BOTH)
        panel = MyPanel1(self)

def run_page():
    app = wx.App(False)
    frame = MyFrame1(None)
    frame.Show()
    app.MainLoop()

if __name__ == '__main__':
    run_page()