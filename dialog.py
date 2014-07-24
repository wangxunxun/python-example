#coding=utf-8

'''
Created on 2014-7-24

@author: xun
'''
import sys
from PySide import QtGui,QtCore
from PySide.QtCore import *
from PySide.QtGui import *

class GridLayout2(QtGui.QDialog):
    def __init__(self,parent=None):
        QtGui.QDialog.__init__(self,parent)
        

        self.setWindowTitle('grid layout2')
 
        title = QtGui.QLabel('Tltle')
        author = QtGui.QLabel('Author')
        review = QtGui.QLabel('Review')
 
        titleEdit = QtGui.QLineEdit()
        authorEdit = QtGui.QLineEdit()
        reviewEdit = QtGui.QTextEdit()
 
        grid = QtGui.QGridLayout()
        grid.setSpacing(10)
 
        grid.addWidget(title,1,0)
        grid.addWidget(titleEdit,1,1)
 
        grid.addWidget(author,2,0)
        grid.addWidget(authorEdit,2,1)
 
        grid.addWidget(review,3,0)
        grid.addWidget(reviewEdit,3,1,5,1)
 
        self.setLayout(grid)
        self.resize(350,300)
        
        

class FontPropertiesDlg(QDialog):
 
    def __init__(self,parent=None):
        super(FontPropertiesDlg, self).__init__(parent)


        FontStyleLabel = QLabel(u"中文字体:")
        self.FontstyleComboBox = QComboBox()
        self.FontstyleComboBox.addItems([u"宋体",u"黑体", u"仿宋", u"隶书", u"楷体"])
        self.FontEffectCheckBox =QCheckBox(u"使用特效")
        FontSizeLabel = QLabel(u"字体大小")
        self.FontSizeSpinBox = QSpinBox()
        self.FontSizeSpinBox.setRange(1, 90)
        okButton = QPushButton(u"确定")
        cancelButton = QPushButton(u"取消")
 
        buttonLayout = QHBoxLayout()
        buttonLayout.addStretch()
        buttonLayout.addWidget(okButton)
        buttonLayout.addWidget(cancelButton)
        layout = QGridLayout()
        layout.addWidget(FontStyleLabel, 0, 0)
        layout.addWidget(self.FontstyleComboBox, 0, 1)
        layout.addWidget(FontSizeLabel, 1, 0)
        layout.addWidget(self.FontSizeSpinBox, 1, 1)
        layout.addWidget(self.FontEffectCheckBox,1,2)
        layout.addLayout(buttonLayout, 2, 0)
        self.setLayout(layout)
 
        self.connect(okButton,SIGNAL("clicked()"),self,SLOT("accept()"))
        self.connect(cancelButton,SIGNAL("clicked()"),self,SLOT("reject()"))
        self.setWindowTitle(u"字体")
        
        
class FontPropertiesDlg1(QDialog):
 
    changed = QtCore.Signal(str) 
    def __init__(self,format,parent=None):
        super(FontPropertiesDlg1, self).__init__(parent)
        self.format=format
        
        FontStyleLabel = QLabel(u"中文字体:")
        self.FontstyleComboBox = QComboBox()
        self.FontstyleComboBox.addItems([u"宋体", u"黑体", u"仿宋",
                                     u"隶书", u"楷体"])
        self.FontEffectCheckBox =QCheckBox(u"使用特效")
        FontSizeLabel = QLabel(u"字体大小")
        self.FontSizeSpinBox = QSpinBox()
        self.FontSizeSpinBox.setRange(1, 90)
        applyButton = QPushButton(u"应用")
        cancelButton = QPushButton(u"取消")
 
        buttonLayout = QHBoxLayout()
        buttonLayout.addStretch()
        buttonLayout.addWidget(applyButton)
        buttonLayout.addWidget(cancelButton)
        
        layout = QGridLayout()
        layout.addWidget(FontStyleLabel, 0, 0)
        layout.addWidget(self.FontstyleComboBox, 0, 1)
        layout.addWidget(FontSizeLabel, 1, 0)
        layout.addWidget(self.FontSizeSpinBox, 1, 1)
        layout.addWidget(self.FontEffectCheckBox,1,2)
        layout.addLayout(buttonLayout, 2, 0)
        self.setLayout(layout)
 
        self.connect(applyButton,SIGNAL("clicked()"),self.apply) 
        self.connect(cancelButton,SIGNAL("clicked()"),self,SLOT("reject()"))
        self.setWindowTitle(u"字体")
 
    def apply(self):
        self.format["fontstyle"] = unicode(self.FontstyleComboBox.currentText())
        self.format["fontsize"] = self.FontSizeSpinBox.value()
        self.format["fonteffect"] = self.FontEffectCheckBox.isChecked()

        self.changed.emit(self.format)

 
