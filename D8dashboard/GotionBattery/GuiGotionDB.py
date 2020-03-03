# -*- coding: utf-8 -*-

###########################################################################
## Wx based python GUI for mySQL database
## Xiaojun Li Phd.
###########################################################################
# # compliation setting
# import sys
# sys.setrecursionlimit(5000)

# GUI
from WxForms import MyFrame1, DBConnection, OpenFileFrame, PopupDisplay
import wx

# general
from pandas import DataFrame

# Batterlean modules
from BatteryData import GotionMySql as GSql
from BatteryDocs import DocProcess
from dfgui import dfgui

# file-scope variables
g_dbconn: GSql
g_dbtable: DataFrame
g_file: DocProcess
g_table_ls: list


class gDBConPanel(DBConnection):
    def __init__(self, parent):
        DBConnection.__init__(self, parent)

    def callDBConnection(self, event):
        global g_dbconn, g_table_ls

        g_dbconn = GSql(host_path=self.i_dburl.Value,
                        user_name=self.i_usrname.Value,
                        password_code=self.i_pwd.Value,
                        db_name='GotionDB')
        restuls = g_dbconn.connect()
        # todo: add error handling
        DFtables, g_table_ls = g_dbconn.fetchAllTablesName()
        # set the html view
        self.m_htmlWin1.SetPage(DFtables.to_html())
        self.m_htmlWin1.Show(True)
        self.Parent.SetStatusText('Database: GotionDB', 0)
        if g_table_ls:
            self.Parent.callRefreshTableList(event)

    # def callmainRefresh(self, event):
    #     self.Close(True)


class gOpenFilePanel(OpenFileFrame):
    def __init__(self, parent):
        OpenFileFrame.__init__(self, parent)

    def CallLoadFile(self, event):
        file_loc = self.m_filePicker5.Path
        self.Parent.setStatusBar(file_loc, 2)
        g_file = DocProcess(file_loc)
        self.Close()
        pass


class gPopDisp(PopupDisplay):
    def __init__(self, parent):
        PopupDisplay.__init__(self, parent)


class gMainFrame(MyFrame1):
    tableLoaded: DataFrame

    def __init__(self, parent):
        MyFrame1.__init__(self, parent)
        self.setStatusBar('not set', 0)
        self.setStatusBar('not selected', 1)
        self.setStatusBar('not selected', 2)

    # private methods
    def setStatusBar(self, states, col_num):
        if col_num == 0:
            self.SetStatusText('Database: ' + states, 0)
        elif col_num == 1:
            self.SetStatusText('Table: ' + states, 1)
        elif col_num == 2:
            self.SetStatusText('File: ' + states, 2)

    def sethtmlwin(self, df_ojb):
        self.m_htmlWinDisp.SetPage(df_ojb.to_html())
        self.m_htmlWinDisp.Show(True)

    # button related methods
    def calldbPanelPop(self, event):
        dbPanel_ins = gDBConPanel(self.GetTopLevelParent())
        dbPanel_ins.Show(True)

    def callOpenFilePanel(self, event):
        openfilepnael_ins = gOpenFilePanel(self.GetTopLevelParent())
        openfilepnael_ins.Show(True)

    def callRefreshTableList(self, event):
        tables = [tb['TABLE_NAME'] for tb in g_table_ls]
        self.m_listBox2.Set(tables)

    def callloadTheTable(self, event):
        table_sel = self.m_listBox2.GetString(self.m_listBox2.GetSelection())
        self.tableLoaded, _ = g_dbconn.downloadTable(table_sel)
        self.sethtmlwin(self.tableLoaded.head(10))
        self.setStatusBar(table_sel, 1)

    def callshowtable(self, event):
        dfgui.show(self.tableLoaded)

    def callExcelTable(self, event):
        g_dbtable.to_excel()

    def callPreviewDoc(self, event):
        event.Skip()

    def callDifffiles(self, event):
        print('todo: implement DIFF !')
        PopupDisp_ins = gPopDisp(self.GetTopLevelParent())
        PopupDisp_ins.Show(True)


###########################################################################
## main entry
###########################################################################


if __name__ == '__main__':
    app = wx.App(False)
    frame = gMainFrame(parent=None)
    frame.SetIcon(wx.Icon("data/GotionIconTransparent.ico"))
    frame.Show()
    app.MainLoop()
