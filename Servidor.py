#*-* encoding: utf-8 *-*
import sys
from PyQt4 import QtGui, QtCore, uic

class Servidor(QtGui.QMainWindow):

    def __init__(self):
        super (Servidor,self).__init__()
        uic.loadUi("Servidor.ui",self)
        self.ajustaTabla()
        self.show()

    def ajustaTabla(self):
        
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setStretchLastSection(True)
        self.tableWidget.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        self.tableWidget.verticalHeader().setResizeMode(QtGui.QHeaderView.Stretch)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv) 
    servidor = Servidor() 
    sys.exit(app.exec_())     