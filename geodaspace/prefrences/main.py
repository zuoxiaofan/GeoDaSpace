import wx
from control import preferencesDialog
from preferences_xrc import xrcDemo

class demo(xrcDemo):
    def __init__(self,parent=None):
        xrcDemo.__init__(self,parent)
        self.config  = preferencesDialog()
    def OnButton_prefsButton(self,evt):
        print self.config.model._modelData
        rs = self.config.ShowModal()
        if rs == wx.ID_OK:
            print "Prefs updated!"
        elif rs == wx.ID_CANCEL:
            print "Canceled..."
        else:
            print "no idea?,",rs

class SimpleStandaloneApp(wx.App):
    def OnInit(self):
        self.frame = demo()
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

def run():
    app = SimpleStandaloneApp(redirect=False)
    app.MainLoop()

if __name__ == '__main__':
    run()
