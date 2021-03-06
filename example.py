#coding=utf-8

'''
Created on 2014-7-23

@author: xun
'''

import sys

from PySide import QtGui,QtCore
from PySide.QtCore import *
from PySide.QtGui import *

from dialog import *
from findandreplace import *
import findandreplace
import feedbackusdialog
import aboutdialog








##试试

class Example(QtGui.QMainWindow, Ui_Dialog):    
    def __init__(self):
        super(Example, self).__init__()        
        self.initUI()
        
    def initUI(self):        

        self.statusBar().showMessage('statusbar:Ready')



        exitAction = self.createAction('&New', self.exit, 'Ctrl+N')
        findandreplace = self.createAction('findandreplace', self.findandreplace)
        
        
        setproxy = QtGui.QAction('setproxy', self)
        setproxy.triggered.connect(self.setproxy)
        
        feedbacktous = QtGui.QAction('feedback', self)
        feedbacktous.triggered.connect(self.feedbacktous)
        
        feedbacktous1 = self.createAction('feedbacktus1', self.feedbacktous1)
        aboutdialog = self.createAction('about', self.aboutdialog)
        
        pretest = QtGui.QAction('pretest', self)
        pretest.setStatusTip('ziti')
        pretest.triggered.connect(self.ziti)
        
        zuozhe = QtGui.QAction('zuozhe', self)
        zuozhe.setStatusTip('zuozhe')
        zuozhe.triggered.connect(self.zuozhe)
                
        help = QtGui.QAction('help', self)
        help.setStatusTip('help')
        help.triggered.connect(self.help)
                
        calculator = QtGui.QAction('calculator', self)
        calculator.setStatusTip('calculator')
        calculator.triggered.connect(self.calculator)
        
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        testmenu = menubar.addMenu('&Test')
        helpmenu = menubar.addMenu('&Help')
        
        fileMenu.addAction(exitAction)
        fileMenu.addAction(setproxy)
        fileMenu.addAction(feedbacktous)
        fileMenu.addAction(findandreplace)
        fileMenu.addAction(feedbacktous1)
        
        testmenu.addAction(pretest)
        testmenu.addAction(zuozhe)
                
        helpmenu.addAction(help)
        helpmenu.addAction(calculator)
        helpmenu.addAction(aboutdialog)
        
        filetoolbar = self.addToolBar("file")
        filetoolbar.addAction(exitAction)
        
        
                
        self.setGeometry(300, 300, 500, 350)
        self.setWindowTitle('Icon')            
        self.show()
    
    def closeEvent(self, event):        
        reply = QtGui.QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QtGui.QMessageBox.Yes | 
            QtGui.QMessageBox.No, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()  
            
    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())       
        
    def calculator(self):
        testdialog = calculator()            
        testdialog.exec_()        

    def help(self, parent=None):
        testdialog = help()  
        testdialog.exec_()

    def setproxy(self):
        dialog = setproxy()
        dialog.exec_()
        
    def feedbacktous(self):
        dialog = feedbacktous()
        dialog.exec_()
        
    def feedbacktous1(self):
        dialog = feedbackusdialog.FeedbackusDidalog()
        dialog.exec_()
        
    def aboutdialog(self):
        dialog = aboutdialog.AboutDialog()
        dialog.exec_()
        
    def ziti(self):
        font= MainDialog()
        font.exec_()
        
    def zuozhe(self):
        z = GridLayout2()
        z.exec_()
        
    def exit(self):
        self.statusBar().showMessage('You have created a new file!',9000)
        
    def findandreplace(self):
        a = QDialog()
        b=Ui_Dialog()
        b.setupUi(a)

        a.exec_()
        
    def createAction(self,text,slot=None,shortcut=None, icon=None,
               tip=None,checkable=False,signal="triggered()"):
        action = QAction(text, self)
        if icon is not None:
            action.setIcon(QIcon("./images/%s.png" % icon))
        if shortcut is not None:
            action.setShortcut(shortcut)
        if tip is not None:
            action.setToolTip(tip)
            action.setStatusTip(tip)
        if slot is not None:
            self.connect(action, SIGNAL(signal), slot)
        if checkable:
            action.setCheckable(True)
        return action
        

        
        
        

        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()   
