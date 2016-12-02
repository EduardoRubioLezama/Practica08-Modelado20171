#*-* encoding: utf-8 *-*
import sys
from PyQt4 import QtGui, QtCore, uic

class Cliente(QtGui.QMainWindow):

    def __init__(self):
        super (Cliente,self).__init__()
        uic.loadUi("Cliente.ui",self)
        self.ajustaTabla()
        self.show()

    def ajustaTabla(self):
        
        self.tableWidget.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        self.tableWidget.verticalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setStretchLastSection(True)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv) 
    cliente = Cliente() 
    sys.exit(app.exec_())         