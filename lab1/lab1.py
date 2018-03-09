import wx

class Ttheory(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)


class Labs(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

class Results(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)



class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="Simple Notebook Example")

        # Here we create a panel and a notebook on the panel
        p = wx.Panel(self)
        nb = wx.Notebook(p)

        # create the page windows as children of the notebook
        page1 = Ttheory(nb)
        page2 = Labs(nb)
        page3 = Results(nb)

        # add the pages to the notebook with the label to show on the tab
        nb.AddPage(page1, "Теория")
        nb.AddPage(page2, "Задание")
        nb.AddPage(page3, "Отчёт")

        # finally, put the notebook in a sizer for the panel to manage
        # the layout
        sizer = wx.BoxSizer()
        sizer.Add(nb, 1, wx.EXPAND)
        p.SetSizer(sizer)


if __name__ == "__main__":
    app = wx.App()
    MainFrame().Show()
    app.MainLoop()