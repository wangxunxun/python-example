'''
Created on 2014-7-30

@author: xun
'''
# -*- coding: utf-8 -*-
#=============================================================================
# Copyright (c) 2013, Ford Motor Company All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# Redistributions of source code must retain the above copyright notice, this
# list of conditions and the following disclaimer. Redistributions in binary
# form must reproduce the above copyright notice, this list of conditions and
# the following disclaimer in the documentation and/or other materials provided
# with the distribution. Neither the name of the Ford Motor Company nor the
# names of its contributors may be used to endorse or promote products derived
# from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#=============================================================================

import sys
from PySide import QtGui
from PySide import QtCore
from PySide.QtGui import QMainWindow



class MenuBar(QtGui.QMenuBar):

    def __init__(self, parent = None):
        super(MenuBar, self).__init__()
        self.parent = parent
        self.menusettings = self.buildMenu()
        self.actions = {}
        self.creatMenus(self.menusettings)
        getattr(self, "MFD4Action").setChecked(True)

    def buildMenu(self):
        menu = {
            'visual': True,
            'menus': [
                {
                    'name': self.tr('File'),
                    'trigger': 'File',
                    'actions': [
                        {
                            'name': self.tr('New Project'),
                            'icon': u'',
                            'shortcut': u'',
                            'trigger': 'NewProject',
                        },
                        {
                            'name': self.tr('Open Project'),
                            'icon': u'',
                            'shortcut': u'',
                            'trigger': 'OpenProject',
                        },
                        {
                            'name': self.tr('Save Project AS...'),
                            'icon': u'',
                            'shortcut': u'',
                            'trigger': 'SaveProjectAs',
                        },
                        {
                            'name': self.tr('Exit'),
                            'icon': u'',
                            'shortcut': u'',
                            'trigger': 'Exit',
                        },
                    ]
                },
                {
                    'name': self.tr('Screen'),
                    'trigger': 'Screen',
                    'actions': [
                        {
                            'name': self.tr('MFD3'),

                            'icon': u'',
                            'shortcut': u'',
                            'trigger': 'MFD3',
                            "checkable": True
                        },
                        {
                            'name': self.tr('MFD4'),
                            'icon': u'',
                            'shortcut': u'',
                            'trigger': 'MFD4',
                            "checkable": True
                        },
                    ]
                },
                {
                    'name': self.tr(' Help '),
                    'trigger': 'Help',
                    'actions': [
                        {
                            'name': self.tr('About SyncDesignTool'),
                            'icon': u'',
                            'shortcut': u'',
                            'trigger': 'About',
                        },
                        {
                            'name': self.tr('Ford developer center'),
                            'icon': u'',
                            'shortcut': u'',
                            'trigger': 'FordDeveloper',
                        },
                        {
                            'name': self.tr('Feedback to us'),
                            'icon': u'',
                            'shortcut': u'',
                            'trigger': 'Feedbackus',
                        },
                    ]
                }
            ]
        }
        return menu

    def creatMenus(self, menusettings):
        self.setVisible(menusettings['visual'])
        for menu in menusettings['menus']:
            setattr(
                self,
                '%smenu' % menu['trigger'],
                self.addMenu(u'%s' % menu['name'])
            )
            submenu = getattr(self, '%smenu' % menu['trigger'])
            for menuaction in menu['actions']:
                if 'type' in menuaction and menuaction['type'] == "submenu":
                    self.createSubAction(menu['trigger'], menuaction)
                else:
                    self.creatAction(submenu, menuaction)

    def createSubAction(self, pmenu_name, menu):
        childmenu = getattr(self, '%smenu' % pmenu_name)
        submenu = childmenu.addMenu(u'%s' % menu['name'])
        setattr(
            self,
            '%smenu' % menu['trigger'],
            submenu)
        for menuaction in menu['actions']:
            self.creatAction(submenu, menuaction)

    def creatAction(self, submenu, menuaction):
        if 'checkable' in menuaction:
            setattr(
                self,
                '%sAction' % menuaction['trigger'],
                QtGui.QAction(
                    QtGui.QIcon(QtGui.QPixmap(menuaction['icon'])),
                    u'%s' % menuaction['name'],
                    self,
                    checkable=menuaction['checkable']
                )
            )
        else:
            setattr(
                self,
                '%sAction' % menuaction['trigger'],
                QtGui.QAction(
                    QtGui.QIcon(QtGui.QPixmap(menuaction['icon'])),
                    u'%s' % menuaction['name'],
                    self,
                )
            )

        action = getattr(self, '%sAction' % menuaction['trigger'])
        action.setShortcut(QtGui.QKeySequence(menuaction['shortcut']))
        submenu.addAction(action)

        self.actions.update({menuaction['trigger']: action})
        
        
if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)
    mainWin = QMainWindow()
    
    a = MenuBar()
    
    mainWin.setMenuBar(a) 


    mainWin.setGeometry(300, 300, 500, 350)
    mainWin.show()
    sys.exit(app.exec_())