class MainDialog(QDialog):
    def __init__(self,parent=None):
        super(MainDialog,self).__init__(parent)

        
        self.FontPropertiesDlg=None

        self.format = dict(fontstyle=u'宋体', fontsize=1, fonteffect=False)
        
        FontButton1 = QPushButton(u"设置字体(模态)")
        FontButton2 = QPushButton(u"设置字体(非模态)")
        self.label = QLabel(u"默认选择")
        
        layout = QGridLayout()
        layout.addWidget(FontButton1,0,0)
        layout.addWidget(FontButton2,0,1)
        layout.addWidget(self.label)
        self.setLayout(layout)
        
        self.connect(FontButton1,SIGNAL("clicked()"),self.FontModalDialog)        
        self.connect(FontButton2,SIGNAL("clicked()"),self.FontModalessDialog)
 
        self.setWindowTitle(u"模态和非模态对话框")
        self.updataData()
 
    def updataData(self,):
        self.label.setText(u"选择的字体：%s<br>字体大小：%d<br>是否特效：%s" %(self.format["fontstyle"],self.format["fontsize"],self.format["fonteffect"]))
    
    def FontModalDialog(self):
        dialog = FontPropertiesDlg(self)
        if dialog.exec_():
            self.format["fontstyle"] = unicode(dialog.FontstyleComboBox.currentText())
            self.format["fontsize"] = dialog.FontSizeSpinBox.value()
            self.format["fonteffect"] = dialog.FontEffectCheckBox.isChecked()
            self.updataData()
    


    def FontModalessDialog(self):
        dialog = FontPropertiesDlg1(self.format,self)
        
#        self.connect(dialog,SIGNAL("changed"), self.updataData)
        dialog.changed.connect(self.updataData)
        dialog.show()
        
        
        
class feedbacktous(QDialog):
    def __init__(self,parent=None):
        super(feedbacktous,self).__init__(parent)
        

        self.setWindowTitle('Feed Back to Us')
        
        okbutton = QtGui.QPushButton('OK')
        cancelbutton = QtGui.QPushButton('Cancel')
        
        name = QtGui.QLabel('Name:')
        emai = QtGui.QLabel('Email:')
        telephone = QtGui.QLabel('Telephone:')
        im = QtGui.QLabel('IM:')
        feedback = QtGui.QLabel('Feedback:')
        
        nameedit = QtGui.QLineEdit()
        emaiedit = QtGui.QLineEdit()
        telephoneedit = QtGui.QLineEdit()
        imedit = QtGui.QLineEdit()
        feedbackedit = QtGui.QTextEdit()
        
        
        buttonlayout = QtGui.QHBoxLayout()
        buttonlayout.addWidget(okbutton)
        buttonlayout.addWidget(cancelbutton)
        buttonlayout.addStretch()
        
        layout = QtGui.QGridLayout()
        layout.addWidget(name, 0, 0)
        layout.addWidget(nameedit, 0, 1)
        layout.addWidget(emai, 0, 2)
        layout.addWidget(emaiedit, 0, 3)
        layout.addWidget(telephone, 1, 0)
        layout.addWidget(telephoneedit, 1, 1)
        layout.addWidget(im, 1, 2)
        layout.addWidget(imedit, 1, 3)
        layout.addWidget(feedback, 2, 0)
        layout.addWidget(feedbackedit, 2, 1, 3, 3)
        layout.addLayout(buttonlayout, 6, 1, 1, 3)
        self.setLayout(layout)

