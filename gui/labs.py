#!/usr/bin/env python
# -*- coding: UTF-8 -*-


import wx

class SettingsMainFrame(wx.Frame):
    def __init__(self, *args, **kwds):

        wx.Frame.__init__(self, None, -1, 'Title', style= wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX)
        self.SetSize((252, 143))
        self.SettingsFramePanel = wx.Panel(self, wx.ID_ANY)
        self.btn_add_lab = wx.Button(self.SettingsFramePanel, wx.ID_ANY, u"Добавить лабораторную работу")
        self.btn_edit_lab = wx.Button(self.SettingsFramePanel, wx.ID_ANY, u"Редактировать лабораторную работу")
        self.btn_del_lab = wx.Button(self.SettingsFramePanel, wx.ID_ANY, u"Удалить лабораторную работу")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.add_lab, self.btn_add_lab)
        self.Bind(wx.EVT_BUTTON, self.edit_lab, self.btn_edit_lab)
        self.Bind(wx.EVT_BUTTON, self.remove_lab, self.btn_del_lab)


    def __set_properties(self):

        self.SetTitle("frame")
        self.btn_add_lab.SetMinSize((250, 26))
        self.btn_edit_lab.SetMinSize((250, 37))
        self.btn_del_lab.SetMinSize((250, 26))


    def __do_layout(self):

        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_2.Add(self.btn_add_lab, 0, 0, 0)
        sizer_2.Add(self.btn_edit_lab, 0, 0, 0)
        sizer_2.Add(self.btn_del_lab, 0, 0, 0)
        self.SettingsFramePanel.SetSizer(sizer_2)
        sizer_1.Add(self.SettingsFramePanel, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        self.Layout()


    def add_lab(self, event):
        print("Event handler 'add_lab' not implemented!")
        event.Skip()

    def edit_lab(self, event):
        print("Event handler 'edit_lab' not implemented!")
        event.Skip()

    def remove_lab(self, event):
        print("Event handler 'remove_lab' not implemented!")
        event.Skip()



class MyApp(wx.App):
    def OnInit(self):
        self.frame = SettingsMainFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True



if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
