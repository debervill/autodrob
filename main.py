# -*- coding: utf-8 -*-
import wx


class MainFramePanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(500, 500),
                          style=wx.FULL_REPAINT_ON_RESIZE)
        self.frame = parent

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.lbl_kaf = wx.StaticText(self, wx.ID_ANY, u"Кафедра «Дорожные машины»",
                                     wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_kaf.Wrap(-1)
        bSizer1.Add(self.lbl_kaf, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.lbl_NameProg = wx.StaticText(self, wx.ID_ANY, u"Подбор параметров дробильного комплекса",
                                          wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_NameProg.Wrap(-1)
        bSizer1.Add(self.lbl_NameProg, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.lbl_predstv = wx.StaticText(self, wx.ID_ANY, u"Предстваьтесь", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_predstv.Wrap(-1)
        bSizer1.Add(self.lbl_predstv, 0, wx.ALL, 5)

        fgSizer1 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer1.SetFlexibleDirection(wx.BOTH)
        fgSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.lbl_name = wx.StaticText(self, wx.ID_ANY, u"Имя", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_name.Wrap(-1)
        fgSizer1.Add(self.lbl_name, 0, wx.ALL, 5)

        self.inpt_name = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer1.Add(self.inpt_name, 0, wx.ALL, 5)

        self.lbl_familia = wx.StaticText(self, wx.ID_ANY, u"Фамилия", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_familia.Wrap(-1)
        fgSizer1.Add(self.lbl_familia, 0, wx.ALL, 5)

        self.inpt_familia = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer1.Add(self.inpt_familia, 0, wx.ALL, 5)

        self.lbl_group = wx.StaticText(self, wx.ID_ANY, u"Группа", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_group.Wrap(-1)
        fgSizer1.Add(self.lbl_group, 0, wx.ALL, 5)

        self.inpt_group = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer1.Add(self.inpt_group, 0, wx.ALL, 5)

        self.lbl_zachetka = wx.StaticText(self, wx.ID_ANY, u"№ Зачётной книжки", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lbl_zachetka.Wrap(-1)
        fgSizer1.Add(self.lbl_zachetka, 0, wx.ALL, 5)

        self.inpt_zachetka = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer1.Add(self.inpt_zachetka, 0, wx.ALL, 5)

        bSizer1.Add(fgSizer1, 1, wx.EXPAND, 5)
        gSizer1 = wx.GridSizer(0, 2, 0, 0)

        self.btn_settongs = wx.Button(self, wx.ID_ANY, u"Настройки", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer1.Add(self.btn_settongs, 0, wx.ALIGN_BOTTOM | wx.ALL, 5)

        self.btn_page2 = wx.Button(self, wx.ID_ANY, u"Далее", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer1.Add(self.btn_page2, 0, wx.ALIGN_BOTTOM | wx.ALIGN_RIGHT | wx.ALL, 5)

        bSizer1.Add(gSizer1, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer1)
        self._bindGuiEvents()
        self.Layout()



    def empty_pole(self):
        dlg = wx.MessageDialog(self, 'Не все поля заполнены. Заполните все поля перед продолжением', 'Ошибка', wx.OK)
        val = dlg.ShowModal()
        if val == wx.ID_OK:
            dlg.Destroy()

    def _bindGuiEvents(self):
        self.btn_page2.Bind(wx.EVT_BUTTON, self.go_page2)
        self.btn_settongs.Bind(wx.EVT_BUTTON, self.run_settings)


    def go_page2(self, event):
        from gui import second_page
        values = []

        name = self.inpt_name.GetValue()
        name = name.replace(' ', '')

        familia = self.inpt_familia.GetValue()
        familia = familia.replace(' ','')
        if len(familia) == 0:
            self.empty_pole()
            return

        group = self.inpt_group.GetValue()
        group = group.replace(' ','')
        if len(group) == 0:
            self.empty_pole()
            return

        zach_number = self.inpt_zachetka.GetValue()
        zach_number = zach_number.replace(' ', '')
        if len(zach_number) == 0:
            self.empty_pole()
            return

        values.append(name)
        values.append(familia)
        values.append(group)
        values.append(zach_number)

        print(values)
        self.frame.Hide()
        second_page.run_page(self)

    def  run_settings(self, event):
        from gui import MainSettings
        MainSettings.run_page()

class MainFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(500, 500), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        self.Centre(wx.BOTH)
        panel = MainFramePanel(self)



if __name__ == "__main__":
    print(" ")
    app = wx.App(False)
    frame =  MainFrame(None)
    frame.Show()
    app.MainLoop()