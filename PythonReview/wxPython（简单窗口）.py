import wx
app = wx.App()
frame = wx.Frame(None, title="Hello wxPython", size=(1000, 900))
wx.StaticText(frame, label="Hello wxPython!")
frame.Show()
app.MainLoop()