# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.html
import wx.richtext


###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Gotion Software Management Tool", pos=wx.DefaultPosition,
                          size=wx.Size(650, 533), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        self.m_menubar1 = wx.MenuBar(0)
        self.m_File = wx.Menu()
        self.m_openfile = wx.MenuItem(self.m_File, wx.ID_ANY, u"Load", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_File.Append(self.m_openfile)

        self.m_menuItem7 = wx.MenuItem(self.m_File, wx.ID_ANY, u"Preview", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_File.Append(self.m_menuItem7)

        self.m_menuItem9 = wx.MenuItem(self.m_File, wx.ID_ANY, u"Update", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_File.Append(self.m_menuItem9)

        self.m_menubar1.Append(self.m_File, u"File")

        self.m_menu2 = wx.Menu()
        self.m_menuItem3 = wx.MenuItem(self.m_menu2, wx.ID_ANY, u"Connection", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu2.Append(self.m_menuItem3)

        self.m_menubar1.Append(self.m_menu2, u"Settings")

        self.m_menu3 = wx.Menu()
        self.m_RefreshTable = wx.MenuItem(self.m_menu3, wx.ID_ANY, u"Refresh", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu3.Append(self.m_RefreshTable)

        self.m_LoadTable = wx.MenuItem(self.m_menu3, wx.ID_ANY, u"Load Table", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu3.Append(self.m_LoadTable)

        self.m_showTable = wx.MenuItem(self.m_menu3, wx.ID_ANY, u"Show Table", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu3.Append(self.m_showTable)

        self.m_showTable1 = wx.MenuItem(self.m_menu3, wx.ID_ANY, u"Excel Table", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu3.Append(self.m_showTable1)

        self.m_menubar1.Append(self.m_menu3, u"Tables")

        self.m_menu4 = wx.Menu()
        self.m_menuItem8 = wx.MenuItem(self.m_menu4, wx.ID_ANY, u"function1", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu4.Append(self.m_menuItem8)

        self.m_menubar1.Append(self.m_menu4, u"Functions")

        self.SetMenuBar(self.m_menubar1)

        gSizer3 = wx.GridSizer(0, 2, 0, 0)

        bSizer6 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText6 = wx.StaticText(self, wx.ID_ANY, u"Existing tables", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText6.Wrap(-1)

        bSizer6.Add(self.m_staticText6, 0, wx.ALL, 5)

        m_listBox2Choices = []
        self.m_listBox2 = wx.ListBox(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(300, 350), m_listBox2Choices,
                                     wx.LB_ALWAYS_SB)
        bSizer6.Add(self.m_listBox2, 0, wx.ALL, 5)

        self.m_buttondiff = wx.Button(self, wx.ID_ANY, u"Diff", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer6.Add(self.m_buttondiff, 0, wx.ALL, 5)

        gSizer3.Add(bSizer6, 1, wx.EXPAND, 5)

        self.m_htmlWinDisp = wx.html.HtmlWindow(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(300, 400),
                                                wx.html.HW_SCROLLBAR_AUTO)
        self.m_htmlWinDisp.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))

        gSizer3.Add(self.m_htmlWinDisp, 0, wx.ALL, 5)

        self.SetSizer(gSizer3)
        self.Layout()
        self.m_statusBar1 = self.CreateStatusBar(3, wx.STB_ELLIPSIZE_START | wx.STB_SHOW_TIPS | wx.STB_SIZEGRIP,
                                                 wx.ID_ANY)

        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_MENU, self.callOpenFilePanel, id=self.m_openfile.GetId())
        self.Bind(wx.EVT_MENU, self.callPreviewDoc, id=self.m_menuItem7.GetId())
        self.Bind(wx.EVT_MENU, self.calldbPanelPop, id=self.m_menuItem3.GetId())
        self.Bind(wx.EVT_MENU, self.callRefreshTableList, id=self.m_RefreshTable.GetId())
        self.Bind(wx.EVT_MENU, self.callshowtable, id=self.m_showTable.GetId())
        self.Bind(wx.EVT_MENU, self.callExcelTable, id=self.m_showTable1.GetId())
        self.m_listBox2.Bind(wx.EVT_LISTBOX, self.callloadTheTable)
        self.m_listBox2.Bind(wx.EVT_LISTBOX_DCLICK, self.callshowtable)
        self.m_buttondiff.Bind(wx.EVT_BUTTON, self.callDifffiles)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def callOpenFilePanel(self, event):
        event.Skip()

    def callPreviewDoc(self, event):
        event.Skip()

    def calldbPanelPop(self, event):
        event.Skip()

    def callRefreshTableList(self, event):
        event.Skip()

    def callshowtable(self, event):
        event.Skip()

    def callExcelTable(self, event):
        event.Skip()

    def callloadTheTable(self, event):
        event.Skip()

    def callDifffiles(self, event):
        event.Skip()


###########################################################################
## Class DBConnection
###########################################################################

class DBConnection(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(400, 300), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        gSizer1 = wx.GridSizer(0, 2, 0, 0)

        bSizer4 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText7 = wx.StaticText(self, wx.ID_ANY, u"Database URL", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText7.Wrap(-1)

        bSizer4.Add(self.m_staticText7, 0, wx.ALL, 5)

        self.i_dburl = wx.TextCtrl(self, wx.ID_ANY, u"sw-wus-hx501q2", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer4.Add(self.i_dburl, 0, wx.ALL, 5)

        self.m_staticText8 = wx.StaticText(self, wx.ID_ANY, u"User Name", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText8.Wrap(-1)

        bSizer4.Add(self.m_staticText8, 0, wx.ALL, 5)

        self.i_usrname = wx.TextCtrl(self, wx.ID_ANY, u"data_viewer", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer4.Add(self.i_usrname, 0, wx.ALL, 5)

        self.m_staticText9 = wx.StaticText(self, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText9.Wrap(-1)

        bSizer4.Add(self.m_staticText9, 0, wx.ALL, 5)

        self.i_pwd = wx.TextCtrl(self, wx.ID_ANY, u"welcome123", wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD)
        bSizer4.Add(self.i_pwd, 0, wx.ALL, 5)

        self.m_staticText10 = wx.StaticText(self, wx.ID_ANY, u"Database", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10.Wrap(-1)

        bSizer4.Add(self.m_staticText10, 0, wx.ALL, 5)

        i_dbChoices = []
        self.i_db = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, i_dbChoices, 0)
        self.i_db.SetSelection(0)
        bSizer4.Add(self.i_db, 0, wx.ALL, 5)

        gSizer1.Add(bSizer4, 1, wx.EXPAND, 5)

        bSizer6 = wx.BoxSizer(wx.VERTICAL)

        self.m_button6 = wx.Button(self, wx.ID_ANY, u"Connect", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer6.Add(self.m_button6, 0, wx.ALL, 5)

        self.m_htmlWin1 = wx.html.HtmlWindow(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(500, 500),
                                             wx.html.HW_SCROLLBAR_AUTO | wx.ALWAYS_SHOW_SB | wx.FULL_REPAINT_ON_RESIZE)
        bSizer6.Add(self.m_htmlWin1, 0, wx.ALL, 5)

        gSizer1.Add(bSizer6, 1, wx.EXPAND, 5)

        self.SetSizer(gSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_button6.Bind(wx.EVT_BUTTON, self.callDBConnection)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def callDBConnection(self, event):
        event.Skip()


###########################################################################
## Class OpenFileFrame
###########################################################################

class OpenFileFrame(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(521, 159), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer5 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText11 = wx.StaticText(self, wx.ID_ANY, u"Select the excel file you wish to load",
                                            wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11.Wrap(-1)

        bSizer5.Add(self.m_staticText11, 0, wx.ALL, 5)

        self.m_filePicker5 = wx.FilePickerCtrl(self, wx.ID_ANY,
                                               u"C:\\SCU\\SCUR_A2\\Tools\\CAN_Mapping\\GWEC01\\CAN_Rx_GWMEC01.xlsx",
                                               u"Select a file", u"documentrs(*.xlsx,*.docx)|*.xlsx;*.docx",
                                               wx.DefaultPosition, wx.Size(500, -1), wx.FLP_DEFAULT_STYLE)
        bSizer5.Add(self.m_filePicker5, 0, wx.ALL, 5)

        self.m_buttonLoadFile = wx.Button(self, wx.ID_ANY, u"Select the File", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer5.Add(self.m_buttonLoadFile, 0, wx.ALL, 5)

        self.SetSizer(bSizer5)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_buttonLoadFile.Bind(wx.EVT_BUTTON, self.CallLoadFile)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def CallLoadFile(self, event):
        event.Skip()


###########################################################################
## Class PopupDisplay
###########################################################################

class PopupDisplay(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(500, 300), style=wx.DEFAULT_FRAME_STYLE | wx.MAXIMIZE_BOX | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer5 = wx.BoxSizer(wx.VERTICAL)

        self.m_richText2 = wx.richtext.RichTextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                                    0 | wx.VSCROLL | wx.HSCROLL | wx.NO_BORDER | wx.WANTS_CHARS)
        bSizer5.Add(self.m_richText2, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer5)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass
