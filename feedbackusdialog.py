#coding=utf-8
'''
Created on 2014年7月24日

@author: wangxun
'''
import os
from PySide import QtGui
from PySide import QtCore



class FeedbackusDidalog(QtGui.QDialog):
    def __init__(self, parent=None):
        super(FeedbackusDidalog, self).__init__(parent)

        self.setWindowTitle(self.tr("Feedback to us"))
        self.setWindowFlags(QtCore.Qt.WindowSystemMenuHint)

        self.resize(450, 290)


        self.name = QtGui.QLabel(self)
        self.name.setText(self.tr("Name:"))
        self.nameLineEdit = QtGui.QLineEdit(self)

        self.email = QtGui.QLabel(self)
        self.email.setText(self.tr("Email:"))

        self.emailLineEdit = QtGui.QLineEdit(self)

        self.telephone = QtGui.QLabel(self)
        self.telephone.setText(self.tr("Telephone:"))
        self.telephoneLineEdit = QtGui.QLineEdit(self)

        self.im = QtGui.QLabel(self)
        self.im.setText(self.tr("IM:"))

        self.imLineEdit = QtGui.QLineEdit(self)

        self.feedback = QtGui.QLabel(self)
        self.feedback.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.feedback.setText(self.tr("Feedback:"))
        self.feedbackTextEdit = QtGui.QTextEdit(self)
        self.feedbackTextEdit.setMaximumHeight(128)

        self.errorTipLable = QtGui.QLabel()
        self.errorTipLable.setObjectName("tip")
        self.errorTipLable.hide()

        self.okButton = QtGui.QPushButton(self.tr("OK"))
        self.cancelButton =  QtGui.QPushButton(self.tr("Cancel"))

        mainlayout = QtGui.QGridLayout()
        mainlayout.addWidget(self.name, 0, 0)
        mainlayout.addWidget(self.nameLineEdit, 0, 1)
        mainlayout.addWidget(self.email, 0, 2)
        mainlayout.addWidget(self.emailLineEdit, 0, 3)

        mainlayout.addWidget(self.telephone, 1, 0)
        mainlayout.addWidget(self.telephoneLineEdit, 1, 1)
        mainlayout.addWidget(self.im, 1, 2)
        mainlayout.addWidget(self.imLineEdit, 1, 3)

        mainlayout.addWidget(self.feedback, 2, 0)
        mainlayout.addWidget(self.feedbackTextEdit, 2, 1, 1, 3)

        mainlayout.addWidget(self.errorTipLable, 3, 1, 1, 3)

        okLayout = QtGui.QHBoxLayout()
        okLayout.addStretch()
        okLayout.addWidget(self.okButton)
        okLayout.addSpacing(75)
        okLayout.addWidget(self.cancelButton)
        okLayout.addSpacing(80)

        mainlayout.addLayout(okLayout, 4, 0, 1, 4)

        self.setLayout(mainlayout)
        self.okButton.clicked.connect(self.getFormData)
        
    def getFormData(self):

        name = self.nameLineEdit.text()
        email = self.emailLineEdit.text()
        telephone = self.telephoneLineEdit.text()
        im = self.imLineEdit.text()
        feedback = self.feedbackTextEdit.toPlainText().rstrip()
        if len(feedback) == 0:
            self.errorTipLable.setText(self.tr("Feedback is required."))
            self.errorTipLable.show()
        elif len(name) > 10:
            self.errorTipLable.setText(self.tr('The len of name should be less than "100".'))
            self.errorTipLable.show()
        elif len(email) > 10:
            self.errorTipLable.setText(self.tr('The len of email should be less than "100".'))
            self.errorTipLable.show()
        elif len(telephone) > 10:
            self.errorTipLable.setText(self.tr('The len of telephone should be less than "100".'))
            self.errorTipLable.show()
        elif len(im) > 10:
            self.errorTipLable.setText(self.tr('The len of im should be less than "100".'))
            self.errorTipLable.show()
        elif len(feedback) > 100:
            self.errorTipLable.setText(self.tr('The len of feedback should be less than "1000".'))
            self.errorTipLable.show()
        else:
            self.feedbackinfo = {
                "name": name,
                "email": email,
                "telephone": telephone,
                "im": im,
                "feedback": feedback
            }
            if len(feedback) == 0:
                self.errorTipLable.show()
            else:
                import threading
                t = threading.Thread(target=self.pushMsg, args=())  
                t.setDaemon(False)
                t.start()

                self.errorTipLable.setText(self.tr("Waiting..."))
                self.errorTipLable.show()

