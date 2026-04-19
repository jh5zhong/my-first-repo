
# 导入wxPython库。这是使用wxPython创建GUI应用程序所必需的。
import wx
class App(wx.App):
    def OnInit(self):
        frame = wx.Frame(parent = None, title = "Hello World0")
        frame.Show()
        return True
if __name__ == '__main__':
    app = App()
    app.MainLoop()







