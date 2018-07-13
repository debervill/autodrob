# -*- coding: utf-8 -*- 

import wx

class PageOne(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        t = wx.StaticText(self, -1, "This is a PageOne object", (20,20))

class PageOne1(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        t = wx.StaticText(self, -1, "This is a PageOne object", (20,20))

class PageOne2(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        t = wx.StaticText(self, -1, "This is a PageOne object", (20, 20))

class MainFramePanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(500, 300),
                          style=wx.TAB_TRAVERSAL)

        bsizer1 = wx.BoxSizer(wx.VERTICAL)

        bsizer2 = wx.BoxSizer(wx.VERTICAL)

        self.m_notebook1 = wx.Notebook(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        bsizer2.Add(self.m_notebook1, 1, wx.EXPAND | wx.ALL, 5)

        bsizer1.Add(bsizer2, 1, wx.EXPAND, 5)

        bSizer3 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_checkBox1 = wx.CheckBox(self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer3.Add(self.m_checkBox1, 0, wx.ALL, 5)

        self.m_checkBox11 = wx.CheckBox(self, wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer3.Add(self.m_checkBox11, 0, wx.ALL, 5)

        self.m_checkBox12 = wx.CheckBox(self, wx.ID_ANY, u"3", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer3.Add(self.m_checkBox12, 0, wx.ALL, 5)

        self.m_checkBox13 = wx.CheckBox(self, wx.ID_ANY, u"4", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer3.Add(self.m_checkBox13, 0, wx.ALL, 5)

        self.m_checkBox14 = wx.CheckBox(self, wx.ID_ANY, u"5", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer3.Add(self.m_checkBox14, 0, wx.ALL, 5)

        self.m_checkBox15 = wx.CheckBox(self, wx.ID_ANY, u"6", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer3.Add(self.m_checkBox15, 0, wx.ALL, 5)

        self.m_checkBox16 = wx.CheckBox(self, wx.ID_ANY, u"7", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer3.Add(self.m_checkBox16, 0, wx.ALL, 5)

        self.m_checkBox17 = wx.CheckBox(self, wx.ID_ANY, u"8", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer3.Add(self.m_checkBox17, 0, wx.ALL, 5)

        self.m_checkBox18 = wx.CheckBox(self, wx.ID_ANY, u"9", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer3.Add(self.m_checkBox18, 0, wx.ALL, 5)

        self.m_checkBox19 = wx.CheckBox(self, wx.ID_ANY, u"10", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer3.Add(self.m_checkBox19, 0, wx.ALL, 5)

        bsizer1.Add(bSizer3, 0, wx.EXPAND, 5)
        # Добавление страниц в noteboock. По данном алгоритму можено (?) динамически доабавлять страницы
        # for i in range(10) и дергать функицию создания страницы
        page1 = PageOne(self.m_notebook1)
        page2 = PageOne1(self.m_notebook1)
        page3 = PageOne2(self.m_notebook1)

        self.m_notebook1.AddPage(page1, "Page 1")
        self.m_notebook1.AddPage(page2, "Page 2")
        self.m_notebook1.AddPage(page3, "Page 3")

        self.SetSizer(bsizer1)
        self.Layout()


class MainFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(500, 300),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        self.Centre(wx.BOTH)
        panel = MainFramePanel(self)

if __name__ == "__main__":
    app = wx.App(False)
    frame =  MainFrame(None)
    frame.Show()
    app.MainLoop()
