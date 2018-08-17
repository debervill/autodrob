#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.8.3 on Fri Aug 17 15:44:00 2018
#

import wx

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class SettingsMainFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: SettingsMainFrame.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((252, 143))
        self.SettingsFramePanel = wx.Panel(self, wx.ID_ANY)
        self.btn_add_lab = wx.Button(self.SettingsFramePanel, wx.ID_ANY, u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043b\u0430\u0431\u043e\u0440\u0430\u0442\u043e\u0440\u043d\u0443\u044e \u0440\u0430\u0431\u043e\u0442\u0443")
        self.btn_edit_lab = wx.Button(self.SettingsFramePanel, wx.ID_ANY, u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043b\u0430\u0431\u043e\u0440\u0430\u0442\u043e\u0440\u043d\u0443\u044e \u0440\u0430\u0431\u043e\u0442\u0443\n")
        self.btn_del_lab = wx.Button(self.SettingsFramePanel, wx.ID_ANY, u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u043b\u0430\u0431\u043e\u0440\u0430\u0442\u043e\u0440\u043d\u0443\u044e \u0440\u0430\u0431\u043e\u0442\u0443")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.add_lab, self.btn_add_lab)
        self.Bind(wx.EVT_BUTTON, self.edit_lab, self.btn_edit_lab)
        self.Bind(wx.EVT_BUTTON, self.remove_lab, self.btn_del_lab)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: SettingsMainFrame.__set_properties
        self.SetTitle("frame")
        self.btn_add_lab.SetMinSize((250, 26))
        self.btn_edit_lab.SetMinSize((250, 37))
        self.btn_del_lab.SetMinSize((250, 26))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: SettingsMainFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_2.Add(self.btn_add_lab, 0, 0, 0)
        sizer_2.Add(self.btn_edit_lab, 0, 0, 0)
        sizer_2.Add(self.btn_del_lab, 0, 0, 0)
        self.SettingsFramePanel.SetSizer(sizer_2)
        sizer_1.Add(self.SettingsFramePanel, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        # end wxGlade

    def add_lab(self, event):  # wxGlade: SettingsMainFrame.<event_handler>
        print("Event handler 'add_lab' not implemented!")
        event.Skip()

    def edit_lab(self, event):  # wxGlade: SettingsMainFrame.<event_handler>
        print("Event handler 'edit_lab' not implemented!")
        event.Skip()

    def remove_lab(self, event):  # wxGlade: SettingsMainFrame.<event_handler>
        print("Event handler 'remove_lab' not implemented!")
        event.Skip()

# end of class SettingsMainFrame

class MyApp(wx.App):
    def OnInit(self):
        self.frame = SettingsMainFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

# end of class MyApp

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()