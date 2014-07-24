
import sys
from PySide.QtGui import *
from wenjian import Ui_Dialog


def PrintHello():
    print("Hello")


# Make main window class
class MainWindow(QMainWindow,Ui_Dialog):
    def __init__(self, parent=None):
        super(MainWindow,self).__init__(parent)
        self.setupUi(self)
        # Connect button click event to PrintHello function
        self.pushButton.clicked.connect(self.load)
        self.pushButton_2.clicked.connect(self.save)
    
    def load(self):
        print 'open'
        print self.lineEdit.text()
        try:
            file = open(self.lineEdit.text())

            self.textEdit.setText(file.read())
            file.close()
        except:
            print 'pass'
    def save(self):
        print 'save'
        print self.textEdit.toPlainText()
        file = open(self.lineEdit.text(), 'w')
        file.write(self.textEdit.toPlainText())
        file.close()

# End of main window class


# Main Function
if __name__=='__main__':
    Program = QApplication(sys.argv)
    Window=MainWindow()
    Window.show()
    Program.exec_()
