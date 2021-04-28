import wx
import os
import UIWidget
import os
import version

def importer(name, root_package=False, relative_globals=None, level=0):
    """ We only import modules, functions can be looked up on the module.
    Usage:

    from foo.bar import baz
    >>> baz = importer('foo.bar.baz')

    import foo.bar.baz
    >>> foo = importer('foo.bar.baz', root_package=True)
    >>> foo.bar.baz

    from .. import baz (level = number of dots)
    >>> baz = importer('baz', relative_globals=globals(), level=2)
    """
    return __import__(name, locals=None, # locals has no use
                      globals=relative_globals,
                      fromlist=[] if root_package else [None],
                      level=level)

# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

class MyCryptoNode(UIWidget.CryptoNode):
    def __init__(self, parent=None, level=0):
        UIWidget.CryptoNode.__init__(self, parent=parent)
        self.level = level
        #self.m_static_level.SetSize((40*(level+1),40))
        #self.m_static_level.SetMinSize((40 * (level + 1), 40))
        #print(level)
        sizer = self.GetSizer()
        assert isinstance(sizer, wx.BoxSizer)
        sizer.InsertSpacer(0,20*level)
        if self.level!=0:
            self.m_static_level.SetLabel(str(level))

        self.childrennodes=[]
        self.parentnode=None

        self.mainframe=None
        self.autoscantemplate()
        self.content = ''
        funca = self.m_choice_crypto.GetString(0)
        self.createsettings(funcname=funca)

    def autoscantemplate(self):
        f = []
        for (dirpath, dirnames, filenames) in os.walk('template'):
            for ff in filenames:
                if ff != '__init__.py':
                    f.append(ff)
            break
        funcs = [os.path.splitext(x)[0] for x in f ]
        #print(funcs)
        self.m_choice_crypto.AppendItems(sorted(funcs))

    def callfunc(self, funcname='',setting={}, direction='' ,content=''):
        modd = importer("template."+funcname)
        r=''
        s=''
        #print(setting)
        if direction == 'encode':
            try:
                r = modd.encode(content, setting)
            except Exception as e :
                s = e.__str__()
        if direction == 'decode':
            try:
                r = modd.decode(content, setting)
            except Exception as e :
                s = e.__str__()
        return (r,s)

    def newcrypto(self, cryptofunc='', info='', content=''):
        #print('get param r:', content)
        assert isinstance(self.mainframe, MyMainFrame)
        self.mainframe.newcrypto(cryptofunc=cryptofunc+':'+info, param=None, level=self.level+1, caller=self, content=content)


    def on_encode( self, event ):
        f = self.m_choice_crypto.GetSelection()
        s = self.m_choice_crypto.GetString(f)

        content = self.m_textCtrt.GetValue()
        rng = self.m_textCtrt.GetSelection()
        cs = content[rng[0]: rng[1]]
        if len(cs) > 0:
            content = cs
        #print(content)

        setting={}

        for item in self.m_panel_setting.GetChildren():
            assert isinstance(item, UIWidget.SettingBlock)
            k = item.m_static.GetLabel()
            v = item.m_text.GetValue()
            setting[k] = v

        if len(content)>0:
            r,k = self.callfunc(funcname=s, setting=setting, direction='encode', content=content)
            if k == '':
                #print('resule :', s, r)
                self.newcrypto(cryptofunc=s, info='encoded' ,content=r)
            else:
                self.mainframe.logmessage(k)

    def on_decode( self, event ):
        f = self.m_choice_crypto.GetSelection()
        s = self.m_choice_crypto.GetString(f)

        content = self.m_textCtrt.GetValue()
        rng = self.m_textCtrt.GetSelection()
        cs = content[rng[0]: rng[1]]
        if len(cs) > 0:
            content = cs
        #print(content)

        setting = {}

        for item in self.m_panel_setting.GetChildren():
            assert isinstance(item, UIWidget.SettingBlock)
            k = item.m_static.GetLabel()
            v = item.m_text.GetValue()
            setting[k] = v

        if len(content)>0:
            r,k = self.callfunc(funcname=s, setting=setting, direction='decode', content=content)
            #print('resule :', s, r)
            rs =''
            if type(r) == str:
                rs = r
            else:
                try:
                    rs = r.decode('utf-8')
                except:
                    #self.mainframe.logmessage('can not decode with utf-8, try iso8859-1.')
                    rs = r.decode('iso8859-1')
            if k == '':
                self.newcrypto(cryptofunc=s, info='decoded',content=rs)
            else:
                self.mainframe.logmessage(k)

    def on_shownode( self, event ):
        for item in self.childrennodes:
            item.on_shownode(True)
            item.Show(True)
        self.mainframe.Layout()
    def on_hidenode( self, event ):
        for item in self.childrennodes:
            item.on_hidenode(False)
            item.Show(False)
        self.mainframe.Layout()
    def on_dismiss( self, event ):
        if self.parentnode:
            for item in self.childrennodes:
                item.on_dismiss(event)
            self.childrennodes=[]
            self.parentnode.childrennodes.remove(self)
            self.mainframe.stack.remove(self)
            self.Destroy()
    def relevel(self,level=0):
        self.level=level
        sizer = self.GetSizer()
        assert isinstance(sizer, wx.BoxSizer)
        spacer = sizer.GetItem(0)
        assert isinstance(spacer, wx.SizerItem)
        spacer.SetMinSize(level*20, 20)
        self.m_static_level.SetLabel(str(level))
        for item in self.childrennodes:
            item.relevel(level=level+1)
    def on_deattach( self, event ):
        self.relevel(1)
        #
        self.parentnode.childrennodes.remove(self)
        self.parentnode = self.mainframe.m_root_pane
        self.parentnode.childrennodes.append(self)
        self.mainframe.deattach(node = self)

    def createsettings(self, funcname=''):
        sizer = self.m_panel_setting.GetSizer()
        assert isinstance(sizer, wx.Sizer)
        willremove = []
        for item in self.m_panel_setting.GetChildren():
            willremove.append(item)
        for item in willremove:
            #sizer.Remove(item)
            self.m_panel_setting.RemoveChild(item)
            item.Destroy()
        funcsetting = importer("template." + funcname)
        dd = funcsetting.setting
        assert isinstance(dd, dict)
        for k in dd:
            aa = UIWidget.SettingBlock(parent=self.m_panel_setting)
            assert isinstance(aa, UIWidget.SettingBlock)
            aa.m_static.SetLabel(k)
            aa.m_text.SetValue(dd[k])
            self.m_panel_setting
            sizer.Add(aa, 0, wx.EXPAND | wx.ALL, 1)
        sizer.Fit( self.m_panel_setting )
        sizer.Layout()
    def on_show_setting( self, event ):
        if self.m_toggle_setting.GetValue():
            self.m_panel_setting.Show()
        else:
            self.m_panel_setting.Hide()
        self.Layout()

    def on_choice_module( self, event ):
        ch = self.m_choice_crypto.GetSelection()
        funca = self.m_choice_crypto.GetString(ch)
        self.createsettings(funca)

