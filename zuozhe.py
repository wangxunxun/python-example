#coding=utf-8
'''
Created on 2014年7月23日

@author: wangxun
'''
import sys

from PySide import QtGui,QtCore
from PySide.QtCore import *
from PySide.QtGui import *                 
 
class MainWindow(QMainWindow):
    def __init__(self,parent=None):
        super(MainWindow,self).__init__(parent)
 
        fileNewAction=QAction(QIcon("./images/filenew.png"),"&New",self)
        fileNewAction.setShortcut(QKeySequence.New)
        helpText = "Create a new file"

        fileNewAction.setStatusTip(helpText)
        self.connect(fileNewAction,SIGNAL("triggered()"),self.fileNew)
 
        self.fileMenu = self.menuBar().addMenu("&File")
        self.fileMenu.addAction(fileNewAction)
 
        filetoolbar = self.addToolBar("&File")
        filetoolbar.addAction(fileNewAction)
            
        self.status = self.statusBar()
        self.status.showMessage("This is StatusBar",5000)
        self.setWindowTitle("PyQt MianWindow")
      
    def fileNew(self):
        self.status.showMessage("You have created a new file!",9000)
def main():
    app = QApplication(sys.argv)
    app.setApplicationName("PyQt MianWindow")
    app.setWindowIcon(QIcon("./images/icon.png"))
    form = MainWindow()
    form.show()
    app.exec_()
 
main()