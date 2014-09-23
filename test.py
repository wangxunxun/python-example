#!/usr/bin/python
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

import os
import sys
from PySide import QtGui
from PySide import QtCore


        
class FLineEdit(QtGui.QLineEdit):

    def __init__(self, text=None, parant=None):
        super(FLineEdit, self).__init__(text, parant)
        self.setObjectName("tooledit")
        # self.textChanged.connect(changeSaveFlag)       
        
class test1(QtGui.QFrame):
    def __init__(self, parent=None):
        super(test1, self).__init__(parent)
        self.initBaseUI()
        
    def initBaseUI(self):
        self.nameLabel = QtGui.QLabel(self.tr("Name:"))
        self.nameLabel.setFixedWidth(78)
        self.nameLineEdit = FLineEdit()
        self.nameLineEdit.setPlaceholderText(self.tr("Please input rpc name."))
        self.nameLineEdit.setFixedHeight(30)

        self.saveButton = QtGui.QPushButton(self.tr(""))
        self.saveButton.setObjectName("ToolButton_Save")
        self.saveButton.setFixedSize(38, 38)
        self.saveButton.setToolTip(self.tr("Save rpc"))

        nameLayout = QtGui.QHBoxLayout()
        nameLayout.addWidget(self.nameLabel)
        nameLayout.addWidget(self.nameLineEdit)
        nameLayout.addWidget(self.saveButton)
        nameLayout.setContentsMargins(19, 0, 5, 0)
        nameLayout.setSpacing(5)

        self.descriptionLabel = QtGui.QLabel(self.tr("Description:"))
        self.descriptionLabel.setFixedWidth(90)
        self.descriptionTextEdit = QtGui.QTextEdit()
        self.descriptionTextEdit.setObjectName("Description")
        self.descriptionTextEdit.setFixedHeight(60)
        infoLayout = QtGui.QHBoxLayout()

        infoLayout.addWidget(self.descriptionLabel)
        infoLayout.addWidget(self.descriptionTextEdit)
        infoLayout.setContentsMargins(15, 5, 5, 0)
        infoLayout.setSpacing(0)

        blankLine = QtGui.QLabel()
        blankLine.setObjectName("blankLine")
        blankLine.setFixedHeight(2)

        self.mainLayout = QtGui.QVBoxLayout()
        self.mainLayout.addLayout(nameLayout)
        self.mainLayout.addLayout(infoLayout)
        self.mainLayout.addWidget(blankLine)
        self.setLayout(self.mainLayout)

class test2(QtGui.QWidget):
    def __init__(self, parent=None):
        super(test2, self).__init__(parent)
        self.initBaseUI()
    def initBaseUI(self):
        self.nameLabel = QtGui.QLabel(self.tr("Name1111:"))
        self.nameLabel.setFixedWidth(77)
        self.lineedit = QtGui.QLineEdit()
        self.lineedit.setFixedHeight(30)
        
        
        layout = QtGui.QHBoxLayout()
        layout.addWidget(self.nameLabel)
        layout.addWidget(self.lineedit)
        self.setLayout(layout)

class CenterWindow(QtGui.QWidget):

    viewID = "CenterWindow"


    def __init__(self, parent=None):
        super(CenterWindow, self).__init__(parent)
        self.parent = parent
        self.setObjectName("CenterWindow")
        self.initUI()

    def initUI(self):
        a = test1()
        b = test2()
        layout = QtGui.QVBoxLayout()
        layout.addWidget(a)
        layout.addWidget(b)
        self.setLayout(layout)


class MainWindow(QtGui.QMainWindow):

    viewID = "MainWindow"


    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setObjectName("Mainwindow")
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

        self.initUI()

    def initUI(self):


        self.setWindowTitle('__softwarename__')
        self.setFixedSize(800 + 28, 700)
        centerwindow = CenterWindow(self)
        self.setCentralWidget(centerwindow)


        vlayout = QtGui.QVBoxLayout()


        vlayout.addStretch()
        vlayout.setContentsMargins(0, 0, 0, 0)
        vlayout.setSpacing(0)




        



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    main = MainWindow()


    main.show()
    exitflag = app.exec_()
    sys.exit(exitflag)

