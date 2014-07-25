#coding=utf-8

import os
from PySide import QtGui 
from PySide import QtCore





version = "2.4"

class AboutDialog(QtGui.QDialog):

    style = '''
        QDialog{
            background-color: rgb(59,67,81);
            color: white;
        }

        QLabel{
            color: white;
        }
        QPushButton {
            height: 46px;
            width: 102px;
            color:white;
            font-size: 14px;
            font-family: "Verdana";
            border-image: url(gui/skin/PNG/button_up.png);
        }

        QPushButton:pressed {
            border-image: url(gui/skin/PNG/button_down.png);
        }
    '''

    title = '''
    AppLink Emulator (ALE) 2.4'''

    copyright = u'''
    © Copyright 2013--2014, Ford Motor Company'''

    contentText = '''
    The ALE application is a software emulator of
    the in-vehicle Applink device.It supports most
    of the Applink 1.0 & 2.0 protocols and provides
    the support for Applink protocol development. 
    But it is not intended to replace the necessary 
    testing within the real in-vehicle device.
    '''

    extensionText = '''
    Created with the Python, Pyside and QT.\n
        Python 2.7.5
            www.python.org\n
        Pyside 1.2.1 (LGPL License)
            www.pyside.org\n
        QT 4.8.5 (LGPL License)
             www.qt-project.org\n
        version %s
    '''% version

    def __init__(self, parent=None):
        super(AboutDialog, self).__init__(parent)
        self.setWindowTitle(self.tr("About ALE"))
        self.setWindowFlags(QtCore.Qt.WindowSystemMenuHint)

        titleLabel = QtGui.QLabel(self.title)
        copyrightLabel = QtGui.QLabel(self.copyright)
        contentTextLabel = QtGui.QLabel(self.contentText)
        self.extensionTextLabel = QtGui.QLabel(self.extensionText)
        self.licenseButton = QtGui.QPushButton(self.tr("License"))

        
        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(titleLabel)
        mainLayout.addWidget(copyrightLabel)
        mainLayout.addWidget(contentTextLabel)
        mainLayout.addWidget(self.licenseButton)
        mainLayout.addWidget(self.extensionTextLabel)
        mainLayout.setSizeConstraint(QtGui.QLayout.SetFixedSize)

        self.extensionTextLabel.hide()
        self.licenseButton.clicked.connect(self.showlicence)

        self.okButton = QtGui.QPushButton(self.tr("OK"))

        okButtonLayout = QtGui.QHBoxLayout() 
        okButtonLayout.addStretch() 
        okButtonLayout.addWidget(self.okButton)

        mainLayout.addLayout(okButtonLayout)
        self.setLayout(mainLayout)
        
        self.setStyleSheet(self.style)

        self.okButton.clicked.connect(self.close)

    def showlicence(self):
        if self.extensionTextLabel.isVisible():
            self.extensionTextLabel.hide()
#            self.changeLicenseButtonIcon("up")
        else:
            self.extensionTextLabel.show()
#            self.changeLicenseButtonIcon("down")

    def changeLicenseButtonIcon(self, flag="up"):
        if flag == "up":
            self.licenseButton.up = QtGui.QIcon(self.licenseButton.pixmap_up)
            self.licenseButton.down = QtGui.QIcon(self.licenseButton.pixmap_up)
            self.licenseButton.setIcon(self.licenseButton.up)
        else:
            self.licenseButton.up = QtGui.QIcon(self.licenseButton.pixmap_down)
            self.licenseButton.down = QtGui.QIcon(self.licenseButton.pixmap_down)
            self.licenseButton.setIcon(self.licenseButton.down)