class MyMainFrame(UIWidget.MainFrame):
    def __init__(self, parent=None):
        UIWidget.MainFrame.__init__(self, parent=parent)
        self.m_scrollsizer = self.m_scrolledWindow1.GetSizer()
        self.m_scrolledWindow1.SetAutoLayout(1)
        assert isinstance(self.m_scrollsizer, wx.BoxSizer)
        self.m_root_pane = MyCryptoNode(parent=self.m_scrolledWindow1)
        self.m_root_pane.mainframe=self
        self.m_scrollsizer.Add(self.m_root_pane, 1 ,wx.ALL|wx.EXPAND, 5)
        self.stack = []
        self.stack.append(self.m_root_pane)
        title = self.GetTitle()
        self.SetTitle(title+version.v)
    def newcrypto(self, cryptofunc='', param=None, level=0, caller=None, content=''):
        spos = self.m_scrolledWindow1.GetScrollPos(orientation=wx.VERTICAL)
        newpane = MyCryptoNode(parent=self.m_scrolledWindow1, level=level)
        newpane.m_textCtrt.SetValue((content))
        newpane.m_static_label.SetLabel(cryptofunc)
        newpane.mainframe = self
        assert isinstance(self.m_scrollsizer, wx.BoxSizer)
        if caller:
            assert isinstance(caller, MyCryptoNode)
            caller.childrennodes.append(newpane)
            newpane.parentnode = caller
        if caller:
            index = self.stack.index(caller)
            self.stack.insert(index+1, newpane)
            #print('caller index', index)
            self.m_scrollsizer.Insert(index+1, newpane,  1, wx.ALL | wx.EXPAND, 5)
        else:
            #print('no caller')
            self.stack.append(newpane)
            self.m_scrollsizer.Add(newpane, 1, wx.ALL | wx.EXPAND, 5)
        self.m_scrolledWindow1.Layout()
        assert isinstance(self.m_scrollsizer, wx.BoxSizer)
        self.m_scrollsizer.Fit(self.m_scrolledWindow1)
        #print(spos)
        #self.m_scrolledWindow1.SetScrollPos(orientation=wx.VERTICAL, pos=spos, refresh=True)
        #self.m_scrolledWindow1.Set
        self.Layout()
        self.m_scrolledWindow1.Scroll(0,spos)
    def deattach(self, node=None):
        assert isinstance(node, MyCryptoNode)
        spos = self.m_scrolledWindow1.GetScrollPos(orientation=wx.VERTICAL)
        self.Layout()
        self.m_scrolledWindow1.Scroll(0, spos)
    def logmessage(self,msg=''):
        assert isinstance(self.m_statusBar1, wx.StatusBar)
        self.m_statusBar1.SetStatusText(msg)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = wx.App()
    frame = MyMainFrame(None)
    frame.Show()
    app.MainLoop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
