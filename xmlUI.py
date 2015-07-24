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
import os

import exportxml





class toXmlUI(QtGui.QDialog):
    def __init__(self, parent=None):
        super(toXmlUI, self).__init__(parent)

        self.setWindowTitle(self.tr("To XML"))
        self.setWindowFlags(QtCore.Qt.WindowSystemMenuHint)

        self.resize(450, 290)

        self.execlname = QtGui.QLabel(self)
        self.execlname.setText(self.tr("File Name:"))
        self.execlnameLineEdit = QtGui.QLineEdit(self)  
        
        self.sheetname = QtGui.QLabel(self)
        self.sheetname.setText(self.tr("Sheet Name:"))
        self.sheetnameLineEdit = QtGui.QLineEdit(self) 
        
        
        self.output = QtGui.QLabel(self)
        self.output.setText(self.tr("Output folder:"))
        self.outputLineEdit = QtGui.QLineEdit(self) 
      
        self.savename = QtGui.QLabel(self)
        self.savename.setText(self.tr("XML Name:"))
        self.savenameLineEdit = QtGui.QLineEdit(self)   
        

        self.okButton = QtGui.QPushButton(self.tr("OK"))
        self.cancelButton =  QtGui.QPushButton(self.tr("Cancel"))








        self.errorTipLable = QtGui.QLabel()
        self.errorTipLable.setObjectName("tip")
        self.errorTipLable.hide()



        mainlayout = QtGui.QGridLayout()
        mainlayout.addWidget(self.execlname, 0, 0)
        mainlayout.addWidget(self.execlnameLineEdit, 0, 1)
        mainlayout.addWidget(self.sheetname, 1, 0)
        mainlayout.addWidget(self.sheetnameLineEdit, 1, 1)

        mainlayout.addWidget(self.output, 2, 0)
        mainlayout.addWidget(self.outputLineEdit, 2, 1)
        mainlayout.addWidget(self.savename, 3, 0)
        mainlayout.addWidget(self.savenameLineEdit, 3,1 )


        mainlayout.addWidget(self.errorTipLable, 4, 1)

        okLayout = QtGui.QHBoxLayout()
        okLayout.addStretch()
        okLayout.addWidget(self.okButton)
        okLayout.addSpacing(75)
        okLayout.addWidget(self.cancelButton)
        okLayout.addSpacing(80)

        mainlayout.addLayout(okLayout, 5, 0, 1, 4)

        self.setLayout(mainlayout)
        self.okButton.clicked.connect(self.getFormData)
        self.cancelButton.clicked.connect(self.reject)

        
    def getFormData(self):

        execlname = self.execlnameLineEdit.text()
        sheetname = self.sheetnameLineEdit.text()
        output = self.outputLineEdit.text()
        savename = self.savenameLineEdit.text()

        if len(execlname) == 0:
            self.errorTipLable.setText(self.tr("FileName is required."))
            self.errorTipLable.show()
        
        if len(sheetname) ==0:
            self.errorTipLable.setText(self.tr("SheetName is required."))
            self.errorTipLable.show()
        
        if len(output) ==0:
            self.errorTipLable.setText(self.tr("Output folder is required."))
            self.errorTipLable.show()    
            
        if len(savename) ==0:
            self.errorTipLable.setText(self.tr("XML Name is required."))
            self.errorTipLable.show()  
        
        if len(execlname) != 0 and len(sheetname) !=0 and len(output) !=0 and len(savename) !=0:
        
            if os.path.exists(execlname):
                try:     
                    sheets = exportxml.exceloperate(execlname).getSheetNames()   
                except:
                    self.errorTipLable.setText(self.tr("There is no sheets."))
                    print 3434
                
                if sheetname in sheets:
                    if os.path.exists(output):
                        aa =exportxml.changetoxml(execlname,sheetname,output,savename)
                        aa.run()
                        self.errorTipLable.setText(self.tr("succeful."))
                    else:
                        os.mkdir(output)
                        aa =exportxml.changetoxml(execlname,sheetname,output,savename)
                        aa.run()
                        self.errorTipLable.setText(self.tr("succeful."))
                else:
                    self.errorTipLable.setText(self.tr("The sheet name is not existed."))
        

            
            else:
                self.errorTipLable.setText(self.tr("The excel file is not existed."))
     

                        

        

class Example(QtGui.QMainWindow, Ui_Dialog):    
    def __init__(self):
        super(Example, self).__init__()        
        self.initUI()
        
    def initUI(self):        

        self.statusBar().showMessage('statusbar:Ready')
        menubar = self.menuBar()
        toolMenu = menubar.addMenu('&Tool')
        helpmenu = menubar.addMenu('&Help')
        toXmlAction = self.createAction('&ToXml', self.toXml)
        aboutUsAction = self.createAction(u'&关于我们',self.test)
        helpmenu.addAction(aboutUsAction)
        toolMenu.addAction(toXmlAction)
             
        self.setGeometry(300, 300, 500, 350)
        self.setWindowTitle('Test Tools')            
        self.show()

    def test(self):
        self.statusBar().showMessage('You have created a new file!',9000)   


    def toXml(self):
        dialog = toXmlUI()
        dialog.exec_()
          

    

        
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
