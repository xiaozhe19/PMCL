import sys
from PyQt5.QtWidgets import QApplication ,QMainWindow
from PyQt5.QtCore import Qt

from ui2 import *

class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyMainWindow,self)
        self.setupUi(self)

if __name__ == "__main__":
  app = QtWidgets.QApplication(sys.argv) 
  MainWindow = QtWidgets.QMainWindow()  
  ui = Ui_MainWindow()          
  ui.setupUi(MainWindow)         
  MainWindow.show()            
  sys.exit(app.exec_()) 
  
       
           