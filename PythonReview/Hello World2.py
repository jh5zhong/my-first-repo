# 一个稍微扩展的wxPython示例，它创建了一个带有菜单栏、状态栏和一些菜单项的窗口
#总的来说，这个代码示例展示了如何使用wxPython创建一个简单的窗口应用程序，包括如何设置窗口的基本属性、添加控件、创建菜单栏和处理用户事件。
#!/usr/bin/env python
"""
Hello World, but with more meat.
"""
# 导入wxPython库：它包含了创建GUI应用程序所需的所有类和函数。
import wx

class HelloFrame(wx.Frame):#定义HelloFrame类,这个类继承自wx.Frame，代表应用程序的主窗口。
    """
    A Frame that says Hello World
    """

#初始化init方法，当创建HelloFrame类的新实例时，这个方法会被调用。
#它设置窗口的基本属性，如添加一个面板（wx.Panel），在面板上添加一个静态文本（wx.StaticText），
#并设置文本的字体为粗体且增大点大小。它还创建了一个垂直的sizer来管理面板上的控件布局，并设置了一个菜单栏和状态栏。

    def __init__(self, *args, **kw):
        # ensure the parent's __init__ is called
        super(HelloFrame, self).__init__(*args, **kw)

        # create a panel in the frame
        pnl = wx.Panel(self)

        # put some text with a larger bold font on it
        st = wx.StaticText(pnl, label="Hello World!")
        font = st.GetFont()
        font.PointSize += 10
        font = font.Bold()
        st.SetFont(font)

        # and create a sizer to manage the layout of child widgets
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(st, wx.SizerFlags().Border(wx.TOP|wx.LEFT, 25))
        pnl.SetSizer(sizer)

        # create a menu bar
        self.makeMenuBar()

        # and a status bar
        self.CreateStatusBar()
        self.SetStatusText("Welcome to wxPython!")

#这个方法创建了一个菜单栏，包括文件（File）和帮助（Help）两个菜单。文件菜单中有“Hello...”和“Exit”两个菜单项，帮助菜单中有一个“About”菜单项。每个菜单项都绑定了一个事件处理程序，用于响应用户的菜单选择。

    def makeMenuBar(self):
        """
        A menu bar is composed of menus, which are composed of menu items.
        This method builds a set of menus and binds handlers to be called
        when the menu item is selected.
        """

        # Make a file menu with Hello and Exit items
        fileMenu = wx.Menu()
        # The "\t..." syntax defines an accelerator key that also triggers
        # the same event
        helloItem = fileMenu.Append(-1, "&Hello...\tCtrl-H",
                "Help string shown in status bar for this menu item")
        fileMenu.AppendSeparator()
        # When using a stock ID we don't need to specify the menu item's
        # label
        exitItem = fileMenu.Append(wx.ID_EXIT)

        # Now a help menu for the about item
        helpMenu = wx.Menu()
        aboutItem = helpMenu.Append(wx.ID_ABOUT)

        # Make the menu bar and add the two menus to it. The '&' defines
        # that the next letter is the "mnemonic" for the menu item. On the
        # platforms that support it those letters are underlined and can be
        # triggered from the keyboard.
        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, "&File")
        menuBar.Append(helpMenu, "&Help")

        # Give the menu bar to the frame
        self.SetMenuBar(menuBar)

        # Finally, associate a handler function with the EVT_MENU event for
        # each of the menu items. That means that when that menu item is
        # activated then the associated handler function will be called.
        self.Bind(wx.EVT_MENU, self.OnHello, helloItem)
        self.Bind(wx.EVT_MENU, self.OnExit,  exitItem)
        self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)
#这些方法是事件处理程序，用于响应用户在菜单上执行的操作。OnExit关闭应用程序窗口，OnHello显示一个带有消息“Hello again from wxPython”的消息框，OnAbout显示一个关于对话框，其中包含有关应用程序的信息。

    def OnExit(self, event):
        """Close the frame, terminating the application."""
        self.Close(True)


    def OnHello(self, event):
        """Say hello to the user."""
        wx.MessageBox("Hello again from wxPython")


    def OnAbout(self, event):
        """Display an About Dialog"""
        wx.MessageBox("This is a wxPython Hello World sample",
                      "About Hello World 2",
                      wx.OK|wx.ICON_INFORMATION)

#当这个脚本被直接运行时（而不是作为模块导入时），这部分代码会执行。它首先创建一个wx.App对象，这是wxPython应用程序的核心。然后，它创建一个HelloFrame对象（即主窗口），显示这个窗口，并启动应用程序的事件循环。
if __name__ == '__main__':
    # When this module is run (not imported) then create the app, the
    # frame, show it, and start the event loop.
    app = wx.App()
    frm = HelloFrame(None, title='Hello World 2')
    frm.Show()
    app.MainLoop()