class setproxy(QDialog):
    def __init__(self,parent=None):
        super(setproxy,self).__init__(parent)
    
    
    

        self.setWindowTitle('Set Proxy')
        
        okbutton = QtGui.QPushButton('OK')
        cancelbutton = QtGui.QPushButton('Cancel')
        
        useproxy = QtGui.QLabel('Use Proxy:')
        host = QtGui.QLabel('Host:')
        port = QtGui.QLabel('Port:')
        user = QtGui.QLabel('User:')
        password = QtGui.QLabel('PassWord:')
        
        hostedit = QtGui.QLineEdit()
        portedit = QtGui.QLineEdit()
        useredit = QtGui.QLineEdit()
        passwordedit = QtGui.QLineEdit()
        
        useproxycheckbox = QtGui.QCheckBox()
        
        buttonlayout = QtGui.QHBoxLayout()
        buttonlayout.addStretch()
        buttonlayout.addWidget(okbutton)
        buttonlayout.addWidget(cancelbutton)

        
        layout = QtGui.QGridLayout()
        layout.addWidget(useproxy, 0, 0)
        layout.addWidget(useproxycheckbox, 0, 1)
        layout.addWidget(host, 1, 0)
        layout.addWidget(hostedit, 1, 1)
        layout.addWidget(port, 2, 0)
        layout.addWidget(portedit, 2, 1)
        layout.addWidget(user, 3, 0)
        layout.addWidget(useredit, 3, 1)
        layout.addWidget(password, 4, 0)
        layout.addWidget(passwordedit, 4, 1)
        layout.addLayout(buttonlayout, 5, 0, 1, 2)
        self.setLayout(layout) 
        
class help(QDialog):
    def __init__(self,parent = None):
        super(help,self).__init__(parent)
        


        self.resize(400, 300)
        self.setWindowTitle('Help')
        FontStyleLabel = QtGui.QLabel(u"zhongwensongti")
        FontstyleComboBox = QtGui.QComboBox()
        FontstyleComboBox.addItems([u"songti", u"heiti", u"fangsong",
                                     u"lishu", u"kaiti"])
        FontSizeLabel = QtGui.QLabel(u"zitidaxiao")
        FontSizeSpinBox = QtGui.QSpinBox()
        FontSizeSpinBox.setRange(0, 90)
        FontEffectCheckBox =QtGui.QCheckBox(u"shiyongtexiao")
        okButton = QtGui.QPushButton(u"queding")
        cancelButton = QtGui.QPushButton(u"quxiao")

        buttonLayout = QtGui.QHBoxLayout()
        buttonLayout.addStretch()
        buttonLayout.addWidget(okButton)
        buttonLayout.addWidget(cancelButton)
        layout = QtGui.QGridLayout()
        layout.addWidget(FontStyleLabel, 0, 0)
        layout.addWidget(FontstyleComboBox, 0, 1)
        layout.addWidget(FontSizeLabel, 1, 0)
        layout.addWidget(FontSizeSpinBox, 1, 1)
        layout.addWidget(FontEffectCheckBox,1,2)
        layout.addLayout(buttonLayout, 2, 0,1,3)
        self.setLayout(layout)  
        
class calculator(QDialog): 
    def __init__(self,parent = None):
        super(calculator,self).__init__(parent)
        self.resize(400, 300)
        self.setWindowTitle('calculator')
        
        grid = QtGui.QGridLayout()
        self.setLayout(grid)
        
 
        names = ['Cls', 'Bck', '', 'Close',
                 '7', '8', '9', '/',
                '4', '5', '6', '*',
                 '1', '2', '3', '-',
                '0', '.', '=', '+']
        
        positions = [(i,j) for i in range(5) for j in range(4)]
        
        for position, name in zip(positions, names):
            
            if name == '':
                continue
            button = QtGui.QPushButton(name)
            grid.addWidget(button, *position)
 
