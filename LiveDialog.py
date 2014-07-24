#coding=utf-8
 
import sys
from PySide.QtCore import *
from PySide.QtGui import *
 
class FontPropertiesDlg(QDialog):
 
    def __init__(self,format,callback,parent=None):
        super(FontPropertiesDlg, self).__init__(parent)
                                
        self.format = format
        self.callback = callback
       
        FontStyleLabel = QLabel(u"中文字体:")
        self.FontstyleComboBox = QComboBox()
        self.FontstyleComboBox.addItems([u"宋体", u"黑体", u"仿宋",
                                     u"隶书", u"楷体"])
        self.FontEffectCheckBox =QCheckBox(u"使用特效")
        FontSizeLabel = QLabel(u"字体大小")
        self.FontSizeSpinBox = QSpinBox()
        self.FontSizeSpinBox.setRange(1, 90)
            
        layout = QGridLayout()
        layout.addWidget(FontStyleLabel, 0, 0)
        layout.addWidget(self.FontstyleComboBox, 0, 1)
        layout.addWidget(FontSizeLabel, 1, 0)
        layout.addWidget(self.FontSizeSpinBox, 1, 1)
        layout.addWidget(self.FontEffectCheckBox,1,2)
        self.setLayout(layout)
 
        self.connect(self.FontstyleComboBox,SIGNAL("itemSelected"),self.apply)
        self.connect(self.FontEffectCheckBox,SIGNAL("toggled(bool)"), self.apply)
        self.connect(self.FontSizeSpinBox,SIGNAL("valueChanged(int)"), self.apply)
        self.setWindowTitle(u"字体")
 
    def apply(self):
        self.format["fontstyle"] = unicode(self.FontstyleComboBox.currentText())
        self.format["fontsize"] = self.FontSizeSpinBox.value()
        self.format["fonteffect"] = self.FontEffectCheckBox.isChecked()
        self.callback()