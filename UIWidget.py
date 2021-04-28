# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"编码解码一把梭", pos = wx.DefaultPosition, size = wx.Size( 1045,533 ), style = wx.DEFAULT_FRAME_STYLE|wx.BORDER_NONE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.m_menu11 = wx.Menu()
		self.m_menu2 = wx.Menu()
		self.m_menu11.AppendSubMenu( self.m_menu2, u"MyMenu" )

		self.m_menu1.AppendSubMenu( self.m_menu11, u"MyMenu" )

		self.m_menubar1.Append( self.m_menu1, u"MyMenu" )

		self.SetMenuBar( self.m_menubar1 )

		self.m_statusBar1 = self.CreateStatusBar( 2, wx.STB_SIZEGRIP, wx.ID_ANY )
		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_scrolledWindow1 = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE|wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow1.SetScrollRate( 20, 20 )
		bSizer4 = wx.BoxSizer( wx.VERTICAL )


		self.m_scrolledWindow1.SetSizer( bSizer4 )
		self.m_scrolledWindow1.Layout()
		bSizer4.Fit( self.m_scrolledWindow1 )
		bSizer1.Add( self.m_scrolledWindow1, 1, wx.EXPAND |wx.ALL, 0 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class CryptoNode
###########################################################################

class CryptoNode ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 843,170 ), style = wx.BORDER_NONE|wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_static_level = wx.StaticText( self, wx.ID_ANY, u"Root", wx.DefaultPosition, wx.Size( 40,-1 ), wx.ALIGN_RIGHT|wx.BORDER_NONE )
		self.m_static_level.Wrap( -1 )

		bSizer2.Add( self.m_static_level, 0, wx.ALL, 5 )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		self.m_textCtrt = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CHARWRAP|wx.TE_MULTILINE )
		self.m_textCtrt.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Courier" ) )

		bSizer5.Add( self.m_textCtrt, 1, wx.ALL|wx.EXPAND, 1 )

		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_static_label = wx.StaticText( self, wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_LEFT )
		self.m_static_label.Wrap( -1 )

		bSizer3.Add( self.m_static_label, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_button7 = wx.Button( self, wx.ID_ANY, u"<<<", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT|wx.BORDER_SUNKEN )
		bSizer3.Add( self.m_button7, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		m_choice_cryptoChoices = []
		self.m_choice_crypto = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice_cryptoChoices, 0 )
		self.m_choice_crypto.SetSelection( 0 )
		bSizer3.Add( self.m_choice_crypto, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_toggle_setting = wx.ToggleButton( self, wx.ID_ANY, u"Show Setting", wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE )
		bSizer3.Add( self.m_toggle_setting, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_button_encode = wx.Button( self, wx.ID_ANY, u"Encode", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT|wx.BORDER_SUNKEN )
		bSizer3.Add( self.m_button_encode, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_button_decode = wx.Button( self, wx.ID_ANY, u"Decode", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT|wx.BORDER_SUNKEN )
		bSizer3.Add( self.m_button_decode, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer3.Add( ( 0, 0), 0, wx.EXPAND, 5 )

		self.m_checkBox_hex = wx.CheckBox( self, wx.ID_ANY, u"Hex", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_checkBox_hex, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		m_choice_codecChoices = [ u"ASCII", u"UTF-8", u"GBK" ]
		self.m_choice_codec = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice_codecChoices, 0 )
		self.m_choice_codec.SetSelection( 0 )
		bSizer3.Add( self.m_choice_codec, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer3.Add( ( 0, 0), 0, wx.EXPAND, 5 )

		self.m_button_show = wx.Button( self, wx.ID_ANY, u"Show", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT|wx.BORDER_SUNKEN )
		bSizer3.Add( self.m_button_show, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_button6 = wx.Button( self, wx.ID_ANY, u"Hide", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT|wx.BORDER_SUNKEN )
		bSizer3.Add( self.m_button6, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_button_hide = wx.Button( self, wx.ID_ANY, u"Dismiss", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT|wx.BORDER_SUNKEN )
		bSizer3.Add( self.m_button_hide, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer5.Add( bSizer3, 0, wx.EXPAND, 1 )

		self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer5.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_panel_setting = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_NONE|wx.TAB_TRAVERSAL )
		self.m_panel_setting.Hide()

		wSizer3 = wx.WrapSizer( wx.HORIZONTAL, wx.REMOVE_LEADING_SPACES|wx.WRAPSIZER_DEFAULT_FLAGS )


		self.m_panel_setting.SetSizer( wSizer3 )
		self.m_panel_setting.Layout()
		wSizer3.Fit( self.m_panel_setting )
		bSizer5.Add( self.m_panel_setting, 0, wx.EXPAND |wx.ALL, 1 )


		bSizer2.Add( bSizer5, 1, wx.EXPAND, 1 )


		bSizer2.Add( ( 20, 0), 0, wx.EXPAND, 0 )


		self.SetSizer( bSizer2 )
		self.Layout()

		# Connect Events
		self.m_button7.Bind( wx.EVT_BUTTON, self.on_deattach )
		self.m_choice_crypto.Bind( wx.EVT_CHOICE, self.on_choice_module )
		self.m_toggle_setting.Bind( wx.EVT_TOGGLEBUTTON, self.on_show_setting )
		self.m_button_encode.Bind( wx.EVT_BUTTON, self.on_encode )
		self.m_button_decode.Bind( wx.EVT_BUTTON, self.on_decode )
		self.m_button_show.Bind( wx.EVT_BUTTON, self.on_shownode )
		self.m_button6.Bind( wx.EVT_BUTTON, self.on_hidenode )
		self.m_button_hide.Bind( wx.EVT_BUTTON, self.on_dismiss )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def on_deattach( self, event ):
		event.Skip()

	def on_choice_module( self, event ):
		event.Skip()

	def on_show_setting( self, event ):
		event.Skip()

	def on_encode( self, event ):
		event.Skip()

	def on_decode( self, event ):
		event.Skip()

	def on_shownode( self, event ):
		event.Skip()

	def on_hidenode( self, event ):
		event.Skip()

	def on_dismiss( self, event ):
		event.Skip()


###########################################################################
## Class SettingBlock
###########################################################################

class SettingBlock ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 169,51 ), style = wx.BORDER_NONE|wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer8 = wx.BoxSizer( wx.VERTICAL )

		self.m_static = wx.StaticText( self, wx.ID_ANY, u"name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_static.Wrap( -1 )

		bSizer8.Add( self.m_static, 0, wx.ALL, 1 )

		self.m_text = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_text.SetFont( wx.Font( 13, wx.FONTFAMILY_TELETYPE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Courier" ) )

		bSizer8.Add( self.m_text, 0, wx.ALL|wx.EXPAND, 1 )


		self.SetSizer( bSizer8 )
		self.Layout()

	def __del__( self ):
		pass


