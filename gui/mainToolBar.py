#===============================================================================
# Copyright (C) 2010 Diego Duclos
#
# This file is part of pyfa.
#
# pyfa is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pyfa is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with pyfa.  If not, see <http://www.gnu.org/licenses/>.
#===============================================================================

import wx
from gui import bitmapLoader
import gui.mainFrame

class MainToolBar(wx.ToolBar):
    def __init__(self, parent):
        style = wx.TB_HORIZONTAL | wx.NO_BORDER | wx.TB_FLAT
        wx.ToolBar.__init__(self, parent, wx.ID_ANY, style=style)

        self.AddCheckLabelTool(10, "Ship Browser", bitmapLoader.getBitmap("ship_big", "icons"), shortHelp="Ship browser")
        self.AddCheckLabelTool(20, "Character Editor", bitmapLoader.getBitmap("character_big", "icons"), shortHelp="Character editor")

        self.Bind(wx.EVT_TOOL, self.toggleShipBrowser, id=10)
        self.Bind(wx.EVT_TOOL, self.toggleCharacterBrowser, id=20)
        self.Realize()

        gui.mainFrame.MainFrame.getInstance().shipBrowser.Hide()

    def toggleShipBrowser(self, event):
        newState = self.GetToolState(10)
        mainFrame = gui.mainFrame.MainFrame.getInstance()


        if newState:
            mainFrame.shipBrowser.build()
            mainFrame.marketShipBrowserSizer.Detach(mainFrame.marketBrowser)
            mainFrame.marketShipBrowserSizer.Add(mainFrame.shipBrowser, 1, wx.EXPAND)
        else:
            mainFrame.marketShipBrowserSizer.Detach(mainFrame.shipBrowser)
            mainFrame.marketShipBrowserSizer.Add(mainFrame.marketBrowser, 1, wx.EXPAND)

        mainFrame.shipBrowser.Show(newState)
        mainFrame.marketBrowser.Show(not newState)
        mainFrame.marketShipBrowserSizer.Layout()

    def toggleCharacterBrowser(self, event):
        print event
